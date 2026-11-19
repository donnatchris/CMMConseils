import pathlib,json,hashlib,shutil,datetime,xml.etree.ElementTree as E,subprocess,pyregf
B=pathlib.Path('/mnt/windows');O=pathlib.Path('/home/sansforensics/analysis/OP-01/sage-reseaux-20261113');sources=[]
for fn in ['Microsoft-Windows-Wcmsvc%4Operational.evtx','Microsoft-Windows-SMBServer%4Operational.evtx','Microsoft-Windows-SmbClient%4Connectivity.evtx']:
 rel='Windows/System32/winevt/Logs/'+fn;p=B/rel;q=O/'raw'/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q);q.chmod(0o600);sources.append({'path':rel,'size':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest()})
profiles=[]
for p in (B/'ProgramData/Microsoft/Wlansvc').rglob('*.xml'):
 try:
  root=E.fromstring(p.read_bytes());fields={v.tag.split('}')[-1]:v.text for v in root.iter() if v.tag.split('}')[-1] in ['name','hex','connectionType','connectionMode','authentication','encryption']};profiles.append({'path':str(p.relative_to(B)),'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'fields':fields})
 except Exception as ex:profiles.append({'path':str(p),'error':str(ex)})
(O/'wifi-profiles-sans-secrets.json').write_text(json.dumps(profiles,ensure_ascii=False,indent=2))
(O/'fin-sources.json').write_text(json.dumps(sources,indent=2))
(O/'mount-final.txt').write_text(subprocess.getoutput('findmnt /mnt/windows')+'\n'+subprocess.getoutput('lsblk -o NAME,SIZE,FSTYPE,RO,TYPE,MOUNTPOINT /dev/loop16')+'\n')
print('Profiles',len(profiles),'ASUS matches',sum('ASUS_Z01RD' in str(r) for r in profiles))
