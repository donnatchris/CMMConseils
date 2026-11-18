import pathlib,json,re,uuid,collections
from dissect.etl import ETL,Buffer
O=pathlib.Path(__file__).resolve().parents[1];P=O/'preuves';summ=[];hits=[];errs=[]
guids=['01d72dd1-9584-43ce-b52e-bc555d29936a','479cf457-af75-4cdc-8c88-124c0693b5f6','054b7ef2-df55-45f0-8cb6-19e42a42eeb3','3fe87be0-2003-4582-91ec-342b21078fbb']
for rel in ['Windows/Logs/NetSetup/service.0.etl','Windows/Logs/NetSetup/service.1.etl','Windows/System32/LogFiles/WMI/NetCore.etl','Windows/System32/LogFiles/WMI/WifiDriverIHVSession.etl.002']:
 p=P/rel;count=0;lo=hi=None;day=0;target=0
 try:
  etl=ETL(p.open('rb'))
  physical=rel.endswith('NetCore.etl')
  buffers=(Buffer(etl,o) for o in range(0,p.stat().st_size,etl.buffer_size)) if physical else etl.buffers()
  for bi,buf in enumerate(buffers):
   if physical and (buf.header.BufferSize!=etl.buffer_size or buf.header.FilledBytes<72):continue
   offset=0
   try:
    for record in buf:
     count+=1;h=record.header;t=h.timestamp.isoformat();lo=min(lo or t,t);hi=max(hi or t,t);payload=bytes(h.payload)
     if '2024-10-27T23:'<=t<'2024-10-28T23:':day+=1
     match=[g for g in guids if uuid.UUID(g).bytes_le in payload or g.encode('utf-16le') in payload.lower()]
     if match or (rel.endswith('NetCore.etl') and (b'R\x005\x008\x00R\x00B\x002\x00E\x00T\x00Q\x00E\x00R' in payload)):
      target+=1
      row={'source':rel,'buffer_index':bi,'buffer_offset':buf.offset,'record_offset_within_buffer_data':offset,'utc':t,'provider_guid':str(h.provider_id),'descriptor':str(getattr(h,'descriptor',None)),'matched_guids':match,'payload_hex':payload.hex()}
      try:
       ev=record.event;row['provider_name']=ev.provider_name();row['symbol']=ev.symbol();row['struct']=str(ev._struct);row['fields']=getattr(ev._struct,'__values__',{}) if ev._struct else {}
      except Exception as ex:row['decode_error']=str(ex)
      row['utf16_strings']=[x.decode('utf-16le',errors='replace') for x in re.findall(rb'(?:[\x20-\x7e]\x00){4,}',payload)]
      hits.append(row)
     offset+=record.aligned_size
   except Exception as ex:errs.append({'source':rel,'buffer':bi,'error':str(ex)})
  summ.append({'source':rel,'etl_start':str(etl.start),'etl_end':str(etl.end),'physical_buffer_scan':physical,'records':count,'first_event_utc':lo,'last_event_utc':hi,'day28_paris_records':day,'target_records':target})
 except Exception as ex:errs.append({'source':rel,'error':str(ex)})
(O/'resultats/etl-summary.json').write_text(json.dumps(summ,indent=2));(O/'resultats/etl-target-events.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2,default=str));(O/'resultats/etl-errors.json').write_text(json.dumps(errs,indent=2));print(json.dumps(summ,indent=2));print('errors',len(errs),'hits',len(hits))
