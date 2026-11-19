#!/usr/bin/env python3
"""TP-02: inventory, selective decryption, signature/schema/time candidate triage.
No timestamp candidate is labelled a human interaction. Passwords only via TTY.
"""
import argparse
import csv
import datetime as dt
import getpass
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import plistlib
import re
import sqlite3
import sys
import tempfile
import shutil
from zoneinfo import ZoneInfo

BASE = Path('/mnt/data/forensic/SADEDINE-2026')
BACKUP = BASE / 'TP-02/00008110-001C69A002BA801E'
MANIFEST = BASE / 'ANALYSES/TP-02/Manifest-decrypted.db'
APPS = {'AppDomain-com.lscsmartconnection.smart', 'AppDomain-com.xiaomi.mihome',
        'AppDomainGroup-group.com.xiaomi.mihome'}
PARIS = ZoneInfo('Europe/Paris')
START = dt.datetime(2024, 10, 15, 13, 30, tzinfo=PARIS).astimezone(dt.timezone.utc)
END = dt.datetime(2024, 10, 28, 19, 20, tzinfo=PARIS).astimezone(dt.timezone.utc)
EXTSTART = dt.datetime(2024, 10, 1, tzinfo=PARIS).astimezone(dt.timezone.utc)
EXTEND = dt.datetime(2024, 11, 16, tzinfo=PARIS).astimezone(dt.timezone.utc)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''): h.update(b)
    return h.hexdigest()


def ro(path):
    return sqlite3.connect(Path(path).resolve().as_uri() + '?mode=ro&immutable=1', uri=True)


def write_csv(path, rows, fields):
    with Path(path).open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def safe(root, domain, relative):
    for val in (domain, relative):
        p = PurePosixPath(val)
        if p.is_absolute() or '..' in p.parts or '\\' in val or '\x00' in val:
            raise ValueError('unsafe logical path')
    if '/' in domain or not domain or not relative:
        raise ValueError('invalid domain/path')
    target = root / domain / relative
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError('path escapes output')
    return target


def classify(domain, path, flags):
    p = path.lower()
    name = PurePosixPath(p).name
    if flags != 1: return 'non_regular_entry', 9, 'not selected for decryption'
    if p.endswith(('-wal', '-shm', '-journal')):
        return 'sqlite_companion_candidate', 1, 'preserve alongside database'
    if re.search(r'\.(db|sqlite|sqlite3|sqlitedb)(\.|$)', name):
        return 'sqlite_candidate', 1, 'verify decrypted signature'
    if p.endswith('.plist'):
        return 'plist_candidate', 1 if domain in APPS or re.search('wifi|network|lockdown|springboard|mobileinstallation', p) else 2, 'configuration or dated fields; may contain secrets'
    if re.search(r'\.(log|ips|trace|jsonl)$', p) or re.search(r'(^|/)(logs?|otpubsublog|mjflog)(/|$)', p):
        return 'log_candidate', 1, 'dated records possible; coverage unverified'
    if '/attachments/' not in p and not re.search(r'\.(png|jpe?g|heic|mov|mp4|gif|webp|pdf|zip)$', p) and re.search('knowledgec|interaction|sms|callhistory|history|photos.sqlite|netusage|datausage|aggregate|currentpower|analytics', p):
        return 'activity_candidate', 1, 'activity source candidate, not proof'
    if domain in APPS and not re.search(r'\.(png|jpe?g|gif|webp|heic|mp4|mov|js|css|html|ttf|woff2?|otf|svg|map|bundle)$', p):
        return 'unclassified_data_candidate', 2, 'include extensionless data; signature unknown'
    return 'other_entry', 3, 'retained for exhaustive scoped inventory'


def inventory(args):
    out = Path(args.out); out.mkdir(parents=True, exist_ok=False)
    rows = []
    with ro(args.manifest) as c:
        for fid, domain, path, flags, blob in c.execute('SELECT fileID,domain,relativePath,flags,file FROM Files ORDER BY domain,relativePath'):
            # All non-App domains plus native Apple apps; all three camera domains.
            if domain not in APPS and domain.startswith('App') and not re.search(r'(^AppDomain-com\.apple\.|^AppDomainGroup-group\.com\.apple\.)', domain): continue
            kind, priority, reason = classify(domain, path, flags)
            row = dict(domain=domain, relativePath=path, fileID=fid, flags=flags,
                       presumed_type=kind, priority=priority, reason=reason,
                       size='', birth_raw='', modified_raw='', status_change_raw='', metadata_status='')
            try:
                p = plistlib.loads(blob)
                obj = p['$objects'][p['$top']['root'].data]
                for key, dest in [('Size','size'),('Birth','birth_raw'),('LastModified','modified_raw'),('LastStatusChange','status_change_raw')]:
                    row[dest] = obj.get(key, '')
                row['metadata_status'] = 'decoded selected MBFile fields only'
            except Exception as e: row['metadata_status'] = type(e).__name__
            rows.append(row)
    # Raise companions to same priority as their base if identifiable.
    idx = {(r['domain'],r['relativePath']):r for r in rows}
    for r in rows:
        for suffix in ('-wal','-shm','-journal'):
            if r['relativePath'].endswith(suffix):
                base = idx.get((r['domain'],r['relativePath'][:-len(suffix)]))
                if base: base['priority'] = min(base['priority'],r['priority'])
    fields = list(rows[0]) if rows else ['domain','relativePath','fileID','priority']
    write_csv(out/'inventory.csv',rows,fields)
    write_csv(out/'interesting-files.csv',[r for r in rows if int(r['priority'])<=2],fields)
    metadata=[]
    for r in rows:
        if int(r['priority'])>2:continue
        for field in ('birth_raw','modified_raw','status_change_raw'):
            try:
                date=dt.datetime.fromtimestamp(float(r[field]),dt.timezone.utc)
                if not EXTSTART<=date<EXTEND:continue
            except (ValueError,TypeError,OverflowError,OSError):continue
            metadata.append(dict(domain=r['domain'],relativePath=r['relativePath'],fileID=r['fileID'],field=field,raw_value=r[field],
                format_hypothesis='MBFile Unix seconds; validate against content',utc=date.isoformat(),paris=date.astimezone(PARIS).isoformat(),
                central_window=START<=date<=END,interpretation='snapshot metadata; not a historical operation or human interaction'))
    write_csv(out/'metadata-time-candidates.csv',sorted(metadata,key=lambda r:r['utc']),
              ['domain','relativePath','fileID','field','raw_value','format_hypothesis','utc','paris','central_window','interpretation'])
    counts = {}
    for r in rows:
        k = f"{r['domain']}|{r['presumed_type']}|P{r['priority']}"
        counts[k] = counts.get(k,0)+1
    summary = {'source':str(args.manifest),'manifest_sha256':sha(args.manifest),
               'rows':len(rows),'interesting_files':sum(int(r['priority'])<=2 for r in rows),'metadata_time_candidates':len(metadata),'counts':counts,'scope':'all non-App domains, native Apple apps and camera apps',
               'types':'presumed from paths only; encrypted content signatures not verified',
               'metadata':'raw MBFile fields, not human activity events'}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'inventory_rows':len(rows),'priority_1_files':sum(r['priority']==1 for r in rows)}))


def selection(args):
    with open(args.inventory,newline='') as f: rows=list(csv.DictReader(f))
    ids = set(args.file_id or [])
    chosen = [r for r in rows if int(r['flags'])==1 and
              (r['fileID'] in ids if ids else int(r['priority'])<=args.max_priority) and
              (not args.domain or r['domain'] in args.domain) and
              (not args.max_file_bytes or int(r['size'] or 0)<=args.max_file_bytes)]
    # Automatically include WAL/SHM/journal for any selected base, even with --file-id.
    selected={(r['domain'],r['relativePath']) for r in chosen}
    for r in rows:
        if int(r['flags'])==1 and any(r['relativePath'].endswith(x) and (r['domain'],r['relativePath'][:-len(x)]) in selected for x in ('-wal','-shm','-journal')) and r not in chosen:
            chosen.append(r)
    return chosen


def extract(args):
    rows = selection(args)
    total = sum(int(r['size'] or 0) for r in rows)
    print(json.dumps({'selected_files':len(rows),'plaintext_size_estimate':total,'dry_run':args.dry_run}))
    if total > args.max_bytes: raise SystemExit('Selection exceeds --max-bytes; refine selection or increase explicitly.')
    if args.dry_run or not rows: return
    if not sys.stdin.isatty(): raise SystemExit('Interactive TTY required for password; no password via CLI/env/log.')
    root = Path(args.out).resolve()
    backup_path = Path(args.backup).resolve()
    if root.is_relative_to(backup_path) or backup_path.is_relative_to(root): raise SystemExit('Output must be separate from original backup.')
    # Create a fresh case run and validate ALL paths before obtaining password.
    root.mkdir(parents=True, exist_ok=False)
    for r in rows: safe(root/'files',r['domain'],r['relativePath'])
    from iphone_backup_decrypt import EncryptedBackup
    password = getpass.getpass('Mot de passe de la sauvegarde TP-02 : ')
    backup = EncryptedBackup(backup_directory=str(backup_path),passphrase=password)
    del password
    logpath=root/'extraction.jsonl'
    with logpath.open('a') as log:
        try:
            backup.test_decryption()
            with backup.manifest_db_cursor() as cursor:
                for r in rows:
                    entry={k:r[k] for k in ('domain','relativePath','fileID')}
                    entry['extracted_utc']=dt.datetime.now(dt.timezone.utc).isoformat()
                    try:
                        fid=r['fileID']
                        if not re.fullmatch('[0-9a-f]{40}',fid): raise ValueError('invalid fileID')
                        # Verify against the library's own decrypted manifest: exact identifiers.
                        found=cursor.execute('SELECT fileID FROM Files WHERE domain=? AND relativePath=? AND flags=1',(r['domain'],r['relativePath'])).fetchall()
                        if found!=[(fid,)]: raise ValueError('manifest mismatch or ambiguous identity')
                        matches=cursor.execute('SELECT fileID FROM Files WHERE domain LIKE ? AND relativePath=? AND flags=1 ORDER BY domain,relativePath LIMIT 1',(r['domain'],r['relativePath'])).fetchone()
                        if matches!=(fid,): raise ValueError('library LIKE selector ambiguous')
                        src=backup_path/fid[:2]/fid
                        if not src.is_file(): src=backup_path/fid
                        entry['ciphertext_sha256']=sha(src)
                        dst=safe(root/'files',r['domain'],r['relativePath']); dst.parent.mkdir(parents=True,exist_ok=True)
                        with tempfile.NamedTemporaryFile(prefix='.tp02-',suffix='.partial',dir=dst.parent,delete=False) as temporary:
                            partial=Path(temporary.name)
                        backup.extract_file(relative_path=r['relativePath'],domain_like=r['domain'],output_filename=str(partial))
                        if r['size'] and partial.stat().st_size!=int(r['size']):
                            entry['warning']='plaintext size differs from manifest; retained for investigation'
                        partial.rename(dst)
                        entry.update(status='ok',output=str(dst),size=dst.stat().st_size,sha256=sha(dst))
                    except Exception as e:
                        # Exception message intentionally omitted: may contain sensitive material.
                        entry.update(status='error',error_class=type(e).__name__)
                    log.write(json.dumps(entry,ensure_ascii=False)+'\n');log.flush()
        except Exception as e:
            log.write(json.dumps({'status':'initialization_error','error_class':type(e).__name__})+'\n')
            raise SystemExit('Decryption initialization failed; see sanitized log.') from None
    print('Extraction completed; inspect statuses in '+str(logpath))


def quote(name): return '"'+name.replace('"','""')+'"'


def times(value):
    """Return explicit hypotheses only; epoch/unit requires source validation."""
    results=[]
    if isinstance(value,(int,float)) and not isinstance(value,bool):
        for label,divisor,offset in [('unix_seconds',1,0),('unix_milliseconds',1000,0),('unix_microseconds',1e6,0),('unix_nanoseconds',1e9,0),('apple_seconds',1,978307200),('apple_nanoseconds',1e9,978307200)]:
            try:
                d=dt.datetime.fromtimestamp(value/divisor+offset,dt.timezone.utc)
                if EXTSTART <= d < EXTEND:results.append((label,d))
            except (ValueError,OverflowError,OSError): pass
    elif isinstance(value,str) and len(value)<100:
        if re.fullmatch(r'-?\d+(\.\d+)?',value): return times(float(value) if '.' in value else int(value))
        try:
            normalized=re.sub(r' (?=[+-]\d{2}:?\d{2}$)','',value.replace('Z','+00:00'))
            d=dt.datetime.fromisoformat(normalized)
            if d.tzinfo is not None:
                d=d.astimezone(dt.timezone.utc)
                if EXTSTART<=d<EXTEND:results.append(('ISO8601_explicit_offset',d))
        except ValueError: pass
    return results


def analyze(args):
    root=Path(args.extracted); out=Path(args.out);out.mkdir(parents=True,exist_ok=False)
    files=[]; schemas=[]; candidates=[]; errors=[]
    logs={}
    if (root/'extraction.jsonl').exists():
        for line in (root/'extraction.jsonl').read_text().splitlines():
            r=json.loads(line)
            if r.get('status')=='ok':logs[Path(r['output']).resolve()]=r
    for path in sorted((root/'files').rglob('*')):
        if not path.is_file() or path.name.endswith('.partial'):continue
        with path.open('rb') as f: sig=f.read(16)
        kind='sqlite' if sig==b'SQLite format 3\x00' else 'plist_candidate' if sig.startswith((b'bplist00',b'<?xml')) else 'other'
        entry={'file':str(path),'sha256':sha(path),'size':path.stat().st_size,'signature_type':kind,
               'fileID':logs.get(path.resolve(),{}).get('fileID','')}
        files.append(entry)
        if kind!='sqlite':continue
        # WAL replay only in private disposable copy, preserving extracted pieces.
        with tempfile.TemporaryDirectory(prefix='tp02-sqlite-') as temp:
            cp=Path(temp)/'database';shutil.copyfile(path,cp)
            for suffix in ('-wal','-shm','-journal'):
                companion=Path(str(path)+suffix)
                if companion.is_file():shutil.copyfile(companion,str(cp)+suffix)
            try:
                c=sqlite3.connect(str(cp));c.execute('PRAGMA query_only=ON')
                try: integrity=c.execute('PRAGMA quick_check').fetchall()
                except sqlite3.Error as error:
                    integrity=[['not_checked',type(error).__name__]]
                    errors.append({'file':str(path),'stage':'quick_check','error_class':type(error).__name__})
                schema={'file':str(path),'integrity':integrity,'tables':[],'wal_present':Path(str(path)+'-wal').is_file()}
                tables=c.execute("SELECT name,sql FROM sqlite_master WHERE type='table'").fetchall()
                for table,sql in tables:
                    ti={'name':table,'sql':sql,'columns':[],'total_rows':None,'rows_scanned':0,'truncated':False}
                    schema['tables'].append(ti)
                    try:
                        columns=c.execute('PRAGMA table_info('+quote(table)+')').fetchall()
                        ti['columns']=columns
                    except sqlite3.Error as error:
                        ti['column_error']=type(error).__name__
                        errors.append({'file':str(path),'table':table,'stage':'columns','error_class':type(error).__name__})
                        continue
                    try:ti['total_rows']=c.execute('SELECT COUNT(*) FROM '+quote(table)+' NOT INDEXED').fetchone()[0]
                    except sqlite3.Error as error:
                        ti['count_error']=type(error).__name__
                        errors.append({'file':str(path),'table':table,'stage':'count','error_class':type(error).__name__})
                    # Time-like column names only. Raw cells never echoed to console.
                    temporal=[x[1] for x in columns if re.search(r'time|date|timestamp|created|modified|access|birth|lastseen',x[1],re.I)]
                    if not temporal:continue
                    has_rowid=True
                    try: c.execute('SELECT _rowid_ FROM '+quote(table)+' LIMIT 0')
                    except sqlite3.Error:has_rowid=False
                    query='SELECT '+('_rowid_,' if has_rowid else '')+','.join(quote(x) for x in temporal)+' FROM '+quote(table)+' NOT INDEXED LIMIT ?'
                    try:
                        for ordinal,values in enumerate(c.execute(query,(args.row_limit+1,))):
                            if ordinal>=args.row_limit:ti['truncated']=True;break
                            ti['rows_scanned']+=1
                            rowid=values[0] if has_rowid else ''
                            values=values[1:] if has_rowid else values
                            for col,value in zip(temporal,values):
                                for fmt,date in times(value):
                                    candidates.append({'file':str(path),'fileID':entry['fileID'],'table':table,'column':col,'scan_ordinal':ordinal,'sqlite_rowid':rowid,
                                        'raw_value':value,'format_hypothesis':fmt,'utc':date.isoformat(),'paris':date.astimezone(PARIS).isoformat(),
                                        'central_window':START<=date<=END,'interpretation':'temporal candidate only; source semantics not validated',
                                        'confidence':'unvalidated','locator_limit':'rowid retained when available; scan ordinal otherwise, requery source'})
                    except sqlite3.Error as e:errors.append({'file':str(path),'table':table,'error_class':type(e).__name__})
                schemas.append(schema);c.close()
            except sqlite3.Error as e:errors.append({'file':str(path),'error_class':type(e).__name__})
    write_csv(out/'decrypted-files.csv',files,['file','sha256','size','signature_type','fileID'])
    write_csv(out/'sqlite-inventory.csv',[r for r in files if r['signature_type']=='sqlite'],['file','sha256','size','signature_type','fileID'])
    (out/'sqlite-schema.json').write_text(json.dumps(schemas,ensure_ascii=False,indent=2)+'\n')
    fields=['file','fileID','table','column','scan_ordinal','sqlite_rowid','raw_value','format_hypothesis','utc','paris','central_window','interpretation','confidence','locator_limit']
    write_csv(out/'temporal-candidates.csv',sorted(candidates,key=lambda r:r['utc']),fields)
    status={'files_examined':len(files),'sqlite_verified':len(schemas),'candidates':len(candidates),'errors':errors,
            'status':'no_decrypted_files_available' if not files else 'triage_completed',
            'limits':['No automatic attribution or human-use inference','Epochs/units are hypotheses pending schema validation',
                      'Only time-like column names scanned; embedded blobs, plist values and logs not parsed',
                      'Row limits and parsing errors recorded; no claim of exhaustive chronology',
                      'Naive local date strings excluded until timezone established']}
    (out/'analysis-status.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in status.items() if k not in ('errors','limits')}))


def main():
    os.umask(0o077)
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='command',required=True)
    i=s.add_parser('inventory');i.add_argument('--manifest',default=str(MANIFEST));i.add_argument('--out',required=True);i.set_defaults(fn=inventory)
    e=s.add_parser('extract');e.add_argument('--inventory',required=True);e.add_argument('--backup',default=str(BACKUP));e.add_argument('--out',required=True)
    e.add_argument('--max-priority',type=int,default=1);e.add_argument('--max-bytes',type=int,default=1024**3)
    e.add_argument('--max-file-bytes',type=int,default=0);e.add_argument('--domain',action='append');e.add_argument('--file-id',action='append');e.add_argument('--dry-run',action='store_true');e.set_defaults(fn=extract)
    a=s.add_parser('analyze');a.add_argument('--extracted',required=True);a.add_argument('--out',required=True);a.add_argument('--row-limit',type=int,default=100000);a.set_defaults(fn=analyze)
    args=p.parse_args();args.fn(args)
if __name__=='__main__':main()
