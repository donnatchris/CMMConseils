#!/usr/bin/env python3
"""Recoupements locaux, sans modification des preuves. Destination neuve obligatoire."""
import argparse, collections, datetime as dt, hashlib, json, plistlib, re, shutil, sqlite3, tempfile
from pathlib import Path
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[3]
ap = argparse.ArgumentParser(); ap.add_argument('--out', required=True); args = ap.parse_args()
OUT = Path(args.out); OUT.mkdir(parents=True, exist_ok=False); OUT.chmod(0o700)
sources = {}; errors = []
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
 return h.hexdigest()
def source(p):
 p=Path(p); p=p if p.is_absolute() else ROOT/p
 if str(p) not in sources: sources[str(p)]={'path':str(p),'size':p.stat().st_size,'sha256_before':digest(p)}
 return p
def read(p): return source(p).read_bytes()
def js(p): return json.loads(read(p))
def save(name,v):
 p=OUT/name;p.write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str)+'\n');p.chmod(0o600)
def date(v):
 if isinstance(v,dt.datetime):d=v.replace(tzinfo=dt.timezone.utc) if v.tzinfo is None else v
 elif isinstance(v,(int,float)) and 0<v<4000000000:d=dt.datetime.fromtimestamp(v,dt.timezone.utc)
 else:return None
 return {'utc':d.isoformat(),'paris':d.astimezone(ZoneInfo('Europe/Paris')).isoformat()}
def mac(v):
 if isinstance(v,bytes):return ':'.join(f'{x:02X}' for x in v) if len(v)==6 else ''
 s=re.sub('[^0-9a-f]','',str(v).lower())
 return ':'.join(s[i:i+2] for i in range(0,12,2)).upper() if len(s)==12 else ''
def anon(v):return hashlib.sha256(str(v).encode()).hexdigest()

fb=js('freebox/preuves-json/lan-browser-pub-raw.json')['result']
by={mac(x['l2ident']['id']):x for x in fb}
def fbs(x):
 return {'mac':x['l2ident']['id'],'name':x.get('primary_name'),'names':x.get('names',[]),
 'first_activity':date(x.get('first_activity')),'last_activity':date(x.get('last_activity')),
 'connectivities':[dict(z,times={k:date(z.get(k)) for k in ['last_activity','last_time_reachable']}) for z in x.get('l3connectivities',[])]}

# Les champs XML sont relus, plutôt que déduits du nom de la machine.
op=[]; smb=[]; ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'}
for name in ['events.jsonl','extractions-acces/events.jsonl']:
 p=source('ordinateur/recherche-OP-01/'+name)
 for num,line in enumerate(p.open(),1):
  r=json.loads(line);data=r.get('data',{});computer=None
  if 'xml' in r:
   try:
    e=ET.fromstring(r['xml']);data={}
    for node in e:
     if node.tag.endswith('System'):continue
     for z in node.iter():
      if len(z)==0 and z.text:data[z.get('Name') or z.tag.split('}')[-1]]=z.text
    computer=e.findtext('e:System/e:Computer',namespaces=ns)
   except ET.ParseError:errors.append({'source':str(p),'line':num,'error':'XML parse'});continue
  base={'source':str(p.relative_to(ROOT)),'line':num,'channel_source':r.get('source'),'record':r.get('record'),'event_id':r.get('id'),'utc':r.get('utc'),'computer':computer}
  if any(mac(data.get(k,''))=='50:E0:85:63:41:5B' for k in ['LocalMac','HWAddress']):
   op.append(dict(base,data={k:data[k] for k in ['LocalMac','HWAddress','Adapter','DeviceGuid','SSID','NetworkHintString'] if k in data}))
  if '192.168.1.139' in json.dumps(data):smb.append(dict(base,data=data))
registry=js('ordinateur/recherche-OP-01/extractions-acces/registry.json')
duid=[{'key':r['key'],'lastwrite':r.get('lastwrite_utc'),'value':v} for r in registry for v in r.get('values',[]) if v['name']=='Dhcpv6DUID']
save('op01-freebox-identite.json',{'freebox':fbs(by['50:E0:85:63:41:5B']),'windows_events':op,'DUID':duid,'conclusion':'Concordance exacte MAC locale Windows / Freebox, corroborée par le nom et le DUID. Ne désigne pas une personne.'})
save('smb-26mars2024.json',{'windows':smb,'freebox_ip_matches':[fbs(x) for x in fb if any(z['addr']=='192.168.1.139' for z in x.get('l3connectivities',[]))],'limit':'Dernière activité conservée, pas journal continu des baux ni preuve de succès SMB.'})

tp='telephones/recherche-TP-02/extraction-systeme-20261014/files/SystemPreferencesDomain/'
priv=plistlib.loads(read(tp+'SystemConfiguration/com.apple.wifi-private-mac-networks.plist'))['List of scanned networks with private mac']
known=plistlib.loads(read(tp+'com.apple.wifi.known-networks.plist'))
matches=[]; allmac=set()
for i,x in enumerate(priv):
 m=mac(x.get('PRIVATE_MAC_ADDRESS',{}).get('PRIVATE_MAC_ADDRESS_VALUE'));allmac.add(m)
 if m in by:
  matches.append({'private_index':i,'mac':m,'ssid_sha256':anon(x.get('SSID_STR')),'private_dates':{k:date(v) for k,v in x.items() if isinstance(v,dt.datetime)},'freebox':fbs(by[m])})
night=['EA:21:6C:F7:47:E7','9C:64:8B:0A:BD:0C','FE:AA:76:95:AC:29']
save('tp02-freebox-wifi.json',{'private_entries':len(priv),'known_entries':len(known),'matches':matches,'night_matches':{m:m in allmac for m in night},'night_freebox':[fbs(by[m]) for m in night],'limit':'Instantanés sauvegardés ; une MAC peut avoir tourné, les préférences peuvent être restaurées. Non-correspondance ne permet pas exclusion historique.'})
save('desktop-freebox.json',[fbs(x) for x in fb if x.get('primary_name')=='DESKTOP-ICPNCMD'])

cam=ROOT/'telephones/recherche-TP-02/extraction-cameras-20261014/files'
# Copies SQLite temporaires avec compagnons ; seules colonnes autorisées sont publiées.
devices=[];tables=[];candidate_dates=[]
for p in [cam/'AppDomain-com.xiaomi.mihome/Documents/8216275811_mihome.sqlite',cam/'AppDomain-com.xiaomi.mihome/Documents/mihome_db.sqlite3']:
 with tempfile.TemporaryDirectory() as td:
  q=Path(td)/p.name;shutil.copyfile(source(p),q)
  for suffix in ['-wal','-shm']:
   side=Path(str(p)+suffix)
   if side.exists():shutil.copyfile(source(side),str(q)+suffix)
  c=sqlite3.connect(str(q));c.row_factory=sqlite3.Row
  for name, in c.execute("select name from sqlite_master where type='table'"):
   if name not in ['ZDEVICE','device','props','operationData','propValues']:continue
   rows=list(c.execute('select * from "'+name+'" NOT INDEXED'));tables.append({'source':str(p.relative_to(ROOT)),'table':name,'rows':len(rows)})
   for rr in rows:
    r=dict(rr)
    if name=='ZDEVICE':
     d={k:r[k] for k in ['Z_PK','ZMODEL','ZMAC','ZLOCALIP','ZEXTFWVERSION','ZLASTONLINE','ZSHAREFLAG','ZADMINFLAG','ZISFROMSERVER','ZISONLINE']};d['ZDID_sha256']=anon(r['ZDID']);d['source']=str(p.relative_to(ROOT));d['freebox_mac_match']=fbs(by[mac(r['ZMAC'])]) if mac(r['ZMAC']) in by else None;devices.append(d)
    elif name=='device': devices.append({'source':str(p.relative_to(ROOT)),'table':name,**{k:r[k] for k in ['model','isShared','isLocked','isOnline']},'did_sha256':anon(r['did'])})
    else:
     for k,v in r.items():
      if 'time' in k.lower() and isinstance(v,(int,float)):candidate_dates.append({'table':name,'field':k,'raw':v,'unix_hypothesis':date(v),'id_sha256':anon(r.get('did'))})
  c.close()
prefs=plistlib.loads(read(cam/'AppDomain-com.lscsmartconnection.smart/Library/Preferences/com.lscsmartconnection.smart.plist'))
lsctimes=[{'device_id_sha256':anon(k.split('-',1)[1]),'raw':v,'unix_hypothesis':date(v),'meaning':'Nom activeTimeKey ; activation/dernière consultation non établies'} for k,v in prefs.items() if k.startswith('activeTimeKey-')]
manifest=js(cam/'AppDomain-com.lscsmartconnection.smart/Documents/RCTAsyncLocalStorage_V1/manifest.json')
lsc=[]
for k,v in manifest.items():
 kind='CloudPanelConfig' if k.endswith('CloudPanelConfig') else 'LOCAL_DATA_KEY' if k.endswith('LOCAL_DATA_KEY') else 'voice' if k.startswith('voice_') else 'other'
 try: obj=json.loads(v) if isinstance(v,str) else v
 except ValueError: obj=v
 row={'key_sha256':anon(k),'kind':kind,'value_type':type(obj).__name__,'fields':list(obj) if isinstance(obj,dict) else None,'value_size':len(str(v))}
 if kind=='CloudPanelConfig' and isinstance(obj,dict) and isinstance(obj.get('timestamp'),(int,float)):
  row['timestamp_raw']=obj['timestamp'];row['unix_milliseconds_hypothesis']=date(obj['timestamp']/1000)
 if kind=='LOCAL_DATA_KEY' and isinstance(obj,dict) and isinstance(obj.get('value'),dict):row['nested_fields']=list(obj['value'])
 lsc.append(row)
ipmac=[]
for dev in devices:
 if dev.get('ZLOCALIP'):
  for x in fb:
   if any(y.get('addr')==dev['ZLOCALIP'] for y in x.get('l3connectivities',[])):
    ipmac.append({'xiaomi_model':dev.get('ZMODEL'),'xiaomi_mac':dev.get('ZMAC'),'ip':dev['ZLOCALIP'],'freebox':fbs(x),'exact_mac':mac(dev.get('ZMAC'))==mac(x['l2ident']['id']),'limit':'Adresse IP et nom concordants ; MAC différente, ne pas fusionner automatiquement.'})
save('cameras-identites.json',{'xiaomi_devices':devices,'xiaomi_ip_candidates':ipmac,'sqlite_tables':tables,'dates_candidates':candidate_dates,'lsc_activeTime':lsctimes,'lsc_last_version':prefs.get('kDefaultLastAppVersion'),'lsc_sdk_field':prefs.get('thing_smart_camera_sdk_version'),'lsc_local_storage':lsc,'limit':'Configurations à la sauvegarde ; aucune session historique ou correspondance SD démontrée par leur seule présence.'})

# Montage SD : rechercher dans les extraits disponibles, sans transformer une absence en exclusion.
volumes=[]
for p in sorted((ROOT/'cartes_sd').glob('recherche-SD-*/202610*/journaux/fsstat.txt')):
 t=read(p).decode(errors='replace');m=re.search(r'Volume ID: (0x[0-9a-fA-F]+)',t)
 if m:volumes.append({'source':str(p.relative_to(ROOT)),'volume_id':m.group(1)})
regnov=[{'key':r['key'],'hive':r.get('hive'),'lastwrite':r.get('lastwrite_utc')} for r in registry if str(r.get('lastwrite_utc','')).startswith('2024-11-12')]
setup=[];coverage=[]
for p in sorted((ROOT/'ordinateur/recherche-OP-01/extractions-acces/raw/Windows/INF').glob('setupapi*.log')):
 b=read(p);t=b.decode('utf-16') if b.startswith(b'\xff\xfe') else b.decode(errors='replace')
 dates=re.findall(r'Section start (\d{4}/\d{2}/\d{2} [\d:.]+)',t);coverage.append({'source':str(p.relative_to(ROOT)),'sections':len(dates),'first':min(dates) if dates else None,'last':max(dates) if dates else None})
 for block in re.split(r'(?m)(?=^>>>  \[)',t):
  if 'Section start 2024/11/12' in block:setup.append({'source':str(p.relative_to(ROOT)),'header':block.splitlines()[0],'dates':re.findall(r'Section (?:start|end) ([\d/ :.]+)',block)})
tokens=['386d4397','6546a41d','121220160204','140b8328'];hits=[]
for r in registry:
 s=json.dumps(r).lower()
 for token in tokens:
  if token in s: hits.append({'token':token,'key':r['key'],'hive':r.get('hive'),'lastwrite':r.get('lastwrite_utc')})
save('sd-windows-12novembre.json',{'sd_volumes':volumes,'registry_entries_examined':len(registry),'registry_nov12':regnov,'registry_literal_hits':hits,'setupapi_coverage':coverage,'setupapi_nov12':setup,'limit':'Registre précédemment extrait sélectivement ; SetupAPI trace des installations, pas toutes les insertions. Recherche textuelle des numéros, non décodage universel des structures binaires.'})

# Relecture des traces et absence de modification à la fin.
for s in sources.values():s['sha256_after']=digest(Path(s['path']));s['unchanged']=s['sha256_after']==s['sha256_before']
save('sources.json',list(sources.values()));save('errors.json',errors)
save('summary.json',{'sources':len(sources),'unchanged':all(s['unchanged'] for s in sources.values()),'op01_events':len(op),'smb_events':len(smb),'tp02_mac_matches':len(matches),'xiaomi_rows':len(devices),'errors':len(errors)})
print((OUT/'summary.json').read_text())
