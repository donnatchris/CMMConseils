#!/usr/bin/env python3
"""Compare toutes les métadonnées des 72 objets, exactitude décimale et doublons."""
import collections
import datetime as dt
from decimal import Decimal
import hashlib
import itertools
import json
import math
from pathlib import Path
import plistlib
import statistics
import struct
import re
import sqlite3
from zoneinfo import ZoneInfo

P=Path('/media/shared/codeProjects/DMMConseils')
Q=P/'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive'
O=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/attributs';O.mkdir(exist_ok=False)
r=json.loads((Q/'resultats.json').read_text());TZ=ZoneInfo('Europe/Paris');objs=[];sources=[]
def canon(v):
    if isinstance(v,bytes):return {'bytes_sha256':hashlib.sha256(v).hexdigest(),'length':len(v)}
    if isinstance(v,plistlib.UID):return {'UID':v.data}
    if isinstance(v,dict):return {k:canon(x) for k,x in v.items()}
    if isinstance(v,list):return [canon(x) for x in v]
    return v
def actual(v,objects,seen=()):
    if isinstance(v,plistlib.UID):
        if v.data in seen:return {'cycle':v.data}
        return actual(objects[v.data],objects,seen+(v.data,))
    if isinstance(v,dict):return {k:actual(x,objects,seen) for k,x in v.items()}
    if isinstance(v,list):return [actual(x,objects,seen) for x in v]
    return v
def timestamp(s):
    text=s.split('[')[0];d=dt.datetime.fromisoformat(text)
    # Integer second conversion; fraction retained separately without float.
    second=int(d.replace(microsecond=0).timestamp())
    fraction=re.search(r'\.(\d+)',text)
    return Decimal(second)+(Decimal('0.'+fraction.group(1)) if fraction else Decimal(0))
for phone,rows in r['phones'].items():
    for x in rows:
        p=Q/phone/(x['fileID']+'.plist');b=p.read_bytes();sources.append({'source':str(p),'sha256':hashlib.sha256(b).hexdigest()})
        pl=plistlib.loads(b);v=actual(pl['$objects'][pl['$top']['root'].data],pl['$objects'])
        attrs=plistlib.loads(v['ExtendedAttributes']) if 'ExtendedAttributes' in v else {}
        last=None
        if 'com.apple.lastuseddate#PS' in attrs:
            sec,nano=struct.unpack('<qq',attrs['com.apple.lastuseddate#PS']);assert 0<=nano<10**9
            last=Decimal(sec)+Decimal(nano)/Decimal(10**9)
        objs.append({'phone':phone,'fileID':x['fileID'],'sha512':x['sha512'],'relativePath':x['relativePath'],'domain':x['domain'],
                     'all_fields':canon(v),'xattrs':canon(attrs),'lastused_epoch_decimal':str(last) if last is not None else None,
                     'lastused_paris':dt.datetime.fromtimestamp(int(last),dt.timezone.utc).astimezone(TZ).isoformat() if last else None})
comparisons=[]
for h in sorted({x['sha512'] for x in objs}):
    a=[x for x in objs if x['phone']=='TP-02' and x['sha512']==h];b=[x for x in objs if x['phone']=='TP-03' and x['sha512']==h]
    for x,y in itertools.product(a,b):
        keys=set(x['all_fields'])|set(y['all_fields'])
        comparisons.append({'sha512':h,'tp02':x['fileID'],'tp03':y['fileID'],
                            'identical_fields':[k for k in sorted(keys) if k in x['all_fields'] and k in y['all_fields'] and x['all_fields'][k]==y['all_fields'][k]],
                            'different_or_missing_fields':[k for k in sorted(keys) if k not in x['all_fields'] or k not in y['all_fields'] or x['all_fields'][k]!=y['all_fields'][k]]})
summary={}
for phone in r['phones']:
    rr=[x for x in objs if x['phone']==phone]
    fields=set(k for x in rr for k in x['all_fields'])
    summary[phone]={'objects':len(rr),'domains':dict(collections.Counter(x['domain'] for x in rr)),
                    'fields':{k:dict(collections.Counter(json.dumps(x['all_fields'].get(k,'[absent]'),sort_keys=True) for x in rr)) for k in sorted(fields) if k not in ['EncryptionKey','ExtendedAttributes','RelativePath','$class']},
                    'xattr_counts':dict(collections.Counter(k for x in rr for k in x['xattrs']))}
dups=[];offsets=[]
for h in sorted({x['sha512'] for x in r['inventory']}):
    iv=sorted([x for x in r['inventory'] if x['sha512']==h],key=lambda x:timestamp(x['creation']))
    if len(iv)>1:
        dups.append({'sha512':h,'inventory':iv,'gaps_seconds':[str(timestamp(y['creation'])-timestamp(x['creation'])) for x,y in zip(iv,iv[1:])],
                     'backup_objects':{phone:[{'fileID':x['fileID'],'relativePath':x['relativePath']} for x in objs if x['phone']==phone and x['sha512']==h] for phone in r['phones']}})
    for x in objs:
        if x['phone']!='TP-03' or x['sha512']!=h or x['lastused_epoch_decimal'] is None:continue
        if x['lastused_paris'].startswith('2024-10-15T13:'):
            offsets.append({'sha512':h,'fileID':x['fileID'],'dnef_first_creation':iv[0]['creation'],'lastused_paris':x['lastused_paris'],
                            'dnef_minus_lastused_seconds':str(timestamp(iv[0]['creation'])-Decimal(x['lastused_epoch_decimal']))})
deltas=[float(x['dnef_minus_lastused_seconds']) for x in offsets];med=statistics.median(deltas)
summary['clock_offsets']={'n':len(deltas),'min':min(deltas),'max':max(deltas),'mean':statistics.mean(deltas),'median':med,'median_absolute_deviation':statistics.median(abs(x-med) for x in deltas),
                           'meaning':'paired timestamp differences, not certified clock calibration'}
summary['dnef_creation_fraction_digits']=dict(collections.Counter(len(re.search(r'\.(\d+)',x['creation']).group(1)) if re.search(r'\.(\d+)',x['creation']) else 0 for x in r['inventory']))
# Protection classes and historical marker metadata for native artefacts.
c=sqlite3.connect((Q/'TP-03/Manifest.db').as_uri()+'?mode=ro&immutable=1',uri=True)
native=[]
rx=re.compile(r'TCC/TCC.db$|user_model_database.sqlite$|PeopleSuggester.SeedSuggestions|coreduetd.plist|FrontBoard/applicationState|\.FirstUnlock$|com.apple.mobilemail/.tipkit/tips-store.db$|knowledgeC|powerlog',re.I)
for fid,domain,rel,blob in c.execute('select fileID,domain,relativePath,file from Files where flags=1'):
    if rx.search(rel):
        pl=plistlib.loads(blob);v=pl['$objects'][pl['$top']['root'].data]
        native.append({'fileID':fid,'domain':domain,'relativePath':rel,**{k:v.get(k) for k in ['Birth','LastModified','LastStatusChange','ProtectionClass','Size']}})
c.close()
for n,v in [('objets.json',objs),('comparaisons.json',comparisons),('doublons.json',dups),('horloges.json',offsets),('synthese.json',summary),('protection-artefacts.json',native),('sources.json',sources)]:
    with (O/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2)
print(json.dumps({'objects':len(objs),'cross_phone_pairs':len(comparisons),'duplicates':len(dups),'clock_offsets':summary['clock_offsets'],
                  'classes':{p:summary[p]['fields']['ProtectionClass'] for p in r['phones']}},ensure_ascii=False))
