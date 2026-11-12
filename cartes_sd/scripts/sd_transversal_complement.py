#!/usr/bin/env python3
"""Compléments bornés sur dérivés locaux ; aucune écriture des médias."""
import array, csv, datetime as dt, hashlib, json, math, os, pathlib, struct, subprocess, sys
ROOT=pathlib.Path(__file__).resolve().parents[2]
OUT=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'cartes_sd/recherche-transversale/20261016');assert OUT.resolve().is_relative_to(ROOT/'cartes_sd/recherche-transversale')
sources={}
def read(p):
 b=p.read_bytes();sources[str(p.relative_to(ROOT))]={'size':len(b),'sha256':hashlib.sha256(b).hexdigest()};return b
def js(p):return json.loads(read(p))
def write(n,v):
 with (OUT/n).open('x') as f:json.dump(v,f,ensure_ascii=False,indent=2)
x=js(OUT/'inventaires/tables-ciblees.json');fat=[]
for r in js(ROOT/'cartes_sd/recherche-SD-01/20261016-complement/inventaires/traces-fat-1999-2000.json'):
 b=read(ROOT/r['raw_copy']);offset=r['raw_copy_slot_offset'];assert b[offset:offset+32].hex()==r['raw_hex'];fat.append({'path':r['path'],'offset':r['absolute_entry_offset'],'binary_copy':r['raw_copy'],'verified':True})
write('inventaires/fat-SD01-contrelecture.json',fat)
extras=[];holes=[]
for r in x:
 for t in r['inspection']['tracks']:
  if t['kind']=='vide' and t['last_field']!=t['expected_last']:
   extras.append({'card':r['card'],'inode':r['inode'],'last':t['last_field'],'expected':t['expected_last'],'excess':t['last_field']-t['expected_last'],'multiple13':(t['last_field']-t['expected_last'])%13==0})
 for h in r['inspection']['mdat_unreferenced_ranges']:
  b=read(ROOT/r['source_artifact']);seg=b[h['offset']:h['offset']+h['bytes']];holes.append({'card':r['card'],'inode':r['inode'],**h,'nonzero':sum(v!=0 for v in seg),'sha256':hashlib.sha256(seg).hexdigest(),'first32':seg[:32].hex()})
write('inventaires/compteurs-video-et-zones-non-indexees.json',{'excess_video':extras,'mdat_ranges':holes})
# Distribution SD-02 absente des colonnes de chronologie ; reprise des métadonnées produites.
diffs=[]
base=ROOT/'cartes_sd/recherche-SD-02/20261016/inventaires/medias'
for p in sorted(base.glob('*.json')):
 r=js(p);streams=r.get('metadata',{}).get('streams',[])
 a=next((s for s in streams if s.get('codec_type')=='audio'),{});v=next((s for s in streams if s.get('codec_type')=='video'),{})
 if a.get('duration') and v.get('duration'):diffs.append((float(a['duration'])-float(v['duration']),r['inode']))
write('inventaires/ecarts-audio-video-SD02.json',{'count':len(diffs),'min':min(diffs,default=None),'max':max(diffs,default=None),'top_ten':sorted(diffs,reverse=True)[:10]})
# Test audio Octobre : un seul compteur modifié en RAM ; pas d'écoute ni de transcription.
r=next(r for r in x if r['card']=='SD-03' and r['inode']=='714049800');b=read(ROOT/r['source_artifact']);assert hashlib.sha256(b).hexdigest()==r['sha256'];fixed=bytearray(b)
for p in r['inspection']['patches']:
 if p['kind']=='soun':struct.pack_into('>I',fixed,p['offset'],p['new'])
fd=os.memfd_create('sd03-octobre-controle',0);os.write(fd,fixed)
try:
 path='/proc/self/fd/'+str(fd)
 argv=['ffmpeg','-v','warning','-threads','1','-i',path,'-map','0:a:0','-f','s16le','-acodec','pcm_s16le','-']
 proc=subprocess.run(argv,pass_fds=(fd,),capture_output=True,timeout=120);pcm=array.array('h');pcm.frombytes(proc.stdout)
 if sys.byteorder!='little':pcm.byteswap()
 rms=[]
 for i in range(0,len(pcm),8000):
  chunk=pcm[i:i+8000];rms.append({'start_seconds':i/8000,'samples':len(chunk),'rms':math.sqrt(sum(v*v for v in chunk)/len(chunk)),'peak':max(abs(v) for v in chunk)})
 write('inventaires/audio-714049800.json',{'argv':argv,'returncode':proc.returncode,'stderr':proc.stderr.decode(),'pcm_sha256':hashlib.sha256(proc.stdout).hexdigest(),'samples':len(pcm),'duration':len(pcm)/8000,'windows_1second':rms,'no_semantic_listening':True})
 argv=['ffmpeg','-hide_banner','-loglevel','info','-threads','1','-i',path,'-map','0:v:0','-vf','showinfo','-fps_mode','passthrough','-f','null','-']
 proc=subprocess.run(argv,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=180)
 log=OUT/'journaux/decodage-showinfo-714049800.txt'
 with log.open('xb') as f:f.write(proc.stderr)
 lines=proc.stderr.decode().splitlines();contexts=[]
 for i,line in enumerate(lines):
  if 'error while decoding' in line or 'left block unavailable' in line or 'corrupt' in line:contexts.append(lines[max(0,i-4):i+6])
 write('inventaires/video-erreur-714049800.json',{'argv':argv,'returncode':proc.returncode,'stderr_sha256':hashlib.sha256(proc.stderr).hexdigest(),'contexts':contexts})
finally:os.close(fd)
# Conversions explicites : choix de sens opposés, aucun étalonnage de caméra.
from zoneinfo import ZoneInfo
local=dt.datetime(2000,1,1,0,0,26,tzinfo=ZoneInfo('Europe/Paris'))
write('inventaires/conversion-1999.json',{'local_Paris_to_UTC':local.astimezone(dt.timezone.utc).isoformat(),'UTC_to_Paris':local.replace(tzinfo=dt.timezone.utc).astimezone(ZoneInfo('Europe/Paris')).isoformat(),'meaning':'Deux sens distincts ; logiciel et convention effectivement employés par la cliente inconnus.'})
write('inventaires/sources-complement.json',sources)
write('journaux/execution-complement.json',{'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'argv':sys.argv,'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'image_access':False})
print('Complément terminé',len(diffs),'vidéos SD-02,',len(fat),'slots SD-01,',len(extras),'excès vidéo')
