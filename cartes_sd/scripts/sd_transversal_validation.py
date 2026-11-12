#!/usr/bin/env python3
"""Validation des populations, des empreintes historiques et des index expérimentaux."""
import csv, hashlib, json, os, pathlib, struct, subprocess, sys
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'cartes_sd/recherche-transversale/20261016');assert OUT.resolve().is_relative_to(ROOT/'cartes_sd/recherche-transversale')
def js(p):return json.loads(p.read_text())
def write(n,v):
 with (OUT/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2)
checks=[];uncovered=[];mismatches=[]
sources=js(OUT/'inventaires/sources.json')|js(OUT/'inventaires/sources-complement.json')
for camp,form in [('SD-01/20261015','csv'),('SD-01/20261016-complement','csv'),('SD-02/20261016','txt'),('SD-03/20261016','txt')]:
 base=ROOT/('cartes_sd/recherche-'+camp);p=base/('manifest-sha256.'+form)
 if form=='csv':manifest={r['path_from_project']:r['sha256'] for r in csv.DictReader(p.open())}
 else:
  manifest={}
  for line in p.read_text().splitlines():
   sha,path=line.split(maxsplit=1);manifest[path.lstrip('*')]=sha
 for path,r in sources.items():
  if path.startswith(str(base.relative_to(ROOT))+'/'):
   if path not in manifest:uncovered.append(path)
   else:
    valid=r['sha256']==manifest[path];checks.append({'path':path,'valid':valid})
    if not valid:mismatches.append(path)
write('inventaires/verification-manifestes-historiques.json',{'checked':len(checks),'mismatches':mismatches,'not_in_manifest':uncovered,'checks':checks})
assert not mismatches
rr=list(csv.DictReader((ROOT/'cartes_sd/recherche-SD-02/20261016/inventaires/chronologie.csv').open()));active={r['inode'] for r in rr if r['allocation']=='alloué'};diffs=[]
for p in (ROOT/'cartes_sd/recherche-SD-02/20261016/inventaires/medias').glob('*.json'):
 r=js(p)
 if r['inode'] not in active:continue
 ss=r.get('metadata',{}).get('streams',[]);a=next((s for s in ss if s.get('codec_type')=='audio'),{});v=next((s for s in ss if s.get('codec_type')=='video'),{})
 if a.get('duration') and v.get('duration'):diffs.append((float(a['duration'])-float(v['duration']),r['inode']))
write('inventaires/ecarts-audio-video-SD02-actifs.json',{'count':len(diffs),'min':min(diffs),'max':max(diffs),'top_ten':sorted(diffs,reverse=True)[:10],'population':'MP4 actifs analysables, hors temporaire et supprimés ; remplace la population mixte du complément'})
patched=[]
for r in js(OUT/'inventaires/tables-ciblees.json'):
 if not r['fat_written'].startswith('2000'):continue
 b=(ROOT/r['source_artifact']).read_bytes();assert hashlib.sha256(b).hexdigest()==r['sha256'];fixed=bytearray(b)
 for p in r['inspection']['patches']:struct.pack_into('>I',fixed,p['offset'],p['new'])
 fd=os.memfd_create('index-audio-video',0);os.write(fd,fixed)
 try:
  argv=['ffprobe','-v','error','-show_streams','-of','json','/proc/self/fd/'+str(fd)];proc=subprocess.run(argv,pass_fds=(fd,),capture_output=True,timeout=60)
  patched.append({'card':r['card'],'inode':r['inode'],'patches':r['inspection']['patches'],'sha256':hashlib.sha256(fixed).hexdigest(),'changed_bytes':[i for i,(a,z) in enumerate(zip(b,fixed)) if a!=z],'argv':argv,'returncode':proc.returncode,'stderr':proc.stderr.decode(),'wrong_sample_count':b'wrong sample count' in proc.stderr,'RAM_only':True})
 finally:os.close(fd)
write('inventaires/test-index-audio-video.json',patched)
# Fins comparées et voisins immédiats, sans correction des horloges.
frames=js(ROOT/'cartes_sd/recherche-SD-03/20261016/inventaires/frames-cibles.json')
frame={r['inode']:r['last_pts'] for r in frames}
from datetime import datetime,timedelta
ends=[]
for r in js(OUT/'inventaires/tables-ciblees.json'):
 if not r['fat_written'].startswith('2000'):continue
 start=datetime.fromisoformat(r['name_start']);ts={t['kind']:t for t in r['inspection']['tracks']};last=float(r.get('frame_audit',{}).get('last_pts') or frame.get(r['inode'],0))
 ends.append({'card':r['card'],'inode':r['inode'],'start':str(start),'audio_end':str(start+timedelta(seconds=ts['soun']['duration_seconds'])),'video_table_end':str(start+timedelta(seconds=ts['vide']['duration_seconds'])),'last_decoded_pts_end':str(start+timedelta(seconds=last)),'last_decoded_pts':last})
write('inventaires/fins-comparees.json',ends)
write('journaux/validation.json',{'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'manifestes_compares':len(checks),'mismatches':mismatches,'patch_tests':len(patched),'remaining_wrong_sample_count':sum(r['wrong_sample_count'] for r in patched)})
print('Empreintes historiques',len(checks),'écarts',len(mismatches),'non couvertes',len(uncovered),'SD02 actifs',len(diffs),'tests index',len(patched),'wrong sample count restants',sum(r['wrong_sample_count'] for r in patched))
