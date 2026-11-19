"""Reconnaît les Shell Items fichier autour des noms ASCII résiduels.

Un Shell Item décrit un fichier : il ne constitue pas son contenu.
"""
import datetime as dt
import hashlib
import json
from pathlib import Path
import struct

B=Path('/media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive/contextes-etendus')
rows=[]
def dos(value):
 t,d=struct.unpack('<HH',value)
 try:return dt.datetime(1980+(d>>9),(d>>5)&15,d&31,t>>11,(t>>5)&63,(t&31)*2).isoformat()
 except ValueError:return None
for p in sorted(B.glob('*.bin')):
 data=p.read_bytes();base=int(p.stem)
 for name in ['Archive_saddedine.zip','Rejets_saddedine.txt','Inventaire_saddedine.csv']:
  at=0
  while (at:=data.find(name.encode()+b'\0',at))>=0:
   start=at-14;at+=1
   if start<0:continue
   size,kind=struct.unpack_from('<HB',data,start)
   if kind&0x70!=0x30 or size<14 or start+size>len(data):continue
   block=data[start:start+size];sig=block.find(b'\x04\x00\xef\xbe')
   if sig<0 or name.encode('utf-16le') not in block:continue
   rows.append({'file':str(p),'partition_offset':base+start,'structure':'file_entry_shell_item_not_file_content',
                'structure_size':size,'kind':kind,'name':name,'recorded_size':struct.unpack_from('<I',block,4)[0],
                'modified_dos_unzoned':dos(block[8:12]),'sha256':hashlib.sha256(block).hexdigest()})
with (B/'shell-items.json').open('x') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print(json.dumps(rows,ensure_ascii=False))
