"""Reconstruction hypothétique bornée : clusters libres en ordre physique.
Aucun octet fabriqué, aucun cluster alloué incorporé. Acceptation après tables et
FFmpeg ; la chaîne FAT historique reste inconnue. Exporte aussi icat -r témoin.
"""
import array,hashlib,io,json,os,subprocess,sys,tarfile
image=sys.argv[1];g=PARAMS['geometry'];cs=g['cluster_bytes'];base=g['partition_offset_bytes'];data=g['data_absolute_offset']
f=open(image,'rb');f.seek(base+g['reserved_sectors']*512);fat=array.array('I',f.read(g['fat_sectors']*512))
if sys.byteorder!='little':fat.byteswap()
entries=sorted(PARAMS['entries'],key=lambda e:e['start_cluster']);classes={x['cluster']:x['classification'] for x in PARAMS['classes']};results=[]
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
 def add(name,b):
  t=tarfile.TarInfo(name);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b))
 for ix,e in enumerate(entries):
  first=e['start_cluster'];needed=(e['size']+cs-1)//cs;chosen=[];excluded=[];c=first
  stop=entries[ix+1]['start_cluster'] if ix+1<len(entries) else first+needed+512
  while len(chosen)<needed and c<stop:
   if not fat[c]&0xfffffff and classes.get(c)=='autre':chosen.append(c)
   else:excluded.append(c)
   c+=1
  rec=dict(inode=e['inode'],path=e['path'],declared_size=e['size'],first_cluster=first,cluster_order_hypothesis='Clusters libres non auxiliaires en ordre physique croissant, bornés par le début suivant ; hypothèse distincte de la chaîne FAT historique effacée',clusters=chosen,excluded_clusters=excluded)
  if len(chosen)<needed:rec['error']='Nombre insuffisant de clusters candidats';results.append(rec);continue
  pieces=[]
  for c in chosen:f.seek(data+(c-2)*cs);pieces.append(f.read(cs))
  b=b''.join(pieces)[:e['size']];rec['sha256']=hashlib.sha256(b).hexdigest();rec['size']=len(b);rec['structure']=inspect(b)
  inode=str(e['inode']);original=subprocess.run(['icat','-r','-o',str(base//512),image,inode],stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120)
  rec['icat_r']=dict(returncode=original.returncode,bytes=len(original.stdout),sha256=hashlib.sha256(original.stdout).hexdigest(),stderr=original.stderr.decode(errors='replace'),prefix_matches=original.stdout==b[:len(original.stdout)])
  add('prive/recuperations/icat-'+inode+'.bin',original.stdout)
  artifact='prive/recuperations/'+inode+'_'+e['path'].rsplit('/',1)[-1];add(artifact,b);rec['artifact']=artifact
  fd=os.memfd_create('sd02-reconstruction',0)
  try:
   with os.fdopen(fd,'wb',closefd=False) as out:out.write(b)
   path='/proc/self/fd/'+str(fd)
   args=['ffprobe','-v','error','-show_format','-show_streams','-of','json',path];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
   rec['ffprobe']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(errors='replace'));rec['metadata']=json.loads(p.stdout) if p.returncode==0 else {}
   args=['ffmpeg','-v','warning','-threads','1','-i',path,'-fps_mode','passthrough','-enc_time_base','demux','-f','null','-'];p=subprocess.run(args,pass_fds=(fd,),stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,timeout=600)
   log='journaux/recuperations/'+inode+'.txt';add(log,p.stderr);rec['decode']=dict(argv=args,returncode=p.returncode,stderr_bytes=len(p.stderr),log=log)
  finally:os.close(fd)
  results.append(rec);print('Reconstruction '+inode+' '+str(rec['decode']),file=sys.stderr,flush=True)
 add('inventaires/recuperations.json',json.dumps(dict(entries=results),ensure_ascii=False,indent=2).encode())
