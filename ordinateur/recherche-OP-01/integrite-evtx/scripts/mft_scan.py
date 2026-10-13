import pathlib,struct,hashlib,json,datetime,collections
source=pathlib.Path('/mnt/windows/$MFT');out=pathlib.Path('/tmp/OP-01-integrite-20261013/ntfs');out.mkdir(exist_ok=True);counts=collections.Counter();directories={};selected=[];logfiles=[];digest=hashlib.sha256();index=0
U16=lambda b,o:struct.unpack_from('<H',b,o)[0];U32=lambda b,o:struct.unpack_from('<I',b,o)[0];U64=lambda b,o:struct.unpack_from('<Q',b,o)[0]
def time(n):
 if not n:return None
 try:return (datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=n//10)).isoformat()
 except:return None
def times(b,o):return dict(zip(['creation','modification','mft_change','access'],[time(U64(b,o+i*8)) for i in range(4)]))
with source.open('rb') as f:
 while True:
  block=f.read(16*1024*1024)
  if not block:break
  digest.update(block)
  for pos in range(0,len(block),1024):
   raw=block[pos:pos+1024];idx=index;index+=1;counts['slots']+=1
   if len(raw)<1024 or raw[:4]!=b'FILE':continue
   counts['FILE_signatures']+=1;b=bytearray(raw);usa=U16(b,4);num=U16(b,6)
   if usa+num*2>1024 or num!=3:counts['fixup_invalid']+=1;continue
   marker=b[usa:usa+2];valid=True
   for i in range(1,num):
    end=i*512-2
    if b[end:end+2]!=marker:valid=False;break
    b[end:end+2]=b[usa+2*i:usa+2*i+2]
   if not valid:counts['fixup_invalid']+=1;continue
   flags=U16(b,22);seq=U16(b,16);attr=U16(b,20);used=U32(b,24);base_ref=U64(b,32);SI=None;names=[];bad=False
   while attr+16<=min(used,1024):
    typ=U32(b,attr)
    if typ==0xffffffff:break
    length=U32(b,attr+4)
    if length<24 or attr+length>1024:bad=True;break
    if b[attr+8]==0:
     size=U32(b,attr+16);voff=U16(b,attr+20);v=attr+voff
     if voff+size<=length:
      if typ==0x10 and size>=32:SI=times(b,v)
      if typ==0x30 and size>=66:
       n=b[v+64];namespace=b[v+65]
       if 66+n*2<=size:names.append({'name':bytes(b[v+66:v+66+n*2]).decode('utf-16le',errors='replace'),'namespace':namespace,'parent_reference':U64(b,v),'times':times(b,v+8)})
    attr+=length
   if bad:counts['attribute_invalid']+=1;continue
   counts['allocated' if flags&1 else 'unallocated']+=1
   if flags&2 and names:
    fn=next((n for n in names if n['namespace']!=2),names[0]);directories[idx]={'name':fn['name'],'parent_reference':fn['parent_reference'],'sequence':seq,'allocated':bool(flags&1)}
   hits=[]
   if SI:
    hits+=[{'attribute':'SI','field':k,'utc':t} for k,t in SI.items() if t and '2024-10-15T08:53:09'<=t<'2024-10-28T09:22']
   for fn in names:hits+=[{'attribute':'FN','name':fn['name'],'field':k,'utc':t} for k,t in fn['times'].items() if t and '2024-10-15T08:53:09'<=t<'2024-10-28T09:22']
   islog=any(n['name'].lower().endswith('.evtx') for n in names)
   if hits or islog:
    r={'mft_index':idx,'offset':idx*1024,'sequence':seq,'allocated':bool(flags&1),'directory':bool(flags&2),'base_reference':base_ref,'SI':SI,'names':names,'gap_hits':hits,'raw_record_hex':raw.hex()}
    if hits:selected.append(r)
    if islog:logfiles.append(r)
  print('scanned',index,flush=True)
def path_for(fn):
 parts=[fn['name']];ref=fn['parent_reference'];seen=set();uncertain=False
 while ref&0xffffffffffff not in [5,0] and ref&0xffffffffffff not in seen:
  idx=ref&0xffffffffffff;seen.add(idx);d=directories.get(idx)
  if not d:parts.append('[parent MFT '+str(idx)+' inconnu]');uncertain=True;break
  if d['sequence']!=ref>>48 or not d['allocated']:uncertain=True
  parts.append(d['name']);ref=d['parent_reference']
 return {'path':'\\'.join(reversed(parts)),'parent_sequence_uncertain':uncertain}
for r in selected+logfiles:
 for fn in r['names']:fn.update(path_for(fn))
for name,rows in [('mft-gap-records.jsonl',selected),('mft-evtx-records.jsonl',logfiles)]:
 (out/name).write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
summary={'source':str(source),'source_size':source.stat().st_size,'sha256':digest.hexdigest(),'counts':dict(counts),'gap_records':len(selected),'gap_allocated':sum(r['allocated'] for r in selected),'evtx_named_records':len(logfiles),'evtx_unallocated':sum(not r['allocated'] for r in logfiles)};(out/'mft-summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
