#!/usr/bin/env python3
"""Requêtes natives B/D et comparaison TP-02/TP-03. Sources jamais modifiées."""
import collections
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import shutil
import sqlite3
import unicodedata
from zoneinfo import ZoneInfo

P=Path('/media/shared/codeProjects/DMMConseils')
B=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive'
OUT=B/'telephones-passe2';os.umask(0o077);OUT.mkdir(exist_ok=False)
TZ=ZoneInfo('Europe/Paris');C=978307200
start=dt.datetime(2024,10,15,13,20,tzinfo=TZ).timestamp();end=dt.datetime(2024,10,15,14,5,tzinfo=TZ).timestamp()
roots={'TP-03':B/'telephones-passe1/copies/TP-03','TP-02':P/'telephones/recherche-TP-02/extraction-systeme-20261014/files'}
sources=[];errors=[];res={}

def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def enc(v):
    if isinstance(v,bytes):return {'hex':v.hex(),'bytes':len(v)}
    if isinstance(v,dt.datetime):return v.isoformat()
    if isinstance(v,plistlib.UID):return {'UID':v.data}
    raise TypeError(type(v).__name__)

def dump(name,v):
    with (OUT/name).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2,default=enc)

def copy(src,phone,rel):
    dst=OUT/'copies'/phone/rel;dst.parent.mkdir(parents=True,exist_ok=True)
    if not dst.exists():
        for suf in ('','-wal','-shm'):
            s=Path(str(src)+suf)
            if not s.is_file():continue
            d=Path(str(dst)+suf);h=sha(s);shutil.copyfile(s,d);assert sha(s)==h==sha(d)
            sources.append({'source':str(s),'copy':str(d),'sha256':h})
    return dst

def query(phone,rel,sql,args=()):
    src=roots[phone]/rel
    if not src.exists():
        errors.append({'phone':phone,'relative':rel,'absent_from_collected_set':True});return []
    cp=copy(src,phone,rel)
    c=sqlite3.connect(cp.as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
    try:
        rows=[dict(x) for x in c.execute(sql,args)]
        sources.append({'phone':phone,'relative':rel,'sql':sql,'args':args})
        return rows
    except Exception as e:
        errors.append({'phone':phone,'relative':rel,'sql':sql,'error':str(e)});return []
    finally:c.close()

def decode(v):
    if not isinstance(v,bytes):return v
    try:
        pl=plistlib.loads(v)
        return pl
    except Exception:return {'hex':v.hex(),'bytes':len(v)}

def dated(v,epoch=C):
    try:return dt.datetime.fromtimestamp(v+epoch,dt.timezone.utc).astimezone(TZ).isoformat() if v else None
    except Exception:return None

def norm(v):return re.sub('[^a-z0-9]','',unicodedata.normalize('NFKD',v).encode('ascii','ignore').decode().lower())
q1=json.loads((P/'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/attributs-et-chronologie.json').read_text())
names={norm(x['path'].rsplit('\\',1)[-1].removesuffix('.pdf')) for x in q1['inventory']}
for phone in roots:
    d={};res[phone]=d
    tcc='HomeDomain/Library/TCC/TCC.db'
    d['tcc']=query(phone,tcc,'select rowid,service,client,auth_value,auth_reason,last_modified,pid,pid_version,boot_uuid from access where last_modified between ? and ?',(start,end))
    for x in d['tcc']:x['paris']=dated(x['last_modified'],0)
    for app in ['com.apple.mobilemail','com.apple.DocumentsApp','com.apple.sharingd','com.apple.quicklook.extension.previewUI']:
        rel=f'AppDomainGroup-group.com.apple.tipsnext/{app}/.tipkit/tips-store.db'
        if phone=='TP-03' and not (roots[phone]/rel).exists():
            original=Path('/home/sansforensics/analysis/tp03-20261110/files')/rel
            if original.exists():copy(original,phone,rel)
        lookup=roots[phone]/rel
        if not lookup.exists() and (OUT/'copies'/phone/rel).exists():
            # One additional collected DB not part of the first-pass selection.
            lookup=OUT/'copies'/phone/rel
        if not lookup.exists():
            d[app]={'absent_from_collected_set':True};continue
        if not (roots[phone]/rel).exists():continue
        sql='''select t.*,a.ZNAME author,b.ZNAME bundle,p.ZNAME process,n.ZNAME context from ATRANSACTION t
          left join ATRANSACTIONSTRING a on a.Z_PK=t.ZAUTHORTS
          left join ATRANSACTIONSTRING b on b.Z_PK=t.ZBUNDLEIDTS
          left join ATRANSACTIONSTRING p on p.Z_PK=t.ZPROCESSIDTS
          left join ATRANSACTIONSTRING n on n.Z_PK=t.ZCONTEXTNAMETS
          where t.ZTIMESTAMP between ? and ? order by t.ZTIMESTAMP'''
        appres={'transactions':query(phone,rel,sql,(start-C,end-C))}
        for x in appres['transactions']:x['paris']=dated(x['ZTIMESTAMP'])
        for table in ['ZCOREDONATIONRECORD','ZCOREEVENTRECORD','ZCOREPARAMETERRECORD','ZCORERULERECORD','ZCORETIPRECORD']:
            values=query(phone,rel,'select * from '+table)
            for x in values:
                for k,v in list(x.items()):
                    if isinstance(v,bytes):x[k]=decode(v)
                    if isinstance(v,(int,float)) and k in ('ZDATE','ZLASTDISPLAYED','ZLASTEVALUATED'):x[k+'_paris']=dated(v)
            appres[table]=values
        ids=[x['Z_PK'] for x in appres['transactions']]
        if ids:
            appres['changes']=query(phone,rel,'select c.*,p.Z_NAME entity_name from ACHANGE c left join Z_PRIMARYKEY p on c.ZENTITY=p.Z_ENT where c.ZTRANSACTIONID between ? and ? order by c.Z_PK',(min(ids),max(ids)))
        d[app]=appres
    fb='HomeDomain/Library/FrontBoard/applicationState.db'
    d['frontboard_keys']=query(phone,fb,'select * from key_tab')
    d['frontboard_selected']=query(phone,fb,'''select a.application_identifier,k.key,v.value from kvs v join key_tab k on k.id=v.key
      join application_identifier_tab a on a.id=v.application_identifier where a.application_identifier in
      ('com.apple.DocumentsApp','com.apple.mobilemail','com.apple.sharingd','com.apple.quicklook.extension.previewUI','com.apple.springboard')''')
    for x in d['frontboard_selected']:x['value']=decode(x['value'])
    cd='HomeDomain/Library/CoreDuet/People/interactionC.db'
    d['interactions']=query(phone,cd,'select Z_PK,ZBUNDLEID,ZTARGETBUNDLEID,ZCONTENTURL,ZSTARTDATE,ZENDDATE,ZCREATIONDATE,ZUPDATEDATE,ZMECHANISM from ZINTERACTIONS')
    rows=query(phone,cd,'select Z_PK,ZCREATIONDATE,ZCONTENTURL,ZUTI,ZIDENTIFIER,ZSIZEINBYTES from ZATTACHMENT')
    d['attachment_count']=len(rows);d['matching_attachments']=[]
    for x in rows:
        hay=norm(json.dumps(x,default=enc,ensure_ascii=False))
        if any(n in hay for n in names):d['matching_attachments'].append(x)
    d['keyboard']=query(phone,'KeyboardDomain/Library/Keyboard/user_model_database.sqlite','select * from usermodeldurablerecords')
    d['preferences']={}
    for n in ['com.apple.PeopleSuggester.SeedSuggestions.plist','com.apple.coreduetd.plist','com.apple.timed.plist','com.apple.backboardd.plist','com.apple.springboard.plist','com.apple.biometrickitd.plist']:
        rel='HomeDomain/Library/Preferences/'+n;src=roots[phone]/rel
        if src.exists():
            cp=copy(src,phone,rel)
            try:d['preferences'][n]=plistlib.loads(cp.read_bytes())
            except Exception as e:errors.append({'phone':phone,'relative':rel,'error':str(e)})
    print(phone,'Mail TX',len(d.get('com.apple.mobilemail',{}).get('transactions',[])),'CoreDuet matches',len(d['matching_attachments']),flush=True)
dump('resultats.json',res);dump('sources.json',sources);dump('erreurs.json',errors)
print('ERRORS',len(errors))
