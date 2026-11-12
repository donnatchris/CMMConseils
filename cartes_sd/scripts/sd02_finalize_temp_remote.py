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

def make(limit):
 tracks={}
 for prefix in ['vd','sd']:
  sizes=[v[0] for v in records[prefix+'sz']];offs=[v[0] for v in records[prefix+'co']];sc=records[prefix+'sc'];cursor=0;chunks=[]
  for ix,off in enumerate(offs,1):
   n=min([v for v in sc if v[0]<=ix][-1][1],len(sizes)-cursor);chunk_sizes=sizes[cursor:cursor+n]
   if off+sum(chunk_sizes)>limit:break
   chunks.append((off,chunk_sizes));cursor+=n
  if not chunks:raise ValueError('Aucun chunk complet')
  sz=[size for _,ss in chunks for size in ss];stsc=[]
  for ix,(_,ss) in enumerate(chunks,1):
   if not stsc or stsc[-1][1]!=len(ss):stsc.append([ix,len(ss),1])
  stts,ticks=timing(len(sz)) if prefix=='vd' else ([[len(sz),1024]],len(sz)*1024)
  tracks['vide' if prefix=='vd' else 'soun']=dict(sizes=sz,chunks=chunks,stsc=stsc,stts=stts,ticks=ticks,stss=[v for v in records.get('vdss',[]) if v[0]<=len(sz)])
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
 end=max(off+sum(ss) for t in tracks.values() for off,ss in t['chunks']);body=source[:end];body=body[:28]+words([len(body)-28])+body[32:];moov=rewrite(template);output=body+moov
 return output,dict(source_limit=limit,retained_source_bytes=end,mp4_metadata_rebuilt=True,tracks={k:dict(samples=len(v['sizes']),chunks=len(v['chunks']),timescale=scales[k],ticks=v['ticks']) for k,v in tracks.items()},seconds=seconds,moov_sha256=hashlib.sha256(moov).hexdigest())
results=[]
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
 def add(name,b):
  t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
 for label,limit in [('taille-logique',entries['1543']['size']),('chaine-complete',len(source))]:
  b,r=make(limit);r.update(label=label,size=len(b),sha256=hashlib.sha256(b).hexdigest(),structure=inspect(b));artifact='prive/reconstructions/temp-'+label+'.mp4';add(artifact,b);r['artifact']=artifact
  fd=os.memfd_create('sd02-temp-reconstruit',0)
  try:
   with os.fdopen(fd,'wb',closefd=False) as out:out.write(b)
   path='/proc/self/fd/'+str(fd);args=['ffprobe','-v','error','-show_format','-show_streams','-of','json',path];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60);r['ffprobe']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'));r['metadata']=json.loads(p.stdout) if not p.returncode else {}
   args=['ffmpeg','-v','warning','-threads','1','-i',path,'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=600);log='journaux/reconstruction-temp-'+label+'.txt';add(log,p.stderr);r['decode']=dict(argv=args,returncode=p.returncode,stderr_bytes=len(p.stderr),log=log)
  finally:os.close(fd)
  results.append(r)
 add('inventaires/reconstructions-temporaires.json',json.dumps(dict(journal_sha256=hashlib.sha256(journal).hexdigest(),template_sha256=hashlib.sha256(template).hexdigest(),entries=results),ensure_ascii=False,indent=2).encode())
