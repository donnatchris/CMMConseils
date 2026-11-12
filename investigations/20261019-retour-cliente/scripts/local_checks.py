#!/usr/bin/env python3
"""New scoped analysis from preserved exports; no source mutation."""
from pathlib import Path
import csv,json,hashlib,datetime as D,collections,re,plistlib,io,argparse
from zoneinfo import ZoneInfo
R=Path(__file__).resolve().parents[3];parser=argparse.ArgumentParser();parser.add_argument('--out',required=True);args=parser.parse_args();O=Path(args.out);O.mkdir(mode=0o700,exist_ok=False);sources=[]
def read(p):
 p=R/p if not isinstance(p,Path) else p;b=p.read_bytes();sources.append({'path':str(p.relative_to(R)),'sha256_before':hashlib.sha256(b).hexdigest()});return b
def js(p):return json.loads(read(p))
def rows(p):return list(csv.DictReader(io.StringIO(read(p).decode('utf-8-sig'))))
def save(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2,default=str))
# SD date coverage and bounded nominal daily union, preserving allocation status.
cards={};daily=[]
for card,path in [('SD-01','cartes_sd/recherche-SD-01/20261015/inventaires/inventaire.csv'),('SD-02','cartes_sd/recherche-SD-02/20261016/inventaires/chronologie.csv'),('SD-03','cartes_sd/recherche-SD-03/20261016/inventaires/chronologie.csv')]:
 rr=rows(path);videos=[x for x in rr if x.get('name_start') and x['path'].lower().endswith('.mp4')];dates=sorted(x['name_start'] for x in videos)
 active=[x for x in videos if x['allocation'] in ('alloue','alloué')];days=collections.defaultdict(list)
 for x in active:
  try:
   a=D.datetime.fromisoformat(x['name_start']); end=x.get('estimated_end');b=D.datetime.fromisoformat(end) if end else a+D.timedelta(seconds=float(x.get('duration') or x.get('ffprobe_duration') or 0))
   if b<a:continue
   cur=a
   while cur<b:
    midnight=D.datetime.combine(cur.date()+D.timedelta(days=1),D.time());stop=min(b,midnight);days[cur.date().isoformat()].append((cur,stop));cur=stop
  except (ValueError,TypeError):pass
 for day,ints in sorted(days.items()):
  merged=[]
  for a,b in sorted(ints):
   if merged and a<=merged[-1][1]:merged[-1]=(merged[-1][0],max(merged[-1][1],b))
   else:merged.append((a,b))
  total=sum((b-a).total_seconds() for a,b in merged)
  daily.append({'card':card,'day_camera':day,'nominal_union_seconds':round(total,3),'percent_24h':round(total/864,3),'intervals':len(merged),'note':'Durées nominales inventoriées; pas une garantie de décodage, horloges non étalonnées.'})
 cards[card]={'inventory':path,'video_rows':len(videos),'active_video_rows':len(active),'first_name':min(dates) if dates else None,'last_name':max(dates) if dates else None,'days_with_named_video':len(set(x[:10] for x in dates)),'march2023_rows':sum(x.startswith('2023-03') for x in dates),'feb2024_rows':sum(x.startswith('2024-02') for x in dates),'oct15_rows':sum(x.startswith('2024-10-15') for x in dates)}
save('sd-coverage.json',cards);save('sd-daily-nominal-coverage.json',daily)
# Independent reconciliation of newly read $I metadata with previous MFT extraction.
new=js('investigations/20261019-retour-cliente/resultats/sift/recycle.json');old=js('ordinateur/recherche-OP-01/fichiers-supprimes/recycle-pairs.json');checks=[]
for n in new:
 if not n['paris'].startswith('2024-10-28'):continue
 hits=[x for x in old if x['I_sha256']==n['sha256']]
 checks.append({**n,'previous_I_mft':[x['I_mft'] for x in hits],'metadata_agrees':len(hits)==1 and hits[0]['info']['original_path']==n['original_path'] and hits[0]['info']['deletion_filetime']==n['filetime'],'content_agrees':any(x.get('sha256')==n.get('R_sha256') for h in hits for x in h['R_matches'])})
save('corbeille-28-detail.json',checks)
# Device / extraction / remote-control candidate paths, no account secrets.
rr=rows('telephones/recherche-TP-02/inventaire-detaille/inventory.csv');patterns={
 'pairing':r'(^|/)(lockdown|pair_records|pairing_records)(/|$)|(^|/)(pair_records|pairing_records)\.',
 'extraction_names':r'cellebrite|graykey|gray.?shift|elcomsoft|oxygen.?forensic|magnet.?axiom|ufed',
 'remote_app_names':r'teamviewer|anydesk|logmein|splashtop|rustdesk|screenconnect|connectwise|airdroid|supremo|vnc',
 'management':r'configurationprofiles|managedconfiguration|mdm|cloudconfiguration',
 'account_devices':r'account.*device|device.*account|trusteddevice|paireddevice'}
candidates={k:[{z:x[z] for z in ('domain','relativePath','fileID','flags','birth_raw','modified_raw')} for x in rr if re.search(p,x['domain']+'/'+x['relativePath'],re.I)] for k,p in patterns.items()}
save('tp02-manifest-targets.json',{'rows_scanned':len(rr),'patterns':patterns,'hits':candidates,'limit':'Noms de chemins uniquement; logiciel inconnu/renommé ou accès compte côté serveur non exclus.'})
# Post-return traces: retain artifact contexts and do not treat metadata as action.
post=[];coverage=[]
for name in ['approfondissement-activite-202410/timeline-correlated.csv','investigation-systeme-oct2024/timeline-new-evidence.csv','chronologie-complete-20261014/chronology-evidence.csv']:
 path='telephones/recherche-TP-02/'+name;rr=rows(path);chosen=[]
 for x in rr:
  t=x.get('paris') or x.get('datetime_paris') or ''
  if t.startswith('2024-10-28'):
   try:
    d=D.datetime.fromisoformat(t)
    if d>D.datetime(2024,10,28,19,20,tzinfo=ZoneInfo('Europe/Paris')) and x.get('relativePath')!='docs/mail.txt':chosen.append(x)
   except ValueError:pass
 post.extend({'timeline':path,**x} for x in chosen);coverage.append({'path':path,'rows':len(rr),'fields':list(rr[0]) if rr else [],'selected':len(chosen)})
save('tp02-after1920.json',{'coverage':coverage,'rows':post,'limit':'Chronologies préexistantes ciblées, non ensemble de la sauvegarde. Une ligne n’est pas un geste humain.'})
# LSC states and metric dates, only selected non-secret values.
b=R/'telephones/recherche-TP-02/extraction-cameras-20261014/files/AppDomain-com.lscsmartconnection.smart'
v=plistlib.loads(read(b/'Library/Preferences/com.lscsmartconnection.smart.plist'));active=[]
for k,x in v.items():
 if k.startswith('activeTimeKey-') and isinstance(x,(int,float)):
  active.append({'device_sha256':hashlib.sha256(k.removeprefix('activeTimeKey-').encode()).hexdigest(),'key':'activeTimeKey','raw':x,'unix_hypothesis_utc':D.datetime.fromtimestamp(x,D.timezone.utc).isoformat(),'limit':'Sémantique et écriture historique non établies; pas date de reset prouvée.'})
metrics=[]
for n in ['Documents/metric.json','Documents/diagnostic.json']:
 for x in json.loads(read(b/n)):metrics.append({'source':n,'begin':x.get('timeStampBegin'),'end':x.get('timeStampEnd'),'keys':list(x)})
opaque=[]
for n in ['Documents/home/detailv1','Documents/home/list313']:
 d=read(b/n);opaque.append({'source':n,'size':len(d),'sqlite_signature':d.startswith(b'SQLite format 3'),'plist_signature':d.startswith(b'bplist'),'limit':'Format non décodé; pas d’historique de partages reconstitué.'})
catalog=js('investigations/20261017-recroisements/resultats/cameras/catalogue-medias.json')
save('lsc-history.json',{'activeTime_snapshot':active,'metrics':metrics,'home_opaque':opaque,'catalogue_count':len(catalog),'catalogue_dates':sorted(set(x.get('date_string') for x in catalog)),'limits':'Valeurs d’état, références de médias et diagnostics ne constituent pas un journal complet des connexions ou partages.'})
for s in sources:
 s['sha256_after']=hashlib.sha256((R/s['path']).read_bytes()).hexdigest();s['unchanged']=s['sha256_before']==s['sha256_after']
save('sources.json',sources)
print(json.dumps({'sd':cards,'recycle_count':len(checks),'recycle_verified':all(x['metadata_agrees'] and x['content_agrees'] for x in checks),'manifest_counts':{k:len(v) for k,v in candidates.items()},'post1920':len(post),'sources_unchanged':all(x['unchanged'] for x in sources)},ensure_ascii=False,indent=2))
