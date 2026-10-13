import pathlib,json,hashlib,datetime,shutil,sqlite3,pyregf,pyscca,pylnk,struct,codecs
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/tmp/OP-01-integrite-20261013/independent');out.mkdir(exist_ok=True);sources=[];results=[];errors=[]
def ft(n):
 if not n:return None
 try:return (datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=n//10)).isoformat()
 except:return None
def meta(p):return {'source':str(p.relative_to(base)),'size':p.stat().st_size,'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def save(p,group):
 dest=out/'raw'/group/p.relative_to(base);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest);m=meta(p);sources.append(m);return dest,m
for p in sorted((base/'Windows/Prefetch').glob('*.pf')):
 try:
  dest,m=save(p,'prefetch');f=pyscca.file();f.open(str(dest));times=[]
  for i in range(8):
   try:n=f.get_last_run_time_as_integer(i);times.append({'slot':i,'filetime':n,'utc':ft(n)})
   except Exception:break
  results.append({'kind':'prefetch','source':m['source'],'executable':f.executable_filename,'version':f.format_version,'run_count':f.run_count,'run_times':times,'file_mtime_utc':m['mtime_utc']});f.close()
 except Exception as ex:errors.append({'source':str(p),'error':str(ex)})
for user in ['fintm','INVITES']:
 home=base/'Users'/user;recent=home/'AppData/Roaming/Microsoft/Windows/Recent'
 for p in sorted(recent.rglob('*.lnk')):
  if not p.is_file():continue
  try:
   dest,m=save(p,'lnk');f=pylnk.file();f.open(str(dest));results.append({'kind':'lnk','source':m['source'],'file_mtime_utc':m['mtime_utc'],'target_creation_utc':ft(f.get_file_creation_time_as_integer()),'target_modification_utc':ft(f.get_file_modification_time_as_integer()),'target_access_utc':ft(f.get_file_access_time_as_integer()),'target':f.local_path,'relative_path':f.relative_path,'arguments':f.command_line_arguments,'corrupted':f.is_corrupted()});f.close()
  except Exception as ex:errors.append({'source':str(p),'error':str(ex)})
 hive=home/'NTUSER.DAT'
 if hive.exists():
  f=pyregf.file();f.open(str(hive));sources.append(meta(hive))
  for path in [r'Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist',r'Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs',r'Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU']:
   key=f.get_key_by_path(path)
   if not key:continue
   def walk(k,path):
    for v in k.values:
     b=v.data or b'';row={'kind':'user_registry','user':user,'key':path,'key_lastwrite_utc':str(k.last_written_time),'value':v.name,'hex':b.hex()}
     if 'UserAssist' in path:
      row['decoded_name']=codecs.decode(v.name,'rot_13');row['data_size']=len(b)
      if len(b)==72:row['run_count']=struct.unpack_from('<I',b,4)[0];row['last_run_filetime']=struct.unpack_from('<Q',b,60)[0];row['last_run_utc']=ft(row['last_run_filetime'])
     results.append(row)
    for sub in k.sub_keys:walk(sub,path+'\\'+sub.name)
   walk(key,path)
  f.close()
 histories=list((home/'AppData/Local/Microsoft/Edge/User Data').glob('*/History'))+list((home/'AppData/Local/Google/Chrome/User Data').glob('*/History'))+list((home/'AppData/Roaming/Mozilla/Firefox/Profiles').glob('*/places.sqlite'))
 for p in histories:
  try:
   dest,m=save(p,'browser')
   for suffix in ['-wal','-shm','-journal']:
    extra=pathlib.Path(str(p)+suffix)
    if extra.exists():save(extra,'browser')
   work=out/'working'/p.relative_to(base);work.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(dest,work)
   for suffix in ['-wal','-shm','-journal']:
    extra=pathlib.Path(str(dest)+suffix)
    if extra.exists():shutil.copyfile(extra,str(work)+suffix)
   con=sqlite3.connect('file:'+str(work)+'?mode=ro',uri=True)
   if p.name=='History':
    counts=con.execute('select count(*),min(visit_time),max(visit_time) from visits').fetchone();results.append({'kind':'browser_coverage','source':m['source'],'visits':counts[0],'first_utc':ft(counts[1]*10) if counts[1] else None,'last_utc':ft(counts[2]*10) if counts[2] else None})
    start=int((datetime.datetime(2024,10,13,22)-datetime.datetime(1601,1,1)).total_seconds()*1e6);end=int((datetime.datetime(2024,10,29,23)-datetime.datetime(1601,1,1)).total_seconds()*1e6)
    for v in con.execute('select v.id,v.visit_time,v.transition,u.url,u.title from visits v join urls u on v.url=u.id where v.visit_time>=? and v.visit_time<? order by v.visit_time',(start,end)):results.append({'kind':'browser_visit','source':m['source'],'visit_id':v[0],'utc':ft(v[1]*10),'transition':v[2],'url':v[3],'title':v[4]})
   else:
    counts=con.execute('select count(*),min(visit_date),max(visit_date) from moz_historyvisits').fetchone();results.append({'kind':'firefox_coverage','source':m['source'],'counts':counts})
   con.close()
  except Exception as ex:errors.append({'source':str(p),'error':str(ex)})
# Current journal configuration, not a reconstruction of 2024.
configs=[]
for hive,paths in [('SOFTWARE',[r'Microsoft\Windows\CurrentVersion\WINEVT\Channels',r'Policies\Microsoft\Windows\EventLog']),('SYSTEM',[r'ControlSet001\Services\Eventlog'])]:
 p=base/'Windows/System32/config'/hive;sources.append(meta(p));f=pyregf.file();f.open(str(p))
 def walk(k,path):
  values=[]
  for v in k.values:
   row={'name':v.name,'type':v.type,'hex':(v.data or b'').hex()}
   try:
    if v.type in [1,2]:row['decoded']=v.get_data_as_string()
    elif v.type in [4,11]:row['decoded']=v.get_data_as_integer()
   except:pass
   values.append(row)
  configs.append({'hive':hive,'key':path,'lastwrite_utc':str(k.last_written_time),'values':values})
  for s in k.sub_keys:walk(s,path+'\\'+s.name)
 for path in paths:
  k=f.get_key_by_path(path)
  if k:walk(k,path)
  else:configs.append({'hive':hive,'key':path,'absent':True})
 f.close()
(out/'results.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in results));(out/'sources.json').write_text(json.dumps(sources,indent=2));(out/'errors.json').write_text(json.dumps(errors,indent=2));(out/'log-config.json').write_text(json.dumps(configs,indent=2));print('sources',len(sources),'results',len(results),'errors',len(errors))
