#!/usr/bin/env python3
"""Caractérisation des clusters libres ; association uniquement par comparaisons.
Une grammaire inférée n'attribue pas à elle seule une origine ou une date.
"""
import collections
import hashlib
import json
from sd01_collect import OUT
from sd01_mp4 import inspect

LENGTHS={b'vdts':24,b'sdts':12,b'vdsc':20,b'sdsc':20,b'vdco':8,b'sdco':8,b'vdsz':8,b'sdsz':8,b'vdss':8}
def parse(data,start=0):
    pos=start; records=collections.defaultdict(list);reason='borne'
    while pos<len(data):
        tag=data[pos:pos+4]
        if tag==b'\0'*4 and not any(data[pos:]):reason='remplissage_nul';break
        if tag not in LENGTHS:reason='type_inconnu';break
        length=LENGTHS[tag]
        if pos+length>len(data):reason='enregistrement_coupe';break
        p=data[pos+4:pos+length]
        records[tag.decode()].append([int.from_bytes(p[i:i+4],'big') for i in range(0,len(p),4)])
        pos+=length
    return dict(start=start,parsed_until=pos,reason=reason,record_count=sum(len(v) for v in records.values()),unparsed_nonzero_bytes=sum(x!=0 for x in data[pos:]),records=dict(records))

def tables(data):
    boxes=inspect(data)['boxes'];out={}
    for trak in (b for b in boxes if b['path']=='/moov/trak'):
        children=[b for b in boxes if trak['offset']<b['offset']<trak['offset']+trak['size']]
        handler=next(b for b in children if b['path'].endswith('/hdlr'))
        kind=data[handler['offset']+16:handler['offset']+20].decode()
        out[kind]={}
        for b in children:
            typ=b['path'].rsplit('/',1)[-1];p=data[b['offset']+8:b['offset']+b['size']]
            if typ in ('stco','stss'):
                count=int.from_bytes(p[4:8],'big');v=[int.from_bytes(p[8+i*4:12+i*4],'big') for i in range(count)]
            elif typ=='stsz':
                size=int.from_bytes(p[4:8],'big');count=int.from_bytes(p[8:12],'big')
                v=[size]*count if size else [int.from_bytes(p[12+i*4:16+i*4],'big') for i in range(count)]
            else:continue
            out[kind][typ]=v
    return out

raw=json.loads((OUT/'inventaires/lecture-fat-independante-v2.json').read_text());files={e['start_cluster']:e for e in raw['entries'] if e['path'].endswith('.mp4') and not e['deleted']}
export=json.loads((OUT/'inventaires/export.json').read_text());paths={e['path']:e for e in export['entries'] if e.get('artifact','').endswith('.mp4') and not e['deleted']}
details=[];counts=collections.Counter();moovhashes=collections.Counter();associated=[];cache={}
for p in sorted((OUT/'prive/residus').glob('*.bin'),key=lambda p:int(p.stem)):
    c=int(p.stem);data=p.read_bytes();r=dict(cluster=c,first_24_hex=data[:24].hex())
    if data[4:8]==b'moov' and int.from_bytes(data[:4],'big')==1006:
        r['class']='modele_moov_1006';r['structure_errors']=inspect(data[:1006])['errors'];r['payload_sha256']=hashlib.sha256(data[:1006]).hexdigest();r['nonzero_after_moov']=sum(x!=0 for x in data[1006:]);moovhashes[r['payload_sha256']]+=1
        if c-1 in files:r['adjacent_active_video']=files[c-1]['path']
    else:
        candidates=[parse(data,start) for start in range(0,24,4) if data[start:start+4] in LENGTHS]
        if candidates:
            parsed=max(candidates,key=lambda q:q['parsed_until']-q['start']);r.update({k:v for k,v in parsed.items() if k!='records'});r['record_counts']={k:len(v) for k,v in parsed['records'].items()};r['class']='journal_auxiliaire_depuis_borne' if parsed['start']==0 else 'fragment_journal_auxiliaire'
            if c-2 in files and parsed['start']==0:
                e=files[c-2];filename=e['path']
                if filename not in cache:cache[filename]=tables((OUT/paths[filename]['artifact']).read_bytes())
                tab=cache[filename];comparisons=[]
                for tag,kind,typ in [('vdsz','vide','stsz'),('sdsz','soun','stsz'),('vdco','vide','stco'),('sdco','soun','stco'),('vdss','vide','stss')]:
                    values=[x[0] for x in parsed['records'].get(tag,[])]
                    target=tab[kind].get(typ,[])
                    first_mismatch=next((i for i,(a,b) in enumerate(zip(values,target)) if a!=b),None)
                    common=first_mismatch if first_mismatch is not None else min(len(values),len(target))
                    comparisons.append(dict(token=tag,entries=len(values),final_entries=len(target),prefix_equal=bool(values) and values==target[:len(values)],common_prefix_entries=common,first_mismatch=first_mismatch,temp_mismatch_value=values[first_mismatch] if first_mismatch is not None else None,final_mismatch_value=target[first_mismatch] if first_mismatch is not None else None))
                r['adjacent_active_video']=filename;r['comparisons']=comparisons
                associated.append(dict(cluster=c,path=filename,all_five_prefixes_equal=all(x['prefix_equal'] for x in comparisons),comparisons=comparisons))
        else:r['class']='non_classe'
    counts[r['class']]+=1;details.append(r)
result=dict(method='Classification des clusters, pas reconstruction ; grammaire inférée et comparaisons aux tables actives',counts=dict(counts),moov_template_hashes=dict(moovhashes),moov_with_adjacent_video=sum('adjacent_active_video' in r for r in details if r['class']=='modele_moov_1006'),log_with_adjacent_video=len(associated),log_all_five_prefixes_equal=sum(r['all_five_prefixes_equal'] for r in associated),details=details)
with (OUT/'inventaires/residus-caracterises-v2.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='details'},indent=2))
print('Non classés',[(r['cluster'],r['first_24_hex']) for r in details if r['class']=='non_classe'][:50])
