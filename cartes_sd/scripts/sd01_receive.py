#!/usr/bin/env python3
"""Reçoit un tar par stdout SSH ; écrit uniquement sous OUT. Refuse tout écrasement."""
import datetime as dt
import json
import pathlib
import subprocess
import tarfile
import shutil
from sd01_collect import ROOT, OUT, SSH, IMAGE

script = ROOT/'cartes_sd/scripts/sd01_export_remote.py'
# Prévol obligatoire à partir de la chronologie complète, pas d'export non borné.
rawpath=OUT/'inventaires/lecture-fat-independante-v2.json'
if not rawpath.exists():rawpath=OUT/'inventaires/lecture-fat-independante.json'
raw=json.loads(rawpath.read_text())
records=[r for r in raw['entries'] if not r['after_end_marker'] and not r['attributes']&16]
declared=sum(r['size'] for r in records)
limit=4*1024**3
if declared>3*1024**3 or len(records)>2000:
    raise SystemExit('Prévol : taille ou nombre de fichiers au-delà du périmètre borné')
if shutil.disk_usage(OUT).free < limit+8*1024**3:
    raise SystemExit('Prévol : marge de 8 Gio insuffisante après export maximal de 4 Gio')
print('Prévol octets déclarés :',declared,'; limite flux :',limit,flush=True)
argv=SSH+['sudo -n python3 - '+IMAGE]
start=dt.datetime.now(dt.timezone.utc).isoformat()
with (OUT/'journaux/export.stderr').open('xb') as err:
    p=subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err)
    listing=(OUT/'inventaires/fls.txt').read_bytes()
    p.stdin.write(b'VERIFIED_LISTING = '+repr(listing).encode()+b'\n'+script.read_bytes())
    p.stdin.close()
    count=0
    received=0
    with tarfile.open(fileobj=p.stdout,mode='r|') as tar:
        for member in tar:
            received+=member.size
            if received>limit or member.size>256*1024**2 or count>=5000:
                p.terminate()
                raise ValueError('Limite de collecte dépassée')
            dest=(OUT/member.name).resolve()
            if not dest.is_relative_to(OUT.resolve()) or not member.isfile():
                raise ValueError(member.name)
            dest.parent.mkdir(parents=True,exist_ok=True)
            with dest.open('xb') as f:
                source=tar.extractfile(member)
                while data:=source.read(1024*1024):
                    f.write(data)
            count+=1
            if count%100==0:
                print('Artefacts reçus :',count,flush=True)
    rc=p.wait()
with (OUT/'journaux/commandes.jsonl').open('a') as f:
    f.write(json.dumps(dict(start_utc=start,end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),argv=argv,stdin_script=str(script.relative_to(ROOT)),returncode=rc,files=count))+'\n')
if rc:
    raise SystemExit(rc)
print('Export terminé',count)
