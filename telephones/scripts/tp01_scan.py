#!/usr/bin/env python3
"""Timestamp triage on SIFT working copies. Candidates require schema validation."""
import collections, datetime as dt, json, pathlib, re, sqlite3, sys
from zoneinfo import ZoneInfo
from tp01_inventory import dump

PARIS=ZoneInfo('Europe/Paris')
LO=dt.datetime(2024,10,1,tzinfo=PARIS).timestamp()
HI=dt.datetime(2024,11,16,tzinfo=PARIS).timestamp()
START=dt.datetime(2024,10,15,13,30,tzinfo=PARIS).timestamp()
OPEN=dt.datetime(2024,10,28,11,30,tzinfo=PARIS).timestamp()
END=dt.datetime(2024,10,28,19,20,tzinfo=PARIS).timestamp()
FORMATS=[('unix_s',1,0),('cocoa_s',1,978307200),('unix_ms',1000,0),('unix_us',1e6,0),('unix_ns',1e9,0),('cocoa_ns',1e9,978307200)]
def q(s): return '"'+s.replace('"','""')+'"'
def date(t): return dt.datetime.fromtimestamp(t,dt.timezone.utc).astimezone(PARIS).isoformat()
def main():
 root=pathlib.Path(sys.argv[1]); out=pathlib.Path(sys.argv[2]);out.mkdir(exist_ok=False)
 coll=json.loads((root/'collection.json').read_text()); schemas=[]; candidates=[];stats=[];errors=[];plistdates=[]
 for item in coll:
  p=root/'files'/item['domain']/item['relativePath']; logical=item['domain']+'/'+item['relativePath']
  if p.name.endswith(('-wal','-shm','-journal')):continue
  with p.open('rb') as f: sig=f.read(16)
  if sig!=b'SQLite format 3\x00': continue
  try:
   c=sqlite3.connect(p.resolve().as_uri()+'?mode=ro',uri=True)
   try: integrity=c.execute('pragma quick_check').fetchall()
   except sqlite3.Error as e:
    integrity=[['not completed: '+str(e)]]
    errors.append({'path':logical,'stage':'quick_check','error':str(e)})
   tables=c.execute("select name,sql from sqlite_master where type='table'").fetchall()
   schemas.append({'path':logical,'quick_check':integrity,'wal':p.with_name(p.name+'-wal').exists(),'tables':tables})
   for table,sql in tables:
    if table.startswith('sqlite_') or (sql and 'VIRTUAL TABLE' in sql.upper()):continue
    cols=c.execute('pragma table_info('+q(table)+')').fetchall()
    timecols=[col for _,col,typ,*_ in cols if re.search('date|time|created|modified|read|start|end|added|last|first',col,re.I)]
    bounds={}
    if timecols:
     expr=[]
     for col in timecols:
      v=f"CASE WHEN typeof({q(col)}) in ('real','integer') AND {q(col)}>0 THEN {q(col)} END"
      expr.extend([f'min({v})',f'max({v})'])
     try:
      values=c.execute('select '+','.join(expr)+' from '+q(table)).fetchone()
      bounds={col:values[i*2:i*2+2] for i,col in enumerate(timecols)}
     except sqlite3.Error:pass
    for _,col,typ,*_ in cols:
     if not re.search('date|time|created|modified|read|start|end|added|last|first',col,re.I):continue
     column=q(col);tn=q(table)
     for fmt,scale,offset in FORMATS:
      low=(LO-offset)*scale;high=(HI-offset)*scale
      if col in bounds:
       minimum,maximum=bounds[col]
       if minimum is None or maximum<low or minimum>=high:continue
      where=f"typeof({column}) in ('real','integer') and {column}>=? and {column}<?"
      try:
       vals=c.execute(f'select rowid,{column} from {tn} where {where}',(low,high)).fetchall()
      except sqlite3.OperationalError as e:
       if 'rowid' not in str(e):
        errors.append({'path':logical,'table':table,'column':col,'error':str(e)});break
       vals=c.execute(f'select null,{column} from {tn} where {where}',(low,high)).fetchall()
      if not vals:continue
      times=[v/scale+offset for rid,v in vals]
      stats.append({'path':logical,'table':table,'column':col,'format_hypothesis':fmt,'count_extended':len(vals),'count_central':sum(START<=t<=END for t in times),'count_before_open':sum(START<=t<OPEN for t in times),'first':date(min(times)),'last':date(max(times)),'days':dict(collections.Counter(date(t)[:10] for t in times))})
      for (rid,v),t in zip(vals,times):
       candidates.append({'path':logical,'table':table,'rowid':rid,'column':col,'raw':v,'format_hypothesis':fmt,'paris':date(t),'central':START<=t<=END,'before_open':START<=t<OPEN})
   c.close()
  except Exception as e: errors.append({'path':logical,'error':str(e)})
 dump(out/'schemas.json',schemas);dump(out/'timestamp-stats.json',stats);dump(out/'timestamp-candidates.json',candidates);dump(out/'errors.json',errors)
 print(json.dumps({'databases':len(schemas),'stats':len(stats),'candidates':len(candidates),'errors':len(errors)}))
if __name__=='__main__':main()
