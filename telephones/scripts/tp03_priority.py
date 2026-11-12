#!/usr/bin/env python3
"""Priority native artefacts, camera metadata and PDF candidates; SIFT working copy."""
import argparse,contextlib,getpass,json,os,pathlib,plistlib,re,sqlite3,unicodedata
from tp01_inventory import sha,ro,dump
def norm(s):return unicodedata.normalize('NFKD',s).casefold()
def main():
 a=argparse.ArgumentParser();a.add_argument('source',type=pathlib.Path);a.add_argument('manifest',type=pathlib.Path);a.add_argument('out',type=pathlib.Path);a.add_argument('project',type=pathlib.Path);a=a.parse_args()
 os.umask(0o077);a.out.mkdir(parents=True,exist_ok=False)
 targets=json.loads((a.project/'ordinateur/recherche-OP-01/extractions-acces/l16b-inventory.json').read_text());targets=[x for x in targets if 'IPHONE13_MINI' in x['path'] and x['path'].lower().endswith('.pdf')]
 sizes={x['size'] for x in targets};names={norm(pathlib.PureWindowsPath(x['path']).name) for x in targets}
 selected=[]
 with ro(a.manifest) as c:
  for fid,d,r,f,b in c.execute('select fileID,domain,relativePath,flags,file from Files where flags=1'):
   pl=plistlib.loads(b);o=pl['$objects'][pl['$top']['root'].data];size=o.get('Size',0)
   native=any(z in r for z in ['SMS/sms.db','CallHistoryDB/CallHistory.storedata','CoreDuet/People/interactionC.db','PhotoData/Photos.sqlite','Health/healthdb','wifi-networks.plist','private-mac-networks.plist'])
   diag=r.endswith('.ips') and '2024-10-' in r
   camera=any(z in d for z in ['lscsmartconnection','xiaomi.mihome']) and not re.search(r'\.(png|jpe?g|heic|mov|mp4|gif|webp|ttf|woff2?|js|css|html)$',r,re.I)
   pdf=r.lower().endswith('.pdf') and (size in sizes or norm(pathlib.PurePosixPath(r).name) in names)
   if native or diag or camera or pdf:selected.append({'fileID':fid,'domain':d,'relativePath':r,'Size':size,'flags':f,'pdf_candidate':pdf})
 if sum(x['Size'] for x in selected)>4*1024**3:raise SystemExit('Selection exceeds 4 GiB')
 from iphone_backup_decrypt import EncryptedBackup,utils
 pw=getpass.getpass('Mot de passe sauvegarde TP-03 : ');backup=EncryptedBackup(backup_directory=str(a.source),passphrase=pw);del pw
 backup.test_decryption();results=[]
 with backup.manifest_db_cursor() as cur,(a.out/'library.log').open('x') as librarylog:
  for x in selected:
   fid=x['fileID'];d=x['domain'];r=x['relativePath'];src=a.source/fid[:2]/fid
   if not re.fullmatch('[a-f0-9]{40}',fid) or '/' in d or '..' in pathlib.PurePosixPath(r).parts or r.startswith('/'):raise ValueError('path')
   dst=a.out/'files'/d/r;dst.parent.mkdir(parents=True,exist_ok=True);before=sha(src)
   try:
    # Exact fileID lookup avoids LIKE wildcard ambiguity and repeated full scans.
    found=cur.execute('select domain,relativePath,file from Files where fileID=?',(fid,)).fetchall()
    if len(found)!=1 or found[0][:2]!=(d,r):raise ValueError('manifest identity')
    fp=utils.FilePlist(found[0][2]);key=backup.keybag.unwrap_key_for_class(fp.protection_class,fp.encryption_key)
    with contextlib.redirect_stdout(librarylog):backup._decrypt_file_to_disk(file_id=fid,key=key,file_plist=fp,output_filepath=str(dst))
    after=sha(src)
    if before!=after:raise ValueError('source changed')
    results.append(dict(x,status='ok',ciphertext_sha256=before,ciphertext_after=after,sha256=sha(dst),bytes=dst.stat().st_size,size_warning=dst.stat().st_size!=x['Size']))
   except Exception as e:results.append(dict(x,status='error',error_class=type(e).__name__))
   dump(a.out/'collection-progress.json',results)
 dump(a.out/'collection.json',[x for x in results if x['status']=='ok']);dump(a.out/'results.json',results)
 print(json.dumps({'selected':len(selected),'ok':sum(x['status']=='ok' for x in results),'errors':sum(x['status']!='ok' for x in results)}))
if __name__=='__main__':main()
