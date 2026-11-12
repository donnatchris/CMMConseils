#!/usr/bin/env python3
"""Inventaire S3 en lecture seule ; aucun secret enregistré."""
import argparse,json,datetime as dt
from pathlib import Path
import boto3
from botocore.config import Config
a=argparse.ArgumentParser();a.add_argument('--out',required=True);o=Path(a.parse_args().out);o.mkdir(parents=True,exist_ok=False);o.chmod(0o700)
r={'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'endpoint':'https://s3.sbg.io.cloud.ovh.net','profile':'ovh-forensic','buckets':[],'errors':[],'read_only':True}
try:
 s=boto3.Session(profile_name='ovh-forensic').client('s3',endpoint_url=r['endpoint'],config=Config(connect_timeout=10,read_timeout=20,retries={'max_attempts':1}))
 for b in s.list_buckets()['Buckets']:
  name=b['Name'];e={'name':name,'objects':[]};r['buckets'].append(e)
  # Le profil est dédié forensic ; ne parcourir que les noms explicitement liés au dossier.
  if not any(x in name.lower() for x in ['sadedine','forensic','dmm','cmm']):e['skipped']='nom non rattaché à la mission';continue
  try:
   for page in s.get_paginator('list_objects_v2').paginate(Bucket=name):
    e['objects'] += [{k:x.get(k) for k in ['Key','Size','ETag','LastModified','ChecksumAlgorithm']} for x in page.get('Contents',[])]
   e['object_count']=len(e['objects']);e['bytes']=sum(x['Size'] for x in e['objects'])
   for method in ['get_bucket_versioning','get_bucket_lifecycle_configuration']:
    try:e[method]={k:v for k,v in getattr(s,method)(Bucket=name).items() if k!='ResponseMetadata'}
    except Exception as ex:e[method]={'error':type(ex).__name__,'code':getattr(ex,'response',{}).get('Error',{}).get('Code')}
  except Exception as ex:e['error']={'type':type(ex).__name__,'code':getattr(ex,'response',{}).get('Error',{}).get('Code')}
except Exception as ex:r['errors'].append({'type':type(ex).__name__,'code':getattr(ex,'response',{}).get('Error',{}).get('Code')})
p=o/'inventaire-s3.json';p.write_text(json.dumps(r,ensure_ascii=False,indent=2,default=str));p.chmod(0o600)
print(json.dumps({'buckets':[{'name':b['name'],'count':b.get('object_count'),'bytes':b.get('bytes'),'error':b.get('error'),'skipped':b.get('skipped')} for b in r['buckets']],'errors':r['errors']}))
