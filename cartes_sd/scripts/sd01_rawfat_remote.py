#!/usr/bin/env python3
"""Contre-lecture indépendante des BPB, FAT et slots de répertoires FAT32.
Pas de dépendance externe. Lecture rb. Les slots après 00 sont conservés comme
slack et ne sont pas assimilés à des entrées logiques actives.
"""
import array
import datetime
import hashlib
import json
import struct
import sys

f=open(sys.argv[1],'rb')
base=8192*512
def read(off,n):
    f.seek(off)
    b=f.read(n)
    if len(b)!=n: raise IOError('lecture courte')
    return b
boot=read(base,512)
u16=lambda b,o:struct.unpack_from('<H',b,o)[0]
u32=lambda b,o:struct.unpack_from('<I',b,o)[0]
bps=u16(boot,11); spc=boot[13]; reserved=u16(boot,14); fats=boot[16]; fatlen=u32(boot,36); total=u32(boot,32)
cs=bps*spc; data=base+(reserved+fats*fatlen)*bps; n=(total-reserved-fats*fatlen)//spc
rawfat=read(base+reserved*bps,fatlen*bps)
fat=array.array('I',rawfat)
if sys.byteorder!='little': fat.byteswap()
def chain(c):
    out=[]; seen=set()
    while 2<=c<n+2 and c not in seen:
        out.append(c); seen.add(c)
        nextc=fat[c]&0xfffffff
        if nextc==0 or nextc>=0xffffff8: break
        c=nextc
    return out
def stamp(date,time=0,tenth=0):
    if not date: return None
    try: return datetime.datetime(1980+(date>>9),date>>5&15,date&31,time>>11,time>>5&63,(time&31)*2)+datetime.timedelta(milliseconds=tenth*10)
    except ValueError: return 'INVALID'
def strstamp(date,time=0,tenth=0):
    s=stamp(date,time,tenth)
    return s.isoformat(' ') if isinstance(s,datetime.datetime) else s
entries=[]; visited=set(); dirs=[]
def walk(c,path,deleted_parent=False):
    if c in visited or c<2 or c>=n+2:return
    visited.add(c)
    clusters=chain(c)
    buf=b''.join(read(data+(x-2)*cs,cs) for x in clusters)
    dirs.append(dict(path=path,start_cluster=c,clusters=clusters,size=len(buf),sha256=hashlib.sha256(buf).hexdigest()))
    lfn=[]; ended=False; children=[]
    for off in range(0,len(buf),32):
        slot=buf[off:off+32]
        if slot[0]==0: ended=True;lfn=[];continue
        deleted=slot[0]==0xe5
        if slot[11]==0xf:
            txt=(slot[1:11]+slot[14:26]+slot[28:32]).decode('utf-16le',errors='replace').split('\x00')[0].rstrip('\uffff')
            lfn.insert(0,txt)
            continue
        short=slot[:8].decode('cp437',errors='replace').rstrip()+('.'+slot[8:11].decode('cp437',errors='replace').rstrip() if slot[8:11].strip() else '')
        name=''.join(lfn) if lfn else short
        lfn=[]
        start=(u16(slot,20)<<16)|u16(slot,26)
        cluster_index=off//cs
        absolute=data+(clusters[cluster_index]-2)*cs+off%cs
        rec=dict(path=(path+'/'+name).lstrip('/'),name=name,short_name=short,absolute_entry_offset=absolute,deleted=deleted,after_end_marker=ended,deleted_parent=deleted_parent,attributes=slot[11],start_cluster=start,first_fat_value=fat[start]&0xfffffff if start<len(fat) else None,size=u32(slot,28),created=strstamp(u16(slot,16),u16(slot,14),slot[13]),written=strstamp(u16(slot,24),u16(slot,22)),accessed=strstamp(u16(slot,18)),raw_hex=slot.hex())
        entries.append(rec)
        if slot[11]&16 and name not in ('.','..') and not ended:
            children.append((deleted,start,rec['path']))
    # Un ancien nom supprimé peut pointer sur un répertoire toujours alloué.
    # Préférer son chemin actuel ; ne pas dupliquer son contenu sous l'ancien nom.
    for deleted,start,childpath in sorted(children):
        walk(start,childpath,deleted_parent or deleted)
walk(u32(boot,44),'')
back=read(base+u16(boot,50)*bps,bps)
info=[]
for rel in (u16(boot,48),u16(boot,50)+u16(boot,48)):
    b=read(base+rel*bps,bps)
    info.append(dict(relative_sector=rel,lead_signature=hex(u32(b,0)),structure_signature=hex(u32(b,484)),trail_signature=hex(u32(b,508)),free_clusters=u32(b,488),next_free_cluster=u32(b,492),sha256=hashlib.sha256(b).hexdigest()))
print(json.dumps(dict(geometry=dict(partition_offset_bytes=base,bytes_per_sector=bps,sectors_per_cluster=spc,cluster_bytes=cs,reserved_sectors=reserved,fats=fats,fat_sectors=fatlen,total_sectors=total,data_absolute_offset=data,total_clusters=n,hidden_sectors=u32(boot,28),volume_id=hex(u32(boot,67)),oem=boot[3:11].decode(errors='replace')),fat_sha256=[hashlib.sha256(read(base+(reserved+i*fatlen)*bps,fatlen*bps)).hexdigest() for i in range(fats)],fat_free_count=sum((v&0xfffffff)==0 for v in fat[2:n+2]),fat_nonfree_count=sum((v&0xfffffff)!=0 for v in fat[2:n+2]),fat_bad_clusters=[i for i in range(2,n+2) if fat[i]&0xfffffff==0xffffff7],boot_differences=[dict(offset=i,main=a,backup=b) for i,(a,b) in enumerate(zip(boot,back)) if a!=b],fsinfo=info,directories=dirs,entries=entries),ensure_ascii=False,indent=2))
