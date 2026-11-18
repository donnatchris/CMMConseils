"""Contre-lecture des attributs FILE_NAME des trois enregistrements du cliché."""
import hashlib
import json
from pathlib import Path
import struct

B=Path('/media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive/vss')
r=json.loads((B/'resultats.json').read_text());out=[]
for store in r['stores']:
 with (B/f"store-{store['index']}-MFT.bin").open('rb') as f:
  for index in sorted({x['mft_index'] for x in store['name_occurrences']}):
   f.seek(index*1024);original=f.read(1024);data=bytearray(original)
   assert data[:4]==b'FILE'
   usa,count=struct.unpack_from('<HH',data,4);seq=data[usa:usa+2]
   for i in range(1,count):
    assert data[i*512-2:i*512]==seq
    data[i*512-2:i*512]=data[usa+2*i:usa+2*i+2]
   names=[];attributes=[];at=struct.unpack_from('<H',data,20)[0]
   while at+16<=len(data):
    typ=struct.unpack_from('<I',data,at)[0]
    if typ==0xffffffff:break
    length=struct.unpack_from('<I',data,at+4)[0];assert length>=16 and at+length<=len(data)
    resident=not data[at+8]
    if typ==0x30 and resident:
     size,offset=struct.unpack_from('<IH',data,at+16);value=data[at+offset:at+offset+size]
     n=value[64];name=value[66:66+2*n].decode('utf-16le')
     names.append({'name':name,'namespace':value[65],'parent_mft':struct.unpack_from('<Q',value)[0]&0xffffffffffff})
    attributes.append({'type':typ,'resident':resident,'length':length});at+=length
   out.append({'mft_index':index,'record_sha256':hashlib.sha256(original).hexdigest(),'allocated':bool(struct.unpack_from('<H',data,22)[0]&1),'names':names,'attributes':attributes})
with (B/'qualification-noms.json').open('x') as f:json.dump(out,f,ensure_ascii=False,indent=2)
print(json.dumps(out,ensure_ascii=False))
