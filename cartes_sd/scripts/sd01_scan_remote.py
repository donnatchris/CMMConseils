#!/usr/bin/env python3
"""Analyse exhaustive des clusters libres FAT32 sans extraction massive.
Offsets JSON absolus, en octets. Regroupement contigu : jusqu'à 4 Mio/lecture.
Les signatures restent des candidats, pas des fichiers reconstitués.
"""
import array
import hashlib
import json
import re
import struct
import sys
import time

start=time.time()
f=open(sys.argv[1],'rb')
base=8192*512
f.seek(base)
boot=f.read(512)
bps=struct.unpack_from('<H',boot,11)[0]
spc=boot[13]
reserved=struct.unpack_from('<H',boot,14)[0]
nf=boot[16]
fatsectors=struct.unpack_from('<I',boot,36)[0]
total=struct.unpack_from('<I',boot,32)[0]
data=base+(reserved+nf*fatsectors)*bps
cs=bps*spc
n=(total-reserved-nf*fatsectors)//spc
f.seek(base+reserved*bps)
fat=array.array('I',f.read(fatsectors*bps))
if sys.byteorder!='little': fat.byteswap()
runs=[]
for cl in range(2,n+2):
    if fat[cl]&0xfffffff==0:
        if runs and cl==runs[-1][1]+1: runs[-1][1]=cl
        else: runs.append([cl,cl])
sig=[]
nonzero=[]
nonzero_ranges=[]
sha=hashlib.sha256()
freebytes=0
nalcounts={}
zerocl=bytes(cs)
for first,last in runs:
    cl=first
    while cl<=last:
        count=min(256,last-cl+1)
        off=data+(cl-2)*cs
        f.seek(off)
        chunk=f.read(count*cs)
        if len(chunk)!=count*cs: raise IOError('short read')
        sha.update(chunk)
        freebytes+=len(chunk)
        # Un lot exactement nul ne peut contenir aucune signature recherchée.
        # Évite le coût des regex à chaque octet nul, sans échantillonnage.
        if chunk==bytes(len(chunk)):
            cl+=count
            continue
        for i in range(count):
            part=chunk[i*cs:(i+1)*cs]
            if part!=zerocl:
                c=cl+i
                if nonzero_ranges and c==nonzero_ranges[-1][1]+1: nonzero_ranges[-1][1]=c
                else: nonzero_ranges.append([c,c])
                nonzero.append(dict(cluster=c,absolute_offset=off+i*cs,sha256=hashlib.sha256(part).hexdigest(),nonzero_bytes=sum(x!=0 for x in part)))
        # Chercher dans chaque lot avec 64 octets de contexte après la borne.
        f.seek(off+len(chunk))
        view=chunk+f.read(64)
        for m in re.finditer(rb'ftyp|moov|mdat|\x00\x00\x00\x01[\x01-\x7f]|(?:19|20)\d{6}_\d{6}|NTFS    |EXFAT   |mkdosfs',view):
            pos=m.start()
            if pos>=len(chunk): continue
            v=m.group()
            if v.startswith(b'\0'):
                nal=v[-1]&31
                nalcounts[str(nal)]=nalcounts.get(str(nal),0)+1
                continue
            rec=dict(absolute_offset=off+pos,signature=v.decode(errors='replace'),cluster=cl+pos//cs,context_hex=view[max(0,pos-4):pos+32].hex())
            if v in (b'ftyp',b'moov',b'mdat') and pos>=4:
                rec['box_size']=int.from_bytes(view[pos-4:pos],'big')
            sig.append(rec)
        cl+=count
    print('Clusters libres lus : '+str(freebytes//cs),file=sys.stderr,flush=True)
print(json.dumps(dict(geometry=dict(partition_absolute_offset=base,sector_bytes=bps,cluster_bytes=cs,data_absolute_offset=data,total_clusters=n),free_cluster_count=freebytes//cs,free_bytes_read=freebytes,free_stream_sha256=sha.hexdigest(),free_runs=runs,nonzero_cluster_count=len(nonzero),nonzero_ranges=nonzero_ranges,nonzero_clusters=nonzero,signature_candidates=sig,h264_annexb_like_counts=nalcounts,elapsed_seconds=time.time()-start),indent=2))
