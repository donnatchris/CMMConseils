#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,mailbox,email.policy,email.parser,re,collections,shutil
from datetime import datetime,timezone
BASE=Path('/home/sansforensics/analysis/op01-avocats-20261116')
ROOT=Path('/media/shared/codeProjects/DMMConseils')
OUT=ROOT/'ordinateur/recherche-OP-01/correspondances-avocats-20261116'
FIELDS=['Date','From','To','Cc','Bcc','Subject','Reply-To','Message-ID']
def h(m,k):
 try:return str(m.get(k,''))
 except (ValueError,IndexError):return ' '.join(v for a,v in m.raw_items() if a.lower()==k.lower())
def clean(s):return re.sub(r'\s+',' ',s).strip()
def factory(f):
 lines=[]
 while True:
  line=f.readline()
  if not line or line in (b'\n',b'\r\n'):break
  lines.append(line)
 return email.parser.BytesParser(policy=email.policy.default).parsebytes(b''.join(lines)+b'\n',headersonly=True)
old={};counts=collections.Counter();checked=0;diffs=[];native=[]
for l in (ROOT/'investigations/20261109-correspondances-elargies/prive/messages.jsonl').open():
 r=json.loads(l)
 for key,label in [('pst-dmm','dmm'),('pst-93300','93300')]:
  if '/'+key+'/' in r['source']:
   suffix=r['source'].split('/'+key+'/',1)[1];old[(label,suffix,r['index'])]=r
for label in ['93300','dmm']:
 for p in sorted((BASE/label).rglob('mbox')):
  suffix=str(p.relative_to(BASE/label));mb=mailbox.mbox(str(p),factory=factory,create=False)
  for idx,m in enumerate(mb,1):
   r=old[(label,suffix,idx)];heads={k:h(m,k) for k in FIELDS};counts[label]+=1
   changed=[k for k in FIELDS if clean(heads[k])!=clean(r['headers'][k])]
   if changed:diffs.append({'reference':r['id'],'fields':changed,'old_headers':r['headers'],'new_headers':heads})
   native.append({'reference':r['id'],'source_group':label,'source':str(p),'index':idx,'headers':heads})
  mb.close()
 print(label+': '+str(counts[label])+' en-têtes contrôlés',flush=True)
report={'verified_utc':datetime.now(timezone.utc).isoformat(),'counts':dict(counts),'total':sum(counts.values()),'differences':diffs,'all_headers_match':not diffs,'method':'Comparaison intégrale des huit champs d’en-tête de chaque message entre le nouveau décodage readpst et le corpus complet conservé ; seules les différences d’espaces et de repli de lignes sont normalisées.'}
assert report['total']==5875
with (OUT/'validation-nouveaux-decodages.json').open('x') as f:json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
with (OUT/'entetes-nouveaux-decodages.json').open('x') as f:json.dump(native,f,ensure_ascii=False,indent=2);f.write('\n')
assert not (OUT/'decodage-sift.json').exists()
shutil.copyfile(BASE/'decodage.json',OUT/'decodage-sift.json')
print(json.dumps({'total':report['total'],'differences':len(diffs),'all_headers_match':not diffs}),flush=True)
