#!/usr/bin/env python3
"""Read-only targeted analysis; results only in a new output directory."""
import sys, pathlib, hashlib, json, mailbox, email.policy, email.parser, unicodedata, re, io, zipfile, subprocess, collections, tempfile
P=pathlib.Path
out=P(sys.argv[1]); out.mkdir(parents=True,exist_ok=False)
private=out/'prive';private.mkdir(mode=0o700)
sources={};errors=[];counts=collections.Counter();hits=[];attachment_hits=[]
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def track(p):
 p=P(p)
 if str(p) not in sources:sources[str(p)]={'sha256_before':sha(p),'size':p.stat().st_size}
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s.casefold()) if not unicodedata.combining(c))
# Transcription page PDF 17; broad surnames intentionally produce candidates.
patterns={
 'Soyer Yann':r'\bsoyer\b', 'De la Rochere Laurent':r'\broch[eè]re\b|\brochere\b|delarochere',
 'Negrevergne Jean Charles':r'negrevergne|negre[ -]vergne', 'Dress Rachel (lecture à vérifier)':r'\bdress\b|\bdress[ -]rachel\b',
 'Rubio Jonathan':r'\brubio\b', 'Pascoet Christian':r'pascoet|pasco[eë]t',
 'Drie Jean Claude (lecture à vérifier)':r'\bdrie\b', 'Benveniste Caroline':r'benveniste',
 'Leproux Gregory':r'leproux', 'Liwer Charlotte':r'liwer', 'Georges Meyer':r'\bmeyer\b'}
regex={k:re.compile(v) for k,v in patterns.items()}
def match(s):
 s=norm(s);return [k for k,r in regex.items() if r.search(s)]
def textbytes(b,name):
 if len(b)>30*1024*1024: raise ValueError('attachment >30 MiB')
 ext=P(name).suffix.lower()
 if ext=='.pdf':
  r=subprocess.run(['pdftotext','-layout','-','-'],input=b,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  if r.returncode:raise ValueError('pdftotext: '+r.stderr.decode(errors='replace')[:160])
  return r.stdout.decode(errors='replace')
 if ext in ('.docx','.odt','.xlsx'):
  with zipfile.ZipFile(io.BytesIO(b)) as z:
   ns=[i for i in z.infolist() if i.filename.endswith('.xml') and i.file_size<20*1024*1024]
   if sum(i.file_size for i in ns)>50*1024*1024:raise ValueError('XML expansion limit')
   return '\n'.join(re.sub('<[^>]+>',' ',z.read(i).decode(errors='replace')) for i in ns)
 if ext in ('.txt','.csv','.html','.htm','.xml','.rtf','.eml'):
  return b.decode('utf-8',errors='replace')
 raise ValueError('unsupported extension '+ext)
def message(msg,source,index):
 counts['messages']+=1
 hdr='\n'.join(str(msg.get(k,'')) for k in ['From','To','Cc','Bcc','Subject','Reply-To'])
 body=[];ah=[]
 for part in msg.walk():
  if part.is_multipart():continue
  data=part.get_payload(decode=True) or b'';name=part.get_filename()
  if name:
   counts['attachments']+=1
   mh=match(name)
   try:
    t=textbytes(data,name); counts['attachments_text_decoded']+=1;mh=sorted(set(mh+match(t)))
   except Exception as e: errors.append({'source':source,'index':index,'attachment':name,'error':str(e)})
   if mh:ah.append({'name':name,'sha256':hashlib.sha256(data).hexdigest(),'matches':mh})
  elif part.get_content_type() in ('text/plain','text/html'):
   body.append(data.decode(part.get_content_charset() or 'utf-8',errors='replace'))
 b='\n'.join(body);hm=match(hdr);bm=match(b)
 if hm or bm or ah:
  hits.append({'source':source,'index':index,'message_id':str(msg.get('Message-ID','')),'date':str(msg.get('Date','')),'header_matches':hm,'body_matches':bm,'attachments':ah,'headers':hdr,'contexts':[norm(b)[max(0,m.start()-100):m.end()+150] for r in regex.values() for m in list(r.finditer(norm(b)))[:2]]})
root=P('/home/sansforensics/analysis/OP-01/operations-28oct-20261014')
for p in sorted(root.glob('pst-*/**/mbox')):
 track(p);n=0
 mb=mailbox.mbox(str(p),factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False)
 for n,msg in enumerate(mb,1):message(msg,str(p),n)
 counts['mbox_files']+=1;mb.close()
for p in sorted(P('/mnt/windows/L16B/MESSAGERIES').rglob('*.eml')):
 track(p);message(email.parser.BytesParser(policy=email.policy.default).parsebytes(p.read_bytes()),str(p),1);counts['eml_files']+=1
for p in sorted(P('/mnt/windows/L16B').rglob('*.zip')):
 if 'TELEPHONES' not in str(p) and 'takeout' not in p.name.lower():continue
 track(p)
 with zipfile.ZipFile(p) as z:
  for zi in z.infolist():
   if zi.filename.endswith('.mbox'):
    with tempfile.TemporaryDirectory() as td:
     q=P(td)/'mail.mbox';q.write_bytes(z.read(zi))
     mb=mailbox.mbox(str(q),factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False)
     for n,msg in enumerate(mb,1):message(msg,str(p)+'::'+zi.filename,n)
     mb.close();counts['takeout_mbox']+=1
   elif zi.filename.endswith('.txt'):
    t=z.read(zi).decode(errors='replace'); mm=match(t);counts['whatsapp_texts']+=1
    if mm:attachment_hits.append({'source':str(p)+'::'+zi.filename,'matches':mm})
# Hash/metadata of all 27 Mini exports; extract text to isolated private results.
mini=[]
for p in sorted(P('/mnt/windows/L16B/TELEPHONES/IPHONE13_MINI').glob('*')):
 if not p.is_file():continue
 track(p);r={'path':str(p),'size':p.stat().st_size,'sha256':sources[str(p)]['sha256_before']}
 t=textbytes(p.read_bytes(),p.name);r['lawyer_matches']=match(t)
 (private/(p.name+'.txt')).write_text(t)
 mini.append(r)
# Sage vs recovered test: find test through documented recycle metadata separately.
p=P('/mnt/windows/L16B/SAGE/sage.pdf');track(p)
r=subprocess.run(['pdftotext','-layout',str(p),'-'],capture_output=True);(private/'sage.txt').write_bytes(r.stdout)
# Nominal search for external inventory or tool, read-only, bounded to allocated files.
found=[]
for base in ['/mnt/windows/L16B','/mnt/windows/Users/fintm','/media/shared/forensic/SADEDINE-2026']:
 for dp,ds,fs in __import__('os').walk(base):
  for name in fs:
   low=name.lower()
   if low in ['inventaire_saddedine.csv','rejets_saddedine.txt','archive_saddedine.zip','ldsd.bat'] or low.endswith('.iso'):
    found.append(str(P(dp)/name))
for p,v in sources.items():v['sha256_after']=sha(p);v['unchanged']=v['sha256_after']==v['sha256_before']
(private/'lawyer-candidates.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2))
(out/'mini-files.json').write_text(json.dumps(mini,ensure_ascii=False,indent=2))
(private/'attachment-errors.json').write_text(json.dumps(errors,ensure_ascii=False,indent=2))
(out/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2))
summary={'counts':dict(counts),'candidate_message_occurrences':len(hits),'unique_candidate_message_ids':len(set(h['message_id'] for h in hits if h['message_id'])),'by_name':dict(collections.Counter(k for h in hits for k in set(h['header_matches']+h['body_matches']+[x for a in h['attachments'] for x in a['matches']]))),'whatsapp_hits':attachment_hits,'attachment_errors':len(errors),'nominal_search_found':found,'patterns':patterns,'mini_files':len(mini),'all_sources_unchanged':all(v['unchanged'] for v in sources.values())}
(out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False))
