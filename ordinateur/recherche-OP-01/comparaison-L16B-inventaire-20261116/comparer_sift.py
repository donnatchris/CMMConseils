#!/usr/bin/env python3
"""Comparaison chemins et SHA-512 de l'intégralité du CSV au L16B de l'image RO."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,hashlib,subprocess,re,os,collections
ROOT=Path('/media/shared/codeProjects/DMMConseils')
OUT=Path(__file__).resolve().parent
WINDOWS=Path('/mnt/windows')
CSV=ROOT/'inventaire-DNEF/documents-recus/Inventaire_saddedine.csv'
HIST=ROOT/'ordinateur/recherche-OP-01/inventaire-L16B-20241028-20261116/inventaire-detaille.json'
START=datetime.now(timezone.utc).isoformat()
def sha(p,algorithm='sha256'):
 h=hashlib.new(algorithm)
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()
def canon(s):return s.replace('/','\\').rstrip('\\').casefold()
mount=json.loads(subprocess.check_output(['findmnt','-J','--mountpoint',str(WINDOWS),'-o','SOURCE,TARGET,FSTYPE,OPTIONS'],text=True))['filesystems'][0]
assert mount['source']=='/mnt/dislocker/dislocker-file' and 'ro' in mount['options'].split(',')
loops=json.loads(subprocess.check_output(['sudo','-n','losetup','-J'],text=True))['loopdevices']
loop=[x for x in loops if x.get('back-file')=='/mnt/ewf/ewf1'];assert len(loop)==1 and loop[0]['ro'] in (True,1,'1')
csvsha=sha(CSV);records=[]
with CSV.open(encoding='utf-8-sig',newline='') as f:
 for line,r in enumerate(csv.reader(f,delimiter=';'),1):
  if r and r[0].lower().startswith('c:\\'):
   assert len(r)>=5 and re.fullmatch('[a-fA-F0-9]{128}',r[4]),line
   records.append({'csv_line':line,'path':r[0],'sha512_inventory':r[4].lower(),'creation_inventory':r[1],'modification_inventory':r[2],'access_inventory':r[3]})
assert len(records)==1555
assert len({canon(x['path']) for x in records})==1555
current=[]
for p in sorted((WINDOWS/'L16B').rglob('*')):
 if p.is_file():current.append({'path':'C:\\'+str(p.relative_to(WINDOWS)).replace('/','\\'),'size':p.stat().st_size,'inode':p.stat().st_ino})
bycurrent={canon(x['path']):x for x in current}
results=[]
with (OUT/'comparaison-SHA512-complete.jsonl').open('x') as log:
 for idx,entry in enumerate(records,1):
  r=dict(entry);actual=bycurrent.get(canon(r['path']))
  r['present_at_path_in_image']=actual is not None
  if actual is None:r['status']='ABSENT DU CHEMIN'
  else:
   p=WINDOWS/actual['path'][3:].replace('\\','/');before=p.stat()
   r.update(size=before.st_size,inode=before.st_ino,mtime_ns=before.st_mtime_ns)
   if before.st_size>100*1024*1024:print('SHA-512 : '+actual['path']+' ('+str(before.st_size)+' octets)',flush=True)
   try:
    r['sha512_computed']=sha(p,'sha512');after=p.stat()
    r['stat_unchanged']=(before.st_size,before.st_ino,before.st_mtime_ns)==(after.st_size,after.st_ino,after.st_mtime_ns)
    assert r['stat_unchanged'],r['path']
    r['matches_inventory']=r['sha512_computed']==r['sha512_inventory']
    r['status']='IDENTIQUE' if r['matches_inventory'] else 'DIVERGENT'
   except Exception as e:r['status']='ERREUR DE LECTURE';r['error_type']=type(e).__name__;r['error']=str(e)
  results.append(r);log.write(json.dumps(r,ensure_ascii=False)+'\n');log.flush()
  if idx%100==0:print('Contrôlés : '+str(idx)+' / '+str(len(records)),flush=True)
assert sha(CSV)==csvsha,'CSV modifié pendant le contrôle'
keys={canon(x['path']) for x in records}
current_only=[x for x in current if canon(x['path']) not in keys]
csv_only=[x for x in results if not x['present_at_path_in_image']]
h=json.loads(HIST.read_text())
history_only=[x for x in h['files_28'] if canon(x['path']) not in keys]
assert {canon(x['path']) for x in h['files_28'] if x['category'].startswith('A')}==keys
summary={'inventory_rows':len(records),'files_in_L16B_image':len(current),'paths_in_common':sum(x['present_at_path_in_image'] for x in results),'current_only':len(current_only),'inventory_paths_absent_from_L16B':len(csv_only),'historical_28_paths_absent_from_CSV':len(history_only),'hash_status_counts':dict(collections.Counter(x['status'] for x in results)),'total_bytes_hashed':sum(x.get('size',0) for x in results if 'sha512_computed' in x)}
report={'started_utc':START,'finished_utc':datetime.now(timezone.utc).isoformat(),'inventory':str(CSV),'inventory_sha256':csvsha,'history_list_sha256':sha(HIST),'mount':mount,'loop':loop[0],'summary':summary,'current_only':current_only,'inventory_paths_absent_from_L16B':csv_only,'historical_28_paths_absent_from_CSV':history_only,'different_contents':[x for x in results if x['status']!='IDENTIQUE'],'comparisons':results}
with (OUT/'resultats-comparaison-L16B-inventaire.json').open('x') as f:json.dump(report,f,ensure_ascii=False,indent=2);f.write('\n')
cols=['Ligne CSV','Chemin inventorié','Présent dans L16B','Résultat SHA-512','Taille octets','SHA-512 inventaire','SHA-512 calculé','Inode','Erreur éventuelle']
with (OUT/'comparaison-SHA512-tous-les-fichiers.csv').open('x',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(cols)
 for x in results:w.writerow([x['csv_line'],x['path'],'Oui' if x['present_at_path_in_image'] else 'Non',x['status'],x.get('size',''),x['sha512_inventory'],x.get('sha512_computed',''),x.get('inode',''),x.get('error','')])
print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)
for x in report['different_contents']:print('DIFFÉRENCE : '+x['path']+' ; '+x['status'],flush=True)
