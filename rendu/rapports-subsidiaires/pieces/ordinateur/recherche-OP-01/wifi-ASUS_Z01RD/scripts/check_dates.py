"""Read-only checks of live-image SRUM network tables and WLAN connection events."""
import pathlib,json,datetime,struct,hashlib,re,collections
import pyregf,pyesedb,pyevtx,xml.etree.ElementTree as E
B=pathlib.Path('/mnt/windows');O=pathlib.Path('/home/sansforensics/analysis/OP-01/wifi-ASUS_Z01RD-20261014/datation');O.mkdir(exist_ok=True)
sources=[];errors=[];target=re.compile(r'ASUS[_ -]?Z01R(?:D)?|Z01RD',re.I)
def meta(p):sources.append({'path':str(p.relative_to(B)),'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
reg=[];p=B/'Windows/System32/config/SOFTWARE';meta(p);f=pyregf.file();f.open(str(p))
def walk(k,path):
 vals={}
 for v in k.values:
  b=v.data or b''
  try:val=v.get_data_as_string() if v.type in [1,2] else v.get_data_as_integer() if v.type in [4,11] else {'hex':b.hex()}
  except Exception:val={'hex':b.hex()}
  vals[v.name or '(default)']=val
 reg.append({'key':path,'lastwrite_utc':str(k.last_written_time),'values':vals})
 for sub in k.sub_keys:walk(sub,path+'\\'+sub.name)
for branch in [r'Microsoft\WlanSvc',r'Microsoft\Windows NT\CurrentVersion\NetworkList']:
 k=f.get_key_by_path(branch)
 if k:walk(k,branch)
f.close();(O/'registry-network-mapping.json').write_text(json.dumps(reg,indent=2));registry_hits=[r for r in reg if target.search(json.dumps(r))]
p=B/'Windows/System32/sru/SRUDB.dat';meta(p);f=pyesedb.file();f.open(str(p));tables=[];records=[];id_hits=[]
for t in f.tables:
 if t.name not in ['SruDbIdMapTable','{973F5D5C-1D90-4944-BE8E-24B94231A174}','{DD6636C4-8929-4683-974E-22C046A43763}']:continue
 cols=[{'name':c.name,'type':c.type} for c in t.columns];times=[]
 for ri in range(t.number_of_records):
  try:
   r=t.get_record(ri);d={}
   for i,c in enumerate(cols):
    b=r.get_value_data(i)
    if not b:d[c['name']]=None;continue
    if c['type'] in [2,3,4,5,14,15,17]:v=r.get_value_data_as_integer(i)
    elif c['type'] in [10,12]:v=r.get_value_data_as_string(i)
    elif c['type']==8 and len(b)==8:v=(datetime.datetime(1899,12,30,tzinfo=datetime.timezone.utc)+datetime.timedelta(days=struct.unpack('<d',b)[0])).isoformat()
    else:v={'hex':b.hex(),'utf16le':b.decode('utf-16le',errors='replace') if len(b)%2==0 else None}
    d[c['name']]=v
   row={'table':t.name,'index':ri,'values':d}
   if t.name=='SruDbIdMapTable':
    if target.search(json.dumps(d)):id_hits.append(row)
   else:
    records.append(row)
    if d.get('TimeStamp'):times.append(d['TimeStamp'])
  except Exception as ex:errors.append({'table':t.name,'index':ri,'error':str(ex)})
 tables.append({'table':t.name,'records':t.number_of_records,'columns':cols,'first_utc':min(times) if times else None,'last_utc':max(times) if times else None})
f.close();(O/'srum-network-records.json').write_text(json.dumps(records,indent=2));(O/'srum-schema.json').write_text(json.dumps(tables,indent=2));(O/'srum-idmap-hits.json').write_text(json.dumps(id_hits,indent=2))
p=B/'Windows/System32/winevt/Logs/Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx';meta(p);f=pyevtx.file();f.open(str(p));events=[];counts=collections.Counter();times=[];success_times=[]
for i in range(f.number_of_records):
 try:
  r=f.get_record(i);t=str(r.creation_time);times.append(t);counts[r.event_identifier]+=1
  if r.event_identifier==8001:success_times.append(t)
  if target.search(r.xml_string):events.append({'record':r.identifier,'id':r.event_identifier,'utc':t,'xml':r.xml_string})
 except Exception as ex:errors.append({'event_index':i,'error':str(ex)})
f.close();summary={'wlan_records':len(times),'wlan_first_utc':min(times),'wlan_last_utc':max(times),'wlan_event_ids':dict(counts),'successful_connection_events':len(success_times),'successful_connection_first_utc':min(success_times) if success_times else None,'successful_connection_last_utc':max(success_times) if success_times else None,'wlan_target_matches':len(events),'registry_target_matches':len(registry_hits),'srum_idmap_target_matches':len(id_hits),'errors':errors}
(O/'wlan-target-events.json').write_text(json.dumps(events,indent=2));(O/'registry-target-hits.json').write_text(json.dumps(registry_hits,indent=2));(O/'summary.json').write_text(json.dumps(summary,indent=2));(O/'sources.json').write_text(json.dumps(sources,indent=2));print(json.dumps(summary,indent=2));print(json.dumps(tables,indent=2))
