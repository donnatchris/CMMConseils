#!/usr/bin/env python3
"""Test de décodage H.264 sans conteneur ni horodatage inventé, deux zones bornées."""
import hashlib,json,pathlib,struct,subprocess,sys
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'cartes_sd/recherche-transversale/20261016');assert OUT.resolve().is_relative_to(ROOT/'cartes_sd/recherche-transversale')
def walk(b,start,end):
 while start+8<=end:
  size,t=struct.unpack_from('>I4s',b,start);assert size>=8 and start+size<=end
  yield t,start,size
  if t in [b'moov',b'trak',b'mdia',b'minf',b'stbl']:yield from walk(b,start+8,start+size)
  start+=size
results=[]
for r in json.loads((OUT/'inventaires/tables-ciblees.json').read_text()):
 holes=r['inspection']['mdat_unreferenced_ranges']
 if not holes:continue
 b=(ROOT/r['source_artifact']).read_bytes();assert hashlib.sha256(b).hexdigest()==r['sha256'];boxes=list(walk(b,0,len(b)));v=next(t for t in r['inspection']['tracks'] if t['kind']=='vide');tr=next(z for z in boxes if z[0]==b'trak' and any(t==b'hdlr' and b[p+16:p+20]==b'vide' for t,p,s in boxes if z[1]<p<z[1]+z[2]));vb={t:(p,s) for t,p,s in boxes if tr[1]<p<tr[1]+tr[2]};p,s=vb[b'stsd'];avcc=b.index(b'avcC',p,p+s);width=(b[avcc+8]&3)+1;pos=avcc+10;params=[]
 for _ in range(b[avcc+9]&31):
  n=int.from_bytes(b[pos:pos+2],'big');pos+=2;params.append(b[pos:pos+n]);pos+=n
 for _ in range(b[pos]):
  if _==0:pos+=1
  n=int.from_bytes(b[pos:pos+2],'big');pos+=2;params.append(b[pos:pos+n]);pos+=n
 p,s=vb[b'stsz'];uniform,count=struct.unpack_from('>II',b,p+12);assert uniform==0;sizes=struct.unpack_from('>'+'I'*count,b,p+20)
 p,s=vb[b'stco'];n=int.from_bytes(b[p+12:p+16],'big');offsets=struct.unpack_from('>'+'I'*n,b,p+16);rows=v['stsc_rows'];idx=0;parts=[b'\0\0\0\1'+n for n in params]
 for ci,off in enumerate(offsets,1):
  count=[row for row in rows if row[0]<=ci][-1][1]
  for size in sizes[idx:idx+count]:
   end=off+size;pos=off
   while pos<end:
    n=int.from_bytes(b[pos:pos+width],'big');pos+=width;assert n>0 and pos+n<=end;parts.append(b'\0\0\0\1'+b[pos:pos+n]);pos+=n
   off=end
  idx+=count
 indexed=b''.join(parts);h=holes[0];pos=h['offset'];end=pos+h['bytes'];extra=[];records=[]
 while pos+width<end:
  n=int.from_bytes(b[pos:pos+width],'big')
  if n<=0 or pos+width+n>end or b[pos+width]&128 or (b[pos+width]&31) not in (1,5):break
  records.append({'offset':pos,'length':n,'type':b[pos+width]&31});extra.append(b'\0\0\0\1'+b[pos+width:pos+width+n]);pos+=width+n
 tests=[]
 for label,data in [('indexed',indexed),('plus_unindexed_prefix',indexed+b''.join(extra))]:
  argv=['ffprobe','-v','error','-threads','1','-f','h264','-show_frames','-show_entries','frame=pict_type','-of','json','pipe:0'];p=subprocess.run(argv,input=data,capture_output=True,timeout=180);frames=json.loads(p.stdout).get('frames',[])
  tests.append({'label':label,'argv':argv,'returncode':p.returncode,'elementary_stream_sha256':hashlib.sha256(data).hexdigest(),'frames':len(frames),'stderr':p.stderr.decode(),'types':{t:sum(f['pict_type']==t for f in frames) for t in ['I','P','B']}})
 results.append({'card':r['card'],'inode':r['inode'],'source_sha256':r['sha256'],'extra_NALs':records,'unindexed_bytes_tested':pos-h['offset'],'remaining_unindexed_bytes':end-pos,'tests':tests,'limit':'Aucun temps original supplémentaire disponible ; test de décodage, sans vidéo réparée ni datation des images supplémentaires.'})
with (OUT/'inventaires/nal-non-indexes.json').open('x') as f:json.dump(results,f,ensure_ascii=False,indent=2)
with (OUT/'journaux/execution-nal.json').open('x') as f:json.dump({'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'image_access':False},f,indent=2)
print([(r['card'],r['inode'],[(t['label'],t['frames'],t['stderr']) for t in r['tests']]) for r in results])
