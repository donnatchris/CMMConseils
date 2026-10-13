import pathlib,json,sqlite3,datetime,re,urllib.parse,tempfile,shutil
root=pathlib.Path(__file__).resolve().parents[1];db=root.parent/'integrite-evtx/independent/raw/browser/Users/fintm/AppData/Roaming/Mozilla/Firefox/Profiles/y5rcl384.default-release/places.sqlite'
tmp=tempfile.TemporaryDirectory(prefix='OP01-firefox-phase2-');work=pathlib.Path(tmp.name)/db.name
for suffix in ['', '-wal', '-shm']:
 source=pathlib.Path(str(db)+suffix)
 if source.exists():shutil.copyfile(source,pathlib.Path(str(work)+suffix))
con=sqlite3.connect('file:'+str(work)+'?mode=ro',uri=True);rows=[];downloads=[]
rx=re.compile(r'anydesk|teamviewer|logmein|screenconnect|remotepc|ultraview|rustdesk|vnc|radmin|splashtop|winscp|filezilla|rclone|ngrok|takeout|wetransfer|transfernow|send-anywhere|mega\.nz|icloud|drive\.google|camera|freebox',re.I)
for t,typ,url,title in con.execute('select v.visit_date,v.visit_type,p.url,p.title from moz_historyvisits v join moz_places p on v.place_id=p.id where v.visit_date>=? and v.visit_date<?',(1609459200000000,1728943200000000)):
 if rx.search(url):
  u=urllib.parse.urlsplit(url);rows.append({'utc':datetime.datetime.fromtimestamp(t/1e6,datetime.timezone.utc).isoformat(),'type':typ,'url_domain_path':u.netloc+u.path,'title':title})
for place,url,attr,content,added,modified in con.execute('select p.id,p.url,a.name,n.content,n.dateAdded,n.lastModified from moz_annos n join moz_anno_attributes a on n.anno_attribute_id=a.id join moz_places p on n.place_id=p.id'):
 u=urllib.parse.urlsplit(url);downloads.append({'place_id':place,'source_domain_path':u.netloc+u.path,'attribute':attr,'content':content,'added_utc':datetime.datetime.fromtimestamp(added/1e6,datetime.timezone.utc).isoformat() if added else None,'modified_utc':datetime.datetime.fromtimestamp(modified/1e6,datetime.timezone.utc).isoformat() if modified else None})
con.close();tmp.cleanup();(root/'firefox-pre15-targets.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(root/'firefox-downloads.json').write_text(json.dumps(downloads,ensure_ascii=False,indent=2));print('targeted visits',len(rows),'download annotations',len(downloads))
for r in downloads:
 if rx.search(r['content'] or ''):print(r['added_utc'],r['attribute'],r['content'][:160])
