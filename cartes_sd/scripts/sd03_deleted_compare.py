#!/usr/bin/env python3
"""Comparaisons des dérivés extraits dans SIFT ; ne relit ni ne modifie la source."""
import hashlib,json
from sd03_collect import OUT
from sd03_stbl_helpers import parse,tables
idx=json.loads((OUT/'inventaires/priorite-index.json').read_text());rs=idx['entries'];deleted=[r for r in rs if r['deleted']];pairs=[]
for d in deleted:
 if not d['path'].endswith('.mp4'):continue
 stem=d['path'].rsplit('/',1)[-1][:-4];finals=[r for r in rs if not r['deleted'] and r['path'].rsplit('/',1)[-1].startswith(stem+'_') and r['path'].endswith('.mp4')]
 for f in finals:
  a=(OUT/d['artifact']).read_bytes();b=(OUT/f['artifact']).read_bytes();p=dict(deleted_inode=d['inode'],deleted_path=d['path'],deleted_declared_size=d['size'],deleted_read_bytes=len(a),final_inode=f['inode'],final_path=f['path'],final_size=len(b),same_start_cluster=d['start_cluster']==f['start_cluster'],compared_prefix_bytes=min(len(a),len(b)),prefix_equal=a==b[:len(a)],prefix_sha256=hashlib.sha256(a).hexdigest(),final_sha256=hashlib.sha256(b).hexdigest(),limitation='Les deux entrées pointent sur le même premier cluster actuel : le préfixe est une concordance de récupération et ne prouve pas que son contenu soit inchangé depuis la suppression.')
  aux=next((r for r in deleted if r['path']==d['path']+'.stbl'),None)
  if aux:
   q=parse((OUT/aux['artifact']).read_bytes());tab=tables(b);comparisons=[]
   for tag,kind,typ in [('vdsz','vide','stsz'),('sdsz','soun','stsz'),('vdco','vide','stco'),('sdco','soun','stco'),('vdss','vide','stss')]:
    values=[v[0] for v in q['records'].get(tag,[])];target=tab[kind].get(typ,[]);wrong=next((i for i,(x,y) in enumerate(zip(values,target)) if x!=y),None)
    comparisons.append(dict(token=tag,temp_count=len(values),final_count=len(target),prefix_equal=values==target[:len(values)],first_mismatch=wrong))
   p['auxiliary_stbl']=dict(inode=aux['inode'],bytes=aux['read_size'],parse_summary={k:v for k,v in q.items() if k!='records'},comparisons=comparisons)
  pairs.append(p)
result=dict(deleted_entries=deleted,pairs=pairs,interpretation='Concordance entre temporaires supprimés et fichier final présent ; processus de finalisation/nettoyage fortement étayé, sans journal d’exécution ni preuve d’intention individuelle.')
with (OUT/'inventaires/comparaison-temporaires.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(pairs,ensure_ascii=False,indent=2))
