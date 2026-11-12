#!/usr/bin/env python3
"""Décodage complet des vidéos hors sélection SIFT, sur les copies locales.
Quatre processus maximum, un thread de décodage chacun. Résultats incrémentaux.
"""
import concurrent.futures
import json
import subprocess
from sd01_collect import OUT

export=json.loads((OUT/'inventaires/export.json').read_text())
complement=json.loads((OUT/'inventaires/decodages-complementaires.json').read_text())
done={r['inode'] for r in complement}
targets=[e for e in export['entries'] if e.get('artifact','').endswith('.mp4') and not e['deleted'] and 'decode' not in e and e['inode'] not in done]
logs=OUT/'journaux/decodage-complement-local'
logs.mkdir(exist_ok=True)
def check(e):
    args=['ffmpeg','-v','warning','-threads','1','-i',str(OUT/e['artifact']),'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-']
    try:
        p=subprocess.run(args,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=600)
        err=p.stderr;rc=p.returncode
    except subprocess.TimeoutExpired as exc:
        err=(exc.stderr or b'')+b'\nTIMEOUT 600s';rc=124
    target=logs/(e['inode']+'.txt')
    with target.open('xb') as f:f.write(err)
    return dict(inode=e['inode'],path=e['path'],argv=args,returncode=rc,stderr_bytes=len(err),log=str(target.relative_to(OUT)))
with (OUT/'inventaires/decodage-complement-local.jsonl').open('x') as result:
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures=[pool.submit(check,e) for e in targets]
        for i,future in enumerate(concurrent.futures.as_completed(futures),1):
            r=future.result();result.write(json.dumps(r)+'\n');result.flush()
            if i%50==0:print('Vidéos supplémentaires décodées',i,'/',len(targets),flush=True)
print('Terminé',len(targets))
