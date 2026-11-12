"""Essai de récupération d'échantillons au-delà de EOF d'un fichier actif.
Métadonnées reconstruites ; données copiées uniquement depuis sa chaîne allouée.
Ne qualifie pas cette restauration comme une vidéo supprimée distincte.
"""
import array,hashlib,io,json,os,struct,subprocess,sys,tarfile
image=sys.argv[1];g=PARAMS['geometry'];e=PARAMS['entry'];cs=g['cluster_bytes'];base=g['partition_offset_bytes'];dataoff=g['data_absolute_offset'];f=open(image,'rb');f.seek(base+g['reserved_sectors']*512);fat=array.array('I',f.read(g['fat_sectors']*512))
if sys.byteorder!='little':fat.byteswap()
chain=[];c=e['start_cluster'];seen=set()
while 2<=c<g['total_clusters']+2 and c not in seen:
 seen.add(c);chain.append(c);v=fat[c]&0xfffffff
 if v>=0xffffff8:break
 c=v
if len(chain)*cs>16*1024**2:raise ValueError('Prévol')
parts=[]
for c in chain:f.seek(dataoff+(c-2)*cs);parts.append(f.read(cs))
source=b''.join(parts);original=source[:e['size']]
if hashlib.sha256(original).hexdigest()!=PARAMS['source_sha256']:raise ValueError('Source logique différente')
def words(v):return struct.pack('>'+str(len(v))+'I',*v)
def box(typ,p):return words([len(p)+8])+typ+p
def full_table(typ,rows):return box(typ,b'\0'*4+words([len(rows)])+b''.join(words(v) for v in rows))

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

moovbox=next(b for b in inspect(original)['boxes'] if b['path']=='/moov');moov=original[moovbox['offset']:moovbox['offset']+moovbox['size']]
boxes=inspect(moov)['boxes'];parsed={}
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
  n=min([v for v in tables['stsc'] if v[0]<=ix][-1][1],len(tables['stsz'])-cursor)
  for _ in range(n):
   if cursor>=len(tables['stsz']):raise ValueError('STSC trop long')
   size=tables['stsz'][cursor];samples.append(dict(index=cursor,off=off,size=size,ticks=ticks,duration=durations[cursor]));off+=size;ticks+=durations[cursor];cursor+=1
 if cursor!=len(tables['stsz']):raise ValueError('STSC trop court')
 tables['samples']=samples;parsed[kind]=tables

# Expand metadata but clamp the malformed final stsc count to remaining stsz.
def slice_type(payload):
 p=0;types=[];nal_types=[]
 while p+4<=len(payload):
  size=int.from_bytes(payload[p:p+4],'big')
  if not size or p+4+size>len(payload):return None
  n=payload[p+4:p+4+size];nal_types.append(n[0]&31)
  if n[0]&31 in [1,5]:
   rbsp=n[1:].replace(b'\0\0\x03',b'\0\0');bits=''.join(f'{v:08b}' for v in rbsp[:32]);at=0;values=[]
   try:
    for _ in range(3):
     z=0
     while bits[at]=='0':z+=1;at+=1
     at+=1;values.append((1<<z)-1+int(bits[at:at+z] or '0',2));at+=z
    types.append(values[1]%5)
   except (IndexError,ValueError):return None
  p+=4+size
 return dict(slice_types=types,nal_types=nal_types) if p==len(payload) else None
video=parsed['vide'];available=[]
for sample in video['samples']:
 if sample['off']>=e['size'] and sample['off']+sample['size']<=len(source):
  parse=slice_type(source[sample['off']:sample['off']+sample['size']])
  if parse:sample=dict(sample,nal_validation=parse);available.append(sample)
first=next(s for s in available if s['nal_validation']['slice_types'] and all(v in [2,4] for v in s['nal_validation']['slice_types']));start=first['ticks']/video['timescale'];selected={}
for kind,t in parsed.items():
 selected[kind]=[s for s in t['samples'] if s['ticks']/t['timescale']>=start and s['off']>=e['size'] and s['off']+s['size']<=len(source)]
tracks={};combined=[]
for kind,ss in selected.items():
 for sample in ss:combined.append((sample['ticks']/parsed[kind]['timescale'],kind,sample))
body=original[:28]+words([0])+b'mdat';cursor=len(body);payload=[];offsets={'vide':[],'soun':[]}
for _,kind,sample in sorted(combined,key=lambda x:(x[0],x[1])):
 b=source[sample['off']:sample['off']+sample['size']];offsets[kind].append(cursor);payload.append(b);cursor+=len(b)
for kind,ss in selected.items():
 stts=[]
 for sample in ss:
  delta=sample['duration']
  if stts and stts[-1][1]==delta:stts[-1][0]+=1
  else:stts.append([1,delta])
 tracks[kind]=dict(sizes=[s['size'] for s in ss],chunks=[(o,[s['size']]) for o,s in zip(offsets[kind],ss)],stsc=[[1,1,1]],stts=stts,ticks=sum(s['duration'] for s in ss),stss=[[1]] if kind=='vide' else [])
body=body[:28]+words([cursor-28])+body[32:]+b''.join(payload);output=body+rebuild(moov,tracks);r=dict(inode=e['inode'],path=e['path'],logical_size=e['size'],source_sha256=PARAMS['source_sha256'],chain=chain,full_chain_size=len(source),original_relative_start_seconds=start,selected_samples=selected,source_moov_sha256=hashlib.sha256(moov).hexdigest(),sha256=hashlib.sha256(output).hexdigest(),size=len(output),structure=inspect(output),hypotheses='Échantillons après EOF dans la chaîne allouée actuelle, positions des tables originales ; compte de dernier chunk borné aux tailles stsz ; départ sur slice intra analysée ; conteneur neuf et pistes remises séparément à zéro. La cohérence doit être contrôlée par décodage et incrustations.')
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
 def add(name,b):
  t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
 fd=os.memfd_create('sd03-essai-apres-eof',0)
 try:
  with os.fdopen(fd,'wb',closefd=False) as out:out.write(output)
  path='/proc/self/fd/'+str(fd);args=['ffprobe','-v','error','-show_format','-show_streams','-of','json',path];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60);r['ffprobe']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'));r['metadata']=json.loads(p.stdout) if not p.returncode else {}
  args=['ffmpeg','-v','warning','-threads','1','-i',path,'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=120);log='journaux/essai-apres-eof.txt';add(log,p.stderr);r['decode']=dict(argv=args,returncode=p.returncode,stderr_bytes=len(p.stderr),stderr_log=log);r['accepted']=not p.returncode and not p.stderr and not r['structure']['errors'];r['artifact']='prive/'+('reconstructions' if r['accepted'] else 'essais-non-valides')+'/266342024-fragment-apres-EOF.mp4';add(r['artifact'],output)
  previews=[]
  for second in [0,max(0,float(r['metadata'].get('format',{}).get('duration',0))-0.5)]:
   args=['ffmpeg','-v','warning','-i',path,'-ss',str(second),'-frames:v','1','-vf','scale=960:-2','-f','image2pipe','-vcodec','png','pipe:1'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120);artifact='prive/apercus-eof/'+str(round(second,3))+'.png'
   if p.stdout:add(artifact,p.stdout)
   previews.append(dict(requested_second=second,artifact=artifact if p.stdout else None,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'),sha256=hashlib.sha256(p.stdout).hexdigest() if p.stdout else None,argv=args))
  r['previews']=previews
 finally:os.close(fd)
 add('inventaires/recuperation-apres-eof.json',json.dumps(r,ensure_ascii=False,indent=2).encode())
