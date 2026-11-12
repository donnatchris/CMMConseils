#!/usr/bin/env python3
"""Exécution SIFT : décodage du journal NTFS, empreintes avant/après."""
import hashlib,json,os,subprocess,re,collections
from pathlib import Path
base=Path('/home/sansforensics/analysis/complement-20261017'); out=base/'ntfs';out.mkdir(exist_ok=False)
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
src=[Path('/mnt/windows/$MFT'),Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014/raw/$LogFile')]
assert 'ro' in subprocess.check_output(['findmnt','-rn','-o','OPTIONS','/mnt/windows'],text=True).strip().split(',')
before=[{'path':str(p),'size':p.stat().st_size,'sha256_before':h(p)} for p in src]
env=dict(os.environ,PYTHONPATH=str(base/'lib'))
with (out/'execution.txt').open('w') as log:
 r=subprocess.run(['python3',str(base/'lib/bin/ntfs_parser'),'--log',str(src[0]),str(src[1]),str(out/'decoded.txt')],env=env,stdout=log,stderr=log)
for p,s in zip(src,before):s.update(sha256_after=h(p));s['unchanged']=s['sha256_before']==s['sha256_after']
(out/'sources.json').write_text(json.dumps(before,indent=2))
s={'returncode':r.returncode,'parser':'dfir_ntfs 1.1.20'}
if (out/'decoded.txt').exists():
 t=(out/'decoded.txt').read_text();blocks=t.split('\n\n---\n\n');usn=re.findall(r'^ Timestamp: (.+)$',t,re.M)
 s.update(bytes=len(t.encode()),blocks=len(blocks),usn_count=len(usn),usn_dates=dict(collections.Counter(x[:10] for x in usn)),embedded_timestamp_years=dict(collections.Counter(re.findall(r'timestamp: (\d{4})-',t))),targets={x:sum(x.lower() in b.lower() for b in blocks) for x in ['L16B','GDRIVE','Archive_saddedine','Inventaire_saddedine','Rejets_saddedine','logmeinrescue','appleid-977451tlu5i']})
 (out/'target-blocks.txt').write_text('\n\n---\n\n'.join(b for b in blocks if any(x.lower() in b.lower() for x in s['targets'])))
 s['decoded_sha256']=h(out/'decoded.txt')
(out/'summary.json').write_text(json.dumps(s,indent=2));print(json.dumps(s))
