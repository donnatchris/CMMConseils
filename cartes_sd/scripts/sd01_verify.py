#!/usr/bin/env python3
"""Contrôles de livraison : empreintes, contre-lecture FAT/TSK et décodages.
Produit des dérivés nouveaux ; ne modifie ni les collectes ni les sources.
"""
import collections
import csv
import datetime as dt
import hashlib
import json
from sd01_collect import OUT

raw=json.loads((OUT/'inventaires/lecture-fat-independante-v2.json').read_text())
export=json.loads((OUT/'inventaires/export.json').read_text())
inv={r['inode']:r for r in csv.DictReader((OUT/'inventaires/inventaire.csv').open())}
checks=[]
for e in export['entries']:
    if 'artifact' not in e:continue
    p=OUT/e['artifact'];h=hashlib.sha256(p.read_bytes()).hexdigest()
    checks.append(dict(inode=e['inode'],artifact=e['artifact'],size=p.stat().st_size,sha256=h,hash_matches_export=h==e['sha256'],size_matches_export=p.stat().st_size==e['extracted_size']))
fatrows=[];mismatches=[]
for e in raw['entries']:
    if e['after_end_marker'] or e['name'] in ('.','..'):continue
    inode=str(3+(e['absolute_entry_offset']-raw['geometry']['data_absolute_offset'])//32)
    row=dict(inode=inode,**e);fatrows.append(row)
    if inode not in inv:mismatches.append(dict(inode=inode,error='absent inventaire TSK'))
    elif not e['attributes']&16 and int(inv[inode]['declared_size'])!=e['size']:mismatches.append(dict(inode=inode,error='taille différente'))
with (OUT/'inventaires/entrees-fat-brutes.csv').open('x',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(fatrows[0]));w.writeheader();w.writerows(fatrows)
decoded={e['inode']:dict(engine='SIFT FFmpeg 6.1.1',returncode=e['decode']['returncode'],stderr_bytes=e['decode']['warnings_bytes']) for e in export['entries'] if 'decode' in e}
for e in json.loads((OUT/'inventaires/decodages-complementaires.json').read_text()):
    decoded[e['inode']]=dict(engine='hôte FFmpeg 8.0.1',returncode=e['returncode'],stderr_bytes=len(e['stderr'].encode()))
for line in (OUT/'inventaires/decodage-complement-local.jsonl').read_text().splitlines():
    e=json.loads(line);decoded[e['inode']]=dict(engine='hôte FFmpeg 8.0.1',returncode=e['returncode'],stderr_bytes=e['stderr_bytes'])
active={e['inode'] for e in export['entries'] if e.get('artifact','').endswith('.mp4') and not e['deleted']}
scan=json.loads((OUT/'inventaires/scan-non-alloue-v2.json').read_text())
residual_hashes=[]
for r in scan['nonzero_clusters']:
    p=OUT/'prive/residus'/f"{r['cluster']}.bin"
    residual_hashes.append(dict(cluster=r['cluster'],hash_matches_scan=hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256']))
result=dict(extraction_count=len(checks),extraction_checks=checks,fat_tsk_comparison=dict(raw_entries=len(fatrows),tsk_entries=len(inv),mismatches=mismatches),decoded_video_count=len(active&decoded.keys()),not_decoded=sorted(active-decoded.keys()),decode_nonzero=[i for i in active if decoded.get(i,{}).get('returncode')],decode_results=decoded,residual_count=len(residual_hashes),residual_hash_mismatches=[r for r in residual_hashes if not r['hash_matches_scan']],segment_hashes_unchanged=(OUT/'journaux/segments-sha256.txt').read_bytes()==(OUT/'journaux/segments-sha256-fin.txt').read_bytes())
with (OUT/'inventaires/controle-final.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
assert all(r['hash_matches_export'] and r['size_matches_export'] for r in checks)
assert not mismatches and not result['not_decoded'] and not result['decode_nonzero'] and not result['residual_hash_mismatches'] and result['segment_hashes_unchanged']
print('Extraits vérifiés',len(checks),'vidéos décodées',result['decoded_video_count'],'résidus vérifiés',len(residual_hashes),'écarts',len(mismatches))
