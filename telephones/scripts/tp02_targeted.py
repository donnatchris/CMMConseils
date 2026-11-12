#!/usr/bin/env python3
"""Targeted chronological evidence, with raw fields, conservative interpretations.
No message text, contact numbers, device tokens or credentials are exported.
"""
import argparse
import collections
import datetime as dt
import json
import os
from pathlib import Path
import plistlib
import re
import sqlite3
import tp02_forensic as common

WEBKIT='https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/Classifier/ResourceLoadStatisticsStore.h'
APPLE='https://developer.apple.com/documentation/foundation/date/timeintervalsincereferencedate-swift.property'
CALL='https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/callHistory.py'


def walk(obj, pointer='$', depth=0):
    if depth>40:return
    if isinstance(obj,dict):
        for k,v in obj.items():
            yield from walk(v,pointer+'/'+str(k),depth+1)
    elif isinstance(obj,(list,tuple)):
        for i,v in enumerate(obj):yield from walk(v,pointer+'/'+str(i),depth+1)
    else:yield pointer,obj


def main():
    os.umask(0o077)
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--extracted',action='append',required=True);p.add_argument('--out',required=True)
    a=p.parse_args();out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
    events=[];file_stats=[];devices=[];errors=[]
    def add(path,ref,raw,fmt,date,observation,interpretation,context=None,confidence='format_hypothesis',interval_end=None):
        if interval_end:
            if interval_end<=common.EXTSTART or date>=common.EXTEND:return
        elif not common.EXTSTART<=date<common.EXTEND:return
        record=origins.get(path.resolve(),{})
        events.append({'domain':record.get('domain',''),'relativePath':record.get('relativePath',''),
            'fileID':record.get('fileID',''),'sha256':record.get('sha256',''),'file':str(path),'locator':ref,
            'raw_value':json.dumps(raw,ensure_ascii=False,default=str),'time_format':fmt,
            'utc':date.isoformat(),'paris':date.astimezone(common.PARIS).isoformat(),
            'interval_end_utc':interval_end.isoformat() if interval_end else '',
            'central_window':'day_overlap_no_hour' if interval_end and date<=common.END and interval_end>common.START else
                             'True' if common.START<=date<=common.END else 'False',
            'observation':observation,'interpretation':interpretation,'confidence':confidence,
            'context':json.dumps(context or {},ensure_ascii=False)})
    origins={}
    for root in map(Path,a.extracted):
        for line in (root/'extraction.jsonl').read_text().splitlines():
            r=json.loads(line)
            if r.get('status')=='ok':origins[Path(r['output']).resolve()]=r
    for path,record in origins.items():
        with path.open('rb') as f:sig=f.read(16)
        stat={'file':str(path),'fileID':record['fileID'],'bytes':path.stat().st_size,'format':'unknown','parsed':False}
        file_stats.append(stat)
        if sig==b'SQLite format 3\x00':
            stat['format']='sqlite'
            try:
                with common.ro(path) as c:
                    tables={r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table'")}
                    if 'OperatingDates' in tables:
                        stat['parsed']=True
                        for rowid,y,m,d in c.execute('SELECT rowid,year,month,monthDay FROM OperatingDates'):
                            try: date=dt.datetime(y,m+1,d,tzinfo=dt.timezone.utc)
                            except ValueError:continue
                            add(path,f'OperatingDates.rowid={rowid}',{'year':y,'month':m,'monthDay':d},
                                'WebKit year/month(0..11)/day; UTC calendar day; no event hour',date,
                                'OperatingDate row retained','automatic statistics-store date; not camera viewing or human-use proof',
                                {'reference':WEBKIT,'build_limit':'current upstream format reference, device build not audited'},
                                'format_supported_by_upstream',date+dt.timedelta(days=1))
                    if 'ZCALLRECORD' in tables:
                        stat['parsed']=True
                        cols='Z_PK,ZDATE,ZDURATION,ZORIGINATED,ZANSWERED,ZCALLTYPE,ZSERVICE_PROVIDER'
                        for pk,raw,duration,originated,answered,calltype,provider in c.execute('SELECT '+cols+' FROM ZCALLRECORD'):
                            date=dt.datetime.fromtimestamp(raw+978307200,dt.timezone.utc)
                            add(path,f'ZCALLRECORD.Z_PK={pk}.ZDATE',raw,'Apple/Cocoa seconds since 2001-01-01 UTC',date,
                                'call-history record','call recorded in retained history; local device origin not established',
                                {'duration_raw':duration,'ZORIGINATED_raw':originated,'ZANSWERED_raw':answered,
                                 'ZCALLTYPE_raw':calltype,'service_provider':provider,'format_reference':CALL},'format_supported_by_parser')
                    if 'message' in tables and 'sms.db' in path.name:
                        stat['parsed']=True
                        for row in c.execute('SELECT rowid,date,date_read,date_delivered,is_from_me,service,is_read,is_sent,is_delivered FROM message'):
                            pk,*values=row
                            for index,field in enumerate(('date','date_read','date_delivered')):
                                raw=values[index]
                                if not isinstance(raw,int) or raw==0:continue
                                sec,ns=divmod(raw,10**9)
                                date=dt.datetime.fromtimestamp(sec+978307200,dt.timezone.utc)+dt.timedelta(microseconds=ns//1000)
                                add(path,f'message.rowid={pk}.{field}',raw,'Apple/Cocoa integer nanoseconds; converted to microseconds, raw preserved',date,
                                    'message temporal field '+field,'receipt/read state can be synchronized; no human or local-device attribution',
                                    dict(zip(('is_from_me_raw','service','is_read_raw','is_sent_raw','is_delivered_raw'),values[3:])),
                                    'format_hypothesis_consistent_with_retained_dates')
                    if 'ZDEVICE' in tables:
                        for pk,model,lastonline in c.execute('SELECT Z_PK,ZMODEL,ZLASTONLINE FROM ZDEVICE'):
                            devices.append({'file':str(path),'locator':f'ZDEVICE.Z_PK={pk}','model':model,'lastonline_raw':lastonline,'interpretation':'device configuration snapshot; not historical camera access'})
                    if 'device' in tables and 'mihome' in record['domain']:
                        for rowid,model in c.execute('SELECT rowid,model FROM device'):
                            devices.append({'file':str(path),'locator':f'device.rowid={rowid}','model':model,'lastonline_raw':'','interpretation':'device configuration snapshot; not historical camera access'})
            except sqlite3.Error as e:errors.append({'file':str(path),'error_class':type(e).__name__})
            continue
        if path.stat().st_size>32*1024**2:
            stat['format']='size_limit_not_parsed';continue
        obj=None
        if sig.startswith(b'bplist00') or sig.startswith(b'<?xml'):
            try:obj=plistlib.loads(path.read_bytes());stat['format']='plist';stat['parsed']=True
            except Exception as e:errors.append({'file':str(path),'error_class':type(e).__name__})
        elif sig.lstrip().startswith((b'{',b'[')):
            try:obj=json.loads(path.read_text());stat['format']='json';stat['parsed']=True
            except (ValueError,UnicodeError):
                try:obj=json.loads(path.read_text().splitlines()[0]);stat['format']='json_header';stat['parsed']=True
                except (ValueError,UnicodeError,IndexError):pass
        if obj is not None:
            for pointer,value in walk(obj):
                if isinstance(value,dt.datetime):
                    date=value.replace(tzinfo=dt.timezone.utc) if value.tzinfo is None else value.astimezone(dt.timezone.utc)
                    add(path,pointer,str(value),'serialized plist date interpreted as UTC',date,'serialized date field',
                        'configuration/cache/diagnostic date; meaning and provenance require validation')
                elif re.search(r'time|date|created|modified|lastseen|lastonline',pointer.split('/')[-1],re.I):
                    for fmt,date in common.times(value):
                        add(path,pointer,value,fmt,date,'temporal scalar in structured file',
                            'format candidate; automatic activity or synchronization possible')
        elif path.suffix.lower() in ('.log','.txt','.ips'):
            try:
                text=path.read_text(errors='strict')
                stat['format']='text_log';stat['parsed']=True
                # Only the timestamp substring is exported; never the message content.
                for line_number,line in enumerate(text.splitlines(),1):
                    match=re.search(r'\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?: ?(?:Z|[+-]\d{2}:?\d{2}))?',line)
                    if match:
                        raw=match.group(0)
                        for fmt,date in common.times(raw):add(path,f'line={line_number}',raw,fmt,date,'log timestamp',
                            'log record; message not interpreted; no human attribution')
            except UnicodeError:pass
    fields=['domain','relativePath','fileID','sha256','file','locator','raw_value','time_format','utc','paris','interval_end_utc','central_window','observation','interpretation','confidence','context']
    common.write_csv(out/'chronology-evidence.csv',sorted(events,key=lambda r:r['utc']),fields)
    common.write_csv(out/'structured-file-inventory.csv',file_stats,['file','fileID','bytes','format','parsed'])
    common.write_csv(out/'xiaomi-models.csv',devices,['file','locator','model','lastonline_raw','interpretation'])
    status={'events_or_date_fields':len(events),'central_exact_time':sum(r['central_window']=='True' for r in events),
            'day_overlap_no_hour':sum(r['central_window']=='day_overlap_no_hour' for r in events),
            'formats':dict(collections.Counter(r['format'] for r in file_stats)),'errors':errors,
            'references':{'apple_epoch':APPLE,'webkit_month_zero_based':WEBKIT,'call_parser':CALL},
            'limits':['Records are observations, not attribution of local human use',
                      'Call and message histories may have been synchronized or restored from another device',
                      'SQLite targeted reads immutable; no WAL replay here; main analyzer works on disposable WAL copies',
                      'Unknown application formats and encrypted/compressed payloads not decoded',
                      '32 MiB limit for structured/text file parsing; no naive log timezone assumptions',
                      'Snapshots do not date original creation of records on TP-02']}
    (out/'status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in status.items() if k not in ('errors','references','limits')}))
if __name__=='__main__':main()
