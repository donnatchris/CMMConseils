#!/usr/bin/env python3
"""Recheck recorded plaintext/ciphertext hashes, without writing originals."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import tp02_forensic as common

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--extracted',action='append',required=True)
p.add_argument('--backup',default=str(common.BACKUP))
p.add_argument('--out',required=True)
a=p.parse_args();os.umask(0o077)
rows=[]
for root in map(Path,a.extracted):
 for line in (root/'extraction.jsonl').read_text().splitlines():
  r=json.loads(line)
  if r.get('status')!='ok':continue
  fid=r['fileID'];src=Path(a.backup)/fid[:2]/fid
  if not src.is_file():src=Path(a.backup)/fid
  row={'fileID':fid,'domain':r['domain'],'relativePath':r['relativePath'],'expected_plaintext_sha256':r['sha256'],'expected_ciphertext_sha256':r['ciphertext_sha256']}
  try:
   row.update(plaintext_sha256=common.sha(r['output']),ciphertext_sha256=common.sha(src))
   row['status']='ok' if row['plaintext_sha256']==r['sha256'] and row['ciphertext_sha256']==r['ciphertext_sha256'] else 'mismatch'
  except Exception as e:row.update(status='error',error_class=type(e).__name__)
  rows.append(row)
summary={'verified_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'files':len(rows),'ok':sum(r['status']=='ok' for r in rows),'rows':rows,
         'limit':'checks selected source objects against pre-extraction hashes; not a full backup hash'}
with open(a.out,'x') as f:json.dump(summary,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({k:summary[k] for k in ('files','ok')}))
raise SystemExit(0 if summary['files']==summary['ok'] else 1)
