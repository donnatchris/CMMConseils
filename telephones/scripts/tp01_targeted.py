#!/usr/bin/env python3
"""Validated queries, plist dates and provenance checks; no communication bodies."""
import datetime as dt, json, pathlib, plistlib, sqlite3, sys, collections
from zoneinfo import ZoneInfo
from tp01_inventory import dump, sha
P=ZoneInfo('Europe/Paris'); C=978307200
def iso(v,offset=0,scale=1):
    if not v:return None
    try:return dt.datetime.fromtimestamp(v/scale+offset,dt.timezone.utc).astimezone(P).isoformat()
    except (ValueError,OverflowError,OSError):return None
def main():
 root=pathlib.Path(sys.argv[1]);out=root/'targeted';out.mkdir(exist_ok=False)
 def db(rel):
  c=sqlite3.connect((root/'files'/rel).as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row;return c
 def query(rel,sql,params=()):
  with db(rel) as c:return [dict(x) for x in c.execute(sql,params)]
 start=dt.datetime(2024,10,15,13,30,tzinfo=P).timestamp();op=dt.datetime(2024,10,28,11,30,tzinfo=P).timestamp();end=dt.datetime(2024,10,28,19,20,tzinfo=P).timestamp()
 sms='HomeDomain/Library/SMS/sms.db';r=query(sms,'select ROWID,date,date_read,date_delivered,date_played,is_from_me,is_read,is_sent,service,ck_sync_state from message order by date')
 dump(out/'sms.json',{'total':len(r),'central':[x for x in r if any(start<=x[k]/1e9+C<=end for k in ['date','date_read','date_delivered','date_played'] if x[k])],'last_before':max((dict(x,paris=iso(x['date'],C,1e9)) for x in r if x['date']/1e9+C<start),key=lambda x:x['date'],default=None),'first_after':min((dict(x,paris=iso(x['date'],C,1e9)) for x in r if x['date']/1e9+C>end),key=lambda x:x['date'],default=None)})
 wa={}
 for tag in ['WhatsApp','WhatsAppSMB']:
  rel=f'AppDomainGroup-group.net.whatsapp.{tag}.shared/ChatStorage.sqlite'
  r=query(rel,'select Z_PK,ZMESSAGEDATE,ZSENTDATE,ZISFROMME,ZMESSAGETYPE,ZMESSAGESTATUS from ZWAMESSAGE where (ZMESSAGEDATE between ? and ?) or (ZSENTDATE between ? and ?) order by ZMESSAGEDATE',(start-C,end-C,start-C,end-C))
  for x in r:x.update(message_paris=iso(x['ZMESSAGEDATE'],C),sent_paris=iso(x['ZSENTDATE'],C))
  wa[tag]=r
 dump(out/'whatsapp.json',wa)
 photo='CameraRollDomain/Media/PhotoData/Photos.sqlite'
 fields=['ZDATECREATED','ZADDEDDATE','ZMODIFICATIONDATE','ZADJUSTMENTTIMESTAMP','ZTRASHEDDATE','ZLASTSHAREDDATE']
 ph={}
 for f in fields:
  r=query(photo,f'select count(*) as total,min({f}) as min,max({f}) as max from ZASSET');r[0].update(min_paris=iso(r[0]['min'],C),max_paris=iso(r[0]['max'],C))
  ph[f]={'range':r,'central':query(photo,f'select Z_PK,{f},ZDIRECTORY,ZFILENAME,ZCLOUDASSETGUID from ZASSET where {f} between ? and ?',(start-C,end-C))}
 dump(out/'photos.json',ph)
 vm='HomeDomain/Library/Voicemail/voicemail.db'
 dump(out/'voicemail-schema.json',query(vm,"select name,sql from sqlite_master where type='table'"))
 dump(out/'voicemail-dates.json',query(vm,'select rowid,date from deleted where date between ? and ? order by date',(start,end)))
 tcc='HomeDomain/Library/TCC/TCC.db';dump(out/'tcc.json',query(tcc,'select service,client,auth_value,auth_reason,last_modified from access where last_modified between ? and ? order by last_modified',(start,end)))
 for part in ['client','server']:
  rel=f'HomeDomain/Library/Application Support/CloudDocs/session/db/{part}.db';table=part+'_items'
  with db(rel) as c:
   cols=[r[1] for r in c.execute('pragma table_info('+table+')')]
   keep=[x for x in cols if any(t in x for t in ['time','device','download','local','name','item_id','parent_id'])]
   sql='select '+','.join('"'+x+'"' for x in keep)+' from '+table+' where item_lastusedtime between ? and ? or item_birthtime between ? and ?'
   dump(out/f'clouddocs-{part}.json',[dict(x) for x in c.execute(sql,(start,end,start,end))])
 inv=json.loads((root/'inventory.json').read_text());dated=[];states=[]
 def walk(v,path,logical):
  if isinstance(v,dict):
   for k,x in v.items():walk(x,path+'/'+str(k),logical)
  elif isinstance(v,list):
   for i,x in enumerate(v):walk(x,path+'/'+str(i),logical)
  elif isinstance(v,dt.datetime):
   t=v.replace(tzinfo=dt.timezone.utc).timestamp()
   if start<=t<=end:dated.append({'path':logical,'key':path,'raw':str(v),'format':'plist UTC datetime','paris':iso(t)})
  elif isinstance(v,(float,int)) and not isinstance(v,bool) and any(s in path.lower() for s in ['date','time','added','last','first']):
   for label,offset,scale in [('unix_s',0,1),('cocoa_s',C,1),('unix_ms',0,1000)]:
    if start<=v/scale+offset<=end:dated.append({'path':logical,'key':path,'raw':v,'format_hypothesis':label,'paris':iso(v,offset,scale)})
 for p in (root/'files').rglob('*.plist'):
  try:
   d=plistlib.loads(p.read_bytes());logical=str(p.relative_to(root/'files'));walk(d,'',logical)
   if 'wifi-networks' in p.name or 'ProfileTruth' in p.name:states.append({'path':logical,'type':type(d).__name__,'length':len(d),'sha256':sha(p)})
  except Exception:pass
 dump(out/'plist-dates.json',dated);dump(out/'plist-states.json',states)
 dump(out/'metadata-central.json',[dict(x,paris=iso(x['raw'])) for x in json.loads((root/'metadata-candidates.json').read_text()) if start<=x['raw']<=end])
 print('Targeted results saved')
if __name__=='__main__':main()
