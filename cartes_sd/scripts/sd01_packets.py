#!/usr/bin/env python3
"""Contrôle des DTS/PTS d'origine pour les avertissements du muxeur null.
N'effectue aucune modification du média. Journaux JSON et empreinte de chaque
sortie de paquets, sans conserver les données de paquets elles-mêmes.
"""
import concurrent.futures
import hashlib
import json
import subprocess
from sd01_collect import OUT

quality=json.loads((OUT/'inventaires/qualite-decodage.json').read_text())
targets=[r for r in quality['entries'] if 'avertissement_sortie_null_DTS' in r['categories']]
def check(r):
    p=next((OUT/'prive/extraits').glob(r['inode']+'_*.mp4'))
    args=['ffprobe','-v','error','-select_streams','v:0','-show_packets','-show_entries','packet=pts,dts','-of','json',str(p)]
    run=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    data=json.loads(run.stdout)['packets']; summary={}
    for field in ('dts','pts'):
        values=[int(x[field]) for x in data if field in x]
        diffs=[y-x for x,y in zip(values,values[1:])]
        summary[field]=dict(count=len(values),nonincreasing=sum(d<=0 for d in diffs),minimum_delta=min(diffs,default=None),maximum_delta=max(diffs,default=None))
    return dict(inode=r['inode'],path=r['path'],argv=args,returncode=run.returncode,stderr=run.stderr.decode(),packets=len(data),raw_output_sha256=hashlib.sha256(run.stdout).hexdigest(),summary=summary)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results=list(pool.map(check,targets))
with (OUT/'inventaires/controle-paquets-DTS.json').open('x') as f:json.dump(results,f,indent=2)
print('Fichiers contrôlés',len(results),'DTS non croissants',sum(r['summary']['dts']['nonincreasing'] for r in results),'PTS non croissants',sum(r['summary']['pts']['nonincreasing'] for r in results))
