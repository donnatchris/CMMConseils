#!/usr/bin/env python3
"""Read-only TP-01 inventory and bounded working-copy collection, run on SIFT.
No message body, password or token is printed. Destination must be new.
"""
import argparse, collections, csv, datetime as dt, hashlib, json, os
import pathlib, plistlib, re, shutil, sqlite3

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def ro(p):
    return sqlite3.connect(p.resolve().as_uri()+'?mode=ro&immutable=1',uri=True)

def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2,default=str)+'\n')

def main():
    a=argparse.ArgumentParser(); a.add_argument('source',type=pathlib.Path); a.add_argument('out',type=pathlib.Path); a=a.parse_args()
    os.umask(0o077); a.out.mkdir(parents=True,exist_ok=False)
    rows=[]; copied=[]; missing=[]; meta=[]; heads={}
    for n in ['Info.plist','Manifest.plist','Status.plist','Manifest.db']:
        src=a.source/n; dst=a.out/n; shutil.copyfile(src,dst)
        heads[n]={'before':sha(src),'copy':sha(dst)}
    with ro(a.out/'Manifest.db') as c:
        check=c.execute('pragma quick_check').fetchall()
        for fid,d,r,flag,b in c.execute('select fileID,domain,relativePath,flags,file from Files order by domain,relativePath'):
            x={'fileID':fid,'domain':d,'relativePath':r,'flags':flag}
            try:
                pl=plistlib.loads(b); o=pl['$objects'][pl['$top']['root'].data]
                for k in ['Size','Birth','LastModified','LastStatusChange']: x[k]=o.get(k)
            except Exception as e: x['metadata_error']=type(e).__name__
            rows.append(x)
            if flag!=1: continue
            src=a.source/fid[:2]/fid
            if not src.is_file(): missing.append(fid); continue
            for k in ['Birth','LastModified','LastStatusChange']:
                v=x.get(k)
                if isinstance(v,(int,float)) and 1727733600<=v<1731711600: meta.append(dict(x,field=k,raw=v))
            selected=bool(re.search(r'\.(db|sqlite|sqlite3|sqlitedb)(-wal|-shm|-journal)?$',r,re.I))
            selected |= r.endswith(('.ips','.log'))
            selected |= r.endswith('.plist') and (not d.startswith('App') or any(z in (d+r).lower() for z in ['whatsapp','lscsmart','xiaomi','lockdown','mobile.installation']))
            if not selected: continue
            if pathlib.PurePosixPath(d).name!=d or '..' in pathlib.PurePosixPath(r).parts or r.startswith('/'): raise ValueError('unsafe path')
            dst=a.out/'files'/d/r; dst.parent.mkdir(parents=True,exist_ok=True)
            before=sha(src); shutil.copyfile(src,dst); after=sha(src); output=sha(dst)
            if before!=after or before!=output: raise ValueError('hash mismatch')
            copied.append(dict(x,sha256=before,sha256_after=after,copy_sha256=output,bytes=dst.stat().st_size))
    for n in heads: heads[n]['after']=sha(a.source/n)
    dump(a.out/'inventory.json',rows);dump(a.out/'collection.json',copied);dump(a.out/'metadata-candidates.json',meta)
    dump(a.out/'summary.json',{'source':str(a.source),'destination':str(a.out),'headers':heads,'quick_check':check,'flags':dict(collections.Counter(x['flags'] for x in rows)),'regular_bytes_manifest':sum(x.get('Size') or 0 for x in rows if x['flags']==1),'missing':missing,'selected':len(copied),'copied_bytes':sum(x['bytes'] for x in copied),'metadata_candidates':len(meta),'python':os.sys.version,'sqlite':sqlite3.sqlite_version,'time_utc':dt.datetime.now(dt.timezone.utc).isoformat()})
    print(json.dumps({'selected':len(copied),'missing':len(missing),'bytes':sum(x['bytes'] for x in copied)}))

if __name__=='__main__': main()
