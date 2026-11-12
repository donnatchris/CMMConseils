#!/usr/bin/env python3
"""Final native integrity, IPS and camera coverage checks without user content."""
import collections,datetime as dt,hashlib,json,pathlib,plistlib,sqlite3,struct,sys
from tp01_inventory import dump,sha,ro
def main():
 root=pathlib.Path(sys.argv[1]);priority=pathlib.Path(sys.argv[2]);out=root/'final-checks';out.mkdir(exist_ok=False)
 a=json.loads((root/'collection.json').read_text());b=json.loads((priority/'collection.json').read_text());index={x['fileID']:x for x in a};dups=[]
 for x in b:
  y=index.get(x['fileID'])
  if y:dups.append({'fileID':x['fileID'],'identical_clear':x['sha256']==y['sha256'],'identical_cipher':x['ciphertext_sha256']==y['ciphertext_sha256']})
 checks=[];source=pathlib.Path(json.loads((root/'summary.json').read_text())['source'])
 with ro(root/'Manifest.db') as c:
  for x in b:
   if not (x['pdf_candidate'] or any(t in x['relativePath'] for t in ['healthdb','sms.db','CallHistory.storedata','Photos.sqlite','private-mac-networks'])):continue
   fid=x['fileID'];raw=c.execute('select file from Files where fileID=?',(fid,)).fetchone()[0];pl=plistlib.loads(raw);obj=pl['$objects'][pl['$top']['root'].data];digest=obj.get('Digest')
   if isinstance(digest,plistlib.UID):digest=pl['$objects'][digest.data]
   sp=source/fid[:2]/fid;dest=priority/'files'/x['domain']/x['relativePath'];cs=sp.stat().st_size;ps=dest.stat().st_size
   check={'fileID':fid,'path':x['domain']+'/'+x['relativePath'],'source_sha256_after':sha(sp),'cipher_unchanged':sha(sp)==x['ciphertext_sha256'],'clear_unchanged':sha(dest)==x['sha256'],'cipher_bytes':cs,'clear_bytes':ps,'padding_difference':cs-ps,'manifest_bytes':x['Size']}
   if isinstance(digest,bytes):
    with sp.open('rb') as f:
     h=hashlib.sha1()
     for chunk in iter(lambda:f.read(1024*1024),b''):h.update(chunk)
    check['digest_matches_cipher_sha1']=h.digest()==digest
   if dest.open('rb').read(16)==b'SQLite format 3\x00':
    with dest.open('rb') as f:header=f.read(100)
    page=int.from_bytes(header[16:18],'big');page=65536 if page==1 else page
    check.update(page_size=page,header_pages=int.from_bytes(header[28:32],'big'),header_bytes=page*int.from_bytes(header[28:32],'big'))
   checks.append(check)
 cam=[]
 for d in ['AppDomain-com.lscsmartconnection.smart','AppDomain-com.xiaomi.mihome']:
  p=root/'files'/d/'Library/WebKit/WebsiteData/ResourceLoadStatistics/observations.db'
  c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True)
  rows=c.execute('select year,month,monthDay from OperatingDates order by year,month,monthDay').fetchall();c.close()
  cam.append({'domain':d,'sha256':sha(p),'raw_rows':rows,'october_2024_days_utc':[f'{y:04d}-{m+1:02d}-{day:02d}' for y,m,day in rows if y==2024 and m==9]})
 access=[];ips=[];errors=[]
 for x in a:
  p=root/'files'/x['domain']/x['relativePath']
  if x['relativePath'].endswith('.ips'):
   try:
    text=p.read_text();decoder=json.JSONDecoder();objects=[];at=0
    while at<len(text):
     while at<len(text) and text[at].isspace():at+=1
     if at==len(text):break
     o,end=decoder.raw_decode(text,at);objects.append(o);at=end
    ips.append({'path':x['relativePath'],'sha256':sha(p),'objects':len(objects),'dates':[{k:o[k] for k in ['timestamp','captureTime','procLaunch','os_version','modelCode'] if k in o} for o in objects if isinstance(o,dict)]})
   except Exception as e:errors.append({'path':x['relativePath'],'error':type(e).__name__})
 for x in b:
  if x['relativePath'].endswith('__access_time__.json'):
   p=priority/'files'/x['domain']/x['relativePath']
   try:
    v=json.loads(p.read_text());access.append({'path':x['domain']+'/'+x['relativePath'],'value':v})
   except Exception as e:errors.append({'path':x['relativePath'],'error':type(e).__name__})
 dump(out/'duplicate-decryptions.json',dups);dump(out/'native-integrity.json',checks);dump(out/'camera-webkit.json',cam);dump(out/'camera-access-times.json',access);dump(out/'ips-metadata.json',ips);dump(out/'errors.json',errors)
 print(json.dumps({'duplicates':len(dups),'identical':all(x['identical_clear'] and x['identical_cipher'] for x in dups),'integrity_checks':len(checks),'ips':len(ips),'errors':len(errors)}))
if __name__=='__main__':main()
