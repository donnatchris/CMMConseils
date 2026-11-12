#!/usr/bin/env python3
"""Mesure du contenu interprétable des auxiliaires libres, sans carving affirmatif."""
import collections,hashlib,json
from sd03_collect import OUT
from sd03_stbl_helpers import parse,LENGTHS
rows=[];counter=collections.Counter()
for p in (OUT/'prive/residus').glob('*.bin'):
 b=p.read_bytes();r=dict(cluster=int(p.stem),size=len(b),sha256=hashlib.sha256(b).hexdigest())
 if b[4:8]==b'moov' and int.from_bytes(b[:4],'big')==1006:
  r.update(kind='modele_moov',nonzero_after_model=sum(x!=0 for x in b[1006:]));counter['modeles']+=1;counter['nonzero_apres_modeles']+=r['nonzero_after_model']
 else:
  candidates=[parse(b,start) for start in range(0,24,4) if b[start:start+4] in LENGTHS]
  if candidates:
   q=max(candidates,key=lambda x:x['parsed_until']-x['start']);r.update(kind='journal',start=q['start'],parsed_until=q['parsed_until'],reason=q['reason'],records=q['record_count'],nonzero_prefix=sum(x!=0 for x in b[:q['start']]),nonzero_suffix=q['unparsed_nonzero_bytes']);counter['journaux']+=1;counter['nonzero_prefixes_journaux']+=r['nonzero_prefix'];counter['nonzero_suffixes_journaux']+=r['nonzero_suffix'];counter['journaux_suffixe_nonzero_sup_24']+=r['nonzero_suffix']>24
  else:r['kind']='non_classe';counter['non_classes']+=1
 rows.append(r)
with (OUT/'inventaires/residus-details.json').open('x') as f:json.dump(dict(summary=dict(counter),rows=sorted(rows,key=lambda r:r['cluster'])),f,ensure_ascii=False,indent=2)
print(dict(counter))
