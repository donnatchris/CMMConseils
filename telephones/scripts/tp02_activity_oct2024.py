#!/usr/bin/env python3
"""Targeted, read-only TP-02 follow-up. No quantities, communications or network secrets exported.
Run from repository root; output must be new. SQLite main files opened immutable, WAL presence audited.
"""
import argparse, collections, csv, datetime as dt, hashlib, json, os, plistlib, re, sqlite3, struct
from pathlib import Path
import tp02_forensic as c
p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args()
os.umask(0o077);root=Path('telephones/recherche-TP-02');out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
def save(name,v): (out/name).write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str)+'\n')
def rows(db,q,args=()): return [dict(x) for x in db.execute(q,args)]
def db(path):
 x=c.ro(path);x.row_factory=sqlite3.Row;return x
review=[]
# Read every pre-existing result JSON/CSV/JSONL, including obsolete passes, without duplicating content.
for f in sorted(root.rglob('*')):
 if not f.is_file() or out in f.parents or root/'approfondissement-activite-202410' in f.parents or 'files' in f.relative_to(root).parts or f.suffix not in ['.json','.jsonl','.csv']:continue
 entry={'path':str(f),'sha256':c.sha(f),'bytes':f.stat().st_size}
 try:
  if f.suffix=='.csv':
   with f.open(newline='') as s:
    reader=csv.DictReader(s);n=0;central=0
    for v in reader:n+=1;central+=str(v.get('central_window','')).lower()=='true'
    entry.update(rows=n,columns=reader.fieldnames,central_rows=central)
  elif f.suffix=='.jsonl':
   data=[json.loads(l) for l in f.read_text().splitlines()];entry.update(rows=len(data),statuses=dict(collections.Counter(v.get('status','') for v in data)))
  else:
   data=json.loads(f.read_text());entry.update(root_type=type(data).__name__,keys=list(data) if isinstance(data,dict) else [],items=len(data) if isinstance(data,(dict,list)) else 1)
  entry['status']='parsed'
 except Exception as e:entry.update(status='error',error_class=type(e).__name__)
 review.append(entry)
save('prior-results-review.json',review)
logs=[json.loads(l) for f in root.glob('extraction-*/extraction.jsonl') for l in f.read_text().splitlines()]
logs=[r for r in logs if r.get('status')=='ok'];index={Path(r['output']).resolve():r for r in logs};used={};events=[]
def source(path):
 path=Path(path).resolve()
 if path not in used:
  rec=index.get(path,{});cipher=c.BACKUP/rec.get('fileID','')[:2]/rec.get('fileID','')
  digest=c.sha(path);info={k:rec.get(k) for k in ['domain','relativePath','fileID','sha256','ciphertext_sha256']}
  info.update(path=str(path),sha256_now=digest,plaintext_matches=digest==rec.get('sha256'),bytes=path.stat().st_size)
  if cipher.is_file():info.update(ciphertext_sha256_now=c.sha(cipher),ciphertext_bytes=cipher.stat().st_size,ciphertext_matches=c.sha(cipher)==rec.get('ciphertext_sha256'))
  used[path]=info
 return used[path]
def find(name,part='extraction-systeme-20261014'):return next((root/part/'files').rglob(name))
def time(raw,fmt):
 if fmt=='plist':return raw.replace(tzinfo=dt.timezone.utc) if raw.tzinfo is None else raw.astimezone(dt.timezone.utc)
 if fmt=='apple_ns':
  sec,ns=divmod(raw,10**9);return dt.datetime.fromtimestamp(sec+978307200,dt.timezone.utc)+dt.timedelta(microseconds=ns//1000)
 return dt.datetime.fromtimestamp(raw+(978307200 if fmt=='apple' else 0),dt.timezone.utc)
def ev(path,loc,raw,fmt,observation,interpretation,end=None):
 d=time(raw,fmt);s=source(path)
 events.append(dict(domain=s['domain'],relativePath=s['relativePath'],fileID=s['fileID'],sha256=s['sha256_now'],locator=loc,raw_value=str(raw),time_format=fmt,utc=d.isoformat(),paris=d.astimezone(c.PARIS).isoformat(),interval_end_utc=time(end,fmt).isoformat() if end is not None else '',observation=observation,interpretation=interpretation,confidence='champ vérifié; attribution matérielle non établie'))
 return d.astimezone(c.PARIS).isoformat()
# Full Wi-Fi property tree, every secret redacted; identifiers represented by equality labels.
labels={}
def label(v,kind):
 b=v if isinstance(v,bytes) else str(v).encode()
 if kind=='bssid' and isinstance(v,str):b=bytes(int(x,16) for x in v.split(':'))
 key=(kind,b)
 if key not in labels:labels[key]=kind+'-'+str(1+sum(k[0]==kind for k in labels))
 return labels[key]
def sanitize(v,key=''):
 low=key.lower()
 if re.search('password|rotationkey|secret|token|psk|keymaterial',low) and not re.search('date|time',low):return {'redacted':'secret non exporté','type':type(v).__name__}
 if low in ['bssid','private_mac_address_value','ipv4networksignature','dhcpserverid'] or re.search('latitude|longitude',low):return label(v,low)
 if isinstance(v,dict):return {k:sanitize(x,k) for k,x in v.items()}
 if isinstance(v,list):return [sanitize(x,key) for x in v]
 if isinstance(v,bytes):return {'type':'data','length':len(v),'text':v.decode('utf8') if key=='SSID' else None}
 if isinstance(v,dt.datetime):return {'type':'plist_date','raw_decoded_utc':str(v),'utc':time(v,'plist').isoformat(),'paris':time(v,'plist').astimezone(c.PARIS).isoformat()}
 return v
known=find('com.apple.wifi.known-networks.plist');private=find('com.apple.wifi-private-mac-networks.plist')
networks=plistlib.loads(known.read_bytes());pr=plistlib.loads(private.read_bytes());network=networks['wifi.network.ssid.ASUS_Z01RD'];private_entries=[(i,v) for i,v in enumerate(pr['List of scanned networks with private mac']) if v.get('SSID_STR')=='ASUS_Z01RD']
wifi={'known_source':source(known),'private_source':source(private),'all_known_properties':sanitize(network),'all_private_properties':[{'index':i,'properties':sanitize(v)} for i,v in private_entries]}
def dates(v,path,loc):
 if isinstance(v,dict):
  for k,x in v.items():dates(x,path,loc+'/'+k)
 elif isinstance(v,list):
  for n,x in enumerate(v):dates(x,path,loc+'/'+str(n))
 elif isinstance(v,dt.datetime):ev(path,loc,v,'plist','état Wi-Fi daté','instantané; historique de provenance non fourni')
dates(network,known,'wifi.network.ssid.ASUS_Z01RD')
for i,v in private_entries:dates(v,private,f'List of scanned networks with private mac/{i}')
other=[]
for k,v in networks.items():
 for field in ['AddedAt','JoinedByUserAt','JoinedBySystemAt']:
  val=v.get(field) if isinstance(v,dict) else None
  if isinstance(val,dt.datetime) and c.START<=time(val,'plist')<=c.END:
   alias='ASUS_Z01RD' if k.endswith('.ASUS_Z01RD') else label(k,'network')
   other.append({'network':alias,'field':field,'paris':time(val,'plist').astimezone(c.PARIS).isoformat(),'raw_utc':str(val)})
wifi['other_networks_in_window']=other
wifi['AddReason_distribution']=dict(collections.Counter(v.get('AddReason') for v in networks.values()))
wifi['reason_date_patterns']=[{'network':label(k,'network') if not k.endswith('.ASUS_Z01RD') else 'ASUS_Z01RD','reason':v.get('AddReason'),'has_user_join': 'JoinedByUserAt' in v,'has_system_join':'JoinedBySystemAt' in v} for k,v in networks.items()]
bss=network.get('BSSList',[])
wifi['comparison']={'BSS_count':len(bss),'unique_BSSID_count':len({v.get('BSSID') for v in bss}),'same_IPv4_signature':len({v.get('IPv4NetworkSignature') for v in bss})==1,'same_DHCP_server':len({v.get('DHCPServerID') for v in bss})==1,'channels':[v.get('Channel') for v in bss], 'private_BSSID_equals_BSS_indices':[[j for j,b in enumerate(bss) if bytes(int(x,16) for x in b['BSSID'].split(':'))==bytes(int(x,16) for x in v['BSSID'].split(':'))] for _,v in private_entries], 'private_mac_locally_administered':[(bool(v['PRIVATE_MAC_ADDRESS']['PRIVATE_MAC_ADDRESS_VALUE'][0]&2)) for _,v in private_entries], 'BSSID_locally_administered':[bool(int(v['BSSID'].split(':')[0],16)&2) for v in bss]}
save('wifi-properties-redacted.json',wifi)
# Corroboration: scan already extracted files for SSID and BSSIDs, emit locations only.
needles=[b'ASUS_Z01RD']+[v['BSSID'].encode() for v in bss]
hits=[]
for rec in logs:
 path=Path(rec['output'])
 if path.stat().st_size>32*1024**2:continue
 data=path.read_bytes();matches=[i for i,n in enumerate(needles) if n in data or n.decode().encode('utf-16-le') in data]
 if matches:hits.append({'fileID':rec['fileID'],'domain':rec['domain'],'relativePath':rec['relativePath'],'needle_indices':matches,'sha256':rec['sha256']})
save('wifi-cross-artifact-hits.json',hits)
# Health times/provenance only. Never query quantity columns.
hp=find('healthdb.sqlite');sp=find('healthdb_secure.sqlite');h=db(hp);s=db(sp);source(hp);source(sp)
lo=c.START.timestamp()-978307200;hi=c.END.timestamp()-978307200
hr=rows(s,'''SELECT s.data_id,s.data_type,s.start_date,s.end_date,o.creation_date,o.provenance,p.sync_identity,p.sync_provenance,p.source_id,p.device_id,p.origin_product_type,p.local_product_type,p.origin_build,p.local_build,p.source_version,p.tz_name,p.derived_flags,hex(o.uuid) sample_uuid FROM samples s JOIN objects o USING(data_id) JOIN data_provenances p ON p.rowid=o.provenance WHERE s.start_date BETWEEN ? AND ? ORDER BY s.start_date''',(lo,hi))
names={7:'HKQuantityTypeIdentifierStepCount',8:'HKQuantityTypeIdentifierDistanceWalkingRunning',9:'HKQuantityTypeIdentifierBasalEnergyBurned',10:'HKQuantityTypeIdentifierActiveEnergyBurned'}
for v in hr:
 v['sample_uuid_sha256']=hashlib.sha256(bytes.fromhex(v.pop('sample_uuid'))).hexdigest();v['type_name']=names[v['data_type']]
 for field in ['start_date','end_date','creation_date']:
  v[field+'_paris']=ev(sp,f"samples.data_id={v['data_id']}"+('->objects.creation_date' if field=='creation_date' else '.'+field),v[field],'apple','Santé '+v['type_name']+' '+field,'intervalle représenté distinct de création; enregistrement automatique possible',v['end_date'] if field=='start_date' else None)
 v['creation_minus_end_seconds']=v['creation_date']-v['end_date']
health={'samples':hr,'types':dict(collections.Counter(v['type_name'] for v in hr)),'day_type_counts':dict(collections.Counter(v['start_date_paris'][:10]+'|'+v['type_name'] for v in hr)), 'creation_groups':dict(collections.Counter(v['creation_date_paris'] for v in hr)), 'hour_intervals_type9':sum(abs(v['end_date']-v['start_date']-3600)<0.001 for v in hr if v['data_type']==9)}
health['source_rows']=rows(h,'SELECT ROWID,local_device,product_type,provenance,sync_identity,logical_source_id FROM sources')
health['devices']=rows(h,'SELECT ROWID,model,hardware,software,creation_date,sync_provenance,sync_identity,length(localIdentifier) localIdentifier_length,hex(uuid) uuid FROM source_devices')
for v in health['devices']:v['uuid_sha256']=hashlib.sha256(bytes.fromhex(v.pop('uuid'))).hexdigest()
health['sync_identities']=[]
for v in rows(h,'SELECT * FROM sync_identities'):
 for k in ['hardware_identifier','database_identifier']:
  b=v[k];v[k+'_length']=len(b);v[k+'_all_zero']=not any(b);v[k+'_sha256']=hashlib.sha256(b).hexdigest();del v[k]
 health['sync_identities'].append(v)
health['all_sample_identity_counts']=rows(s,'SELECT p.sync_identity,p.origin_product_type,p.local_product_type,count(*) n,min(s.start_date) first_start,max(s.start_date) last_start FROM samples s JOIN objects o USING(data_id) JOIN data_provenances p ON p.rowid=o.provenance GROUP BY 1,2,3')
# Keys only; user-entered metadata flag if available, no other values.
health['metadata_keys_central']=rows(s,'''SELECT k.key,count(*) n FROM metadata_values v JOIN metadata_keys k ON k.rowid=v.key_id JOIN samples s ON s.data_id=v.object_id WHERE s.start_date BETWEEN ? AND ? GROUP BY k.key''',(lo,hi))
save('health-details.json',health)
# Messages and input context linkage by exact CK SHA1(chat_identifier), export match result only.
mp=find('sms.db');m=db(mp)
fields='ROWID,date,date_read,date_delivered,is_read,is_finished,is_from_me,is_sent,is_delivered,service,version,message_source,ck_sync_state,did_notify_recipient,was_delivered_quietly,is_system_message,is_service_message'
sms=rows(m,'SELECT '+fields+' FROM message WHERE date BETWEEN ? AND ? ORDER BY date',(int(lo*10**9),int(hi*10**9)))
ip=find('UITextInputContextIdentifiers.plist','extraction-complements-20261014')
# Select HomeDomain explicitly, as Safari also has a plist.
ip=root/'extraction-complements-20261014/files/HomeDomain/Library/Preferences/UITextInputContextIdentifiers.plist';iv=plistlib.loads(ip.read_bytes());contexts=[]
for key,val in iv.items():
 if isinstance(val,dt.datetime) and c.START<=time(val,'plist')<=c.END:
  row={'key':key,'raw_utc':str(val),'paris':ev(ip,key,val,'plist','date SETTIME du contexte de clavier','préférence de langue; texte saisi non démontré'),'input_mode_type':type(iv.get(key.removesuffix('_SETTIME'))).__name__}
  contexts.append(row)
for v in sms:
 for field in ['date','date_read','date_delivered']:
  if v[field]:v[field+'_paris']=ev(mp,f"message.ROWID={v['ROWID']}.{field}",v[field],'apple_ns','SMS '+field,'état du message; consultation locale non établie')
 v['read_delay_seconds']=(v['date_read']-v['date'])/1e9
 chats=rows(m,'SELECT c.ROWID,c.chat_identifier,c.last_read_message_timestamp,c.ck_sync_state FROM chat c JOIN chat_message_join j ON j.chat_id=c.ROWID WHERE j.message_id=?',(v['ROWID'],))
 for chat in chats:
  ident=chat.pop('chat_identifier');digest=hashlib.sha1(ident.encode()).hexdigest();chat['context_SHA1_chat_identifier_match']=[k for k in iv if digest in k]
 v['chats_without_identifiers']=chats
save('sms-input-details.json',{'messages':sms,'contexts':contexts})
# Photos group changes: clusters, not a re-export of all assets.
pp=find('Photos.sqlite','extraction-complements-20261014');ph=db(pp);source(pp)
photo={'schema_tables':rows(ph,"SELECT name,sql FROM sqlite_master WHERE type='table' AND (name LIKE '%IMPORT%' OR name LIKE '%HISTORY%' OR name LIKE '%TRANSACTION%')"),'thumbnail_asset':rows(ph,"SELECT a.Z_PK,a.ZDATECREATED,a.ZADDEDDATE,a.ZMODIFICATIONDATE,a.ZCLOUDLOCALSTATE,a.ZCLOUDASSETGUID IS NOT NULL cloud_guid_present,aa.ZLASTVIEWEDDATE,aa.ZIMPORTEDBYBUNDLEIDENTIFIER FROM ZASSET a JOIN ZADDITIONALASSETATTRIBUTES aa ON aa.Z_PK=a.ZADDITIONALATTRIBUTES WHERE a.ZFILENAME='IMG_1773.MP4'")}
for field in ['ZMODIFICATIONDATE','ZADDEDDATE']:
 rr=rows(ph,'SELECT Z_PK,'+field+' t,ZCLOUDASSETGUID IS NOT NULL cloud FROM ZASSET WHERE '+field+' BETWEEN ? AND ?',(lo,hi));counts=collections.Counter(time(v['t'],'apple').astimezone(c.PARIS).isoformat()[:16]+time(v['t'],'apple').astimezone(c.PARIS).isoformat()[-6:] for v in rr)
 photo[field+'_minute_clusters']=counts.most_common(15)
 photo[field+'_central_cloud_guid_counts']=dict(collections.Counter(v['cloud'] for v in rr))
photo['oct28_counts']={}
daylo=dt.datetime(2024,10,28,tzinfo=c.PARIS).timestamp()-978307200
for tab,field in [('ZASSET','ZMODIFICATIONDATE'),('ZASSET','ZADDEDDATE'),('ZADDITIONALASSETATTRIBUTES','ZLASTVIEWEDDATE')]:
 photo['oct28_counts'][field]=ph.execute('SELECT count(*) FROM '+tab+' WHERE '+field+' BETWEEN ? AND ?',(daylo,hi)).fetchone()[0]
save('photos-details.json',photo)
# Panel distinguish executable paths from keyword counts. Export short fixed contexts only.
bp=find('0000000432_2.51.0/main.jsbundle','extraction-cameras-20261014');text=bp.read_text();source(bp);meta=bp.with_suffix(bp.suffix+'.meta');source(meta)
terms=['ipcLocalViewTime','ui_source:\'0000000432\'','p2pIsConnected','showVideoLoad','reGetStream','ipcCommonState','uiPhase:\'preview\'']
panel={'bundle':str(bp),'metadata':str(meta),'meta_bytes':meta.stat().st_size,'meta_format':'opaque; non reconnu JSON/plist','meta_parsed':False,'code_contexts':[]}
for term in terms:
 matches=list(re.finditer(re.escape(term),text));panel['code_contexts'].append({'term':term,'count':len(matches),'contexts':[{'character_offset':v.start(),'text':text[max(0,v.start()-90):v.end()+120]} for v in matches[:3]]})
save('panel-code-details.json',panel)
# Calls: every non-content field distribution, unique IDs hashed solely for comparison.
cp=find('CallHistory.storedata');cl=db(cp);source(cp)
cols=[v['name'] for v in rows(cl,'PRAGMA table_info(ZCALLRECORD)')]
forbidden={'ZADDRESS','ZNAME','ZLOCATION','ZIMAGEURL','ZBLOCKEDBYEXTENSION','ZBLOCKEDBYEXTENSIONNAME','ZUNIQUE_ID','ZCONVERSATIONID','ZLOCALPARTICIPANTUUID','ZOUTGOINGLOCALPARTICIPANTUUID','ZPARTICIPANTGROUPUUID'}
allowed=[k for k in cols if k not in forbidden]
cr=rows(cl,'SELECT '+','.join(allowed)+' FROM ZCALLRECORD WHERE ZDATE BETWEEN ? AND ? ORDER BY ZDATE',(lo,hi))
for v in cr:v['paris']=ev(cp,f"ZCALLRECORD.Z_PK={v['Z_PK']}.ZDATE",v['ZDATE'],'apple','enregistrement d’appel','direction/type sans origine matérielle démontrée')
call={'records':cr,'distributions':{k:dict(collections.Counter(str(v[k]) for v in cr)) for k in allowed if k not in ['Z_PK','ZDATE','ZDURATION']},'schema':rows(cl,"SELECT name,sql FROM sqlite_master WHERE type='table'")}
call['identifier_presence']={k:cl.execute('SELECT count('+k+') FROM ZCALLRECORD WHERE ZDATE BETWEEN ? AND ?',(lo,hi)).fetchone()[0] for k in forbidden if k not in ['ZADDRESS','ZNAME','ZLOCATION','ZIMAGEURL','ZBLOCKEDBYEXTENSION','ZBLOCKEDBYEXTENSIONNAME']}
call['unique_id_cardinality']=cl.execute('SELECT count(distinct ZUNIQUE_ID),count(*) FROM ZCALLRECORD WHERE ZDATE BETWEEN ? AND ?',(lo,hi)).fetchone()[:]
call['all_period_comparison']=rows(cl,'SELECT strftime(\'%Y\',ZDATE+978307200,\'unixepoch\') year,count(*) n,sum(ZLOCALPARTICIPANTUUID IS NOT NULL) localuuid,sum(ZINITIATOR IS NOT NULL) initiator FROM ZCALLRECORD GROUP BY 1')
save('calls-details.json',call)
# Consistency: targeted existing consistency data + current SQLite headers & companions in manifest.
old=json.loads((root/'coherence-complete-20261014.json').read_text());cons={'target_files':[]}
manifest=db(c.MANIFEST)
for path in [known,private,hp,sp,mp,cp,pp,bp]:
 si=source(path);rec=next((v for v in old['rows'] if v['fileID']==si['fileID']),None)
 item={'source':si,'prior_consistency':rec}
 blob=manifest.execute('SELECT file FROM Files WHERE fileID=?',(si['fileID'],)).fetchone()[0];ar=plistlib.loads(blob);mb=ar['$objects'][ar['$top']['root'].data];item['MBFile']={k:mb.get(k) for k in ['Size','Birth','LastModified','LastStatusChange']}
 item['manifest_companions']=rows(manifest,'SELECT fileID,relativePath FROM Files WHERE domain=? AND relativePath IN (?,?,?)',(si['domain'],si['relativePath']+'-wal',si['relativePath']+'-shm',si['relativePath']+'-journal'))
 with path.open('rb') as f:head=f.read(100)
 if head.startswith(b'SQLite format 3\x00'):
  page=struct.unpack('>H',head[16:18])[0] or 65536;page=65536 if page==1 else page
  item['sqlite_header']={'page_size':page,'write_version':head[18],'read_version':head[19],'change_counter':struct.unpack('>I',head[24:28])[0],'database_pages':struct.unpack('>I',head[28:32])[0],'freelist_pages':struct.unpack('>I',head[36:40])[0],'version_valid_for':struct.unpack('>I',head[92:96])[0],'sqlite_version':struct.unpack('>I',head[96:100])[0]}
  item['MBFile_minus_plaintext']=mb.get('Size',0)-path.stat().st_size
  item['delta_pages']=(mb.get('Size',0)-path.stat().st_size)/page
 cons['target_files'].append(item)
cons['mismatch_extensions']=dict(collections.Counter(Path(v['relativePath']).suffix for v in old['rows'] if v['manifest_size']!=v['plaintext_size']))
cons['mismatch_signs']=dict(collections.Counter('MBFile_larger' if v['manifest_size']>v['plaintext_size'] else 'MBFile_smaller' for v in old['rows'] if v['manifest_size']!=v['plaintext_size']))
lib=Path('telephones/scripts/.venv-iphone/lib/python3.14/site-packages/iphone_backup_decrypt')
cons['library_files']=[{'path':str(lib/n),'sha256':c.sha(lib/n)} for n in ['utils.py','iphone_backup.py']]
save('backup-details.json',cons)
# Existing targeted chronologies: selected corroborating events, values limited to dates/scalars.
with (root/'chronologie-complete-20261014/chronology-evidence.csv').open() as f:
 for v in csv.DictReader(f):
  if v['central_window']!='True' or not any(k in v['relativePath'] for k in ['commcenter.data.archive','BKAgentService','iBooks','WidgetKitExtension-2024-10-28','mobileslideshow','__access_time__']):continue
  # Skip uncertain epoch candidates except explicit plist/ISO or validated access_time.
  if v['time_format'] not in ['serialized plist date interpreted as UTC','ISO8601_explicit_offset'] and '__access_time__' not in v['relativePath']:continue
  path=Path(v['file']);ss=source(path)
  events.append({k:v.get(k,'') for k in ['domain','relativePath','fileID','sha256','locator','raw_value','time_format','utc','paris','interval_end_utc','observation','interpretation','confidence']})
# Existing MBFile events specifically thumbnail/panel/Xiaomi configuration; include as metadata.
with (root/'metadata-complete-central.csv').open() as f:
 for v in csv.DictReader(f):
  if not any(k in v['relativePath'] for k in ['IMG_1773.MP4/LocalVideoKeyFrame.jpg','0000000432_2.51.0/main.jsbundle','AppConfig/561CB9034971AB05FF2B2BBC88056031']):continue
  events.append(dict(domain=v['domain'],relativePath=v['relativePath'],fileID=v['fileID'],sha256='',locator='MBFile.'+v['field'],raw_value=v['raw_value'],time_format='unix',utc=time(int(v['raw_value']),'unix').isoformat(),paris=v['paris'],interval_end_utc='',observation='métadonnée MBFile',interpretation='date de fichier; déclencheur applicatif non établi',confidence='champ vérifié; acquisition tardive'))
# Before/after ensures all target plaintext sources remained identical.
for path,info in used.items():info['sha256_after']=c.sha(path);info['unchanged_during_run']=info['sha256_after']==info['sha256_now']
save('source-verification.json',list(used.values()))
c.write_csv(out/'timeline-correlated.csv',sorted(events,key=lambda v:v['utc']),list(events[0]))
save('operations.json',{'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'script':str(Path(__file__)),'script_sha256':c.sha(__file__),'prior_results_parsed':len(review),'target_sources_verified':len(used),'timeline_fields':len(events),'sqlite_mode':'ro&immutable=1; no WAL replay; companions checked against manifest','new_decryption':False,'secret_export':False,'limits':['Health measurements never queried','No network identifiers or communications exported','Dates are observations, not persons or foreground events']})
print(json.dumps({'output':str(out),'sources':len(used),'events':len(events),'reviewed_results':len(review)}))
