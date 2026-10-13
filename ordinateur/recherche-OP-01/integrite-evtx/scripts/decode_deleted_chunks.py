import pathlib,json,struct,zlib,hashlib,pyevtx,collections
root=pathlib.Path('/tmp/OP-01-integrite-20261013/ntfs');rows=json.loads((root/'deleted-evtx-summary.json').read_text());chunkmap=collections.defaultdict(list)
for f in pathlib.Path('/mnt/windows/Windows/System32/winevt/Logs').glob('*.evtx'):
 b=f.read_bytes()
 for i in range((len(b)-4096)//65536):
  c=b[4096+i*65536:4096+(i+1)*65536]
  if c[:8]==b'ElfChnk\0':chunkmap[hashlib.sha256(c).hexdigest()].append({'source':f.name,'chunk_index':i})
containers=root/'derived-containers';containers.mkdir(exist_ok=True);events=open(root/'deleted-chunks-decoded.jsonl','w');mapping=[];summary=[]
for r in rows:
 if not r.get('chunk_signatures'):continue
 p=root/'deleted-evtx-data'/(str(r['mft_index'])+'-'+r['name']);b=p.read_bytes();chunks=[];ids=[]
 for off in r['chunk_signatures']:
  c=b[off:off+65536];chunks.append(c);ids.append(struct.unpack_from('<Q',c,32)[0]);mapping.append({'mft_index':r['mft_index'],'recovered_name':r['name'],'recovered_offset':off,'chunk_sha256':hashlib.sha256(c).hexdigest(),'identical_current_chunks':chunkmap.get(hashlib.sha256(c).hexdigest(),[])})
 # Derived parsing container: synthetic file header, original chunks unchanged.
 h=bytearray(4096);h[:8]=b'ElfFile\0';struct.pack_into('<QQQIHHHH',h,8,0,len(chunks)-1,max(ids)+1,128,2,3,4096,len(chunks));struct.pack_into('<I',h,124,zlib.crc32(h[:120]));dest=containers/(str(r['mft_index'])+'.derived.evtx');dest.write_bytes(bytes(h)+b''.join(chunks));f=pyevtx.file();s={'mft_index':r['mft_index'],'chunks':len(chunks),'decoded':0,'failed':0,'synthetic_header':True}
 try:
  f.open(str(dest));s['reported_records']=f.number_of_records
  for i in range(f.number_of_records):
   try:
    rec=f.get_record(i);events.write(json.dumps({'mft_index':r['mft_index'],'nominal_old_filename':r['name'],'record':rec.identifier,'creation_utc':str(rec.creation_time),'written_utc':str(rec.written_time),'provider':rec.source_name,'id':rec.event_identifier,'xml':rec.xml_string},ensure_ascii=False)+'\n');s['decoded']+=1
   except Exception as ex:s['failed']+=1;s.setdefault('errors',[]).append({'index':i,'error':str(ex)})
  f.close()
 except Exception as ex:s['open_error']=str(ex)
 summary.append(s)
events.close();(root/'deleted-chunk-correspondence.json').write_text(json.dumps(mapping,indent=2));(root/'deleted-decode-summary.json').write_text(json.dumps(summary,indent=2));print([(s['mft_index'],s['decoded'],s['failed'],s.get('reported_records')) for s in summary]);print('chunks matched current',sum(bool(m['identical_current_chunks']) for m in mapping),'/',len(mapping))
