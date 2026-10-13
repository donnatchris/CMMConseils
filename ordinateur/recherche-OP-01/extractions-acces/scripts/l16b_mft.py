import pathlib,struct,json,datetime,collections
out=pathlib.Path('/home/sansforensics/analysis/OP-01/extractions-acces-20261013');inventory=json.loads((out/'l16b-inventory.json').read_text());rows=[]
U16=lambda b,o:struct.unpack_from('<H',b,o)[0];U32=lambda b,o:struct.unpack_from('<I',b,o)[0];U64=lambda b,o:struct.unpack_from('<Q',b,o)[0]
def times(b,o):
 result={}
 for i,k in enumerate(['creation','modification','mft_change','access']):
  n=U64(b,o+i*8);result[k]=(datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=n//10)).isoformat() if n else None
 return result
with open('/mnt/windows/$MFT','rb') as f:
 for r in inventory:
  f.seek(r['inode']*1024);raw=f.read(1024);b=bytearray(raw);row={'path':r['path'],'mft_index':r['inode'],'raw_record_hex':raw.hex()}
  try:
   if b[:4]!=b'FILE':raise ValueError('not FILE')
   usa=U16(b,4);num=U16(b,6)
   if num!=3:raise ValueError('unexpected fixup')
   for i in range(1,num):
    if b[i*512-2:i*512]!=b[usa:usa+2]:raise ValueError('bad fixup')
    b[i*512-2:i*512]=b[usa+i*2:usa+i*2+2]
   row['sequence']=U16(b,16);row['allocated']=bool(U16(b,22)&1);attr=U16(b,20);row['FN']=[]
   while attr+24<=min(U32(b,24),1024):
    typ=U32(b,attr)
    if typ==0xffffffff:break
    length=U32(b,attr+4)
    if length<24 or attr+length>1024:raise ValueError('invalid attribute')
    if not b[attr+8]:
     size=U32(b,attr+16);v=attr+U16(b,attr+20)
     if v+size<=attr+length:
      if typ==0x10 and size>=32:row['SI']=times(b,v)
      if typ==0x30 and size>=66:row['FN'].append({'name':bytes(b[v+66:v+66+b[v+64]*2]).decode('utf-16le','replace'),'namespace':b[v+65],'parent_reference':U64(b,v),'times':times(b,v+8)})
    attr+=length
  except Exception as e:row['error']=str(e)
  rows.append(row)
(out/'l16b-mft.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows));print('MFT L16B',len(rows),'errors',sum('error' in r for r in rows),flush=True)
