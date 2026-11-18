"""Analyse des neuf objets natifs nouvellement déchiffrés, sur copies."""
import datetime as dt
import hashlib
import io
import json
from pathlib import Path
import plistlib
import re
import sys
from zoneinfo import ZoneInfo
P=Path('/media/shared/codeProjects/DMMConseils');sys.path.insert(0,str(P/'telephones/scripts'))
from tp03_recover_preferences import TolerantDates
B=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/complement-natif-v2'
TZ=ZoneInfo('Europe/Paris');res=[]
def enc(v):
    if isinstance(v,bytes):return {'hex':v.hex(),'bytes':len(v)}
    if isinstance(v,dt.datetime):return {'utc':v.isoformat(),'paris':v.replace(tzinfo=dt.timezone.utc).astimezone(TZ).isoformat()}
    if isinstance(v,plistlib.UID):return {'UID':v.data}
    raise TypeError(type(v).__name__)
for x in json.loads((B/'collection.json').read_text()):
    p=B/'files'/x['domain']/x['relativePath'];raw=p.read_bytes();assert hashlib.sha256(raw).hexdigest()==x['sha256']
    row={'domain':x['domain'],'relativePath':x['relativePath'],'sha256':x['sha256'],'bytes':len(raw),'format':raw[:8].decode('ascii','replace'),'date_candidates':[]}
    try:row['value']=TolerantDates(dict_type=dict).parse(io.BytesIO(raw)) if raw.startswith(b'bplist00') else plistlib.loads(raw)
    except Exception as e:row['error_class']=type(e).__name__;res.append(row);continue
    def walk(v,key):
        if isinstance(v,dt.datetime):row['date_candidates'].append({'key':key,'native_date':enc(v)})
        elif isinstance(v,dict):
            for k,w in v.items():walk(w,key+'/'+str(k))
        elif isinstance(v,list):
            for i,w in enumerate(v):walk(w,key+'/'+str(i))
        elif isinstance(v,(int,float)) and not isinstance(v,bool) and re.search('time|date|unlock|launch',key,re.I):
            for epoch,name in [(0,'unix_s'),(978307200,'cocoa_s')]:
                try:
                    date=dt.datetime.fromtimestamp(v+epoch,dt.timezone.utc)
                    if 2018<=date.year<=2027:row['date_candidates'].append({'key':key,'raw':v,'epoch_hypothesis':name,'paris':date.astimezone(TZ).isoformat()})
                except (ValueError,OverflowError,OSError):pass
    walk(row['value'],'');res.append(row)
with (B/'analyse.json').open('x') as f:json.dump(res,f,ensure_ascii=False,indent=2,default=enc)
print(json.dumps([{'domain':x['domain'],'path':x['relativePath'],'keys':list(x.get('value',{})) if isinstance(x.get('value'),dict) else None,'date_candidates':x['date_candidates'],'error_class':x.get('error_class')} for x in res],ensure_ascii=False))
