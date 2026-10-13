import pathlib,json,zipfile,hashlib,collections
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/home/sansforensics/analysis/OP-01/extractions-acces-20261013');rows=[]
for p in sorted((base/'L16B').rglob('*.zip')):
 try:
  with zipfile.ZipFile(p) as z:
   members=[{'name':x.filename,'size':x.file_size,'compressed':x.compress_size,'crc':f'{x.CRC:08x}','date_fields':list(x.date_time),'encrypted':bool(x.flag_bits&1)} for x in z.infolist()]
  rows.append({'source':str(p.relative_to(base)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':p.stat().st_size,'members':members})
 except Exception as e:rows.append({'source':str(p.relative_to(base)),'error':str(e)})
(out/'archives.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));print('archives',len(rows),flush=True)

p=base/'L16B/MESSAGERIES/rct93300@gmail.com/takeout-20241028T114105Z-001.zip'
with zipfile.ZipFile(p) as z:b=z.read('Takeout/archive_browser.html')
(out/'takeout-archive_browser.html').write_bytes(b)
(out/'takeout-manifest-source.json').write_text(json.dumps({'archive':str(p.relative_to(base)),'member':'Takeout/archive_browser.html','size':len(b),'sha256':hashlib.sha256(b).hexdigest()},indent=2))
