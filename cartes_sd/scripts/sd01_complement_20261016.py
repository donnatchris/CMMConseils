#!/usr/bin/env python3
"""Complément ciblé sur les dérivés validés : aucune connexion SIFT ni scan disque.
Usage depuis le projet : python3 cartes_sd/scripts/sd01_complement_20261016.py
Les sorties sont nouvelles et refusent l'écrasement. Aucun nouveau décodage.
"""
import collections
import csv
import datetime as dt
import hashlib
import json
import pathlib
import platform
from sd01_mp4 import inspect

ROOT=pathlib.Path(__file__).resolve().parents[2]
OLD=ROOT/'cartes_sd/recherche-SD-01/20261015'
OUT=ROOT/'cartes_sd/recherche-SD-01/20261016-complement'
used={}
def read(p):
    p=p.resolve();data=p.read_bytes()
    used[str(p.relative_to(ROOT))]=dict(size=len(data),sha256=hashlib.sha256(data).hexdigest())
    return data
def js(p):return json.loads(read(p))
def write(name,data):
    p=OUT/name;p.parent.mkdir(exist_ok=True,parents=True)
    with p.open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2)
def table(name,rows):
    with (OUT/name).open('x',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def date(s):return dt.datetime.fromisoformat(s)
raw=js(OLD/'inventaires/lecture-fat-independante-v2.json')
videos=list(csv.DictReader(read(OLD/'inventaires/videos.csv').decode().splitlines()))
active=[r for r in videos if r['allocation']=='alloue']
export=js(OLD/'inventaires/export.json')
files={e['inode']:e for e in export['entries'] if 'artifact' in e}
oldmanifest={r['path_from_project']:r for r in csv.DictReader(read(OLD/'manifest-sha256.csv').decode().splitlines())}
entries={e['path']:e for e in raw['entries']}
directories={e['path']:e for e in raw['directories']}
offset=raw['geometry']['data_absolute_offset'];cs=raw['geometry']['cluster_bytes']

def fatstamp(b,do,to=None,cs=False):
    d=int.from_bytes(b[do:do+2],'little')
    if not d:return None
    t=int.from_bytes(b[to:to+2],'little') if to is not None else 0
    stamp=dt.datetime(1980+(d>>9),(d>>5)&15,d&31,t>>11,(t>>5)&63,(t&31)*2)
    if cs:stamp+=dt.timedelta(milliseconds=b[13]*10)
    return stamp.isoformat(' ')

anomalies=[]
for e in raw['entries']:
    if not any(str(e.get(k,'')).startswith(('1999-','2000-')) for k in ('created','written','accessed')):continue
    b=bytes.fromhex(e['raw_hex'])
    decoded=dict(created=fatstamp(b,16,14,True),written=fatstamp(b,24,22),accessed=fatstamp(b,18))
    assert all(decoded[k]==e[k] for k in decoded)
    parent=e['path'].rsplit('/',1)[0] if '/' in e['path'] else ''
    inode='2' if not parent else str(3+(entries[parent]['absolute_entry_offset']-offset)//32)
    blobpath=OLD/'prive/repertoires'/f'{inode}.bin';blob=read(blobpath)
    direct=directories[parent]
    for i,c in enumerate(direct['clusters']):
        start=offset+(c-2)*cs
        if start<=e['absolute_entry_offset']<start+cs:
            local=i*cs+e['absolute_entry_offset']-start
            assert blob[local:local+32]==b
            break
    else:raise ValueError('slot hors copie de répertoire')
    anomalies.append(dict(**e,tsk_inode=3+(e['absolute_entry_offset']-offset)//32,raw_copy=str(blobpath.relative_to(ROOT)),raw_copy_slot_offset=local,alias=e['name'] in ('.','..')))
write('inventaires/traces-fat-1999-2000.json',anomalies)
table('inventaires/traces-fat-1999-2000.csv',[{k:e[k] for k in ('tsk_inode','path','alias','created','written','accessed','start_cluster','absolute_entry_offset','raw_hex','raw_copy','raw_copy_slot_offset')} for e in anomalies])

daydirs=[]
for path,e in entries.items():
    clips=sorted((r for r in active if r['path'].rsplit('/',1)[0]==path),key=lambda r:r['name_start'])
    if not clips:continue
    dot=entries[path+'/.']
    daydirs.append(dict(day=e['name'],parent_created=e['created'],parent_written=e['written'],dot_created=dot['created'],dot_written=dot['written'],first_end=clips[0]['estimated_end'],last_end=clips[-1]['estimated_end'],parent_created_minus_last_end=(date(e['created'])-date(clips[-1]['estimated_end'])).total_seconds(),dot_created_minus_first_end=(date(dot['created'])-date(clips[0]['estimated_end'])).total_seconds()))
table('inventaires/repertoires-premier-dernier-clip.csv',daydirs)

feb=[r for r in active if '2024-02-01'<=r['name_start']<'2024-03-12']
october=[r for r in active if r['name_start'].startswith('2024-10-15')]
table('inventaires/chronologie-fevrier-mars.csv',feb)
table('inventaires/chronologie-20241015.csv',october)
neighbors={'20484616','20984840','21076020','22944776','41167372','46966792'}
targets=[r for r in active if r['inode'] in neighbors|{'20903944','22835208'} or r['name_start'].startswith('2024-10-15')]
medias=[]
for r in targets:
    data=read(OLD/files[r['inode']]['artifact'])
    assert hashlib.sha256(data).hexdigest()==files[r['inode']]['sha256']
    meta=js(OLD/'journaux/ffprobe'/f"{r['inode']}.json")
    structure=inspect(data)
    descriptions=[]
    for b in structure['boxes']:
        if b['path'].endswith('/stsd'):
            content=data[b['offset']:b['offset']+b['size']]
            descriptions.append(dict(size=b['size'],sha256=hashlib.sha256(content).hexdigest()))
    medias.append(dict(inode=r['inode'],path=r['path'],size=len(data),sha256=hashlib.sha256(data).hexdigest(),format=meta.get('format'),streams=[{k:s.get(k) for k in ('index','codec_name','profile','codec_type','codec_tag_string','sample_rate','channels','width','height','level','r_frame_rate','avg_frame_rate','time_base','duration','nb_frames','extradata_size','tags')} for s in meta.get('streams',[])],stsd=descriptions,structure=structure))
write('inventaires/medias-cibles.json',medias)

summary=dict(raw_slots_examined=len(raw['entries']),raw_fat_1999_slots=sum(any(str(e.get(k,'')).startswith('1999-') for k in ('created','written','accessed')) for e in raw['entries']),fat_2000_slots=len(anomalies),fat_2000_alias_slots=sum(e['alias'] for e in anomalies),daily_directories=len(daydirs),parent_within_2seconds_last=sum(abs(e['parent_created_minus_last_end'])<=2 for e in daydirs),dot_within_2seconds_first=sum(abs(e['dot_created_minus_first_end'])<=2 for e in daydirs),october15_video_count=len(october),october15_duration_seconds=sum(float(r['duration']) for r in october),october15_fat_written_minus_estimated_end_range=[min(float(r['fat_written_minus_start_seconds'])-float(r['duration']) for r in october),max(float(r['fat_written_minus_start_seconds'])-float(r['duration']) for r in october)],october15_stsd_pairs=dict(collections.Counter('|'.join(b['sha256'] for b in m['stsd']) for m in medias if m['path'].find('/20241015/')>=0)),october15_sample_table_anomalies=[m['inode'] for m in medias if '/20241015/' in m['path'] and any(t['stsz_sample_count']!=t['chunk_sample_count'] or t['chunks_beyond_eof'] for t in m['structure']['tracks'])],october15_largest_internal_gaps=sorted([dict(inode=r['inode'],next_start=r['name_start'],gap_seconds=float(r['gap_from_previous_end'])) for r in october[1:]],key=lambda r:r['gap_seconds'],reverse=True)[:5],media_hashes_rechecked=len(medias))
write('inventaires/synthese-complement.json',summary)

for relative in ('docs/mail.txt','discussion-chat.md','remise-documents/attestation-de-remise.md','cartes_sd/analyse-cartes_sd.md','ordinateur/analyse-ordinateur.md','telephones/analyse-TP-02.md','freebox/analyse-freebox.md'):
    read(ROOT/relative)
# Les dérivés de la campagne initiale doivent toujours correspondre au manifeste.
checked=[]
for path,info in used.items():
    if path in oldmanifest:
        assert info['sha256']==oldmanifest[path]['sha256'],path
        checked.append(path)
write('sources/fichiers-consultes.json',dict(files=used,old_manifest_hash_checks=checked))
write('journaux/execution.json',dict(utc=dt.datetime.now(dt.timezone.utc).isoformat(),python=platform.python_version(),command='python3 cartes_sd/scripts/sd01_complement_20261016.py',method='Réexamen local ciblé ; aucune connexion SSH, aucun scan ou décodage intégral supplémentaire',checked_old_artifacts=len(checked)))
print(json.dumps(summary,indent=2))
