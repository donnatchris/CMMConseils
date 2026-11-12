#!/usr/bin/env python3
"""Selective encrypted iPhone backup collection on SIFT, passphrase by getpass."""
import argparse,collections,datetime as dt,getpass,json,os,pathlib,plistlib,re,shutil,sqlite3
from tp01_inventory import sha,ro,dump
def main():
 a=argparse.ArgumentParser();a.add_argument('source',type=pathlib.Path);a.add_argument('out',type=pathlib.Path);a=a.parse_args()
 os.umask(0o077);a.out.mkdir(parents=True,exist_ok=False)
 heads={}
 for name in ['Info.plist','Manifest.plist','Status.plist','Manifest.db']:
  src=a.source/name
  if not src.exists():heads[name]={'missing':True};continue
  dst=a.out/('Manifest-encrypted.db' if name=='Manifest.db' else name);before=sha(src);shutil.copyfile(src,dst)
  heads[name]={'before':before,'copy':sha(dst)}
 from iphone_backup_decrypt import EncryptedBackup
 password=getpass.getpass('Mot de passe sauvegarde TP-03 : ')
 try:
  backup=EncryptedBackup(backup_directory=str(a.source),passphrase=password);del password
  backup.test_decryption();backup.save_manifest_file(str(a.out/'Manifest.db'))
 except Exception as e:raise SystemExit('Decryption initialization error: '+type(e).__name__) from None
 rows=[];copied=[];missing=[];meta=[];errors=[];selected=[]
 with ro(a.out/'Manifest.db') as c:
  check=c.execute('pragma quick_check').fetchall()
  for fid,d,r,flag,b in c.execute('select fileID,domain,relativePath,flags,file from Files order by domain,relativePath'):
   x={'fileID':fid,'domain':d,'relativePath':r,'flags':flag}
   try:
    pl=plistlib.loads(b);o=pl['$objects'][pl['$top']['root'].data]
    for k in ['Size','Birth','LastModified','LastStatusChange']:x[k]=o.get(k)
   except Exception as e:x['metadata_error']=type(e).__name__
   rows.append(x)
   if flag!=1:continue
   src=a.source/fid[:2]/fid
   if not src.is_file():missing.append(fid);continue
   for k in ['Birth','LastModified','LastStatusChange']:
    v=x.get(k)
    if isinstance(v,(float,int)) and 1727733600<=v<1731711600:meta.append(dict(x,field=k,raw=v))
   take=bool(re.search(r'\.(db|sqlite|sqlite3|sqlitedb|storedata)(-wal|-shm|-journal)?$',r,re.I))
   take |= r.endswith(('.ips','.log'))
   take |= r.endswith(('.plist','.plist.backup')) and (not d.startswith('App') or any(z in (d+r).lower() for z in ['whatsapp','lscsmart','xiaomi','lockdown','mobile.installation']))
   if take:selected.append(x)
 dump(a.out/'inventory.json',rows);dump(a.out/'metadata-candidates.json',meta)
 with backup.manifest_db_cursor() as cur,(a.out/'extraction.jsonl').open('x') as log:
  for x in selected:
   fid=x['fileID'];d=x['domain'];r=x['relativePath'];src=a.source/fid[:2]/fid
   try:
    if not re.fullmatch('[a-f0-9]{40}',fid):raise ValueError('fileID')
    if pathlib.PurePosixPath(d).name!=d or '..' in pathlib.PurePosixPath(r).parts or r.startswith('/'):raise ValueError('path')
    match=cur.execute('select fileID from Files where domain LIKE ? and relativePath=? and flags=1 order by domain,relativePath limit 1',(d,r)).fetchone()
    if match!=(fid,):raise ValueError('selector')
    dst=a.out/'files'/d/r;dst.parent.mkdir(parents=True,exist_ok=True)
    before=sha(src);backup.extract_file(relative_path=r,domain_like=d,output_filename=str(dst));after=sha(src)
    if before!=after:raise ValueError('source_changed')
    row=dict(x,ciphertext_sha256=before,ciphertext_after=after,sha256=sha(dst),bytes=dst.stat().st_size,status='ok')
    if x.get('Size')!=row['bytes']:row['size_warning']=True
    copied.append(row)
   except Exception as e:
    row=dict(x,status='error',error_class=type(e).__name__);errors.append(row)
   log.write(json.dumps(row,ensure_ascii=False)+'\n');log.flush()
 for n in heads:
  if not heads[n].get('missing'):heads[n]['after']=sha(a.source/n)
 dump(a.out/'collection.json',copied);dump(a.out/'errors.json',errors)
 dump(a.out/'summary.json',{'source':str(a.source),'headers':heads,'manifest_plain_sha256':sha(a.out/'Manifest.db'),'quick_check':check,'flags':dict(collections.Counter(x['flags'] for x in rows)),'regular_bytes_manifest':sum(x.get('Size') or 0 for x in rows if x['flags']==1),'missing':missing,'selected':len(selected),'copied':len(copied),'errors':len(errors),'plaintext_bytes':sum(x['bytes'] for x in copied),'size_warnings':sum(bool(x.get('size_warning')) for x in copied),'python':os.sys.version,'sqlite':sqlite3.sqlite_version,'time_utc':dt.datetime.now(dt.timezone.utc).isoformat()})
 print(json.dumps({'copied':len(copied),'errors':len(errors),'missing':len(missing)}))
if __name__=='__main__':main()
