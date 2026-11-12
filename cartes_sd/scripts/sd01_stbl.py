#!/usr/bin/env python3
"""Test explicite du journal .stbl ; grammaire inférée, validée par correspondance.
Ne produit pas de vidéo ni de table modifiée. Échec si un token est inconnu.
"""
import collections
import json
from sd01_collect import OUT
from sd01_mp4 import inspect

stbl=next((OUT/'prive/cibles').glob('1551_*.stbl')).read_bytes()
final=next((OUT/'prive/cibles').glob('76861460_*.mp4')).read_bytes()
sizes={b'vdts':24,b'sdts':12,b'vdsc':20,b'sdsc':20,b'vdco':8,b'sdco':8,b'vdsz':8,b'sdsz':8,b'vdss':8}
records=collections.defaultdict(list);pos=0
while pos<len(stbl):
    tag=stbl[pos:pos+4]
    if tag not in sizes:raise ValueError((pos,tag))
    size=sizes[tag]
    payload=stbl[pos+4:pos+size]
    if len(payload)!=size-4:raise ValueError('truncated record')
    records[tag.decode()].append([int.from_bytes(payload[i:i+4],'big') for i in range(0,len(payload),4)])
    pos+=size
boxes=inspect(final)['boxes'];tables={}
for trak in [b for b in boxes if b['path']=='/moov/trak']:
    children=[b for b in boxes if trak['offset']<b['offset']<trak['offset']+trak['size']]
    handler=next(b for b in children if b['path'].endswith('/hdlr'))
    kind=final[handler['offset']+16:handler['offset']+20].decode()
    tables[kind]={}
    for b in children:
        typ=b['path'].rsplit('/',1)[-1];off=b['offset'];payload=final[off+8:off+b['size']]
        if typ in ('stco','stss'):
            count=int.from_bytes(payload[4:8],'big'); vals=[int.from_bytes(payload[8+4*i:12+4*i],'big') for i in range(count)]
        elif typ=='stsz':
            uniform=int.from_bytes(payload[4:8],'big');count=int.from_bytes(payload[8:12],'big')
            vals=[uniform]*count if uniform else [int.from_bytes(payload[12+4*i:16+4*i],'big') for i in range(count)]
        else:continue
        tables[kind][typ]=vals
comparisons=[]
for tag,kind,typ in [('vdsz','vide','stsz'),('sdsz','soun','stsz'),('vdco','vide','stco'),('sdco','soun','stco'),('vdss','vide','stss')]:
    values=[r[0] for r in records[tag]];target=tables[kind][typ]
    comparisons.append(dict(token=tag,table=kind+'/'+typ,temp_entries=len(values),final_entries=len(target),prefix_equal=values==target[:len(values)],first_mismatch=next((i for i,(a,b) in enumerate(zip(values,target)) if a!=b),None)))
out=dict(method='Grammaire de tokens inférée de .stbl ; comparaison sans transformation avec les tables MP4 finalisées',bytes_consumed=pos,file_size=len(stbl),record_counts={k:len(v) for k,v in records.items()},comparisons=comparisons,records=records)
with (OUT/'inventaires/comparaison-stbl.json').open('x') as f:json.dump(out,f,indent=2)
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
