"""Read-only follow-up collection, run in SIFT with sudo python3."""
import pathlib,json,re,hashlib,pyregf
B=pathlib.Path('/mnt/windows')
O=pathlib.Path('/home/sansforensics/analysis/OP-01/wifi-ASUS_Z01RD-20261014/origine');O.mkdir(exist_ok=True)
rows=[]
with (B/'pagefile.sys').open('rb') as f:
 for off in [147842884,331615117,459192222,549269230,2752380159]:
  start=(off//4096)*4096-32768;f.seek(start);b=f.read(69632)
  (O/('pagefile-%s-64k.bin'%off)).write_bytes(b);strings=[]
  for enc,rx in [('ascii',rb'[\x20-\x7e]{6,}'),('utf16le',rb'(?:[\x20-\x7e]\x00){6,}')]:
   for m in re.finditer(rx,b):strings.append({'offset':start+m.start(),'encoding':enc,'text':m.group().decode(enc)})
  rows.append({'offset':off,'start':start,'sha256':hashlib.sha256(b).hexdigest(),'strings':strings})
(O/'wide-contexts.json').write_text(json.dumps(rows,indent=2));regs=[]
branches={'SYSTEM':[r'Select',r'ControlSet001\Control\ComputerName',r'ControlSet001\Services\WlanSvc',r'ControlSet001\Services\SharedAccess',r'ControlSet001\Services\icssvc',r'ControlSet001\Services\BTHPORT\Parameters\Devices',r'ControlSet001\Enum\BTHENUM'],'SOFTWARE':[r'Microsoft\WcmSvc',r'Microsoft\Windows\CurrentVersion\Internet Settings\Connections']}
for hive,paths in branches.items():
 f=pyregf.file();f.open(str(B/'Windows/System32/config'/hive))
 def walk(k,path):
  vals={}
  for v in k.values:
   b=v.data or b''
   try:val=v.get_data_as_string() if v.type in [1,2] else v.get_data_as_integer() if v.type in [4,11] else {'hex':b.hex()}
   except Exception:val={'hex':b.hex()}
   vals[v.name or '(default)']=val
  regs.append({'hive':hive,'key':path,'lastwrite':str(k.last_written_time),'values':vals})
  for sub in k.sub_keys:walk(sub,path+'\\'+sub.name)
 for branch in paths:
  k=f.get_key_by_path(branch)
  if k:walk(k,branch)
  else:regs.append({'hive':hive,'key':branch,'absent':True})
 f.close()
(O/'registry-origin.json').write_text(json.dumps(regs,indent=2))
