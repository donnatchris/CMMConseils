#!/usr/bin/env python3
"""Caractérisation des clusters libres ; association uniquement par comparaisons.
Une grammaire inférée n'attribue pas à elle seule une origine ou une date.
"""
import collections
import hashlib
import json

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
