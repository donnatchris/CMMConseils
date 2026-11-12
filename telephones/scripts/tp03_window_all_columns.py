#!/usr/bin/env python3
"""Broad numeric triage for 16 October, without timestamp column-name filter.

Only ordinary SQLite tables; candidates are not automatically activity evidence.
Usage: script GENERAL PRIORITY NEW_OUTPUT
"""
import collections
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import sys
from zoneinfo import ZoneInfo


def main():
    roots = [Path(x) for x in sys.argv[1:3]]
    out = Path(sys.argv[3])
    os.umask(0o077)
    out.mkdir(parents=True, exist_ok=False)
    paris = ZoneInfo('Europe/Paris')
    lo = dt.datetime(2024, 10, 16, tzinfo=paris).timestamp()
    hi = dt.datetime(2024, 10, 17, tzinfo=paris).timestamp()
    epochs = [('unix_s', 0, 1), ('unix_ms', 0, 1000), ('unix_us', 0, 1000000),
              ('unix_ns', 0, 1000000000), ('cocoa_s', 978307200, 1),
              ('cocoa_ns', 978307200, 1000000000)]
    errors, candidates, sources, seen = [], [], [], set()
    quote = lambda s: '"' + s.replace('"', '""') + '"'
    counters = collections.Counter()
    for root in roots:
        collection = json.loads((root / 'collection.json').read_text())
        for item in collection:
            rel = item['domain'] + '/' + item['relativePath']
            if rel in seen:
                continue
            seen.add(rel)
            path = root / 'files' / rel
            with path.open('rb') as f:
                if f.read(16) != b'SQLite format 3\x00':
                    continue
            counters['sqlite_files'] += 1
            tracked = [Path(str(path) + suffix) for suffix in ['', '-wal']]
            def hashes():
                result = {}
                for p in tracked:
                    if p.exists():
                        with p.open('rb') as f:
                            result[str(p)] = hashlib.file_digest(f, 'sha256').hexdigest()
                return result
            before = hashes()
            c = sqlite3.connect(path.as_uri() + '?mode=ro', uri=True)
            try:
                tables = c.execute("select name from sqlite_master where type='table' and sql not like 'CREATE VIRTUAL%'").fetchall()
                for (table,) in tables:
                    counters['ordinary_tables'] += 1
                    try:
                        cols = c.execute('pragma table_info(' + quote(table) + ')').fetchall()
                        for _, col, affinity, *_ in cols:
                            if any(s in affinity.upper() for s in ['BLOB', 'CHAR', 'TEXT', 'CLOB']):
                                continue
                            counters['numeric_or_unspecified_columns'] += 1
                            field = quote(col)
                            stem = ' from ' + quote(table) + ' where typeof(' + field + ") in ('real','integer')"
                            sql = 'select min(' + field + '),max(' + field + ')' + stem
                            minimum, maximum = c.execute(sql).fetchone()
                            if minimum is None:
                                continue
                            for label, epoch, scale in epochs:
                                low, high = (lo - epoch) * scale, (hi - epoch) * scale
                                if maximum < low or minimum >= high:
                                    continue
                                q = ('select ' + field + ',count(*)' + stem + ' and ' + field + '>=? and ' + field + '<? group by ' + field)
                                for value, count in c.execute(q, (low, high)):
                                    instant = value / scale + epoch
                                    candidates.append({'path': rel, 'table': table, 'column': col,
                                                       'hypothesis': label, 'raw': value, 'count': count,
                                                       'paris': dt.datetime.fromtimestamp(instant, dt.timezone.utc).astimezone(paris).isoformat()})
                    except Exception as e:
                        errors.append({'path': rel, 'table': table, 'error': str(e)})
                after = hashes()
                if before != after:
                    raise RuntimeError('Database/WAL changed')
                sources.append({'path': str(path), 'before': before, 'after': after})
            finally:
                c.close()
            if counters['sqlite_files'] % 100 == 0:
                print(json.dumps(dict(counters)), flush=True)
    for name, data in [('candidates', candidates), ('sources', sources), ('errors', errors), ('counts', dict(counters))]:
        (out / (name + '.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'counts': dict(counters), 'candidate_values': len(candidates), 'query_errors': len(errors)}))


if __name__ == '__main__':
    main()
