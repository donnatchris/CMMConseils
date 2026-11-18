"""Décodage non destructif des archives d'état et contrôle des dates natives."""
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import plistlib
import sqlite3
import sys
from zoneinfo import ZoneInfo
P=Path('/media/shared/codeProjects/DMMConseils')
sys.path.insert(0,str(P/'telephones/scripts'))
from tp03_recover_preferences import TolerantDates
O=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/telephones-passe2'
res={};TZ=ZoneInfo('Europe/Paris')
def enc(v):
    if isinstance(v,bytes):return {'bytes':len(v),'sha256':hashlib.sha256(v).hexdigest()}
    if isinstance(v,plistlib.UID):return {'UID':v.data}
    if isinstance(v,dt.datetime):return {'utc':v.isoformat(),'paris':v.replace(tzinfo=dt.timezone.utc).astimezone(TZ).isoformat()}
    raise TypeError(type(v).__name__)
for ph in ['TP-03','TP-02']:
    p=O/'copies'/ph/'HomeDomain/Library/FrontBoard/applicationState.db'
    c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True)
    rows=c.execute('''select a.application_identifier,k.key,v.value from kvs v join key_tab k on k.id=v.key join application_identifier_tab a on a.id=v.application_identifier where a.application_identifier in ('com.apple.DocumentsApp','com.apple.mobilemail')''').fetchall()
    decoded=[]
    for app,key,blob in rows:
        if not isinstance(blob,bytes):continue
        row={'app':app,'key':key,'blob_sha256':hashlib.sha256(blob).hexdigest()}
        try:row['value']=TolerantDates(dict_type=dict).parse(io.BytesIO(blob))
        except Exception as e:row['error']=str(e);row['error_class']=type(e).__name__
        candidates=[]
        def walk(v,path):
            if isinstance(v,dt.datetime):
                if v.year==2024 and v.month==10:candidates.append({'path':path,'native_date':enc(v)})
            elif isinstance(v,dict):
                for k,x in v.items():
                    if k=='NS.time' and isinstance(x,(int,float)):
                        try:
                            when=dt.datetime(2001,1,1)+dt.timedelta(seconds=x)
                            if when.year==2024 and when.month==10:candidates.append({'path':path+'/'+k,'NSDate_cocoa':x,'date':enc(when)})
                        except Exception:pass
                    walk(x,path+'/'+str(k))
            elif isinstance(v,list):
                for i,x in enumerate(v):walk(x,path+'/'+str(i))
        walk(row.get('value'),'');row['october_2024_dates']=candidates;decoded.append(row)
    c.close();res[ph]={'db_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'decoded':decoded}
with (O/'frontboard-decode.json').open('x') as f:json.dump(res,f,ensure_ascii=False,indent=2,default=enc)
print(json.dumps({ph:{'db_sha256':d['db_sha256'],'fields':len(d['decoded']),'errors':sum('error' in x for x in d['decoded']),'october_dates':sum(len(x['october_2024_dates']) for x in d['decoded'])} for ph,d in res.items()}))
