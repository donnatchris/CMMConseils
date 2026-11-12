#!/usr/bin/env python3
"""Lecture structurelle NSKeyedArchiver et sondage APM, sans exécuter de code archivé."""
import argparse,collections,datetime as dt,hashlib,json,math,plistlib,re,zlib
from pathlib import Path
from zoneinfo import ZoneInfo
R=Path(__file__).resolve().parents[3];a=argparse.ArgumentParser();a.add_argument('--out',required=True);o=Path(a.parse_args().out);o.mkdir(parents=True,exist_ok=False);o.chmod(0o700)
b=R/'telephones/recherche-TP-02/extraction-cameras-20261014/files/AppDomain-com.lscsmartconnection.smart/Documents'
sources=[];errors=[]
def sha(v):return hashlib.sha256(v).hexdigest()
def get(p):
 data=p.read_bytes();sources.append({'path':str(p.relative_to(R)),'sha256_before':sha(data),'size':len(data)});return data
def utc(t):return dt.datetime.fromtimestamp(t,dt.timezone.utc).isoformat()
def decode(v):
 objects=v['$objects'];active=set()
 def f(x):
  if isinstance(x,plistlib.UID):
   n=x.data
   if n in active:return {'cycle':n}
   active.add(n);y=f(objects[n]);active.remove(n);return y
  if isinstance(x,list):return [f(y) for y in x]
  if isinstance(x,dict):
   if 'NS.keys' in x:return {str(f(k)):f(v) for k,v in zip(x['NS.keys'],x['NS.objects'])}
   if 'NS.objects' in x:return f(x['NS.objects'])
   if 'NS.time' in x:return {'apple_seconds':x['NS.time'],'utc':utc(978307200+x['NS.time'])}
   return {k:f(v) for k,v in x.items() if k!='$class'}
  return x
 return f(v['$top'].get('root',next(iter(v['$top'].values()))))
catalog=[];covers=[]
for p in sorted((b/'ipc_photo_library/ipc_photo_date_catalog').glob('*')):
 try:
  decoded=decode(plistlib.loads(get(p)))
  for i,x in enumerate(decoded):
   row={'source':str(p.relative_to(R)),'index':i,'device_sha256':sha(str(x.get('devId')).encode()),'isVideo':x.get('isVideo'),'date_string':x.get('date'),'time_string':x.get('time'),'timestamp_raw':x.get('timeStamp'),'file_basename':Path(str(x.get('filePath'))).name,'thumbnail_basename':Path(str(x.get('thumbnail'))).name}
   if isinstance(x.get('timeStamp'),(int,float)):row['unix_hypothesis_utc']=utc(x['timeStamp'])
   row['media_extracted_locally']=(b/'ipc_photo_library'/row['file_basename']).is_file();catalog.append(row)
 except Exception as ex:errors.append({'path':str(p),'error':type(ex).__name__})
for p in sorted(b.glob('*_converPictureInfo')):
 try:
  x=decode(plistlib.loads(get(p)));blob=x.get('converPictureData',b'')
  covers.append({'source':str(p.relative_to(R)),'device_sha256':sha(p.name.split('_')[0].encode()),'date':x.get('converPictureTimeStamp'),'blob_size':len(blob),'blob_sha256':sha(blob),'known_image_signature':any(blob.startswith(z) for z in [b'\x89PNG\r\n\x1a\n',b'\xff\xd8\xff',b'GIF8'])})
 except Exception as ex:errors.append({'path':str(p),'error':type(ex).__name__})
apm=[]
for p in sorted(b.glob('*_apm_v1.0.db')):
 data=get(p);co=collections.Counter(data);entropy=-sum(n/len(data)*math.log2(n/len(data)) for n in co.values())
 # zlib/gzip ne sont retenus que si un flux COMPLET atteint EOF sous le plafond de 16 Mio.
 candidates=[i for i in range(len(data)-1) if data[i:i+2] in [b'\x78\x01',b'\x78\x9c',b'\x78\xda',b'\x1f\x8b']]
 valid=[];caps=0
 for i in candidates:
  try:
   d=zlib.decompressobj(31 if data[i:i+2]==b'\x1f\x8b' else 15);v=d.decompress(data[i:],16*1024*1024)
   if len(v)==16*1024*1024:caps+=1
   if d.eof:valid.append({'offset':i,'bytes':len(v),'sha256':sha(v)})
  except zlib.error:pass
 signatures={n:data.find(sig) for n,sig in {'SQLite':b'SQLite format 3\x00','bplist':b'bplist00','zip':b'PK\x03\x04','xz':b'\xfd7zXZ\x00','zstd':b'\x28\xb5\x2f\xfd'}.items()}
 apm.append({'source':str(p.relative_to(R)),'size':len(data),'size_mod4096':len(data)%4096,'entropy':round(entropy,6),'signatures_offsets':signatures,'compression_candidates':len(candidates),'complete_streams':valid,'output_caps':caps,'limit':'Sondage de signatures et flux zlib/gzip, pas déchiffrement ni identification du format.'})
for s in sources:s['sha256_after']=sha((R/s['path']).read_bytes());s['unchanged']=s['sha256_before']==s['sha256_after']
summary={'catalogue_entries':len(catalog),'catalogue_device_count':len(set(x['device_sha256'] for x in catalog)),'catalogue_oct15_28_entries':sum('2024-10-15'<=str(x.get('date_string'))<='2024-10-28' for x in catalog),'covers':len(covers),'apm_files':len(apm),'unchanged':all(x['unchanged'] for x in sources),'errors':errors}
for name,v in [('catalogue-medias.json',catalog),('couvertures.json',covers),('apm-sondage.json',apm),('sources.json',sources),('summary.json',summary)]:
 p=o/name;p.write_text(json.dumps(v,ensure_ascii=False,indent=2));p.chmod(0o600)
print(json.dumps(summary))
