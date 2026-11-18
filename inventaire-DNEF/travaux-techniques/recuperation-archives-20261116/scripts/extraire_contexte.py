"""Fenêtres étendues autour des premières mentions physiques des fichiers cibles.

Sorties distinctes, aucune modification des extractions initiales.
"""
import hashlib
import json
import os
from pathlib import Path

B=Path('/media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive')
O=B/'contextes-etendus';O.mkdir(exist_ok=False);rows=[];seen=set()
fd=os.open('/mnt/dislocker/dislocker-file',os.O_RDONLY)
for line in (B/'balayage-v3/occurrences.jsonl').read_text().splitlines():
 x=json.loads(line)
 if x['source_scope']!='unallocated' or not any(y in x['label'] for y in ['Archive_saddedine','Rejets_saddedine','Inventaire_saddedine']):continue
 start=max(0,x['offset']-16384);start-=start%4096
 if start in seen:continue
 seen.add(start);data=os.pread(fd,65536,start);dest=O/f'{start}.bin';dest.write_bytes(data)
 magic=bytes.fromhex('4c0000000114020000000000c000000000000046');positions=[];at=0
 while (at:=data.find(magic,at))>=0:positions.append(start+at);at+=1
 rows.append({'source_offset':x['offset'],'label':x['label'],'start':start,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'file':str(dest),'shell_link_headers':positions})
os.close(fd)
with (O/'resultats.json').open('x') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print(json.dumps(rows,ensure_ascii=False))
