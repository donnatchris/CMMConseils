#!/usr/bin/env python3
"""A exécuter dans SIFT sur montage RO. Résultats sans secrets de comptes."""
import collections,datetime as dt,email,email.utils,hashlib,json,mailbox,re,subprocess
from pathlib import Path
import pyregf,pyevtx
import xml.etree.ElementTree as ET
O=Path('/home/sansforensics/analysis/complement-20261017/resultats');O.mkdir(exist_ok=False);O.chmod(0o700)
if 'ro' not in subprocess.check_output(['findmnt','-rn','-o','OPTIONS','/mnt/windows'],text=True).strip().split(','):raise SystemExit('Montage non RO')
sources={};errors=[]
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
def src(p):
 p=Path(p)
 if str(p) not in sources:sources[str(p)]={'path':str(p),'size':p.stat().st_size,'sha256_before':h(p)}
 return p
def save(n,v):
 p=O/n;p.write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str));p.chmod(0o600)
tokens=['386d4397','6546a41d','121220160204','140b8328','desktop-icpncmd','ac:ed:5c:da:47:74','aced5cda4774','e0:a2:5a:0a:a3:f7']
hits=[];dates=[];stats=[]
paths=[Path('/mnt/windows/Windows/System32/config')/n for n in ['SYSTEM','SOFTWARE']]
paths += [p for p in Path('/mnt/windows/Users').glob('*/NTUSER.DAT') if p.is_file()]
for p in paths:
 src(p);f=pyregf.file();f.open(str(p));stack=[(f.get_root_key(),'')];keys=0;vals=0
 while stack:
  key,path=stack.pop();keys+=1
  try:
   ts=key.get_last_written_time();t=str(ts)
   if t.startswith('2024-11-12'):dates.append({'hive':str(p),'key':path,'lastwrite_utc':t})
   candidates=[x for x in tokens if x in path.lower()]
   for i in range(key.number_of_values):
    v=key.get_value(i);vals+=1;data=v.get_data() or b''
    text=data.decode('utf-16-le',errors='ignore').lower()+' '+data.decode('latin1',errors='ignore').lower();matches=[x for x in tokens if x in text]
    # Valeurs de volume 32 bits, uniquement si exactement 4 octets pour éviter les faux positifs.
    if len(data)==4:
     hexnum=f'{int.from_bytes(data,"little"):08x}'
     if hexnum in tokens:matches.append(hexnum)
    if matches:hits.append({'hive':str(p),'key':path,'value_name':v.name,'lastwrite_utc':t,'matches':matches,'data_sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
   if candidates:hits.append({'hive':str(p),'key':path,'lastwrite_utc':t,'matches':candidates,'kind':'key_name'})
   for i in range(key.number_of_sub_keys):
    k=key.get_sub_key(i);stack.append((k,path+'\\'+k.name))
  except Exception as ex:errors.append({'source':str(p),'key':path,'error':type(ex).__name__})
 f.close();stats.append({'source':str(p),'keys':keys,'values':vals});print('registry',p.name,keys,flush=True)
save('registry-hits.json',hits);save('registry-12novembre.json',dates);save('registry-coverage.json',stats)

# Journaux PnP/stockage complets disponibles : sélectionner les dates, pas les dates de fichier.
events=[];coverage=[];ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'}
for p in Path('/mnt/windows/Windows/System32/winevt/Logs').glob('*.evtx'):
 if not any(x in p.name.lower() for x in ['partition','kernel-pnp','driverframework','devicesetup','storage-class','stordiag','userpnp']):continue
 src(p);f=pyevtx.file();f.open(str(p));count=f.number_of_records;selected=0;bounds=[]
 for i in range(count):
  try:
   r=f.get_record(i);d=r.get_creation_time();t=str(d);bounds.append(t)
   if not '2024-11-11'<=t[:10]<='2024-11-13':continue
   e=ET.fromstring(r.get_xml_string());data={}
   for node in e:
    if node.tag.endswith('System'):continue
    for z in node.iter():
     if len(z)==0 and z.text:data[z.get('Name') or z.tag.split('}')[-1]]=z.text
   events.append({'source':str(p),'index':i,'record':r.identifier,'utc':t,'event_id':r.event_identifier,'data':data});selected+=1
  except Exception as ex:errors.append({'source':str(p),'index':i,'error':type(ex).__name__})
 f.close();coverage.append({'source':str(p),'records':count,'first':min(bounds) if bounds else None,'last':max(bounds) if bounds else None,'selected':selected})
save('stockage-11-13novembre.json',events);save('stockage-coverage.json',coverage);print('storage',len(events),flush=True)

# Recherche MIME décodée dans les deux PST déjà exportés ; aucune exécution de pièce jointe.
base=Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014');mailhits=[];mailstats=[]
for p in sorted(list((base/'pst-dmm').rglob('mbox'))+list((base/'pst-93300').rglob('mbox'))):
 src(p);mb=mailbox.mbox(str(p),create=False);n=0;skipped=0
 for key,msg in mb.iteritems():
  n+=1;classes=set();attachments=[];domains=set();date=msg.get('Date')
  header=' '.join(str(msg.get(k,'')) for k in ['Subject','From','To'])
  if 'logmeinrescue' in header.lower():classes.add('rescue_header')
  for part in msg.walk():
   if part.is_multipart():continue
   fn=part.get_filename() or '';fnlower=fn.lower()
   if 'appleid-977451tlu5i' in fnlower:classes.add('phishing_filename_exact')
   if fn and part.get_content_type()=='application/pdf':attachments.append({'name':fn,'part_type':part.get_content_type()})
   payload=part.get_payload(decode=True) or b''
   if len(payload)>50*1024*1024:skipped+=1;continue
   if b'logmeinrescue' in payload.lower():classes.add('rescue_payload')
   if b'appleid-977451tlu5i' in payload.lower():classes.add('phishing_literal')
   if part.get_content_maintype()=='text':
    text=payload.decode(part.get_content_charset() or 'utf-8',errors='replace').lower()
    if 'logmeinrescue' in text:classes.add('rescue_text')
    if 'appleid-977451tlu5i' in text:classes.add('phishing_text')
  if classes:mailhits.append({'source':str(p),'mbox_key':key,'date_header':date,'message_id_sha256':hashlib.sha256(str(msg.get('Message-ID','')).encode()).hexdigest(),'classes':sorted(classes),'pdf_attachments':attachments})
 mb.close();mailstats.append({'source':str(p),'messages':n,'oversize_parts_skipped':skipped});print('mbox',p.parent.name,n,flush=True)
save('messageries-cibles.json',mailhits);save('messageries-coverage.json',mailstats)
for s in sources.values():s['sha256_after']=h(Path(s['path']));s['unchanged']=s['sha256_before']==s['sha256_after']
save('sources.json',list(sources.values()));save('errors.json',errors)
save('summary.json',{'registry_hits':len(hits),'registry_nov12':len(dates),'storage_events':len(events),'mail_messages':sum(x['messages'] for x in mailstats),'mail_hits':len(mailhits),'errors':len(errors),'unchanged':all(x['unchanged'] for x in sources.values())})
print('done',flush=True)
