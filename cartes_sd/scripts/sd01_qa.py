#!/usr/bin/env python3
"""Étapes auxiliaires de QA enregistrées : qualité, contrôles, anciens boots,
manifeste local. Utiliser une nouvelle campagne SD01_RUN pour reproduire.
"""
import collections
import hashlib
import json
import pathlib
import subprocess
import sys
import csv
import datetime as dt
from sd01_collect import OUT,ROOT

phase=sys.argv[1]
if phase=='qualite':
    export=json.loads((OUT/'inventaires/export.json').read_text());rows=[];counts=collections.Counter()
    for e in export['entries']:
        if 'decode' not in e:continue
        text=(OUT/'journaux/decodage'/f"{e['inode']}.txt").read_text();tags=[]
        if 'non monotonically increasing dts' in text:tags.append('avertissement_sortie_null_DTS')
        if 'wrong sample count' in text:tags.append('comptage_echantillons')
        if any(t in text for t in ('Invalid NAL','Packet corrupt','Error splitting','Decoding error')):tags.append('corruption_flux')
        if text and not tags:tags.append('autre')
        counts.update(tags);rows.append(dict(inode=e['inode'],path=e['path'],returncode=e['decode']['returncode'],stderr_bytes=len(text.encode()),categories=tags))
    with (OUT/'inventaires/qualite-decodage.json').open('x') as f:json.dump(dict(count=len(rows),categories=dict(counts),entries=rows),f,indent=2)
elif phase=='complement':
    rows=[]
    for inode in ('11500564','36542512','41329160','76861456'):
        p=next((OUT/'prive/extraits').glob(inode+'_*.mp4'))
        args=['ffmpeg','-v','warning','-threads','2','-i',str(p),'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-']
        run=subprocess.run(args,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        row=dict(inode=inode,argv=args,returncode=run.returncode,stderr=run.stderr.decode())
        if inode in ('41329160','76861456'):
            args=['ffprobe','-v','error','-select_streams','v:0','-show_packets','-show_entries','packet=pts,dts,pts_time,dts_time','-of','json',str(p)]
            run=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            with (OUT/'journaux'/f'paquets-{inode}.json').open('xb') as f:f.write(run.stdout)
            data=json.loads(run.stdout)['packets'];ts=[int(r['dts']) for r in data if 'dts' in r];ps=[int(r['pts']) for r in data if 'pts' in r]
            row['packets']=dict(argv=args,returncode=run.returncode,count=len(data),dts_nonincreasing=sum(b<=a for a,b in zip(ts,ts[1:])),pts_nonincreasing=sum(b<=a for a,b in zip(ps,ps[1:])))
        rows.append(row)
    with (OUT/'inventaires/decodages-complementaires.json').open('x') as f:json.dump(rows,f,indent=2)
elif phase=='boot':
    candidates=[];signatures=collections.Counter()
    for p in (OUT/'prive/residus').glob('*.bin'):
        data=p.read_bytes();base=19771392+(int(p.stem)-2)*16384
        for name in (b'EFI PART',b'NTFS    ',b'EXFAT   ',b'mkdosfs',b'FAT32',b'MSDOS5.0'):
            if name in data:signatures[name.decode()]+=1
        for off in range(0,len(data),512):
            s=data[off:off+512]
            if s[510:512]!=b'\x55\xaa':continue
            bps=int.from_bytes(s[11:13],'little');spc=s[13]
            candidates.append(dict(absolute_offset=base+off,bytes_per_sector=bps,sectors_per_cluster=spc,plausible_fat_bpb=bps in (512,1024,2048,4096) and spc in (1,2,4,8,16,32,64,128) and s[16] in (1,2)))
    last=(OUT/'structures/fin-partition.bin').read_bytes()[-512:]
    result=dict(method='Tous les secteurs de 512 octets des clusters libres non nuls ; marque 55aa puis validation élémentaire BPB ; recherche littérale complémentaire GPT/NTFS/exFAT/FAT',signature_counts=dict(signatures),sectors_55aa=candidates,plausible_fat_boot_candidates=[r for r in candidates if r['plausible_fat_bpb']],last_sector_sha256=hashlib.sha256(last).hexdigest(),last_sector_signature_hex=last[-2:].hex())
    with (OUT/'inventaires/recherche-anciens-boot.json').open('x') as f:json.dump(result,f,indent=2)
elif phase=='horloges':
    raw=json.loads((OUT/'inventaires/lecture-fat-independante-v2.json').read_text())
    body={r[2]:r for r in (s.split('|') for s in (OUT/'inventaires/timeline.body').read_text().splitlines())}
    checks=[]
    for r in raw['entries']:
        if r['name'] in ('.','..') or r['after_end_marker']:continue
        inode=str(3+(r['absolute_entry_offset']-raw['geometry']['data_absolute_offset'])//32)
        for name,index in [('created',10),('written',8),('accessed',7)]:
            if not r[name]:continue
            epoch=dt.datetime.fromisoformat(r[name]).replace(tzinfo=dt.timezone.utc).timestamp()
            diff=epoch-int(body[inode][index]);checks.append(dict(inode=inode,field=name,raw=r[name],tsk_body_epoch=int(body[inode][index]),raw_interpreted_utc_minus_body_seconds=round(diff,6)))
    result=dict(method='UTC utilisé uniquement comme convention de conversion numérique ; pas preuve du fuseau caméra',checks=checks,difference_counts=dict(collections.Counter(str(r['raw_interpreted_utc_minus_body_seconds']) for r in checks)),written_or_accessed_mismatches=[r for r in checks if r['field']!='created' and r['raw_interpreted_utc_minus_body_seconds']!=0],creation_over_one_second=[r for r in checks if r['field']=='created' and not 0<=r['raw_interpreted_utc_minus_body_seconds']<=1])
    with (OUT/'inventaires/concordance-horodatages.json').open('x') as f:json.dump(result,f,indent=2)
    print({k:v for k,v in result.items() if k!='checks'})
elif phase=='manifest':
    files=sorted(p for p in OUT.rglob('*') if p.is_file() and p.name!='manifest-sha256.csv')
    files+=sorted((ROOT/'cartes_sd/scripts').glob('*.py'))
    with (OUT/'manifest-sha256.csv').open('x',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['path_from_project','size','sha256']);writer.writeheader()
        for p in files:
            h=hashlib.sha256()
            with p.open('rb') as source:
                while data:=source.read(1024*1024):h.update(data)
            writer.writerow(dict(path_from_project=str(p.relative_to(ROOT)),size=p.stat().st_size,sha256=h.hexdigest()))
    print('Fichiers manifestés',len(files))
else:raise SystemExit('qualite | complement | boot | horloges | manifest')
