#!/usr/bin/env python3
"""SIFT : export tar sur stdout, sans fichier distant. Image ouverte rb uniquement."""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tarfile

image = sys.argv[1]
env = dict(os.environ, TZ='UTC')
def run(args):
    p = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    return p.stdout, dict(argv=args, returncode=p.returncode, stderr=p.stderr.decode(errors='replace'))

with tarfile.open(fileobj=sys.stdout.buffer, mode='w|') as tar:
    def add(name, data):
        t = tarfile.TarInfo(name)
        t.size = len(data)
        t.mode = 0o600
        tar.addfile(t, io.BytesIO(data))
    if 'VERIFIED_LISTING' in globals():
        listing=VERIFIED_LISTING
        status=dict(source='inventaires/fls.txt collecte précédente',sha256=hashlib.sha256(listing).hexdigest())
    else:
        listing, status = run(['fls','-o','8192','-r','-p', image])
    records = []
    # Ajouter la racine pour inspecter aussi les slots supprimés et le slack.
    listing=b'd/d 2: /\n'+listing
    for line in listing.decode().splitlines():
        m = re.match(r'([^ ]+)\s+(\*\s+)?(\d+):\s+(.*)', line)
        if not m:
            records.append(dict(unparsed=line))
            continue
        typ, deleted, inode, path = m.groups()
        if typ.startswith('v'):
            continue
        stat, sr = run(['istat','-z','UTC','-o','8192',image,inode])
        add('journaux/istat/'+inode+'.txt', stat)
        rec = dict(type=typ, deleted=bool(deleted), inode=inode, path=path, istat_status=sr)
        if typ.startswith('d') and b'Sectors:\n' in stat:
            sectors=[int(s) for s in re.findall(rb'\b\d+\b',stat.split(b'Sectors:\n',1)[1])]
            if len(sectors)>4096:
                raise ValueError('Répertoire au-delà de 2 Mio')
            with open(image,'rb') as source:
                content=bytearray()
                for sector in sectors:
                    if sector:
                        source.seek((8192+sector)*512)
                        content.extend(source.read(512))
            add('prive/repertoires/'+inode+'.bin',bytes(content))
        if typ.startswith('r'):
            size_match=re.search(rb'Size: (\d+)',stat)
            if size_match and int(size_match.group(1))>256*1024**2:
                raise ValueError('Fichier au-delà de la limite de 256 Mio')
            args = ['icat']+(['-r'] if deleted else [])+['-o','8192',image,inode]
            data, result = run(args)
            name = 'prive/extraits/'+inode+'_'+path.rsplit('/',1)[-1]
            add(name, data)
            rec.update(extraction=result, artifact=name, extracted_size=len(data), sha256=hashlib.sha256(data).hexdigest())
            if path.endswith('.mp4'):
                # Copie en mémoire vive anonyme : ffprobe peut chercher sans fichier distant.
                fd=os.memfd_create('sd01-video',0)
                with os.fdopen(fd,'wb',closefd=False) as mem:
                    mem.write(data)
                probe_args=['ffprobe','-v','error','-show_format','-show_streams','-of','json','/proc/self/fd/'+str(fd)]
                p=subprocess.run(probe_args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                add('journaux/ffprobe/'+inode+'.json',p.stdout)
                rec['ffprobe']=dict(argv=probe_args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'))
                # Décodage intégral des clips de la période centrale et des deux anomalies 2000.
                if not deleted and (re.search(r'/202410(?:1[5-9]|2[0-8])/',path) or inode in ('22835208','20903944')):
                    args=['ffmpeg','-v','warning','-threads','2','-i','/proc/self/fd/'+str(fd),'-f','null','-']
                    p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=600)
                    add('journaux/decodage/'+inode+'.txt',p.stderr)
                    rec['decode']=dict(argv=args,returncode=p.returncode,warnings_bytes=len(p.stderr))
                os.close(fd)
        records.append(rec)
    with open(image, 'rb') as f:
        for name, offset, size in [('mbr-et-avant-partition',0,8192*512),('reserve-fat32',8192*512,6*512),('fat1',(8192+6)*512,15209*512),('fat2',(8192+15215)*512,15209*512),('fin-partition',(8192+62325752)*512,8*512)]:
            f.seek(offset)
            data=f.read(size)
            add('structures/'+name+'.bin',data)
    add('inventaires/export.json', json.dumps(dict(listing_status=status, entries=records), ensure_ascii=False, indent=2).encode())
