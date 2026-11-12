#!/usr/bin/env python3
"""Collecte SD-02 par SSH sift. Toutes les sorties persistantes dans le projet.
Usage: python3 cartes_sd/scripts/sd02_collect.py PHASE [SCRIPT SORTIE]
Les scripts distants sont transmis sur stdin, sans fichier distant persistant.
"""
import datetime as dt
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT=pathlib.Path(__file__).resolve().parents[2]
RUN=os.environ.get('SD02_RUN','20261016')
if not re.fullmatch(r'[0-9]{8}[a-z0-9_-]*',RUN):raise ValueError('Nom de campagne invalide')
OUT=ROOT/'cartes_sd/recherche-SD-02'/RUN
IMAGE='/mnt/ewf-sd02/ewf1'
EWF='/media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/SD02.E01'
SSH=['ssh','-F','/home/chris/.ssh/config','-o','BatchMode=yes','sift']

def remote(command,target,stdin=None):
    dest=(OUT/target).resolve()
    if not dest.is_relative_to(OUT.resolve()):raise ValueError('Destination hors projet')
    dest.parent.mkdir(exist_ok=True,parents=True)
    start=dt.datetime.now(dt.timezone.utc).isoformat()
    with dest.open('xb') as stdout,dest.with_suffix(dest.suffix+'.stderr').open('xb') as err:
        p=subprocess.run(SSH+[command],input=stdin,stdout=stdout,stderr=err)
    (OUT/'journaux').mkdir(exist_ok=True)
    with (OUT/'journaux/commandes.jsonl').open('a') as f:
        f.write(json.dumps(dict(start_utc=start,end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),argv=SSH+[command],stdin_script=stdin.decode() if stdin else None,output=str(dest.relative_to(ROOT)),returncode=p.returncode),ensure_ascii=False)+'\n')
    print(target,p.returncode,flush=True)
    if p.returncode:raise SystemExit(p.returncode)

def main():
    phase=sys.argv[1]
    if phase=='integrite':remote(f'sudo -n ewfverify -q -d sha256 {EWF}','journaux/ewfverify-sha256.txt')
    elif phase in ('segments','final'):
        suffix='-fin' if phase=='final' else ''
        remote('sha256sum /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/SD02.E[0-9][0-9]',f'journaux/segments-sha256{suffix}.txt')
    elif phase=='etat':
        remote('cat /media/shared/AGENTS.md; cat /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/SD02.info; stat /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/SD02.E[0-9][0-9]; sudo -n stat '+IMAGE+'; findmnt /media/shared','journaux/provenance.txt')
        remote(f'sudo -n ewfinfo {EWF}','journaux/ewfinfo.txt')
        remote(f'sudo -n mmls {IMAGE}','journaux/mmls.txt')
        remote(f'sudo -n fsstat -o 8192 {IMAGE}','journaux/fsstat.txt')
        remote("python3 -c 'import platform,subprocess,json,shutil; print(platform.platform()); print(subprocess.getoutput(\"dpkg-query -W sleuthkit libewf-tools ffmpeg testdisk python3\")); print(json.dumps({x:shutil.which(x) for x in [\"fls\",\"istat\",\"icat\",\"ffprobe\",\"ffmpeg\",\"photorec\",\"blkls\",\"mactime\"]}))'",'journaux/outils.txt')
    elif phase=='fls':remote(f'sudo -n fls -o 8192 -r -p {IMAGE}','inventaires/fls.txt')
    elif phase=='body':remote(f'sudo -n fls -z UTC -o 8192 -r -p -m / {IMAGE}','inventaires/timeline.body')
    elif phase=='mactime':remote('mactime -b /dev/stdin -z UTC -d','inventaires/timeline-mactime.csv',(OUT/'inventaires/timeline.body').read_bytes())
    elif phase=='script':remote('sudo -n python3 - '+IMAGE,sys.argv[3],pathlib.Path(sys.argv[2]).read_bytes())
    else:raise ValueError('Phase inconnue')

if __name__=='__main__':main()
