#!/usr/bin/env python3
"""Synthèses dérivées reproductibles après achèvement de la collecte SD-02.
Aucune inférence d'heure civile ni d'intention. Refuse de remplacer ses sorties.
"""
import collections,csv,datetime as dt,hashlib,json,re
from sd02_collect import OUT,ROOT

def dump(name,data):
 with (OUT/name).open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2)
def csvout(name,rows):
 if not rows:return
 with (OUT/name).open('x',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
plan=json.loads((OUT/'inventaires/plan-medias.json').read_text());index=json.loads((OUT/'inventaires/medias-index.json').read_text());records=[json.loads((OUT/'inventaires/medias'/f"{e['inode']}.json").read_text()) for e in index['entries']];byinode={e['inode']:e for e in plan['entries']};byrecord={e['inode']:e for e in records}
active=[e for e in records if not e['deleted']];deleted=[e for e in records if e['deleted']];videos=[e for e in active if e['path'].endswith('.mp4')];finals=[e for e in videos if '/record/' in e['path']];dated=[];timeline=[];anomalies=[];descriptions=collections.Counter();timeheaders=collections.Counter();codecs=collections.Counter();accesses=collections.Counter();duplicates=collections.defaultdict(list)
for r in records:
 e=byinode[r['inode']];fmt=r.get('metadata',{}).get('format',{});streams=r.get('metadata',{}).get('streams',[]);duration=float(fmt['duration']) if fmt.get('duration') else None
 if not r['deleted'] and r.get('sha256'):duplicates[r['sha256']].append(r['path'])
 if not r['deleted']:accesses[e['accessed']]+=1
 if r in videos:
  timeheaders.update((str(b['creation_raw']),str(b['modification_raw'])) for b in r.get('mp4_structure',{}).get('boxes',[]) if 'creation_raw' in b)
  descriptions.update((str(v['size']),v['sha256']) for v in r.get('stsd',[]))
  codecs.update((s.get('codec_type'),s.get('codec_name'),s.get('width'),s.get('height'),s.get('sample_rate')) for s in streams)
 m=re.search(r'(\d{8})_(\d{6})_10(?:_(\d+))?\.mp4$',r['path']);start=None;end=None;name_error=None;declared_suffix=None
 if m:
  try:start=dt.datetime.strptime(m[1]+m[2],'%Y%m%d%H%M%S')
  except ValueError:name_error='date impossible'
  if m[3]:declared_suffix=int(m[3])
 if start and duration is not None:end=start+dt.timedelta(seconds=duration)
 delta=None
 if end and e['written'] and not e['written'].startswith(('INVALID','1999','2000')):
  delta=(dt.datetime.fromisoformat(e['written'])-end).total_seconds()
 row=dict(inode=r['inode'],path=r['path'],allocation='supprimé' if r['deleted'] else 'alloué',declared_size=e['size'],read_size=r.get('read_size'),sha256=r.get('sha256'),name_start=start.isoformat(' ') if start else None,name_date_error=name_error,ffprobe_duration=duration,name_suffix=declared_suffix,duration_minus_suffix=round(duration-declared_suffix,6) if duration is not None and declared_suffix is not None else None,estimated_end=end.isoformat(' ') if end else None,fat_created=e['created'],fat_written=e['written'],fat_accessed=e['accessed'],fat_written_minus_estimated_end=round(delta,6) if delta is not None else None,mp4_creation_time=fmt.get('tags',{}).get('creation_time'),ffprobe_rc=r.get('ffprobe',{}).get('returncode'),ffprobe_stderr=r.get('ffprobe',{}).get('stderr'),decode_rc=r.get('decode',{}).get('returncode'),decode_log=r.get('decode',{}).get('log'))
 timeline.append(row)
 structure=r.get('mp4_structure',{});table_issues=[t for t in structure.get('tracks',[]) if t['chunks_beyond_eof'] or t['stsz_sample_count']!=t['chunk_sample_count'] or t['stsz_sample_count']!=t['stts_sample_count']]
 packet_issues={k:v for k,v in r.get('packets',{}).get('summary',{}).items() if v['nonincreasing']}
 if name_error or r.get('error') or structure.get('errors') or table_issues or packet_issues or r.get('ffprobe',{}).get('returncode') or r.get('ffprobe',{}).get('stderr'):
  anomalies.append(dict(inode=r['inode'],path=r['path'],deleted=r['deleted'],name_error=name_error,error=r.get('error'),structural_errors=structure.get('errors'),table_issues=table_issues,packet_issues=packet_issues,ffprobe=r.get('ffprobe'),decode=r.get('decode')))
 if r in finals and start and end:dated.append((start,end,row))
days=collections.defaultdict(list)
for start,end,row in dated:days[start.date().isoformat()].append((start,end,row))
gaps=[];daily=[]
for day,items in sorted(days.items()):
 items.sort(key=lambda x:x[0]);coverage_end=None;daygaps=[]
 for start,end,row in items:
  if coverage_end is not None:
   gap=(start-coverage_end).total_seconds();daygaps.append(gap);gaps.append(dict(day=day,next_inode=row['inode'],next_path=row['path'],previous_coverage_end=coverage_end.isoformat(' '),next_name_start=start.isoformat(' '),gap_seconds=round(gap,6)))
  coverage_end=max(coverage_end,end) if coverage_end else end
 daily.append(dict(day=day,count=len(items),first_name_start=items[0][0].isoformat(' '),last_name_start=items[-1][0].isoformat(' '),last_estimated_end=max(x[1] for x in items).isoformat(' '),sum_duration_seconds=round(sum((end-start).total_seconds() for start,end,_ in items),6),max_internal_gap_seconds=round(max(daygaps,default=0),6),internal_overlaps=sum(x<0 for x in daygaps)))
csvout('inventaires/chronologie.csv',timeline);csvout('inventaires/par-jour.csv',daily);csvout('inventaires/intervalles.csv',gaps);dump('inventaires/anomalies-medias.json',anomalies)
# Comparaison uniquement par empreintes et en conservant les chemins distincts.
old=ROOT/'cartes_sd/recherche-SD-01/20261015/inventaires/export.json'
if not old.exists():
 candidates=list((ROOT/'cartes_sd/recherche-SD-01').glob('*/inventaires/export.json'));old=candidates[0] if candidates else None
matches=[]
if old:
 previous=json.loads(old.read_text());lookup=collections.defaultdict(list)
 for e in previous['entries']:
  if e.get('sha256') and not e.get('deleted'):lookup[e['sha256']].append(e['path'])
 for r in active:
  if r.get('sha256') in lookup:matches.append(dict(sd02=r['path'],sd01=lookup[r['sha256']],sha256=r['sha256']))
raw=json.loads((OUT/'inventaires/lecture-fat-v2.json').read_text());directory_dates=[]
for e in raw['entries']:
 if e['deleted'] or e['after_end_marker'] or not e['attributes']&16 or not re.search(r'/record/\d{8}$',e['path']):continue
 dots=[x for x in raw['entries'] if x['path']==e['path']+'/.'];dayname=e['path'].rsplit('/',1)[-1];day=dayname[:4]+'-'+dayname[4:6]+'-'+dayname[6:];d=next((x for x in daily if x['day']==day),{})
 directory_dates.append(dict(path=e['path'],parent_created=e['created'],parent_written=e['written'],dot_created=dots[0]['created'] if dots else None,dot_written=dots[0]['written'] if dots else None,first_active_name_start=d.get('first_name_start'),last_active_estimated_end=d.get('last_estimated_end')))
csvout('inventaires/repertoires-horloges.csv',directory_dates)
suffix_deltas=[r['duration_minus_suffix'] for r in timeline if r['allocation']=='alloué' and r['duration_minus_suffix'] is not None]
write_deltas=[r['fat_written_minus_estimated_end'] for r in timeline if r['allocation']=='alloué' and r['fat_written_minus_estimated_end'] is not None]
summary=dict(entries=len(records),active_regular=len(active),deleted_regular=len(deleted),active_mp4=len(videos),finalized_record_mp4=len(finals),valid_named_finalized_mp4=len(dated),read_errors=[dict(inode=r['inode'],path=r['path'],error=r['error']) for r in records if r.get('error')],hash_active_bytes=sum(r.get('read_size',0) for r in active),active_ffprobe_failed=[r['path'] for r in videos if r.get('ffprobe',{}).get('returncode')],active_decode_count=sum('decode' in r for r in active),active_decode_failed=[r['path'] for r in active if r.get('decode',{}).get('returncode')],active_decode_warning_logs=[dict(inode=r['inode'],path=r['path'],decode=r['decode']) for r in active if r.get('decode',{}).get('stderr_bytes')],active_table_anomaly_files=[a['path'] for a in anomalies if not a['deleted'] and a['table_issues']],active_structural_error_files=[a['path'] for a in anomalies if not a['deleted'] and a['structural_errors']],active_packet_anomalies=[a for a in anomalies if not a['deleted'] and a['packet_issues']],mp4_creation_times=dict(collections.Counter(r.get('metadata',{}).get('format',{}).get('tags',{}).get('creation_time') for r in videos)),raw_mp4_times=[dict(creation=a,modification=b,count=n) for (a,b),n in timeheaders.items()],codec_profiles=[dict(profile=list(k),count=v) for k,v in codecs.items()],sample_description_hashes=[dict(size=k[0],sha256=k[1],count=v) for k,v in descriptions.items()],duplicates=[dict(sha256=h,paths=p) for h,p in duplicates.items() if len(p)>1],icat_crosschecks=sum('icat_crosscheck' in r for r in active),icat_crosscheck_mismatch=[r['path'] for r in active if r.get('icat_crosscheck',{}).get('matches') is False],sd01_comparison_source=str(old.relative_to(ROOT)) if old else None,sd01_identical_active_files=matches,daily=daily,active_access_dates=dict(accesses),deleted_read_sizes=dict(collections.Counter(str(r.get('read_size')) for r in deleted)),deleted_ffprobe_success=sum(r.get('ffprobe',{}).get('returncode')==0 for r in deleted),selection_rule=plan['selection_rule'],duration_minus_suffix_min=min(suffix_deltas),duration_minus_suffix_max=max(suffix_deltas),fat_written_minus_end_min=min(write_deltas),fat_written_minus_end_max=max(write_deltas))
dump('inventaires/synthese-medias.json',summary)
print(json.dumps({k:v for k,v in summary.items() if k not in ('active_decode_warning_logs','sample_description_hashes','active_access_dates','daily','deleted_read_sizes','active_packet_anomalies')},ensure_ascii=False,indent=2))
