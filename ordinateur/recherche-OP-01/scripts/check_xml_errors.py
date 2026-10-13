import pathlib,json,subprocess,xml.etree.ElementTree as E,re,collections
out=pathlib.Path('/tmp/OP-01-scelles-20261013'); inv=json.loads((out/'inventory.json').read_text()); result=[]
fout=open(out/'xml-errors.jsonl','w')
for item in inv:
 if not item['parse_errors']: continue
 text=subprocess.check_output(['sudo','-n','evtxexport','-f','xml','/mnt/windows/Windows/System32/winevt/Logs/'+item['source']],text=True)
 for x in re.findall(r'<Event .*?</Event>',text,re.S):
  try: E.fromstring(x)
  except Exception as ex:
   t=re.search(r'SystemTime="([^"]+)"',x); rid=re.search(r'<EventRecordID>(.*?)</EventRecordID>',x); t=t[1] if t else None
   row={'source':item['source'],'utc':t,'record':rid[1] if rid else None,'error':str(ex),'xml':x}; fout.write(json.dumps(row)+'\n')
   if t and '2024-10-13T22'<=t<'2024-10-29T23': result.append({k:v for k,v in row.items() if k!='xml'})
fout.close(); (out/'xml-errors-period.json').write_text(json.dumps(result,indent=2)); print('period_errors',len(result));print(json.dumps(result)[:8000])
