#!/usr/bin/env python3
"""Classification prudente des clusters libres exportés et empreintés."""
import collections,json
from sd02_collect import OUT
from sd02_stbl_helpers import parse,LENGTHS
count=collections.Counter();items=[]
for f in (OUT/'prive/residus').glob('*.bin'):
 b=f.read_bytes();c=int(f.stem)
 if b[4:8]==b'moov' and int.from_bytes(b[:4],'big')==1006:kind='modele_moov'
 else:
  candidates=[parse(b,start) for start in range(0,24,4) if b[start:start+4] in LENGTHS]
  if candidates:
   r=max(candidates,key=lambda q:q['parsed_until']-q['start']);kind='journal' if r['start']==0 else 'fragment_journal'
  else:kind='autre'
 count[kind]+=1;items.append(dict(cluster=c,classification=kind,first24hex=b[:24].hex()))
with (OUT/'inventaires/residus-classes.json').open('x') as f:json.dump(dict(counts=dict(count),items=sorted(items,key=lambda e:e['cluster'])),f,indent=2)
print(count)
