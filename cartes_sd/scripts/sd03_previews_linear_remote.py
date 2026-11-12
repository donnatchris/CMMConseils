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
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
 def add(name,b):
  t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
 for e in PARAMS['entries']:
  b=read(e);fd=os.memfd_create('sd03-apercu',0)
  try:
   with os.fdopen(fd,'wb',closefd=False) as out:out.write(b)
   for second in e['preview_seconds']:
    path='/proc/self/fd/'+str(fd);args=['ffmpeg','-v','warning','-i',path,'-ss',str(second),'-frames:v','1','-vf','scale=960:-2','-f','image2pipe','-vcodec','png','pipe:1'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=90);artifact='prive/apercus-lineaires/'+str(e['inode'])+'-'+str(second)+'.png'
    if p.stdout:add(artifact,p.stdout)
    records.append(dict(inode=e['inode'],source_path=e['path'],source_sha256=hashlib.sha256(b).hexdigest(),requested_second=second,artifact=artifact if p.stdout else None,argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'),sha256=hashlib.sha256(p.stdout).hexdigest() if p.stdout else None))
  finally:os.close(fd)
 add('inventaires/apercus-lineaires-index.json',json.dumps(records,ensure_ascii=False,indent=2).encode())
