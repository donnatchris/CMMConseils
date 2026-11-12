from pathlib import Path
import json,hashlib,mailbox,email.policy,email.parser,zipfile,tempfile,collections,re,unicodedata,sys
O=Path(sys.argv[1]);O.mkdir(exist_ok=False);(O/'blobs').mkdir();(O/'textes').mkdir();sources={};blobs={};n=0
msgs=(O/'messages.jsonl').open('w');refs=(O/'references.jsonl').open('w')
def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def track(p):sources[str(p)]={'sha256_before':sha(p),'size':p.stat().st_size}
def blob(data,name,origin):
 h=hashlib.sha256(data).hexdigest()
 if h not in blobs:
  (O/'blobs'/h).write_bytes(data);blobs[h]={'sha256':h,'size':len(data),'names':[]}
 if name not in blobs[h]['names']:blobs[h]['names'].append(name)
 refs.write(json.dumps({'sha256':h,'name':name,**origin},ensure_ascii=False)+'\n');return h
fields=['From','To','Cc','Bcc','Subject','Reply-To','Date','Message-ID']
def msg(m,src,idx):
 global n
 n+=1;key=f'M{n:05}';body=[];ats=[]
 for part in m.walk():
  if part.is_multipart():continue
  data=part.get_payload(decode=True) or b'';name=part.get_filename()
  if name or part.get_content_type() not in ('text/plain','text/html'):
   if data:ats.append(blob(data,name or '',{'message':key,'source':src,'index':idx}))
  else:
   try:t=data.decode(part.get_content_charset() or 'utf8',errors='replace')
   except LookupError:t=data.decode('utf8',errors='replace')
   if part.get_content_type()=='text/html':t=re.sub('<[^>]+>',' ',t)
   body.append(t)
 row={'id':key,'source':src,'index':idx,'headers':{k:str(m.get(k,'')) for k in fields},'text':'\n'.join(body),'attachments':ats};msgs.write(json.dumps(row,ensure_ascii=False)+'\n')
root=Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014')
for p in sorted(root.glob('pst-*/**/mbox')):
 track(p);mb=mailbox.mbox(str(p),factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False)
 for i,m in enumerate(mb,1):msg(m,str(p),i)
 mb.close();msgs.flush();refs.flush();print('mbox',n,flush=True)
for p in sorted(Path('/mnt/windows/L16B/MESSAGERIES').rglob('*.eml')):
 track(p);msg(email.parser.BytesParser(policy=email.policy.default).parsebytes(p.read_bytes()),str(p),1)
for p in sorted(Path('/mnt/windows/L16B').rglob('*.zip')):
 if 'takeout' not in p.name.lower():continue
 track(p)
 with zipfile.ZipFile(p) as z:
  for zi in z.infolist():
   if not zi.filename.endswith('.mbox'):continue
   with tempfile.TemporaryDirectory() as td:
    q=Path(td)/'m';q.write_bytes(z.read(zi));mb=mailbox.mbox(str(q),factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False)
    for i,m in enumerate(mb,1):msg(m,str(p)+'::'+zi.filename,i)
    mb.close()
# All allocated L16B standalone documents are included, not only the 27 Mini PDFs.
exts={'.pdf','.doc','.docx','.xls','.xlsx','.odt','.ods','.rtf','.txt','.csv','.jpg','.jpeg','.png','.tif','.tiff'}
for p in sorted(Path('/mnt/windows/L16B').rglob('*')):
 if p.is_file() and p.suffix.lower() in exts:
  track(p);blob(p.read_bytes(),p.name,{'source':str(p),'standalone':True})
for p,v in sources.items():v['sha256_after']=sha(Path(p));v['unchanged']=v['sha256_after']==v['sha256_before']
msgs.close();refs.close();(O/'blobs.json').write_text(json.dumps(list(blobs.values()),ensure_ascii=False));(O/'sources.json').write_text(json.dumps(sources,ensure_ascii=False));print(json.dumps({'messages':n,'unique_blobs':len(blobs),'bytes':sum(x['size'] for x in blobs.values()),'sources':len(sources),'all_unchanged':all(v['unchanged'] for v in sources.values())}),flush=True)
