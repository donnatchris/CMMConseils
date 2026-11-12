#!/usr/bin/env python3
"""Recherche complémentaire dans les blocs exportés, sans attribution implicite."""
import collections,csv,datetime as dt,hashlib,json,re,struct
from sd02_collect import OUT
raw=json.loads((OUT/'inventaires/lecture-fat-v2.json').read_text());g=raw['geometry'];scan=json.loads((OUT/'inventaires/espace-libre.json').read_text());classes=json.loads((OUT/'inventaires/residus-classes.json').read_text());plan=json.loads((OUT/'inventaires/plan-medias.json').read_text());known={e['absolute_entry_offset'] for e in plan['entries']};known.update(e['absolute_entry_offset'] for e in raw['entries']);slots=[];datehits=[];models=collections.Counter()
for p in (OUT/'prive/residus').glob('*.bin'):
 c=int(p.stem);b=p.read_bytes();base=g['data_absolute_offset']+(c-2)*g['cluster_bytes']
 if b[4:8]==b'moov' and int.from_bytes(b[:4],'big')==1006:models[hashlib.sha256(b[:1006]).hexdigest()]+=1
 for off in range(0,len(b)-31,32):
  s=b[off:off+32]
  if s[11]!=32 or s[8:11]!=b'MP4' or not re.fullmatch(rb'[\xe5_0-9][0-9A-F~_ ]{7}',s[:8]):continue
  cl=(int.from_bytes(s[20:22],'little')<<16)|int.from_bytes(s[26:28],'little');size=int.from_bytes(s[28:32],'little');date=int.from_bytes(s[16:18],'little')
  try:created=dt.date(1980+(date>>9),(date>>5)&15,date&31).isoformat()
  except ValueError:continue
  if not 2<=cl<g['total_clusters']+2 or not 0<size<256*1024**2:continue
  slots.append(dict(absolute_offset=base+off,cluster=c,known_in_inventory=base+off in known,deleted=s[0]==229,short_hex=s[:11].hex(),created_date=created,start_cluster=cl,declared_size=size,raw_hex=s.hex()))
 for needle in [b'1999',b'2000',b'202402',b'202403',b'20241015',b'1999\0', '1999'.encode('utf-16le'),'2000'.encode('utf-16le'),'202402'.encode('utf-16le'),'202403'.encode('utf-16le'),'20241015'.encode('utf-16le')]:
  pos=b.find(needle)
  if pos>=0:datehits.append(dict(cluster=c,absolute_offset=base+pos,needle_hex=needle.hex(),context_hex=b[max(0,pos-16):pos+len(needle)+32].hex()))
regions=[]
for name in ['mbr-et-avant-partition','reserve-fat32','fin-partition']:
 p=OUT/'structures'/f'{name}.bin';b=p.read_bytes();signatures=[]
 for m in re.finditer(rb'ftyp|moov|mdat|NTFS    |EXFAT   |mkdosfs|FAT32   |EFI PART',b):signatures.append(dict(offset=m.start(),signature=m.group().decode()))
 regions.append(dict(artifact=str(p.relative_to(OUT)),size=len(b),sha256=hashlib.sha256(b).hexdigest(),nonzero_bytes=sum(v!=0 for v in b),signature_candidates=signatures))
# Les chaînes allouées orphelines ne sont pas supposées contiguës.
import array,sys
fat=array.array('I',(OUT/'structures/fat1.bin').read_bytes())
if sys.byteorder!='little':fat.byteswap()
a=json.loads((OUT/'inventaires/allocation.json').read_text());lost=set(a['allocated_unreferenced_clusters']);incoming={fat[c]&0xfffffff for c in lost};chains=[]
for first in sorted(lost-incoming):
 chain=[];c=first
 while c in lost and c not in chain:chain.append(c);c=fat[c]&0xfffffff
 b=b''.join((OUT/'prive/complements/perdus'/f'{c}.bin').read_bytes() for c in chain);chains.append(dict(start_cluster=first,clusters=chain,end_value=hex(c),bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),first32hex=b[:32].hex(),signatures=[dict(offset=m.start(),signature=m.group().decode()) for m in re.finditer(rb'ftyp|moov|mdat|NTFS    |EXFAT   |mkdosfs',b)]))
result=dict(free_signature_counts=dict(collections.Counter(x['signature'] for x in scan['signature_candidates'])),classification_counts=classes['counts'],moov_template_hashes=dict(models),mp4_directory_slots=slots,new_mp4_directory_slots=[s for s in slots if not s['known_in_inventory']],date_string_candidates=datehits,outside_data_regions=regions,lost_chains=chains)
with (OUT/'inventaires/residus-synthese.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k not in ('mp4_directory_slots','date_string_candidates','lost_chains')},ensure_ascii=False,indent=2))
