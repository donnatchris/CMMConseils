#!/usr/bin/env python3
"""Jointure TSK/FAT, inventaire horodaté et plan d'analyse/extraction borné.
À lancer après contrôles d'intégrité et inventaire. N'écrit aucune source.
"""
import collections
import csv
import json
import re
from sd02_collect import OUT

raw=json.loads((OUT/'inventaires/lecture-fat-v2.json').read_text())
g=raw['geometry'];root=g['data_absolute_offset']
fls={}
for line in (OUT/'inventaires/fls.txt').read_text().splitlines():
    m=re.match(r'(\S+)\s+(\*\s+)?(\d+):\s+(.*)',line)
    if m:
        typ,deleted,inode,path=m.groups()
        if not typ.lower().startswith('v'):fls[inode]=dict(type=typ,deleted=bool(deleted),path=path)
# Les entrées virtuelles OrphanFiles sont des slots résiduels, pas un chemin réel.
import datetime as dt, struct
orphan=json.loads((OUT/'inventaires/orphelins-slots.json').read_text())
blob=bytes.fromhex(orphan['hex']);fatblob=(OUT/'structures/fat1.bin').read_bytes()
def stamp(date,time=0,tenth=0):
    if not date:return None
    try:return (dt.datetime(1980+(date>>9),(date>>5)&15,date&31,time>>11,(time>>5)&63,(time&31)*2)+dt.timedelta(milliseconds=tenth*10)).isoformat(' ')
    except ValueError:return 'INVALID'
u16=lambda b,o:struct.unpack_from('<H',b,o)[0]
u32=lambda b,o:struct.unpack_from('<I',b,o)[0]
known={3+(e['absolute_entry_offset']-root)//32 for e in raw['entries']}
for inode,rec in fls.items():
    if int(inode) in known or not rec['path'].startswith('$OrphanFiles/'):continue
    absolute=root+(int(inode)-3)*32;offset=absolute-orphan['absolute_offset']
    if not 0<=offset<=len(blob)-32:raise ValueError('Slot orphelin hors lecture')
    b=blob[offset:offset+32];cl=(u16(b,20)<<16)|u16(b,26)
    if b[0]!=229 or b[11]!=32:raise ValueError('Slot orphelin non validé')
    raw['entries'].append(dict(path=rec['path'],name=rec['path'].split('/')[-1],short_name=rec['path'].split('/')[-1],absolute_entry_offset=absolute,deleted=True,after_end_marker=False,deleted_parent=True,attributes=b[11],start_cluster=cl,first_fat_value=u32(fatblob,cl*4)&0xfffffff,size=u32(b,28),created=stamp(u16(b,16),u16(b,14),b[13]),written=stamp(u16(b,24),u16(b,22)),accessed=stamp(u16(b,18)),raw_hex=b.hex(),orphan_slot=True))
rows=[];errors=[]
for e in raw['entries']:
    if e['name'] in ('.','..') or e['after_end_marker']:continue
    inode=str(3+(e['absolute_entry_offset']-root)//32)
    f=fls.get(inode)
    if not f:
        errors.append(dict(inode=inode,path=e['path'],error='absent de fls'))
        continue
    row=dict(inode=inode,path=f['path'],raw_path=e['path'],type=f['type'],deleted=e['deleted'],deleted_parent=e['deleted_parent'],size=e['size'],start_cluster=e['start_cluster'],first_fat_value=e['first_fat_value'],created=e['created'],written=e['written'],accessed=e['accessed'],absolute_entry_offset=e['absolute_entry_offset'],raw_hex=e['raw_hex'])
    if f['deleted']!=e['deleted']:errors.append(dict(inode=inode,error='état différent'))
    rows.append(row)
found={r['inode'] for r in rows}
errors.extend(dict(inode=i,path=e['path'],error='absent lecture FAT') for i,e in fls.items() if i not in found)
with (OUT/'inventaires/inventaire.csv').open('x',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
files=[e for e in rows if e['type'].endswith('/r')]
videos=[e for e in files if not e['deleted'] and e['path'].lower().endswith('.mp4')]
anomalous=[e for e in raw['entries'] if any(str(e.get(k,'')).startswith(('1999-','2000-')) for k in ('created','written','accessed'))]
days=collections.defaultdict(list)
for e in videos:
    m=re.search(r'(\d{8})_(\d{6})_',e['path'])
    if m:days[m[1]].append(e)
decode=set()
for e in videos:
    if '/20241015/' in e['path'] or any(str(e.get(k,'')).startswith(('1999-','2000-')) for k in ('created','written')):decode.add(e['inode'])
# Témoins premier/dernier de chaque jour, pour caractériser le fonctionnement.
for day,items in days.items():
    ordered=sorted(items,key=lambda e:e['path'])
    decode.update((ordered[0]['inode'],ordered[-1]['inode']))
priorities=[]
focus=set()
day15=sorted(days.get('20241015',[]),key=lambda e:e['path'])
if day15:
    focus.update((day15[0]['inode'],day15[-1]['inode']))
    focus.add(min(day15,key=lambda e:abs(int(re.search(r'20241015_(\d{6})',e['path'])[1])-133000))['inode'])
for e in files:
    score=100
    if e['deleted'] and e['first_fat_value']==0:score=0
    elif any(str(e.get(k,'')).startswith(('1999-','2000-')) for k in ('created','written')):score=1
    elif not e['path'].endswith('.mp4') or '20242010' in e['path']:score=2
    elif e['inode'] in focus:score=3
    elif '/20241015/' in e['path']:score=4
    elif e['inode'] in decode:score=5
    if score<100:priorities.append((score,e))
# Conservation sélective, pas de duplication intégrale des 31,9 Go.
limit=1024**3;save=[];saved_size=0
for score,e in sorted(priorities,key=lambda p:(p[0],p[1]['path'])):
    if e['size']<=256*1024**2 and saved_size+e['size']<=limit:
        save.append(e['inode']);saved_size+=e['size']
plan=dict(geometry=g,entries=files,save_inodes=save,decode_inodes=sorted(decode),save_max_bytes=limit,tar_max_bytes=2*1024**3,selection_rule='Conservation : supprimés, dates 1999/2000 création/écriture, non-vidéos, témoins ; décodage : toutes vidéos du 15, dates aberrantes, premier/dernier par jour et anomalies structurelles détectées en cours. Tous les fichiers vidéo reçoivent un examen des tables, FFprobe et les temps des paquets.')
with (OUT/'inventaires/plan-medias.json').open('x') as f:json.dump(plan,f,ensure_ascii=False,indent=2)
summary=dict(tsk_real_entries=len(fls),raw_rows=len(rows),join_errors=errors,types=dict(collections.Counter(e['type']+(' supprimé' if e['deleted'] else ' alloué') for e in rows)),allocated_video_count=len(videos),regular_declared_bytes=sum(e['size'] for e in files),video_declared_bytes=sum(e['size'] for e in videos),maximum_file_size=max(e['size'] for e in files),deleted_entries=[e for e in rows if e['deleted']],fat_1999_2000_entries=anomalous,day_counts={d:len(v) for d,v in sorted(days.items())},save_declared_bytes=saved_size,save_files=len(save),decode_requested=len(decode),rejected_directories=raw.get('rejected_directories',[]))
with (OUT/'inventaires/etat-inventaire.json').open('x') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in summary.items() if k not in ('deleted_entries','fat_1999_2000_entries','day_counts')},ensure_ascii=False,indent=2))
if errors:raise SystemExit('Écarts FAT/TSK à examiner avant analyse')
