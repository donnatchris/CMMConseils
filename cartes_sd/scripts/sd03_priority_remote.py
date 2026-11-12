#!/usr/bin/env python3
"""SIFT : analyse logique FAT en lecture seule, MP4 anonymes en RAM, tar stdout.
Geometry/entries/selection dans PARAMS. Plafond d'extractions impératif.
Le parseur inspect() pur est préfixé au script par sd03_receive.py.
"""
import array
import concurrent.futures
import hashlib
import io
import json
import os
import subprocess
import sys
import tarfile
import time

image=sys.argv[1];g=PARAMS['geometry'];base=g['partition_offset_bytes'];cs=g['cluster_bytes'];n=g['total_clusters'];dataoff=g['data_absolute_offset'];sector=base//512
f=open(image,'rb');f.seek(base+g['reserved_sectors']*512)
fat=array.array('I',f.read(g['fat_sectors']*512))
if sys.byteorder!='little':fat.byteswap()
entries=PARAMS['entries'];save=set(PARAMS['save_inodes']);decode=set(PARAMS['decode_inodes'])
if sum(e['size'] for e in entries if str(e['inode']) in save)>PARAMS['save_max_bytes']:raise ValueError('Prévol taille sauvegarde')
saved=0;records=[]

def chain(c):
    result=[];seen=set()
    while 2<=c<n+2:
        if c in seen:raise ValueError('Cycle FAT')
        seen.add(c);result.append(c);v=fat[c]&0xfffffff
        if v>=0xffffff8:break
        if not 2<=v<n+2:raise ValueError('Chaîne active interrompue')
        c=v
    return result

def readfile(e):
    if e['size']>256*1024**2:raise ValueError('Média supérieur à 256 Mio')
    if not e['size']:return b'',[]
    ch=chain(e['start_cluster']);left=e['size'];parts=[];i=0
    while i<len(ch) and left:
        j=i+1
        while j<len(ch) and ch[j]==ch[j-1]+1 and j-i<256:j+=1
        length=min(left,(j-i)*cs);f.seek(dataoff+(ch[i]-2)*cs);part=f.read(length)
        if len(part)!=length:raise IOError('Lecture courte')
        parts.append(part);left-=len(part);i=j
    if left:raise IOError('Chaîne plus courte que la taille')
    return b''.join(parts),ch

with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
    def add(name,b):
        t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
    for index,e in enumerate(entries):
        inode=str(e['inode']);r=dict(inode=inode,path=e['path'],size=e['size'],deleted=e['deleted'],start_cluster=e['start_cluster'],method='lecture chaîne FAT active' if not e['deleted'] else 'icat -r heuristique pour entrée supprimée')
        try:
            if e['deleted']:
                if e['size']>256*1024**2:raise ValueError('Suppression supérieure au plafond')
                args=['icat','-r','-o',str(sector),image,inode]
                p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120)
                content=p.stdout;ch=[];r['recovery']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'))
            else:content,ch=readfile(e)
            r.update(read_size=len(content),sha256=hashlib.sha256(content).hexdigest(),allocated_chain_clusters=len(ch),prefix_bytes=min(len(content),16384),prefix_sha256=hashlib.sha256(content[:16384]).hexdigest())
            if (e['path'].lower().endswith('.mp4') or content[4:8]==b'ftyp') and content:
                r['mp4_structure']=inspect(content)
                descriptions=[]
                for b in r['mp4_structure']['boxes']:
                    if b['path'].endswith('/stsd'):
                        descriptions.append(dict(size=b['size'],sha256=hashlib.sha256(content[b['offset']:b['offset']+b['size']]).hexdigest()))
                r['stsd']=descriptions
                fd=os.memfd_create('sd03-video',0)
                try:
                    with os.fdopen(fd,'wb',closefd=False) as mem:mem.write(content)
                    path='/proc/self/fd/'+str(fd)
                    args=['ffprobe','-v','error','-show_format','-show_streams','-of','json',path]
                    p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
                    r['ffprobe']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'))
                    try:r['metadata']=json.loads(p.stdout)
                    except ValueError:r['metadata']={}
                    anomalies=r['mp4_structure']['errors'] or any(t['chunks_beyond_eof'] or t['stsz_sample_count']!=t['chunk_sample_count'] or t['stts_sample_count']!=t['stsz_sample_count'] for t in r['mp4_structure']['tracks'])
                    # Tous les cas ciblés, les anomalies structurelles et les récupérations.
                    if inode in decode or (anomalies and not e['deleted']) or (e['deleted'] and not e['first_fat_value'] and not r['mp4_structure']['errors']):
                        args=['ffmpeg','-v','warning','-threads','1','-i',path,'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-']
                        p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=600)
                        log='journaux/priorite-decodage/'+inode+'.txt';add(log,p.stderr)
                        r['decode']=dict(argv=args,returncode=p.returncode,stderr_bytes=len(p.stderr),log=log)
                    # Temps d'origine des paquets : inventaire complet sans conserver payload.
                    args=['ffprobe','-v','error','-select_streams','v:0','-show_packets','-show_entries','packet=pts,dts','-of','json',path]
                    p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
                    packets=json.loads(p.stdout).get('packets',[]) if p.returncode==0 else []
                    summaries={}
                    for field in ('dts','pts'):
                        values=[int(x[field]) for x in packets if field in x];delta=[b-a for a,b in zip(values,values[1:])]
                        summaries[field]=dict(count=len(values),nonincreasing=sum(x<=0 for x in delta),max_delta=max(delta,default=None),min_delta=min(delta,default=None))
                    r['packets']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'),summary=summaries,raw_output_sha256=hashlib.sha256(p.stdout).hexdigest())
                finally:os.close(fd)
            if inode in save:
                saved+=len(content)
                if saved>PARAMS['save_max_bytes']:raise ValueError('Plafond de sauvegarde')
                artifact='prive/priorite/'+inode+'_'+e['path'].rsplit('/',1)[-1]
                add(artifact,content);r['artifact']=artifact
            # Contrôle indépendant TSK des fichiers sauvegardés, tous bornés.
            if inode in save and not e['deleted']:
                args=['icat','-o',str(sector),image,inode]
                p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120)
                r['icat_crosscheck']=dict(argv=args,returncode=p.returncode,bytes=len(p.stdout),sha256=hashlib.sha256(p.stdout).hexdigest(),matches=(p.stdout==content),stderr=p.stderr.decode(errors='replace'))
        except Exception as ex:r['error']=type(ex).__name__+': '+str(ex)
        add('inventaires/priorite/'+inode+'.json',json.dumps(r,ensure_ascii=False,indent=2).encode())
        records.append({k:v for k,v in r.items() if k not in ('metadata','mp4_structure')})
        if index%100==0:print('SD03 médias analysés '+str(index+1)+'/'+str(len(entries)),file=sys.stderr,flush=True)
    add('inventaires/priorite-index.json',json.dumps(dict(entries=records,saved_bytes=saved,all_entries=len(entries)),ensure_ascii=False,indent=2).encode())
