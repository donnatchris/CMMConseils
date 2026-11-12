import pathlib,hashlib,json,shutil,datetime
src=pathlib.Path('/mnt/windows'); out=pathlib.Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014'); out.mkdir(exist_ok=False)
rows=[]
def copy(p):
 rel=p.relative_to(src); dest=out/'raw'/rel; dest.parent.mkdir(parents=True,exist_ok=True)
 h=hashlib.sha256()
 with p.open('rb') as a,dest.open('xb') as b:
  while block:=a.read(4*1024*1024): h.update(block);b.write(block)
 rows.append({'path':str(rel),'size':dest.stat().st_size,'sha256':h.hexdigest()});print(str(rel),flush=True)
for user in (src/'Users').iterdir():
 recent=user/'AppData/Roaming/Microsoft/Windows/Recent'
 for folder in ['AutomaticDestinations','CustomDestinations']:
  if (recent/folder).is_dir():
   for p in (recent/folder).iterdir():
    if p.is_file():copy(p)
for p in (src/'L16B/MESSAGERIES').rglob('*.pst'):copy(p)
copy(src/'$LogFile')
(out/'sources.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
cloud=[]
for user in (src/'Users').iterdir():
 for rel in ['AppData/Local/Microsoft/OneDrive','AppData/Local/Google/DriveFS','AppData/Local/Dropbox','AppData/Roaming/Dropbox','AppData/Local/Apple Inc']:
  p=user/rel
  if p.is_dir():
   for f in p.rglob('*'):
    if f.is_file():
     s=f.stat();cloud.append({'path':str(f.relative_to(src)),'size':s.st_size,'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()})
(out/'cloud-inventory.json').write_text(json.dumps(cloud,ensure_ascii=False,indent=2))
print('DONE',len(rows),'sources',len(cloud),'cloud files',flush=True)
