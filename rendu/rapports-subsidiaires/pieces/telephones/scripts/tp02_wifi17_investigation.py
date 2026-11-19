#!/usr/bin/env python3
"""Read-only discriminating TP-02 Wi-Fi/installation investigation. No secrets exported.
Run from repository root, with a new output directory. Reuses extracted evidence exclusively.
"""
import argparse,collections,csv,datetime as dt,hashlib,io,json,os,plistlib,re,sqlite3,struct,uuid
from pathlib import Path
import tp02_forensic as c
p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args();os.umask(0o077)
R=Path('telephones/recherche-TP-02');O=Path(a.out);O.mkdir(parents=True,exist_ok=False)
logs=[json.loads(l) for f in sorted(R.glob('extraction-*/extraction.jsonl')) for l in f.read_text().splitlines()];logs=[v for v in logs if v.get('status')=='ok'];index={Path(v['output']).resolve():v for v in logs}
used={};events=[];U=dt.timezone.utc;epoch=dt.datetime(2001,1,1,tzinfo=U);day=dt.datetime(2024,10,17,tzinfo=c.PARIS).astimezone(U);end=day+dt.timedelta(days=1);focuslo=dt.datetime(2024,10,17,16,45,tzinfo=c.PARIS).astimezone(U);focushi=dt.datetime(2024,10,17,18,tzinfo=c.PARIS).astimezone(U)
lo=(day-epoch).total_seconds();hi=(end-epoch).total_seconds()
def sha(x):return hashlib.sha256(x if isinstance(x,bytes) else str(x).encode()).hexdigest()
def save(n,v):
 with (O/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2,default=str);f.write('\n')
def find(n):return next(Path(v['output']) for v in logs if Path(v['relativePath']).name==n)
def source(path):
 path=Path(path).resolve()
 if path not in used:
  rec=index.get(path,{});s={k:rec.get(k) for k in ['domain','relativePath','fileID','sha256','ciphertext_sha256']};s['file']=str(path);s['sha256_now']=c.sha(path);s['bytes']=path.stat().st_size
  s['matches_extraction']=s['sha256_now']==rec.get('sha256') if rec else None
  if rec:
   cipher=c.BACKUP/rec['fileID'][:2]/rec['fileID'];s['ciphertext_sha256_now']=c.sha(cipher);s['ciphertext_matches']=s['ciphertext_sha256_now']==rec['ciphertext_sha256']
  used[path]=s
 return used[path]
def db(path):source(path);x=c.ro(path);x.row_factory=sqlite3.Row;return x
def rows(db,q,args=()):return [dict(v) for v in db.execute(q,args)]
def t(raw,fmt):
 if isinstance(raw,dt.datetime):return raw.replace(tzinfo=U) if raw.tzinfo is None else raw.astimezone(U)
 return epoch+dt.timedelta(seconds=raw) if fmt=='cocoa' else dt.datetime.fromtimestamp(raw,U)
def datespec(raw,fmt='plist_date'):
 d=t(raw,fmt);return {'raw_value':str(raw),'format':fmt,'utc':d.isoformat(),'paris':d.astimezone(c.PARIS).isoformat()}
def ev(path,loc,raw,fmt,kind,meaning,needs='inconnu; enregistrement transportable par copie du fichier'):
 d=t(raw,fmt)
 if not day<=d<end:return
 s=source(path);events.append(dict(domain=s['domain'],relativePath=s['relativePath'],fileID=s['fileID'],sha256=s['sha256_now'],locator=loc,raw_value=str(raw),format=fmt,utc=d.isoformat(),paris=d.astimezone(c.PARIS).isoformat(),in_1645_1800=str(focuslo<=d<=focushi),kind=kind,observation=meaning,requirements_at_source=needs,TP02_attribution='à évaluer; historique copiable'))
def plist(path):source(path);return plistlib.loads(Path(path).read_bytes())
def sanitize_loc(s):
 s=re.sub(r'[A-Fa-f0-9]{8}-[A-Fa-f0-9-]{27,}', '[id]',s)
 s=re.sub(r'[^/\s]*@[^/\s]*','[compte]',s)
 s=re.sub(r'(?<!\w)\+?\d{8,}(?!\w)','[identifiant]',s)
 return s
# Hardware and store identifiers compared exactly, not assumed interchangeable UUIDs.
info=plist(c.BACKUP/'Info.plist');mp=plist(c.BACKUP/'Manifest.plist');status=plist(c.BACKUP/'Status.plist');lock=mp.get('Lockdown',{});current_udid=lock.get('UniqueDeviceID') or info.get('Unique Identifier')
identity={'current_UDID_sha256':sha(current_udid),'serial_matches_attestation':info.get('Serial Number')=='F5466LV9V7','header_UDID_agreement':{k:v==current_udid for k,v in info.items() if k in ['Target Identifier','Unique Identifier']},'product':info.get('Product Type'),'version':info.get('Product Version'),'header_dates':{},'header_identifier_catalog':[]}
for n,v in [('Info',info),('Manifest',mp),('Status',status)]:
 for k,x in v.items():
  if isinstance(x,dt.datetime):identity['header_dates'][n+'/'+k]=datespec(x)
  elif isinstance(x,str) and k in ['GUID','UUID','Unique Identifier','Target Identifier']:identity['header_identifier_catalog'].append({'artifact':n,'key':k,'sha256':sha(x),'length':len(x)})
# Exact selected restoration/setup records; never copy tokens, preflight app list or account values.
backup=find('com.apple.MobileBackup.plist');bv=plist(backup)
restore={'RestoreInfo':bv.get('RestoreInfo'),'RestoreStateInfo':bv.get('RestoreStateInfo'),'DeviceTransferInfo_present':'DeviceTransferInfo' in bv,'DeviceTrransferInfo_present':'DeviceTrransferInfo' in bv,'AirTrafficFinishedRestoring':bv.get('AirTrafficFinishedRestoring'),'cloud_snapshot_id_sha256':sha(bv.get('RestoreCloudFormatInfo',{}).get('SnapshotID','')),'other_dates':{},'FSEvent_UUID_values':[]}
# Selected dictionary has only build versions, booleans, numeric status, dates; reject unknown identifying fields.
for key in ['RestoreInfo','RestoreStateInfo']:
 restore[key]={k:(datespec(v) if isinstance(v,dt.datetime) else v) for k,v in (bv.get(key) or {}).items() if k in ['RestoreDate','BackupBuildVersion','DeviceBuildVersion','WasCloudRestore','estimatedTimeRemaining','progress','date','restoredSnapshotBackupPolicy','isCloud','isBackground','state','backupAttemptCount']}
for k in ['MegaBackupFlowStartDate','AccountEnabledDate']:
 if isinstance(bv.get(k),dt.datetime):restore['other_dates'][k]=datespec(bv[k])
for vol,val in bv.get('FSEventState',{}).get('eventDatabaseUUIDForVolumeUUID',{}).items():restore['FSEvent_UUID_values'].append({'volume_uuid_sha256':sha(vol),'event_database_uuid_sha256':sha(val)})
pu=find('com.apple.purplebuddy.plist');pv=plist(pu);setup={k:pv.get(k) for k in ['SetupDone','SetupFinishedAllSteps','SetupState','RestoreChoice','SetupVersion','setupMigratorVersion','WiFiPresented','SSDeviceType','chronicle']}
for k in ['SetupLastExit']:
 if isinstance(pv.get(k),dt.datetime):setup[k]=datespec(pv[k])
setup['lastPrepareLaunchSentinel_dates']=[datespec(v) for v in pv.get('lastPrepareLaunchSentinel',[]) if isinstance(v,dt.datetime)]
restore['purplebuddy']=setup
sa=find('com.apple.SetupAssistant.plist');sav=plist(sa);restore['SetupAssistant']={k:(datespec(v,'unix') if k=='CKStartupTime' else v) for k,v in sav.items() if k in ['CKStartupTime','CKPerBootTasks']}
# Profile summary and events only, not payload secrets.
profiles=[]
for rec in logs:
 if 'configurationprofiles' not in rec['domain'] or not rec['relativePath'].endswith('.plist') or rec.get('size',0)==0:continue
 path=Path(rec['output'])
 try:v=plist(path)
 except Exception:continue
 entry={'relativePath':rec['relativePath'],'fileID':rec['fileID'],'keys':list(v) if isinstance(v,dict) else []}
 if path.name=='CloudConfigurationDetails.plist':entry['configuration']={k:v.get(k) for k in ['PostSetupProfileWasInstalled','IsSupervised','CloudConfigurationUIComplete','ConfigurationSource','AllowPairing','ConfigurationWasApplied']}
 profiles.append(entry)
restore['configuration_profiles']=profiles
save('installation-restoration-details.json',restore)
# Full network comparison (SSID aliases except target), including raw dates and private coverage.
kp=find('com.apple.wifi.known-networks.plist');prp=find('com.apple.wifi-private-mac-networks.plist');kn=plist(kp);pr=plist(prp);priv=pr.get('List of scanned networks with private mac',[])
netrows=[];datecols=['AddedAt','JoinedByUserAt','JoinedBySystemAt','LastDiscoveredAt','UpdatedAt','WiFiNetworkPasswordModificationDate','addedAt','MacGenerationTimeStamp','FirstJoinWithNewMacTimestamp','lastJoined','lastUpdated','LinkDownTimestamp'];rawdatefiles=[]
for path in [kp,prp]:
 b=Path(path).read_bytes();parser=plistlib._BinaryPlistParser(dict);parser.parse(io.BytesIO(b));objects=[]
 for i,off in enumerate(parser._object_offsets):
  if b[off]==0x33:
   val=struct.unpack('>d',b[off+1:off+9])[0];d=epoch+dt.timedelta(seconds=val);objects.append({'object_index':i,'byte_offset':off,'raw_cocoa_seconds':val,'raw_double_hex':b[off+1:off+9].hex(),'utc':d.isoformat(),'paris':d.astimezone(c.PARIS).isoformat()})
 rawdatefiles.append({'fileID':source(path)['fileID'],'dates':objects})
def normmac(v):
 if isinstance(v,bytes):return v
 try:return bytes(int(x,16) for x in v.split(':'))
 except (AttributeError,ValueError):return b''
for i,(key,v) in enumerate(kn.items(),1):
 ssid=v.get('SSID');target=ssid==b'ASUS_Z01RD';alias='ASUS_Z01RD' if target else f'network-{i:02d}'
 prs=[(j,x) for j,x in enumerate(priv) if x.get('SSID_STR','').encode()==ssid];ix,ps=prs[0] if prs else (None,{})
 row={'network_alias':alias,'SSID_sha256':sha(ssid),'reason':v.get('AddReason'),'known_locator':('wifi.network.ssid.ASUS_Z01RD' if target else f'top-level index={i-1}; SSID hash'),'known_fileID':source(kp)['fileID'],'known_sha256':source(kp)['sha256_now'],'private_fileID':source(prp)['fileID'],'private_sha256':source(prp)['sha256_now'],'private_entry_index':ix,'private_entry_count':len(prs),'security':v.get('SupportedSecurityTypes'),'PrivateMacAddReason':ps.get('PrivateMacAddReason'),'preSwUpdateNetwork':ps.get('preSwUpdateNetwork'),'successful_private_assoc':ps.get('privateMacSuccessfulAssocAtleastOnce'),'NoAssociationWithNewMac':ps.get('NoAssociationWithNewMac'),'private_mac_present':bool(ps.get('PRIVATE_MAC_ADDRESS',{}).get('PRIVATE_MAC_ADDRESS_VALUE')),'BSS_count':len(v.get('BSSList',[]))}
 for field in datecols:
  val=v.get(field) if field in v else v.get('__OSSpecific__',{}).get(field) if field=='WiFiNetworkPasswordModificationDate' else ps.get(field)
  for col in ['raw_decoded','raw_cocoa_seconds','utc','paris']:row[field+'_'+col]=''
  if isinstance(val,dt.datetime):
   ds=datespec(val);row[field+'_raw_decoded']=str(val);row[field+'_utc']=ds['utc'];row[field+'_paris']=ds['paris'];match=[z for x in rawdatefiles for z in x['dates'] if z['utc']==ds['utc']];row[field+'_raw_cocoa_seconds']=match[0]['raw_cocoa_seconds'] if match else ''
 if all(isinstance(ps.get(k),dt.datetime) for k in ['MacGenerationTimeStamp','FirstJoinWithNewMacTimestamp']):row['generation_to_firstjoin_seconds']=(ps['FirstJoinWithNewMacTimestamp']-ps['MacGenerationTimeStamp']).total_seconds()
 else:row['generation_to_firstjoin_seconds']=''
 row['addedAt_equal_between_files']=v.get('AddedAt')==ps.get('addedAt') if v.get('AddedAt') and ps.get('addedAt') else None
 row['user_join_precedes_added']=v.get('JoinedByUserAt')<v.get('AddedAt') if v.get('JoinedByUserAt') and v.get('AddedAt') else None
 row['private_BSSID_matches_BSS_indices']=str([j for j,x in enumerate(v.get('BSSList',[])) if normmac(x.get('BSSID')) and normmac(x.get('BSSID'))==normmac(ps.get('BSSID'))])
 netrows.append(row)
c.write_csv(O/'comparaison-reseaux.csv',netrows,list(netrows[0]))
save('wifi-binary-date-validation.json',rawdatefiles)
stats={}
for reason in sorted({v['reason'] for v in netrows}):
 subset=[v for v in netrows if v['reason']==reason];stats[reason]={'networks':len(subset),'private_entries':sum(v['private_entry_count']>0 for v in subset),'generation_dates':sum(bool(v['MacGenerationTimeStamp_utc']) for v in subset),'firstjoin_dates':sum(bool(v['FirstJoinWithNewMacTimestamp_utc']) for v in subset),'both_dates':sum(bool(v['MacGenerationTimeStamp_utc'] and v['FirstJoinWithNewMacTimestamp_utc']) for v in subset),'user_join_precedes_added':sum(v['user_join_precedes_added'] is True for v in subset),'identical_addedAt':sum(v['addedAt_equal_between_files'] is True for v in subset)}
save('network-comparison-summary.json',stats)
# Photos migration and embedded journal: validate exact byte boundaries with bplist trailer.
pp=find('Photos.sqlite');ph=db(pp);store=ph.execute('SELECT Z_UUID FROM Z_METADATA').fetchone()[0]
mr=rows(ph,'SELECT Z_PK,ZMIGRATIONDATE,ZDEVICEUNIQUEID,ZSTOREUUID,ZFRAMEWORKUUID,ZHARDWAREMODEL,ZOSVERSION,ZMIGRATIONTYPE,ZORIGIN,ZCPLENABLED,ZFORCEREBUILDREASON,ZMODELVERSION,ZSOURCEMODELVERSION,ZINITIALSYNCDATE FROM ZMIGRATIONHISTORY')
for v in mr:
 v['device_id_matches_backup_UDID']=v['ZDEVICEUNIQUEID']==current_udid;v['device_id_sha256']=sha(v.pop('ZDEVICEUNIQUEID'));v['store_uuid_matches_current']=v['ZSTOREUUID']==store;v['store_uuid_sha256']=sha(v.pop('ZSTOREUUID'));v['framework_uuid_sha256']=sha(v.pop('ZFRAMEWORKUUID'));v['date']=datespec(v['ZMIGRATIONDATE'],'cocoa')
jp=find('MigrationHistory-change.plj');source(jp);jb=jp.read_bytes();records=[];nested=0
for start in [m.start() for m in re.finditer(b'bplist00',jb)]:
 for finish in range(start+40,len(jb)+1):
  tail=jb[finish-32:finish]
  if tail[:6]!=b'\0'*6 or tail[6] not in [1,2,4,8] or tail[7] not in [1,2,4,8]:continue
  n=int.from_bytes(tail[8:16],'big');top=int.from_bytes(tail[16:24],'big');off=int.from_bytes(tail[24:32],'big')
  if n<1 or top>=n or off<8 or off+n*tail[6]!=finish-start-32:continue
  try:v=plistlib.loads(jb[start:finish])
  except Exception:continue
  if 'migrationDate' not in v:nested+=1;break
  rec={'start_offset':start,'end_offset_exclusive':finish,'embedded_sha256':sha(jb[start:finish]),'device_matches_UDID':v.get('deviceUniqueID')==current_udid,'store_matches_current':v.get('storeUUID')==store,'date':datespec(v['migrationDate']),'hardware':v.get('hardwareModel'),'os_build':v.get('osVersion'),'migrationType':v.get('migrationType'),'origin':v.get('origin'),'modelVersion':v.get('modelVersion'),'sqlite_matching_pks':[z['Z_PK'] for z in mr if z['date']['utc']==datespec(v['migrationDate'])['utc'] and z['ZOSVERSION']==v.get('osVersion') and z['ZMIGRATIONTYPE']==v.get('migrationType')]};records.append(rec);break
photo={'migration_rows':mr,'current_store_uuid_sha256':sha(store),'journal_records':records,'embedded_archives_skipped':nested,'journal_format_limit':'Only independently validated embedded bplists decoded; outer journal framing not interpreted','global_dates':rows(ph,'SELECT Z_PK,ZKEY,ZDATEVALUE FROM ZGLOBALKEYVALUE WHERE ZDATEVALUE IS NOT NULL')}
for v in photo['global_dates']:v['date']=datespec(v['ZDATEVALUE'],'cocoa')
# Persistent history monotonicity and historical contexts near the day.
trq='''SELECT t.Z_PK,t.ZTIMESTAMP,a.ZNAME author,b.ZNAME bundle,n.ZNAME context,ps.ZNAME process FROM ATRANSACTION t LEFT JOIN ATRANSACTIONSTRING a ON a.Z_PK=t.ZAUTHORTS LEFT JOIN ATRANSACTIONSTRING b ON b.Z_PK=t.ZBUNDLEIDTS LEFT JOIN ATRANSACTIONSTRING n ON n.Z_PK=t.ZCONTEXTNAMETS LEFT JOIN ATRANSACTIONSTRING ps ON ps.Z_PK=t.ZPROCESSIDTS WHERE t.ZTIMESTAMP>=? AND t.ZTIMESTAMP<? ORDER BY t.Z_PK'''
pt=rows(ph,trq,(lo,hi));photo['transactions_17']=pt
for v in pt:ev(pp,f"ATRANSACTION.Z_PK={v['Z_PK']}",v['ZTIMESTAMP'],'cocoa','transaction Photos',v['context'],'exécution assetsd nécessaire sur appareil source lors du commit; réseau non prouvé par seul libellé CPL; aucun déverrouillage requis établi')
photo['transaction_neighbors']=rows(ph,'SELECT Z_PK,ZTIMESTAMP FROM ATRANSACTION WHERE Z_PK BETWEEN 117243 AND 117249 ORDER BY Z_PK')
photo['time_regressions_2024_2025']=rows(ph,'''SELECT Z_PK,ZTIMESTAMP,prev,prev-ZTIMESTAMP regression_seconds FROM (SELECT Z_PK,ZTIMESTAMP,lag(ZTIMESTAMP) over(order by Z_PK) prev FROM ATRANSACTION) WHERE ZTIMESTAMP BETWEEN ? AND ? AND ZTIMESTAMP<prev ORDER BY regression_seconds DESC LIMIT 10''',((dt.datetime(2024,1,1,tzinfo=U)-epoch).total_seconds(),(dt.datetime(2026,1,1,tzinfo=U)-epoch).total_seconds()))
# Serialize a local SQLite snapshot to memory and re-read relevant history on a disposable file: proof of copying rows, not iOS restore experiment.
mem=sqlite3.connect(':memory:');ph.backup(mem);preserved=mem.execute('SELECT Z_PK,ZTIMESTAMP FROM ATRANSACTION WHERE Z_PK IN (117245,117246)').fetchall();photo['logical_copy_control']={'method':'sqlite3.Connection.backup to :memory: only','preserved_transaction_rows':[list(v) for v in preserved],'identical':preserved==[tuple(v) for v in ph.execute('SELECT Z_PK,ZTIMESTAMP FROM ATRANSACTION WHERE Z_PK IN (117245,117246)')],'limit':'demonstrates logical history preservation by copy, not restore behavior of iOS 17/18'};mem.close()
save('photos-continuity-and-journal.json',photo)
identity['photo_migration_UDID_matches']=sum(v['device_id_matches_backup_UDID'] for v in mr);identity['photo_store_uuid_matches']=sum(v['store_uuid_matches_current'] for v in mr)
# Health identities and dates without quantities or personal health preferences.
hp=find('healthdb.sqlite');sp=find('healthdb_secure.sqlite');h=db(hp);hs=db(sp);hdp=find('com.apple.healthd.plist');hd=plist(hdp)
health={'identities':[],'device_context':rows(h,'SELECT ROWID,sync_identity_id,device_type,currentOS_name,currentOS_version,product_type_name,date_modified FROM device_context'),'source_devices':rows(h,'SELECT ROWID,hardware,software,creation_date,sync_provenance,sync_identity,length(localIdentifier) identifier_length FROM source_devices'),'technical_kv_keys':rows(h,"SELECT ROWID,domain,key,mod_date,sync_identity FROM key_value WHERE domain LIKE '%sync%' OR key LIKE '%identifier%' OR key LIKE '%database%'")}
for v in rows(h,'SELECT * FROM sync_identities'):
 for k in ['hardware_identifier','database_identifier']:
  v[k+'_matches_healthd']=(v[k]==hd.get('SyncIdentityHardwareIdentifier')) if k=='hardware_identifier' else False;v[k+'_sha256']=sha(v[k]);v[k+'_zero']=not any(v[k]);del v[k]
 health['identities'].append(v)
health['samples17_by_creation']=rows(hs,'''SELECT s.data_id,s.data_type,s.start_date,s.end_date,o.creation_date,p.sync_identity,p.sync_provenance FROM samples s JOIN objects o USING(data_id) JOIN data_provenances p ON p.rowid=o.provenance WHERE o.creation_date>=? AND o.creation_date<? ORDER BY o.creation_date,s.data_id''',(lo,hi))
for v in health['samples17_by_creation']:
 for field in ['start_date','end_date','creation_date']:
  v[field+'_converted']=datespec(v[field],'cocoa')
  ev(sp,f"samples.data_id={v['data_id']}->"+field,v[field],'cocoa','Santé '+field,'type '+str(v['data_type'])+'; intervalle et création distincts','calcul/écriture automatique possible; aucune manipulation requise; objet transférable')
health['cloud_tables_counts']={tab:h.execute('SELECT count(*) FROM '+tab).fetchone()[0] for tab in ['sync_stores','cloud_sync_stores','cached_sync_requests','sync_anchors']}
health['old_technical_preference_dates']={k:datespec(v) for k,v in hd.items() if k in ['HDAchievementDoctorLastSuccessfulRunDate','HDAWDSubmissionManager.FitnessFriendsMonthly.LastSubmissionAttempt'] and isinstance(v,dt.datetime)}
save('health-continuity-details.json',health);save('identifier-comparisons.json',identity)
# New TipKit process history and address book transactions: no text or contacts.
tips=[]
for sub in ['com.apple.mobilephone','com.apple.MobileSMS']:
 path=R/'extraction-systeme-20261014/files/AppDomainGroup-group.com.apple.tipsnext'/sub/'.tipkit/tips-store.db';d=db(path);transactions=rows(d,trq,(lo,hi))
 for v in transactions:
  v['changes']=rows(d,'SELECT ch.Z_PK,ch.ZCHANGETYPE,pk.Z_NAME entity,ch.ZENTITYPK FROM ACHANGE ch JOIN Z_PRIMARYKEY pk ON pk.Z_ENT=ch.ZENTITY WHERE ch.ZTRANSACTIONID=?',(v['Z_PK'],));ev(path,f"ATRANSACTION.Z_PK={v['Z_PK']}",v['ZTIMESTAMP'],'cocoa','transaction TipKit',str(v['process'])+'; '+str(v['author']),'moteur de règles local sur appareil source; pas une preuve de tip affiché ou de premier plan; historique copiable')
 tips.append({'client':sub,'transactions_17':transactions,'lastdisplayed_17_count':d.execute('SELECT count(*) FROM ZCORETIPRECORD WHERE ZLASTDISPLAYED>=? AND ZLASTDISPLAYED<?',(lo,hi)).fetchone()[0],'schema_has_ANSCK_tables':d.execute("SELECT count(*) FROM sqlite_master WHERE name LIKE 'ANSCK%'").fetchone()[0]})
save('tipkit-process-events.json',tips)
ap=find('AddressBook.sqlitedb');ad=db(ap);ar=rows(ad,'SELECT ROWID,client_identifier,sequence_number,save_timestamp FROM ClientSequence WHERE save_timestamp>=? AND save_timestamp<?',(lo,hi))
for v in ar:v['client_identifier_sha256']=sha(v.pop('client_identifier'));ev(ap,f"ClientSequence.ROWID={v['rowid'] if 'rowid' in v else v['ROWID']}",v['save_timestamp'],'cocoa','AddressBook séquence','save_timestamp de séquence client','enregistrement de séquence; origine locale/compte non discriminée')
save('addressbook-sequence-events.json',ar)
# Bounded scan for all already extracted structured dates incl. embedded bplist (not a new backup inventory).
scan={'files':0,'parsed':0,'embedded_plists':0,'errors':[]};seen=set()
def walk(v,path,loc,depth=0):
 if depth>25:return
 if isinstance(v,dict):
  for k,x in v.items():
   if re.search('password|secret|token|rotationkey',str(k),re.I) and not re.search('date|time',str(k),re.I):continue
   walk(x,path,loc+'/'+sanitize_loc(str(k)),depth+1)
 elif isinstance(v,list):
  for j,x in enumerate(v):walk(x,path,loc+'/'+str(j),depth+1)
 elif isinstance(v,dt.datetime):ev(path,loc,v,'plist_date','date plist','propriété datée; sémantique non déduite du seul nom')
 elif isinstance(v,bytes) and v.startswith(b'bplist00') and len(v)<1024**2:
  try:nested=plistlib.loads(v)
  except Exception:return
  scan['embedded_plists']+=1;walk(nested,path,loc+'/[embedded plist]',depth+1)
 elif isinstance(v,(int,float)) and not isinstance(v,bool) and re.search('time|date',loc.split('/')[-1],re.I):
  for fmt,offset in [('unix',0),('cocoa',978307200)]:
   if day.timestamp()<=v+offset<end.timestamp():ev(path,loc,v,fmt,'scalaire temporel candidat','format candidat à valider; possible identifiant numérique')
for rec in logs:
 path=Path(rec['output'])
 if path.stat().st_size>32*1024**2 or path.name=='keychain-backup.plist':continue
 with path.open('rb') as f:sig=f.read(16)
 if not sig.startswith((b'bplist00',b'<?xml',b'{',b'[')):continue
 scan['files']+=1
 try:
  data=path.read_bytes()
  if sig.startswith((b'bplist00',b'<?xml')):v=plistlib.loads(data)
  else:v=json.loads(data.decode())
  scan['parsed']+=1;walk(v,path,'$')
 except Exception as e:scan['errors'].append({'fileID':rec['fileID'],'class':type(e).__name__})
save('structured-date-scan-coverage.json',scan)
# Existing SQLite triage candidates: deduplicated by file/table/row/column/raw/format, not re-labelled as proven events.
candidates=[];seen=set()
for f in sorted(R.glob('analyse-*/temporal-candidates.csv')):
 with f.open() as fd:
  for v in csv.DictReader(fd):
   if not day.isoformat()<=v.get('utc','')<end.isoformat():continue
   key=tuple(v.get(k,'') for k in ['file','table','sqlite_rowid','column','raw_value','format_hypothesis'])
   if key in seen:continue
   seen.add(key);candidates.append({k:v.get(k) for k in ['file','fileID','table','sqlite_rowid','column','raw_value','format_hypothesis','utc','paris']})
save('previous-sqlite-candidates-17.json',candidates)
# Targeted manifest coverage: document absent categories and available extracted candidates with exact fileIDs.
coverage={}
with c.ro(c.MANIFEST) as ma:
 for term in ['.obliterated','data_ark','CloudConfiguration','CurrentPowerLog','netusage','ADDataStore','knowledgeC','shutdown','configurationprofiles','CrashReporter','MobileBackup','backupd','timed','mobileactivation','NetworkInterfaces','ICLOUD.apple.wifid']:
  rr=[dict(zip(['fileID','domain','relativePath','flags'],v)) for v in ma.execute('SELECT fileID,domain,relativePath,flags FROM Files WHERE relativePath LIKE ?',('%'+term+'%',))];coverage[term]=rr
save('targeted-manifest-coverage.json',coverage)
# Clock snapshot, keychain wrapper structure only; do not access or export encrypted v_Data contents.
timed=find('com.apple.timed.plist');tv=plist(timed);clock={k:tv.get(k) for k in ['TMAutomaticTimeZoneEnabled','TMAutomaticTimeOnlyEnabled','NtpUseServicePort']};save('clock-snapshot.json',clock)
keychain=find('keychain-backup.plist');kv=plist(keychain);save('keychain-format-limit.json',{'fileID':source(keychain)['fileID'],'categories':{k:len(v) for k,v in kv.items() if isinstance(v,list)},'item_key_sets':{k:sorted({key for v in vals for key in v}) for k,vals in kv.items() if isinstance(vals,list)},'keybag_uuid_sha256':sha(kv.get('keybag-uuid','')),'limit':'Only encrypted v_Data and v_PersistentRef wrappers; no readable Wi-Fi dates/sync attributes validated; no inner decryption performed'})
# Deduplicate all-day date fields; preserve separate locations/formats.
unique={tuple(v[k] for k in ['fileID','locator','raw_value','format']):v for v in events};events=sorted(unique.values(),key=lambda v:(v['utc'],v['fileID'],v['locator']))
c.write_csv(O/'activite-17octobre.csv',events,list(events[0]));
for path,v in used.items():v['sha256_after']=c.sha(path);v['unchanged']=v['sha256_after']==v['sha256_now']
save('source-verification.json',list(used.values()))
save('operations.json',{'script_sha256':c.sha(__file__),'utc':dt.datetime.now(U).isoformat(),'sources':len(used),'all_plaintext_matches':all(v['matches_extraction'] is not False for v in used.values()),'all_ciphertext_matches':all(v.get('ciphertext_matches',True) for v in used.values()),'all_unchanged':all(v['unchanged'] for v in used.values()),'day_events':len(events),'focus_events':sum(v['in_1645_1800']=='True' for v in events),'networks':len(netrows),'journal_records':len(records),'new_extraction':False,'originals_written':False,'tipkit_transactions17':{v['client']:len(v['transactions_17']) for v in tips}})
print(json.dumps({'networks':len(netrows),'journal_records':len(records),'sources':len(used),'day_events':len(events),'focus_events':sum(v['in_1645_1800']=='True' for v in events),'tipkit_transactions17':{v['client']:len(v['transactions_17']) for v in tips},'network_summary':stats}))
