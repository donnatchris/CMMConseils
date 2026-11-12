#!/usr/bin/env python3
"""Collecte SSH en lecture seule ; stdout/stderr et commandes conservés localement.
Exécuter depuis la racine du dépôt : python3 cartes_sd/scripts/sd01_collect.py PHASE
Les scripts distants sont transmis sur stdin, jamais enregistrés sur FORENSIC.
"""
import datetime as dt
import json
import pathlib
import os
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
RUN = os.environ.get('SD01_RUN','20261015')
if not re.fullmatch(r'[0-9]{8}[a-z0-9_-]*',RUN):
    raise ValueError('SD01_RUN doit être un nom de campagne, pas un chemin')
OUT = ROOT / 'cartes_sd/recherche-SD-01' / RUN
IMAGE = '/mnt/ewf-sd01/ewf1'
EWF = '/media/shared/forensic/SADEDINE-2026/ANALYSES/SD-01/SD01.E01'
SSH = ['ssh', '-F', '/home/chris/.ssh/config', '-o', 'BatchMode=yes', 'sift']

def remote(command, target, stdin=None):
    dest = OUT / target
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Refuser d'écraser une collecte existante.
    with dest.open('xb') as stdout, dest.with_suffix(dest.suffix+'.stderr').open('xb') as stderr:
        start = dt.datetime.now(dt.timezone.utc).isoformat()
        proc = subprocess.run(SSH + [command], input=stdin, stdout=stdout, stderr=stderr)
    rec = dict(start_utc=start, end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
               argv=SSH+[command], stdin_script=stdin.decode() if stdin else None,
               output=str(dest.relative_to(ROOT)), returncode=proc.returncode)
    with (OUT/'journaux/commandes.jsonl').open('a') as f:
        f.write(json.dumps(rec, ensure_ascii=False)+'\n')
    print(target, proc.returncode, flush=True)
    return proc.returncode

def main():
    phase = sys.argv[1]
    if phase == 'integrite':
        remote(f'sudo -n ewfverify -q {EWF}', 'journaux/ewfverify.txt')
        remote('sha256sum '+EWF+' '+EWF.replace('.E01','.E02'), 'journaux/segments-sha256.txt')
        remote(f'sudo -n sha256sum {IMAGE}', 'journaux/media-sha256.txt')
    elif phase == 'inventaire':
        remote("python3 -c 'import platform,shutil,subprocess,json; names=[\"ewfverify\",\"ewfinfo\",\"ewfmount\",\"mmls\",\"fsstat\",\"fls\",\"istat\",\"icat\",\"blkls\",\"mactime\",\"ffprobe\",\"ffmpeg\",\"photorec\"]; print(platform.platform()); print(subprocess.getoutput(\"dpkg-query -W sleuthkit libewf-tools ffmpeg testdisk python3\")); print(json.dumps({n:shutil.which(n) for n in names}))'", 'journaux/outils.txt')
        remote(f'sudo -n mmls {IMAGE}', 'journaux/mmls.txt')
        remote(f'sudo -n fsstat -o 8192 {IMAGE}', 'journaux/fsstat.txt')
        remote(f'sudo -n fls -o 8192 -r -p {IMAGE}', 'inventaires/fls.txt')
        remote(f'sudo -n fls -o 8192 -r -d -p {IMAGE}', 'inventaires/fls-supprimes.txt')
        remote(f'sudo -n fls -z UTC -o 8192 -r -p -m / {IMAGE}', 'inventaires/timeline.body')
        remote(f'sudo -n ewfinfo {EWF}', 'journaux/ewfinfo.txt')
        remote("stat /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-01/SD01.E0*; findmnt /media/shared; sudo -n stat /mnt/ewf-sd01/ewf1; ls -la /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-01/", 'journaux/provenance.txt')
    elif phase == 'script':
        remote('sudo -n python3 - '+IMAGE, sys.argv[3], pathlib.Path(sys.argv[2]).read_bytes())
    elif phase == 'mactime':
        remote('mactime -b /dev/stdin -z UTC -d', 'inventaires/timeline-mactime.csv', (OUT/'inventaires/timeline.body').read_bytes())
    elif phase == 'contexte':
        remote('cat /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-01/SD01.info', 'journaux/SD01.info.txt')
        remote('find /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-01/RECUPERATION /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-01/RECUPERATION.1 -maxdepth 3 -type f -printf "%s %p\\n"', 'journaux/inventaire-travaux-anterieurs.txt')
    elif phase == 'allocation':
        raw=(OUT/'inventaires/lecture-fat-independante-v2.json').read_bytes()
        code=b'RAW_VERIFIED = '+repr(raw).encode()+b'\n'+(ROOT/'cartes_sd/scripts/sd01_allocation_remote.py').read_bytes()
        remote('sudo -n python3 - '+IMAGE,'inventaires/audit-allocation-v2.json',code)
    elif phase == 'final':
        remote('sha256sum '+EWF+' '+EWF.replace('.E01','.E02'), 'journaux/segments-sha256-fin.txt')
        remote('stat '+EWF+' '+EWF.replace('.E01','.E02'), 'journaux/segments-stat-fin.txt')
    else:
        raise SystemExit('Phase inconnue')

if __name__ == '__main__':
    main()
