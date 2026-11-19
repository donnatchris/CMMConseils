"""Vérifie les cinq transactions Fichiers et leur protection, sans écriture source."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import plistlib
import sqlite3
from zoneinfo import ZoneInfo

TZ = ZoneInfo('Europe/Paris')
P = Path('/media/shared/codeProjects/DMMConseils')
Q = P / 'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive'
root = Path('/home/sansforensics/analysis/tp03-20261110/files')
rel = 'com.apple.DocumentsApp/.tipkit/tips-store.db'
path = root / 'AppDomainGroup-group.com.apple.tipsnext' / rel
def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()
before = sha(path)
wal = Path(str(path)+'-wal')
assert not wal.exists() or wal.stat().st_size == 0
c = sqlite3.connect(path.as_uri()+'?mode=ro&immutable=1', uri=True)
c.row_factory = sqlite3.Row
sql = '''select c.*,p.Z_NAME entity_name from ACHANGE c
 left join Z_PRIMARYKEY p on c.ZENTITY=p.Z_ENT
 where c.ZTRANSACTIONID between 254 and 258 order by c.Z_PK'''
changes = [dict(x) for x in c.execute(sql)]
records = {t: [dict(x) for x in c.execute('select * from '+t)] for t in ['ZCOREDONATIONRECORD','ZCOREEVENTRECORD','ZCORETIPRECORD']}
c.close()
m = Q/'TP-03/Manifest.db'
mh = sha(m)
c = sqlite3.connect(m.as_uri()+'?mode=ro&immutable=1', uri=True)
rows = []
for fid, domain, blob in c.execute('select fileID,domain,file from Files where relativePath=? and flags=1', (rel,)):
    p = plistlib.loads(blob); v = p['$objects'][p['$top']['root'].data]
    rows.append({'fileID':fid, 'domain':domain, 'relativePath':rel, **{k:v.get(k) for k in ['ProtectionClass','Birth','LastModified','LastStatusChange','Size']}})
c.close()
out = {'source':str(path), 'sha256_before':before, 'sha256_after':sha(path),
       'manifest_sha256_before':mh, 'manifest_sha256_after':sha(m), 'manifest_entry':rows,
       'sql':sql,'changes':changes,'current_records':records,
       'firstunlock_in_extracted_sets':[]}
for phone,base in [('TP-03',root),('TP-02',P/'telephones/recherche-TP-02/extraction-systeme-20261014/files')]:
    for group in ['group.com.apple.shortcuts','group.is.workflow.my.app']:
        p = base / ('AppDomainGroup-'+group) / '.FirstUnlock'
        row = {'phone':phone,'source':str(p),'present_in_extracted_set':p.exists()}
        if p.exists():
            h = sha(p); v = plistlib.loads(p.read_bytes()); obj = v['$objects'][v['$top']['root'].data]
            row.update({'NSDate_seconds':obj['NS.time'],'paris':dt.datetime.fromtimestamp(obj['NS.time']+978307200, dt.timezone.utc).astimezone(TZ).isoformat(), 'sha256':h,'unchanged':h==sha(p)})
        out['firstunlock_in_extracted_sets'].append(row)
def encode(v):
    if isinstance(v,bytes): return {'hex':v.hex()}
    raise TypeError(type(v).__name__)
print(json.dumps(out,ensure_ascii=False,indent=2,default=encode))
