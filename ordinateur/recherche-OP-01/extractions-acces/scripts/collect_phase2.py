import pathlib,json,hashlib,datetime,os,re,pyregf,shutil,pyevtx,xml.etree.ElementTree as E,collections
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/home/sansforensics/analysis/OP-01/extractions-acces-20261013');out.mkdir(parents=True,exist_ok=True);err=[];sources=[]
def meta(p):return {'source':str(p.relative_to(base)),'size':p.stat().st_size,'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def save(p):
 dest=out/'raw'/p.relative_to(base);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest);sources.append(meta(p));return dest
files=[]
for p in sorted((base/'L16B').rglob('*')):
 if not p.is_file():continue
 st=p.stat();files.append({'path':str(p.relative_to(base)),'size':st.st_size,'mtime_utc':datetime.datetime.fromtimestamp(st.st_mtime,datetime.timezone.utc).isoformat(),'inode':st.st_ino})
(out/'l16b-inventory.json').write_text(json.dumps(files,ensure_ascii=False,indent=2));print('L16B files',len(files),flush=True)
reg=[]
branches={'SYSTEM':[r'Select',r'MountedDevices',r'ControlSet001\Enum\USBSTOR',r'ControlSet001\Enum\SCSI',r'ControlSet001\Enum\USB',r'ControlSet001\Enum\SWD\WPDBUSENUM',r'ControlSet001\Control\DeviceClasses\{53f56307-b6bf-11d0-94f2-00a0c91efb8b}',r'ControlSet001\Control\Terminal Server',r'ControlSet001\Control\Lsa',r'ControlSet001\Services'], 'SOFTWARE':[r'Microsoft\Windows\CurrentVersion\Uninstall',r'WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall',r'Microsoft\Windows\CurrentVersion\Run',r'Microsoft\Windows\CurrentVersion\RunOnce',r'WOW6432Node\Microsoft\Windows\CurrentVersion\Run',r'Microsoft\Windows NT\CurrentVersion\Winlogon',r'Microsoft\Windows NT\CurrentVersion\ProfileList',r'Microsoft\Windows\CurrentVersion\Policies\System',r'Policies\Microsoft\Windows\WinRM',r'Microsoft\Windows\CurrentVersion\App Paths']}
for user in ['fintm','INVITES']:
 branches['NTUSER:'+user]=[r'Software\Microsoft\Windows\CurrentVersion\Run',r'Software\Microsoft\Windows\CurrentVersion\RunOnce',r'Software\Microsoft\Windows\CurrentVersion\Explorer\MountPoints2',r'Software\Microsoft\Terminal Server Client',r'Software\Microsoft\Windows\CurrentVersion\Explorer\ComDlg32',r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',r'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU',r'Software\Microsoft\Windows\CurrentVersion\Explorer\TypedPaths']
for label,paths in branches.items():
 p=base/'Windows/System32/config'/label if not label.startswith('NTUSER:') else base/'Users'/label.split(':')[1]/'NTUSER.DAT';f=pyregf.file();f.open(str(p));sources.append(meta(p))
 def walk(k,path):
  row={'hive':label,'key':path,'lastwrite_utc':str(k.last_written_time),'values':[]}
  for v in k.values:
   b=v.data or b'';item={'name':v.name,'type':v.type,'hex':b.hex()}
   try:
    if v.type in [1,2]:item['decoded']=v.get_data_as_string()
    elif v.type==7:item['decoded']=list(v.get_data_as_multi_string())
    elif v.type in [4,11]:item['decoded']=v.get_data_as_integer()
   except Exception as ex:item['decode_error']=str(ex)
   row['values'].append(item)
  reg.append(row)
  for sub in k.sub_keys:walk(sub,path+'\\'+sub.name)
 for path in paths:
  k=f.get_key_by_path(path)
  if k:walk(k,path)
  else:reg.append({'hive':label,'key':path,'absent':True})
 f.close()
(out/'registry.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2));print('registry',len(reg),flush=True)
# Bounded inventory of software footprints, never execute evidence programs.
rx=re.compile(r'anydesk|teamviewer|screenconnect|rustdesk|ultraview|tightvnc|ultravnc|realvnc|radmin|splashtop|remotepc|logmein|dwagent|meshagent|atera|netsupport|ngrok|rclone|winscp|filezilla|ldsd|amcache',re.I);software=[]
for root in [base/'Program Files',base/'Program Files (x86)',base/'ProgramData',base/'Users/fintm/AppData',base/'Windows/AppCompat',base/'Windows/appcompat']:
 if not root.exists():continue
 for dp,dirs,names in os.walk(root):
  depth=len(pathlib.Path(dp).relative_to(root).parts)
  if depth>=5:dirs[:]=[]
  for n in dirs+names:
   if rx.search(n):
    p=pathlib.Path(dp)/n;st=p.stat();software.append({'path':str(p.relative_to(base)),'is_directory':p.is_dir(),'size':st.st_size,'mtime_utc':datetime.datetime.fromtimestamp(st.st_mtime,datetime.timezone.utc).isoformat()})
(out/'software-footprints.json').write_text(json.dumps(software,indent=2))
# Raw connection/install evidence and portable application traces.
for p in [base/'Windows/INF/setupapi.dev.log',base/'Windows/appcompat/Programs/Amcache.hve',base/'Windows/System32/sru/SRUDB.dat']:
 if p.exists():save(p)
for user in ['fintm','INVITES','Public']:
 for rel in ['AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt','AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup','Desktop']:
  path=base/'Users'/user/rel
  if path.is_file():save(path)
  elif path.is_dir():
   for p in path.iterdir():
    if p.is_file() and (rel.endswith('Startup') or p.suffix.lower() in ['.rdp','.bat','.cmd','.ps1']):save(p)
# Full, selected historic channels; XML retained even for non-conforming EventData.
logs=base/'Windows/System32/winevt/Logs';summary=[];events=open(out/'events.jsonl','w')
for p in sorted(logs.glob('*.evtx')):
 name=p.name
 if name not in ['System.evtx','Application.evtx','Security.evtx','Windows PowerShell.evtx'] and not any(t in name for t in ['PowerShell%4','WinRM%4','SMBServer%4Security','SmbClient%4Security','SmbClient%4Connectivity','Windows Defender%4Operational','TerminalServices-LocalSessionManager%4Operational','NetworkProfile%4Operational','WLAN-AutoConfig%4Operational']):continue
 save(p);f=pyevtx.file();f.open(str(p));selected=0
 for i in range(f.number_of_records):
  try:
   r=f.get_record(i);t=str(r.creation_time);provider=r.source_name;eid=r.event_identifier;xml=r.xml_string
   keep=name not in ['System.evtx','Application.evtx','Security.evtx'] or provider=='Service Control Manager' and eid in [7045,7040] or provider in ['MsiInstaller','Microsoft-Windows-Security-Auditing','Microsoft-Windows-Eventlog'] or rx.search(xml) is not None
   if keep:
    events.write(json.dumps({'source':name,'utc':t,'provider':provider,'id':eid,'record':r.identifier,'xml':xml},ensure_ascii=False)+'\n');selected+=1
  except Exception as ex:err.append({'source':name,'index':i,'error':str(ex)})
 summary.append({'source':name,'records':f.number_of_records,'selected':selected});f.close();print(name,selected,flush=True)
events.close();(out/'event-sources.json').write_text(json.dumps(summary,indent=2));(out/'sources.json').write_text(json.dumps(sources,ensure_ascii=False,indent=2));(out/'errors.json').write_text(json.dumps(err,indent=2));print('done')
