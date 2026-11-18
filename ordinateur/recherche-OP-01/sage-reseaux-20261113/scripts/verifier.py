import json,pathlib,hashlib,datetime
from dissect.eventlog.evtx import Evtx
B=pathlib.Path(__file__).resolve().parents[1];O=B/'resultats';proofs=B/'preuves'
source_rows=[]
for n in ['sources.json','complement-sources.json','reseau-complement-sources.json','fin-sources.json']:
 source_rows+=json.loads((O/n).read_text())
by={r['path']:r for r in source_rows};verification=[]
for p in sorted(proofs.rglob('*')):
 if p.is_file():
  rel=str(p.relative_to(proofs));sha=hashlib.file_digest(p.open('rb'),'sha256').hexdigest();r=by.get(rel);verification.append({'path':rel,'size':p.stat().st_size,'sha256':sha,'source_sha256':r['sha256'] if r else None,'equal':r is not None and sha==r['sha256']})
(O/'verification-transfert.json').write_text(json.dumps(verification,indent=2));assert all(x['equal'] for x in verification)
network=json.loads((O/'network-events.json').read_text());sage=json.loads((O/'sage-events.json').read_text())
rows=network+sage+json.loads((O/'systeme-reseau-horloge.json').read_text())
# Fields independently compared: RecordID, EventID, UTC, Name/SSID and NCSI Capability.
# No GUID string comparison: the secondary library renders GUID byte order differently.
checks=[]
for fn in ['Microsoft-Windows-NetworkProfile%4Operational.evtx','Microsoft-Windows-WLAN-AutoConfig%4Operational.evtx','Microsoft-Windows-NCSI%4Operational.evtx','Application.evtx','System.evtx']:
 targets={int(x['record']):x for x in rows if x['source']==fn and x['paris'].startswith('2024-10-28')}
 count=0;matched=[];mismatches=[]
 for r in Evtx((proofs/'Windows/System32/winevt/Logs'/fn).open('rb')):
  count+=1;rid=int(str(r['EventRecordID']))
  if rid not in targets:continue
  x=targets[rid];ts=datetime.datetime.fromisoformat(str(r['TimeCreated_SystemTime']));original=datetime.datetime.fromisoformat(x['utc']);diff=abs((ts-original).total_seconds())
  fields={k:{'secondary':str(r[k]),'primary':str(x['data'][k])} for k in ['Name','SSID','Capability'] if k in x['data']}
  ok=int(str(r['EventID']))==int(x['id']) and diff<=.000003 and all(v['secondary']==v['primary'] for v in fields.values())
  detail={'record':rid,'event_id':int(str(r['EventID'])),'utc':str(ts),'time_difference_seconds':diff,'fields':fields,'equal':ok};matched.append(detail)
  if not ok:mismatches.append(detail)
 checks.append({'source':fn,'records_secondary':count,'selected_primary':len(targets),'selected_secondary':len(matched),'all_selected_found':len(matched)==len(targets),'mismatches':mismatches,'checks':matched})
(O/'verification-decodeur-independant.json').write_text(json.dumps(checks,indent=2));assert all(x['all_selected_found'] and not x['mismatches'] for x in checks)
print('Transfer hashes:',len(verification),'all match. Secondary event decoder:',[(x['source'],x['selected_secondary']) for x in checks])
