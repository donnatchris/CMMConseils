import pathlib,json,hashlib,collections,pyfsntfs,datetime,struct
root=pathlib.Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013');raw=root/'recovered';raw.mkdir(exist_ok=True);v=pyfsntfs.volume();v.open('/mnt/dislocker/dislocker-file');bitmap=v.get_file_entry(6);bits=bitmap.read_buffer_at_offset(bitmap.size,0);cluster=v.cluster_block_size;counts=collections.Counter();total=0;output=(root/'recovery-results.jsonl').open('w');cap=64*1024*1024;global_cap=12*1024**3
(root/'bitmap-source.json').write_text(json.dumps({'mft_index':6,'size':len(bits),'sha256':hashlib.sha256(bits).hexdigest(),'cluster_size':cluster,'libfsntfs':pyfsntfs.get_version(),'per_file_cap':cap,'total_read_cap':global_cap},indent=2))
def kind(b):
 if b[:8]==b'ElfFile\0':return 'EVTX'
 if b.startswith(b'%PDF-'):return 'PDF'
 if b.startswith(b'PK\x03\x04') or b.startswith(b'PK\x05\x06'):return 'ZIP'
 if b.startswith(b'SQLite format 3\0'):return 'SQLite'
 if b[:8]==bytes.fromhex('d0cf11e0a1b11ae1'):return 'OLE'
 if b[:20]==bytes.fromhex('4c0000000114020000000000c000000000000046'):return 'LNK'
 if b.startswith(b'!BDN'):return 'PST_OST'
 if b.startswith(b'MZ'):return 'PE'
 if b[:3]==b'MAM' or b[4:8]==b'SCCA':return 'Prefetch'
 if not b or not b.strip(b'\0'):return 'ZERO'
 return 'other'
for num,line in enumerate((root/'recovery-selection.jsonl').open()):
 row=json.loads(line);r={k:row[k] for k in ['mft_index','sequence','allocated','preferred_path','parent_uncertain','SI','extension','selection_reasons','logical_size_from_mft']};idx=row['mft_index']
 try:
  f=v.get_file_entry(idx);r['native_size']=f.size;r['extents']=[f.get_extent(i) for i in range(f.number_of_extents)];allocated=0;clusters=0;unknown=0
  for offset,length,flags in r['extents']:
   if flags or offset<0:unknown+=length;continue
   for c in range(offset//cluster,(offset+length+cluster-1)//cluster):
    clusters+=1
    if c//8>=len(bits):unknown+=cluster
    else:allocated+=(bits[c//8]>>(c%8))&1
  r.update({'extent_clusters':clusters,'clusters_currently_allocated':allocated,'allocation_unknown_bytes':unknown,'data_resident':not r['extents']})
  if total+min(f.size,cap)>global_cap:r['skipped']='total_read_cap'
  else:
   n=min(f.size,cap);b=f.read_buffer_at_offset(n,0);total+=len(b);r.update({'read_bytes':len(b),'complete_logical_read':len(b)==f.size,'sha256_read_bytes':hashlib.sha256(b).hexdigest(),'nonzero_bytes':len(b)-b.count(0),'signature':kind(b),'header_hex':b[:64].hex()})
   if r['nonzero_bytes']:
    path=raw/(str(idx)+'.bin');path.write_bytes(b);r['recovered_file']=str(path.relative_to(root))
   if row['preferred_path'].split('\\')[-1].startswith('$I') and len(b)>=24 and struct.unpack_from('<Q',b)[0] in [1,2]:
    version,size,ft=struct.unpack_from('<QQQ',b);start=28 if version==2 else 24
    path=b[start:].decode('utf-16le','replace').split('\0',1)[0];r['recycle_info']={'version':version,'original_size':size,'deletion_filetime':ft,'deletion_utc':(datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=ft//10)).isoformat(),'original_path':path}
 except Exception as ex:r['error']=str(ex)
 counts[r.get('signature',r.get('skipped','error'))]+=1;output.write(json.dumps(r,ensure_ascii=False)+'\n');output.flush()
 if num%100==0:print('processed',num+1,'bytes',total,'counts',dict(counts),flush=True)
output.close();v.close();(root/'recovery-summary.json').write_text(json.dumps({'counts':counts,'bytes_read':total,'processed':num+1},indent=2));print('DONE',num+1,total,dict(counts),flush=True)
