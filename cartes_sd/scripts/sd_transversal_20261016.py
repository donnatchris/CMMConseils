#!/usr/bin/env python3
"""Contrôle local ciblé, indépendant des parseurs antérieurs. Aucune lecture d'image."""
import argparse, bisect, collections, csv, datetime as dt, hashlib, json, pathlib, struct, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
p = argparse.ArgumentParser(); p.add_argument('--out', default='cartes_sd/recherche-transversale/20261016'); args=p.parse_args()
OUT=(ROOT/args.out).resolve(); assert OUT.is_relative_to(ROOT/'cartes_sd/recherche-transversale')
OUT.mkdir(parents=True,exist_ok=True)
for d in ('inventaires','journaux'): (OUT/d).mkdir(exist_ok=True)
sources={}
def digest(b): return hashlib.sha256(b).hexdigest()
def read(path):
 path=path.resolve(); b=path.read_bytes(); sources[str(path.relative_to(ROOT))]={'size':len(b),'sha256':digest(b)}; return b
def js(path): return json.loads(read(path))
def write(name,obj):
 with (OUT/name).open('x') as f: json.dump(obj,f,ensure_ascii=False,indent=2)
def csvout(name,rows):
 with (OUT/name).open('x') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def table(b,box,width):
 pos,size=box; n=struct.unpack_from('>I',b,pos+12)[0]; assert size==16+n*4*width
 return [struct.unpack_from('>'+'I'*width,b,pos+16+4*width*i) for i in range(n)]
def children(b,start,end):
 out=[]
 while start<end:
  assert start+8<=end
  size,typ=struct.unpack_from('>I4s',b,start); assert size>=8 and start+size<=end
  out.append((typ,(start,size)));start+=size
 return out
def inspect(b):
 top=children(b,0,len(b)); moov=dict(top)[b'moov']; mdats=[(v[0]+8,sum(v)) for t,v in top if t==b'mdat']; tracks=[]; spans=[]; patches=[]
 for typ,tr in children(b,moov[0]+8,sum(moov)):
  if typ!=b'trak': continue
  mdia=dict(children(b,tr[0]+8,sum(tr)))[b'mdia']; mc=dict(children(b,mdia[0]+8,sum(mdia))); hp=mc[b'hdlr'][0]; kind=b[hp+16:hp+20].decode(); mh=mc[b'mdhd'][0]; assert b[mh+8]==0
  scale=struct.unpack_from('>I',b,mh+20)[0]; mi=mc[b'minf']; st=dict(children(b,mi[0]+8,sum(mi)))[b'stbl']; boxes=dict(children(b,st[0]+8,sum(st)))
  sc=table(b,boxes[b'stsc'],3); co=[v[0] for v in table(b,boxes[b'stco'],1)]; ts=table(b,boxes[b'stts'],2); sz=boxes[b'stsz']; uniform,n=struct.unpack_from('>II',b,sz[0]+12)
  sizes=[uniform]*n if uniform else list(struct.unpack_from('>'+'I'*n,b,sz[0]+20)); assert sz[1]==20+(0 if uniform else 4*n)
  pts=[];time=0
  for count,duration in ts:
   for _ in range(count): pts.append(time/scale);time+=duration
  assert len(pts)==n
  counts=[]
  for ci in range(1,len(co)+1): counts.append(sc[bisect.bisect_right([r[0] for r in sc],ci)-1][1])
  previous=sum(counts[:-1]); remaining=n-previous; last=counts[-1]
  r={'kind':kind,'sample_count':n,'chunk_count':len(co),'stsc_rows':sc,'stsc_offset':boxes[b'stsc'][0],'previous_samples':previous,'last_field':last,'expected_last':remaining,'cumulative_defect':last==previous and last!=remaining,'declared_chunk_samples':sum(counts),'duration_seconds':time/scale,'last_sample_pts':pts[-1], 'stsd_sha256':digest(b[boxes[b'stsd'][0]:sum(boxes[b'stsd'])])}
  if len(sc)>1 and sc[-1][0]==len(co) and 0<remaining and last!=remaining:
   patches.append({'kind':kind,'offset':boxes[b'stsc'][0]+16+(len(sc)-1)*12+4,'old':last,'new':remaining})
  # Mapping intrinsèque existant : tailles bornées par stsz, aucun octet inventé.
  sample=0; bad=[]; outside=[]; nal_bad=[]; nal_types=collections.Counter(); chunk_details=[]
  avcc=b.find(b'avcC',boxes[b'stsd'][0],sum(boxes[b'stsd'])); nal_width=(b[avcc+8]&3)+1 if avcc>=0 else None
  for ci,(off,count) in enumerate(zip(co,counts),1):
   begin=sample; actual=sizes[sample:min(sample+count,n)]; end=off+sum(actual)
   if not any(a<=off<=end<=z for a,z in mdats): outside.append({'chunk':ci,'offset':off,'end':end,'first_sample':sample+1})
   if actual:spans.append((off,end,kind,ci))
   chunk_details.append({'chunk':ci,'offset':off,'end':end,'first_sample':sample+1,'available_sizes':len(actual),'announced_samples':count})
   for j,s in enumerate(actual):
    idx=begin+j
    if kind=='vide':
     end_sample=off+s; pos=off; error=None
     while pos<end_sample:
      if pos+nal_width>end_sample or end_sample>len(b):error='length_or_sample_outside';break
      length=int.from_bytes(b[pos:pos+nal_width],'big');pos+=nal_width
      if length<=0 or pos+length>end_sample:error='NAL_length_outside_sample';break
      if b[pos]&128:error='forbidden_zero_bit';break
      nal_types[b[pos]&31]+=1;pos+=length
     if error:nal_bad.append({'sample':idx+1,'chunk':ci,'offset':off,'size':s,'pts':pts[idx],'error':error})
    off+=s
   sample+=count
  r.update(chunks_outside_mdat=outside,nal_length_width=nal_width,nal_errors=nal_bad,nal_type_counts=dict(nal_types),last_chunks=chunk_details[-3:])
  tracks.append(r)
 # Couverture des tailles réellement disponibles (ne valide pas les compteurs fautifs).
 sortedsp=sorted(spans);holes=[];overlaps=[]
 for a,z in mdats:
  cursor=a
  for left,right,kind,ci in sortedsp:
   if right<=a or left>=z:continue
   if left>cursor:holes.append({'offset':cursor,'bytes':left-cursor})
   if left<cursor:overlaps.append({'offset':left,'bytes':min(cursor,right)-left,'kind':kind,'chunk':ci})
   cursor=max(cursor,min(right,z))
  if cursor<z:holes.append({'offset':cursor,'bytes':z-cursor})
 return {'top_boxes':[(t.decode(),v) for t,v in top], 'tracks':tracks,'patches':patches,'mdat_unreferenced_ranges':holes,'mdat_overlap_ranges':overlaps}

campaigns={c:ROOT/f'cartes_sd/recherche-SD-{c}'/('20261015' if c=='01' else '20261016') for c in ['01','02','03']}
rows={c:list(csv.DictReader(read(base/('inventaires/videos.csv' if c=='01' else 'inventaires/chronologie.csv')).decode().splitlines())) for c,base in campaigns.items()}
# Ensemble : 7 anomalies SD-01, témoins voisins ; 10 anomalies SD-03 et témoins ; 3 SD-02 finalisés.
selected=[]
an01=js(campaigns['01']/'inventaires/mp4-anomalies.json')
ids01={str(r['inode']) for r in an01 if not r.get('deleted')}
for c in ['01','03']:
 rr=[r for r in rows[c] if r.get('name_start') and r['allocation'] in ('alloue','alloué')]
 for i,r in enumerate(rr):
  if (c=='01' and r['inode'] in ids01) or (c=='03' and (r['fat_written'].startswith('2000') or r['inode']=='172620304')):
   for j in range(max(0,i-1),min(len(rr),i+2)):
    if (c,rr[j]['inode']) not in [(cc,e['inode']) for cc,e in selected]: selected.append((c,rr[j]))
for inode in ['273341448','657582352','657582356']:
 selected.append(('02',next(r for r in rows['02'] if r['inode']==inode)))
results=[]
for c,r in selected:
 base=campaigns[c]
 if c=='01': artifact=r['artifact']
 else: artifact=js(base/f"inventaires/medias/{r['inode']}.json").get('artifact')
 if not artifact or not (base/artifact).exists():
  matches=list((base/'prive').rglob(r['inode']+'_*.mp4'))
  if not matches:continue
  path=matches[0]
 else:path=base/artifact
 b=read(path);assert digest(b)==r['sha256'],path
 result={'card':'SD-'+c,'inode':r['inode'],'path':r['path'],'source_artifact':str(path.relative_to(ROOT)),'sha256':digest(b),'fat_created':r['fat_created'],'fat_written':r['fat_written'],'name_start':r['name_start'],'inspection':inspect(b)}
 if c=='01' and r['inode'] in ['20903944','22835208']:
  argv=['ffprobe','-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time,pkt_pos,pict_type','-of','json',str(path)]
  proc=subprocess.run(argv,capture_output=True,timeout=180); frames=json.loads(proc.stdout).get('frames',[])
  write('inventaires/frames-SD01-'+r['inode']+'.json',frames)
  (OUT/('journaux/frames-SD01-'+r['inode']+'.txt')).write_bytes(proc.stderr)
  result['frame_audit']={'argv':argv,'returncode':proc.returncode,'frame_count':len(frames),'last_pts':frames[-1].get('best_effort_timestamp_time') if frames else None,'stderr_bytes':len(proc.stderr)}
 # Nouvelle expérience index seulement : ffprobe léger sur copie anonyme RAM, tous les fichiers aux dates 2000.
 if r['fat_written'].startswith('2000'):
  import os
  fixed=bytearray(b)
  for patch in result['inspection']['patches']:
   if patch['kind']=='soun': struct.pack_into('>I',fixed,patch['offset'],patch['new'])
  fd=os.memfd_create('transversal-index',0)
  try:
   os.write(fd,fixed);argv=['ffprobe','-v','error','-show_streams','-of','json','/proc/self/fd/'+str(fd)]
   proc=subprocess.run(argv,pass_fds=(fd,),capture_output=True,timeout=60)
   result['audio_index_test']={'argv':argv,'returncode':proc.returncode,'stderr':proc.stderr.decode(),'patched_sha256':digest(fixed),'changed_bytes':[i for i,(a,z) in enumerate(zip(b,fixed)) if a!=z],'only_in_RAM':True}
  finally:os.close(fd)
 results.append(result)
write('inventaires/tables-ciblees.json',results)
flat=[]
for r in results:
 for t in r['inspection']['tracks']:
  flat.append({k:r[k] for k in ['card','inode','path','fat_written']}|{k:t[k] for k in ['kind','sample_count','chunk_count','previous_samples','last_field','expected_last','cumulative_defect','duration_seconds','last_sample_pts']}|{'nal_error_count':len(t['nal_errors']),'chunks_outside_mdat':len(t['chunks_outside_mdat'])})
csvout('inventaires/tables-ciblees.csv',flat)
# Valeurs FAT décodées indépendamment des champs texte et contrôlées sur copies binaires.
fatchecks=[]
for c,fn in [('01','lecture-fat-independante-v2.json'),('02','lecture-fat-v2.json'),('03','lecture-fat.json')]:
 base=campaigns[c];fat=js(base/'inventaires'/fn)
 for e in fat['entries']:
  raw=bytes.fromhex(e['raw_hex'])
  if not any(struct.unpack_from('<H',raw,o)[0]>>9==20 for o in (16,18,24)):continue
  offset=e['absolute_entry_offset'];cluster=2+(offset-19771392)//16384;incluster=(offset-19771392)%16384
  # fichiers de répertoire nommés par cluster ; cf. index des structures.
  dirs=[d for d in fat['directories'] if cluster in d['clusters']]
  verified=False;copy_path=None
  if dirs:
   d=dirs[0];copy=base/f"prive/repertoires/{d['start_cluster']}.bin"
   if copy.exists():
    bb=read(copy);idx=d['clusters'].index(cluster)*16384+incluster;assert bb[idx:idx+32]==raw; verified=True;copy_path=str(copy.relative_to(ROOT))
  def date(off):
   v=struct.unpack_from('<H',raw,off)[0];return [1980+(v>>9),(v>>5)&15,v&31]
  fatchecks.append({'card':'SD-'+c,'path':e['path'],'offset':offset,'raw_hex':e['raw_hex'],'created_date':date(16),'written_date':date(24),'access_date':date(18),'creation_time_word':struct.unpack_from('<H',raw,14)[0],'creation_tenths':raw[13],'write_time_word':struct.unpack_from('<H',raw,22)[0],'binary_copy_verified':verified,'binary_copy':copy_path})
write('inventaires/fat-2000.json',fatchecks)
# Chronologie croisée, périodes demandées, sans inventer un étalonnage.
chron=[]
for c,rr in rows.items():
 for r in rr:
  start=r.get('name_start','')
  if start and (start[:10] in ['2024-02-21','2024-02-29','2024-03-01','2024-10-15']):
   chron.append({'card':'SD-'+c,**{k:r.get(k,'') for k in ['inode','path','name_start','fat_created','fat_written','estimated_end','video_duration','audio_duration']},'duration':r.get('duration',r.get('ffprobe_duration',''))})
csvout('inventaires/chronologie-croisee.csv',sorted(chron,key=lambda r:(r['name_start'],r['card'])))
# Examen de la distribution audio-vidéo : métadonnées réutilisées, pas de décodage exhaustif.
distributions={}
for c in ['01','02','03']:
 diffs=[]
 if c=='01':
  for r in rows[c]:
   meta=js(campaigns[c]/f"journaux/ffprobe/{r['inode']}.json") if (campaigns[c]/f"journaux/ffprobe/{r['inode']}.json").exists() else None
   if meta:
    streams=meta.get('streams',[]);a=next((s for s in streams if s['codec_type']=='audio'),{});v=next((s for s in streams if s['codec_type']=='video'),{})
    if 'duration' in a and 'duration' in v:diffs.append((float(a['duration'])-float(v['duration']),r['inode']))
 else:
  for r in rows[c]:
   if r.get('audio_duration') and r.get('video_duration'):diffs.append((float(r['audio_duration'])-float(r['video_duration']),r['inode']))
 distributions[c]={'count':len(diffs),'min':min(diffs,default=None),'max':max(diffs,default=None),'top_ten':sorted(diffs,reverse=True)[:10]}
write('inventaires/ecarts-audio-video.json',distributions)
# Sources documentaires et codes consultés, empreintés sans recopier les médias.
for f in ['docs/mail.txt','remise-documents/attestation-de-remise.md','cartes_sd/analyse-cartes_sd.md','generer-pdf/commande.md','discussion-chat.md']+[f'cartes_sd/analyse-cartes_sd-SD-{c}.md' for c in campaigns]:read(ROOT/f)
write('inventaires/sources.json',sources)
write('journaux/execution.json',{'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'argv':sys.argv,'python':sys.version,'ffprobe':subprocess.run(['ffprobe','-version'],capture_output=True,text=True).stdout.splitlines()[0],'files_checked':len(results),'source_count':len(sources),'image_access':False,'script_sha256':digest(pathlib.Path(__file__).read_bytes())})
print(json.dumps({'files':len(results),'tracks':len(flat),'fat_slots':len(fatchecks),'binary_slots_verified':sum(e['binary_copy_verified'] for e in fatchecks),'date2000_cases':[(r['card'],r['inode']) for r in results if r['fat_written'].startswith('2000')]},indent=2))
