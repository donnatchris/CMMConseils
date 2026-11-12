#!/usr/bin/env python3
"""Comparer inventaires locaux/S3 et contre-vérifier quatre ETags multipart (8 Mio)."""
import argparse,collections,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[3];a=argparse.ArgumentParser();a.add_argument('--out',required=True);o=Path(a.parse_args().out);o.mkdir(parents=True,exist_ok=False);o.chmod(0o700)
cloud=R/'investigations/20261017-recroisements/resultats/cloud'
remote=json.loads((cloud/'inventaire-s3.json').read_text())['buckets'][0]
by={x['Key']:x for x in remote['objects']};root=Path('/mnt/data/forensic/SADEDINE-2026');missing=[];groups=[];mismatch=[];allrows=[]
for group in ['OP-01','SD-01','SD-02','SD-03','TP-02']:
 files=sorted(p for p in (root/group).rglob('*') if p.is_file());n=0;size=0;miss=0;missbytes=0
 for p in files:
  key='SADEDINE-2026/'+str(p.relative_to(root));s=p.stat().st_size;n+=1;size+=s;r=by.get(key)
  status='same_size' if r and r['Size']==s else 'size_mismatch' if r else 'absent'
  row={'key':key,'local_path':str(p),'size':s,'remote_status':status};allrows.append(row)
  if not r:missing.append(row);miss+=1;missbytes+=s
  elif r['Size']!=s:mismatch.append(row)
 groups.append({'group':group,'local_files':n,'local_bytes':size,'missing_files':miss,'missing_bytes':missbytes,'same_size_files':n-miss-sum(x['key'].startswith('SADEDINE-2026/'+group+'/') for x in mismatch)})
checks=[]
for x in json.loads((cloud/'head-echantillon.json').read_text()):
 p=Path('/mnt/data/forensic')/x['key'];before=p.stat();partmd5=[];sha=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):partmd5.append(hashlib.md5(b).digest());sha.update(b)
 etag=hashlib.md5(b''.join(partmd5)).hexdigest()+'-'+str(len(partmd5));after=p.stat()
 checks.append({'key':x['key'],'local_sha256':sha.hexdigest(),'part_bytes':8*1024*1024,'reconstructed_etag':etag,'s3_etag':x['ETag'],'match':etag==x['ETag'].strip('"'),'source_stat_unchanged':(before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns),'limit':'Concordance ETag multipart MD5 avec découpage 8 Mio ; pas relecture distante intégrale SHA-256.'});print(x['key'],checks[-1]['match'],flush=True)
for name,v in [('resume-conservation.json',{'groups':groups,'mismatches':mismatch,'remote_objects':len(by),'local_inventory_only':True,'TP01_TP03_excluded':True,'ANALYSES_not_covered_by_original_image_inventory':True,'disk_copy_not_identified':True}),('inventaire-local.json',allrows),('objets-manquants.json',missing),('etags-controle.json',checks)]:
 p=o/name;p.write_text(json.dumps(v,indent=2));p.chmod(0o600)
print(json.dumps(groups))
