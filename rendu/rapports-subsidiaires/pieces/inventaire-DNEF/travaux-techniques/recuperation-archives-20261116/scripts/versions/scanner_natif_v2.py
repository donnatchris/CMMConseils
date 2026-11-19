"""Balayage intégral des clusters NTFS libres et des fichiers mémoire/métadonnées.

Lecture seule. Détection par noms ASCII/UTF16 et structures ZIP ; toute récupération
candidate reste distincte d'une attribution à Archive_saddedine.zip.
"""
import collections
import ctypes
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import pyfsntfs
import re
import struct
import subprocess
import time
import zipfile

P=Path('/media/shared/codeProjects/DMMConseils');O=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive/balayage-v2'
os.umask(0o077);O.mkdir(parents=True,exist_ok=False)
(O/'fragments').mkdir();(O/'archives-candidates').mkdir()
SOURCE=Path('/mnt/dislocker/dislocker-file');fd=os.open(SOURCE,os.O_RDONLY)
boot=os.pread(fd,512,0);sector=struct.unpack_from('<H',boot,11)[0];cluster=sector*boot[13];total=struct.unpack_from('<Q',boot,40)[0]*sector
assert boot[3:11]==b'NTFS    ' and cluster==4096
assert 'ro,' in subprocess.check_output(['findmnt','-n','-o','OPTIONS','/mnt/windows'],text=True)
v=pyfsntfs.volume();v.open(str(SOURCE));entry=v.get_file_entry(6);bits=entry.read_buffer_at_offset(entry.size,0);v.close()
(O/'bitmap.bin').write_bytes(bits);(O/'boot.bin').write_bytes(boot)
clusters=total//cluster;runs=[];start=None
for bi,byte in enumerate(bits):
    first=bi*8
    if first>=clusters:break
    if byte==0 and first+8<=clusters:
        if start is None:start=first
    elif byte==255:
        if start is not None:runs.append((start*cluster,(first-start)*cluster));start=None
    else:
        for j in range(min(8,clusters-first)):
            index=first+j
            if not (byte>>j)&1:
                if start is None:start=index
            elif start is not None:runs.append((start*cluster,(index-start)*cluster));start=None
if start is not None:runs.append((start*cluster,(clusters-start)*cluster))
with (O/'free-runs.bin').open('xb') as f:
    for offset,length in runs:f.write(struct.pack('<QQ',offset,length))
freebytes=sum(n for _,n in runs)
geom={'source':str(SOURCE),'volume_bytes':total,'sector_size':sector,'cluster_size':cluster,'free_runs':len(runs),'free_bytes':freebytes,
      'bitmap_sha256':hashlib.sha256(bits).hexdigest(),'boot_sha256':hashlib.sha256(boot).hexdigest(),'volume_serial_hex':f'{struct.unpack_from("<Q",boot,72)[0]:016x}'}
with (O/'geometrie.json').open('x') as f:json.dump(geom,f,indent=2)
print('GEOMETRY',json.dumps(geom),flush=True)

words=['Archive_saddedine.zip','Rejets_saddedine.txt','Inventaire_saddedine.csv','IPHONE13_MINI','Dossier bourarach','inventaire de saisie','nombre de fichiers saisis']
patterns={}
for word in words:
    for encoding in ['utf-8','utf-16le']:patterns[word.encode(encoding)]=word+'|'+encoding
patterns[b'PK\x05\x06']='ZIP_EOCD';patterns[b'PK\x06\x06']='ZIP64_EOCD'
pattern_list=list(patterns)
lib=ctypes.CDLL(str(O.parent/'outils/signatures.so'))
lib.initialize.argtypes=[ctypes.POINTER(ctypes.c_char_p),ctypes.POINTER(ctypes.c_size_t),ctypes.c_int]
lib.initialize.restype=ctypes.c_int
lib.scan.argtypes=[ctypes.c_char_p,ctypes.c_size_t,ctypes.POINTER(ctypes.c_int),ctypes.POINTER(ctypes.c_size_t),ctypes.c_size_t]
lib.scan.restype=ctypes.c_long
pa=(ctypes.c_char_p*len(pattern_list))(*pattern_list)
lengths=(ctypes.c_size_t*len(pattern_list))(*(len(x) for x in pattern_list))
assert lib.initialize(pa,lengths,len(pattern_list))>0
capacity=200000
ids=(ctypes.c_int*capacity)();ends=(ctypes.c_size_t*capacity)()
nameslog=(O/'occurrences.jsonl').open('x');ziplog=(O/'zip-candidats.jsonl').open('x');progress=(O/'progression.jsonl').open('x')
counts=collections.Counter();saved=collections.Counter();seen=set();seen_zip=set();recovered=[];errors=[]
started=time.monotonic();readbytes=0;last_progress=0

def allocation(offset,length):
    first=offset//cluster;last=min(clusters,(offset+length+cluster-1)//cluster)
    return {'clusters':last-first,'allocated_clusters':sum((bits[i//8]>>(i%8))&1 for i in range(first,last))}

def inspect_zip(eocd,scope):
    if eocd in seen_zip:return
    seen_zip.add(eocd)
    raw=os.pread(fd,22,eocd)
    if len(raw)!=22:return
    sig,disk,cd_disk,n_disk,n,cdsize,cdoff,comment=struct.unpack('<4s4H2LH',raw)
    if disk or cd_disk or not n or n_disk!=n or not (0<cdsize<=32*1024**2) or cdoff==0xffffffff:return
    archive_start=eocd-cdsize-cdoff;archive_end=eocd+22+comment
    if archive_start<0 or archive_end>total:return
    cd=os.pread(fd,cdsize,eocd-cdsize)
    if not cd.startswith(b'PK\x01\x02'):return
    at=0;members=[]
    while at+46<=len(cd) and cd[at:at+4]==b'PK\x01\x02':
        flag=struct.unpack_from('<H',cd,at+8)[0];nl,xl,cl=struct.unpack_from('<HHH',cd,at+28)
        if at+46+nl+xl+cl>len(cd):break
        name=cd[at+46:at+46+nl].decode('utf-8' if flag&2048 else 'cp437',errors='replace')
        members.append(name);at+=46+nl+xl+cl
    if len(members)!=n:return
    length=archive_end-archive_start
    interesting=[x for x in members if re.search(r'IPHONE13_MINI|L16B|saddedine|bourarach',x,re.I)]
    row={'eocd_offset':eocd,'scope':scope,'start':archive_start,'bytes':length,'members':n,'interesting_names':interesting,'all_names':members,
         'header_valid':os.pread(fd,4,archive_start)==b'PK\x03\x04','matches_recorded_archive_size':length==3525227798}
    if interesting or row['matches_recorded_archive_size']:
        row['allocation']=allocation(archive_start,length)
        if row['header_valid'] and length<=4*1024**3 and (row['matches_recorded_archive_size'] or n>=100 and len(interesting)>=3):
            dest=O/'archives-candidates'/f'{archive_start}-{length}.zip';h=hashlib.sha256()
            with dest.open('xb') as out:
                pos=archive_start
                while pos<archive_end:
                    block=os.pread(fd,min(32*1024**2,archive_end-pos),pos)
                    if not block:raise OSError('short carving read')
                    out.write(block);h.update(block);pos+=len(block)
            row['candidate_file']=str(dest.relative_to(O));row['sha256']=h.hexdigest()
            try:
                with zipfile.ZipFile(dest) as z:
                    row['zipfile_member_count']=len(z.infolist())
                    row['crc_check_bad_member']=z.testzip()
            except Exception as ex:row['validation_error']=str(ex)
            recovered.append(row['candidate_file'])
    ziplog.write(json.dumps(row,ensure_ascii=False)+'\n');ziplog.flush()

def process(data,base,scope,physical=True):
    found=lib.scan(data,len(data),ids,ends,capacity)
    if found<0:raise RuntimeError('Native signature result capacity exceeded')
    for i in range(found):
        pattern=pattern_list[ids[i]];label=patterns[pattern]
        match_start=ends[i]-len(pattern);match_end=ends[i]
        offset=base+match_start;key=(scope,offset,label)
        if key in seen:continue
        seen.add(key);counts[label]+=1
        if label=='ZIP_EOCD' and physical:
            try:inspect_zip(offset,scope)
            except Exception as ex:errors.append({'offset':offset,'error':str(ex)})
        if label.startswith('ZIP'):continue
        row={'source_scope':scope,'offset':offset,'label':label,'physical_partition_offset':offset if physical else None}
        if saved[label]<2000:
            start=max(0,match_start-512);fragment=data[start:min(len(data),match_end+8192)]
            dest=O/'fragments'/f'{len(seen):08d}.bin';dest.write_bytes(fragment)
            row.update(fragment=str(dest.relative_to(O)),fragment_start=base+start,sha256=hashlib.sha256(fragment).hexdigest());saved[label]+=1
        else:row['fragment_not_saved']='per_pattern_cap_2000'
        nameslog.write(json.dumps(row,ensure_ascii=False)+'\n');nameslog.flush()

def tick(scope):
    global last_progress
    if readbytes-last_progress>=4*1024**3:
        elapsed=time.monotonic()-started
        row={'scope':scope,'bytes_read':readbytes,'elapsed_seconds':elapsed,'MiB_s':readbytes/1024**2/elapsed,'matches':dict(counts)}
        progress.write(json.dumps(row)+'\n');progress.flush();print('PROGRESS',json.dumps(row),flush=True);last_progress=readbytes

# Files where an opened external text/list or ZIP directory may have remained.
logical=[]
for name in ['pagefile.sys','swapfile.sys','hiberfil.sys','$MFT','$LogFile']:
    p=Path('/mnt/windows')/name
    if not p.is_file():continue
    h=hashlib.sha256();tail=b'';offset=0
    with p.open('rb') as f:
        while data:=f.read(32*1024**2):
            h.update(data);combined=tail+data;process(combined,offset-len(tail),name,False)
            offset+=len(data);readbytes+=len(data);tail=combined[-256:];tick(name)
    logical.append({'source':str(p),'bytes':offset,'sha256':h.hexdigest()})
with (O/'fichiers-logiques.json').open('x') as f:json.dump(logical,f,indent=2)
print('MEMORY_COMPLETE',json.dumps({'files':len(logical),'matches':dict(counts)}),flush=True)

free_digest=hashlib.sha256()
for run_index,(offset,length) in enumerate(runs):
    end=offset+length;pos=offset;tail=b''
    while pos<end:
        data=os.pread(fd,min(32*1024**2,end-pos),pos)
        if not data:raise OSError('short free-space read')
        free_digest.update(data);combined=tail+data;process(combined,pos-len(tail),'unallocated',True)
        pos+=len(data);readbytes+=len(data);tail=combined[-256:];tick('unallocated')
    if run_index%10000==0:progress.write(json.dumps({'free_run_completed':run_index,'free_runs_total':len(runs),'bytes_read':readbytes})+'\n');progress.flush()
summary={'finished_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'free_bytes_scanned':freebytes,'free_runs_scanned':len(runs),
         'free_stream_sha256':free_digest.hexdigest(),'total_bytes_scanned':readbytes,'elapsed_seconds':time.monotonic()-started,
         'matches':dict(counts),'fragments_saved':dict(saved),'archives_candidates_saved':recovered,'errors':errors,
         'limits':['No general decompression of hibernation/pagefile memory compression','A fragmented archive without extents may escape contiguous ZIP reconstruction','An empty file cannot be identified by a content signature']}
with (O/'synthese.json').open('x') as f:json.dump(summary,f,ensure_ascii=False,indent=2)
for f in [nameslog,ziplog,progress]:f.close()
os.close(fd);print('DONE',json.dumps(summary),flush=True)
