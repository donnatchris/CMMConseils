from pathlib import Path
import json,plistlib,hashlib,datetime as D,re
from zoneinfo import ZoneInfo
R=Path(__file__).resolve().parents[3];O=R/'investigations/20261019-retour-cliente/resultats/plists';O.mkdir(exist_ok=False);sources=[]
def read(p):
 b=p.read_bytes();sources.append({'path':str(p.relative_to(R)),'sha256_before':hashlib.sha256(b).hexdigest()});return plistlib.loads(b)
def cv(x):
 if isinstance(x,D.datetime):return {'utc':x.replace(tzinfo=D.timezone.utc).isoformat(),'paris':x.replace(tzinfo=D.timezone.utc).astimezone(ZoneInfo('Europe/Paris')).isoformat()}
 return x
b=R/'telephones/recherche-TP-02/extraction-systeme-20261014/files/SystemPreferencesDomain'
v=read(b/'com.apple.wifi.known-networks.plist');x=next(x for k,x in v.items() if isinstance(x,dict) and ('ASUS_Z01RD' in k or x.get('SSID')==b'ASUS_Z01RD'))
known={k:cv(x[k]) for k in ('AddReason','AddedAt','JoinedByUserAt','JoinedBySystemAt','LastDiscoveredAt')};known['BSSList']=[{k:cv(r[k]) for k in ('BSSID','LastAssociatedAt','Channel') if k in r} for r in x['BSSList']]
v=read(b/'SystemConfiguration/com.apple.wifi-private-mac-networks.plist');x=next(x for x in v['List of scanned networks with private mac'] if x.get('SSID_STR')=='ASUS_Z01RD')
priv={k:cv(x[k]) for k in ('BSSID','MacGenerationTimeStamp','FirstJoinWithNewMacTimestamp','addedAt','lastJoined','LinkDownTimestamp')}
(O/'asus-dates-radio.json').write_text(json.dumps({'known_network':known,'private_network':priv,'limit':'BSSID conservés dans un état tardif; les dates LastAssociatedAt sont du 28, aucun BSSID historiquement certifié au 17.'},indent=2))
base=R/'telephones/recherche-TP-02/extraction-complements-20261014/files';profiles=[]
for p in sorted(base.rglob('*.plist')):
 if not any(t in str(p) for t in ('ConfigurationProfiles','managedconfiguration','FMIPAccounts')):continue
 try:
  x=read(p);d={'source':str(p.relative_to(R)),'type':type(x).__name__,'top_entries':len(x),'top_keys':list(x) if isinstance(x,dict) else []}
  # Report only structural paths for actual management-specific fields, never profile secrets.
  hits=[]
  def walk(v,path):
   if isinstance(v,dict):
    for k,y in v.items():
     if str(k) in ('PayloadType','IsSupervised','IsMDMUnremovable','OrganizationName','ServerURL','CheckInURL','EnrollmentURL'):hits.append({'path':path+'/'+str(k),'value':y if str(k) in ('PayloadType','IsSupervised','IsMDMUnremovable') else '[present, redacted]'})
     walk(y,path+'/'+str(k))
   elif isinstance(v,list):
    for i,y in enumerate(v):walk(y,path+'/'+str(i))
  walk(x,'');d['management_fields']=hits;profiles.append(d)
 except Exception as e:profiles.append({'source':str(p.relative_to(R)),'error':str(e)})
(O/'profiles-account-structure.json').write_text(json.dumps(profiles,ensure_ascii=False,indent=2,default=str))
p=R/'telephones/recherche-TP-02/extraction-cameras-20261014/files/AppDomain-com.lscsmartconnection.smart/Documents/panel/__access_time__.json'
bb=p.read_bytes();sources.append({'path':str(p.relative_to(R)),'sha256_before':hashlib.sha256(bb).hexdigest()});x=json.loads(bb);late=[]
for k,y in x.items():
 if not isinstance(y,dict) or not isinstance(y.get('time'),(float,int)):continue
 d=D.datetime.fromtimestamp(y['time'],D.timezone.utc).astimezone(ZoneInfo('Europe/Paris'))
 if d.date()==D.date(2024,10,28) and d.hour>=19:late.append({'key':k,'raw_time':y['time'],'paris_unix_interpretation':d.isoformat()})
(O/'lsc-after1920.json').write_text(json.dumps(late,indent=2))
for s in sources:s['sha256_after']=hashlib.sha256((R/s['path']).read_bytes()).hexdigest();s['unchanged']=s['sha256_before']==s['sha256_after']
(O/'sources.json').write_text(json.dumps(sources,indent=2));print('sources',len(sources),'profiles',len(profiles),'LSC late fields',len(late),'unchanged',all(s['unchanged'] for s in sources))
