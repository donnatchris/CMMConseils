#!/usr/bin/env python3
"""Q1, lecture seule des preuves et exports neufs. À exécuter sur SIFT."""
import argparse
import collections
import csv
import datetime as dt
import hashlib
import json
from pathlib import Path, PureWindowsPath
import plistlib
import shutil
import sqlite3
import subprocess
from zoneinfo import ZoneInfo


def digest(p, algorithm='sha256'):
    h = hashlib.new(algorithm)
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''):
            h.update(block)
    return h.hexdigest()


def dated(v):
    if v is None:
        return None
    return dt.datetime.fromtimestamp(v, dt.timezone.utc).astimezone(ZoneInfo('Europe/Paris')).isoformat()


def plain(v, objects, seen=()):
    if isinstance(v, plistlib.UID):
        if v.data in seen:
            return {'reference': v.data}
        return plain(objects[v.data], objects, seen + (v.data,))
    if isinstance(v, dict):
        return {k: plain(x, objects, seen) for k, x in v.items()}
    if isinstance(v, list):
        return [plain(x, objects, seen) for x in v]
    if isinstance(v, bytes):
        return {'hex': v.hex()}
    if isinstance(v, dt.datetime):
        return v.isoformat()
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('project', type=Path)
    ap.add_argument('out', type=Path)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=False, mode=0o700)
    p = a.project
    inv = p / 'inventaire-DNEF/documents-recus/Inventaire_saddedine.csv'
    with inv.open(newline='', encoding='utf-8-sig') as f:
        inventory = [dict(line=i, path=r[0], creation=r[1], modification=r[2], access=r[3], sha512=r[4])
                     for i, r in enumerate(csv.reader(f, delimiter=';'), 1)
                     if len(r) == 5 and r[0].startswith('C:\\L16B\\TELEPHONES\\IPHONE13_MINI\\')]
    assert len(inventory) == 27
    refs = {
        'TP-02': p / 'investigations/20261108-complement-pv/prive/comparaison-pdf-identites.json',
        'TP-03': p / 'telephones/recherche-TP-03/priorite/pdf-identities.json',
    }
    manifests = {
        'TP-02': Path('/media/shared/forensic/SADEDINE-2026/ANALYSES/TP-02/Manifest-decrypted.db'),
        'TP-03': Path('/home/sansforensics/analysis/tp03-20261110/Manifest.db'),
    }
    roots = {
        'TP-02': p / 'investigations/20261108-complement-pv/prive/pdf-extraits-20261109-essai8/files',
        'TP-03': Path('/home/sansforensics/analysis/tp03-priority-20261110/files'),
    }
    results = {'inventory_sha256': digest(inv), 'inventory': inventory, 'sources': {}, 'phones': {}}
    for phone in refs:
        ref = json.loads(refs[phone].read_text())
        unique = {x['fileID']: dict(x, expected_sha256=r['sha256']) for r in ref for x in r['matches']}
        work = a.out / phone
        work.mkdir()
        source_parts = [Path(str(manifests[phone]) + s) for s in ('', '-wal', '-shm')]
        before = {str(q): digest(q) for q in source_parts if q.exists()}
        for q in source_parts:
            if q.exists():
                shutil.copyfile(q, work / ('Manifest.db' + str(q)[len(str(manifests[phone])):]))
        after = {str(q): digest(q) for q in source_parts if q.exists()}
        assert before == after, 'Source changed during copy'
        con = sqlite3.connect((work / 'Manifest.db').as_uri() + '?mode=ro', uri=True)
        assert con.execute('pragma quick_check').fetchone()[0] == 'ok'
        results['sources'][phone] = {'before': before, 'after': after, 'reference_sha256': digest(refs[phone])}
        records = []
        for fid, x in sorted(unique.items()):
            domain, relative, flags, blob = con.execute('select domain,relativePath,flags,file from Files where fileID=?', (fid,)).fetchone()
            assert (domain, relative, flags) == (x['domain'], x['relativePath'], 1)
            assert hashlib.sha1((domain + '-' + relative).encode()).hexdigest() == fid
            pl = plistlib.loads(blob)
            obj = pl['$objects'][pl['$top']['root'].data]
            (work / (fid + '.plist')).write_bytes(blob)
            pdf = roots[phone] / domain / relative
            h256, h512 = digest(pdf), digest(pdf, 'sha512')
            assert h256 == x['expected_sha256']
            matches = [r for r in inventory if r['sha512'].lower() == h512]
            assert matches, 'No SHA-512 DNEF match'
            info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True, check=True).stdout
            metadata = {}
            for line in info.splitlines():
                k, sep, v = line.partition(':')
                if sep and k in ('Creator', 'Producer', 'CreationDate', 'ModDate', 'Pages'):
                    metadata[k] = v.strip()
            records.append(dict(phone=phone, fileID=fid, domain=domain, relativePath=relative,
                                sha256=h256, sha512=h512, bytes=pdf.stat().st_size,
                                birth_raw=obj.get('Birth'), birth_paris=dated(obj.get('Birth')),
                                modified_paris=dated(obj.get('LastModified')),
                                status_change_paris=dated(obj.get('LastStatusChange')),
                                mbfile=plain(obj, pl['$objects']), pdf_metadata=metadata,
                                dnef_lines=[r['line'] for r in matches]))
        con.close()
        assert all(any(r['line'] in z['dnef_lines'] for z in records) for r in inventory)
        results['phones'][phone] = records
    results['summary'] = {k: dict(objects=len(v), distinct_sha512=len({r['sha512'] for r in v}),
                                 births=dict(collections.Counter(r['birth_paris'][:10] if r['birth_paris'] else None for r in v)),
                                 pdf_creators=dict(collections.Counter(r['pdf_metadata'].get('Creator') for r in v)))
                          for k, v in results['phones'].items()}
    results['summary']['inventory_distinct_sha512'] = len({r['sha512'] for r in inventory})
    (a.out / 'resultats.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(results['summary'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
