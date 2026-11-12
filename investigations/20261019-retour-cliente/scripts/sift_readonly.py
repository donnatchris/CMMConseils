#!/usr/bin/env python3
"""Read-only OP-01 checks. New output directory required; no evidence writes."""
import pathlib,json,hashlib,datetime as D,struct,subprocess,collections,xml.etree.ElementTree as E
import pyevtx
from zoneinfo import ZoneInfo
B=pathlib.Path('/mnt/windows'); O=pathlib.Path('/home/sansforensics/analysis/complement-20261019/resultats');O.mkdir(mode=0o700,exist_ok=False)
Z=ZoneInfo('Europe/Paris');U=D.timezone.utc
mount=subprocess.check_output(['findmnt','-n','-o','OPTIONS','--mountpoint',str(B)],text=True)
assert 'ro' in mount.strip().split(',')
(O/'mount.txt').write_text(subprocess.check_output(['findmnt','/mnt/windows'],text=True))
def h(p):
 x=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):x.update(b)
 return x.hexdigest()
def save(n,v): (O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str))
errors=[];sources=[];events=[];inv=[];ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'}
for p in sorted((B/'Windows/System32/winevt/Logs').glob('*.evtx')):
 before=h(p);f=pyevtx.file();count=0;first=last=None;days=collections.Counter();selected=0
 try:
  f.open(str(p))
  for i in range(f.number_of_records):
   try:
    r=f.get_record(i); t=r.creation_time.replace(tzinfo=U);s=t.isoformat();count+=1;first=min(first or s,s);last=max(last or s,s)
    paris=t.astimezone(Z); date=paris.date().isoformat()
    if '2024-10-15'<=date<='2024-10-29':days[date]+=1
    # All records on 28/29 plus central retention interval, not just known providers.
    if not ('2024-10-16'<=date<='2024-10-29'):continue
    x=r.xml_string;e=E.fromstring(x); prov=e.find('e:System/e:Provider',ns)
    row={'source':p.name,'record':r.identifier,'id':r.event_identifier,'utc':s,'paris':paris.isoformat(),'provider':prov.get('Name') if prov is not None else None,'xml':x}
    events.append(row);selected+=1
   except Exception as ex:errors.append({'source':p.name,'index':i,'error':str(ex)})
 except Exception as ex:errors.append({'source':p.name,'error':str(ex)})
 finally:f.close()
 after=h(p);sources.append({'path':str(p),'sha256_before':before,'sha256_after':after,'unchanged':before==after})
 inv.append({'source':p.name,'records':count,'first_utc':first,'last_utc':last,'days_paris':dict(days),'selected':selected})
 if selected:print(p.name,count,selected,flush=True)
save('evtx-inventory.json',inv);save('events-16-29oct.json',events)
post=[r for r in events if '2024-10-28T19:20:00+01:00'<r['paris']<'2024-10-29']
save('events-apres-1920.json',post)
recycle=[]
for p in sorted((B/'$Recycle.Bin').rglob('$I*')):
 if not p.is_file():continue
 try:
  b=p.read_bytes();before=h(p)
  if len(b)<28:continue
  v,size,ft=struct.unpack_from('<QQQ',b)
  if v not in (1,2):continue
  path=b[28 if v==2 else 24:].decode('utf-16le',errors='replace').rstrip('\x00')
  t=D.datetime(1601,1,1,tzinfo=U)+D.timedelta(microseconds=ft//10)
  row={'source':str(p),'version':v,'size':size,'filetime':ft,'utc':t.isoformat(),'paris':t.astimezone(Z).isoformat(),'original_path':path,'sha256':before}
  rp=p.with_name('$R'+p.name[2:]);row['R_exists']=rp.is_file()
  if t.astimezone(Z).date()==D.date(2024,10,28) and rp.is_file():row.update(R_sha256=h(rp),R_size=rp.stat().st_size)
  recycle.append(row);sources.append({'path':str(p),'sha256_before':before,'sha256_after':h(p),'unchanged':before==h(p)})
 except Exception as ex:errors.append({'source':str(p),'error':str(ex)})
save('recycle.json',recycle)
# Pair records: metadata only, never private keys/certificates.
pairs=[]
import plistlib
for base in [B/'ProgramData/Apple/Lockdown',B/'ProgramData/Apple Computer/Lockdown']:
 for p in base.glob('*'):
  if not p.is_file():continue
  before=h(p);row={'source':str(p),'size':p.stat().st_size,'mtime_utc':D.datetime.fromtimestamp(p.stat().st_mtime,U).isoformat(),'sha256':before}
  try:
   v=plistlib.loads(p.read_bytes());row['keys']=list(v);row['identifier_fields']={k:v[k] for k in ['HostID','SystemBUID','DeviceName','SerialNumber','UDID'] if k in v}
  except Exception as ex:row['parse_error']=str(ex)
  pairs.append(row);sources.append({'path':str(p),'sha256_before':before,'sha256_after':h(p),'unchanged':before==h(p)})
save('apple-pairing-op01.json',pairs)
save('sources.json',sources);save('errors.json',errors)
save('summary.json',{'evtx_files':len(inv),'records':sum(r['records'] for r in inv),'post1920_events':len(post),'post1920_providers':dict(collections.Counter(r['provider'] for r in post)),'recycle_total':len(recycle),'recycle_28':[r for r in recycle if r['paris'].startswith('2024-10-28')],'apple_pair_files':len(pairs),'errors':len(errors),'sources_unchanged':all(r['unchanged'] for r in sources)})
print('Finished',len(post),'post1920',len(errors),'errors',flush=True)
