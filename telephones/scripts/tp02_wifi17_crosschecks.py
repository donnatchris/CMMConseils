#!/usr/bin/env python3
"""Focused follow-up controls: field histories, identifier matches, CommCenter and OP-01 WLAN bytes.
No source writes, no network access, no secret exports. Run once after tp02_wifi17_investigation.py.
"""
import argparse,collections,csv,datetime as dt,hashlib,json,os,plistlib,re,struct,uuid,zlib
from pathlib import Path
import tp02_forensic as c
p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args();O=Path(a.out);R=Path('telephones/recherche-TP-02');os.umask(0o077);U=dt.timezone.utc
logs=[json.loads(l) for f in R.glob('extraction-*/extraction.jsonl') for l in f.read_text().splitlines()];logs=[v for v in logs if v.get('status')=='ok']
def save(n,v):
 with (O/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2,default=str);f.write('\n')
def find(n):return next(Path(v['output']) for v in logs if Path(v['relativePath']).name==n)
def sh(x):return hashlib.sha256(x if isinstance(x,bytes) else str(x).encode()).hexdigest()
rr=list(csv.DictReader((O/'comparaison-reseaux.csv').open()));both=[v for v in rr if v['generation_to_firstjoin_seconds']];neg=[v for v in both if float(v['generation_to_firstjoin_seconds'])<0]
fields={'both_dates':len(both),'first_join_precedes_current_generation':len(neg),'negative_aliases':[v['network_alias'] for v in neg],'negative_near14days_within4h':sum(abs(float(v['generation_to_firstjoin_seconds'])+1209600)<14400 for v in neg),'identical_generation_clusters':dict(collections.Counter(v['MacGenerationTimeStamp_utc'] for v in rr if v['MacGenerationTimeStamp_utc'])),'CloudSync_historical_userdate':[{'alias':v['network_alias'],'user':v['JoinedByUserAt_utc'],'added':v['AddedAt_utc']} for v in rr if v['reason']=='Cloud Sync' and v['user_join_precedes_added']=='True'],'system_app_seconds_sequences':[{'alias':v['network_alias'],'delta_seconds':float(v['generation_to_firstjoin_seconds'])} for v in both if v['reason']=='System App' and 0<=float(v['generation_to_firstjoin_seconds'])<10],'limit':'These are evolving snapshot fields. Negative intervals are not negative radio sessions, nor proof of clock changes.'};save('network-field-history-controls.json',fields)
cp=find('com.apple.commcenter.data.archive.plist');before=c.sha(cp);v=plistlib.loads(cp.read_bytes());rec=next(v for v in logs if Path(v['output'])==cp);entries=[]
for x in v.get('label-remap-history',{}).values():
 if x.get('from_dated')!=1729178133:continue
 entry={'action':x.get('action'),'to_label_omitted':True,'dates':{}}
 for k in ['from_dated','to_dated','ts']:
  raw=x.get(k);d=dt.datetime.fromtimestamp(raw,U);entry['dates'][k]={'raw_unix':raw,'utc':d.isoformat(),'paris':d.astimezone(c.PARIS).isoformat()}
 entries.append(entry)
save('commcenter-label-remap.json',{'source':{k:rec[k] for k in ['fileID','domain','relativePath','sha256']},'entries':entries,'sha256_before':before,'sha256_after':c.sha(cp),'limit':'mdn match transfer is the literal label-remapping action; it does not prove transfer of a phone, SIM insertion or a boot'})
# Exact scalar identity crosschecks, not unbounded strings from personal payloads.
info=plistlib.loads((c.BACKUP/'Info.plist').read_bytes());status=plistlib.loads((c.BACKUP/'Status.plist').read_bytes());ph=c.ro(find('Photos.sqlite'));h=c.ro(find('healthdb.sqlite'));hd=plistlib.loads(find('com.apple.healthd.plist').read_bytes());keychain=plistlib.loads(find('keychain-backup.plist').read_bytes())
ids={'TP02_UDID':info['Unique Identifier'],'Photos_current_store_UUID':ph.execute('select Z_UUID from Z_METADATA').fetchone()[0],'Health_hardware_ID_2':h.execute('select hardware_identifier from sync_identities where ROWID=2').fetchone()[0],'Health_database_ID_2':h.execute('select database_identifier from sync_identities where ROWID=2').fetchone()[0],'Health_source_UUID_1':h.execute('select uuid from sources where rowid=1').fetchone()[0],'Backup_Info_GUID':info.get('GUID'),'Backup_Status_UUID':status.get('UUID'),'Keychain_keybag_UUID':keychain.get('keybag-uuid')}
patterns={}
for name,val in ids.items():
 if val is None:continue
 pats=[val.lower().encode(),val.encode('utf-16le')] if isinstance(val,str) else [val,str(uuid.UUID(bytes=val)).encode(),str(uuid.UUID(bytes=val)).upper().encode()] if len(val)==16 else [val]
 patterns[name]=pats
matches=[];checked=0
for rec in logs:
 path=Path(rec['output'])
 if path.stat().st_size>32*1024**2 or path.name=='keychain-backup.plist':continue
 checked+=1;data=path.read_bytes()
 for name,pats in patterns.items():
  if any(pat in data or (isinstance(ids[name],str) and pat in data.lower()) for pat in pats):matches.append({'identifier':name,'domain':rec['domain'],'relativePath':rec['relativePath'],'fileID':rec['fileID'],'sha256':rec['sha256']})
save('cross-artifact-identifier-matches.json',{'identifiers':[{'name':k,'sha256':sh(v),'type':type(v).__name__,'length':len(v)} for k,v in ids.items() if v is not None],'checked_files':checked,'matches':matches,'limit':'literal encoded-value comparison; no hardware binding inferred solely from UUID match; large Photos DB examined separately via SQL'})
# Two existing OP-01 raw WLAN artefacts. Validate record envelopes and expose time coverage, not personal networks.
kn=plistlib.loads(find('com.apple.wifi.known-networks.plist').read_bytes())['wifi.network.ssid.ASUS_Z01RD'];pr=plistlib.loads(find('com.apple.wifi-private-mac-networks.plist').read_bytes());private=next(x for x in pr['List of scanned networks with private mac'] if x.get('SSID_STR')=='ASUS_Z01RD')
needles={'SSID':[b'ASUS_Z01RD','ASUS_Z01RD'.encode('utf16le') if False else 'ASUS_Z01RD'.encode('utf-16le')],'private_client_mac':[private['PRIVATE_MAC_ADDRESS']['PRIVATE_MAC_ADDRESS_VALUE']]}
for i,x in enumerate(kn.get('BSSList',[])):
 raw=bytes(int(y,16) for y in x['BSSID'].split(':'));needles['AP_BSSID_'+str(i)]=[raw,x['BSSID'].encode(),x['BSSID'].upper().encode(),x['BSSID'].encode('utf-16le')]
results=[]
paths=[Path('ordinateur/recherche-OP-01/extractions-acces/raw/Windows/System32/winevt/Logs/Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx'),Path('ordinateur/recherche-OP-01/integrite-evtx/ntfs/deleted-evtx-data/677359-Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx')]
for path in paths:
 data=path.read_bytes();out={'path':str(path),'sha256':sh(data),'bytes':len(data),'file_header_valid':data[:8]==b'ElfFile\0','literal_hits':{k:sum(data.count(pat) for pat in vals) for k,vals in needles.items()},'chunks':[]};pos=data.find(b'ElfChnk\0');dates=[];record_count=0
 while pos!=-1:
  chunk=data[pos:pos+65536]
  if len(chunk)<65536:break
  free=struct.unpack_from('<I',chunk,48)[0]
  if 512<=free<=65536:
   hc=struct.unpack_from('<I',chunk,124)[0]==zlib.crc32(chunk[:120]+chunk[128:512]);dc=struct.unpack_from('<I',chunk,52)[0]==zlib.crc32(chunk[512:free]);off=512;count=0
   while off+28<=free and chunk[off:off+4]==b'**\0\0':
    size=struct.unpack_from('<I',chunk,off+4)[0]
    if size<28 or off+size>free or struct.unpack_from('<I',chunk,off+size-4)[0]!=size:break
    rid,ft=struct.unpack_from('<QQ',chunk,off+8);d=dt.datetime(1601,1,1,tzinfo=U)+dt.timedelta(microseconds=ft//10)
    if hc and dc:dates.append(d.isoformat());record_count+=1
    count+=1;off+=size
   out['chunks'].append({'file_offset':pos,'header_crc_ok':hc,'data_crc_ok':dc,'record_envelopes':count})
  pos=data.find(b'ElfChnk\0',pos+8)
 out.update(validated_record_envelopes=record_count,earliest_utc=min(dates) if dates else None,latest_utc=max(dates) if dates else None,records_oct17=sum(s.startswith('2024-10-17') for s in dates),sha256_after=c.sha(path));results.append(out)
save('op01-raw-wlan-controls.json',{'files':results,'mounted_windows_available':Path('/mnt/windows/Windows').exists(),'source_E01_available':Path('/mnt/data/forensic/SADEDINE-2026/OP-01/OP01.E01').exists(),'limits':['Record envelope parser reuses format checks from OP-01 integrite-evtx scripts','No BinXML event semantics decoded; literal MAC searches can miss alternate encodings','No OP-01 disk remount or new volume extraction','Corrupted recovered file assessed only where chunk and record framing validate']})
# Add the actual remapping history timestamp, as distinct from from_dated.
with (O/'activite-17octobre.csv').open() as f:rd=csv.DictReader(f);fields_csv=rd.fieldnames;timeline=list(rd)
for x in entries:
 ds=x['dates']['ts'];timeline.append(dict(domain=rec['domain'] if False else 'WirelessDomain',relativePath='Library/Preferences/com.apple.commcenter.data.archive.plist',fileID=next(v['fileID'] for v in logs if Path(v['output'])==cp),sha256=before,locator='$/label-remap-history/[id]/ts',raw_value=str(ds['raw_unix']),format='unix',utc=ds['utc'],paris=ds['paris'],in_1645_1800='True',kind='historique CommCenter',observation='action=mdn match transfer; remappage de libellé',requirements_at_source='traitement CommCenter; ni boot ni changement de matériel prouvé',TP02_attribution='rattachement à installation à évaluer; copie du plist possible'))
c.write_csv(O/'activite-17octobre.csv',sorted(timeline,key=lambda x:(x['utc'],x['fileID'],x['locator'])),fields_csv)
save('crosscheck-operations.json',{'script_sha256':c.sha(__file__),'utc':dt.datetime.now(U).isoformat(),'day_events':len(timeline),'focus_events':sum(x['in_1645_1800']=='True' for x in timeline),'source_writes':False,'new_extraction':False})
print(json.dumps({'day_events':len(timeline),'focus_events':sum(x['in_1645_1800']=='True' for x in timeline),'identifier_matches':len(matches),'op01':[(x['validated_record_envelopes'],x['earliest_utc'],x['latest_utc'],x['records_oct17'],x['literal_hits']) for x in results]}))
