import pathlib,json,hashlib,pyregf,pyesedb,datetime,struct,re,shutil
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/home/sansforensics/analysis/OP-01/extractions-acces-20261013/additional');out.mkdir(parents=True,exist_ok=True);sources=[];errors=[]
for rel in ['Windows/appcompat/Programs/Amcache.hve','Windows/System32/sru/SRUDB.dat']:
 p=base/rel;dest=out/'raw'/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest);sources.append({'source':rel,'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
# Amcache: inventory, not a direct execution assertion.
f=pyregf.file();f.open(str(out/'raw/Windows/appcompat/Programs/Amcache.hve'));rows=[]
for path in [r'Root\InventoryApplication',r'Root\InventoryApplicationFile',r'Root\InventoryApplicationShortcut',r'Root\File',r'Root\Programs']:
 root=f.get_key_by_path(path)
 if not root:continue
 def walk(k,path):
  values=[]
  for v in k.values:
   b=v.data or b'';r={'name':v.name,'type':v.type,'hex':b.hex()}
   try:
    if v.type in [1,2]:r['decoded']=v.get_data_as_string()
    elif v.type in [4,11]:r['decoded']=v.get_data_as_integer()
    elif v.type==7:r['decoded']=list(v.get_data_as_multi_string())
   except Exception as ex:r['decode_error']=str(ex)
   values.append(r)
  rows.append({'key':path,'lastwrite_utc':str(k.last_written_time),'values':values})
  for s in k.sub_keys:walk(s,path+'\\'+s.name)
 walk(root,path)
f.close();(out/'amcache.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print('amcache',len(rows),flush=True)
# SRUM schema and actual coverage. Preserve raw values for selected historic rows.
f=pyesedb.file();f.open(str(out/'raw/Windows/System32/sru/SRUDB.dat'));schema=[];selected=open(out/'srum-historic.jsonl','w');idmap=[]
for ti in range(f.number_of_tables):
 t=f.get_table(ti);cols=[{'name':c.name,'type':c.type} for c in t.columns];times=[];chosen=0
 for ri in range(t.number_of_records):
  try:
   record=t.get_record(ri);values=[];timestamp=None
   for i,c in enumerate(cols):
    b=record.get_value_data(i);v={'name':c['name'],'type':c['type'],'hex':b.hex() if b else None}
    if b:
     try:
      if c['type'] in [2,3,4,5,14,15,17]:v['decoded']=record.get_value_data_as_integer(i)
      elif c['type'] in [10,12]:v['decoded']=record.get_value_data_as_string(i)
      elif c['type']==8 and len(b)==8:
       v['decoded']=(datetime.datetime(1899,12,30,tzinfo=datetime.timezone.utc)+datetime.timedelta(days=struct.unpack('<d',b)[0])).isoformat()
     except Exception as ex:v['decode_error']=str(ex)
    values.append(v)
    if c['name'].lower()=='timestamp':timestamp=v.get('decoded')
   if timestamp:times.append(timestamp)
   row={'table':t.name,'index':ri,'utc':timestamp,'values':values}
   if t.name=='SruDbIdMapTable':idmap.append(row)
   elif timestamp and '2021-01-01'<=timestamp<'2024-10-30':selected.write(json.dumps(row,ensure_ascii=False)+'\n');chosen+=1
  except Exception as ex:errors.append({'table':t.name,'index':ri,'error':str(ex)})
 schema.append({'table':t.name,'records':t.number_of_records,'columns':cols,'first_utc':min(times) if times else None,'last_utc':max(times) if times else None,'historic_selected':chosen});print(t.name,t.number_of_records,chosen,flush=True)
selected.close();f.close();(out/'srum-schema.json').write_text(json.dumps(schema,indent=2));(out/'srum-idmap.json').write_text(json.dumps(idmap,ensure_ascii=False,indent=2));(out/'sources.json').write_text(json.dumps(sources,indent=2));(out/'errors.json').write_text(json.dumps(errors,indent=2))
