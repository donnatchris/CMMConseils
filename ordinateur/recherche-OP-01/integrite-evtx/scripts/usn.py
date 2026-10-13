import pyfsntfs,pathlib,struct,json,hashlib,datetime,collections
out=pathlib.Path('/tmp/OP-01-integrite-20261013/ntfs');out.mkdir(exist_ok=True);v=pyfsntfs.volume();v.open('/mnt/dislocker/dislocker-file');f=v.get_file_entry(155201);s=f.get_alternate_data_stream_by_name('$J');meta={'mft_index':155201,'logical_size':s.size,'extents':[],'pyfsntfs':pyfsntfs.get_version()};logical=0;regions=[]
for i in range(s.number_of_extents):
 off,size,flags=s.get_extent(i);meta['extents'].append({'index':i,'physical_offset':off,'logical_offset':logical,'size':size,'flags':flags})
 if flags==0:regions.append((logical,size))
 logical+=size
meta['max_hex']=f.get_alternate_data_stream_by_name('$Max').read_buffer(32).hex();meta['allocated_bytes']=sum(size for off,size in regions);meta['extent_total_logical_size']=logical
# Preserve the tail containing all non-sparse extents; cap the read to avoid dumping sparse gigabytes.
start=min(off for off,size in regions);size=s.size-start
if size>128*1024*1024:raise RuntimeError('non-sparse tail too large')
b=s.read_buffer_at_offset(size,start);(out/'usn-tail.bin').write_bytes(b);meta['extracted_logical_start']=start;meta['extracted_size']=len(b);meta['sha256']=hashlib.sha256(b).hexdigest();rows=[];errors=[];times=[];counts=collections.Counter();off=0;selected=open(out/'usn-period.jsonl','w');logentries=open(out/'usn-logfiles.jsonl','w')
while off+60<=len(b):
 length,major,minor=struct.unpack_from('<IHH',b,off)
 if length==0:off+=8;continue
 if major!=2 or length<60 or length%8 or off+length>len(b):errors.append({'offset':start+off,'length':length,'major':major});off+=8;continue
 frn,parent,usn,stamp=struct.unpack_from('<QQQQ',b,off+8);reason,source,security,attrs=struct.unpack_from('<IIII',b,off+40);namelen,nameoff=struct.unpack_from('<HH',b,off+56)
 if nameoff+namelen>length:errors.append({'offset':start+off,'error':'name_bounds'});off+=length;continue
 name=b[off+nameoff:off+nameoff+namelen].decode('utf-16le',errors='replace');utc=(datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=stamp//10)).isoformat();times.append(utc);counts['records']+=1
 row={'offset':start+off,'usn':usn,'file_reference':frn,'parent_reference':parent,'utc':utc,'reason_hex':hex(reason),'source_hex':hex(source),'file_attributes_hex':hex(attrs),'name':name}
 if '2024-10-13T22'<=utc<'2024-10-29T23':selected.write(json.dumps(row,ensure_ascii=False)+'\n');counts['period']+=1
 if name.lower().endswith('.evtx'):logentries.write(json.dumps(row,ensure_ascii=False)+'\n');counts['log_files']+=1
 off+=length
selected.close();logentries.close();meta.update({'counts':dict(counts),'first_utc':min(times) if times else None,'last_utc':max(times) if times else None,'invalid_candidates':len(errors)});(out/'usn-summary.json').write_text(json.dumps(meta,indent=2));(out/'usn-errors.json').write_text(json.dumps(errors,indent=2));v.close();print(json.dumps({k:val for k,val in meta.items() if k!='extents'},indent=2))
