#!/usr/bin/env python3
"""Relecture des EVTX conservés avec python-evtx, sorties neuves uniquement."""
from pathlib import Path
import argparse,json,hashlib,datetime as dt,collections
import xml.etree.ElementTree as ET
from Evtx.Evtx import Evtx
from zoneinfo import ZoneInfo
R=Path(__file__).resolve().parents[3]
a=argparse.ArgumentParser();a.add_argument('--out',required=True);o=Path(a.parse_args().out);o.mkdir(parents=True,exist_ok=False);o.chmod(0o700)
ns={'e':'http://schemas.microsoft.com/win/2004/08/events/event'}
base=R/'ordinateur/recherche-OP-01/extractions-acces/raw/Windows/System32/winevt/Logs'
paths=[base/x for x in ['System.evtx','Microsoft-Windows-SMBServer%4Security.evtx','Microsoft-Windows-SmbClient%4Connectivity.evtx','Microsoft-Windows-SmbClient%4Security.evtx','Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx']]
paths += [R/'ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/raw/Windows/System32/winevt/Logs/Microsoft-Windows-Dhcp-Client%4Admin.evtx']
sources=[];events=[];errors=[]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for p in paths:
 before=h(p);count=0;dates=[];chosen=0
 with Evtx(str(p)) as log:
  for rec in log.records():
   count+=1
   try:
    ts=rec.timestamp();d=ts.replace(tzinfo=dt.timezone.utc) if ts.tzinfo is None else ts;dates.append(d.isoformat())
    # Système : 11-13 novembre, autres canaux : parsing de tous les enregistrements.
    if p.name=='System.evtx' and not dt.datetime(2024,11,10,23,tzinfo=dt.timezone.utc)<=d<dt.datetime(2024,11,13,23,tzinfo=dt.timezone.utc):continue
    xml=rec.xml();e=ET.fromstring(xml);data={}
    for node in e:
     if node.tag.endswith('System'):continue
     for z in node.iter():
      if len(z)==0 and z.text:data[z.get('Name') or z.tag.split('}')[-1]]=z.text
    eid=e.findtext('e:System/e:EventID',namespaces=ns);prov=e.find('e:System/e:Provider',ns)
    reasons=[];txt=json.dumps(data).lower()
    if p.name=='System.evtx':reasons.append('fenetre-11-13-novembre')
    if '192.168.1.139' in txt:reasons.append('smb-ip-139')
    if any(x in txt for x in ['desktop-icpncmd','ac:ed:5c:da:47:74','aced5cda4774','ea:21:6c:f7:47:e7','9c:64:8b:0a:bd:0c','fe:aa:76:95:ac:29']):reasons.append('identites-inconnues')
    if any(x in txt for x in ['50:e0:85:63:41:5b','50e08563415b']) and '2024-10-15' in d.isoformat():reasons.append('identite-op01-15oct')
    if reasons:
     events.append({'source':str(p.relative_to(R)),'record':rec.record_num(),'utc':d.isoformat(),'paris':d.astimezone(ZoneInfo('Europe/Paris')).isoformat(),'provider':prov.get('Name') if prov is not None else None,'id':eid,'computer':e.findtext('e:System/e:Computer',namespaces=ns),'reasons':reasons,'data':data});chosen+=1
   except Exception as exc:errors.append({'source':str(p.relative_to(R)),'index':count,'error':type(exc).__name__})
 after=h(p);sources.append({'path':str(p.relative_to(R)),'sha256_before':before,'sha256_after':after,'unchanged':before==after,'records':count,'first':min(dates) if dates else None,'last':max(dates) if dates else None,'selected':chosen});print(p.name,count,chosen,flush=True)
for name,v in [('events.json',events),('sources.json',sources),('errors.json',errors)]:
 p=o/name;p.write_text(json.dumps(v,ensure_ascii=False,indent=2));p.chmod(0o600)
print('done',len(events),'errors',len(errors))
