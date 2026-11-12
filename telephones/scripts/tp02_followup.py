#!/usr/bin/env python3
"""Extended TP-02 read-only examination: Photos, Health provenance, Wi-Fi and call context."""
import argparse
import collections
import datetime as dt
import json
import os
from pathlib import Path
import plistlib
import sqlite3
import tp02_forensic as common

p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',default='telephones/recherche-TP-02');p.add_argument('--out',required=True)
a=p.parse_args();os.umask(0o077);root=Path(a.root);out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
photos=root/'extraction-complements-20261014/files/CameraRollDomain/Media/PhotoData/Photos.sqlite'
fields=['ZDATECREATED','ZADDEDDATE','ZMODIFICATIONDATE','ZTRASHEDDATE','ZADJUSTMENTTIMESTAMP','ZANALYSISSTATEMODIFICATIONDATE']
lo=common.START.timestamp()-978307200;hi=common.END.timestamp()-978307200
rows=[];stats={};asset_records=[]
with common.ro(photos) as c:
 stats['assets_total']=c.execute('SELECT COUNT(*) FROM ZASSET').fetchone()[0]
 stats['quick_check']=c.execute('PRAGMA quick_check').fetchall()
 sha=common.sha(photos)
 for field in fields:
  query='SELECT Z_PK,ZFILENAME,ZDIRECTORY,'+field+',ZTRASHEDSTATE FROM ZASSET WHERE '+field+' BETWEEN ? AND ? ORDER BY '+field
  data=c.execute(query,(lo,hi)).fetchall();stats[field]=len(data)
  for pk,name,directory,raw,state in data:
   date=dt.datetime.fromtimestamp(raw+978307200,dt.timezone.utc)
   rows.append({'file':str(photos),'sha256':sha,'locator':f'ZASSET.Z_PK={pk}.{field}','raw_value':raw,
     'time_format':'Apple/Cocoa seconds','utc':date.isoformat(),'paris':date.astimezone(common.PARIS).isoformat(),
     'filename':name,'directory':directory,'state_raw':state,'interpretation':'photolibrary field; sync/import/automatic processing possible, no local human attribution'})
 lastviews=c.execute('SELECT a.Z_PK,a.ZFILENAME,a.ZDIRECTORY,aa.ZLASTVIEWEDDATE,a.ZTRASHEDSTATE FROM ZASSET a JOIN ZADDITIONALASSETATTRIBUTES aa ON aa.Z_PK=a.ZADDITIONALATTRIBUTES WHERE aa.ZLASTVIEWEDDATE BETWEEN ? AND ? ORDER BY aa.ZLASTVIEWEDDATE',(lo,hi)).fetchall()
 stats['ZLASTVIEWEDDATE']=len(lastviews)
 for pk,name,directory,raw,state in lastviews:
  date=dt.datetime.fromtimestamp(raw+978307200,dt.timezone.utc)
  rows.append({'file':str(photos),'sha256':sha,'locator':f'ZASSET.Z_PK={pk}->ZADDITIONALASSETATTRIBUTES.ZLASTVIEWEDDATE','raw_value':raw,
   'time_format':'Apple/Cocoa seconds','utc':date.isoformat(),'paris':date.astimezone(common.PARIS).isoformat(),'filename':name,'directory':directory,
   'state_raw':state,'interpretation':'last-view field retained in photolibrary; origin and update semantics not validated'})
 data=c.execute('''SELECT a.Z_PK,a.ZFILENAME,a.ZDIRECTORY,a.ZUUID,a.ZDATECREATED,a.ZADDEDDATE,
 aa.ZORIGINALFILENAME,aa.ZIMPORTEDBYBUNDLEIDENTIFIER,aa.ZIMPORTEDBYDISPLAYNAME,aa.ZEXIFTIMESTAMPSTRING,
 a.ZCLOUDASSETGUID IS NOT NULL,a.ZCLOUDLOCALSTATE,aa.ZCAMERACAPTUREDEVICE
 FROM ZASSET a LEFT JOIN ZADDITIONALASSETATTRIBUTES aa ON aa.Z_PK=a.ZADDITIONALATTRIBUTES
 WHERE a.ZDATECREATED BETWEEN ? AND ?''',(lo,hi)).fetchall()
 names=['Z_PK','filename','directory','uuid','created_raw','added_raw','original_filename','import_bundle','import_display','exif_timestamp_raw','cloud_guid_present','cloud_local_state_raw','camera_capture_device_raw']
 asset_records=[dict(zip(names,r)) for r in data]
 stats['import_bundles']=dict(collections.Counter(str(r['import_bundle']) for r in asset_records))
 stats['created_day_counts']=dict(collections.Counter(dt.datetime.fromtimestamp(r['created_raw']+978307200,dt.timezone.utc).astimezone(common.PARIS).date().isoformat() for r in asset_records))
 stats['modification_minute_clusters']=dict(collections.Counter(r['paris'][:16]+r['paris'][-6:] for r in rows if r['locator'].endswith('.ZMODIFICATIONDATE')).most_common(10))
 stats['lastview_day_counts']=dict(collections.Counter(r['paris'][:10] for r in rows if r['locator'].endswith('.ZLASTVIEWEDDATE')))
 stats['video_thumbnail_context']=c.execute("SELECT a.Z_PK,a.ZDATECREATED,a.ZADDEDDATE,a.ZMODIFICATIONDATE,aa.ZLASTVIEWEDDATE,aa.ZIMPORTEDBYBUNDLEIDENTIFIER FROM ZASSET a LEFT JOIN ZADDITIONALASSETATTRIBUTES aa ON aa.Z_PK=a.ZADDITIONALATTRIBUTES WHERE a.ZFILENAME='IMG_1773.MP4'").fetchall()
common.write_csv(out/'photos-date-fields.csv',sorted(rows,key=lambda r:r['utc']),list(rows[0]))
common.write_csv(out/'photos-assets-created-central.csv',asset_records,names)
(out/'photos-summary.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
# Health source metadata only, no quantities/medical measurements exported.
secure=next((root/'extraction-systeme-20261014/files').rglob('healthdb_secure.sqlite'))
health=next((root/'extraction-systeme-20261014/files').rglob('healthdb.sqlite'))
healthrows=[]
with common.ro(secure) as c,common.ro(health) as h:
 query='''SELECT s.data_id,s.start_date,s.end_date,s.data_type,o.creation_date,p.origin_product_type,p.local_product_type,p.sync_provenance,p.source_id,p.device_id,p.tz_name
 FROM samples s JOIN objects o ON o.data_id=s.data_id JOIN data_provenances p ON p.ROWID=o.provenance
 WHERE s.start_date BETWEEN ? AND ? ORDER BY s.start_date'''
 for r in c.execute(query,(lo,hi)):
  record=dict(zip(['data_id','start_raw','end_raw','data_type_raw','creation_raw','origin_product_type','local_product_type','sync_provenance_raw','source_id','device_id','tz_name'],r))
  source=h.execute('SELECT local_device,product_type FROM sources WHERE ROWID=?',(record['source_id'],)).fetchone()
  device=h.execute('SELECT model,hardware,software,localIdentifier FROM source_devices WHERE ROWID=?',(record['device_id'],)).fetchone()
  record.update(source_local_device_raw=source[0] if source else None,source_product_type=source[1] if source else None,
   device_model=device[0] if device else None,device_hardware=device[1] if device else None,device_software=device[2] if device else None,
   device_identifier_present=bool(device[3]) if device else False,
   paris=dt.datetime.fromtimestamp(record['start_raw']+978307200,dt.timezone.utc).astimezone(common.PARIS).isoformat(),
   interpretation='source metadata compatible with matching phone model; no serial number or human interaction proved')
  healthrows.append(record)
common.write_csv(out/'health-provenance-central.csv',healthrows,list(healthrows[0]))
healthstats={'samples':len(healthrows),'days':dict(collections.Counter(r['paris'][:10] for r in healthrows)),
 'products':dict(collections.Counter(r['origin_product_type'] for r in healthrows)),
 'limits':'local/source/sync flags retained raw; same model is not a unique device identifier; automatic collection possible'}
(out/'health-summary.json').write_text(json.dumps(healthstats,ensure_ascii=False,indent=2)+'\n')
# Wi-Fi context limited to network identifiers and join dates, never passwords.
wifi=root/'extraction-systeme-20261014/files/SystemPreferencesDomain/com.apple.wifi.known-networks.plist'
private=root/'extraction-systeme-20261014/files/SystemPreferencesDomain/SystemConfiguration/com.apple.wifi-private-mac-networks.plist'
v=plistlib.loads(wifi.read_bytes());w=plistlib.loads(private.read_bytes())
key='wifi.network.ssid.ASUS_Z01RD';network=v[key]
context={'known_network_count':len(v),'known_source_sha256':common.sha(wifi),'private_source_sha256':common.sha(private),'network_key':key,
 'AddReason_raw':network.get('AddReason'),
 'known_dates':{k:str(network[k]) for k in ('AddedAt','JoinedByUserAt','JoinedBySystemAt','LastDiscoveredAt','UpdatedAt') if k in network},
 'private_entries':[],'limits':['SSID does not identify operator or physical access point','Snapshot fields are not a complete connection log','Configuration syncing/restoration and device clock not independently excluded']}
for index,r in enumerate(w.get('List of scanned networks with private mac',[])):
 if r.get('SSID_STR')=='ASUS_Z01RD':context['private_entries'].append({'list_index':index,'PresentInKnownNetworks':r.get('PresentInKnownNetworks'),
  'dates':{k:str(r[k]) for k in ('addedAt','lastJoined','MacGenerationTimeStamp','FirstJoinWithNewMacTimestamp') if k in r}})
(out/'wifi-corroboration.json').write_text(json.dumps(context,ensure_ascii=False,indent=2)+'\n')
# Call source fields: publish missingness and distribution only, no participant identifiers.
calls=next((root/'extraction-systeme-20261014/files').rglob('CallHistory.storedata'))
with common.ro(calls) as c:
 records=c.execute('SELECT ZDATE,ZLOCALPARTICIPANTUUID IS NOT NULL,ZOUTGOINGLOCALPARTICIPANTUUID IS NOT NULL,ZINITIATOR IS NOT NULL,ZSERVICE_PROVIDER,ZORIGINATED,ZANSWERED FROM ZCALLRECORD WHERE ZDATE BETWEEN ? AND ?',(lo,hi)).fetchall()
 callstats={'central_records':len(records),'day_counts':dict(collections.Counter(dt.datetime.fromtimestamp(r[0]+978307200,dt.timezone.utc).astimezone(common.PARIS).date().isoformat() for r in records)),
 'service_provider_counts':dict(collections.Counter(str(r[4]) for r in records)),'ZORIGINATED_raw_counts':dict(collections.Counter(str(r[5]) for r in records)),
 'localparticipant_uuid_present':sum(r[1] for r in records),'outgoinglocalparticipant_uuid_present':sum(r[2] for r in records),'initiator_present':sum(r[3] for r in records),
 'limits':'participant UUID fields not established as originating hardware identifiers; no operator attribution or serial-number binding'}
(out/'calls-origin-assessment.json').write_text(json.dumps(callstats,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'photo_date_fields':len(rows),'assets_created_central':len(asset_records),'health_samples':len(healthrows),'calls':len(records)}))
