#!/usr/bin/env python3
"""Recherche sur le corpus PST complet déjà exporté ; Takeout relu directement."""
from pathlib import Path
import json,hashlib,re,unicodedata,collections,email.parser,email.policy,email.utils,zipfile,mailbox,tempfile,html
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
ROOT=Path('/mnt/data/codeProjects/DMMConseils')
OUT=ROOT/'ordinateur/recherche-OP-01/correspondances-avocats-20261116'
PREV=ROOT/'investigations/20261109-correspondances-elargies/prive/messages.jsonl'
FILES=ROOT/'ordinateur/recherche-OP-01/extraction-messageries-20261116'
NAMES={'SOYER':r'soyer','DE LA ROCHÈRE':r'rocher[eé]|delarochere','NEGREVERGNE':r'negre[\s-]*vergne','DRESS':r'dress','RUBIO':r'rubio','PASCOËT':r'pasco[eë]t','DRIE':r'drie','BENVENISTE':r'benveniste','LEPROUX':r'leproux','LIWER':r'liwer','MEYER':r'meyer','KHALLOUKI':r'khallouki|mk\.avocatparis@gmail\.com','FAKIROFF':r'fakiroff|roosevelt-avocats\.fr','WAHRHEIT':r'wahrheit','WAHRHEIT (variante à vérifier)':r'wahreit','GUILLOU':r'guillou'}
FIELDS=['Date','From','To','Cc','Bcc','Subject','Reply-To','Message-ID']
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s.casefold()) if not unicodedata.combining(c))
RX={n:re.compile(norm(v)) for n,v in NAMES.items()}
def terms(s):
 s=norm(s)
 return [n for n,r in RX.items() if r.search(s)]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def headers(m):
 out={}
 for k in FIELDS:
  try:out[k]=str(m.get(k,''))
  except (ValueError,IndexError):out[k]=' '.join(v for a,v in m.raw_items() if a.lower()==k.lower())
 return out
raw=[json.loads(l) for l in PREV.open()]
counts=collections.Counter();rows=[];sources=[]
for r in raw:
 src=r['source']
 if '/pst-93300/' in src:grp='93300'
 elif '/pst-dmm/' in src:grp='dmm'
 elif '::Takeout/' in src:continue
 else:continue
 counts[grp]+=1;h=r['headers'];quoted=[]
 for match in list(re.finditer(r'^From:\s*[^\n]+\n',html.unescape(r['text']),re.M))[:12]:
  q=email.parser.Parser(policy=email.policy.default).parsestr(html.unescape(r['text'])[match.start():]);qh=headers(q)
  if qh['Date'] and qh['Subject'] and terms(' '.join(qh.values())):quoted.append({'kind':'En-tête RFC822 reproduit dans le texte','headers':qh})
 party=terms(' '.join(h[k] for k in ['From','To','Cc','Bcc','Reply-To']))
 bh=terms(r['text'])
 if party or bh or r['id']=='M03025':
  rows.append({'source_group':grp,'source':src,'index':r['index'],'previous_ids':[r['id']],'headers':h,'party_matches':party,'body_name_matches':bh,'quoted_headers':quoted,'attachment_sha256':r['attachments'],'provenance':'Corpus PST complet exporté le 9 novembre 2026, réexaminé intégralement'})
expected=json.loads((FILES/'verification-extraction.json').read_text())
for e in expected['files']:
 p=FILES/e['destination_relative'];actual=sha(p);assert actual==e['exported_sha256']==e['expected_sha256']
 sources.append({'path':str(p),'size':p.stat().st_size,'sha256':actual,'matches_previous_controls':True})
zip_path=FILES/'fichiers/L16B/MESSAGERIES/rct93300@gmail.com/takeout-20241028T114105Z-001.zip'
oldtake={r['index']:r for r in raw if '::Takeout/' in r['source']}
with zipfile.ZipFile(zip_path) as z:
 for info in z.infolist():
  if not info.filename.endswith('.mbox'):continue
  with tempfile.TemporaryDirectory(prefix='op01-takeout-') as td:
   p=Path(td)/'mbox';p.write_bytes(z.read(info));sources.append({'archive':str(zip_path),'member':info.filename,'mbox_sha256':sha(p)})
   mb=mailbox.mbox(str(p),factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False)
   for idx,m in enumerate(mb,1):
    counts['Takeout']+=1;h=headers(m);prev=oldtake[idx]
    for k in FIELDS:assert re.sub(r'\s+',' ',h[k]).strip()==re.sub(r'\s+',' ',prev['headers'][k]).strip(),(idx,k)
    party=terms(' '.join(h[k] for k in ['From','To','Cc','Bcc','Reply-To']));bh=terms(prev['text'])
    if party or bh:rows.append({'source_group':'Takeout','source':str(zip_path)+'::'+info.filename,'index':idx,'previous_ids':[prev['id']],'headers':h,'party_matches':party,'body_name_matches':bh,'quoted_headers':[],'provenance':'MBOX Takeout relu et reparsé directement ; tous les en-têtes concordent avec le corpus antérieur'})
   mb.close()
assert dict(counts)=={'93300':2039,'dmm':3836,'Takeout':301},dict(counts)
result={'created_utc':datetime.now(timezone.utc).isoformat(),'counts':dict(counts),'patterns':NAMES,'sources':sources,'previous_messages_jsonl_sha256':sha(PREV),'previous_messages_jsonl_path':str(PREV),'errors':[],'method':'Réexamen intégral du corpus PST exporté et vérifié antérieurement ; relecture directe de Takeout ; empreintes des trois conteneurs recalculées et identiques.','sift_interruption':'Nouveau décodage des deux PST terminé sur SIFT ; parcours de validation interrompu par perte de connexion SSH. Il ne fonde pas les comptes rendus.','candidates':rows}
with (OUT/'candidats-metadonnees.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'counts':dict(counts),'candidate_count':len(rows),'party_candidates':sum(bool(r['party_matches']) for r in rows)},ensure_ascii=False))
