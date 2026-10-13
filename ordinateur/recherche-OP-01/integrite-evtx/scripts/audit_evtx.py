import pathlib,struct,zlib,json,datetime,collections,pyevtx,re
base=pathlib.Path('/mnt/windows/Windows/System32/winevt/Logs');out=pathlib.Path('/tmp/OP-01-integrite-20261013');out.mkdir(exist_ok=True)
U32=lambda b,o:struct.unpack_from('<I',b,o)[0]; U64=lambda b,o:struct.unpack_from('<Q',b,o)[0]
def ft(n):
 try:return (datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=n//10)).isoformat()
 except:return None
summary=[];chunkout=open(out/'chunks.jsonl','w');recout=open(out/'records-binary.jsonl','w');recovered=open(out/'recovered.jsonl','w');slackout=open(out/'slack-candidates.jsonl','w');alerts=open(out/'clear-and-audit-events.jsonl','w');errors=[]
for f in sorted(base.glob('*.evtx')):
 b=f.read_bytes(); row={'source':f.name,'size':len(b),'signature':b[:8].hex(),'first_chunk_number':U64(b,8),'last_chunk_number':U64(b,16),'next_record_id':U64(b,24),'header_chunks':struct.unpack_from('<H',b,42)[0],'physical_chunks':(len(b)-4096)//65536,'file_flags':U32(b,120),'header_crc_stored':U32(b,124),'header_crc_computed':zlib.crc32(b[:120])&0xffffffff}; row['header_crc_ok']=row['header_crc_stored']==row['header_crc_computed'];ids=[];dates=[];badchunks=[];badrecords=[];targetchunks=[];slackcount=0;validchunks=0
 for idx in range(row['physical_chunks']):
  c=b[4096+idx*65536:4096+(idx+1)*65536]
  if c[:8]!=b'ElfChnk\0':continue
  validchunks+=1;free=U32(c,48);last=U32(c,44); cr={'source':f.name,'chunk_index':idx,'first_record_number':U64(c,8),'last_record_number':U64(c,16),'first_id':U64(c,24),'last_id':U64(c,32),'last_record_offset':last,'free_offset':free,'flags':U32(c,120),'header_crc_stored':U32(c,124),'header_crc_computed':zlib.crc32(c[:120]+c[128:512])&0xffffffff,'data_crc_stored':U32(c,52)};cr['header_crc_ok']=cr['header_crc_stored']==cr['header_crc_computed'];cr['data_crc_computed']=zlib.crc32(c[512:free])&0xffffffff if 512<=free<=65536 else None;cr['data_crc_ok']=cr['data_crc_stored']==cr['data_crc_computed'];offset=512;chunkrecords=[]
  if not cr['header_crc_ok'] or not cr['data_crc_ok']:badchunks.append(idx)
  while 512<=free<=65536 and offset+28<=free:
   if c[offset:offset+4]!=b'**\0\0':break
   size=U32(c,offset+4)
   if size<28 or offset+size>free:badrecords.append({'chunk':idx,'offset':offset,'problem':'invalid_size','size':size});break
   rid=U64(c,offset+8);time=ft(U64(c,offset+16));trailer=U32(c,offset+size-4)==size
   r={'source':f.name,'chunk_index':idx,'offset':4096+idx*65536+offset,'chunk_offset':offset,'size':size,'record':rid,'written_utc':time,'size_trailer_ok':trailer};recout.write(json.dumps(r)+'\n');ids.append(rid);dates.append(time);chunkrecords.append(r)
   if not trailer:badrecords.append({'chunk':idx,'offset':offset,'problem':'size_trailer'})
   if time and '2024-10-13T22'<=time<'2024-10-29T23' and idx not in targetchunks:targetchunks.append(idx)
   offset+=size
  cr['record_count']=len(chunkrecords);cr['parsed_end']=offset;cr['sequence_bad']=[(a['record'],z['record']) for a,z in zip(chunkrecords,chunkrecords[1:]) if z['record']!=a['record']+1];cr['first_id_matches']=not chunkrecords or chunkrecords[0]['record']==cr['first_id'];cr['last_id_matches']=not chunkrecords or chunkrecords[-1]['record']==cr['last_id'];chunkout.write(json.dumps(cr)+'\n')
  if 512<=free<=65536:
   pos=c.find(b'**\0\0',free)
   while pos!=-1 and pos+28<=len(c):
    size=U32(c,pos+4)
    if size>=28 and pos+size<=len(c) and U32(c,pos+size-4)==size:
     rid=U64(c,pos+8);n=U64(c,pos+16);time=ft(n)
     if time and '2000'<=time[:4]<='2026':slackcount+=1;slackout.write(json.dumps({'source':f.name,'chunk_index':idx,'offset':4096+idx*65536+pos,'size':size,'record':rid,'written_utc':time,'raw_hex':c[pos:pos+size].hex()})+'\n')
    pos=c.find(b'**\0\0',pos+4)
 row.update({'valid_chunk_signatures':validchunks,'raw_records':len(ids),'min_id':min(ids) if ids else None,'max_id':max(ids) if ids else None,'unique_ids':len(set(ids)),'duplicate_ids':len(ids)-len(set(ids)),'binary_first_utc':min(t for t in dates if t) if any(dates) else None,'binary_last_utc':max(t for t in dates if t) if any(dates) else None,'bad_crc_chunks':badchunks,'bad_record_sizes':badrecords,'target_chunks':targetchunks,'slack_candidates':slackcount})
 sortedids=sorted(set(ids));row['id_gaps']=[{'after':a,'before':z,'missing':z-a-1} for a,z in zip(sortedids,sortedids[1:]) if z>a+1]
 try:
  ev=pyevtx.file();ev.open(str(f));row.update({'libevtx_corrupted':ev.is_corrupted(),'libevtx_records':ev.number_of_records,'libevtx_recovered':ev.number_of_recovered_records})
  for r in ev.recovered_records:
   try: recovered.write(json.dumps({'source':f.name,'record':r.identifier,'offset':r.offset,'creation_utc':str(r.creation_time),'written_utc':str(r.written_time),'provider':r.source_name,'id':r.event_identifier,'xml':r.xml_string},ensure_ascii=False)+'\n')
   except Exception as ex:errors.append({'source':f.name,'operation':'recovered_record','error':str(ex)})
  for r in ev.records:
   if (r.source_name=='Microsoft-Windows-Eventlog' and r.event_identifier in [104,1100,1101,1102,1104,1105,1108]) or (r.source_name=='Microsoft-Windows-Security-Auditing' and r.event_identifier in [4719,4616]):
    try:alerts.write(json.dumps({'source':f.name,'record':r.identifier,'creation_utc':str(r.creation_time),'provider':r.source_name,'id':r.event_identifier,'xml':r.xml_string},ensure_ascii=False)+'\n')
    except Exception as ex:errors.append({'source':f.name,'operation':'audit_record','error':str(ex)})
  ev.close()
 except Exception as ex:row['libevtx_error']=str(ex)
 summary.append(row);print(f.name,'raw',len(ids),'crc_bad',len(badchunks),'recovered',row.get('libevtx_recovered'),flush=True)
for f in [chunkout,recout,recovered,slackout,alerts]:f.close()
(out/'structure-summary.json').write_text(json.dumps(summary,indent=2));(out/'errors.json').write_text(json.dumps(errors,indent=2))
