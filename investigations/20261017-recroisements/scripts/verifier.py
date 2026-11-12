#!/usr/bin/env python3
"""Vérification des conclusions nouvelles, empreintes d'extraction et fichiers sources."""
from pathlib import Path
import argparse,base64,csv,hashlib,json,plistlib,socket
R=Path(__file__).resolve().parents[3];D=R/'investigations/20261017-recroisements';a=argparse.ArgumentParser();a.add_argument('--out',required=True);out=Path(a.parse_args().out)
if out.exists():raise SystemExit('Destination existante')
def h(p):
 v=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):v.update(b)
 return v.hexdigest()
def j(p):return json.loads(p.read_text())
checks={};ev=j(D/'resultats/evtx/events.json');fb=j(R/'freebox/preuves-json/lan-browser-pub-raw.json')['result']
local={e['data']['LocalMac'] for e in ev if 'LocalMac' in e['data']};mac='50:E0:85:63:41:5B'
checks['op01_raw_evtx_mac_matches_freebox']=mac in local and any(x['l2ident']['id']==mac and x['primary_name']=='LAPTOP-RMCOB2VU' for x in fb)
smb=[e for e in ev if e['id']=='551']
checks['smb_two_raw_events']=len(smb)==2
checks['smb_binary_ipv4_matches_text']=all(socket.inet_ntoa(base64.b64decode(e['data']['ClientAddress'])[4:8])=='192.168.1.139' and e['data']['ClientName'].endswith('192.168.1.139') for e in smb)
checks['smb_failures']=all(e['data']['Status']=='0xc000006d' for e in smb)
checks['smb_candidate_same_date']=any(x['l2ident']['id']=='F8:28:19:77:42:71' and any(y['addr']=='192.168.1.139' and y.get('last_activity')==1711464500 for y in x.get('l3connectivities',[])) for x in fb)
cam=j(D/'resultats/recoupements-v2/cameras-identites.json')
checks['xiaomi_exact_mac']=any(x.get('ZMAC')=='E0:A2:5A:0A:A3:F7' and x.get('ZMODEL')=='mxiang.camera.mwc11' and x.get('freebox_mac_match',{}).get('mac')=='E0:A2:5A:0A:A3:F7' for x in cam['xiaomi_devices'])
checks['mwc10_difference_preserved']=any(x['exact_mac'] is False for x in cam['xiaomi_ip_candidates'])
checks['night_iphones_not_mapped']=not any(j(D/'resultats/recoupements-v2/tp02-freebox-wifi.json')['night_matches'].values())
# Les extractions téléphoniques consommées doivent correspondre aux empreintes historiques.
logs={}
for p in (R/'telephones/recherche-TP-02').glob('extraction*/extraction.jsonl'):
 for line in p.open():
  x=json.loads(line)
  if x.get('status')=='ok' and x.get('output'):logs[x['output']]=x
sources={}
for folder in ['recoupements-v2','cameras','evtx']:
 for x in j(D/f'resultats/{folder}/sources.json'):
  path=Path(x['path']);path=path if path.is_absolute() else R/path;sources[str(path)]=x['sha256_before']
hashes=[];phone=[]
backup=Path('/mnt/data/forensic/SADEDINE-2026/TP-02/00008110-001C69A002BA801E')
for path,expected in sources.items():
 p=Path(path);actual=h(p);hashes.append({'path':str(p),'sha256':actual,'matches_campaign_start':actual==expected})
 if '/telephones/' in str(p):
  record=logs.get(str(p));x={'path':str(p),'historical_record_found':record is not None}
  if record:
   x['plaintext_matches_extraction']=actual==record['sha256'];fid=record['fileID'];q=backup/fid[:2]/fid
   if not q.exists():q=backup/fid
   x['ciphertext_matches_extraction']=h(q)==record['ciphertext_sha256'] if q.exists() else None
  phone.append(x)
checks['all_sources_unchanged']=all(x['matches_campaign_start'] for x in hashes)
checks['all_phone_sources_verified']=all(x.get('plaintext_matches_extraction') and x.get('ciphertext_matches_extraction') for x in phone)
checks['sample_etags_match']=all(x['match'] and x['source_stat_unchanged'] for x in j(D/'resultats/conservation/etags-controle.json'))
data={'checks':checks,'all_pass':all(checks.values()),'source_count':len(hashes),'phone_sources':phone,'sources':hashes,'limits':'Contrôles de dérivés et échantillon S3 ; pas certification complète des acquisitions ou de leur histoire.'}
out.write_text(json.dumps(data,ensure_ascii=False,indent=2));out.chmod(0o600);print(json.dumps({'checks':checks,'source_count':len(hashes),'phone_sources':len(phone)}))
if not all(checks.values()):raise SystemExit(1)
