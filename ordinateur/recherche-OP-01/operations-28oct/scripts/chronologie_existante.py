"""Reconstitue les dates PST et les liens Kingston depuis les extractions existantes."""
import csv
import hashlib
import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

root = Path(__file__).resolve().parents[2]
out = Path(__file__).resolve().parents[1]
sources = root / 'extractions-acces'
rows = []
for line in (sources / 'l16b-mft.jsonl').open():
    record = json.loads(line)
    if not record['path'].lower().endswith('.pst'):
        continue
    fn = next(x for x in record['FN'] if x['namespace'] in (1, 3))
    for field, timestamp in [('FN.creation', fn['times']['creation']),
                             ('SI.modification', record['SI']['modification'])]:
        rows.append({'utc': timestamp,
                     'paris': datetime.fromisoformat(timestamp).astimezone(ZoneInfo('Europe/Paris')).isoformat(),
                     'path': record['path'], 'mft_index': record['mft_index'],
                     'field': field, 'source': 'extractions-acces/l16b-mft.jsonl'})
rows.sort(key=lambda r: r['utc'])
with (out / 'pst-chronologie.csv').open('w') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
devices = json.loads((sources / 'usb-mounteddevices-crosscheck.json').read_text())
kingston = [r for r in devices if 'Kingston' in r['device_utf16']]
(out / 'kingston-volumes.json').write_text(json.dumps(kingston, ensure_ascii=False, indent=2) + '\n')
files = [sources / 'l16b-mft.jsonl', sources / 'usb-mounteddevices-crosscheck.json',
         out / 'pst-chronologie.csv', out / 'kingston-volumes.json']
(out / 'SHA256SUMS').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root)}\n' for p in files))
print(f'{len(rows)} dates PST ; {len(kingston)} supports Kingston')
