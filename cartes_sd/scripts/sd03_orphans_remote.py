"""Contre-lecture des slots TSK non couverts par la récursion FAT logique.
TARGETS est transmis en mémoire. Pas de reconstruction de répertoire implicite.
"""
import array,datetime as dt,hashlib,json,struct,sys
f=open(sys.argv[1],'rb');base=8192*512;f.seek(base);b=f.read(512);bps=struct.unpack_from('<H',b,11)[0];cs=bps*b[13];reserved=struct.unpack_from('<H',b,14)[0];fatsectors=struct.unpack_from('<I',b,36)[0];data=base+(reserved+b[16]*fatsectors)*bps;total=(struct.unpack_from('<I',b,32)[0]-reserved-b[16]*fatsectors)//b[13]
f.seek(base+reserved*bps);fat=array.array('I',f.read(fatsectors*bps))
if sys.byteorder!='little':fat.byteswap()
def stamp(date,time=0,tenth=0):
 if not date:return None
 try:return (dt.datetime(1980+(date>>9),(date>>5)&15,date&31,time>>11,(time>>5)&63,(time&31)*2)+dt.timedelta(milliseconds=tenth*10)).isoformat(' ')
 except ValueError:return 'INVALID'
u16=lambda b,o:struct.unpack_from('<H',b,o)[0];u32=lambda b,o:struct.unpack_from('<I',b,o)[0]
entries=[];blocks={}
for target in TARGETS:
 absolute=data+(int(target['inode'])-3)*32;cluster=2+(absolute-data)//cs
 if not 2<=cluster<total+2:raise ValueError('Slot hors zone de données')
 if cluster not in blocks:
  f.seek(data+(cluster-2)*cs);blob=f.read(cs);blocks[cluster]=dict(cluster=cluster,absolute_offset=data+(cluster-2)*cs,size=len(blob),sha256=hashlib.sha256(blob).hexdigest(),hex=blob.hex())
 offset=(absolute-data)%cs;s=bytes.fromhex(blocks[cluster]['hex'])[offset:offset+32]
 if len(s)!=32 or s[0] in (0,255) or s[11]&15==15:raise ValueError('Slot court non validé')
 cl=(u16(s,20)<<16)|u16(s,26)
 entries.append(dict(path=target['path'],name=target['path'].rsplit('/',1)[-1],short_name=s[:11].decode('cp437',errors='replace'),absolute_entry_offset=absolute,deleted=s[0]==229,after_end_marker=False,deleted_parent=True,attributes=s[11],start_cluster=cl,first_fat_value=fat[cl]&0xfffffff if cl<len(fat) else None,size=u32(s,28),created=stamp(u16(s,16),u16(s,14),s[13]),written=stamp(u16(s,24),u16(s,22)),accessed=stamp(u16(s,18)),raw_hex=s.hex(),path_source='TSK : slot résiduel contre-vérifié, pas une arborescence FAT active démontrée'))
print(json.dumps(dict(entries=entries,blocks=list(blocks.values())),ensure_ascii=False,indent=2))
