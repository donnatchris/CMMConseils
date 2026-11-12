import pathlib,json,collections,zipfile,xml.etree.ElementTree as E,hashlib,struct,datetime,re,sqlite3,shutil,subprocess,tempfile,pyscca,pylnk
root=pathlib.Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013');rows=[json.loads(l) for l in (root/'recovery-results.jsonl').read_text().splitlines()];binrows=[r for r in rows if 'recycle_info' in r];paired=[];results=[];errors=[]
def ft(n):
 try:return (datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=n//10)).isoformat() if n else None
 except:return None
for r in binrows:
 name=r['preferred_path'].rsplit('\\',1)[-1];target='$R'+name[2:];matches=[x for x in rows if x['preferred_path'].rsplit('\\',1)[-1]==target and x['preferred_path'].rsplit('\\',1)[0]==r['preferred_path'].rsplit('\\',1)[0]];paired.append({'I_mft':r['mft_index'],'I_allocated':r['allocated'],'I_sha256':r.get('sha256_read_bytes'),'info':r['recycle_info'],'R_matches':[{'mft_index':x['mft_index'],'path':x['preferred_path'],'allocated':x['allocated'],'signature':x.get('signature'),'sha256':x.get('sha256_read_bytes'),'read_bytes':x.get('read_bytes'),'size_equals_I':x.get('native_size')==r['recycle_info']['original_size'],'recovered_file':x.get('recovered_file')} for x in matches]})
(root/'recycle-pairs.json').write_text(json.dumps(paired,ensure_ascii=False,indent=2))
rx=re.compile(r'logmein|anydesk|teamviewer|screenconnect|rustdesk|tightvnc|ultravnc|ngrok|rclone|winscp|filezilla|takeout|wetransfer|transfernow|ldsd|appleid-977451',re.I)
for r in rows:
 if not r.get('recovered_file'):continue
 p=root/r['recovered_file'];b=p.read_bytes();entry={'mft_index':r['mft_index'],'nominal_path':r['preferred_path'],'signature':r['signature'],'complete_logical_read':r['complete_logical_read'],'current_allocated_clusters':r['clusters_currently_allocated'],'extent_clusters':r['extent_clusters']}
 try:
  if r['signature']=='ZIP':
   with zipfile.ZipFile(p) as z:
    entry['zip_members']=[{'name':x.filename,'size':x.file_size,'crc':f'{x.CRC:08x}','date_fields':list(x.date_time)} for x in z.infolist()];size=sum(x.file_size for x in z.infolist());entry['zip_total_uncompressed']=size
    if size<=512*1024*1024 and all(x.file_size<=128*1024*1024 for x in z.infolist()):entry['zip_bad_crc_member']=z.testzip()
    else:entry['zip_crc_skipped']='decompression_size_cap'
    if 'word/document.xml' in z.namelist():
     data=z.read('word/document.xml');t=E.fromstring(data);texts=[n.text or '' for n in t.iter() if n.tag.endswith('}t')];entry['word_nonempty_runs']=sum(bool(x.strip()) for x in texts);entry['word_tables']=len(t.findall('.//{*}tbl'));entry['word_rows']=len(t.findall('.//{*}tr'));entry['word_nonempty_cells']=sum(any(n.text and n.text.strip() for n in cell.findall('.//{*}t')) for cell in t.findall('.//{*}tc'));flat=' '.join(texts).lower();entry['credential_label_counts']={key:flat.count(key) for key in ['mot de passe','mots de passe','identifiant','login','password']};entry['word_xml_sha256']=hashlib.sha256(data).hexdigest()
  elif r['signature']=='LNK':
   f=pylnk.file();f.open(str(p));entry['lnk']={'target':f.local_path,'relative_path':f.relative_path,'arguments':f.command_line_arguments,'target_creation_utc':ft(f.get_file_creation_time_as_integer()),'target_modification_utc':ft(f.get_file_modification_time_as_integer()),'target_access_utc':ft(f.get_file_access_time_as_integer()),'corrupted':f.is_corrupted()};f.close()
  elif r['signature']=='Prefetch':
   f=pyscca.file();f.open(str(p));times=[]
   for i in range(8):
    try:times.append(ft(f.get_last_run_time_as_integer(i)))
    except:break
   entry['prefetch']={'executable':f.executable_filename,'run_count':f.run_count,'run_times':times};f.close()
  elif r['signature']=='PDF':
   result=subprocess.run(['pdftotext',str(p),'-'],capture_output=True,timeout=30);text=result.stdout.decode('utf-8','replace');dest=root/'pdf-text'/(str(r['mft_index'])+'.txt');dest.parent.mkdir(exist_ok=True);dest.write_text(text);entry['pdf_extract_returncode']=result.returncode;entry['pdf_text_chars']=len(text);entry['pdf_text_file']=str(dest.relative_to(root));entry['target_terms_found']=sorted(set(m.group(0).lower() for m in rx.finditer(text)))
  elif r['signature']=='SQLite':
   with tempfile.TemporaryDirectory() as d:
    tmp=pathlib.Path(d)/'copy.db';shutil.copyfile(p,tmp);con=sqlite3.connect('file:'+str(tmp)+'?mode=ro',uri=True);entry['sqlite_integrity']=con.execute('pragma quick_check').fetchmany(10);entry['sqlite_tables']=con.execute("select name from sqlite_master where type='table'").fetchall();con.close()
  elif r['signature']=='other' and r['extension'] in ['.ps1','.bat','.cmd','.vbs','.url','.rdp','.txt','.log','.json','.xml','.html','.htm','.eml','.msg']:
   text=b.decode('utf-16le','ignore') if b.startswith(b'\xff\xfe') else b.decode('utf-8','ignore');entry['target_terms_found']=sorted(set(m.group(0).lower() for m in rx.finditer(text)));entry['looks_text']=sum(c in '\r\n\t' or c.isprintable() for c in text)/max(1,len(text))>.95
 except Exception as ex:entry['parse_error']=str(ex);errors.append({'mft_index':r['mft_index'],'error':str(ex)})
 results.append(entry)
(root/'content-analysis.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in results));(root/'content-errors.json').write_text(json.dumps(errors,indent=2));print('analysis',len(results),'recycle metadata',len(paired),'errors',len(errors),flush=True)
