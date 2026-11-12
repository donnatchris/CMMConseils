#!/usr/bin/env python3
"""Génère les paramètres d'une étape, depuis les seuls index de la campagne.
Refuse l'écrasement. Usage : sd02_parameters.py structures|priorite|residus|
recuperations|complements|finalisation|apercus|fragment-final.
"""
import json,sys
from sd02_collect import OUT
phase=sys.argv[1]
def read(name):return json.loads((OUT/'inventaires'/name).read_text())
if phase=='structures':name='parametres-structures.json';p=dict(raw=read('lecture-fat-v2.json'),tar_max_bytes=128*1024**2)
elif phase=='residus':name='parametres-residus.json';p=dict(scan=read('espace-libre.json'),tar_max_bytes=512*1024**2)
else:
 plan=read('plan-medias.json')
 if phase=='priorite':
  p=dict(plan);p['entries']=[e for e in plan['entries'] if e['inode'] in ['1543','1547','1551','273341448']];p['save_inodes']=[e['inode'] for e in p['entries']];p['decode_inodes']=p['save_inodes'];p['save_max_bytes']=64*1024**2;p['tar_max_bytes']=128*1024**2;name='plan-priorite.json'
 elif phase=='recuperations':
  p=dict(geometry=plan['geometry'],entries=[e for e in plan['entries'] if e['deleted'] and not e['first_fat_value']],classes=read('residus-classes.json')['items'],tar_max_bytes=512*1024**2);name='plan-recuperations.json'
 elif phase=='complements':
  e=next(e for e in plan['entries'] if e['inode']=='1543');p=dict(geometry=plan['geometry'],lost_clusters=read('allocation.json')['allocated_unreferenced_clusters'],temp_start=e['start_cluster'],temp_size=e['size'],istat_inodes=[3,1035,1072,1073,1074,1075,1543,1547,1551,273341448,575101256,517729284],tar_max_bytes=32*1024**2);name='plan-complements.json'
 elif phase in ['supplement','ecarts']:
  p=dict(plan)
  if phase=='supplement':es=[min([e for e in plan['entries'] if not e['deleted'] and '/record/20241112/' in e['path']],key=lambda e:e['path'].rsplit('/',1)[-1])]
  else:es=[e for e in plan['entries'] if e['inode'] in ['657582352','657582356']]
  p.update(entries=es,save_inodes=[e['inode'] for e in es],decode_inodes=[e['inode'] for e in es],save_max_bytes=64*1024**2,tar_max_bytes=128*1024**2);name='plan-'+phase+'.json'
 elif phase=='finalisation':p=read('plan-priorite.json');p['tar_max_bytes']=32*1024**2;name='plan-finalisation.json'
 elif phase=='apercus':
  es=[e for e in plan['entries'] if e['inode'] in ['1543','1547','1551','273341448']];finals=sorted([e for e in plan['entries'] if not e['deleted'] and '/record/202411' in e['path']],key=lambda e:e['path']);es +=[finals[0],finals[-1]];rs=read('recuperations.json')['entries'];p=dict(geometry=plan['geometry'],entries=es,recuperations=[rs[0],rs[-1]],tar_max_bytes=32*1024**2);name='plan-apercus.json'
 elif phase=='fragment-final':
  p=read('plan-finalisation.json');e=next(e for e in plan['entries'] if e['inode']=='575101252');bound=min(x['start_cluster'] for x in plan['entries'] if x['deleted'] and not x['first_fat_value']);p['previous_entry']=e;p['tail_clusters']=[x['cluster'] for x in read('residus-classes.json')['items'] if e['start_cluster']<=x['cluster']<bound and x['classification']=='autre'];p['tar_max_bytes']=32*1024**2;name='plan-fragment-final.json'
 else:raise ValueError(phase)
with (OUT/'inventaires'/name).open('x') as f:json.dump(p,f)
print(name)
