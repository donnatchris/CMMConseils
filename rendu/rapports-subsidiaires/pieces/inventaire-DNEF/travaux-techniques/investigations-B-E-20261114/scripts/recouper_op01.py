#!/usr/bin/env python3
"""Prefetch, UserAssist, Apple et exports existants, OP-01 monté RO."""
import codecs
import collections
import csv
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import shutil
import struct
import subprocess
import pyscca
import pyregf

P=Path('/media/shared/codeProjects/DMMConseils');W=Path('/mnt/windows')
O=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/op01-artefacts';os.umask(0o077);O.mkdir(exist_ok=False)
sources=[];errors=[];res={}
rx=re.compile(r'itunes|appledevices|applemobile|usbmux|imazing|3utools|ifunbox|iexplorer|cellebrite|ufed|oxygen|elcomsoft|xry|ldsd|iphone13|archive_saddedine|inventaire_saddedine|rejets_saddedine|L16B',re.I)

def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def copied(p):
    d=O/'copies'/p.relative_to(W);d.parent.mkdir(parents=True,exist_ok=True)
    h=sha(p);shutil.copyfile(p,d);assert h==sha(d)==sha(p)
    sources.append({'source':str(p),'copy':str(d),'sha256':h,'bytes':p.stat().st_size})
    return d

def ft(n):
    return (dt.datetime(1601,1,1,tzinfo=dt.timezone.utc)+dt.timedelta(microseconds=n//10)).isoformat() if n else None

def dump(n,v):
    with (O/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2)

res['mount']=subprocess.check_output(['findmnt','-n','-o','SOURCE,OPTIONS','/mnt/windows'],text=True).strip()
assert 'ro,' in res['mount']
pf=[];pfcounts=collections.Counter()
for p in sorted((W/'Windows/Prefetch').glob('*.pf')):
    pfcounts['files']+=1
    try:
        f=pyscca.file();f.open(str(p));exe=f.executable_filename;times=[]
        for i in range(8):
            try:times.append(ft(f.get_last_run_time_as_integer(i)))
            except Exception:break
        files=[f.get_filename(i) for i in range(f.number_of_filenames)]
        targets=[n for n in files if rx.search(n)]
        day=any(t and t.startswith(('2024-10-15','2024-10-28')) for t in times)
        if rx.search(exe) or targets or day:
            cp=copied(p)
            pf.append({'prefetch':p.name,'executable':exe,'run_count':f.run_count,'run_times':times,'target_references':targets,'all_file_references':files,'sha256':sha(cp)})
        f.close();pfcounts['parsed']+=1
    except Exception as e:errors.append({'prefetch':p.name,'error':str(e)});pfcounts['errors']+=1
res['prefetch']={'counts':dict(pfcounts),'selected':pf};print('PF',dict(pfcounts),len(pf),flush=True)
ua=[]
for user in ['fintm','INVITES']:
    src=W/'Users'/user/'NTUSER.DAT'
    if not src.exists():continue
    cp=copied(src);f=pyregf.file();f.open(str(cp))
    root=f.get_key_by_path(r'Software\Microsoft\Windows\CurrentVersion\Explorer\UserAssist')
    if root:
        for guid in root.sub_keys:
            cnt=guid.get_sub_key_by_name('Count')
            if not cnt:continue
            for v in cnt.values:
                n=codecs.decode(v.name or '', 'rot_13');b=v.data or b''
                last=ft(struct.unpack_from('<Q',b,60)[0]) if len(b)>=72 else None
                if rx.search(n) or last and last.startswith(('2024-10-15','2024-10-28')):
                    ua.append({'user':user,'guid':guid.name,'name':n,'bytes':len(b),'raw_hex':b.hex(),'last_run_utc':last,'run_count':struct.unpack_from('<I',b,4)[0] if len(b)>=8 else None,'key_lastwrite':str(cnt.last_written_time)})
    f.close()
res['userassist']=ua
pair=[]
for p in sorted((W/'ProgramData/Apple/Lockdown').glob('*.plist')):
    cp=copied(p);v=plistlib.loads(cp.read_bytes())
    pair.append({'filename':p.name,'sha256':sha(cp),'keys':sorted(v),
                 'HostID_sha256':hashlib.sha256(str(v.get('HostID')).encode()).hexdigest(),
                 'SystemBUID_sha256':hashlib.sha256(str(v.get('SystemBUID')).encode()).hexdigest(),
                 'private_material_exported':False})
res['pair_records']=pair
setup=[]
for p in sorted((W/'Windows/INF').glob('setupapi*.log')):
    text=p.read_text(errors='replace')
    sections=re.split(r'(?=^>>>\s+\[)',text,flags=re.M)
    selected=[]
    for section in sections:
        if re.search(r'VID_05AC|Apple|iPhone|00008110|001249321444801E|001C69A002BA801E|Kingston|DataTraveler',section,re.I):
            selected.append({'header':section.splitlines()[0] if section else '',
                             'dates_local_unqualified':re.findall(r'(?:Section start|Section end)\s+(\d{4}/\d\d/\d\d\s+\d\d:\d\d:\d\d\.\d+)',section),
                             'text':section})
    if selected:copied(p);setup.append({'source':p.name,'sections':selected})
res['setupapi']=setup
exports={
 'amcache':P/'ordinateur/recherche-OP-01/extractions-acces/additional/amcache.json',
 'registry':P/'ordinateur/recherche-OP-01/extractions-acces/registry.json',
 'mft_old':P/'ordinateur/recherche-OP-01/extractions-acces/mft-targets/mft-target-records.jsonl',
 'usb_property_dates':P/'ordinateur/recherche-OP-01/extractions-acces/usb-property-dates.json',
 'usb_mapping':P/'ordinateur/recherche-OP-01/extractions-acces/usb-mounteddevices-crosscheck.json',
 'logfile_context':P/'ordinateur/recherche-OP-01/integrite-evtx/ntfs/usn-logfiles.jsonl',
}
res['export_hits']={}
for key,p in exports.items():
    sources.append({'source':str(p),'sha256':sha(p),'kind':'previous_export'})
    if p.suffix=='.jsonl':rows=[json.loads(l) for l in p.read_text().splitlines()]
    else:rows=json.loads(p.read_text())
    if isinstance(rows,list):res['export_hits'][key]=[x for x in rows if rx.search(json.dumps(x,ensure_ascii=False))]
    else:res['export_hits'][key]=rows
events=[]
p=P/'ordinateur/recherche-OP-01/chronologie.csv';sources.append({'source':str(p),'sha256':sha(p)})
with p.open(newline='') as f:
    for x in csv.DictReader(f):
        if rx.search(x['data_json']) or x['provider']=='Microsoft-Windows-Kernel-General' and x['event_id']=='1':events.append(x)
res['events_export']=events
jl=P/'ordinateur/recherche-OP-01/operations-28oct/resultats-sift/jumplists-standard/20261014063026_AutomaticDestinations.csv'
sources.append({'source':str(jl),'sha256':sha(jl)})
with jl.open(newline='',encoding='utf-8-sig') as f:res['jumplists']=[x for x in csv.DictReader(f) if rx.search(json.dumps(x,ensure_ascii=False))]
logs=[]
for root in [W/'Users/fintm/AppData/Roaming/Apple Computer',W/'Users/fintm/AppData/Local/Apple Computer',W/'Users/fintm/AppData/Local/Apple',W/'ProgramData/Apple',W/'ProgramData/Apple Computer']:
    if not root.exists():continue
    for dp,ds,fs in os.walk(root,followlinks=False):
        ds[:]=[n for n in ds if n not in ['MobileSync'] and not (Path(dp)/n).is_symlink()]
        if len(Path(dp).relative_to(root).parts)>=5:ds[:]=[]
        for n in fs:
            p=Path(dp)/n
            if p.suffix.lower() in ['.log','.txt','.xml'] and p.stat().st_size<20000000:
                text=p.read_text(errors='replace')
                lines=[l for l in text.splitlines() if rx.search(l) or re.search(r'2024[-/]10[-/](15|28)',l)]
                logs.append({'path':str(p.relative_to(W)),'sha256':sha(p),'target_lines':lines[:500],'capped':len(lines)>500})
                if lines:copied(p)
res['apple_logs']=logs
dump('resultats.json',res);dump('sources.json',sources);dump('erreurs.json',errors)
print(json.dumps({'prefetch':dict(pfcounts),'userassist_selected':len(ua),'setupapi_sources':len(setup),'apple_log_files':len(logs),'errors':len(errors)}))
