#!/usr/bin/env python3
"""Inventaire et schémas B/D sur copies neuves ; exécution SIFT."""
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
import sys
from zoneinfo import ZoneInfo

PROJECT = Path('/media/shared/codeProjects/DMMConseils')
OUT = PROJECT / 'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/telephones-passe1'
GENERAL = Path('/home/sansforensics/analysis/tp03-20261110')
PRIORITY = Path('/home/sansforensics/analysis/tp03-priority-20261110')
P = ZoneInfo('Europe/Paris')
START = dt.datetime(2024,10,15,13,20,tzinfo=P).timestamp()
END = dt.datetime(2024,10,15,14,5,tzinfo=P).timestamp()
os.umask(0o077)
OUT.mkdir(parents=True, exist_ok=False)
sources, errors, result = [], [], {}


def sha(p):
    with p.open('rb') as f:
        return hashlib.file_digest(f,'sha256').hexdigest()


def encoded(v):
    if isinstance(v, bytes):
        return {'hex':v.hex(), 'bytes':len(v)}
    if isinstance(v, dt.datetime):
        return v.isoformat()
    if isinstance(v, plistlib.UID):
        return {'UID': v.data}
    raise TypeError(type(v).__name__)


def dump(name,v):
    with (OUT / name).open('x') as f:
        json.dump(v,f,ensure_ascii=False,indent=2,default=encoded)


def copied(src, tag):
    dst = OUT/'copies'/tag
    dst.parent.mkdir(parents=True,exist_ok=True)
    checks=[]
    for suffix in ('','-wal','-shm'):
        sp=Path(str(src)+suffix)
        if not sp.exists():continue
        dp=Path(str(dst)+suffix)
        before=sha(sp)
        shutil.copyfile(sp,dp)
        assert before==sha(sp)==sha(dp)
        checks.append({'source':str(sp),'copy':str(dp),'sha256':before})
    sources.extend(checks)
    return dst


def inspect_db(src, tag):
    cp=copied(src,tag)
    c=sqlite3.connect(cp.as_uri()+'?mode=ro',uri=True)
    c.row_factory=sqlite3.Row
    data={'source':str(src),'tables':[], 'candidates':[], 'queries':[]}
    try:
        schema=[dict(x) for x in c.execute("select name,sql from sqlite_master where type='table'")]
        data['schema']=schema
        for s in schema:
            table=s['name']
            if s['sql'] and s['sql'].upper().startswith('CREATE VIRTUAL'):continue
            qt='"'+table.replace('"','""')+'"'
            try:
                cols=[dict(x) for x in c.execute('pragma table_info('+qt+')')]
                data['tables'].append({'name':table,'columns':cols,'count':c.execute('select count(*) from '+qt).fetchone()[0]})
                for col in cols:
                    name=col['name']
                    if col['type'].upper() in ('TEXT','BLOB','VARCHAR'):continue
                    if not re.search(r'date|time|start|end|creat|modif|updat|unlock|lock|boot',name,re.I):continue
                    qc='"'+name.replace('"','""')+'"'
                    mm=c.execute('select min('+qc+'),max('+qc+') from '+qt).fetchone()
                    if not all(isinstance(v,(int,float)) for v in mm):continue
                    for scale,epoch,label in [(1,0,'unix_s'),(1000,0,'unix_ms'),(1e9,0,'unix_ns'),(1,978307200,'cocoa_s'),(1000,978307200,'cocoa_ms'),(1e9,978307200,'cocoa_ns')]:
                        lo,hi=(START-epoch)*scale,(END-epoch)*scale
                        if mm[0]>hi or mm[1]<lo:continue
                        sql='select * from '+qt+' where '+qc+' between ? and ? limit 501'
                        rows=[dict(x) for x in c.execute(sql,(lo,hi))]
                        if rows:data['candidates'].append({'table':table,'column':name,'epoch':label,'sql':sql,'args':[lo,hi],'rows':rows,'capped':len(rows)==501})
            except Exception as e:errors.append({'source':str(src),'table':table,'error':str(e)})
        if src.name=='TCC.db':
            sql='select rowid,* from access where last_modified between ? and ?'
            data['tcc_window']=[dict(x) for x in c.execute(sql,(START,END))]
            data['queries'].append({'sql':sql,'args':[START,END]})
        if src.name=='user_model_database.sqlite':
            data['keyboard_records']=[dict(x) for x in c.execute('select * from usermodeldurablerecords')]
    finally:c.close()
    return data


manifest=PROJECT/'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/TP-03/Manifest.db'
cp=copied(manifest,'TP-03/Manifest.db')
con=sqlite3.connect(cp.as_uri()+'?mode=ro',uri=True)
rx=re.compile(r'knowledge|unlock|lockstate|boot|shutdown|logarchive|tracev3|powerlog|aggregate|springboard|backboard|frontboard|recent|fileprovider|mobilemail|quicklook|sharing|PeopleSuggester|coreduet|Keyboard/user_model|timed|biometr|analytics',re.I)
selected=[]
for fid,domain,relative,flags,blob in con.execute('select fileID,domain,relativePath,flags,file from Files where flags=1'):
    if not rx.search(domain+'/'+relative):continue
    pl=plistlib.loads(blob);obj=pl['$objects'][pl['$top']['root'].data]
    selected.append({'fileID':fid,'domain':domain,'relativePath':relative,**{k:obj.get(k) for k in ('Birth','LastModified','LastStatusChange','ProtectionClass','Size')}})
con.close()
result['manifest_targets']=selected
result['databases']={}
result['plists']={}
db_rx=re.compile(r'TCC/TCC.db$|Keyboard/user_model_database.sqlite$|CoreDuet|knowledge|FrontBoard|SpringBoard|fileprovider|FileProvider|MobileMail|QuickLook|/Mail/|biometric|powerlog|aggregate|appstate',re.I)
plist_rx=re.compile(r'PeopleSuggester|coreduetd|springboard|backboard|biometr|timed|boot|firstunlock|lockstate|MobileMail|fileprovider|sharing|QuickLook',re.I)
for root in (GENERAL,PRIORITY):
    for p in (root/'files').rglob('*'):
        if not p.is_file() or p.name.endswith(('-wal','-shm','-journal')):continue
        rel=p.relative_to(root/'files')
        if str(rel) in result['databases'] or str(rel) in result['plists']:continue
        if p.suffix=='.plist' and plist_rx.search(str(rel)):
            try:
                cp=copied(p,'TP-03/'+str(rel))
                result['plists'][str(rel)]={'source':str(p),'value':plistlib.loads(cp.read_bytes())}
            except Exception as e:errors.append({'source':str(p),'error':str(e)})
        elif db_rx.search(str(rel)):
            with p.open('rb') as f:header=f.read(16)
            if header==b'SQLite format 3\x00':
                result['databases'][str(rel)]=inspect_db(p,'TP-03/'+str(rel))
                print('DB',rel,flush=True)
dump('resultats.json',result)
dump('sources.json',sources)
dump('erreurs.json',errors)
print(json.dumps({'manifest_candidates':len(selected),'databases':len(result['databases']),'plists':len(result['plists']),'errors':len(errors)}))
