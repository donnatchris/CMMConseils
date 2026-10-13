import pathlib,json,re,collections,xml.etree.ElementTree as E
root=pathlib.Path(__file__).resolve().parents[1];rx=re.compile(r'anydesk|teamviewer|screenconnect|rustdesk|ultraview|tightvnc|ultravnc|realvnc|radmin|splashtop|remotepc|logmein|dwagent|meshagent|atera|netsupport|ngrok|rclone|winscp|filezilla|ldsd',re.I)
summary={};reg=json.loads((root/'registry.json').read_text());summary['registry_rows']=len(reg);summary['registry_target_hits']=[r for r in reg if rx.search(json.dumps(r))];summary['autoruns']=[r for r in reg if re.search(r'\\Run(?:Once)?$',r['key']) or r['key'].endswith('Winlogon')]
a=[json.loads(l) for l in (root.parent/'integrite-evtx/independent/results.jsonl').read_text().splitlines()];summary['independent_target_hits']=[r for r in a if rx.search(json.dumps(r))]
if (root/'additional/amcache.json').exists():
 am=json.loads((root/'additional/amcache.json').read_text());summary['amcache_rows']=len(am);summary['amcache_target_hits']=[r for r in am if rx.search(json.dumps(r))]
if (root/'events.jsonl').exists():
 events=[json.loads(l) for l in (root/'events.jsonl').read_text().splitlines()];groups={}
 for r in events:
  k=r['source'];g=groups.setdefault(k,{'count':0,'first':r['utc'],'last':r['utc'],'before15':0,'ids_before15':collections.Counter()});g['count']+=1;g['first']=min(g['first'],r['utc']);g['last']=max(g['last'],r['utc'])
  if r['utc']<'2024-10-15':g['before15']+=1;g['ids_before15'][r['id']]+=1
 summary['events_coverage']=groups
 summary['historic_detections']=[r for r in events if r['utc']<'2024-10-15' and 'Defender' in r['source'] and r['id'] in [1116,1117,1118,1119,1121,1122]]
 summary['historic_service_installs']=[r for r in events if r['utc']<'2024-10-15' and r['provider']=='Service Control Manager' and r['id']==7045]
 summary['historic_tool_hits']=[r for r in events if r['utc']<'2024-10-15' and rx.search(r['xml'])]
(root/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print({k:len(v) if isinstance(v,list) else v for k,v in summary.items() if k!='events_coverage'});print(summary.get('events_coverage'))
