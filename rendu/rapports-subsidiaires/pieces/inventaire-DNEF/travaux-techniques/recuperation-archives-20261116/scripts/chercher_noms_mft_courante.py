"""Recherche des trois noms dans toute la MFT courante, y compris entrées actives.

Conserve uniquement les enregistrements qui portent une mention cible, et leurs noms.
"""
import hashlib
import json
from pathlib import Path
import struct

B=Path('/media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive')
O=B/'mft-noms-complets';O.mkdir(exist_ok=False);source=Path('/mnt/windows/$MFT')
patterns=[s.encode('utf-16le') for s in ['Archive_saddedine','Rejets_saddedine','Inventaire_saddedine']]
h=hashlib.sha256();hits=set();offset=0;tail=b''
with source.open('rb') as f:
 while block:=f.read(8*1024**2):
  h.update(block);data=(tail+block).lower()
  for pattern in patterns:
   at=0
   while (at:=data.find(pattern.lower(),at))>=0:hits.add((offset-len(tail)+at)//1024);at+=1
  offset+=len(block);tail=block[-128:]
assert h.hexdigest()=='4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b'
rows=[]
with source.open('rb') as f:
 for index in sorted(hits):
  f.seek(index*1024);original=f.read(1024);(O/f'{index}.bin').write_bytes(original);data=bytearray(original)
  assert data[:4]==b'FILE';usa,count=struct.unpack_from('<HH',data,4);seq=data[usa:usa+2]
  for i in range(1,count):
   assert data[i*512-2:i*512]==seq;data[i*512-2:i*512]=data[usa+2*i:usa+2*i+2]
  names=[];at=struct.unpack_from('<H',data,20)[0]
  while at+16<=len(data):
   typ=struct.unpack_from('<I',data,at)[0]
   if typ==0xffffffff:break
   length=struct.unpack_from('<I',data,at+4)[0];assert length>=16 and at+length<=len(data)
   if typ==0x30 and not data[at+8]:
    n,v=struct.unpack_from('<IH',data,at+16);value=data[at+v:at+v+n]
    names.append({'name':value[66:66+2*value[64]].decode('utf-16le'),'namespace':value[65]})
   at+=length
  rows.append({'index':index,'allocated':bool(struct.unpack_from('<H',data,22)[0]&1),'names':names,'record_sha256':hashlib.sha256(original).hexdigest()})
result={'source':str(source),'bytes_scanned':offset,'sha256':h.hexdigest(),'records':rows}
with (O/'resultats.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
