#!/usr/bin/env python3
"""Contrôles matériels des artefacts dérivés et de la cohérence du rapport."""
import hashlib,json,pathlib,re,subprocess
from sd02_collect import OUT,ROOT
checks=[]
def verify(label,condition):
 checks.append(dict(check=label,ok=bool(condition)))
 if not condition:raise AssertionError(label)
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024**2):h.update(b)
 return h.hexdigest()
idx=json.loads((OUT/'inventaires/medias-index.json').read_text());s=json.loads((OUT/'inventaires/synthese-medias.json').read_text());verify('Tous les fichiers réguliers inventoriés analysés',idx['all_entries']==3632 and len(idx['entries'])==3632)
verify('Aucune erreur de lecture active',not any(r.get('error') for r in idx['entries'] if not r['deleted']))
for r in idx['entries']:
 if not r['deleted']:verify('Taille active '+r['inode'],r['read_size']==r['size'])
 if r.get('artifact'):verify('Extraction '+r['inode'],digest(OUT/r['artifact'])==r['sha256'])
verify('Tous contrôles icat actifs concordants',not s['icat_crosscheck_mismatch'])
for name in ['supplement','ecarts']:
 for r in json.loads((OUT/'inventaires'/f'{name}-index.json').read_text())['entries']:
  verify(name+' decode '+r['inode'],r.get('decode',{}).get('returncode')==0 and r['decode']['stderr_bytes']==0)
  verify(name+' extraction '+r['inode'],digest(OUT/r['artifact'])==r['sha256'])
  for preview in r.get('previews',[]):verify(name+' aperçu '+preview['artifact'],digest(OUT/preview['artifact'])==preview['sha256'])
for item in ['structures-index','complements-index','apercus-index']:
 for r in json.loads((OUT/'inventaires'/f'{item}.json').read_text()):
  verify(item+' '+r['artifact'],digest(OUT/r['artifact'])==r['sha256'])
for r in json.loads((OUT/'inventaires/recuperations.json').read_text())['entries']:
 verify('Récupération '+r['inode'],digest(OUT/r['artifact'])==r['sha256'] and not r['decode']['returncode'] and not r['decode']['stderr_bytes'] and not r['structure']['errors'])
for name in ['recuperation-fragment-final','reconstructions-temporaires']:
 d=json.loads((OUT/'inventaires'/f'{name}.json').read_text());rs=d['entries'] if 'entries'in d else[d]
 for r in rs:verify(name+' '+r['artifact'],digest(OUT/r['artifact'])==r['sha256'])
scan=json.loads((OUT/'inventaires/espace-libre.json').read_text());h=hashlib.sha256()
for r in scan['nonzero_clusters']:
 b=(OUT/'prive/residus'/f"{r['cluster']}.bin").read_bytes();verify('Cluster libre '+str(r['cluster']),hashlib.sha256(b).hexdigest()==r['sha256']);h.update(b)
verify('Flux libre complet',scan['free_cluster_count']==len(scan['nonzero_clusters']) and h.hexdigest()==scan['free_stream_sha256'])
verify('FAT égales',(OUT/'structures/fat1.bin').read_bytes()==(OUT/'structures/fat2.bin').read_bytes())
verify('15 segments inchangés',(OUT/'journaux/segments-sha256.txt').read_bytes()==(OUT/'journaux/segments-sha256-fin.txt').read_bytes() and len((OUT/'journaux/segments-sha256.txt').read_text().splitlines())==15)
report=ROOT/'cartes_sd/analyse-cartes_sd-SD-02.md';text=report.read_text();verify('Rapport final sans état intermédiaire','Investigation en cours'not in text and 'État intermédiaire vérifié'not in text)
missing=[]
for target in re.findall(r'\]\(([^)]+)\)',text):
 if '://'in target or target.startswith('#'):continue
 path=(report.parent/target.split('#')[0]).resolve()
 if not path.exists():missing.append(target)
verify('Liens locaux du rapport',not missing)
private=list((OUT/'prive').rglob('*.mp4'))+list((OUT/'structures').glob('*.bin'))
p=subprocess.run(['git','check-ignore','--stdin'],cwd=ROOT,input='\n'.join(str(f.relative_to(ROOT)) for f in private)+'\n',text=True,capture_output=True)
verify('Médias et structures exclus de Git',set(p.stdout.splitlines())=={str(f.relative_to(ROOT)) for f in private})
with (OUT/'inventaires/controle-final.json').open('x') as f:json.dump(dict(passed=True,checks=len(checks),media_files_ignored=len(private),missing_links=missing,details=checks),f,ensure_ascii=False,indent=2)
print('Contrôles réussis :',len(checks))
