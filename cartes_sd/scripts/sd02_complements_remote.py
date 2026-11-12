"""Exports bornés : clusters perdus, chaîne temporaire entière et istat ciblés."""
import array,hashlib,io,json,subprocess,sys,tarfile
image=sys.argv[1];g=PARAMS['geometry'];f=open(image,'rb');cs=g['cluster_bytes'];base=g['partition_offset_bytes'];off=g['data_absolute_offset'];records=[]
f.seek(base+g['reserved_sectors']*512);fat=array.array('I',f.read(g['fat_sectors']*512))
if sys.byteorder!='little':fat.byteswap()
def read(c):f.seek(off+(c-2)*cs);return f.read(cs)
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
 def add(path,b,source):
  t=tarfile.TarInfo(path);t.size=len(b);t.mode=0o600;tar.addfile(t,io.BytesIO(b));records.append(dict(artifact=path,size=len(b),sha256=hashlib.sha256(b).hexdigest(),source=source))
 for c in PARAMS['lost_clusters']:add('prive/complements/perdus/'+str(c)+'.bin',read(c),dict(cluster=c,absolute_offset=off+(c-2)*cs,fat_value=fat[c]&0xfffffff))
 c=PARAMS['temp_start'];ch=[]
 while 2<=c<g['total_clusters']+2 and c not in ch:
  ch.append(c);v=fat[c]&0xfffffff
  if v>=0xffffff8:break
  c=v
 if len(ch)*cs>16*1024**2:raise ValueError('Plafond chaîne temporaire')
 add('prive/complements/temp-chaine-complete.bin',b''.join(read(c) for c in ch),dict(clusters=ch,declared_size=PARAMS['temp_size'],description='Chaîne actuelle complète, inclut au-delà de EOF ; pas assimilée au fichier logique'))
 for inode in PARAMS['istat_inodes']:
  args=['istat','-z','UTC','-o',str(base//512),image,str(inode)];p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60)
  add('journaux/istat/'+str(inode)+'.txt',p.stdout+p.stderr,dict(argv=args,returncode=p.returncode))
 add('inventaires/complements-index.json',json.dumps(records,ensure_ascii=False,indent=2).encode(),dict(type='index'))
