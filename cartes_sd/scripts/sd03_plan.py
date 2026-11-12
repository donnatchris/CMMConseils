#!/usr/bin/env python3
"""Inventaire SD-03 indépendant, jointure TSK/FAT, sélection bornée et explicite."""
import collections,csv,datetime as dt,json,re
from sd03_collect import OUT
raw=json.loads((OUT/'inventaires/lecture-fat.json').read_text());g=raw['geometry'];root=g['data_absolute_offset'];fls={}
for line in (OUT/'inventaires/fls.txt').read_text().splitlines():
 m=re.match(r'(\S+)\s+(\*\s+)?(\d+):\s+(.*)',line)
 if m:
  typ,deleted,inode,path=m.groups()
  if not typ.lower().startswith('v'):fls[inode]=dict(type=typ,deleted=bool(deleted),path=path)
extra=OUT/'inventaires/orphelins-slots.json'
if extra.exists():raw['entries'].extend(json.loads(extra.read_text())['entries'])
rows=[];errors=[]
for e in raw['entries']:
 if e['name'] in ('.','..') or e['after_end_marker']:continue
 inode=str(3+(e['absolute_entry_offset']-root)//32);f=fls.get(inode)
 if not f:errors.append(dict(inode=inode,path=e['path'],error='absent de fls'));continue
 row=dict(inode=inode,path=f['path'],raw_path=e['path'],type=f['type'],deleted=e['deleted'],deleted_parent=e['deleted_parent'],size=e['size'],start_cluster=e['start_cluster'],first_fat_value=e['first_fat_value'],created=e['created'],written=e['written'],accessed=e['accessed'],absolute_entry_offset=e['absolute_entry_offset'],raw_hex=e['raw_hex'])
 if f['deleted']!=e['deleted']:errors.append(dict(inode=inode,path=f['path'],error='allocation différente'))
 rows.append(row)
found={r['inode'] for r in rows};errors.extend(dict(inode=i,path=e['path'],error='absent lecture FAT') for i,e in fls.items() if i not in found)
if not rows:raise ValueError('Aucune entrée vérifiée')
with (OUT/'inventaires/inventaire.csv').open('x',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
files=[e for e in rows if e['type'].endswith('/r')];videos=[e for e in files if not e['deleted'] and e['path'].lower().endswith('.mp4')]
anomalous=[e for e in raw['entries'] if any(str(e.get(k,'')).startswith(('1999-','2000-')) for k in ('created','written','accessed'))];anomalous_dirs=[e['path'] for e in anomalous if e['attributes']&16 and e['name'] not in ('.','..')]
days=collections.defaultdict(list);invalid=[];decode=set();focus=set()
for e in videos:
 m=re.search(r'(\d{8})_(\d{6})_10(?:_(\d+))?\.mp4$',e['path'],re.I)
 if m:
  try:dt.datetime.strptime(m[1]+m[2],'%Y%m%d%H%M%S')
  except ValueError:invalid.append(e['inode'])
  if '/record/' in e['path']:days[m[1]].append(e)
 if '/20241015/' in e['path'] or '/20241028/' in e['path'] or '/.record_tmp/' in e['path'] or e['inode'] in invalid or any(e['path'].startswith(d+'/') for d in anomalous_dirs) or any(str(e.get(k,'')).startswith(('1999-','2000-')) for k in ('created','written')):decode.add(e['inode'])
for day,items in days.items():
 ordered=sorted(items,key=lambda e:e['path'].rsplit('/',1)[-1]);decode.update((ordered[0]['inode'],ordered[-1]['inode']));focus.update((ordered[0]['inode'],ordered[-1]['inode']))
priorities=[]
for e in files:
 score=100
 if e['deleted'] and not e['first_fat_value']:score=0
 elif any(str(e.get(k,'')).startswith(('1999-','2000-')) for k in ('created','written')) or e['inode'] in invalid:score=1
 elif any(e['path'].startswith(d+'/') for d in anomalous_dirs):score=3
 elif '/.record_tmp/' in e['path'] or not e['path'].lower().endswith('.mp4'):score=2
 elif e['inode'] in focus and '/20241015/' in e['path']:score=3
 elif '/20241015/' in e['path']:score=4
 elif e['inode'] in focus:score=5
 if score<100:priorities.append((score,e))
limit=2*1024**3;save=[];saved_size=0
for score,e in sorted(priorities,key=lambda p:(p[0],p[1]['path'])):
 if e['size']<=256*1024**2 and saved_size+e['size']<=limit:save.append(e['inode']);saved_size+=e['size']
plan=dict(geometry=g,entries=files,save_inodes=save,decode_inodes=sorted(decode),save_max_bytes=limit,tar_max_bytes=3*1024**3,selection_rule='Tous fichiers : lecture/empreinte ; tous MP4 : structure, FFprobe, temps des paquets. Décodage intégral : 15/28 octobre, fichiers temporaires, dates 1999/2000 ou dossiers associés, noms impossibles, premier/dernier finalisés par jour, anomalies structurelles. Conservation plafonnée à 2 Gio : supprimés au premier cluster libre, anomalies, temporaires/non-vidéos, 15 octobre et témoins.')
with (OUT/'inventaires/plan-medias.json').open('x') as f:json.dump(plan,f,ensure_ascii=False,indent=2)
summary=dict(tsk_real_entries=len(fls),raw_rows=len(rows),join_errors=errors,types=dict(collections.Counter(e['type']+(' supprimé' if e['deleted'] else ' alloué') for e in rows)),allocated_video_count=len(videos),regular_declared_bytes=sum(e['size'] for e in files),video_declared_bytes=sum(e['size'] for e in videos),maximum_file_size=max((e['size'] for e in files),default=0),deleted_entries=[e for e in rows if e['deleted']],fat_1999_2000_entries=anomalous,invalid_date_inodes=invalid,day_counts={d:len(v) for d,v in sorted(days.items())},save_declared_bytes=saved_size,save_files=len(save),decode_requested=len(decode),rejected_directories=raw.get('rejected_directories',[]))
with (OUT/'inventaires/etat-inventaire.json').open('x') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in summary.items() if k not in ('deleted_entries','fat_1999_2000_entries','day_counts','rejected_directories')},ensure_ascii=False,indent=2))
if errors:raise SystemExit('Écarts FAT/TSK à examiner avant analyse')
