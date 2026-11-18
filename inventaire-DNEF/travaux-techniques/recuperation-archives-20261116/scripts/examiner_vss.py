"""Vue dérivée en mémoire excluant seulement les entrées du cliché VSS invalide.

Le volume source reste RO. Aucun octet de l'image n'est modifié.
"""
import hashlib
import io
import json
import os
from pathlib import Path
import pyvshadow
import pyfsntfs
import re
import struct
import uuid

P=Path('/media/shared/codeProjects/DMMConseils');O=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive/vss';O.mkdir(exist_ok=False)
FD=os.open('/mnt/dislocker/dislocker-file',os.O_RDONLY);SIZE=os.fstat(FD).st_size
patches=[];catalogs=[];off=struct.unpack_from('<Q',os.pread(FD,512,7680),48)[0];visited=set()
BAD='2d9169d8-be7b-11f1-8dc9-50e08563415f'
while off and off not in visited:
 visited.add(off);data=os.pread(FD,16384,off);(O/f'catalog-{off}.bin').write_bytes(data)
 for pos in range(128,len(data),128):
  typ=struct.unpack_from('<Q',data,pos)[0]
  if typ not in [2,3]:continue
  store=str(uuid.UUID(bytes_le=data[pos+16:pos+32]));row={'offset':off+pos,'type':typ,'store':store}
  if typ==3:row['store_header_offset']=struct.unpack_from('<Q',data,pos+32)[0]
  catalogs.append(row)
  if store==BAD:patches.append({'offset':off+pos,'original_hex':data[pos:pos+128].hex(),'replacement_hex':(b'\0'*128).hex()})
 off=struct.unpack_from('<Q',data,40)[0]
assert len(patches)==2
class Overlay(io.RawIOBase):
 def __init__(self,read_at,size):super().__init__();self.pos=0;self.read_at=read_at;self.size=size
 def readable(self):return True
 def seekable(self):return True
 def tell(self):return self.pos
 def seek(self,offset,whence=0):
  self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
  if self.pos<0:raise ValueError('negative offset')
  return self.pos
 def read(self,size=-1):
  n=max(0,self.size-self.pos) if size<0 else min(size,max(0,self.size-self.pos))
  data=self.read_at(self.pos,n);self.pos+=len(data);return data
 def readinto(self,b):
  data=self.read(len(b));b[:len(data)]=data;return len(data)
def patched_read(offset,length):
 data=bytearray(os.pread(FD,length,offset))
 for patch in patches:
  lo=max(offset,patch['offset']);hi=min(offset+len(data),patch['offset']+128)
  if lo<hi:data[lo-offset:hi-offset]=b'\0'*(hi-lo)
 return bytes(data)
result={'source':'/mnt/dislocker/dislocker-file','derived_view':True,'source_modified':False,'excluded_store':BAD,'patches':patches,'catalog_entries':catalogs,'stores':[]}
volume=pyvshadow.volume()
try:
 volume.open_file_object(Overlay(patched_read,SIZE));result['stores_after_exclusion']=volume.number_of_stores
 for i in range(volume.number_of_stores):
  store=volume.get_store(i);item={'index':i,'size':store.size,'identifier':str(store.identifier)}
  try:
   def readstore(offset,length):return store.read_buffer_at_offset(length,offset)
   filesystem=pyfsntfs.volume();filesystem.open_file_object(Overlay(readstore,store.size))
   mft=filesystem.get_file_entry(0);item['mft_size']=mft.size;h=hashlib.sha256();hits=[]
   with (O/f'store-{i}-MFT.bin').open('xb') as f:
    offset=0;tail=b''
    while offset<mft.size:
     data=mft.read_buffer_at_offset(min(8*1024**2,mft.size-offset),offset)
     if not data:raise OSError('short snapshot MFT read')
     f.write(data);h.update(data);chunk=tail+data
     for word in ['Archive_saddedine','Rejets_saddedine','Inventaire_saddedine']:
      pattern=word.encode('utf-16le');at=0
      while True:
       loc=chunk.lower().find(pattern.lower(),at)
       if loc<0:break
       absolute=offset-len(tail)+loc;hits.append({'word':word,'offset':absolute,'mft_index':absolute//1024});at=loc+1
     offset+=len(data);tail=chunk[-128:]
   item['mft_sha256']=h.hexdigest();item['name_occurrences']=hits
   targets=[]
   for hit in hits:
    e=filesystem.get_file_entry(hit['mft_index']);name=e.name
    row={'index':hit['mft_index'],'name':name,'size':e.size}
    if name and name.lower() in ['archive_saddedine.zip','rejets_saddedine.txt','inventaire_saddedine.csv']:
     dest=O/f'store-{i}-{hit["mft_index"]}-{name}';dh=hashlib.sha256();at=0
     with dest.open('xb') as out:
      while at<e.size:
       block=e.read_buffer_at_offset(min(16*1024**2,e.size-at),at)
       if not block:raise OSError('short recovery')
       out.write(block);dh.update(block);at+=len(block)
     row.update(recovered=str(dest),sha256=dh.hexdigest())
    targets.append(row)
   item['target_records']=targets;filesystem.close()
  except Exception as ex:item['error']=str(ex)
  result['stores'].append(item)
 volume.close()
except Exception as ex:result['error']=str(ex)
with (O/'resultats.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
os.close(FD)
print(json.dumps(result,ensure_ascii=False))
