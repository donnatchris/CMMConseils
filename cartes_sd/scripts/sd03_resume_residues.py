#!/usr/bin/env python3
"""Reprise d'un transfert interrompu : contrôle des présents, sans écrasement.
Les fragments incomplets sont conservés séparément. Ne relit pas les blocs valides.
"""
import hashlib,json
from sd03_collect import OUT
scan=json.loads((OUT/'inventaires/espace-libre.json').read_text());valid=[];bad=[];todo=[]
for rec in scan['nonzero_clusters']:
 p=OUT/'prive/residus'/f"{rec['cluster']}.bin"
 if p.exists():
  b=p.read_bytes()
  if len(b)==scan['geometry']['cluster_bytes'] and hashlib.sha256(b).hexdigest()==rec['sha256']:valid.append(rec['cluster']);continue
  dest=OUT/'prive/residus-incomplets'/p.name;dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists():raise FileExistsError(dest)
  bad.append(dict(cluster=rec['cluster'],size=len(b),sha256=hashlib.sha256(b).hexdigest(),preserved_as=str(dest.relative_to(OUT))));p.rename(dest)
 todo.append(rec)
partial=OUT/'inventaires/residus-classes.json'
if partial.exists():partial.rename(OUT/'inventaires/residus-classes-partiel-non-valide.json')
with (OUT/'inventaires/reprise-residus-etat.json').open('x') as f:json.dump(dict(original_transfer_exitcode=143,verified_existing_count=len(valid),incomplete=bad,remaining=len(todo),reason='Transfert interrompu sans message stderr ; cause non établie. Résultats partiels non utilisés comme inventaire complet.'),f,ensure_ascii=False,indent=2)
new=dict(scan);new['nonzero_clusters']=todo
with (OUT/'inventaires/parametres-residus-reprise.json').open('x') as f:json.dump(dict(scan=new,tar_max_bytes=256*1024**2),f)
print('Valides',len(valid),'incomplets',bad,'restants',len(todo))
