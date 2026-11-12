import pathlib,json,zipfile,hashlib,unicodedata
root=pathlib.Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013');base=pathlib.Path('/mnt/windows/L16B');original=root/'recovered/76808.bin';rows=[];sha=lambda b:hashlib.sha256(b).hexdigest();canon=lambda n:unicodedata.normalize('NFC',n.removeprefix('GDRIVE/'))
with zipfile.ZipFile(original) as old,zipfile.ZipFile(base/'GDRIVE.zip') as current:
 oldmap={canon(n):n for n in old.namelist() if not n.endswith('/')};newmap={canon(n):n for n in current.namelist() if not n.endswith('/')}
 folder={unicodedata.normalize('NFC',str(p.relative_to(base/'GDRIVE'))):p for p in (base/'GDRIVE').rglob('*') if p.is_file()}
 for name,member in oldmap.items():
  b=old.read(member);r={'name':name,'original_member_sha256':sha(b),'original_member_bytes':len(b),'present_current_zip':name in newmap,'present_current_folder':name in folder}
  if name in newmap:
   try:r['current_zip_sha256']=sha(current.read(newmap[name]));r['equal_current_zip']=r['current_zip_sha256']==r['original_member_sha256']
   except Exception as ex:r['current_zip_read_error']=str(ex)
  if name in folder:r['current_folder_sha256']=sha(folder[name].read_bytes());r['equal_current_folder']=r['current_folder_sha256']==r['original_member_sha256']
  if name=='GESTION DES MOTS DE PASSES 2.docx':r['recycle_docx_sha256']=sha((root/'recovered/77995.bin').read_bytes());r['equal_recycle_docx']=r['recycle_docx_sha256']==r['original_member_sha256']
  rows.append(r)
result={'original_zip_sha256':sha(original.read_bytes()),'current_zip_sha256':sha((base/'GDRIVE.zip').read_bytes()),'members':rows,'old_only_names':sorted(oldmap.keys()-newmap.keys()),'new_only_names':sorted(newmap.keys()-oldmap.keys())};(root/'drive-content-comparison.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('members',len(rows),'equal zip',sum(r.get('equal_current_zip',False) for r in rows),'equal folder',sum(r.get('equal_current_folder',False) for r in rows),'omitted',result['old_only_names'],flush=True)
