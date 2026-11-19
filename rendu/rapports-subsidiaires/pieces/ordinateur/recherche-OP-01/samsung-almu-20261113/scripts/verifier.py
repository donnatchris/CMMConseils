from pathlib import Path
import json,hashlib,datetime
from dissect.eventlog.evtx import Evtx
B=Path(__file__).resolve().parents[1];O=B/'resultats';P=B/'preuves';src={x['path']:x for x in json.loads((O/'sources.json').read_text())};hashes=[]
for p in sorted(P.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(P));sha=hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
 expected=src[rel]['sha256'] if rel in src else next(x['sha256'] for x in json.loads((O/'ntfs-direct-check.json').read_text()) if x['mft_index']==181043) if rel=='mft-181043-test.pdf' else None
 hashes.append({'path':rel,'size':p.stat().st_size,'sha256':sha,'source_sha256':expected,'equal':sha==expected})
(O/'verification-transfert.json').write_text(json.dumps(hashes,indent=2));assert all(x['equal'] for x in hashes)
rows=json.loads((O/'print-events-day.json').read_text())+[x for x in json.loads((O/'samsung-events.json').read_text()) if x['serial_exact']];groups={}
for x in rows:groups.setdefault(x['source'],{})[x['record']]=x
checks=[]
for name,selected in groups.items():
 found=[];errs=[]
 for r in Evtx((P/'Windows/System32/winevt/Logs'/name).open('rb')):
  rid=int(str(r['EventRecordID']))
  if rid not in selected:continue
  x=selected[rid];diff=abs((datetime.datetime.fromisoformat(str(r['TimeCreated_SystemTime']))-datetime.datetime.fromisoformat(x['utc'])).total_seconds());names=['Param1','Param3','Param5','Param6','Param7','Param8','DeviceInstanceId']
  fieldchecks={}
  for k in names:
   if k not in x['data']:continue
   key=k if k in r else next((a for a in r if a.endswith('_'+k)),None)
   fieldchecks[k]=str(r.get(key))==str(x['data'][k])
  ok=int(str(r['EventID']))==x['id'] and diff<=.000003 and all(fieldchecks.values());found.append(rid)
  if not ok:errs.append({'record':rid,'difference_seconds':diff,'fields':fieldchecks,'data':str(r)})
 checks.append({'source':name,'expected':len(selected),'found':len(found),'all_found':len(selected)==len(found),'errors':errs})
(O/'verification-evenements-independante.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));assert all(x['all_found'] and not x['errors'] for x in checks)
print('Empreintes',len(hashes),'toutes concordantes ; événements',sum(x['found'] for x in checks),'vérifiés par second décodeur.')
