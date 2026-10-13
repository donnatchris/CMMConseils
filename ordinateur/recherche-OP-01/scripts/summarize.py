import pathlib,json,csv,collections,hashlib,datetime
from zoneinfo import ZoneInfo
root=pathlib.Path(__file__).resolve().parents[1]
rows=[json.loads(s) for s in (root/'events.jsonl').read_text().splitlines()]
errors=[json.loads(s) for s in (root/'xml-errors.jsonl').read_text().splitlines()]
inv=json.loads((root/'inventory.json').read_text())
with (root/'chronologie.csv').open('w') as f:
 w=csv.writer(f); w.writerow(['timestamp_utc','timestamp_europe_paris','source_file','provider','event_id','record_id','data_json'])
 for r in sorted(rows,key=lambda x:(x['utc'],x['source'],int(x['record']))): w.writerow([r[k] for k in ['utc','paris','source','provider','id','record']]+[json.dumps(r['data'],ensure_ascii=False)])
rejected=[r for r in errors if r['utc'] and '2024-10-13T22:00:00'<=r['utc']<'2024-10-29T23:00:00']
counts=collections.Counter(r['paris'][:10] for r in rows)
for r in rejected: counts[datetime.datetime.fromisoformat(r['utc'].replace('Z','+00:00')).astimezone(ZoneInfo('Europe/Paris')).date().isoformat()]+=1
summary={'logs':len(inv),'parsed':sum(i['events'] for i in inv),'rejected':len(errors),'selected_parsed':len(rows),'selected_rejected':len(rejected),'days_including_rejected':dict(counts),'undated_rejected':sum(r['utc'] is None for r in errors),'export_failures':[i['source'] for i in inv if i['returncode']],'parsed_in_gap':sum('2024-10-15T08:53:09'<=r['utc']<'2024-10-28T09:22:00' for r in rows),'rejected_in_gap':sum('2024-10-15T08:53:09'<=r['utc']<'2024-10-28T09:22:00' for r in errors if r['utc'])}
(root/'summary.json').write_text(json.dumps(summary,indent=2))
for f in (root/'evtx').glob('*.evtx'):
 expected=next(i['sha256'] for i in inv if i['source']==f.name); assert hashlib.sha256(f.read_bytes()).hexdigest()==expected,f
with (root/'SHA256SUMS').open('w') as out:
 for p in sorted(root.rglob('*')):
  if p.is_file() and p.name!='SHA256SUMS': out.write(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(root))+'\n')
print(json.dumps(summary,indent=2))
