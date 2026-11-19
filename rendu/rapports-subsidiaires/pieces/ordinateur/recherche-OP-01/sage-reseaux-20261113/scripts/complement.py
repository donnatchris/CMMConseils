import pathlib,json,re,hashlib,datetime,shutil
import pyscca
B=pathlib.Path('/mnt/windows');O=pathlib.Path('/home/sansforensics/analysis/OP-01/sage-reseaux-20261113');S=[];ERR=[]
def save(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str))
def copy(p):
 p=pathlib.Path(p);s=p.stat();r={'path':str(p.relative_to(B)),'size':s.st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()};S.append(r)
 q=O/'raw'/p.relative_to(B);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);q.chmod(0o600);return q
base=B/'ProgramData/Ciel/Applications/Ciel Gestion Commerciale'
copy(base/'Compléments utilisateur/Logs/Standard.SgLog')
log=(base/'Compléments utilisateur/Logs/Standard.SgLog').read_bytes().decode('cp1252')
save('sage-log-day.json',[{'line':i+1,'text':l} for i,l in enumerate(log.splitlines()) if l.startswith('28/10/2024')])
# Hash company database files and capture non-secret file header only.
dbs=[]
for p in base.glob('*/CDMDATA'):
 s=p.stat();dbs.append({'path':str(p.relative_to(B)),'size':s.st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'header_hex':p.open('rb').read(64).hex(),'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()})
save('sage-databases.json',dbs)
# Alias files contain only local database path; preserve these path records.
alias=[]
for p in (base/'Compléments utilisateur/Alias').glob('*'):
 if 'cdm0003Z' in p.name or 'cdm00040E' in p.name:
  copy(p);alias.append({'path':str(p.relative_to(B)),'hex':p.read_bytes().hex()})
save('sage-alias-day.json',alias)
# Marker presence and timestamp only; no authentication secrets are read.
p=B/'ProgramData/Ciel/Données Communes/AlreadyConnectedOnSageID';s=p.stat();save('sage-marker.json',{'path':str(p.relative_to(B)),'size':s.st_size,'mtime_utc':datetime.datetime.fromtimestamp(s.st_mtime,datetime.timezone.utc).isoformat()})
p=B/'Windows/INF/setupapi.dev.20241203_223829.log';copy(p);t=p.read_bytes().decode('cp1252');blocks=[]
for m in re.finditer(r'(?ms)^>>>  \[.*?(?=^>>>  \[|\Z)',t):
 block=m.group()
 if 'Section start 2024/10/28' in block:
  blocks.append({'line':t[:m.start()].count('\n')+1,'header':block.splitlines()[0],'text':block})
save('setupapi-day-blocks.json',blocks)
pf=[]
for p in (B/'Windows/Prefetch').glob('*'):
 if re.search('(?i)wgc|sage|ciel|wcp',p.name):
  try:
   copy(p);f=pyscca.file();f.open(str(p));times=[]
   for i in range(8):
    try:times.append(str(f.get_last_run_time(i)))
    except Exception:pass
   pf.append({'path':str(p.relative_to(B)),'executable':f.executable_filename,'run_count':f.run_count,'run_times_utc':times,'filenames':[f.get_filename(i) for i in range(f.number_of_filenames)]});f.close()
  except Exception as ex:ERR.append({'path':str(p),'error':str(ex)})
save('prefetch.json',pf);save('complement-sources.json',S);save('complement-errors.json',ERR)
print('complement sources',len(S),'setup blocks',len(blocks),'prefetch',len(pf),flush=True)
