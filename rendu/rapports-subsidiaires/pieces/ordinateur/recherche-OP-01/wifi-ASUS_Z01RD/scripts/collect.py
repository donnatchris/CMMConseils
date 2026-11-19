import pathlib,json,hashlib,datetime,struct,shutil,subprocess
import xml.etree.ElementTree as E
import pyregf,pyevtx
from zoneinfo import ZoneInfo
B=pathlib.Path('/mnt/windows')
O=pathlib.Path('/home/sansforensics/analysis/OP-01/wifi-ASUS_Z01RD-20261014');O.mkdir(parents=True,exist_ok=True)
target='ASUS_Z01RD'; sources=[];errors=[]
def source(p,copy=False):
 s=p.stat(); row={'path':str(p.relative_to(B)),'size':s.st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()};sources.append(row)
 if copy:
  q=O/'raw'/p.relative_to(B);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);q.chmod(0o600)
 return row
profiles=[]
for p in sorted((B/'ProgramData/Microsoft/Wlansvc').rglob('*.xml')):
 try:
  e=E.fromstring(p.read_bytes());d={x.tag.split('}')[-1]:x.text for x in e.iter() if x.tag.split('}')[-1] in ['name','hex','connectionType','connectionMode','authentication','encryption','protected']}
  hit=target.casefold() in json.dumps(d).casefold();row=source(p,hit);row['fields']=d;row['match']=hit;profiles.append(row)
 except Exception as ex:errors.append({'path':str(p),'error':str(ex)})
(O/'profiles.json').write_text(json.dumps(profiles,indent=2))
reg=[]
def walk(k,path):
 row={'key':path,'lastwrite_utc':str(k.last_written_time),'values':{}}
 for v in k.values:
  b=v.data or b''
  try:
   if v.type in [1,2]: val=v.get_data_as_string()
   elif v.type in [4,11]:val=v.get_data_as_integer()
   else:val={'hex':b.hex()}
  except Exception:val={'hex':b.hex()}
  row['values'][v.name or '(default)']=val
 reg.append(row)
 for sub in k.sub_keys:walk(sub,path+'\\'+sub.name)
p=B/'Windows/System32/config/SOFTWARE';source(p);f=pyregf.file();f.open(str(p))
for branch in [r'Microsoft\Windows NT\CurrentVersion\NetworkList',r'Microsoft\WlanSvc']:
 k=f.get_key_by_path(branch)
 if k:walk(k,branch)
f.close()
(O/'registry.json').write_text(json.dumps(reg,indent=2))
hits=[r for r in reg if target.casefold() in json.dumps(r).casefold()]
(O/'registry-hits.json').write_text(json.dumps(hits,indent=2))
print('Profiles',len(profiles),'matches',sum(x['match'] for x in profiles),'registry matches',len(hits),flush=True)
ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'};inv=[];events=[]
for p in sorted((B/'Windows/System32/winevt/Logs').glob('*.evtx')):
 if not any(t in p.name for t in ['WLAN','NetworkProfile','Dhcp','NCSI']):continue
 source(p,True);f=pyevtx.file();f.open(str(p));count=f.number_of_records;lo=hi=None;hit=0
 for i in range(count):
  try:
   r=f.get_record(i);xml=r.xml_string;t=str(r.creation_time);lo=min(lo or t,t);hi=max(hi or t,t)
   if target.casefold() not in xml.casefold():continue
   e=E.fromstring(xml);data={x.get('Name',str(j)):x.text for j,x in enumerate(e.findall('e:EventData/e:Data',ns))}
   dt=r.creation_time.replace(tzinfo=datetime.timezone.utc)
   events.append({'source':p.name,'utc':t,'paris':dt.astimezone(ZoneInfo('Europe/Paris')).isoformat(),'id':r.event_identifier,'record':r.identifier,'data':data,'xml':xml});hit+=1
  except Exception as ex:errors.append({'path':p.name,'index':i,'error':str(ex)})
 inv.append({'source':p.name,'records':count,'first_utc':lo,'last_utc':hi,'matches':hit});f.close();print(p.name,count,hit,flush=True)
(O/'events.json').write_text(json.dumps(events,indent=2));(O/'event-inventory.json').write_text(json.dumps(inv,indent=2));(O/'sources.json').write_text(json.dumps(sources,indent=2));(O/'errors.json').write_text(json.dumps(errors,indent=2))
(O/'mount-check.txt').write_text(subprocess.check_output(['findmnt','/mnt/windows'],text=True)+subprocess.check_output(['lsblk','-o','NAME,SIZE,FSTYPE,RO,TYPE,MOUNTPOINT','/dev/loop14'],text=True))
print('Done',O,flush=True)
