#!/usr/bin/env python3
"""Relecture de chaque empreinte finale ; mise à jour du seul index exclu."""
import datetime as dt,hashlib,json
from sd03_collect import OUT,ROOT
manifest=OUT/'manifest-sha256.txt';count=0
for line in manifest.read_text().splitlines():
 expected,name=line.split('  ',1);p=(ROOT/name).resolve()
 if not p.is_relative_to(ROOT):raise ValueError('Chemin hors projet')
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024**2):h.update(b)
 if h.hexdigest()!=expected:raise AssertionError(name)
 count+=1
p=OUT/'manifest-info.json';info=json.loads(p.read_text());info.update(verification_utc=dt.datetime.now(dt.timezone.utc).isoformat(),verified_files=count,verification_success=count==info['files']);p.write_text(json.dumps(info,ensure_ascii=False,indent=2))
print('Manifeste intégralement vérifié :',count,'fichiers')
