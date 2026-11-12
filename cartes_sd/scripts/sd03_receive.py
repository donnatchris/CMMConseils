#!/usr/bin/env python3
"""Réception de tar SSH bornée et contrôlée, toutes destinations dans OUT.
Usage: SCRIPT SORTIE-STDERR [PARAMETRES-JSON]. Le script est transmis en mémoire.
Les membres tar sont relatifs, réguliers, bornés, sans écrasement ni liens.
"""
import datetime as dt
import hashlib
import json
import pathlib
import shutil
import subprocess
import sys
import tarfile
from sd03_collect import OUT,ROOT,SSH,IMAGE

def main():
    source=pathlib.Path(sys.argv[1]).resolve()
    label=sys.argv[2]
    if not label.replace('-','').isalnum():raise ValueError('Label invalide')
    params=json.loads(pathlib.Path(sys.argv[3]).read_text()) if len(sys.argv)>3 else {}
    maxbytes=int(params.get('tar_max_bytes',6*1024**3));margin=8*1024**3
    if not 0<maxbytes<=6*1024**3 or shutil.disk_usage(OUT).free<maxbytes+margin:raise ValueError('Plafond ou réserve disque')
    code=source.read_bytes()
    # Fonctions pures MP4 utilisées sur les données, pas le point d'entrée SD-01.
    parser=(ROOT/'cartes_sd/scripts/sd01_mp4.py').read_text().split('\ndef main():',1)[0].replace('from sd01_collect import OUT','')
    payload=('PARAMS = '+repr(params)+'\n').encode()+parser.encode()+b'\n'+code
    argv=SSH+['sudo -n python3 - '+IMAGE]
    start=dt.datetime.now(dt.timezone.utc).isoformat();received=0;count=0
    with (OUT/'journaux'/f'{label}.stderr').open('xb') as err:
        p=subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err)
        # stdin contient uniquement du code/paramètres, jamais une extraction.
        p.stdin.write(payload);p.stdin.close()
        try:
            with tarfile.open(fileobj=p.stdout,mode='r|') as tar:
                for member in tar:
                    dest=(OUT/member.name).resolve()
                    if not dest.is_relative_to(OUT.resolve()) or not member.isfile() or member.size>256*1024**2:raise ValueError('Membre hors périmètre')
                    received+=member.size;count+=1
                    if received>maxbytes or count>150000:raise ValueError('Plafond de collecte')
                    dest.parent.mkdir(exist_ok=True,parents=True)
                    with dest.open('xb') as f:
                        stream=tar.extractfile(member)
                        while data:=stream.read(1024**2):f.write(data)
                    if count%250==0:print(label,'membres',count,'octets',received,flush=True)
            rc=p.wait()
        except BaseException:
            p.terminate();p.wait();raise
    with (OUT/'journaux/commandes.jsonl').open('a') as f:
        f.write(json.dumps(dict(start_utc=start,end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),argv=argv,script=str(source.relative_to(ROOT)),script_sha256=hashlib.sha256(code).hexdigest(),pure_mp4_parser_sha256=hashlib.sha256(parser.encode()).hexdigest(),parameters=params,returncode=rc,received_files=count,received_bytes=received),ensure_ascii=False)+'\n')
    if rc:raise SystemExit(rc)
    print('Collecte terminée',label,count,received)

if __name__=='__main__':main()
