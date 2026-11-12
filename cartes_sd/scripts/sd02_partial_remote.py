"""Conteneurs dérivés d'un temporaire non finalisé, exclusivement en mémoire.
Grammaire STBL inférée ; conserve les chunks complets dans la borne choisie.
Métadonnées MP4 reconstruites explicitement, jamais présentées comme originales.
"""
import array,hashlib,io,json,os,struct,subprocess,sys,tarfile
LENGTHS={b'vdts':24,b'sdts':12,b'vdsc':20,b'sdsc':20,b'vdco':8,b'sdco':8,b'vdsz':8,b'sdsz':8,b'vdss':8}
image=sys.argv[1];g=PARAMS['geometry'];f=open(image,'rb');cs=g['cluster_bytes'];base=g['partition_offset_bytes'];data=g['data_absolute_offset'];f.seek(base+g['reserved_sectors']*512);fat=array.array('I',f.read(g['fat_sectors']*512))
if sys.byteorder!='little':fat.byteswap()
def read(e,full=False):
 c=e['start_cluster'];parts=[];seen=set()
 while 2<=c<g['total_clusters']+2 and c not in seen:
  seen.add(c);f.seek(data+(c-2)*cs);parts.append(f.read(cs));v=fat[c]&0xfffffff
  if v>=0xffffff8:break
  c=v
 b=b''.join(parts);return b if full else b[:e['size']]
entries={e['inode']:e for e in PARAMS['entries']};source=read(entries['1543'],True);template=read(entries['1547']);journal=read(entries['1551']);records={};pos=0
while pos<len(journal):
 tag=journal[pos:pos+4];length=LENGTHS.get(tag)
 if length is None or pos+length>len(journal):raise ValueError('Journal non analysable')
 vals=list(struct.unpack('>'+str((length-4)//4)+'I',journal[pos+4:pos+length]));records.setdefault(tag.decode(),[]).append(vals);pos+=length

def box(typ,payload):return struct.pack('>I',len(payload)+8)+typ+payload
def words(vals):return struct.pack('>'+str(len(vals))+'I',*vals)
def full_table(typ,rows):return box(typ,b'\0'*4+words([len(rows)])+b''.join(words(v) for v in rows))
def timing(count):
 times=[0]*len(records['vdsz']);previous_index=0;previous_time=0;previous_delta=0
 for v in records['vdts']:
  index=v[3]
  if index==0:continue
  for i in range(previous_index+1,index):times[i]=previous_time+previous_delta*(i-previous_index)
  predicted=previous_time+previous_delta*(index-previous_index-1)+v[2]
  if predicted!=v[4]:raise ValueError('Cumul vdts incohérent')
  times[index]=v[4];previous_index=index;previous_time=v[4];previous_delta=v[2]
 if count>=len(times):raise ValueError('Dernière durée non documentée')
 durations=[times[i+1]-times[i] for i in range(count)];runs=[]
 for delta in durations:
  if delta<=0:raise ValueError('Durée non positive')
  if runs and runs[-1][1]==delta:runs[-1][0]+=1
  else:runs.append([1,delta])
 return runs,sum(durations)

def rebuild(template,tracks):
 # Read timescales from the actual per-track template.
 boxes=inspect(template)['boxes'];scales={}
 for tr in [x for x in boxes if x['path']=='/moov/trak']:
  children=[x for x in boxes if tr['offset']<x['offset']<tr['offset']+tr['size']];hdlr=next(x for x in children if x['path'].endswith('/hdlr'));kind=template[hdlr['offset']+16:hdlr['offset']+20].decode();mdhd=next(x for x in children if x['path'].endswith('/mdhd'));scales[kind]=int.from_bytes(template[mdhd['offset']+20:mdhd['offset']+24],'big')
 mvhd=next(x for x in boxes if x['path']=='/moov/mvhd');moviescale=int.from_bytes(template[mvhd['offset']+20:mvhd['offset']+24],'big');seconds=max(t['ticks']/scales[k] for k,t in tracks.items())
 containers={b'moov',b'trak',b'mdia',b'minf',b'stbl',b'edts',b'dinf',b'udta'}
 def rewrite(blob,kind=None):
  result=b'';p=0
  while p+8<=len(blob):
   size=int.from_bytes(blob[p:p+4],'big');typ=blob[p+4:p+8];payload=blob[p+8:p+size]
   if size<8 or p+size>len(blob):raise ValueError('Modèle de boîte invalide')
   local_kind=kind
   if typ==b'trak':
    # hdlr is nested but occurs once in each track.
    at=blob[p:p+size].find(b'hdlr');local_kind=blob[p+at+12:p+at+16].decode()
   t=tracks.get(local_kind)
   if typ in containers:payload=rewrite(payload,local_kind)
   elif typ==b'mvhd':payload=payload[:16]+words([round(seconds*moviescale)])+payload[20:]
   elif typ==b'tkhd':payload=payload[:20]+words([round(t['ticks']/scales[local_kind]*moviescale)])+payload[24:]
   elif typ==b'mdhd':payload=payload[:16]+words([t['ticks']])+payload[20:]
   elif t and typ==b'stts':result+=full_table(typ,t['stts']);p+=size;continue
   elif t and typ==b'stsc':result+=full_table(typ,t['stsc']);p+=size;continue
   elif t and typ==b'stsz':payload=b'\0'*4+words([0,len(t['sizes'])]+t['sizes'])
   elif t and typ==b'stco':result+=full_table(typ,[[o] for o,_ in t['chunks']]);p+=size;continue
   elif t and typ==b'stss':result+=full_table(typ,t['stss']);p+=size;continue
   result+=box(typ,payload);p+=size
  if p!=len(blob):raise ValueError('Fin de modèle non traitée')
  return result
 return rewrite(template)

e=PARAMS['previous_entry'];clusters=PARAMS['tail_clusters'];parts=[]
for c in clusters:
 if fat[c]&0xfffffff:raise ValueError('Cluster du fragment alloué')
 f.seek(data+(c-2)*cs);parts.append(f.read(cs))
missing=((e['size']+cs-1)//cs-len(clusters))*cs;tail=b''.join(parts)[:e['size']-missing];at=tail.find(b'moov')-4
if at<0:raise ValueError('MOOV absent')
length=int.from_bytes(tail[at:at+4],'big')
if at+length!=len(tail):raise ValueError('MOOV non terminal')
moov=tail[at:];boxes=inspect(moov)['boxes'];parsed={}
for tr in [x for x in boxes if x['path']=='/moov/trak']:
 children=[x for x in boxes if tr['offset']<x['offset']<tr['offset']+tr['size']];hdlr=next(x for x in children if x['path'].endswith('/hdlr'));kind=moov[hdlr['offset']+16:hdlr['offset']+20].decode();tables={}
 for x in children:
  typ=x['path'].split('/')[-1];p=moov[x['offset']+8:x['offset']+x['size']]
  if typ in ['stco','stss']:
   count=int.from_bytes(p[4:8],'big');tables[typ]=list(struct.unpack('>'+str(count)+'I',p[8:8+4*count]))
  elif typ in ['stsc','stts']:
   width=3 if typ=='stsc' else 2;count=int.from_bytes(p[4:8],'big');tables[typ]=[list(struct.unpack('>'+str(width)+'I',p[8+i*width*4:8+(i+1)*width*4])) for i in range(count)]
  elif typ=='stsz':
   uniform=int.from_bytes(p[4:8],'big');count=int.from_bytes(p[8:12],'big');tables[typ]=[uniform]*count if uniform else list(struct.unpack('>'+str(count)+'I',p[12:12+4*count]))
  elif typ=='mdhd':tables['timescale']=int.from_bytes(p[12:16],'big')
 samples=[];cursor=0
 durations=[delta for count,delta in tables['stts'] for _ in range(count)]
 if len(durations)!=len(tables['stsz']):raise ValueError('Durées/taille incohérentes')
 ticks=0
 for ix,off in enumerate(tables['stco'],1):
  n=[v for v in tables['stsc'] if v[0]<=ix][-1][1]
  for _ in range(n):
   if cursor>=len(tables['stsz']):raise ValueError('STSC trop long')
   size=tables['stsz'][cursor];samples.append(dict(index=cursor,off=off,size=size,ticks=ticks,duration=durations[cursor]));off+=size;ticks+=durations[cursor];cursor+=1
 if cursor!=len(tables['stsz']):raise ValueError('STSC trop court')
 tables['samples']=samples;parsed[kind]=tables
video=parsed['vide'];syncs={v-1 for v in video['stss']};first=next(s for s in video['samples'] if s['index'] in syncs and missing<=s['off'] and s['off']+s['size']<=missing+at);start_seconds=first['ticks']/video['timescale'];selected={}
for kind,t in parsed.items():
 selected[kind]=[s for s in t['samples'] if s['ticks']/t['timescale']>=start_seconds and missing<=s['off'] and s['off']+s['size']<=missing+at]
tracks={};combined=[]
for kind,ss in selected.items():
 for s in ss:combined.append((s['ticks']/parsed[kind]['timescale'],kind,s))
body=read(entries['1543'])[:28]+words([0])+b'mdat';cursor=len(body);payload=[];new_offsets={'vide':[],'soun':[]}
for _,kind,s in sorted(combined,key=lambda x:(x[0],x[1])):
 b=tail[s['off']-missing:s['off']-missing+s['size']]
 if len(b)!=s['size']:raise ValueError('Échantillon court')
 new_offsets[kind].append(cursor);payload.append(b);cursor+=len(b)
for kind,ss in selected.items():
 stts=[]
 for sample in ss:
  delta=sample['duration']
  if stts and stts[-1][1]==delta:stts[-1][0]+=1
  else:stts.append([1,delta])
 first_index=ss[0]['index'];last_index=ss[-1]['index'];tracks[kind]=dict(sizes=[s['size'] for s in ss],chunks=[(off,[sample['size']]) for off,sample in zip(new_offsets[kind],ss)],stsc=[[1,1,1]],stts=stts,ticks=sum(s['duration'] for s in ss),stss=[[v-first_index] for v in parsed[kind].get('stss',[]) if first_index<v<=last_index+1])
body=body[:28]+words([cursor-28])+body[32:]+b''.join(payload);output=body+rebuild(moov,tracks);artifact='prive/recuperations/575101252-fragment-final.mp4';r=dict(inode=e['inode'],original_path=e['path'],original_declared_size=e['size'],tail_clusters=clusters,inferred_missing_prefix_bytes=missing,surviving_tail_bytes=len(tail),original_moov_offset=at+missing,original_moov_sha256=hashlib.sha256(moov).hexdigest(),first_retained_original_video_sample=first['index']+1,original_start_seconds=start_seconds,tracks={k:dict(samples=len(v['sizes']),ticks=v['ticks'],timescale=parsed[k]['timescale'],original_first_ticks=selected[k][0]['ticks']) for k,v in tracks.items()},artifact=artifact,sha256=hashlib.sha256(output).hexdigest(),size=len(output),metadata_rebuilt=True,structure=inspect(output),hypotheses='Ordre physique croissant des seuls clusters libres non auxiliaires du reliquat terminal ; position logique ancrée par taille déclarée et MOOV terminal ; conteneur neuf, horloges des pistes ramenées séparément à zéro, décalage A/V inférieur à un échantillon audio possible')
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
 def add(name,b):
  t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
 add(artifact,output);add('prive/recuperations/575101252-moov.bin',moov)
 fd=os.memfd_create('sd02-fragment-final',0)
 try:
  with os.fdopen(fd,'wb',closefd=False) as out:out.write(output)
  path='/proc/self/fd/'+str(fd);args=['ffprobe','-v','error','-show_format','-show_streams','-of','json',path];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60);r['ffprobe']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'));r['metadata']=json.loads(p.stdout) if not p.returncode else {}
  args=['ffmpeg','-v','warning','-threads','1','-i',path,'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=600);log='journaux/recuperations/575101252-fragment-final.txt';add(log,p.stderr);r['decode']=dict(argv=args,returncode=p.returncode,stderr_bytes=len(p.stderr),log=log)
  previews=[]
  for second in [0,60]:
   args=['ffmpeg','-v','error','-ss',str(second),'-i',path,'-frames:v','1','-vf','scale=960:-2','-f','image2pipe','-vcodec','png','pipe:1'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60);name='prive/apercus/fragment-final-'+str(second)+'.png';add(name,p.stdout);previews.append(dict(artifact=name,argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'),sha256=hashlib.sha256(p.stdout).hexdigest()))
  r['previews']=previews
 finally:os.close(fd)
 add('inventaires/recuperation-fragment-final.json',json.dumps(r,ensure_ascii=False,indent=2).encode())
