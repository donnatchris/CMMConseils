"""Contrôle ciblé sur SIFT, sources ouvertes en lecture seule et sans rejeu WAL.
Exécution : ssh -F ~/.ssh/config sift 'python3 -' < verifier_sift.py > resultats.json
Aucun secret nécessaire : utilise les acquisitions déjà déchiffrées.
"""
import collections
import datetime as dt
import hashlib
import json
from pathlib import Path
import plistlib
import re
import sqlite3
import struct
from zoneinfo import ZoneInfo

P = Path('/media/shared/codeProjects/DMMConseils')
Q = P / 'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive'
B = P / 'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive'
TZ = ZoneInfo('Europe/Paris')
START = dt.datetime(2024, 10, 15, 13, 25, tzinfo=TZ).timestamp()
END = dt.datetime(2024, 10, 15, 13, 51, tzinfo=TZ).timestamp()
COCOA = 978307200
sources = {}
queries = []

def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()

def track(p):
    if p not in sources:
        sources[p] = sha(p)

def load(p):
    track(p)
    return p.read_bytes()

def connect(p):
    track(p)
    wal = Path(str(p) + '-wal')
    if wal.exists():
        track(wal)
        assert wal.stat().st_size == 0, f'WAL non vide : {p}'
    return sqlite3.connect(p.as_uri() + '?mode=ro&immutable=1', uri=True)

def query(p, sql, args=()):
    con = connect(p)
    con.row_factory = sqlite3.Row
    try:
        rows = [dict(x) for x in con.execute(sql, args)]
    finally:
        con.close()
    queries.append({'source': str(p), 'sql': sql, 'args': args, 'count': len(rows)})
    return rows

def paris(v, epoch=0):
    return dt.datetime.fromtimestamp(v + epoch, dt.timezone.utc).astimezone(TZ).isoformat()

def unarchive(v, objects):
    if isinstance(v, plistlib.UID):
        return unarchive(objects[v.data], objects)
    if isinstance(v, dict):
        return {k: unarchive(x, objects) for k, x in v.items()}
    if isinstance(v, list):
        return [unarchive(x, objects) for x in v]
    return v

old = json.loads(load(Q / 'resultats.json'))
out = {'window_paris': [paris(START), paris(END)], 'end_inclusive': True, 'phones': {}}
roots = {
    'TP-03': Path('/home/sansforensics/analysis/tp03-20261110/files'),
    'TP-02': P / 'telephones/recherche-TP-02/extraction-systeme-20261014/files',
}
for phone, root in roots.items():
    d = out['phones'][phone] = {}
    tcc = query(root / 'HomeDomain/Library/TCC/TCC.db',
                'select rowid,service,client,auth_value,auth_reason,last_modified,boot_uuid from access where last_modified between ? and ?', (START, END))
    for x in tcc:
        x['paris'] = paris(x['last_modified'])
    d['tcc'] = tcc
    for app in ['com.apple.mobilemail', 'com.apple.DocumentsApp']:
        p = root / f'AppDomainGroup-group.com.apple.tipsnext/{app}/.tipkit/tips-store.db'
        if not p.exists():
            d[app] = {'collected_database_absent': True}
            continue
        rows = query(p, '''select t.Z_PK,t.ZTIMESTAMP,a.ZNAME author,b.ZNAME bundle,p.ZNAME process
          from ATRANSACTION t left join ATRANSACTIONSTRING a on a.Z_PK=t.ZAUTHORTS
          left join ATRANSACTIONSTRING b on b.Z_PK=t.ZBUNDLEIDTS
          left join ATRANSACTIONSTRING p on p.Z_PK=t.ZPROCESSIDTS
          where t.ZTIMESTAMP between ? and ? order by t.ZTIMESTAMP''', (START-COCOA, END-COCOA))
        for x in rows:
            x['paris'] = paris(x['ZTIMESTAMP'], COCOA)
        d[app] = {'transactions': rows}
        if rows:
            changes = query(p, '''select p.Z_NAME entity_name,count(*) n from ACHANGE c
              left join Z_PRIMARYKEY p on c.ZENTITY=p.Z_ENT
              where c.ZTRANSACTIONID between ? and ? group by p.Z_NAME''', (rows[0]['Z_PK'], rows[-1]['Z_PK']))
            d[app]['changes'] = changes
        d[app]['tip_display_dates'] = query(p, 'select Z_PK,ZLASTDISPLAYED from ZCORETIPRECORD')
    keyboard = query(root / 'KeyboardDomain/Library/Keyboard/user_model_database.sqlite',
                     'select rowid,key,value,last_update_date from usermodeldurablerecords where last_update_date between ? and ?', (START, END))
    for x in keyboard:
        x['paris'] = paris(x['last_update_date'])
    d['keyboard'] = keyboard
    prefs = root / 'HomeDomain/Library/Preferences/com.apple.PeopleSuggester.SeedSuggestions.plist'
    if prefs.exists():
        v = plistlib.loads(load(prefs))
        d['people_suggester_keys'] = list(v)
        date = v.get('DeviceIdDate')
        d['people_suggester_date_paris'] = date.replace(tzinfo=dt.timezone.utc).astimezone(TZ).isoformat() if isinstance(date, dt.datetime) else None
    manifest = Q / phone / 'Manifest.db'
    ids = {x['fileID']: x for x in old['phones'][phone]}
    con = connect(manifest)
    d['pdf_objects'] = []
    d['system_marker_candidates'] = []
    d['protection_classes'] = []
    for fid, domain, rel, blob in con.execute('select fileID,domain,relativePath,file from Files where flags=1'):
        marker = re.search(r'(firstunlock|knowledgeC\.db|powerlog|\.tracev3$|\.logarchive|(^|/)Biome/|keybag|lockstate|printcenter|printing|printjob)', domain+'/'+rel, re.I)
        native = re.search(r'TCC/TCC.db$|user_model_database.sqlite$|mobilemail/\.tipkit/tips-store.db$', rel)
        if not (fid in ids or marker or native):
            continue
        pl = plistlib.loads(blob)
        v = unarchive(pl['$top']['root'], pl['$objects'])
        row = {'fileID': fid, 'domain': domain, 'relativePath': rel,
               **{k: v.get(k) for k in ['Birth', 'LastModified', 'LastStatusChange', 'ProtectionClass']}}
        if fid in ids:
            row['sha512_previously_verified'] = ids[fid]['sha512']
            attrs = plistlib.loads(v['ExtendedAttributes']) if 'ExtendedAttributes' in v else {}
            raw = attrs.get('com.apple.lastuseddate#PS')
            if raw:
                sec, nano = struct.unpack('<qq', raw)
                assert 0 <= nano < 10**9
                row['lastused_hex'] = raw.hex()
                native_date = dt.datetime.fromtimestamp(sec, dt.timezone.utc).astimezone(TZ)
                offset = native_date.strftime('%z')
                row['lastused_paris'] = native_date.strftime('%Y-%m-%dT%H:%M:%S') + f'.{nano:09d}' + offset[:3] + ':' + offset[3:]
                row['lastused_in_window'] = START <= sec+nano/1e9 <= END
            d['pdf_objects'].append(row)
        if marker:
            d['system_marker_candidates'].append(row)
        if native:
            d['protection_classes'].append(row)
    con.close()
    d['pdf_summary'] = {
        'objects': len(d['pdf_objects']),
        'lastused_in_window': sum(x.get('lastused_in_window', False) for x in d['pdf_objects']),
        'status_change_in_window': sum(START <= x['LastStatusChange'] <= END for x in d['pdf_objects']),
        'birth_in_window': sum(START <= x['Birth'] <= END for x in d['pdf_objects']),
    }
out['firstunlock_app_markers'] = []
for p in (B / 'complement-natif-v2/files').rglob('.FirstUnlock'):
    v = plistlib.loads(load(p))
    objects = v['$objects']
    decoded = unarchive(v['$top']['root'], objects)
    out['firstunlock_app_markers'].append({'source': str(p), 'decoded': decoded})
out['queries'] = queries
out['sources'] = [{'path': str(p), 'sha256_before': h, 'sha256_after': sha(p), 'unchanged': h == sha(p)} for p, h in sources.items()]
out['all_sources_unchanged'] = all(x['unchanged'] for x in out['sources'])
def encode(v):
    if isinstance(v, dt.datetime):
        return v.isoformat()
    if isinstance(v, bytes):
        return {'hex': v.hex()}
    raise TypeError(type(v).__name__)
print(json.dumps(out, ensure_ascii=False, indent=2, default=encode))
