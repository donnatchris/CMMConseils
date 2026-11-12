#!/usr/bin/env python3
"""Empreinte finale de tous les artefacts de campagne, avec dépendances."""
import datetime as dt,hashlib,json
from sd02_collect import OUT,ROOT
manifest=OUT/'manifest-sha256.txt';info=OUT/'manifest-info.json';excluded={manifest,info};paths={p for p in OUT.rglob('*') if p.is_file() and p not in excluded};paths.add(ROOT/'cartes_sd/analyse-cartes_sd-SD-02.md');paths.update((ROOT/'cartes_sd/scripts').glob('sd02_*.py'))
for rel in ['cartes_sd/scripts/sd01_mp4.py','cartes_sd/scripts/sd01_collect.py','docs/mail.txt','remise-documents/attestation-de-remise.md','cartes_sd/analyse-cartes_sd.md','cartes_sd/recherche-SD-01/20261016-complement/sources/contexte-et-observations.md','.gitignore']:
 p=ROOT/rel
 if p.is_file():paths.add(p)
rows=[];total=0
for p in sorted(paths):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024**2):h.update(b)
 rows.append(h.hexdigest()+'  '+str(p.relative_to(ROOT)));total+=p.stat().st_size
with manifest.open('x') as f:f.write('\n'.join(rows)+'\n')
with info.open('x') as f:json.dump(dict(created_utc=dt.datetime.now(dt.timezone.utc).isoformat(),files=len(rows),bytes=total,manifest=str(manifest.relative_to(ROOT)),manifest_sha256=hashlib.sha256(manifest.read_bytes()).hexdigest(),excluded=[str(p.relative_to(ROOT)) for p in excluded],note='Empreintes de preuves dérivées, pas une nouvelle acquisition physique. Médias privés exclus de Git mais conservés dans le projet.'),f,ensure_ascii=False,indent=2)
print(len(rows),'fichiers',total,'octets')
