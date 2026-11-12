#!/usr/bin/env python3
"""Cross-device identifier checks, local evidence only; no network account access."""
import datetime as dt,hashlib,json,pathlib,plistlib,re,sys
from tp01_inventory import sha,dump
def mac(v):
 if isinstance(v,bytes) and len(v)==6:return ':'.join(f'{b:02X}' for b in v)
 if not isinstance(v,str):return None
 s=re.sub('[:-]','',v)
 if re.fullmatch('[a-fA-F0-9]{12}',s):return ':'.join(s[i:i+2].upper() for i in range(0,12,2))
 return None
def main():
 project=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);out.mkdir(exist_ok=False)
 sourcefiles=[];radio=[]
 roots={'TP-01':pathlib.Path('/home/sansforensics/analysis/tp01-20261110'),'TP-02':project/'telephones/recherche-TP-02/extraction-systeme-20261014','TP-03':pathlib.Path('/home/sansforensics/analysis/tp03-20261110')}
 for code,root in roots.items():
  files=list((root/'files/SystemPreferencesDomain').rglob('*wifi*.plist*'))
  if code=='TP-01':files+=list((root/'supplement/files/SystemPreferencesDomain').rglob('*wifi*.plist*'))
  for p in files:
   before=sha(p)
   try:d=plistlib.loads(p.read_bytes())
   except Exception:continue
   def walk(v,key,ssid=None):
    if isinstance(v,dict):
     ssid=v.get('SSID_STR',v.get('SSID',ssid))
     if isinstance(ssid,bytes):ssid=ssid.decode('utf-8','replace')
     for k,x in v.items():walk(x,key+'/'+str(k),ssid)
    elif isinstance(v,list):
     for i,x in enumerate(v):walk(x,key+'/'+str(i),ssid)
    else:
     m=mac(v)
     if m:
      role='access_point' if 'bssid' in key.lower() else ('client_candidate' if re.search('mac.*address|wifi.*address',key,re.I) else 'other')
      radio.append({'device':code,'source':str(p),'key':key,'ssid':ssid,'mac':m,'role':role})
   walk(d,'');sourcefiles.append({'path':str(p),'before':before,'after':sha(p)})
  header=root/'Manifest.plist' if code!='TP-02' else pathlib.Path('/media/shared/forensic/SADEDINE-2026/TP-02/00008110-001C69A002BA801E/Manifest.plist')
  if header.is_file():
   d=plistlib.loads(header.read_bytes()).get('Lockdown',{})
   for k,v in d.items():
    if ('wifi' in k.lower() or 'macaddress' in k.lower()) and mac(v):radio.append({'device':code,'source':str(header),'key':k,'ssid':None,'mac':mac(v),'role':'hardware_metadata'})
  if code in ['TP-01','TP-02']:
   p=root/'Info.plist' if code=='TP-01' else header.with_name('Info.plist');d=plistlib.loads(p.read_bytes())
   for k,v in d.items():
    if 'wifi' in k.lower() and mac(v):radio.append({'device':code,'source':str(p),'key':k,'ssid':None,'mac':mac(v),'role':'hardware_metadata'})
 fb=project/'freebox/preuves-json/lan-browser-pub-raw.json';data=json.loads(fb.read_text());hosts=data.get('result',data) if isinstance(data,dict) else data
 matches=[]
 for x in radio:
  if x['role'] not in ['client_candidate','hardware_metadata']:continue
  for h in hosts:
   addresses=[mac(h.get('l2ident',{}).get('id')),mac(h.get('mac'))]
   if x['mac'] in addresses:matches.append(dict(x,freebox_name=h.get('primary_name'),freebox_first=h.get('first_activity'),freebox_last=h.get('last_activity')))
 target=['EA:21:6C:F7:47:E7','9C:64:8B:0A:BD:0C','FE:AA:76:95:AC:29']
 nightly={m:[x for x in radio if x['mac']==m and x['role'] in ['client_candidate','hardware_metadata']] for m in target}
 pair=project/'investigations/20261019-retour-cliente/resultats/sift/apple-pairing-op01.json'
 d=json.loads(pair.read_text());m=plistlib.loads((roots['TP-03']/'Manifest.plist').read_bytes())['Lockdown'];udid=m['UniqueDeviceID']
 dump(out/'radio-identifiers.json',radio);dump(out/'freebox-matches.json',matches);dump(out/'nightly-iphones.json',nightly)
 dump(out/'pairing-tp03.json',{'backup_udid':udid,'backup_serial':m['SerialNumber'],'udid_sha256':hashlib.sha256(udid.encode()).hexdigest(),'pair_record_expected_name':udid+'.plist','prior_result_contains_exact_filename':udid+'.plist' in pair.read_text(),'prior_result_sha256':sha(pair),'prior_result':str(pair),'manifest_plist_sha256':sha(roots['TP-03']/'Manifest.plist')})
 dump(out/'sources.json',sourcefiles+[{'path':str(fb),'sha256':sha(fb)}]);print(json.dumps({'radio_values':len(radio),'matches':len(matches),'nightly_matches':{k:len(v) for k,v in nightly.items()}}))
if __name__=='__main__':main()
