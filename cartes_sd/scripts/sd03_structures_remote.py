#!/usr/bin/env python3
"""Conservation limitée des structures brutes et des répertoires, par stdout."""
import hashlib
import io
import json
import sys
import tarfile

raw=PARAMS['raw'];g=raw['geometry'];f=open(sys.argv[1],'rb');cs=g['cluster_bytes'];base=g['partition_offset_bytes'];bps=g['bytes_per_sector'];fatbytes=g['fat_sectors']*bps
records=[]
def read(off,n):
    f.seek(off);b=f.read(n)
    if len(b)!=n:raise IOError('Lecture courte')
    return b
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
    def add(name,b,description):
        t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
        records.append(dict(artifact=name,size=len(b),sha256=hashlib.sha256(b).hexdigest(),source=description))
    regions=[('mbr-et-avant-partition',0,base),('reserve-fat32',base,g['reserved_sectors']*bps),('fat1',base+g['reserved_sectors']*bps,fatbytes),('fat2',base+(g['reserved_sectors']+g['fat_sectors'])*bps,fatbytes)]
    tail=g['data_absolute_offset']+g['total_clusters']*cs;end=base+g['total_sectors']*bps
    if tail<end:regions.append(('fin-partition',tail,end-tail))
    for name,off,size in regions:add('structures/'+name+'.bin',read(off,size),dict(absolute_offset=off,length=size))
    total=0
    for d in raw['directories']:
        total+=d['size']
        if total>64*1024**2:raise ValueError('Répertoires au-delà de 64 Mio')
        b=b''.join(read(g['data_absolute_offset']+(c-2)*cs,cs) for c in d['clusters'])
        if hashlib.sha256(b).hexdigest()!=d['sha256']:raise ValueError('Répertoire changé')
        add('prive/repertoires/'+str(d['start_cluster'])+'.bin',b,d)
    add('inventaires/structures-index.json',json.dumps(records,ensure_ascii=False,indent=2).encode(),dict(type='index des structures exportées'))
