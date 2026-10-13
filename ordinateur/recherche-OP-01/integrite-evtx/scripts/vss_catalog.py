import pathlib,struct,json,datetime,uuid,subprocess
out=pathlib.Path('/tmp/OP-01-integrite-20261013/ntfs');out.mkdir(exist_ok=True)
p=subprocess.run(['vshadowinfo','/mnt/dislocker/dislocker-file'],capture_output=True,text=True);(out/'vshadowinfo.txt').write_text(p.stdout+'\n'+p.stderr)
rows=[];errors=[]
with open('/mnt/dislocker/dislocker-file','rb') as f:
 f.seek(7680);h=f.read(512);(out/'vss-volume-header.bin').write_bytes(h);catalog=struct.unpack_from('<Q',h,48)[0];seen=set();i=0
 while catalog and catalog not in seen and i<128:
  seen.add(catalog);f.seek(catalog);b=f.read(16384);(out/('vss-catalog-'+str(i)+'.bin')).write_bytes(b)
  if len(b)!=16384 or b[:16]!=h[:16] or struct.unpack_from('<I',b,20)[0]!=2:errors.append({'offset':catalog,'error':'catalog_header_invalid'});break
  for off in range(128,len(b),128):
   typ=struct.unpack_from('<Q',b,off)[0]
   if typ==2:
    n=struct.unpack_from('<Q',b,off+48)[0];utc=(datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=n//10)).isoformat();rows.append({'catalog_offset':catalog,'entry_offset':off,'type':typ,'store_id':str(uuid.UUID(bytes_le=b[off+16:off+32])),'creation_filetime':n,'creation_utc':utc,'volume_size':struct.unpack_from('<Q',b,off+8)[0]})
   elif typ==3:rows.append({'catalog_offset':catalog,'entry_offset':off,'type':typ,'store_id':str(uuid.UUID(bytes_le=b[off+16:off+32])),'store_header_offset':struct.unpack_from('<Q',b,off+32)[0]})
  catalog=struct.unpack_from('<Q',b,40)[0];i+=1
summary={'vshadowinfo_returncode':p.returncode,'catalog_blocks':i,'entries':rows,'errors':errors};(out/'vss-catalog-summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
