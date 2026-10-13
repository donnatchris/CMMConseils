import pathlib,pyfsntfs,json,hashlib,struct,datetime,zlib,pyevtx
out=pathlib.Path('/tmp/OP-01-integrite-20261013/ntfs');rows=[json.loads(s) for s in (out/'mft-evtx-records.jsonl').read_text().splitlines() if not json.loads(s)['allocated']];dest=out/'deleted-evtx-data';dest.mkdir(exist_ok=True);v=pyfsntfs.volume();v.open('/mnt/dislocker/dislocker-file');results=[];records=open(out/'deleted-evtx-candidates.jsonl','w');total=0
for row in rows:
 idx=row['mft_index'];name=next((n['name'] for n in row['names'] if n['name'].lower().endswith('.evtx')),str(idx));r={'mft_index':idx,'sequence':row['sequence'],'name':name,'record_allocated':row['allocated'],'SI':row['SI'],'reconstructed_paths':[n['path'] for n in row['names'] if n['namespace']!=2]}
 try:
  f=v.get_file_entry(idx);r['data_size']=f.size;r['extents']=[f.get_extent(i) for i in range(f.number_of_extents)]
  if f.size>64*1024*1024 or total+f.size>1024*1024*1024:r['skipped']='size_cap';results.append(r);continue
  b=f.read_buffer_at_offset(f.size,0);total+=len(b);p=dest/(str(idx)+'-'+name);p.write_bytes(b);r['copied_size']=len(b);r['sha256']=hashlib.sha256(b).hexdigest();r['file_signature_valid']=b[:8]==b'ElfFile\0';r['chunk_signatures']=[];r['records']=0;pos=b.find(b'ElfChnk\0')
  while pos!=-1:
   if pos+65536<=len(b):
    c=b[pos:pos+65536];free=struct.unpack_from('<I',c,48)[0];r['chunk_signatures'].append(pos)
    if 512<=free<=65536:
     off=512
     while off+28<=free and c[off:off+4]==b'**\0\0':
      size=struct.unpack_from('<I',c,off+4)[0]
      if size<28 or off+size>free or struct.unpack_from('<I',c,off+size-4)[0]!=size:break
      rid,t=struct.unpack_from('<QQ',c,off+8)
      try:utc=(datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=t//10)).isoformat()
      except:utc=None
      records.write(json.dumps({'mft_index':idx,'name':name,'recovered_file_offset':pos+off,'record':rid,'written_utc':utc,'chunk_crc_header_ok':struct.unpack_from('<I',c,124)[0]==zlib.crc32(c[:120]+c[128:512]),'chunk_crc_data_ok':struct.unpack_from('<I',c,52)[0]==zlib.crc32(c[512:free]),'raw_hex':c[off:off+size].hex()})+'\n');r['records']+=1;off+=size
   pos=b.find(b'ElfChnk\0',pos+8)
 except Exception as ex:r['error']=str(ex)
 results.append(r);print(idx,name,r.get('copied_size'),len(r.get('chunk_signatures',[])),flush=True)
records.close();v.close();(out/'deleted-evtx-summary.json').write_text(json.dumps(results,ensure_ascii=False,indent=2));print('files',len(results),'bytes',total,'headers',sum(r.get('file_signature_valid',False) for r in results),'chunks',sum(len(r.get('chunk_signatures',[])) for r in results),'records',sum(r.get('records',0) for r in results))
