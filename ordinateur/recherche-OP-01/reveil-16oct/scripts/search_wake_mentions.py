import pathlib,subprocess,re,json,struct,datetime,hashlib
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/tmp/OP-01-reveil-20261013'); hits=[];stats=[]
for p in sorted((base/'Windows/System32/winevt/Logs').glob('*.evtx')):
 proc=subprocess.Popen(['sudo','-n','evtxexport','-f','xml',str(p)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);buf=[];n=0
 for line in proc.stdout:
  if line.startswith('<Event '):buf=[line]
  elif buf:buf.append(line)
  if line.strip()!='</Event>' or not buf:continue
  raw=''.join(buf);buf=[];n+=1
  if not any(v in raw for v in ['2024-10-16T03:51:07','2024-10-16T05:51:07','2024-10-16 03:51:07','2024-10-16 05:51:07']):continue
  t=re.search(r'SystemTime="([^"]+)"',raw);rid=re.search(r'<EventRecordID>(.*?)</EventRecordID>',raw)
  hits.append({'source':p.name,'utc':t[1] if t else None,'record':rid[1] if rid else None,'xml':raw})
 err=proc.stderr.read();rc=proc.wait();stats.append({'source':p.name,'records':n,'returncode':rc,'stderr':err})
(out/'due-time-mentions.json').write_text(json.dumps(hits,indent=2));(out/'due-time-scan.json').write_text(json.dumps(stats,indent=2));print('mentions',[(r['source'],r['utc'],r['record']) for r in hits],flush=True)
delta=datetime.datetime(2024,10,16,3,51,7)-datetime.datetime(1601,1,1);filetime=(delta.days*86400+delta.seconds)*10000000+1331631
needles={'filetime_le':struct.pack('<Q',filetime),'iso_ascii':b'2024-10-16T03:51:07','iso_utf16le':'2024-10-16T03:51:07'.encode('utf-16le')};result=[]
for hive in ['SOFTWARE','SYSTEM']:
 p=base/'Windows/System32/config'/hive;b=p.read_bytes();row={'hive':hive,'sha256':hashlib.sha256(b).hexdigest(),'patterns':{}}
 for name,needle in needles.items():
  offsets=[];pos=b.find(needle)
  while pos!=-1:offsets.append(pos);pos=b.find(needle,pos+1)
  row['patterns'][name]={'hex':needle.hex(),'offsets':offsets}
 result.append(row)
(out/'hive-due-time-search.json').write_text(json.dumps(result,indent=2));print('hives',result,flush=True)
