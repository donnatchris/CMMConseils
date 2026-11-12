#!/usr/bin/env python3
"""Audit indépendant des chaînes allouées et du slack des fichiers actifs.
RAW_VERIFIED est la contre-lecture JSON v2 transmise par le collecteur.
"""
import array
import collections
import hashlib
import json
import re
import sys

raw=json.loads(RAW_VERIFIED)
g=raw['geometry'];f=open(sys.argv[1],'rb');cs=g['cluster_bytes'];data=g['data_absolute_offset'];n=g['total_clusters']
f.seek(g['partition_offset_bytes']+g['reserved_sectors']*g['bytes_per_sector'])
fat=array.array('I',f.read(g['fat_sectors']*g['bytes_per_sector']))
if sys.byteorder!='little':fat.byteswap()
def chain(c):
    out=[];seen=set();error=None
    while 2<=c<n+2:
        if c in seen:error='cycle';break
        seen.add(c);out.append(c);v=fat[c]&0xfffffff
        if v>=0xffffff8:break
        if v<2 or v>=n+2:error='invalid_next_'+str(v);break
        c=v
    return out,error
owners=collections.defaultdict(list);problems=[];direct=[];slacks=[];excess=[]
active=[e for e in raw['entries'] if not e['deleted'] and not e['after_end_marker'] and e['name'] not in ('.','..')]
# Le répertoire racine n'a pas de slot dans lui-même.
for c in (2,):owners[c].append('/')
for e in active:
    if not e['start_cluster']:continue
    ch,error=chain(e['start_cluster'])
    for c in ch:owners[c].append(e['path'])
    capacity=len(ch)*cs
    if error or capacity<e['size']:problems.append(dict(path=e['path'],error=error,capacity=capacity,size=e['size']))
    if e['attributes']&16:continue
    needed=(e['size']+cs-1)//cs
    if len(ch)>needed:
        parts=[]
        for c in ch[needed:]:
            f.seek(data+(c-2)*cs);part=f.read(cs)
            parts.append(dict(cluster=c,absolute_offset=data+(c-2)*cs,nonzero_bytes=sum(x!=0 for x in part),sha256=hashlib.sha256(part).hexdigest(),signature_candidates=[dict(offset=m.start(),signature=m.group().decode(errors='replace')) for m in re.finditer(rb'ftyp|moov|mdat|(?:19|20)\d{6}_\d{6}',part)]))
        excess.append(dict(path=e['path'],required_clusters=needed,allocated_clusters=len(ch),extra_clusters=parts))
    if any(e['name'].startswith(s) for s in ('20240221_','20240301_','20241028_232503')):
        h=hashlib.sha256();left=e['size']
        for c in ch:
            f.seek(data+(c-2)*cs);part=f.read(min(cs,left));h.update(part);left-=len(part)
            if not left:break
        direct.append(dict(path=e['path'],declared_size=e['size'],bytes_hashed=e['size']-left,chain_clusters=len(ch),sha256=h.hexdigest()))
    if e['size']%cs:
        idx=e['size']//cs
        if idx<len(ch):
            offset=data+(ch[idx]-2)*cs+e['size']%cs;length=cs-e['size']%cs
            f.seek(offset);part=f.read(length)
            sig=[dict(absolute_offset=offset+m.start(),signature=m.group().decode(errors='replace')) for m in re.finditer(rb'ftyp|moov|mdat|(?:19|20)\d{6}_\d{6}|NTFS    |EXFAT   |mkdosfs',part)]
            slacks.append(dict(path=e['path'],absolute_offset=offset,length=length,nonzero_bytes=sum(b!=0 for b in part),sha256=hashlib.sha256(part).hexdigest(),signature_candidates=sig))
lost=[c for c in range(2,n+2) if fat[c]&0xfffffff and c not in owners]
print(json.dumps(dict(active_entries=len(active),referenced_clusters=len(owners),allocated_unreferenced_clusters=lost,crosslinks={str(c):v for c,v in owners.items() if len(v)>1},chain_problems=problems,direct_hash_checks=direct,fat_reserved_entries=[hex(fat[0]),hex(fat[1])],excess_allocation=excess,slack_bytes_read=sum(s['length'] for s in slacks),slack_nonzero_bytes=sum(s['nonzero_bytes'] for s in slacks),slack=slacks),ensure_ascii=False,indent=2))
