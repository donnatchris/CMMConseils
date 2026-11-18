#!/usr/bin/python3
import os,re,json,pathlib,hashlib,datetime,subprocess,shutil,collections,xml.etree.ElementTree as E
import pyregf,pyevtx
from zoneinfo import ZoneInfo
B=pathlib.Path('/mnt/windows');O=pathlib.Path('/home/sansforensics/analysis/OP-01/sage-reseaux-20261113');O.mkdir(exist_ok=True,parents=True)
S=[];ERR=[]
def save(n,v): (O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str))
def src(p,copy=False):
 p=pathlib.Path(p);s=p.stat();r={'path':str(p.relative_to(B)),'size':s.st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()};S.append(r)
 if copy:
  q=O/'raw'/p.relative_to(B);q.parent.mkdir(exist_ok=True,parents=True);shutil.copyfile(p,q);q.chmod(0o600)
 return r
save('mount.json',{'findmnt':subprocess.getoutput('findmnt /mnt/windows'),'loops':subprocess.getoutput('lsblk -o NAME,SIZE,FSTYPE,RO,TYPE,MOUNTPOINT /dev/loop16'),'dislocker':subprocess.getoutput('pgrep -a dislocker')})
# Inventory Sage/Ciel subtrees without following junctions.
roots=[]
for base in [B/'ProgramData',B/'Program Files',B/'Program Files (x86)',B/'Users/Public/Documents',B/'Users/fintm/Documents',B/'Users/fintm/AppData/Local',B/'Users/fintm/AppData/Roaming']:
 if not base.exists():continue
 for p in base.iterdir():
  if re.search('sage|ciel',p.name,re.I) and p.is_dir(): roots.append(p)
inv=[]
for root in roots:
 for d,ds,fs in os.walk(root,followlinks=False):
  ds[:]=[x for x in ds if not (pathlib.Path(d)/x).is_symlink()]
  for fn in fs:
   p=pathlib.Path(d)/fn
   try:
    s=p.stat();row={'path':str(p.relative_to(B)),'size':s.st_size,'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()};inv.append(row)
    if s.st_size<30_000_000 and p.suffix.lower() in ['.log','.txt','.ini','.xml','.json','.config','.lic','.dat','.sai','.csv','.trace'] and not any(x in str(p).lower() for x in ['/help/','/aide/']):src(p,True)
   except Exception as ex:ERR.append({'path':str(p),'error':str(ex)})
save('sage-inventory.json',inv);print('sage inventory',len(inv),'copied',len(S),flush=True)
# Registry network hardware identity, settings and Sage configuration.
reg=[]
def walk(k,path,hive,depth=0,maxdepth=30):
 row={'hive':hive,'key':path,'lastwrite_utc':str(k.last_written_time),'values':{}}
 for v in k.values:
  try:
   val=v.get_data_as_string() if v.type in [1,2] else v.get_data_as_integer() if v.type in [4,11] else {'hex':(v.data or b'').hex()}
  except Exception:val={'hex':(v.data or b'').hex()}
  row['values'][v.name or '(default)']=val
 reg.append(row)
 if depth<maxdepth:
  for sub in k.sub_keys:walk(sub,path+'\\'+sub.name,hive,depth+1,maxdepth)
branches={'Windows/System32/config/SYSTEM':[r'Select',r'ControlSet001\Control\TimeZoneInformation',r'ControlSet001\Control\Network',r'ControlSet001\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}',r'ControlSet001\Services\Tcpip\Parameters\Interfaces',r'ControlSet001\Enum\USB',r'ControlSet001\Enum\USBSTOR'], 'Windows/System32/config/SOFTWARE':[r'Microsoft\Windows NT\CurrentVersion\NetworkList',r'Microsoft\WlanSvc',r'Sage',r'Ciel',r'WOW6432Node\Sage',r'WOW6432Node\Ciel'], 'Users/fintm/NTUSER.DAT':[r'Software\Sage',r'Software\Ciel',r'Software\Ciel Gestion Commerciale',r'Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2']}
for hp,bs in branches.items():
 try:
  src(B/hp,False);f=pyregf.file();f.open(str(B/hp))
  for b in bs:
   k=f.get_key_by_path(b)
   if k:walk(k,b,hp)
  # top-level Sage-like vendor names, including SAGE with suffixes
  for top in (['Software'] if 'NTUSER' in hp else ['','WOW6432Node'] if hp.endswith('SOFTWARE') else []):
   k=f.get_key_by_path(top) if top else f.root_key
   if k:
    for sub in k.sub_keys:
     if re.search(r'sage|ciel',sub.name,re.I):walk(sub,(top+'\\' if top else '')+sub.name,hp)
  f.close()
 except Exception as ex:ERR.append({'path':hp,'error':str(ex)})
save('registry.json',reg);print('registry',len(reg),flush=True)
# Full EVTX sweep: network day + context; Sage names in every retained record.
ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'};net=[];sage=[];evinv=[]
for p in sorted((B/'Windows/System32/winevt/Logs').glob('*.evtx')):
 try:
  f=pyevtx.file();f.open(str(p));lo=hi=None;day=0;selected=False
  for i in range(f.number_of_records):
   try:
    r=f.get_record(i);t=r.creation_time.replace(tzinfo=datetime.timezone.utc);ts=t.isoformat();lo=min(lo or ts,ts);hi=max(hi or ts,ts)
    if '2024-10-27T23:'<=ts<'2024-10-28T23:':day+=1
    isnet=any(x in p.name for x in ['WLAN','NetworkProfile','Dhcp','NCSI','Wired','WWAN','RasClient','RemoteAccess','USB','DeviceSetupManager','Kernel-PnP']) and '2024-10-13'<=ts<'2024-10-30'
    xml=r.xml_string
    issage=bool(re.search(r'(?i)\bsage\b|\bciel\b|\bwg[ce]\.exe\b|SageID|Sage50',xml))
    if not(isnet or issage):continue
    try:
     e=E.fromstring(xml);provider=e.find('e:System/e:Provider',ns).get('Name');data={v.get('Name',str(j)):v.text for j,v in enumerate(e.findall('e:EventData/e:Data',ns))}
    except Exception:provider='';data={}
    row={'source':p.name,'utc':ts,'paris':t.astimezone(ZoneInfo('Europe/Paris')).isoformat(),'id':r.event_identifier,'record':r.identifier,'provider':provider,'data':data,'xml':xml}
    if isnet:net.append(row)
    if issage:sage.append(row)
    selected=True
   except Exception as ex:ERR.append({'path':p.name,'index':i,'error':str(ex)})
  evinv.append({'source':p.name,'records':f.number_of_records,'first_utc':lo,'last_utc':hi,'records_day_28_paris':day});f.close()
  if selected or p.name in ['Application.evtx','Security.evtx']:src(p,True)
 except Exception as ex:ERR.append({'path':p.name,'error':str(ex)})
save('network-events.json',net);save('sage-events.json',sage);save('evtx-inventory.json',evinv);save('sources.json',S);save('errors.json',ERR)
print('done network',len(net),'sage',len(sage),'errors',len(ERR),flush=True)
