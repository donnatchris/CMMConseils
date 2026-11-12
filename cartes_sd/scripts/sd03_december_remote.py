import struct
"""Aperçus ponctuels depuis les chaînes FAT actives, décodés dans SIFT en RAM."""
import array,hashlib,io,json,os,subprocess,sys,tarfile
image=sys.argv[1];g=PARAMS['geometry'];f=open(image,'rb');base=g['partition_offset_bytes'];cs=g['cluster_bytes'];data=g['data_absolute_offset'];f.seek(base+g['reserved_sectors']*512);fat=array.array('I',f.read(g['fat_sectors']*512))
if sys.byteorder!='little':fat.byteswap()
records=[]
def read(e):
 c=e['start_cluster'];seen=set();parts=[];left=e['size']
 if left>256*1024**2:raise ValueError('Prévol média')
 while 2<=c<g['total_clusters']+2 and c not in seen and left:
  seen.add(c);f.seek(data+(c-2)*cs);part=f.read(min(cs,left));parts.append(part);left-=len(part);v=fat[c]&0xfffffff
  if v>=0xffffff8:break
  c=v
 if left:raise ValueError('Chaîne courte')
 return b''.join(parts)
results=[]
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
 def add(name,b):
  t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
 for e in PARAMS['entries']:
  b=read(e);structure=inspect(b);details=[];patches=[]
  for tr in [x for x in structure['boxes'] if x['path']=='/moov/trak']:
   children=[x for x in structure['boxes'] if tr['offset']<x['offset']<tr['offset']+tr['size']];h=next(x for x in children if x['path'].endswith('/hdlr'));kind=b[h['offset']+16:h['offset']+20].decode();sc=next(x for x in children if x['path'].endswith('/stsc'));co=next(x for x in children if x['path'].endswith('/stco'));sz=next(x for x in children if x['path'].endswith('/stsz'));payload=b[sc['offset']+8:sc['offset']+sc['size']];count=int.from_bytes(payload[4:8],'big');rows=[list(struct.unpack_from('>III',payload,8+12*i)) for i in range(count)];chunks=int.from_bytes(b[co['offset']+12:co['offset']+16],'big');samples=int.from_bytes(b[sz['offset']+16:sz['offset']+20],'big')
   previous=sum([r for r in rows if r[0]<=i][-1][1] for i in range(1,chunks));last=[r for r in rows if r[0]<=chunks][-1];expected=samples-previous;record=dict(kind=kind,samples=samples,chunks=chunks,last_stsc_row=last,samples_before_last_chunk=previous,remaining_for_last_chunk=expected,last_field_equals_previous_cumulative=last[1]==previous,last_field_correct=last[1]==expected)
   if kind=='soun' and rows[-1][0]==chunks and expected>0 and last[1]!=expected:
    offset=sc['offset']+16+12*(len(rows)-1)+4;patches.append(dict(offset=offset,old=last[1],new=expected,kind=kind,meaning='Remplace seulement le nombre audio du dernier chunk par stsz moins le cumul des précédents ; hypothèse corrective, pas preuve de cause'))
   details.append(record)
  result=dict(inode=e['inode'],path=e['path'],source_sha256=hashlib.sha256(b).hexdigest(),table_observations=details,proposed_patches=patches)
  if e['inode']==PARAMS['test_inode'] and patches:
   fixed=bytearray(b)
   for patch in patches:struct.pack_into('>I',fixed,patch['offset'],patch['new'])
   result['test']=dict(original_bytes=len(b),patched_sha256=hashlib.sha256(fixed).hexdigest(),changed_byte_offsets=[i for i,(a,z) in enumerate(zip(b,fixed)) if a!=z],modified_in_ram_only=True,structure=inspect(bytes(fixed)));fd=os.memfd_create('sd03-test-index',0)
   try:
    with os.fdopen(fd,'wb',closefd=False) as out:out.write(fixed)
    path='/proc/self/fd/'+str(fd);args=['ffprobe','-v','error','-show_format','-show_streams','-of','json',path];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60);result['test']['ffprobe']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'),metadata=json.loads(p.stdout) if not p.returncode else {})
    args=['ffmpeg','-v','warning','-threads','1','-i',path,'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=300);log='journaux/test-index-'+e['inode']+'.txt';add(log,p.stderr);result['test']['decode']=dict(argv=args,returncode=p.returncode,stderr_bytes=len(p.stderr),stderr_log=log)
   finally:os.close(fd)
  results.append(result)
 add('inventaires/anomalie-decembre.json',json.dumps(dict(entries=results,scope='Contre-vérification arithmétique des tables, expérience sur copie RAM uniquement ; ne date ni reset ni auteur'),ensure_ascii=False,indent=2).encode())
