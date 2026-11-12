#!/usr/bin/env python3
"""Valide le dossier et écrit un manifeste neuf, sans modifier les preuves."""
import ast,hashlib,json,re
from pathlib import Path
D=Path(__file__).resolve().parents[1];R=D.parents[1]
manifest=D/'SHA256SUMS'
if manifest.exists():raise SystemExit('Manifeste existant : conserver avant nouvelle finalisation')
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
checks={};bad=[]
for p in (D/'scripts').glob('*.py'):ast.parse(p.read_text())
checks['python_syntax']=True
for p in [D/'README.md',D/'compte-rendu.md']:
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' not in target and not (p.parent/target.split('#')[0]).exists():bad.append([str(p),target])
checks['links']=not bad
checks['independent_checks']=json.loads((D/'resultats/verification-finale.json').read_text())['all_pass']
checks['reproducible']=all(x['identical_json'] for x in json.loads((D/'resultats/reproduction.json').read_text()))
for rel in ['resultats/sift/resultats/sources.json','resultats/sift/ntfs/sources.json']:
 checks[rel]=all(x['sha256_before']==x['sha256_after'] for x in json.loads((D/rel).read_text()))
checks['sift_no_errors']=json.loads((D/'resultats/sift/resultats/errors.json').read_text())==[]
checks['ntfs_completed']=json.loads((D/'resultats/sift/ntfs/summary.json').read_text())['returncode']==0
checks['zip_sources_unchanged']=all(x['unchanged'] for x in json.loads((D/'resultats/sift/zip/results.json').read_text()))
c=json.loads((D/'resultats/sift/zip/comparaison-dossier.json').read_text());checks['zip_folder_matches']=c['all_matches'] and c['all_unchanged'] and c['unique_files']==93
keys=re.findall(r'\b(?:\d{6}-){7}\d{6}\b',(R/'docs/codes-d-acces.md').read_text())
checks['no_complete_recovery_key']=not any(any(k.encode() in p.read_bytes() for k in keys) for p in D.rglob('*') if p.is_file())
checks['no_unfinished_marker']='<!-- NTFS_COMPLEMENT -->' not in (D/'compte-rendu.md').read_text()
(D/'resultats/controle-livraison.json').write_text(json.dumps({'checks':checks,'broken_links':bad,'all_pass':all(checks.values())},indent=2))
if not all(checks.values()):raise SystemExit('Contrôle échoué : consulter controle-livraison.json')
reports=[]
for p in (D/'rapports-avant').rglob('*.md'):
 rel=p.relative_to(D/'rapports-avant');reports.append({'path':str(rel),'before_sha256':h(p),'after_sha256':h(R/rel)})
(D/'resultats/rapports-modifies.json').write_text(json.dumps(reports,indent=2))
files=sorted(p for p in D.rglob('*') if p.is_file())
manifest.write_text(''.join(f'{h(p)}  {p.relative_to(D)}\n' for p in files))
for p in files+[manifest]:p.chmod(0o600)
print(json.dumps({'checks':len(checks),'all_pass':True,'manifest_files':len(files),'updated_reports':len(reports)}))
