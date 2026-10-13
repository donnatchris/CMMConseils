import pathlib,json,csv,re,xml.etree.ElementTree as E,datetime,struct,collections,hashlib
p=pathlib.Path(__file__).resolve().parents[1];ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'};T=json.loads((p/'tasks-inventory.json').read_text());R=json.loads((p/'registry-selected.json').read_text());events=[];logcounts=[]
for f in sorted((p/'logs').glob('*.xml')):
 n=0;bad=0;times=[]
 for raw in re.findall(r'<Event .*?</Event>',f.read_text(),re.S):
  try:e=E.fromstring(raw)
  except Exception:bad+=1;continue
  n+=1;s=e.find('e:System',ns);t=s.find('e:TimeCreated',ns).get('SystemTime');times.append(t);provider=s.find('e:Provider',ns).get('Name');eid=s.findtext('e:EventID',namespaces=ns);data={v.get('Name',str(i)):v.text for i,v in enumerate(e.findall('e:EventData/e:Data',ns))}
  keep=provider=='Microsoft-Windows-Kernel-Power' and eid=='107' and '2024-09-01'<=t<'2024-11-01'
  keep|='Maintenance' in f.name and '2024-10-07'<=t<'2024-10-29'
  keep|='2024-10-15'<=t<'2024-10-16' and f.name!='System.evtx.xml'
  if keep:events.append({'source':f.name[:-4],'utc':t,'id':eid,'record':s.findtext('e:EventRecordID',namespaces=ns),'provider':provider,'data':data})
 logcounts.append({'source':f.name[:-4],'parsed':n,'xml_rejected':bad,'first':min(times) if times else None,'last':max(times) if times else None})
(p/'relevant-events.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in sorted(events,key=lambda r:r['utc'])))
with (p/'wake-capable-tasks.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['task','wake_to_run','enabled_in_xml','registration_date_in_xml','file_mtime_utc','taskcache_guid','taskcache_lastwrite_utc'])
 for task in T:
  if task.get('wake_to_run')!='true':continue
  match=next((r for r in R if '\\TaskCache\\Tasks\\' in r['key'] and any(v.get('decoded')=='\\'+task['path'].replace('/','\\') for v in r['values'] if v['name']=='Path')),None)
  w.writerow([task['path'],task.get('wake_to_run'),task.get('enabled'),task.get('registration_date'),task['mtime_utc'],match['key'].split('\\')[-1] if match else None,match['lastwrite_utc'] if match else None])
delta=datetime.datetime(2024,10,16,3,51,7)-datetime.datetime(1601,1,1);ft=(delta.days*86400+delta.seconds)*10000000+1331631;needle=struct.pack('<Q',ft).hex();selected=[{'hive':r['hive'],'key':r['key'],'value':v['name']} for r in R for v in r['values'] if needle in v['hex']]
summary={'task_files':len(T),'task_xml_errors':sum('error' in t for t in T),'wake_capable':sum(t.get('wake_to_run')=='true' for t in T),'wake_capable_explicitly_disabled':sum(t.get('wake_to_run')=='true' and t.get('enabled')=='false' for t in T),'selected_registry_keys':len(R),'taskcache_task_keys':sum('\\TaskCache\\Tasks\\' in r['key'] for r in R),'exact_target_filetime':ft,'exact_target_le_hex':needle,'exact_target_in_selected_registry_values':selected,'logcounts':logcounts}
(p/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,indent=2))
