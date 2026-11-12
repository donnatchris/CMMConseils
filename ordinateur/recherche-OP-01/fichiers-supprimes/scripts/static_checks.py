import pathlib,json,subprocess,re,urllib.parse,collections,importlib.util
root=pathlib.Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013');rows=[json.loads(l) for l in (root/'recovery-results.jsonl').read_text().splitlines()];out=[];keys=['anydesk','teamviewer','logmein','lmiruntime','screenconnect','rustdesk','ultravnc','tightvnc','radmin','splashtop','remotepc','dwagent','meshagent','netsupport','ngrok','rclone','winscp','filezilla','appleid-977451','ldsd'];have_pefile=importlib.util.find_spec('pefile') is not None
if have_pefile:import pefile
for r in rows:
 if not r.get('recovered_file') or r.get('signature') not in ['PE','PDF']:continue
 p=root/r['recovered_file'];item={'mft_index':r['mft_index'],'signature':r['signature'],'nominal_path':r['preferred_path'],'record_allocated':r['allocated']}
 if r['signature']=='PE':
  b=p.read_bytes().lower();item['target_terms']=[k for k in keys if k.encode() in b or k.encode('utf-16le') in b]
  if have_pefile:
   try:
    pe=pefile.PE(str(p),fast_load=True);item['machine']=pe.FILE_HEADER.Machine;item['coff_timestamp']=pe.FILE_HEADER.TimeDateStamp;item['sections']=[x.Name.decode('ascii','replace').rstrip('\0') for x in pe.sections];item['security_directory_bytes']=pe.OPTIONAL_HEADER.DATA_DIRECTORY[4].Size;pe.close()
   except Exception as ex:item['pe_error']=str(ex)
 else:
  try:
   info=subprocess.run(['pdfinfo',str(p)],capture_output=True,timeout=30);lines=info.stdout.decode('utf-8','replace').splitlines();item['pdfinfo_returncode']=info.returncode;item['metadata']={s.split(':',1)[0].strip():s.split(':',1)[1].strip() for s in lines if ':' in s and s.split(':',1)[0].strip() in ['Title','Producer','CreationDate','ModDate','Pages','JavaScript','Encrypted']}
   urls=subprocess.run(['pdfinfo','-url',str(p)],capture_output=True,timeout=30);domains=[]
   for url in re.findall(r'https?://\S+',urls.stdout.decode('utf-8','replace')):
    try:
     host=urllib.parse.urlsplit(url).hostname
     if host:domains.append(host)
    except:pass
   item['url_domains']=sorted(set(domains))
   result=subprocess.run(['/usr/local/bin/pdfid.py',str(p)],capture_output=True,timeout=30)
   output=result.stdout.decode('utf-8','replace');item['pdfid_returncode']=result.returncode;item['pdfid_counts']={m.group(1):int(m.group(2)) for m in re.finditer(r'^\s*(/[A-Za-z]+)\s+(\d+)',output,re.M)}
  except Exception as ex:item['error']=str(ex)
 out.append(item)
(root/'static-checks.json').write_text(json.dumps({'pefile_available':have_pefile,'results':out},ensure_ascii=False,indent=2));print('static',len(out),'PE target matches',sum(bool(r.get('target_terms')) for r in out),'PDFs with Javascript',sum(r.get('metadata',{}).get('JavaScript')=='yes' for r in out),flush=True)
