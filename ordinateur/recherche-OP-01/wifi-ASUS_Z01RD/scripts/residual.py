import pathlib,json,hashlib,datetime
B=pathlib.Path('/mnt/windows');O=pathlib.Path('/home/sansforensics/analysis/OP-01/wifi-ASUS_Z01RD-20261014')
patterns={'ascii':b'asus_z01rd','utf16le':'asus_z01rd'.encode('utf-16le'),'ssid_hex':b'415355535f5a30315244'}
files=set((B/'Windows/System32/winevt/Logs').glob('*.evtx'))
for root in [B/'Windows/System32/config',B/'Windows/System32/sru',B/'ProgramData/Microsoft/Wlansvc']:
 for p in root.rglob('*'):
  if p.is_file():files.add(p)
for user in (B/'Users').iterdir():
 if user.is_dir():
  files.update(p for p in user.glob('NTUSER*') if p.is_file())
  q=user/'AppData/Local/Microsoft/Windows'
  files.update(p for p in q.glob('UsrClass*') if p.is_file())
for n in ['pagefile.sys','swapfile.sys','hiberfil.sys']:
 if (B/n).exists():files.add(B/n)
rows=[];hits=[]
for p in sorted(files):
 row={'path':str(p.relative_to(B)),'size':p.stat().st_size,'matches':[]};h=hashlib.sha256();offset=0;tail=b''
 try:
  with p.open('rb') as f:
   while True:
    b=f.read(8*1024*1024)
    if not b:break
    h.update(b);window=(tail+b).lower();start=offset-len(tail)
    for label,needle in patterns.items():
     pos=window.find(needle)
     while pos>=0:
      absolute=start+pos
      if absolute+len(needle)>offset:row['matches'].append({'encoding':label,'offset':absolute})
      pos=window.find(needle,pos+1)
    offset+=len(b);tail=b[-64:]
  row['sha256']=h.hexdigest()
 except Exception as ex:row['error']=str(ex)
 rows.append(row)
 if row['matches']:hits.append(row);print('HIT',row['path'],len(row['matches']),flush=True)
 if len(rows)%50==0:print('Scanned',len(rows),'files',flush=True)
(O/'residual-inventory.json').write_text(json.dumps(rows,indent=2));(O/'residual-hits.json').write_text(json.dumps(hits,indent=2))
print('Done',len(rows),'files',sum(x['size'] for x in rows),'bytes',len(hits),'hit files',sum('error' in x for x in rows),'errors',flush=True)
