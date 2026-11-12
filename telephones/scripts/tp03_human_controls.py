#!/usr/bin/env python3
"""Additional negative controls, patterns and plist triage on TP-03 SIFT copies.

Usage GENERAL PRIORITY FIRST_PASS NEW_OUTPUT
"""
import collections
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import sqlite3
import sys
from zoneinfo import ZoneInfo

P = ZoneInfo('Europe/Paris')
C = 978307200
LO = dt.datetime(2024, 10, 16, tzinfo=P).timestamp()
HI = dt.datetime(2024, 10, 17, tzinfo=P).timestamp()


def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()


def main():
    root, priority, first, out = map(Path,sys.argv[1:5]);os.umask(0o077);out.mkdir(parents=True,exist_ok=False)
    d=json.loads((first/'results.json').read_text());result={};sources=[];errors=[]
    def query(r,rel,sql,args=()):
        p=r/'files'/rel;before=sha(p);c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
        try:rows=[dict(x) for x in c.execute(sql,args)]
        finally:c.close()
        after=sha(p);assert before==after;sources.append({'path':str(p),'sql':sql,'args':args,'before':before,'after':after});return rows
    tip='AppDomainGroup-group.com.apple.tipsnext/com.apple.MobileSMS/.tipkit/tips-store.db'
    changes=query(root,tip,'''select c.ZTRANSACTIONID,p.Z_NAME entity_name,c.ZCHANGETYPE,count(*) n
        from ACHANGE c left join Z_PRIMARYKEY p on p.Z_ENT=c.ZENTITY
        group by c.ZTRANSACTIONID,p.Z_NAME,c.ZCHANGETYPE order by c.ZTRANSACTIONID''')
    bytx=collections.defaultdict(collections.Counter)
    for x in changes:bytx[x['ZTRANSACTIONID']][x['entity_name']+':'+str(x['ZCHANGETYPE'])]+=x['n']
    groups=[]
    for x in d['tipkit_transactions']:
        if x['author_name']!='com.apple.MobileSMS_com.apple.tipsnext.shared':continue
        if not groups or x['ZTIMESTAMP']-groups[-1][-1]['ZTIMESTAMP']>2:groups.append([])
        groups[-1].append(x)
    target=collections.Counter()
    for tx in range(1217,1225):target.update(bytx[tx])
    result['target_signature']=dict(target);result['comparable_groups']=[]
    for group in groups:
        signature=collections.Counter()
        for x in group:signature.update(bytx[x['Z_PK']])
        if signature==target:result['comparable_groups'].append({'transactions':[x['Z_PK'] for x in group],'start':group[0]['paris'],'end':group[-1]['paris'],'signature':dict(signature)})
    result['tip_displayed_control']=[{'Z_PK':x['Z_PK'],'ZID':x['ZID'],'ZLASTDISPLAYED':x['ZLASTDISPLAYED']} for x in d['tipkit_tables']['ZCORETIPRECORD'] if x['ZLASTDISPLAYED'] is not None]
    result['target_changes_count']=sum(target.values())
    result['tip_donation_dates']=[{'id':x['Z_PK'],'event':x['ZEVENT'],'paris':dt.datetime.fromtimestamp(x['ZDATE']+C,dt.timezone.utc).astimezone(P).isoformat()} for x in d['tipkit_tables']['ZCOREDONATIONRECORD']]
    hs='HealthDomain/Health/healthdb_secure.sqlite'
    result['health_target_metadata']=query(priority,hs,'''select m.object_id,k.key,m.value_type,
        m.string_value,m.numerical_value,m.date_value,length(m.data_value) data_bytes
        from metadata_values m join metadata_keys k on k.ROWID=m.key_id
        where m.object_id in (348331,348332)''')
    result['health_external_sync']=query(priority,hs,'select object_id,source_id,object_code,version,deleted from external_sync_ids where object_id in (348331,348332)')
    result['health_source_schema']=query(priority,'HealthDomain/Health/healthdb.sqlite',"select sql from sqlite_master where name='sources'")
    # No quantities or medical values exported.
    rel='HomeDomain/Library/CoreDuet/People/interactionC.db'
    result['interaction_ranges']=query(root,rel,'''select count(*) n,min(ZSTARTDATE) first_start,max(ZSTARTDATE) last_start,
        min(ZCREATIONDATE) first_creation,max(ZCREATIONDATE) last_creation,max(ZUPDATEDATE) last_update from ZINTERACTIONS''')
    result['interaction_16']=query(root,rel,'''select Z_PK,ZBUNDLEID,ZDIRECTION,ZSTARTDATE,ZCREATIONDATE,ZUPDATEDATE from ZINTERACTIONS
        where ZSTARTDATE between ? and ? or ZCREATIONDATE between ? and ? or ZUPDATEDATE between ? and ?''',(LO-C,HI-C)*3)
    result['datausage_ranges']={}
    rel='WirelessDomain/Library/Databases/DataUsage.sqlite'
    for table,column in [('ZPROCESS','ZTIMESTAMP'),('ZPROCESS','ZFIRSTTIMESTAMP'),('ZLIVEUSAGE','ZTIMESTAMP'),('ZWIFIDATA','ZTIMESTAMP'),('ZEVENT','ZTIMESTAMP')]:
        result['datausage_ranges'][table+'/'+column]=query(root,rel,'select count(*) n,min('+column+') first,max('+column+') last from '+table)
    rel='AppDomainGroup-group.com.apple.PegasusConfiguration/AlpsWarehouse/data_warehouse.db'
    result['daily_payloads']=query(root,rel,'select timestamp,length(payload) payload_bytes from spotlight_sfm where timestamp between ? and ? order by timestamp',(dt.datetime(2024,10,15,14,19,tzinfo=P).timestamp(),dt.datetime(2024,10,28,11,30,tzinfo=P).timestamp()))
    result['plist_candidates']=[];result['plist_counts']=collections.Counter();plist_sources=[]
    def walk(v,key,source):
        if isinstance(v,dict):
            for k,x in v.items():walk(x,key+'/'+str(k),source)
        elif isinstance(v,list):
            for i,x in enumerate(v):walk(x,key+'/'+str(i),source)
        elif isinstance(v,dt.datetime):
            t=v.replace(tzinfo=dt.timezone.utc).timestamp()
            if LO<=t<HI:result['plist_candidates'].append({'path':source,'key':key,'kind':'plist_datetime','paris':dt.datetime.fromtimestamp(t,dt.timezone.utc).astimezone(P).isoformat()})
        elif isinstance(v,(int,float)) and not isinstance(v,bool):
            for kind,epoch,scale in [('unix_s',0,1),('unix_ms',0,1000),('cocoa_s',C,1),('cocoa_ns',C,1e9)]:
                if (LO-epoch)*scale<=v<(HI-epoch)*scale:
                    result['plist_candidates'].append({'path':source,'key':key,'kind':kind,'raw':v,'paris':dt.datetime.fromtimestamp(v/scale+epoch,dt.timezone.utc).astimezone(P).isoformat()})
        elif isinstance(v,bytes) and v.startswith(b'bplist00'):
            try:walk(plistlib.loads(v),key+'/embedded_plist',source)
            except Exception:result['plist_counts']['embedded_parse_error']+=1
    for p in sorted((root/'files').rglob('*.plist')):
        rel=str(p.relative_to(root/'files'))
        if rel=='KeychainDomain/keychain-backup.plist':continue
        try:
            before=sha(p);walk(plistlib.loads(p.read_bytes()),'',rel);after=sha(p);assert before==after
            plist_sources.append({'path':rel,'before':before,'after':after});result['plist_counts']['parsed']+=1
        except Exception as e:errors.append({'path':rel,'error':str(e)});result['plist_counts']['parse_error']+=1
    # Keychain attributes remain encrypted internally: report only counts/absence of readable dates.
    p=root/'files/KeychainDomain/keychain-backup.plist';k=plistlib.loads(p.read_bytes())
    result['keychain_metadata_limit']={'sha256':sha(p),'classes':{name:{'items':len(items),'readable_cdat_mdat':sum('cdat' in x or 'mdat' in x for x in items)} for name,items in k.items() if isinstance(items,list)}}
    for name,value in [('results',result),('sources',sources),('plist-sources',plist_sources),('errors',errors)]:
        (out/(name+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'comparable_groups':len(result['comparable_groups']),'plist_counts':result['plist_counts'],'plist_candidates':len(result['plist_candidates']),'errors':len(errors)}))


if __name__=='__main__':main()
