#!/usr/bin/env python3
"""Contrôles des artefacts SD-03, sans nouvelle lecture des sources."""
import hashlib,json,re,subprocess
from sd03_collect import OUT,ROOT
checks=[]
def verify(label,ok):
 checks.append(dict(check=label,ok=bool(ok)))
 if not ok:raise AssertionError(label)
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024**2):h.update(b)
 return h.hexdigest()
def load(n):return json.loads((OUT/'inventaires'/n).read_text())
def artifact(r,label):
 if r.get('artifact') and r.get('sha256'):verify(label+' '+r['artifact'],digest(OUT/r['artifact'])==r['sha256'])
idx=load('medias-index.json');s=load('synthese-medias.json')
verify('Tous fichiers réguliers analysés',idx['all_entries']==2437 and len(idx['entries'])==2437)
for r in idx['entries']:
 if not r['deleted']:verify('Lecture active '+r['inode'],not r.get('error') and r['read_size']==r['size'])
 artifact(r,'Média')
verify('Contrôles icat concordants',not s['icat_crosscheck_mismatch'])
for r in load('priorite-index.json')['entries']:artifact(r,'Priorité')
for name in ['structures-index.json','complements-index.json','apercus-index.json','apercus-lineaires-index.json']:
 for r in load(name):artifact(r,name)
for r in load('frames-cibles.json'):
 verify('Inventaire images '+r['inode'],digest(OUT/r['frames_artifact'])==r['frames_sha256']);artifact(r['preview'],'Dernier aperçu')
obs=load('observations-visuelles.json')['observations'];verify('23 images effectivement observées',len(obs)==23)
for r in obs:artifact(r,'Observation visuelle')
tail=load('recuperation-apres-eof.json');artifact(tail,'Récupération');verify('Fragment validé',tail['accepted'] and tail['decode']['returncode']==0 and tail['decode']['stderr_bytes']==0)
for r in tail['previews']:artifact(r,'Aperçu récupération')
scan=load('espace-libre.json');nonzero={r['cluster']:r for r in scan['nonzero_clusters']};h=hashlib.sha256();count=0;zero=bytes(16384)
for first,last in scan['free_runs']:
 for c in range(first,last+1):
  r=nonzero.get(c)
  if r:
   b=(OUT/'prive/residus'/f'{c}.bin').read_bytes();verify('Cluster libre '+str(c),len(b)==16384 and hashlib.sha256(b).hexdigest()==r['sha256'])
  else:b=zero
  h.update(b);count+=1
verify('Flux libre complet reconstitué',count==471351==scan['free_cluster_count'] and h.hexdigest()==scan['free_stream_sha256'])
verify('Tous clusters non nuls classés',len(load('residus-classes.json')['items'])==len(nonzero)==11577)
verify('FAT égales',(OUT/'structures/fat1.bin').read_bytes()==(OUT/'structures/fat2.bin').read_bytes())
initial=(OUT/'journaux/segments-sha256.txt').read_bytes();verify('12 segments inchangés',initial==(OUT/'journaux/segments-sha256-fin.txt').read_bytes() and len(initial.splitlines())==12)
report=ROOT/'cartes_sd/analyse-cartes_sd-SD-03.md';text=report.read_text();verify('Rapport final',"Investigation en cours" not in text and 'État intermédiaire vérifié' not in text)
missing=[]
for target in re.findall(r'\]\(([^)]+)\)',text):
 if '://' in target or target.startswith('#'):continue
 if not (report.parent/target.split('#')[0]).resolve().exists():missing.append(target)
verify('Liens locaux du rapport',not missing)
private=[f for f in (OUT/'prive').rglob('*') if f.is_file()]+list((OUT/'structures').glob('*.bin'))
p=subprocess.run(['git','check-ignore','--stdin'],cwd=ROOT,input='\n'.join(str(f.relative_to(ROOT)) for f in private)+'\n',text=True,capture_output=True)
verify('Médias et structures exclus de Git',set(p.stdout.splitlines())=={str(f.relative_to(ROOT)) for f in private})
with (OUT/'inventaires/controle-final.json').open('x') as f:json.dump(dict(passed=True,checks=len(checks),ignored_private_files=len(private),missing_links=missing,details=checks),f,ensure_ascii=False,indent=2)
print('Contrôles réussis :',len(checks))
