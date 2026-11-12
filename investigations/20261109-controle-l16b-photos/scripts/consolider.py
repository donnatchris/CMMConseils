#!/usr/bin/env python3
"""Compare local recorded inventories with a new read-only SIFT content check."""
from pathlib import Path
import collections, datetime, hashlib, json
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parents[1]
SRC = ROOT/'ordinateur/recherche-OP-01/extractions-acces'
hashes = {}
def read(p):
    data = p.read_bytes(); hashes[str(p.relative_to(ROOT))] = hashlib.sha256(data).hexdigest()
    return json.loads(data)

old = read(SRC/'l16b-inventory.json')
data = (SRC/'l16b-mft.jsonl').read_bytes()
hashes[str((SRC/'l16b-mft.jsonl').relative_to(ROOT))] = hashlib.sha256(data).hexdigest()
mft = [json.loads(x) for x in data.splitlines()]
live = read(OUT/'prive/controle-sift.json')
old_archives = read(SRC/'archives.json')
old_pst = read(ROOT/'ordinateur/recherche-OP-01/operations-28oct/resultats-sift/sources.json')
groups = collections.defaultdict(list)
later = []
for rec in mft:
    created = rec['FN'][0]['times']['creation']
    groups[rec['path'].split('/')[1]].append(created)
    if not created.startswith('2024-10-28'):
        later.append({'path': rec['path'], 'fn_creation_utc': created, 'si': rec['SI']})

def paris(t):
    return datetime.datetime.fromisoformat(t).astimezone(ZoneInfo('Europe/Paris')).isoformat()

expected_archive = {x['source']: x['sha256'] for x in old_archives}
expected_pst = {x['path']: x['sha256'] for x in old_pst if x['path'].lower().endswith('.pst')}
hash_compare = {p: {'sha256': h, 'prior_archive_hash_match': expected_archive.get(p) == h}
                for p, h in live['target_hashes_before'].items() if p in expected_archive}
current = {x['path']: x['bytes'] for x in live['inventory']}
prior = {x['path']: x['size'] for x in old}
report = {'file_count': len(current), 'bytes': sum(current.values()),
          'same_paths_and_sizes_as_recorded_inventory': current == prior,
          'groups': {g: {'files': len(ts), 'fn_creation_min_paris': paris(min(ts)),
                         'fn_creation_max_paris': paris(max(ts))} for g, ts in groups.items()},
          'later_fn_entries': later, 'live_targets_unchanged': live['targets_unchanged'],
          'live_target_sha256': live['target_hashes_before'], 'archive_hash_comparison': hash_compare,
          'pst_hash_comparison': {p: {'sha256': h, 'prior_hash_match': expected_pst.get(p) == h}
                                  for p, h in live['target_hashes_before'].items() if p.lower().endswith('.pst')},
          'eml_count': len(live['eml']),
          'eml_by_directory': dict(collections.Counter(x['path'].split('/')[2] for x in live['eml'])),
          'archive_summary': [{'path': x['path'], 'member_count': len(x['members']),
                              'member_extensions': dict(collections.Counter(Path(m['name']).suffix.lower() for m in x['members'])),
                              'errors': x['errors'],
                              'structured_content': [{k: m[k] for k in ['name', 'csv', 'ofx', 'expected_account_mentioned'] if k in m}
                                                     for m in x['members'] if any(k in m for k in ['csv','ofx','expected_account_mentioned'])]}
                             for x in live['archives']],
          'limits': ['No final seizure inventory/CD/destination archive available.',
                     'File-name timestamps are not signatures or identification of an operator.',
                     'Screenshots describe categories, not an exhaustive file-name/hash list.',
                     'No legal relevance assessment of all messages/documents or independent bank authentication.']}
(OUT/'resultats.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(OUT/'sources-controle.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
