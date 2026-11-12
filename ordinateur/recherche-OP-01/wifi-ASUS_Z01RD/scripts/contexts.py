import pathlib,json,re,hashlib
B=pathlib.Path('/mnt/windows')
O=pathlib.Path('/home/sansforensics/analysis/OP-01/wifi-ASUS_Z01RD-20261014')
hits=json.loads((O/'residual-hits.json').read_text());rows=[]
for h in hits:
 with (B/h['path']).open('rb') as f:
  for m in h['matches']:
   off=m['offset'];start=max(0,off-512);f.seek(start);b=f.read(1042)
   q=O/'contexts'/('pagefile-%s.bin'%off);q.parent.mkdir(exist_ok=True);q.write_bytes(b);q.chmod(0o600)
   strings=[{'offset':start+x.start(),'text':x.group().decode('ascii')} for x in re.finditer(rb'[\x20-\x7e]{5,}',b)]
   rows.append({'match':m,'start':start,'sha256':hashlib.sha256(b).hexdigest(),'strings':strings})
(O/'pagefile-contexts.json').write_text(json.dumps(rows,indent=2))
