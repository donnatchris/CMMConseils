#!/usr/bin/env python3
"""Read-only content check of the L16B image mount. JSON on stdout only."""
from pathlib import Path
import base64, collections, csv, datetime, email.policy, hashlib, io, json, re, subprocess, zipfile
from email.parser import BytesParser

ROOT = Path('/mnt/windows')
mount = subprocess.check_output(['findmnt', '-rn', '-o', 'OPTIONS', str(ROOT)], text=True).strip()
if 'ro' not in mount.split(','):
    raise RuntimeError('Expected read-only image mount')

def sha_file(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(4*1024*1024), b''): h.update(block)
    return h.hexdigest()

files = sorted(p for p in (ROOT/'L16B').rglob('*') if p.is_file())
inventory = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size} for p in files]
targets = [p for p in files if p.suffix.lower() == '.pst' or '/SAGE/' in str(p) or '/SHINE/' in str(p) or 'takeout-' in p.name.lower()]
before = {str(p.relative_to(ROOT)): sha_file(p) for p in targets}
archives = []
for p in targets:
    if p.suffix.lower() != '.zip': continue
    row = {'path': str(p.relative_to(ROOT)), 'members': [], 'errors': []}
    with zipfile.ZipFile(p) as z:
        for info in z.infolist():
            try:
                data = z.read(info)
                item = {'name': info.filename, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
                row['members'].append(item)
                if '/SHINE/' in str(p) and info.filename.lower().endswith('.csv'):
                    text = data.decode('utf-8-sig')
                    dialect = csv.Sniffer().sniff(text[:8000], delimiters=',;\t')
                    rows = list(csv.DictReader(io.StringIO(text), dialect=dialect))
                    dates = []
                    for r in rows:
                        for k, val in r.items():
                            if 'date' not in str(k).lower() or not val: continue
                            for fmt in ('%Y-%m-%d', '%d/%m/%Y', '%d-%m-%Y'):
                                try: dates.append(datetime.datetime.strptime(val[:10], fmt).date().isoformat()); break
                                except ValueError: pass
                    item['csv'] = {'columns': list(rows[0]) if rows else [], 'row_count': len(rows),
                                   'parsed_date_field_count': len(dates), 'min_date': min(dates) if dates else None,
                                   'max_date': max(dates) if dates else None,
                                   'date_fields_outside_pv_period': sum(not ('2023-01-01' <= d <= '2024-10-15') for d in dates)}
                if '/SHINE/' in str(p) and info.filename.lower().endswith('.ofx'):
                    text = data.decode('utf-8', errors='replace')
                    item['ofx'] = {'transaction_entries': text.count('<STMTTRN>'),
                                   'dates': {k: re.findall('<'+k+r'>([^<\r\n]+)', text) for k in ['DTSTART','DTEND']},
                                   'account_id_present': bool(re.search(r'<ACCTID>', text)),
                                   'note': 'Account identifiers and transaction descriptions not exported.'}
                if info.filename == 'Takeout/archive_browser.html':
                    item['expected_account_mentioned'] = b'rct93300@gmail.com' in data
            except Exception as ex:
                row['errors'].append({'member': info.filename, 'error': type(ex).__name__})
    archives.append(row)

eml = []
for p in files:
    if '/MESSAGERIES/' not in str(p) or p.suffix.lower() != '.eml': continue
    data = p.read_bytes(); msg = BytesParser(policy=email.policy.default).parsebytes(data)
    eml.append({'path': str(p.relative_to(ROOT)), 'sha256': hashlib.sha256(data).hexdigest(),
                'date_header': str(msg.get('Date', '')), 'has_from': bool(msg.get('From')),
                'has_to': bool(msg.get('To')), 'defects': [type(x).__name__ for x in msg.defects]})

after = {str(p.relative_to(ROOT)): sha_file(p) for p in targets}
print(json.dumps({'mount_options': mount, 'inventory': inventory,
                  'target_hashes_before': before, 'target_hashes_after': after,
                  'targets_unchanged': before == after, 'archives': archives, 'eml': eml}, ensure_ascii=False, indent=2))
