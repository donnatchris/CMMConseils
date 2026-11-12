import pathlib,json,hashlib,re,datetime as D,collections
from zoneinfo import ZoneInfo
import pyevtx
B=pathlib.Path('/home/sansforensics/analysis/complement-20261019/resultats');O=B/'xml-fallback';O.mkdir(exist_ok=False)
e=json.loads((B/'errors.json').read_text());groups=collections.defaultdict(list)
for x in e:groups[x['source']].append(x)
rows=[];sources=[]
for n,errs in groups.items():
 p=pathlib.Path('/mnt/windows/Windows/System32/winevt/Logs')/n;h=hashlib.sha256(p.read_bytes()).hexdigest();f=pyevtx.file();f.open(str(p))
 for err in errs:
  r=f.get_record(err['index']);t=r.creation_time.replace(tzinfo=D.timezone.utc);xml=r.xml_string;m=re.search(r'<Provider\s+Name="([^"]+)"',xml)
  rows.append({'source':n,'index':err['index'],'record':r.identifier,'id':r.event_identifier,'utc':t.isoformat(),'paris':t.astimezone(ZoneInfo('Europe/Paris')).isoformat(),'provider':m.group(1) if m else None,'xml':xml,'method':'pyevtx record properties; provider regex only, XML not validated'})
 f.close();sources.append({'path':str(p),'sha256_before':h,'sha256_after':hashlib.sha256(p.read_bytes()).hexdigest()})
(O/'records.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(O/'sources.json').write_text(json.dumps(sources,indent=2));(O/'summary.json').write_text(json.dumps({'recovered':len(rows),'days':dict(collections.Counter(x['paris'][:10] for x in rows)),'after1920_28':sum('2024-10-28T19:20:00+01:00'<x['paris']<'2024-10-29' for x in rows)},indent=2))
