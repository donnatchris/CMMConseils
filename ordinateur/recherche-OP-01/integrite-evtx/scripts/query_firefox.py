import pathlib,json,sqlite3,shutil,datetime,collections
root=pathlib.Path(__file__).resolve().parents[1]/'independent';results=[]
start=int(datetime.datetime(2024,10,13,22,tzinfo=datetime.timezone.utc).timestamp()*1e6);end=int(datetime.datetime(2024,10,29,23,tzinfo=datetime.timezone.utc).timestamp()*1e6)
for p in root.glob('raw/browser/Users/*/AppData/Roaming/Mozilla/Firefox/Profiles/*/places.sqlite'):
 work=pathlib.Path('/tmp/OP01-firefox')/p.parent.name;work.mkdir(parents=True,exist_ok=True)
 for f in p.parent.iterdir():
  if f.is_file():shutil.copyfile(f,work/f.name)
 con=sqlite3.connect('file:'+str(work/'places.sqlite')+'?mode=ro',uri=True)
 for v in con.execute('select v.id,v.visit_date,v.visit_type,p.url,p.title from moz_historyvisits v join moz_places p on v.place_id=p.id where v.visit_date>=? and v.visit_date<? order by v.visit_date',(start,end)):
  results.append({'source':str(p.relative_to(root)),'visit_id':v[0],'utc':datetime.datetime.fromtimestamp(v[1]/1e6,datetime.timezone.utc).isoformat(),'visit_type':v[2],'url':v[3],'title':v[4]})
 con.close()
(root/'firefox-period-visits.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in results));print('visits',len(results),dict(collections.Counter(r['utc'][:10] for r in results)))
