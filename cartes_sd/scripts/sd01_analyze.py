#!/usr/bin/env python3
"""Dérivations locales reproductibles ; aucune lecture/écriture des sources."""
import array
import collections
import csv
import datetime as dt
import hashlib
import json
import pathlib
import re
import struct
from sd01_collect import OUT

def dump(name,obj):
    p=OUT/'inventaires'/name
    with p.open('x') as f: json.dump(obj,f,ensure_ascii=False,indent=2)

def table(name,rows,fields=None):
    with (OUT/'inventaires'/name).open('x',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)

def iso(epoch):
    return dt.datetime.fromtimestamp(int(epoch),dt.timezone.utc).replace(tzinfo=None).isoformat(' ') if int(epoch) else ''

def main():
    entries=json.loads((OUT/'inventaires/export.json').read_text())['entries']
    body={}
    for line in (OUT/'inventaires/timeline.body').read_text().splitlines():
        p=line.split('|')
        if len(p)==11: body[p[2]]=p
    inventory=[]
    videos=[]
    for e in entries:
        if 'inode' not in e or e['inode']=='2' or e['type'].lower().startswith('v'): continue
        inode=e['inode']
        stat=(OUT/'journaux/istat'/f'{inode}.txt').read_text()
        def match(pattern):
            m=re.search(pattern,stat)
            return m.group(1) if m else ''
        row=dict(inode=inode,path=e['path'],type=e['type'],allocation='supprime' if e['deleted'] else 'alloue',
                 declared_size=match(r'Size: (\d+)'),extracted_size=e.get('extracted_size',''),sha256=e.get('sha256',''),
                 fat_created=match(r'Created:\s*([^\n]+)'),fat_written=match(r'Written:\s*([^\n]+)'),fat_accessed=match(r'Accessed:\s*([^\n]+)'),
                 artifact=e.get('artifact',''),extraction_returncode=e.get('extraction',{}).get('returncode',''),ffprobe_returncode=e.get('ffprobe',{}).get('returncode',''),decode_returncode=e.get('decode',{}).get('returncode',''),decode_warnings_bytes=e.get('decode',{}).get('warnings_bytes',''))
        if e['path'].endswith('.mp4'):
            m=re.search(r'(\d{8})_(\d{6})_(\d{2})(?:_(\d{4}))?\.mp4$',e['path'])
            row.update(name_start='',name_suffix='',duration='',estimated_end='',gap_from_previous_end='',fat_written_minus_start_seconds='',suffix_minus_duration='',creation_time='',codecs='',width='',height='')
            if m:
                row['name_start']=dt.datetime.strptime(m[1]+m[2],'%Y%m%d%H%M%S').isoformat(' ')
                row['name_suffix']=int(m[4]) if m[4] else ''
            probe=OUT/'journaux/ffprobe'/f'{inode}.json'
            try: meta=json.loads(probe.read_text())
            except (ValueError,FileNotFoundError): meta={}
            fmt=meta.get('format',{})
            row['creation_time']=fmt.get('tags',{}).get('creation_time','')
            streams=meta.get('streams',[])
            row['codecs']=','.join(s.get('codec_name','?') for s in streams)
            for s in streams:
                if s.get('codec_type')=='video': row.update(width=s.get('width',''),height=s.get('height',''))
            if 'duration' in fmt:
                row['duration']=float(fmt['duration'])
                if row['name_start']:
                    start=dt.datetime.fromisoformat(row['name_start'])
                    row['estimated_end']=(start+dt.timedelta(seconds=row['duration'])).isoformat(' ')
                    if row['name_suffix']!='': row['suffix_minus_duration']=round(row['name_suffix']-row['duration'],6)
                    try:
                        written=dt.datetime.strptime(row['fat_written'].split(' (')[0],'%Y-%m-%d %H:%M:%S')
                        row['fat_written_minus_start_seconds']=(written-start).total_seconds()
                    except ValueError: pass
            videos.append(row)
        inventory.append(row)
    active=sorted((v for v in videos if v['allocation']=='alloue' and '/record/' in v['path']),key=lambda v:v['name_start'])
    prev=None
    gaps=[]
    for v in active:
        if prev and prev['estimated_end'] and v['name_start']:
            gap=(dt.datetime.fromisoformat(v['name_start'])-dt.datetime.fromisoformat(prev['estimated_end'])).total_seconds()
            v['gap_from_previous_end']=round(gap,6)
            gaps.append(dict(previous_inode=prev['inode'],next_inode=v['inode'],previous_end=prev['estimated_end'],next_start=v['name_start'],gap_seconds=round(gap,6)))
        prev=v
    fields=list(dict.fromkeys(k for row in inventory for k in row))
    table('inventaire.csv',inventory,fields)
    table('videos.csv',videos,list(dict.fromkeys(k for row in videos for k in row)))
    table('intervalles.csv',gaps)
    day=dt.date.fromisoformat(active[0]['name_start'][:10])
    last=dt.date.fromisoformat(active[-1]['name_start'][:10])
    daily=[]
    while day<=last:
        vs=[v for v in active if v['name_start'].startswith(day.isoformat())]
        daily.append(dict(day=day.isoformat(),videos=len(vs),duration_seconds=round(sum(v['duration'] for v in vs if v['duration']!=''),6),first_start=vs[0]['name_start'] if vs else '',last_start=vs[-1]['name_start'] if vs else '',last_estimated_end=vs[-1]['estimated_end'] if vs else ''))
        day+=dt.timedelta(days=1)
    table('par-jour.csv',daily)
    normalized=[]
    for inode,p in body.items():
        for typ,index in [('acces',7),('ecriture',8),('changement_non_disponible_FAT',9),('creation',10)]:
            if int(p[index]): normalized.append(dict(date_fat_sans_fuseau_certain=iso(p[index]),type=typ,inode=inode,path=p[1],size=p[6]))
    normalized.sort(key=lambda r:(r['date_fat_sans_fuseau_certain'],r['inode'],r['type']))
    table('timeline-normalisee.csv',normalized)
    hashes=collections.defaultdict(list)
    for v in inventory:
        if v['sha256']: hashes[v['sha256']].append(v['inode'])
    summary=dict(entry_count=len(inventory),types=dict(collections.Counter((e['type']+' '+e['allocation']) for e in inventory)),
                 video_count=len(videos),active_record_video_count=len(active),first=active[0]['name_start'],last=active[-1]['name_start'],
                 total_video_duration_seconds=sum(v['duration'] for v in active if v['duration']!=''),
                 creation_time_counts=dict(collections.Counter(v['creation_time'] for v in active)),
                 codecs=dict(collections.Counter(v['codecs'] for v in active)),
                 probe_failures=[v['inode'] for v in videos if v['ffprobe_returncode']!=0],
                 decode_count=sum('decode' in e for e in entries),decode_failures=[e['inode'] for e in entries if e.get('decode',{}).get('returncode',0)!=0],
                 decode_warnings=[e['inode'] for e in entries if e.get('decode',{}).get('warnings_bytes',0)],
                 nonvideos=[v for v in inventory if v['type'].startswith('r') and not v['path'].endswith('.mp4')],
                 duplicates={h:ids for h,ids in hashes.items() if len(ids)>1},
                 temporal_anomalies=[v for v in inventory if re.search(r'\b(?:1999|2000)-',v['fat_created']+' '+v['fat_written'])],
                 max_gaps=sorted(gaps,key=lambda g:g['gap_seconds'],reverse=True)[:20],
                 study_days=[d for d in daily if '2024-10-14'<=d['day']<='2024-10-29'],
                 suffix_duration_range=[min(v['suffix_minus_duration'] for v in active if v['suffix_minus_duration']!=''),max(v['suffix_minus_duration'] for v in active if v['suffix_minus_duration']!='')])
    dump('synthese.json',summary)
    print(json.dumps({k:v for k,v in summary.items() if k not in ('nonvideos','temporal_anomalies','max_gaps')},ensure_ascii=False,indent=2))

if __name__=='__main__': main()
