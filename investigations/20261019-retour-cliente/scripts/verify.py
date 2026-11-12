from pathlib import Path
import json,hashlib,collections,re,datetime as D
R=Path(__file__).resolve().parents[3];C=R/'investigations/20261019-retour-cliente';checks={};errors=[]
def js(p):return json.loads(p.read_text())
s=js(C/'resultats/sift/summary.json');checks['evtx_359_records_275577']=s['evtx_files']==359 and s['records']==275577
r=js(C/'resultats/sift/events-16-29oct.json')+js(C/'resultats/sift/xml-fallback/records.json')
checks['event_counts_28_29']=dict(collections.Counter(x['paris'][:10] for x in r))=={'2024-10-28':6072,'2024-10-29':3594}
checks['no_events_after_1920']=not any('2024-10-28T19:20:00+01:00'<x['paris']<'2024-10-29' for x in r)
checks['fallback_285']=len(js(C/'resultats/sift/xml-fallback/records.json'))==285
rr=js(C/'resultats/local-v2/corbeille-28-detail.json');checks['ten_recycle_all_match']=len(rr)==10 and all(x['metadata_agrees'] and x['content_agrees'] for x in rr)
for kind,path in [('remote','resultats/sift/sources.json'),('fallback','resultats/sift/xml-fallback/sources.json'),('local','resultats/local-v2/sources.json'),('plists','resultats/plists/sources.json')]:
 ss=js(C/path);checks[kind+'_hashes_unchanged']=all(x['sha256_before']==x['sha256_after'] for x in ss)
 if kind in ('local','plists'):
  checks[kind+'_source_hashes_current']=all(hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256_after'] for x in ss)
m=js(C/'resultats/sift/mft-apres1920/mft-summary.json');old=js(R/'ordinateur/recherche-OP-01/extractions-acces/mft-targets/mft-summary.json');checks['mft_same_sha256_as_previous']=m['sha256']==old['sha256'];checks['mft_six_selected']=m['selected_records']==6
v=[json.loads(x) for x in (C/'resultats/sift/mft-apres1920/mft-selected-records.jsonl').read_text().splitlines()];checks['five_icloud_one_pairing']=sum(any('iCloudPhotos' in n['path'] for n in x['names']) for x in v)==5 and any(x['mft_index']==113002 for x in v)
checks['istat_confirms_pairing_dates']=all(z in (C/'resultats/sift/istat-pairing-113002.txt').read_text() for z in ['2022-07-04 11:19:51','2023-12-14 15:43:30'])
reports=js(C/'resultats/rapports-modifies.json');checks['nine_reports_hashes_current']=len(reports)==9 and all(hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256_after'] for x in reports)
checks['source_image_133021_hash']=hashlib.sha256((R/'cartes_sd/recherche-SD-03/20261016/prive/apercus/714049800-138.88.png').read_bytes()).hexdigest()=='8cc9a0f4c6654ffbbeb10c30b68eb5c808639cfb3c48e49947e4d67eec93366c'
# Validate new local Markdown link targets (anchors excluded).
for p in [C/'compte-rendu.md',C/'README.md']:
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if target.startswith(('http:','https:','#')):continue
  dest=target.split('#')[0]
  if dest and not (p.parent/dest).exists():errors.append({'path':str(p.relative_to(R)),'missing_target':dest})
checks['new_report_link_targets_exist']=not errors
checks['no_draft_placeholders']='<!--' not in (C/'compte-rendu.md').read_text()
checks['new_context_all_reports']=all('19 octobre' in (R/x['path']).read_text() for x in reports)
result={'checks':checks,'all_passed':all(checks.values()),'link_errors':errors,'limits':'Contrôles de cohérence et empreintes; pas validation indépendante de toutes les interprétations ni acquisition nouvelle.'}
(C/'resultats/verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False,indent=2))
if not result['all_passed']:raise SystemExit(1)
