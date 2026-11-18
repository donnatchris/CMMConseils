#!/usr/bin/env python3
"""Réexamen des PST décodés et du ZIP Takeout ; sorties sans corps de message."""
from pathlib import Path
import json,hashlib,mailbox,email.parser,email.policy,re,unicodedata,html,zipfile,tempfile,collections
from html.parser import HTMLParser
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
BASE=Path('/home/sansforensics/analysis/op01-avocats-20261116')
PROJECT=Path('/media/shared/codeProjects/DMMConseils')
OUT=PROJECT/'ordinateur/recherche-OP-01/correspondances-avocats-20261116'
NAMES={'SOYER':r'soyer','DE LA ROCHÈRE':r'rocher[eé]|delarochere','NEGREVERGNE':r'negre[\s-]*vergne','DRESS':r'dress','RUBIO':r'rubio','PASCOËT':r'pasco[eë]t','DRIE':r'drie','BENVENISTE':r'benveniste','LEPROUX':r'leproux','LIWER':r'liwer','MEYER':r'meyer','KHALLOUKI':r'khallouki|mk\.avocatparis@gmail\.com','FAKIROFF':r'fakiroff|roosevelt-avocats\.fr','WAHRHEIT':r'wahrheit','WAHRHEIT (variante à vérifier)':r'wahreit','GUILLOU':r'guillou'}
FIELDS=['Date','From','To','Cc','Bcc','Subject','Reply-To','Message-ID']
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s.casefold()) if not unicodedata.combining(c))
RX={n:re.compile(norm(r)) for n,r in NAMES.items()}
def terms(s):
 s=norm(s)
 return [n for n,r in RX.items() if r.search(s)]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def header(m,k):
 try:return str(m.get(k,''))
 except (ValueError,IndexError):return ' '.join(v for a,v in m.raw_items() if a.lower()==k.lower())
def headers(m):return {k:header(m,k) for k in FIELDS}
def date_paris(s):
 try:
  d=email.utils.parsedate_to_datetime(s)
  return d.astimezone(ZoneInfo('Europe/Paris')).isoformat() if d.tzinfo else d.isoformat()+' (fuseau absent)'
 except Exception:return ''
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ('style','script'):self.skip+=1
  if t in ('div','p','br','tr'):self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ('style','script'):self.skip=max(0,self.skip-1)
  if t in ('div','p','tr'):self.parts.append('\n')
 def handle_data(self,s):
  if not self.skip:self.parts.append(s)
def decode(part):
 b=part.get_payload(decode=True)
 if b is None:return ''
 enc=part.get_content_charset()
 for c in dict.fromkeys([enc,'utf-8','cp1252','latin1']):
  if c:
   try:return b.decode(c)
   except (UnicodeError,LookupError):pass
 return b.decode('utf-8',errors='replace')
def text(part):
 s=decode(part)
 if part.get_content_type()=='text/html':
  p=Plain();p.feed(s);s=''.join(p.parts)
 return html.unescape(s)
old=collections.defaultdict(list)
for line in (PROJECT/'investigations/20261109-correspondances-elargies/prive/messages.jsonl').open():
 r=json.loads(line);old[re.sub(r'\s+','',r['headers']['Message-ID'])].append(r['id'])
rows=[];counts=collections.Counter();sources=[];errors=[]
def process(m,label,src,idx):
 h=headers(m);counts[label]+=1
 party=terms(' '.join(h[k] for k in ['From','To','Cc','Bcc','Reply-To']))
 body_terms=set();quoted=[];attachments=[]
 for part in m.walk():
  if part is not m and part.get_content_type()=='message/rfc822':
   for sub in part.get_payload() if isinstance(part.get_payload(),list) else []:
    sh=headers(sub)
    if terms(' '.join(sh.values())):quoted.append({'kind':'message/rfc822','headers':sh})
  if part.is_multipart():continue
  name=part.get_filename()
  if name:
   b=part.get_payload(decode=True)
   if b:attachments.append({'name':name,'sha256':hashlib.sha256(b).hexdigest(),'size':len(b)})
  if part.get_content_type() not in ('text/plain','text/html'):continue
  s=text(part);body_terms.update(terms(s))
  # An NDR can contain a complete original MIME message in a text part.
  for match in list(re.finditer(r'^From:\s*[^\n]+\n',s,re.M))[:12]:
   try:
    q=email.parser.Parser(policy=email.policy.default).parsestr(s[match.start():])
    qh=headers(q)
    if qh['Date'] and qh['Subject'] and terms(' '.join(qh.values())):
     quoted.append({'kind':'En-tête RFC822 reproduit dans le texte','headers':qh})
   except Exception as e:errors.append({'source':src,'index':idx,'error_type':type(e).__name__})
 if party or body_terms:
  mid=re.sub(r'\s+','',h['Message-ID'])
  rows.append({'source_group':label,'source':src,'index':idx,'previous_ids':old.get(mid,[]) if mid else [],'headers':h,'date_paris':date_paris(h['Date']),'party_matches':party,'body_name_matches':sorted(body_terms),'quoted_headers':quoted,'attachments':attachments})
for label in ['93300','dmm']:
 for p in sorted((BASE/label).rglob('mbox')):
  sh=sha(p);n=counts[label]
  mb=mailbox.mbox(str(p),factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False)
  for idx,m in enumerate(mb,1):process(m,label,str(p),idx)
  mb.close();sources.append({'path':str(p),'sha256':sh,'messages':counts[label]-n})
 print('Messages parcourus '+label+' : '+str(counts[label]),flush=True)
zpath=PROJECT/'ordinateur/recherche-OP-01/extraction-messageries-20261116/fichiers/L16B/MESSAGERIES/rct93300@gmail.com/takeout-20241028T114105Z-001.zip'
with zipfile.ZipFile(zpath) as z:
 for info in z.infolist():
  if info.filename.lower().endswith('.mbox'):
   with tempfile.TemporaryDirectory(prefix='op01-takeout-') as td:
    p=Path(td)/'mbox';p.write_bytes(z.read(info));sources.append({'archive':str(zpath),'archive_sha256':sha(zpath),'member':info.filename,'mbox_sha256':sha(p)})
    mb=mailbox.mbox(str(p),factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False)
    for idx,m in enumerate(mb,1):process(m,'Takeout',str(zpath)+'::'+info.filename,idx)
    mb.close()
assert dict(counts)=={'93300':2039,'dmm':3836,'Takeout':301},dict(counts)
OUT.mkdir(mode=0o700,exist_ok=True)
with (OUT/'candidats-metadonnees.json').open('x') as f:json.dump({'created_utc':datetime.now(timezone.utc).isoformat(),'counts':dict(counts),'patterns':NAMES,'sources':sources,'errors':errors,'candidates':rows},f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'counts':dict(counts),'candidates':len(rows),'header_candidates':sum(bool(r['party_matches']) for r in rows),'errors':len(errors)},ensure_ascii=False),flush=True)
