#!/usr/bin/env python3
import hashlib,json,zipfile
from pathlib import Path
out=Path('/home/sansforensics/analysis/complement-20261017/zip');out.mkdir(exist_ok=False)
def h(p):
 d=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):d.update(b)
 return d.hexdigest()
res=[]
for p in Path('/mnt/windows/L16B').rglob('GDRIVE*.zip'):
 before=h(p);entries=[]
 with zipfile.ZipFile(p) as z:
  for info in z.infolist():
   if info.is_dir():continue
   x={'name':info.filename,'size':info.file_size}
   try:
    d=hashlib.sha256()
    with z.open(info) as f:
     for b in iter(lambda:f.read(1048576),b''):d.update(b)
    x['sha256']=d.hexdigest();x['crc_ok']=True
   except Exception as e:x['error']=type(e).__name__+': '+str(e)
   entries.append(x)
 res.append({'path':str(p),'sha256':before,'unchanged':h(p)==before,'entries':entries})
(out/'results.json').write_text(json.dumps(res,ensure_ascii=False,indent=2))
s={'archives':[{'path':x['path'],'files':len(x['entries']),'errors':sum('error' in e for e in x['entries']),'unchanged':x['unchanged']} for x in res]}
if len(res)==2:
 a,b=[{e['name']:e.get('sha256') for e in x['entries']} for x in res];s['identical_readable_files']=sum(v is not None and b.get(k)==v for k,v in a.items())
(out/'summary.json').write_text(json.dumps(s,indent=2));print(json.dumps(s))
