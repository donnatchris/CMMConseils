#!/usr/bin/env python3
"""Temps des paquets des 37 clips du 15 : réemploi des 6 contrôles existants,
FFprobe sans décodage pour les 31 autres, sur copies locales seulement."""
import hashlib
import json
import subprocess
import pathlib
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parents[2]
OLD=ROOT/'cartes_sd/recherche-SD-01/20261015'
OUT=ROOT/'cartes_sd/recherche-SD-01/20261016-complement'
prior={r['inode']:r for r in json.loads((OLD/'inventaires/controle-paquets-DTS.json').read_text())}
media=json.loads((OUT/'inventaires/medias-cibles.json').read_text())
rows=[]
for m in media:
    if '/20241015/' not in m['path']:continue
    inode=m['inode'];base=Fraction(next(s['time_base'] for s in m['streams'] if s['codec_type']=='video'))
    if inode in prior:
        r=dict(prior[inode]);r['method']='Réemploi du contrôle du 15/10/2026'
    else:
        src=next((OLD/'prive/extraits').glob(inode+'_*.mp4'))
        args=['ffprobe','-v','error','-select_streams','v:0','-show_packets','-show_entries','packet=pts,dts','-of','json',str(src)]
        p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        if p.returncode:raise RuntimeError(p.stderr.decode())
        packets=json.loads(p.stdout)['packets'];summary={}
        for field in ('pts','dts'):
            values=[int(x[field]) for x in packets if field in x];delta=[b-a for a,b in zip(values,values[1:])]
            summary[field]=dict(count=len(values),nonincreasing=sum(d<=0 for d in delta),minimum_delta=min(delta,default=None),maximum_delta=max(delta,default=None))
        r=dict(inode=inode,path=m['path'],method='FFprobe local complémentaire, sans décodage',argv=args,returncode=p.returncode,stderr=p.stderr.decode(),packets=len(packets),raw_output_sha256=hashlib.sha256(p.stdout).hexdigest(),summary=summary)
    r['time_base']=str(base)
    r['max_dts_gap_seconds']=float(base*r['summary']['dts']['maximum_delta'])
    rows.append(r)
result=dict(reused_count=sum('Réemploi' in r['method'] for r in rows),new_ffprobe_count=sum('Réemploi' not in r['method'] for r in rows),total=len(rows),dts_nonincreasing=sum(r['summary']['dts']['nonincreasing'] for r in rows),pts_nonincreasing=sum(r['summary']['pts']['nonincreasing'] for r in rows),max_intrafile_dts_gap_seconds=max(r['max_dts_gap_seconds'] for r in rows),ffprobe_version=subprocess.check_output(['ffprobe','-version']).decode().splitlines()[0],entries=rows)
with (OUT/'inventaires/paquets-video-20241015.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='entries'},indent=2))
