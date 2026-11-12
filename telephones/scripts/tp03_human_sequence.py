#!/usr/bin/env python3
"""Read-only deeper examination of TP-03 sequence; run on SIFT working copies.

Usage: tp03_human_sequence.py GENERAL PRIORITY NEW_OUTPUT [TP02_ROOT]
All SQL and hashes, including WALs, are recorded. No password or key material.
"""
import collections
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import plistlib
import sqlite3
import sys
from zoneinfo import ZoneInfo

P = ZoneInfo('Europe/Paris')
C = 978307200


def digest(p):
    with p.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def iso(t):
    if t is None:
        return None
    try:
        return dt.datetime.fromtimestamp(t + C, dt.timezone.utc).astimezone(P).isoformat()
    except (ValueError, OverflowError):
        return None


def encode(v):
    if isinstance(v, bytes):
        result = {'bytes': len(v), 'sha256': hashlib.sha256(v).hexdigest()}
        try:
            result['plist'] = plistlib.loads(v)
        except Exception:
            try:
                result['utf8'] = v.decode('utf-8')
            except UnicodeError:
                result['hex'] = v.hex()
        return result
    if isinstance(v, (dt.datetime, plistlib.UID)):
        return str(v)
    raise TypeError(type(v).__name__)


def main():
    general, priority, out = map(Path, sys.argv[1:4])
    tp02 = Path(sys.argv[4]) if len(sys.argv) > 4 else None
    os.umask(0o077)
    out.mkdir(parents=True, exist_ok=False)
    sources, errors, result = [], [], {}

    def query(root, rel, sql, args=()):
        p = root / 'files' / rel
        tracked = [Path(str(p) + suffix) for suffix in ['', '-wal', '-shm']]
        before = {str(x): digest(x) for x in tracked if x.is_file()}
        try:
            c = sqlite3.connect(p.as_uri() + '?mode=ro', uri=True)
            c.row_factory = sqlite3.Row
            try:
                rows = [dict(r) for r in c.execute(sql, args)]
            finally:
                c.close()
        except Exception as e:
            errors.append({'path': str(p), 'sql': sql, 'error': str(e)})
            rows = []
        after = {str(x): digest(x) for x in tracked if x.is_file()}
        # SHM is a transient reader coordination structure; database/WAL are evidence copies.
        stable = all(after.get(k) == v for k, v in before.items() if not k.endswith('-shm'))
        sources.append({'path': str(p), 'sql': sql, 'args': args, 'before': before,
                        'after': after, 'db_wal_unchanged': stable})
        if not stable:
            raise RuntimeError('Database/WAL changed')
        return rows

    tip = 'AppDomainGroup-group.com.apple.tipsnext/com.apple.MobileSMS/.tipkit/tips-store.db'
    pa = 'HomeDomain/Library/Accessibility/com.apple.personalaudio.sqlite'
    q = lambda rel, sql, args=(): query(general, rel, sql, args)
    result['tipkit_tables'] = {}
    for table in ['Z_PRIMARYKEY', 'ZCORETIPRECORD', 'ZCORERULERECORD',
                  'ZCOREPARAMETERRECORD', 'ZCOREEVENTRECORD', 'ZCOREDONATIONRECORD']:
        result['tipkit_tables'][table] = q(tip, 'select * from ' + table)
    txsql = '''select t.*, a.ZNAME author_name,b.ZNAME bundle_name,
        n.ZNAME context_name,p.ZNAME process_name from ATRANSACTION t
        left join ATRANSACTIONSTRING a on a.Z_PK=t.ZAUTHORTS
        left join ATRANSACTIONSTRING b on b.Z_PK=t.ZBUNDLEIDTS
        left join ATRANSACTIONSTRING n on n.Z_PK=t.ZCONTEXTNAMETS
        left join ATRANSACTIONSTRING p on p.Z_PK=t.ZPROCESSIDTS'''
    result['tipkit_transactions'] = q(tip, txsql + ' order by t.Z_PK')
    for x in result['tipkit_transactions']:
        x['paris'] = iso(x['ZTIMESTAMP'])
    result['tipkit_changes_target'] = q(tip, '''select c.*,p.Z_NAME entity_name
        from ACHANGE c left join Z_PRIMARYKEY p on p.Z_ENT=c.ZENTITY
        where ZTRANSACTIONID between 1217 and 1224 order by c.Z_PK''')
    result['tipkit_change_patterns'] = q(tip, '''select c.ZTRANSACTIONID,p.Z_NAME entity_name,
        c.ZCHANGETYPE,count(*) n from ACHANGE c left join Z_PRIMARYKEY p on p.Z_ENT=c.ZENTITY
        group by c.ZTRANSACTIONID,p.Z_NAME,c.ZCHANGETYPE order by c.ZTRANSACTIONID''')
    result['pa_events'] = q(pa, '''select Z_PK,ZCLOUDKITEVENTTYPE,ZCOUNTAFFECTEDOBJECTS,
        ZCOUNTFINISHEDOBJECTS,ZERRORCODE,ZSUCCEEDED,ZSTARTEDAT,ZENDEDAT,ZERRORDOMAIN
        from ANSCKEVENT order by Z_PK''')
    for x in result['pa_events']:
        x['start_paris'], x['end_paris'] = iso(x['ZSTARTEDAT']), iso(x['ZENDEDAT'])
    result['pa_transactions'] = q(pa, txsql + ' order by t.Z_PK')
    for x in result['pa_transactions']:
        x['paris'] = iso(x['ZTIMESTAMP'])
    result['pa_settings_counts'] = q(pa, 'select count(*) n from ZPERSONALAUDIOSETTINGS')
    result['pa_settings_metadata'] = q(pa, 'select Z_PK,ZVERSION,length(ZAUDIOSETTINGS) audio_bytes from ZPERSONALAUDIOSETTINGS')

    hs = 'HealthDomain/Health/healthdb_secure.sqlite'
    sql = '''select s.data_id,s.data_type,s.start_date,s.end_date,o.creation_date,o.provenance
        from samples s join objects o using(data_id)'''
    health = query(priority, hs, sql + ' where s.data_id between 348290 and 348370 order by s.data_id')
    for x in health:
        for k in ['start_date', 'end_date', 'creation_date']:
            x[k + '_paris'] = iso(x[k])
        x['creation_delay_seconds'] = x['creation_date'] - x['end_date']
    result['health_neighbors'] = health
    result['health_delay_distribution'] = query(priority, hs, '''select s.data_type,o.provenance,
        cast((o.creation_date-s.end_date)/3600 as integer) delay_hours,count(*) n,
        min(o.creation_date-s.end_date) delay_min,max(o.creation_date-s.end_date) delay_max
        from samples s join objects o using(data_id) where o.provenance=166
        group by s.data_type,o.provenance,delay_hours order by s.data_type,delay_hours''')
    result['health_schema'] = query(priority, hs, "select name,sql from sqlite_master where type='table'")
    # Sources which could corroborate an intentional action; ranges expose retention limits.
    central_start = dt.datetime(2024, 10, 15, 14, 19, tzinfo=P).timestamp() - C
    central_end = dt.datetime(2024, 10, 28, 11, 30, tzinfo=P).timestamp() - C
    result['corroboration_schemas'] = {}
    for rel in ['HomeDomain/Library/CoreDuet/People/interactionC.db',
                'WirelessDomain/Library/Databases/DataUsage.sqlite',
                'WirelessDomain/Library/Databases/CellularUsage.db',
                'HomeDomain/Library/Safari/History.db',
                'HomeDomain/Library/Safari/BrowserState.db',
                'RootDomain/Library/Caches/locationd/consolidated.db']:
        result['corroboration_schemas'][rel] = q(rel, "select name,sql from sqlite_master where type='table'")
    result['safari_history_range'] = q('HomeDomain/Library/Safari/History.db',
        'select count(*) n,min(visit_time) first,max(visit_time) last from history_visits')
    result['safari_visits_sealed'] = q('HomeDomain/Library/Safari/History.db',
        'select id,visit_time from history_visits where visit_time between ? and ?', (central_start, central_end))
    result['preferences'] = []
    for name in ['com.apple.springboard.plist', 'com.apple.backboardd.plist',
                 'com.apple.biometrickitd.plist', 'com.apple.ScreenTimeAgent.plist',
                 'com.apple.UsageTrackingAgent.plist', 'com.apple.timed.plist',
                 'com.apple.duetactivityscheduler.plist', 'com.apple.routined.plist',
                 'com.apple.mobiletimerd.plist', 'com.apple.osanalytics.addaily.plist']:
        p = general / 'files/HomeDomain/Library/Preferences' / name
        try:
            result['preferences'].append({'path': str(p), 'sha256': digest(p),
                                          'value': plistlib.loads(p.read_bytes())})
        except Exception as e:
            errors.append({'path': str(p), 'error': str(e)})
    if tp02:
        result['tp02_tipkit_schema'] = query(tp02, tip, "select name,sql from sqlite_master where type='table'")
        result['tp02_tipkit_transactions'] = query(tp02, tip, txsql + ' order by t.Z_PK')
        result['tp02_pa_target'] = query(tp02, pa, '''select Z_PK,ZCLOUDKITEVENTTYPE,ZERRORCODE,
            ZSUCCEEDED,ZSTARTEDAT,ZENDEDAT,ZERRORDOMAIN from ANSCKEVENT
            where ZSTARTEDAT between ? and ?''', (central_start, central_end))
    for name, value in [('results', result), ('sources', sources), ('errors', errors)]:
        (out / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2, default=encode) + '\n')
    print(json.dumps({'output': str(out), 'queries': len(sources), 'errors': len(errors),
                      'tip_transactions': len(result['tipkit_transactions']), 'pa_events': len(result['pa_events'])}))


if __name__ == '__main__':
    main()
