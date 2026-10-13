import pathlib,subprocess,xml.etree.ElementTree as E,json,hashlib,datetime,collections
from zoneinfo import ZoneInfo
base=pathlib.Path('/mnt/windows/Windows/System32/winevt/Logs'); out=pathlib.Path('/tmp/OP-01-scelles-20261013'); out.mkdir(exist_ok=True)
ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'}
start='2024-10-13T22:00:00'; end='2024-10-29T23:00:00'
summary=[]; target=out.open if False else open(out/'events.jsonl','w'); raw=open(out/'events.xml','w'); raw.write('<Events>\n')
for f in sorted(base.glob('*.evtx')):
 p=subprocess.Popen(['sudo','-n','evtxexport','-f','xml',str(f)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
 buf=[]; n=0; hit=0; errors=0; lo=None; hi=None; days=collections.Counter()
 for line in p.stdout:
  if line.startswith('<Event '): buf=[line]
  elif buf: buf.append(line)
  if line.strip()!='</Event>' or not buf: continue
  xml=''.join(buf); buf=[]
  try:
   e=E.fromstring(xml); s=e.find('e:System',ns); t=s.find('e:TimeCreated',ns).get('SystemTime'); n+=1; lo=min(lo or t,t); hi=max(hi or t,t)
   if not start<=t<end: continue
   dt=datetime.datetime.fromisoformat(t.replace('Z','+00:00')); local=dt.astimezone(ZoneInfo('Europe/Paris')).isoformat(); days[local[:10]]+=1; hit+=1
   data={x.get('Name',str(i)):x.text for i,x in enumerate(e.findall('e:EventData/e:Data',ns))}
   u=e.find('e:UserData',ns)
   if u is not None: data['UserData']=E.tostring(u,encoding='unicode')
   row={'source':f.name,'utc':t,'paris':local,'provider':s.find('e:Provider',ns).get('Name'),'id':s.findtext('e:EventID',namespaces=ns),'record':s.findtext('e:EventRecordID',namespaces=ns),'version':s.findtext('e:Version',namespaces=ns),'data':data}
   target.write(json.dumps(row,ensure_ascii=False)+'\n'); raw.write(xml)
  except Exception as ex: errors+=1
 stderr=p.stderr.read(); rc=p.wait()
 summary.append({'source':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'size':f.stat().st_size,'events':n,'first':lo,'last':hi,'selected':hit,'days':dict(days),'parse_errors':errors,'returncode':rc,'stderr':stderr})
 print(f.name,n,hit,errors,rc,flush=True)
raw.write('</Events>\n'); raw.close(); target.close(); (out/'inventory.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
