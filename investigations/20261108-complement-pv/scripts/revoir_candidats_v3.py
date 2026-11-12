import json,mailbox,email.policy,email.parser,pathlib,subprocess,zipfile,io,re,hashlib
B=pathlib.Path('/media/shared/codeProjects/CMMConseils/investigations/20261108-complement-pv')
h=json.loads((B/'prive/sift-recupere/prive/lawyer-candidates.json').read_text());out=B/'prive/verification-20261109-v3';out.mkdir(exist_ok=False)
results=[]; cache={}
for i,x in enumerate(h):
 if '::' in x['source']:continue
 if x['source'] not in cache:
  mb=mailbox.mbox(x['source'],factory=lambda f:email.parser.BytesParser(policy=email.policy.default).parse(f),create=False);cache[x['source']]=(mb,list(mb.keys()))
 mb,keys=cache[x['source']];msg=mb[keys[x['index']-1]]
 assert str(msg.get('Message-ID',''))==x['message_id']
 row={'candidate':i,'message_id_verified':True,'parts':[]}
 for part in msg.walk():
  if part.is_multipart():continue
  name=part.get_filename();d=part.get_payload(decode=True) or b''
  if name and any(a['sha256']==hashlib.sha256(d).hexdigest() for a in x['attachments']):
   if name.lower().endswith('.pdf'):t=subprocess.run(['pdftotext','-layout','-','-'],input=d,capture_output=True,check=True).stdout.decode()
   elif name.lower().endswith('.docx'):
    with zipfile.ZipFile(io.BytesIO(d)) as z:t='\n'.join(re.sub('<[^>]+>',' ',z.read(n).decode()) for n in z.namelist() if n.endswith('.xml'))
   else:continue
   row['parts'].append({'name':name,'contexts':[t[max(0,m.start()-200):m.end()+300] for m in re.finditer(r'meyer|dress|pasco[eë]t',t,re.I)]})
  elif not name and part.get_content_type()=='text/plain':row['parts'].append({'body':d.decode(part.get_content_charset() or 'utf8',errors='replace')})
 results.append(row)
(out/'review.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print('verified',len(results))
