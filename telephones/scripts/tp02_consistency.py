#!/usr/bin/env python3
"""Audit decrypted manifest identity and metadata/payload consistency, no keys exported."""
import argparse
import datetime as dt
import getpass
import hashlib
import json
import os
from pathlib import Path
import plistlib
import struct
import sys
import tempfile
import tp02_forensic as common

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--extracted',action='append',required=True);p.add_argument('--out',required=True)
p.add_argument('--fresh-manifest',action='store_true');a=p.parse_args();os.umask(0o077)
result={'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'rows':[]}
if a.fresh_manifest:
 if not sys.stdin.isatty():raise SystemExit('TTY required')
 from iphone_backup_decrypt import EncryptedBackup
 password=getpass.getpass('Mot de passe TP-02 (contrôle indépendant du manifeste) : ')
 backup=EncryptedBackup(backup_directory=str(common.BACKUP),passphrase=password);del password
 before=common.sha(common.BACKUP/'Manifest.db')
 with tempfile.TemporaryDirectory(prefix='tp02-manifest-check-') as tmp:
  fresh=Path(tmp)/'Manifest.db';backup.save_manifest_file(str(fresh))
  result['manifest']={'encrypted_sha256_before':before,'encrypted_sha256_after':common.sha(common.BACKUP/'Manifest.db'),
    'fresh_decrypted_sha256':common.sha(fresh),'controlled_decrypted_sha256':common.sha(common.MANIFEST)}
  result['manifest']['identical']=result['manifest']['fresh_decrypted_sha256']==result['manifest']['controlled_decrypted_sha256']
with common.ro(common.MANIFEST) as c:
 for root in map(Path,a.extracted):
  for line in (root/'extraction.jsonl').read_text().splitlines():
   r=json.loads(line)
   if r.get('status')!='ok':continue
   v=plistlib.loads(c.execute('SELECT file FROM Files WHERE fileID=?',(r['fileID'],)).fetchone()[0])
   obj=v['$objects'][v['$top']['root'].data];path=Path(r['output']);src=common.BACKUP/r['fileID'][:2]/r['fileID']
   if not src.exists():src=common.BACKUP/r['fileID']
   row={'fileID':r['fileID'],'domain':r['domain'],'relativePath':r['relativePath'],'manifest_size':obj.get('Size'),
    'plaintext_size':path.stat().st_size,'ciphertext_size':src.stat().st_size}
   row['padding_length']=row['ciphertext_size']-row['plaintext_size']
   row['cbc_size_relation_valid']=1<=row['padding_length']<=16
   digest=obj.get('Digest')
   if isinstance(digest,plistlib.UID):digest=v['$objects'][digest.data]
   if isinstance(digest,dict):digest=digest.get('NS.data')
   if isinstance(digest,bytes) and len(digest)==20:
    h=hashlib.sha1()
    with path.open('rb') as f:
     for block in iter(lambda:f.read(1024**2),b''):h.update(block)
    cipher_hash=hashlib.sha1()
    with src.open('rb') as f:
     for block in iter(lambda:f.read(1024**2),b''):cipher_hash.update(block)
    row.update(manifest_digest_sha1=digest.hex(),plaintext_sha1=h.hexdigest(),ciphertext_sha1=cipher_hash.hexdigest(),
      digest_matches_plaintext=digest.hex()==h.hexdigest(),digest_matches_ciphertext=digest.hex()==cipher_hash.hexdigest())
   with path.open('rb') as f:header=f.read(100)
   if header.startswith(b'SQLite format 3\x00'):
    page=struct.unpack('>H',header[16:18])[0];page=65536 if page==1 else page
    count=struct.unpack('>I',header[28:32])[0]
    row.update(sqlite_page_size=page,sqlite_header_pages=count,sqlite_header_bytes=page*count,
     sqlite_header_size_match=page*count==path.stat().st_size)
   result['rows'].append(row)
rows=result['rows']
result['summary']={'files':len(rows),'size_mismatches':sum(r['manifest_size']!=r['plaintext_size'] for r in rows),
 'invalid_cbc_length_relations':sum(not r['cbc_size_relation_valid'] for r in rows),
 'digest_present':sum('manifest_digest_sha1' in r for r in rows),'digest_matches_ciphertext':sum(r.get('digest_matches_ciphertext',False) for r in rows),
 'digest_matches_plaintext':sum(r.get('digest_matches_plaintext',False) for r in rows),
 'digest_matches_neither':sum('manifest_digest_sha1' in r and not (r['digest_matches_ciphertext'] or r['digest_matches_plaintext']) for r in rows),
 'sqlite_header_size_mismatches':sum('sqlite_header_size_match' in r and not r['sqlite_header_size_match'] for r in rows)}
result['limits']=['CBC padding/length is not cryptographic authentication','Digest compared empirically to both plaintext and ciphertext SHA1; no assumed plaintext-only semantics','SQLite header page count alone is not an integrity check']
with open(a.out,'x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(result['summary']))
if 'manifest' in result:print('Manifeste déchiffré indépendant identique :',result['manifest']['identical'])
