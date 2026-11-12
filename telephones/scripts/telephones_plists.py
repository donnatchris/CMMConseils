#!/usr/bin/env python3
"""Bounded plist date triage; secrets and medical quantities are not exported."""
import datetime as dt,json,pathlib,plistlib,re,sys
from zoneinfo import ZoneInfo
from tp01_inventory import dump,sha
P=ZoneInfo('Europe/Paris');START=dt.datetime(2024,10,15,13,30,tzinfo=P).timestamp();END=dt.datetime(2024,10,28,19,20,tzinfo=P).timestamp()
def main():
 root=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);out.mkdir(exist_ok=False);dates=[];errors=[];sources=[];states=[]
 for p in (root/'files').rglob('*'):
  if not p.is_file() or not p.name.endswith(('.plist','.plist.backup')):continue
  rel=str(p.relative_to(root/'files'));before=sha(p)
  try:d=plistlib.loads(p.read_bytes())
  except Exception as e:errors.append({'path':rel,'error_class':type(e).__name__});continue
  def walk(v,key):
   if isinstance(v,dict):
    for k,x in v.items():walk(x,key+'/'+str(k))
   elif isinstance(v,list):
    for i,x in enumerate(v):walk(x,key+'/'+str(i))
   elif isinstance(v,dt.datetime):
    t=v.replace(tzinfo=dt.timezone.utc).timestamp()
    if START<=t<=END:dates.append({'path':rel,'key':key,'raw_utc':str(v),'paris':dt.datetime.fromtimestamp(t,dt.timezone.utc).astimezone(P).isoformat(),'format':'native plist datetime'})
   elif isinstance(v,(float,int)) and not isinstance(v,bool) and re.search('date|time|added|last|first',key,re.I):
    for name,offset,scale in [('Unix seconds',0,1),('Cocoa seconds',978307200,1),('Unix milliseconds',0,1000)]:
     t=v/scale+offset
     if START<=t<=END:dates.append({'path':rel,'key':key,'raw':v,'paris':dt.datetime.fromtimestamp(t,dt.timezone.utc).astimezone(P).isoformat(),'format_hypothesis':name})
  walk(d,'');sources.append({'path':rel,'sha256_before':before,'sha256_after':sha(p)})
  if p.name in ['com.apple.MobileBackup.plist','com.apple.purplebuddy.plist','com.apple.healthd.plist']:
   keep={}
   def redact(v):
    if isinstance(v,dict):return {k:redact(x) for k,x in v.items() if re.search('restore|date|build|hardware|version|choice|model|finished|identifier|state|setup',k,re.I)}
    if isinstance(v,bytes):return {'sha256':__import__('hashlib').sha256(v).hexdigest(),'bytes':len(v)}
    return v
   if isinstance(d,dict):keep=redact(d)
   states.append({'path':rel,'values':keep})
 dump(out/'dates.json',dates);dump(out/'errors.json',errors);dump(out/'sources.json',sources);dump(out/'provenance-preferences.json',states)
 print(json.dumps({'plists':len(sources),'dates':len(dates),'errors':len(errors)}))
if __name__=='__main__':main()
