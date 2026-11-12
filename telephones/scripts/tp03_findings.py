#!/usr/bin/env python3
"""Explicit native queries and provenance assessment on decrypted TP-03 copies."""
import collections,datetime as dt,hashlib,json,pathlib,plistlib,sqlite3,sys
from zoneinfo import ZoneInfo
from tp01_inventory import dump,sha
P=ZoneInfo('Europe/Paris');C=978307200
START=dt.datetime(2024,10,15,13,30,tzinfo=P).timestamp();END=dt.datetime(2024,10,28,19,20,tzinfo=P).timestamp()
def iso(v,scale=1):
 if not v:return None
 return dt.datetime.fromtimestamp(v/scale+C,dt.timezone.utc).astimezone(P).isoformat()
def main():
 root=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);out.mkdir(exist_ok=False)
 sources=[];errors=[]
 def query(rel,sql,args=()):
  p=root/'files'/rel
  try:
   before=sha(p);c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
   r=[dict(x) for x in c.execute(sql,args)];c.close();after=sha(p)
   sources.append({'path':str(p),'before':before,'after':after,'sql':sql,'parameters':args})
   return r
  except Exception as e:errors.append({'path':str(p),'error':str(e),'sql':sql});return []
 sm='HomeDomain/Library/SMS/sms.db';sms=query(sm,'select count(*) total,min(date) first,max(date) last from message')
 central=query(sm,'select ROWID,date,date_read,date_delivered,is_from_me,is_read,service,ck_sync_state from message where date between ? and ? or date_read between ? and ? or date_delivered between ? and ?',tuple([(START-C)*1e9,(END-C)*1e9]*3))
 dump(out/'sms.json',{'range':sms,'central':central})
 ca='HomeDomain/Library/CallHistoryDB/CallHistory.storedata';calls=query(ca,'select count(*) total,min(ZDATE) first,max(ZDATE) last from ZCALLRECORD')
 cr=query(ca,'select Z_PK,ZDATE,ZORIGINATED,ZANSWERED,ZDURATION,ZUNIQUE_ID from ZCALLRECORD where ZDATE between ? and ?',(START-C,END-C))
 dump(out/'calls.json',{'range':calls,'central':cr})
 hs='HealthDomain/Health/healthdb_secure.sqlite';h='HealthDomain/Health/healthdb.sqlite'
 hr=query(hs,'select s.data_id,s.data_type,s.start_date,s.end_date,o.creation_date,o.provenance from samples s join objects o using(data_id) where o.creation_date between ? and ? or s.start_date between ? and ? order by o.creation_date',(START-C,END-C,START-C,END-C))
 for x in hr:
  for field in ['start_date','end_date','creation_date']:x[field+'_paris']=iso(x[field])
 prov=[r for i in sorted({x['provenance'] for x in hr}) for r in query(hs,'select * from data_provenances where ROWID=?',(i,))]
 src=[r for i in sorted({x['source_id'] for x in prov}) for r in query(h,'select ROWID,local_device,product_type,sync_identity,deleted from sources where ROWID=?',(i,))]
 dev=[r for i in sorted({x['device_id'] for x in prov}) for r in query(h,'select ROWID,hardware,software,creation_date,sync_provenance,sync_identity,length(localIdentifier) identifier_length from source_devices where ROWID=?',(i,))]
 identities=query(h,'select ROWID,hex(hardware_identifier) hardware_hex,hex(database_identifier) database_hex from sync_identities')
 dump(out/'health.json',{'samples':hr,'provenances':prov,'sources':src,'devices':dev,'identities':identities})
 ph='CameraRollDomain/Media/PhotoData/Photos.sqlite';photo={}
 for field in ['ZDATECREATED','ZADDEDDATE','ZMODIFICATIONDATE','ZADJUSTMENTTIMESTAMP','ZTRASHEDDATE','ZLASTSHAREDDATE']:
  photo[field]=query(ph,'select count(*) count from ZASSET where '+field+' between ? and ?',(START-C,END-C))
 photo['total']=query(ph,'select count(*) count from ZASSET')
 photo['migration_schema']=query(ph,"select sql from sqlite_master where name='ZMIGRATIONHISTORY'")
 photo['migrations']=query(ph,'select Z_PK,ZMIGRATIONDATE,ZDEVICEUNIQUEID,ZSTOREUUID,ZHARDWAREMODEL,ZOSVERSION from ZMIGRATIONHISTORY')
 photo['transactions']=query(ph,'select Z_PK,ZTIMESTAMP,ZAUTHOR,ZBUNDLEID,ZCONTEXTNAME,ZPROCESSID from ATRANSACTION where ZTIMESTAMP between ? and ?',(START-C,END-C))
 dump(out/'photos.json',photo)
 pref=[]
 for p in (root/'files').rglob('*.plist'):
  try:
   d=plistlib.loads(p.read_bytes());rel=str(p.relative_to(root/'files'))
   # Retain only datetime fields and date-labelled scalar candidates centrally.
   def walk(v,key):
    if isinstance(v,dict):
     for k,x in v.items():walk(x,key+'/'+str(k))
    elif isinstance(v,list):
     for i,x in enumerate(v):walk(x,key+'/'+str(i))
    elif isinstance(v,dt.datetime):
     t=v.replace(tzinfo=dt.timezone.utc).timestamp()
     if START<=t<=END:pref.append({'path':rel,'key':key,'raw_utc':str(v),'paris':dt.datetime.fromtimestamp(t,dt.timezone.utc).astimezone(P).isoformat()})
   walk(d,'')
  except Exception:pass
 dump(out/'plist-dates.json',pref);dump(out/'queries-sources.json',sources);dump(out/'errors.json',errors)
 print(json.dumps({'health_rows':len(hr),'sms_central':len(central),'calls_central':len(cr),'errors':len(errors)}))
if __name__=='__main__':main()
