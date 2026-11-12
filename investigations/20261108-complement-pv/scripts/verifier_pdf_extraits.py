from pathlib import Path
import json,hashlib,collections
B=Path('investigations/20261108-complement-pv');backup=Path('/mnt/data/forensic/SADEDINE-2026/TP-02/00008110-001C69A002BA801E')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=[json.loads(s) for s in (B/'prive/pdf-extraits-20261109-essai8/extraction.jsonl').read_text().splitlines()];m=json.loads((B/'prive/sift-recupere/mini-files.json').read_text());checks=[];matches=[]
for x in r:
 if x['status']!='ok':continue
 p=backup/x['fileID'][:2]/x['fileID']
 if not p.exists():p=backup/x['fileID']
 checks.append({'fileID':x['fileID'],'ciphertext_unchanged':sha(p)==x['ciphertext_sha256'],'plaintext_hash_verified':sha(Path(x['output']))==x['sha256'],'pdf_signature':Path(x['output']).read_bytes().startswith(b'%PDF-')})
for x in m:
 found=[{'fileID':v['fileID'],'domain':v['domain'],'relativePath':v['relativePath']} for v in r if v.get('status')=='ok' and v['sha256']==x['sha256']]
 matches.append({'l16b_path':x['path'],'sha256':x['sha256'],'matches':found})
(B/'prive/controle-pdf-extraits.json').write_text(json.dumps(checks,indent=2))
(B/'prive/comparaison-pdf-identites.json').write_text(json.dumps(matches,ensure_ascii=False,indent=2))
s={'attempt':8,'password_recorded':False,'extraction_statuses':dict(collections.Counter(x['status'] for x in r)),'l16b_files':len(m),'identical_l16b_files':sum(bool(x['matches']) for x in matches),'all_ciphertext_unchanged':all(x['ciphertext_unchanged'] for x in checks),'all_plaintext_hashes_verified':all(x['plaintext_hash_verified'] for x in checks),'all_pdf_signatures':all(x['pdf_signature'] for x in checks),'matching_domains':dict(collections.Counter(y['domain'] for x in matches for y in x['matches'])),'interpretation':'SHA256 identity establishes common content, not transfer direction/date or exclusive physical origin'}
(B/'resultats/comparaison-pdf-tp02.json').write_text(json.dumps(s,ensure_ascii=False,indent=2));print(json.dumps(s))
