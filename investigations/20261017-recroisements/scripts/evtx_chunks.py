#!/usr/bin/env python3
"""Vérifie tous les chunks physiques, y compris hors compteur déclaré."""
import argparse,json
from pathlib import Path
from Evtx.Evtx import Evtx
R=Path(__file__).resolve().parents[3]
a=argparse.ArgumentParser();a.add_argument('--out',required=True);out=Path(a.parse_args().out)
if out.exists():raise SystemExit('Destination existante')
paths=['ordinateur/recherche-OP-01/extractions-acces/raw/Windows/System32/winevt/Logs/System.evtx','ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/raw/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Admin.evtx'];results=[]
for rel in paths:
 p=R/rel;item={'source':rel,'physical_chunks':(p.stat().st_size-4096)//65536,'records':0,'selected':[],'chunk_errors':[]}
 with Evtx(str(p)) as f:
  item['declared_chunks']=f.get_file_header().chunk_count()
  for ch in f.get_file_header().chunks(include_inactive=True):
   try:
    for record in ch.records():
     item['records']+=1;t=record.timestamp().isoformat()
     if (p.name=='System.evtx' and '2024-11-11'<=t[:10]<='2024-11-13') or (p.name!='System.evtx' and t[:10]=='2024-10-15'):
      item['selected'].append({'record':record.record_num(),'utc':t})
   except Exception as e:item['chunk_errors'].append(type(e).__name__)
 results.append(item)
out.write_text(json.dumps(results,indent=2));print(json.dumps([{'source':x['source'],'records':x['records'],'selected':len(x['selected']),'errors':x['chunk_errors']} for x in results]))
