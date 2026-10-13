import pathlib,pyevtx,json,collections
base=pathlib.Path('/mnt/windows/Windows/System32/winevt/Logs');out=pathlib.Path('/tmp/OP-01-integrite-20261013');rec=open(out/'recovered-complete.jsonl','w');alerts=open(out/'clear-and-audit-complete.jsonl','w');errors=open(out/'recovery-errors.jsonl','w');summ=[]
for p in sorted(base.glob('*.evtx')):
 f=pyevtx.file();row={'source':p.name,'recovered_ok':0,'recovered_failed':0,'allocated_failed':0,'allocated_examined':0,'alerts':0}
 try:
  f.open(str(p));row['recovered_reported']=f.number_of_recovered_records
  for i in range(f.number_of_recovered_records):
   try:
    r=f.get_recovered_record(i);item={'source':p.name,'index':i,'record':r.identifier,'offset':r.offset,'creation_utc':str(r.creation_time),'written_utc':str(r.written_time),'provider':r.source_name,'id':r.event_identifier,'xml':r.xml_string};rec.write(json.dumps(item,ensure_ascii=False)+'\n');row['recovered_ok']+=1
   except Exception as ex:row['recovered_failed']+=1;errors.write(json.dumps({'source':p.name,'kind':'recovered','index':i,'error':str(ex)})+'\n')
  for i in range(f.number_of_records):
   try:
    r=f.get_record(i);row['allocated_examined']+=1
    if r.event_identifier not in [104,1100,1101,1102,1104,1105,1108,4719,4616]:continue
    provider=r.source_name
    if provider=='Microsoft-Windows-Eventlog' and r.event_identifier in [104,1100,1101,1102,1104,1105,1108] or provider=='Microsoft-Windows-Security-Auditing' and r.event_identifier in [4719,4616]:
     alerts.write(json.dumps({'source':p.name,'record':r.identifier,'offset':r.offset,'creation_utc':str(r.creation_time),'provider':provider,'id':r.event_identifier,'xml':r.xml_string},ensure_ascii=False)+'\n');row['alerts']+=1
   except Exception as ex:row['allocated_failed']+=1;errors.write(json.dumps({'source':p.name,'kind':'allocated','index':i,'error':str(ex)})+'\n')
  f.close()
 except Exception as ex:row['error']=str(ex)
 summ.append(row);print(p.name,row['recovered_ok'],row['recovered_failed'],row['alerts'],flush=True)
for f in [rec,alerts,errors]:f.close()
(out/'recovery-summary.json').write_text(json.dumps(summ,indent=2))
