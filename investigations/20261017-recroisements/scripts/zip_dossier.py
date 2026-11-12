#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
base=Path('/home/sansforensics/analysis/complement-20261017/zip');dest=base/'comparaison-dossier.json'
if dest.exists():raise SystemExit('Destination existante')
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
res=[];seen={}
for a in json.loads((base/'results.json').read_text()):
 for e in a['entries']:
  if 'sha256' not in e:continue
  p=Path('/mnt/windows/L16B')/e['name']
  if not p.is_relative_to('/mnt/windows/L16B/GDRIVE'):raise ValueError('Chemin inattendu')
  if str(p) not in seen:
   seen[str(p)]={'path':str(p),'sha256_before':h(p) if p.is_file() else None}
  res.append({'archive':Path(a['path']).name,'member':e['name'],'matches_folder':e['sha256']==seen[str(p)]['sha256_before']})
for s in seen.values():
 p=Path(s['path']);s['sha256_after']=h(p) if p.is_file() else None;s['unchanged']=s['sha256_before']==s['sha256_after']
d={'comparisons':res,'sources':list(seen.values()),'unique_files':len(seen),'all_matches':all(x['matches_folder'] for x in res),'all_unchanged':all(x['unchanged'] for x in seen.values())};dest.write_text(json.dumps(d,ensure_ascii=False,indent=2));print({k:d[k] for k in ['unique_files','all_matches','all_unchanged']})
