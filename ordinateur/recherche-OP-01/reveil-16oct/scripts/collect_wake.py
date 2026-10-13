import pathlib,hashlib,json,datetime,xml.etree.ElementTree as E,pyregf,subprocess,re,shutil
out=pathlib.Path('/tmp/OP-01-reveil-20261013');out.mkdir(exist_ok=True); base=pathlib.Path('/mnt/windows'); tasks=base/'Windows/System32/Tasks'; records=[]; ns={'t':'http://schemas.microsoft.com/windows/2004/02/mit/task'}
for p in sorted(tasks.rglob('*')):
 if not p.is_file(): continue
 raw=p.read_bytes(); rel=p.relative_to(tasks); dest=out/'tasks'/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
 r={'path':str(rel),'sha256':hashlib.sha256(raw).hexdigest(),'size':len(raw),'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat()}
 try:
  e=E.fromstring(raw);r.update({'registration_date':e.findtext('t:RegistrationInfo/t:Date',namespaces=ns),'author':e.findtext('t:RegistrationInfo/t:Author',namespaces=ns),'wake_to_run':e.findtext('t:Settings/t:WakeToRun',namespaces=ns),'enabled':e.findtext('t:Settings/t:Enabled',namespaces=ns),'triggers':E.tostring(e.find('t:Triggers',ns),encoding='unicode') if e.find('t:Triggers',ns) is not None else None,'actions':E.tostring(e.find('t:Actions',ns),encoding='unicode') if e.find('t:Actions',ns) is not None else None,'settings':E.tostring(e.find('t:Settings',ns),encoding='unicode') if e.find('t:Settings',ns) is not None else None})
 except Exception as ex:r['error']=str(ex)
 records.append(r)
(out/'tasks-inventory.json').write_text(json.dumps(records,ensure_ascii=False,indent=2));print('tasks',len(records),'wake',sum(r.get('wake_to_run')=='true' for r in records),flush=True)
reg=[]; reginfo=[]
for hive,paths in [('SOFTWARE',[r'Microsoft\Windows NT\CurrentVersion\Schedule',r'Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update',r'Microsoft\Windows\CurrentVersion\WindowsUpdate\Orchestrator']),('SYSTEM',[r'Select',r'ControlSet001\Control\Power'])]:
 p=base/'Windows/System32/config'/hive;f=pyregf.file();f.open(str(p));reginfo.append({'hive':hive,'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pyregf_version':pyregf.get_version()})
 def walk(k,path):
  row={'hive':hive,'key':path,'lastwrite_utc':str(k.get_last_written_time()),'lastwrite_filetime':k.get_last_written_time_as_integer(),'values':[]}
  for v in k.values:
   value={'name':v.name,'type':v.type,'hex':v.data.hex() if v.data else ''}
   try:
    if v.type in [1,2,6]:value['decoded']=v.get_data_as_string()
    elif v.type==7:value['decoded']=list(v.get_data_as_multi_string())
    elif v.type in [4,5,11]:value['decoded']=v.get_data_as_integer()
   except Exception as ex:value['decode_error']=str(ex)
   row['values'].append(value)
  reg.append(row)
  for sub in k.sub_keys:walk(sub,path+'\\'+sub.name)
 for path in paths:
  try:k=f.get_key_by_path(path)
  except Exception as ex:reginfo.append({'hive':hive,'path':path,'error':str(ex)});continue
  if k:walk(k,path)
  else:reginfo.append({'hive':hive,'path':path,'absent':True})
 f.close()
(out/'registry-selected.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2));(out/'registry-sources.json').write_text(json.dumps(reginfo,indent=2));print('registry keys',len(reg),flush=True)
logs=base/'Windows/System32/winevt/Logs';src=[]
for name in ['System.evtx','Microsoft-Windows-TaskScheduler%4Maintenance.evtx','Microsoft-Windows-WindowsUpdateClient%4Operational.evtx','Microsoft-Windows-BackgroundTaskInfrastructure%4Operational.evtx']:
 p=logs/name; dest=out/'logs'/name;dest.parent.mkdir(exist_ok=True);shutil.copyfile(p,dest)
 with open(out/'logs'/(name+'.xml'),'w') as f:rc=subprocess.run(['sudo','-n','evtxexport','-f','xml',str(p)],stdout=f,stderr=subprocess.PIPE,text=True)
 src.append({'source':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'returncode':rc.returncode,'stderr':rc.stderr})
(out/'log-sources.json').write_text(json.dumps(src,indent=2));print('logs done')
