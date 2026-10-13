import pathlib,hashlib,shutil,json,datetime,importlib.util
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/home/sansforensics/analysis/OP-01/extractions-acces-20261013');sources=[];quarantine=[]
def save(p):
 dest=out/'raw'/p.relative_to(base);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest);sources.append({'source':str(p.relative_to(base)),'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
for p in sorted((base/'Windows/INF').glob('setupapi*.log')):save(p)
q=base/'ProgramData/Microsoft/Windows Defender/Quarantine'
if q.exists():
 for p in q.rglob('*'):
  if p.is_file():
   st=p.stat();quarantine.append({'source':str(p.relative_to(base)),'size':st.st_size,'mtime_utc':datetime.datetime.fromtimestamp(st.st_mtime,datetime.timezone.utc).isoformat()})
   if 'Entries' in p.parts and st.st_size<8*1024*1024:save(p)
p=base/'Users/fintm/AppData/Local/Packages/microsoft.windowscommunicationsapps_8wekyb3d8bbwe/LocalState/Files/S0/438/Attachments/AppleID-977451TLU5I[58342].pdf'
exists=p.exists()
if exists:save(p)
(out/'followup-sources.json').write_text(json.dumps(sources,indent=2));(out/'quarantine-inventory.json').write_text(json.dumps({'original_pdf_present':exists,'files':quarantine},indent=2));print('sources',len(sources),'quarantine',len(quarantine),'originalPDF',exists,flush=True)
for m in ['dissect','Crypto']:print(m,importlib.util.find_spec(m) is not None,flush=True)
