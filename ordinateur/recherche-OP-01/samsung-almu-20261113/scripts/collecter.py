import pathlib,json,re,datetime,hashlib,shutil,subprocess,xml.etree.ElementTree as E,collections
import pyevtx,pyregf
from zoneinfo import ZoneInfo
B=pathlib.Path('/mnt/windows');O=pathlib.Path('/home/sansforensics/analysis/OP-01/samsung-almu-20261113');O.mkdir(exist_ok=True,parents=True)
S=[];ERR=[];serial='R58RB2ETQER';aliases=['7&95c02d9&0&0000','7&ce3bc01&0&0000','7&ce3bc01&0&0001'];containers=['1CA7345B-8094-54CF-9254-1FD5A1078FA8','351A21C4-96A2-5BB0-ACAE-B2A64FC0DF96']
def save(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str))
def src(p,copy=False):
 p=pathlib.Path(p);s=p.stat();r={'path':str(p.relative_to(B)),'size':s.st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()};S.append(r)
 if copy:
  q=O/'raw'/p.relative_to(B);q.parent.mkdir(exist_ok=True,parents=True);shutil.copyfile(p,q);q.chmod(0o600)
 return r
save('mount.json',{'mount':subprocess.getoutput('findmnt /mnt/windows'),'loop':subprocess.getoutput('lsblk -o NAME,SIZE,FSTYPE,RO,TYPE,MOUNTPOINT /dev/loop16')})
# Exact handset serial first; hardware aliases are distinguished explicitly.
hits=[];prints=[];inv=[]
for p in sorted((B/'Windows/System32/winevt/Logs').glob('*.evtx')):
 try:
  f=pyevtx.file();f.open(str(p));lo=hi=None;nexact=nalias=0;selected=False
  for i in range(f.number_of_records):
   r=f.get_record(i);t=r.creation_time.replace(tzinfo=datetime.timezone.utc);ts=t.isoformat();lo=min(lo or ts,ts);hi=max(hi or ts,ts);xml=r.xml_string
   exact=serial.lower() in xml.lower();alias=any(a.lower() in xml.lower() for a in aliases+containers)
   day='2024-10-27T23:'<=ts<'2024-10-28T23:';isprint='PrintService' in p.name and day
   if not(exact or alias or isprint):continue
   e=E.fromstring(xml);data={x.get('Name',str(j)):x.text for j,x in enumerate(e.findall('{*}EventData/{*}Data'))};ud=e.find('{*}UserData')
   if ud is not None:data.update({x.tag.split('}')[-1]:x.text for x in ud.iter() if len(x)==0})
   row={'source':p.name,'utc':ts,'paris':t.astimezone(ZoneInfo('Europe/Paris')).isoformat(),'id':r.event_identifier,'record':r.identifier,'data':data,'xml':xml}
   if exact or alias:
    row['serial_exact']=exact;row['alias_only']=not exact;hits.append(row);nexact+=int(exact);nalias+=int(not exact)
   if isprint:prints.append(row)
   selected=True
  inv.append({'source':p.name,'records':f.number_of_records,'first_utc':lo,'last_utc':hi,'exact_serial_matches':nexact,'alias_only_matches':nalias});f.close()
  if selected:src(p,True)
 except Exception as ex:ERR.append({'source':p.name,'error':str(ex)})
save('samsung-events.json',hits);save('print-events-day.json',prints);save('evtx-inventory.json',inv);print('EVTX done',len(hits),len(prints),flush=True)
# Full retained SetupAPI rotations, preserving sections with exact serial or alias.
setup=[];setupinv=[]
for p in sorted((B/'Windows/INF').glob('setupapi*.log')):
 try:
  b=p.read_bytes();t=b.decode('utf-16' if b[:2] in [b'\xff\xfe',b'\xfe\xff'] else 'cp1252',errors='replace');exact=serial.lower() in t.lower();n=0
  for m in re.finditer(r'(?ms)^>>>  \[.*?(?=^>>>  \[|\Z)',t):
   block=m.group();isexact=serial.lower() in block.lower();isalias=any(a.lower() in block.lower() for a in aliases)
   if isexact or isalias:
    setup.append({'source':str(p.relative_to(B)),'line':t[:m.start()].count('\n')+1,'serial_exact':isexact,'header':block.splitlines()[0],'start':re.findall(r'Section start ([^\r\n]+)',block),'end':re.findall(r'Section end ([^\r\n]+)',block),'text':block});n+=1
  dates=re.findall(r'Section start (\d{4}/\d{2}/\d{2} [\d:.]+)',t)
  setupinv.append({'source':str(p.relative_to(B)),'size':len(b),'section_first':min(dates) if dates else None,'section_last':max(dates) if dates else None,'serial_occurrences':t.lower().count(serial.lower()),'matched_sections':n});src(p,exact or n>0)
 except Exception as ex:ERR.append({'source':str(p),'error':str(ex)})
save('setupapi-samsung.json',setup);save('setupapi-inventory.json',setupinv);print('Setup done',len(setup),flush=True)
# Read only device-specific allocated registry entries; do not collect credential stores.
reg=[];reginv=[]
def values(k):
 out={}
 for v in k.values:
  try:out[v.name or '(default)']=v.get_data_as_string() if v.type in [1,2] else v.get_data_as_integer() if v.type in [4,11] else {'hex':(v.data or b'').hex()}
  except Exception:out[v.name or '(default)']={'hex':(v.data or b'').hex()}
 return out
def subtree(k,path,hp):
 reg.append({'hive':hp,'key':path,'lastwrite_utc':str(k.last_written_time),'values':values(k)})
 for sub in k.sub_keys:subtree(sub,path+'\\'+sub.name,hp)
def search(k,path,hp):
 vals=values(k);context=path+' '+json.dumps(vals);match=any(t.lower() in context.lower() for t in [serial]+aliases+containers)
 if match:subtree(k,path,hp)
 else:
  for sub in k.sub_keys:search(sub,path+'\\'+sub.name,hp)
for hp,branches in {'Windows/System32/config/SYSTEM':[r'ControlSet001\Enum\USB',r'ControlSet001\Enum\SWD',r'ControlSet001\Control\DeviceContainers',r'ControlSet001\Control\DeviceClasses',r'ControlSet001\Services\DeviceAssociationService'], 'Windows/System32/config/SOFTWARE':[r'Microsoft\Windows Portable Devices',r'Microsoft\Windows\CurrentVersion\Device Metadata',r'Microsoft\Windows\CurrentVersion\WINEVT\Publishers']}.items():
 f=pyregf.file();f.open(str(B/hp));src(B/hp)
 for branch in branches:
  k=f.get_key_by_path(branch);before=len(reg)
  if k:search(k,branch,hp)
  reginv.append({'hive':hp,'branch':branch,'exists':bool(k),'selected_keys':len(reg)-before})
 f.close()
save('samsung-registry.json',reg);save('registry-coverage.json',reginv)
# Relevant actual output files, retained spool remnants and application print snapshots.
files=[]
for p in [B/'L16B/SAGE/sage.pdf',B/'$Recycle.Bin/S-1-5-21-1394434332-468722268-2897565647-1001/$R2RYNYS.pdf',B/'$Recycle.Bin/S-1-5-21-1394434332-468722268-2897565647-1001/$I2RYNYS.pdf']:
 if p.exists():files.append(src(p,True))
for d in [B/'L16B',B/'Users/fintm/OneDrive/Bureau',B/'Users/fintm/Desktop',B/'Windows/System32/spool/PRINTERS']:
 if d.exists():
  for p in d.iterdir():
   if p.is_file() and (re.search(r'(?i)^(test|sage)\.pdf$|\.(spl|shd)$',p.name)):files.append(src(p,True))
pdir=B/'ProgramData/Ciel/Applications/Ciel Gestion Commerciale/ALMU.1296571903/Dernières impressions'
for p in pdir.glob('*'):
 if p.is_file():files.append(src(p,True))
save('output-files.json',files);save('sources.json',S);save('errors.json',ERR);print('Done registry',len(reg),'files',len(files),'errors',len(ERR),flush=True)
