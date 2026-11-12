#!/usr/bin/env python3
"""Supplemental provenance queries and missing filename-pattern coverage."""
import collections,datetime as dt,json,pathlib,plistlib,shutil,sqlite3,sys,zipfile
from zoneinfo import ZoneInfo
from tp01_inventory import sha,dump
P=ZoneInfo('Europe/Paris')
def main():
 root=pathlib.Path(sys.argv[1]);source=pathlib.Path(sys.argv[2]);out=root/(sys.argv[3] if len(sys.argv)>3 else 'supplement');out.mkdir(exist_ok=False)
 inv=json.loads((root/'inventory.json').read_text());copied=[]
 for x in inv:
  if x['flags']!=1:continue
  if x['relativePath'].endswith('.plist.backup') or ('com.alibaba.iAliexpress' in x['domain'] and x['relativePath'].endswith('.ahe') and 1728990000<=(x.get('Birth') or 0)<1730111400):
   s=source/x['fileID'][:2]/x['fileID'];p=out/'files'/x['domain']/x['relativePath'];p.parent.mkdir(parents=True,exist_ok=True)
   before=sha(s);shutil.copyfile(s,p);after=sha(s)
   copied.append(dict(x,sha256=before,after=after,copy_sha256=sha(p),signature=p.read_bytes()[:16].hex()))
 dump(out/'collection.json',copied)
 def query(rel,sql,args=()):
  c=sqlite3.connect((root/'files'/rel).as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
  try:return [dict(x) for x in c.execute(sql,args)]
  finally:c.close()
 result={}
 for tag,rel,table in [('cargo','AppDomain-com.ctrip.EBooking/Documents/CargoSDK/cargo.db','table_data'),('language','AppDomain-com.ctrip.EBooking/Documents/v4_fr-FR.db','multi_language')]:
  fields='id,appid,locale,key,timestamp,env,length(value) as value_length' if tag=='cargo' else 'id,appid,key,lang,last_timestamp,length(value) as value_length'
  time='timestamp' if tag=='cargo' else 'last_timestamp'
  result[tag]=query(rel,f'select {fields} from {table} where {time} between 1728991800000 and 1730139600000')
 result['clouddocs_devices']=query('HomeDomain/Library/Application Support/CloudDocs/session/db/server.db','select * from devices')
 result['clouddocs_boot']=query('HomeDomain/Library/Application Support/CloudDocs/session/db/server.db','select * from server_boot_history order by date')
 result['voicemail']=query('HomeDomain/Library/Voicemail/voicemail.db','select rowid,date,trashed_date,duration,flags,expiration from deleted where date between ? and ? order by date',(1728991800,1730139600))
 result['transactions']=[]
 for p in (root/'files').rglob('*.db'):
  if 'tips-store' not in p.name:continue
  rel=str(p.relative_to(root/'files'))
  try:
   r=query(rel,'select Z_PK,ZTIMESTAMP,ZAUTHOR,ZCONTEXTNAME from ATRANSACTION where ZTIMESTAMP between ? and ? order by ZTIMESTAMP',(750684600,751832400))
   if r:result['transactions'].append({'path':rel,'rows':r})
  except sqlite3.Error:pass
 result['profiles']=[]
 for p in (root/'files').rglob('ProfileTruth.plist'):
  d=plistlib.loads(p.read_bytes());result['profiles'].append({'path':str(p.relative_to(root/'files')),'keys':list(d.keys()),'root_value_types':{k:type(v).__name__ for k,v in d.items()}})
 result['wifi_backup']=[]
 wifi_dates=[]
 def walk_dates(v,path,dates):
  if isinstance(v,dict):
   for k,x in v.items():walk_dates(x,path+'/'+str(k),dates)
  elif isinstance(v,list):
   for i,x in enumerate(v):walk_dates(x,path+'/'+str(i),dates)
  elif isinstance(v,dt.datetime):dates.append({'key':path,'raw_utc':str(v),'paris':v.replace(tzinfo=dt.timezone.utc).astimezone(P).isoformat()})
 for p in (out/'files').rglob('*.plist.backup'):
  try:
   d=plistlib.loads(p.read_bytes());result['wifi_backup'].append({'path':str(p.relative_to(out/'files')),'type':type(d).__name__,'keys':list(d.keys()) if isinstance(d,dict) else None,'length':len(d)})
   for i,x in enumerate(d.get('List of known networks',[])):
    dates=[];walk_dates(x,'',dates);wifi_dates.append({'index':i,'ssid':x.get('SSID_STR'),'dates':dates})
  except Exception as e:result['wifi_backup'].append({'path':str(p),'error':str(e)})
 dump(out/'wifi-dates.json',wifi_dates)
 result['ahe']=[]
 for p in (out/'files').rglob('*.ahe'):
  x={'path':str(p.relative_to(out/'files')),'size':p.stat().st_size,'zip':zipfile.is_zipfile(p)}
  if x['zip']:
   with zipfile.ZipFile(p) as z:x['members']=[{'name':i.filename,'date_time':i.date_time} for i in z.infolist()]
  result['ahe'].append(x)
 dump(out/'results.json',result);print('Supplement saved')
if __name__=='__main__':main()
