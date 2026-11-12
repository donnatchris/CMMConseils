#!/usr/bin/env python3
"""Recoupement local des index dérivés et FAT exportée ; aucune source écrite."""
import array,collections,csv,json,sys
from sd02_collect import OUT
raw=json.loads((OUT/'inventaires/lecture-fat-v2.json').read_text());g=raw['geometry'];fat=array.array('I',(OUT/'structures/fat1.bin').read_bytes())
if sys.byteorder!='little':fat.byteswap()
plan=json.loads((OUT/'inventaires/plan-medias.json').read_text());owners={};index={}
active=[e for e in raw['entries'] if not e['deleted'] and not e['after_end_marker'] and e['name'] not in ('.','..')]
for e in active:
 c=e['start_cluster'];seen=set();i=0
 while 2<=c<g['total_clusters']+2 and c not in seen:
  seen.add(c);owners[c]=e['path'];index[c]=i;i+=1;v=fat[c]&0xfffffff
  if v>=0xffffff8:break
  c=v
rows=[]
for e in plan['entries']:
 if e['deleted']:rows.append(dict(inode=e['inode'],deleted_path=e['path'],deleted_declared_size=e['size'],start_cluster=e['start_cluster'],current_fat_value=e['first_fat_value'],current_owner=owners.get(e['start_cluster']),current_owner_cluster_index=index.get(e['start_cluster'])))
with (OUT/'inventaires/supprimes-reutilisation.csv').open('x',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
focus=[]
for e in raw['entries']:
 if e['path'].endswith(('σ0241013','σ0241014','σ0241015')):
  focus.append(dict(path=e['path'],created=e['created'],written=e['written'],start_cluster=e['start_cluster'],current_owner=owners.get(e['start_cluster']),current_owner_cluster_index=index.get(e['start_cluster'])))
result=dict(deleted_file_count=len(rows),first_cluster_currently_owned=sum(bool(r['current_owner']) for r in rows),first_cluster_now_inside_other_file=sum(bool(r['current_owner']) and r['current_owner_cluster_index']>0 for r in rows),first_cluster_free=sum(not r['current_fat_value'] for r in rows),first_cluster_allocated_without_owner=sum(bool(r['current_fat_value']) and not r['current_owner'] for r in rows),focus_directories=focus)
(OUT/'inventaires/reutilisation-synthese.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2))
