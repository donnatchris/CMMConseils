import pathlib,hashlib,json,shutil,re,datetime,collections
import pyevtx
B=pathlib.Path('/mnt/windows');O=pathlib.Path('/home/sansforensics/analysis/OP-01/sage-reseaux-20261113');sources=[]
paths=['Windows/Logs/NetSetup/service.0.etl','Windows/Logs/NetSetup/service.1.etl','Windows/System32/LogFiles/WMI/NetCore.etl','Windows/System32/LogFiles/WMI/WifiDriverIHVSession.etl.002','Windows/INF/oem161.inf','Windows/INF/wceisvista.inf','Windows/System32/winevt/Logs/System.evtx']
for rel in paths:
 p=B/rel;q=O/'raw'/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);q.chmod(0o600);s=p.stat();sources.append({'path':rel,'size':s.st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()})
(O/'reseau-complement-sources.json').write_text(json.dumps(sources,indent=2))
# Only GUID/serial network records; no account or credential searches.
rx=re.compile(r'01D72DD1|479CF457|054B7EF2|3FE87BE0|R58RB2ETQER|RNDIS',re.I);hits=[]
for p in sorted((B/'Windows/System32/winevt/Logs').glob('*.evtx')):
 f=pyevtx.file();f.open(str(p))
 for i in range(f.number_of_records):
  r=f.get_record(i)
  if not datetime.datetime(2024,10,27,23)<=r.creation_time<datetime.datetime(2024,10,28,23):continue
  xml=r.xml_string
  if rx.search(xml):hits.append({'source':p.name,'record':r.identifier,'id':r.event_identifier,'utc':str(r.creation_time),'xml':xml})
 f.close()
(O/'network-guid-events.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2));print('network guid hits',len(hits),flush=True)
