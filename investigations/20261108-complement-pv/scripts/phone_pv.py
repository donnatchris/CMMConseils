from pathlib import Path
import sqlite3,hashlib,json,datetime as dt,shutil,re,plistlib,csv,unicodedata
from zoneinfo import ZoneInfo
B=Path('investigations/20261108-complement-pv'); src=Path('telephones/recherche-TP-02/extraction-systeme-20261014/files/HomeDomain/Library/SMS/sms.db');dst=B/'prive/sms-copie';dst.mkdir(exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
sources=[]
for p in [src,Path(str(src)+'-wal'),Path(str(src)+'-shm')]:
 if p.exists():
  before=sha(p);shutil.copyfile(p,dst/p.name);sources.append({'path':str(p),'sha256_before':before,'sha256_after':sha(p)})
c=sqlite3.connect((dst/src.name).resolve().as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
paris=ZoneInfo('Europe/Paris');start=dt.datetime(2024,10,28,11,30,tzinfo=paris);end=dt.datetime(2024,10,28,12,15,tzinfo=paris)
def stamp(v):return dt.datetime.fromtimestamp(v/1e9+978307200,dt.timezone.utc).astimezone(paris).isoformat() if v else None
lo=int((start.timestamp()-978307200)*1e9);hi=int((end.timestamp()-978307200)*1e9)
rows=[]
for r in c.execute('select ROWID,text,date,date_read,date_delivered,service,is_from_me,is_read,handle_id from message where date between ? and ? or date_read between ? and ? order by date',(lo,hi,lo,hi)):
 d=dict(r);t=d.pop('text') or '';d['date_paris']=stamp(d['date']);d['read_paris']=stamp(d['date_read']);d['apple_mentioned']=bool(re.search(r'apple|icloud',t,re.I));d['text_redacted']=re.sub(r'\b\d{4,8}\b','[CODE/CHIFFRES MASQUÉS]',t);rows.append(d)
(B/'prive/sms-fenetre.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
(B/'resultats/sms-fenetre-resume.json').write_text(json.dumps({'window':[start.isoformat(),end.isoformat()],'rows':[{k:v for k,v in r.items() if k not in ('text_redacted','handle_id')} for r in rows],'sources':sources},indent=2))
# Metadata-only full manifest selection, on an isolated SQLite copy.
p=Path('/mnt/data/forensic/SADEDINE-2026/ANALYSES/TP-02/Manifest-decrypted.db');before=sha(p)
q=B/'prive/Manifest-copie.db';shutil.copyfile(p,q)
for suffix in ['-wal','-shm']:
 companion=Path(str(p)+suffix)
 if companion.exists():shutil.copyfile(companion,Path(str(q)+suffix))
c=sqlite3.connect(q.resolve().as_uri()+'?mode=ro',uri=True)
pdfs=[]
for fid,domain,path,blob in c.execute('select fileID,domain,relativePath,file from Files where flags=1'):
 if not path.lower().endswith('.pdf'):continue
 v=plistlib.loads(blob);o=v['$objects'][v['$top']['root'].data]
 pdfs.append({'fileID':fid,'domain':domain,'relativePath':path,'size':o.get('Size'),'birth_raw':o.get('Birth'),'modified_raw':o.get('LastModified'),'priority':1})
(B/'prive/manifest-pdfs.json').write_text(json.dumps(pdfs,ensure_ascii=False,indent=2))
(B/'resultats/manifest-controle.json').write_text(json.dumps({'source':str(p),'sha256_before':before,'sha256_after':sha(p),'pdf_entries':len(pdfs),'full_regular_file_scan':True},indent=2))
print(json.dumps({'sms_rows':len(rows),'apple_mentions':sum(r['apple_mentioned'] for r in rows),'pdf_entries':len(pdfs)}))
