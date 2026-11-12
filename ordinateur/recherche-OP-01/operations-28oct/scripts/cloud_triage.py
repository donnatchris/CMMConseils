import pathlib,json,hashlib,sqlite3,shutil,datetime
root=pathlib.Path('/mnt/windows');out=pathlib.Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014')
manifest=[];schemas=[]
for rel in ['Users/fintm/AppData/Local/Microsoft/OneDrive/settings','Users/fintm/AppData/Local/Microsoft/OneDrive/settings/Personal']:
 p=root/rel
 if not p.is_dir():continue
 for f in p.iterdir():
  if not f.is_file() or '.db' not in f.name:continue
  dest=out/'cloud-raw'/f.relative_to(root);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(f,dest)
  manifest.append({'path':str(f.relative_to(root)),'size':f.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
for r in manifest:
 if not r['path'].endswith('.db'):continue
 p=out/'cloud-raw'/r['path']
 try:
  con=sqlite3.connect(f'file:{p}?mode=ro',uri=True)
  tables=con.execute("select name,sql from sqlite_master where type='table'").fetchall()
  found=[]
  for name,sql in tables:
   q='"'+name.replace('"','""')+'"'
   count=con.execute('select count(*) from '+q).fetchone()[0]
   hits=[]
   for row in con.execute('select * from '+q):
    if any(any(t in str(v).lower() for t in ['l16b','saddedine','140b8328','archive_saddedine']) for v in row):hits.append([str(v)[:1000] for v in row])
   found.append({'table':name,'schema':sql,'count':count,'target_rows':hits})
  schemas.append({'path':r['path'],'tables':found});con.close()
 except Exception as e:schemas.append({'path':r['path'],'error':str(e)})
(out/'cloud-sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
(out/'cloud-sqlite-triage.json').write_text(json.dumps(schemas,ensure_ascii=False,indent=2))
print('bases',len(schemas),'copies',len(manifest),'lignes cibles',sum(len(t['target_rows']) for s in schemas for t in s.get('tables',[])))
# Les métadonnées des copies des Jump Lists ne sont pas les métadonnées source.
meta=[]
for p in (out/'raw/Users').rglob('*'):
 if p.is_file():
  s=(root/p.relative_to(out/'raw')).stat();meta.append({'path':str(p.relative_to(out/'raw')),'size':s.st_size,'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()})
(out/'jumplist-source-metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
