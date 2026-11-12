#!/usr/bin/env python3
"""Additional targeted correlations in existing TP-02 extractions. No source writes."""
import argparse,collections,csv,datetime as dt,hashlib,json,os,plistlib,re,struct,uuid
os.umask(0o077)
from pathlib import Path
import tp02_forensic as c
p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args();out=Path(a.out);root=Path('telephones/recherche-TP-02')
def save(n,v):
 with (out/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2,default=str);f.write('\n')
def db(path):x=c.ro(path);x.row_factory=__import__('sqlite3').Row;return x
def rows(db,q,args=()):return [dict(v) for v in db.execute(q,args)]
pp=root/'extraction-complements-20261014/files/CameraRollDomain/Media/PhotoData/Photos.sqlite';ph=db(pp);before=c.sha(pp)
lo=c.START.timestamp()-978307200;hi=c.END.timestamp()-978307200
trans=rows(ph,'''SELECT t.Z_PK,t.ZTIMESTAMP,a.ZNAME author,b.ZNAME bundle,n.ZNAME context,ps.ZNAME process FROM ATRANSACTION t LEFT JOIN ATRANSACTIONSTRING a ON a.Z_PK=t.ZAUTHORTS LEFT JOIN ATRANSACTIONSTRING b ON b.Z_PK=t.ZBUNDLEIDTS LEFT JOIN ATRANSACTIONSTRING n ON n.Z_PK=t.ZCONTEXTNAMETS LEFT JOIN ATRANSACTIONSTRING ps ON ps.Z_PK=t.ZPROCESSIDTS WHERE t.ZTIMESTAMP BETWEEN ? AND ? ORDER BY t.ZTIMESTAMP''',(lo,hi))
for v in trans:
 d=dt.datetime.fromtimestamp(v['ZTIMESTAMP']+978307200,dt.timezone.utc);v['utc']=d.isoformat();v['paris']=d.astimezone(c.PARIS).isoformat()
 v['changes']=rows(ph,'''SELECT ch.Z_PK,ch.ZCHANGETYPE,ch.ZENTITY,ch.ZENTITYPK,pk.Z_NAME entity_name,hex(ch.ZCOLUMNS) columns_bitmask FROM ACHANGE ch LEFT JOIN Z_PRIMARYKEY pk ON pk.Z_ENT=ch.ZENTITY WHERE ch.ZTRANSACTIONID=?''',(v['Z_PK'],))
# Migration identity comparison only; do not export raw device identifiers.
healthdb=next((root/'extraction-systeme-20261014/files').rglob('healthdb.sqlite'));h=db(healthdb)
identities=rows(h,'SELECT ROWID,hardware_identifier,database_identifier FROM sync_identities')
migrations=rows(ph,'SELECT Z_PK,ZMIGRATIONDATE,ZHARDWAREMODEL,ZOSVERSION,ZCPLENABLED,ZMIGRATIONTYPE,ZORIGIN,ZINITIALSYNCDATE,ZDEVICEUNIQUEID FROM ZMIGRATIONHISTORY')
for v in migrations:
 raw=v.pop('ZDEVICEUNIQUEID');v['device_id_present']=bool(raw);v['device_id_sha256']=hashlib.sha256(str(raw).encode()).hexdigest() if raw else None
 v['matches_health_hardware_identity']=[]
 if raw:
  try:b=uuid.UUID(raw).bytes
  except (ValueError,AttributeError):b=b''
  v['matches_health_hardware_identity']=[x['ROWID'] for x in identities if b and x['hardware_identifier'] in [b,b[::-1]]]
 v['utc']=dt.datetime.fromtimestamp(v['ZMIGRATIONDATE']+978307200,dt.timezone.utc).isoformat()
 v['paris']=dt.datetime.fromisoformat(v['utc']).astimezone(c.PARIS).isoformat()
photo={'source_sha256':before,'transactions':trans,'migration_rows':migrations,'transaction_day_counts':dict(collections.Counter(v['paris'][:10] for v in trans)),'oct28_context_counts':dict(collections.Counter(v['context'] for v in trans if v['paris'].startswith('2024-10-28'))),'source_sha256_after':c.sha(pp)}
photo['asset23769_lifecycle']=rows(ph,'''SELECT t.Z_PK,t.ZTIMESTAMP,ch.ZCHANGETYPE,n.ZNAME context FROM ACHANGE ch JOIN ATRANSACTION t ON t.Z_PK=ch.ZTRANSACTIONID LEFT JOIN ATRANSACTIONSTRING n ON n.Z_PK=t.ZCONTEXTNAMETS WHERE ch.ZENTITY=3 AND ch.ZENTITYPK=23769 ORDER BY t.ZTIMESTAMP''')
photo['asset23769_current_count']=ph.execute('SELECT count(*) FROM ZASSET WHERE Z_PK=23769').fetchone()[0]
for v in photo['asset23769_lifecycle']:
 v['utc']=dt.datetime.fromtimestamp(v['ZTIMESTAMP']+978307200,dt.timezone.utc).isoformat()
 v['paris']=dt.datetime.fromisoformat(v['utc']).astimezone(c.PARIS).isoformat()
save('photos-transaction-correlations.json',photo)
# Correlate Health identity (binary, UUID text and hashes) against previously extracted small plists only.
needles=[]
for x in identities:
 if any(x['hardware_identifier']):
  b=x['hardware_identifier'];needles.extend([b,str(uuid.UUID(bytes=b)).encode(),str(uuid.UUID(bytes=b)).upper().encode()])
hits=[];checked=0
for folder in root.glob('extraction-*'):
 for f in (folder/'files').rglob('*.plist'):
  if f.stat().st_size>8*1024**2:continue
  checked+=1;data=f.read_bytes()
  if any(n in data for n in needles):hits.append({'file':str(f),'sha256':c.sha(f)})
healthd=root/'extraction-complements-20261014/files/HomeDomain/Library/Preferences/com.apple.healthd.plist'
hd=plistlib.loads(healthd.read_bytes());identity_binding={'path':str(healthd),'sha256':c.sha(healthd),'key':'SyncIdentityHardwareIdentifier','matches_sync_identity_rows':[x['ROWID'] for x in identities if x['hardware_identifier']==hd.get('SyncIdentityHardwareIdentifier')]}
save('health-identity-crosschecks.json',{'healthd_binding':identity_binding,'checked_plists':checked,'hits':hits,'migration_matches':[{'Z_PK':v['Z_PK'],'matches':v['matches_health_hardware_identity']} for v in migrations],'limit':'literal representations only; absence does not exclude hashed, encoded or unextracted linkage'})
# Test input context candidate hashes across all retained chat/handle identifiers; output locations only.
mp=next((root/'extraction-systeme-20261014/files').rglob('sms.db'));m=db(mp);target='22855b35cec236c76d0d2911c2b4437e1171dff';matches=[];attempts=0
for tab,cols in [('chat',['chat_identifier','guid','group_id','original_group_id']),('handle',['id','uncanonicalized_id'])]:
 for col in cols:
  for v in m.execute('SELECT ROWID,'+col+' FROM '+tab+' WHERE '+col+' IS NOT NULL'):
   for enc in ['utf-8','utf-16le']:
    attempts+=1
    if hashlib.sha1(str(v[1]).encode(enc)).hexdigest()==target:matches.append({'table':tab,'column':col,'rowid':v[0],'encoding':enc})
save('input-context-linkage-test.json',{'target_context_suffix':target,'hash_candidates_tested':attempts,'matches':matches,'unjoined_central_SMS_rowids':[v[0] for v in m.execute('SELECT m.ROWID FROM message m LEFT JOIN chat_message_join j ON j.message_id=m.ROWID WHERE m.ROWID BETWEEN 74688 AND 74690 AND j.chat_id IS NULL')],'limit':'tested SHA1 forms only, no validated Apple identifier derivation; no assertion that the context belongs to these SMS'})
# OP-01 existing textual results: exact literal search; no extraction or raw registry dump.
network=root/'extraction-systeme-20261014/files/SystemPreferencesDomain/com.apple.wifi.known-networks.plist';kn=plistlib.loads(network.read_bytes())['wifi.network.ssid.ASUS_Z01RD'];macs=[v['BSSID'] for v in kn['BSSList']]
patterns=[b'ASUS_Z01RD']+[v.encode() for v in macs];ophits=[];opfiles=[]
for f in Path('ordinateur').rglob('*'):
 if not f.is_file() or f.suffix not in ['.md','.txt','.xml','.json','.jsonl','.csv'] or f.stat().st_size>64*1024**2:continue
 data=f.read_bytes();opfiles.append({'path':str(f),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 found=[n for n,v in enumerate(patterns) if v.lower() in data.lower()]
 if found:ophits.append({'path':str(f),'needle_indices':found})
save('op01-network-comparison.json',{'files_read':opfiles,'hits':ophits,'limits':['existing textual exports <=64 MiB only','binary EVTX, hives, disk image not newly parsed','no network identifier in this output','same SSID would not prove AP ownership']})
# Distribution of SQLite headers for existing confirmed databases (no integrity rescan).
with (root/'resultats-finaux-20261014/sqlite-confirmed.csv').open() as f:confirmed=list(csv.DictReader(f))
headers=[]
for v in confirmed:
 path=Path(v['file'])
 with path.open('rb') as f:b=f.read(100)
 headers.append({'fileID':v.get('fileID'),'change_counter':int.from_bytes(b[24:28],'big'),'freelist_pages':int.from_bytes(b[36:40],'big'),'version_valid_for':int.from_bytes(b[92:96],'big'),'sqlite_version':int.from_bytes(b[96:100],'big')})
save('sqlite-header-patterns.json',{'headers':headers,'pattern_counts':dict(collections.Counter(str((v['change_counter'],v['freelist_pages'],v['version_valid_for'],v['sqlite_version'])) for v in headers)),'limit':'common header is compatible with backup rewriting; not proof of exact API or loss of rows'})
# Append transaction observations to timeline, preserving raw Apple seconds, exact transaction/change references.
with (out/'timeline-correlated.csv').open() as f:rd=csv.DictReader(f);fields=rd.fieldnames;timeline=list(rd)
src=next(v for v in json.loads((out/'source-verification.json').read_text()) if v['relativePath']=='Media/PhotoData/Photos.sqlite')
for v in trans:
 timeline.append(dict(domain=src['domain'],relativePath=src['relativePath'],fileID=src['fileID'],sha256=before,locator=f"ATRANSACTION.Z_PK={v['Z_PK']} -> ATRANSACTIONSTRING; changes="+','.join(str(x['Z_PK']) for x in v['changes']),raw_value=v['ZTIMESTAMP'],time_format='apple',utc=v['utc'],paris=v['paris'],interval_end_utc='',observation='transaction Photos: '+str(v['context']),interpretation='contexte interne conservé; peut être hérité par restauration; requête Photos distincte de visionnage',confidence='jointures et champ vérifiés; contexte conservé'))
# Explicit procedural declarations and previously extracted Unix-key context; no identity values exported.
mail=Path('docs/mail.txt')
for iso,obs in [('2024-10-15T13:30:00+02:00','perte d’accès déclarée'),('2024-10-28T10:22:00+01:00','début d’ouverture déclaré'),('2024-10-28T19:20:00+01:00','restitution déclarée')]:
 d=dt.datetime.fromisoformat(iso);timeline.append(dict(domain='document client',relativePath=str(mail),fileID='',sha256=c.sha(mail),locator='chronologie déclarée du mail',raw_value=iso,time_format='Europe/Paris déclaration approximative',utc=d.astimezone(dt.timezone.utc).isoformat(),paris=iso,interval_end_utc='',observation=obs,interpretation='horaire approximatif; procès-verbal à vérifier',confidence='déclaration'))
extra=[]
for folder in root.glob('extraction-*'):
 for path in (folder/'files').rglob('*.plist'):
  if 'book' not in path.name.lower() and 'BKAgent' not in path.name and path.name!='com.apple.commcenter.data.archive.plist':continue
  try:obj=plistlib.loads(path.read_bytes())
  except Exception:continue
  vals=[]
  if obj.get('CKStartupTime')==1730111967:vals.append(('CKStartupTime',1730111967))
  if path.name=='com.apple.commcenter.data.archive.plist':
   def walk(v,k=''):
    if isinstance(v,dict):
     for key,x in v.items():walk(x,k+'/'+key)
    elif k.endswith('/from_dated') and v==1729178133:vals.append(('label-remap-history/[identifiant masqué]/from_dated',v))
   walk(obj)
  for loc,raw in vals:
   rec=next(json.loads(l) for l in (folder/'extraction.jsonl').read_text().splitlines() if json.loads(l).get('output')==str(path.resolve()))
   d=dt.datetime.fromtimestamp(raw,dt.timezone.utc);event=dict(domain=rec['domain'],relativePath=rec['relativePath'],fileID=rec['fileID'],sha256=c.sha(path),locator=loc,raw_value=raw,time_format='unix',utc=d.isoformat(),paris=d.astimezone(c.PARIS).isoformat(),interval_end_utc='',observation='état de préférence '+loc,interpretation='traitement automatique possible; pas un démarrage système établi',confidence='champ vérifié')
   timeline.append(event);extra.append(event)
save('additional-preference-events.json',extra)
# Recheck extra inputs against extraction log, including source objects, without decrypting again.
extra_sources=[]
for path in [healthd]+[Path(next(json.loads(l)['output'] for fold in root.glob('extraction-*') for l in (fold/'extraction.jsonl').read_text().splitlines() if json.loads(l).get('fileID')==e['fileID'])) for e in extra]:
 rec=next(json.loads(l) for fold in root.glob('extraction-*') for l in (fold/'extraction.jsonl').read_text().splitlines() if json.loads(l).get('output')==str(path.resolve()))
 fid=rec['fileID'];cipher=c.BACKUP/fid[:2]/fid;actual=c.sha(path);ch=c.sha(cipher)
 extra_sources.append(dict(fileID=fid,relativePath=rec['relativePath'],sha256=actual,plaintext_matches=actual==rec['sha256'],ciphertext_sha256=ch,ciphertext_matches=ch==rec['ciphertext_sha256']))
save('additional-source-verification.json',extra_sources)
manifest_hash=c.sha(c.MANIFEST)
for event in timeline:
 event['hash_scope']='artefact déchiffré ou document'
 if event['locator'].startswith('MBFile.'):
  event['sha256']=manifest_hash;event['hash_scope']='Manifest-decrypted.db; fileID désigne objet référencé'
 d=dt.datetime.fromisoformat(event['utc']);event['central_window']=str(c.START<=d<=c.END)
 event['procedural_phase']='avant ouverture déclarée' if d<dt.datetime(2024,10,28,9,22,tzinfo=dt.timezone.utc) else 'après ouverture déclarée'
 if d>c.END:event['procedural_phase']='après restitution déclarée'
 if d<c.START:event['procedural_phase']='avant perte d’accès déclarée'
fields+=['hash_scope','central_window','procedural_phase']
c.write_csv(out/'timeline-correlated.csv',sorted(timeline,key=lambda v:v['utc']),fields)
save('correlation-operations.json',{'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'script_sha256':c.sha(__file__),'transactions':len(trans),'timeline_rows':len(timeline),'photo_unchanged':before==c.sha(pp),'input_context_hash_tests':attempts,'OP01_text_files':len(opfiles),'new_decryption':False})
print(json.dumps({'transactions':len(trans),'OP01_text_files':len(opfiles),'OP01_hits':len(ophits),'health_identity_hits':len(hits),'timeline_rows':len(timeline)}))
