"""Sépare les raccourcis résiduels des fichiers cibles ; aucune création factice."""
import hashlib
import json
from pathlib import Path
import pylnk
import struct
import sys
P=Path('/media/shared/codeProjects/DMMConseils');B=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive'
S=B/'balayage-v3';O=B/(sys.argv[1] if len(sys.argv)>1 else 'qualification-finale');O.mkdir(exist_ok=False)
magic=bytes.fromhex('4c0000000114020000000000c000000000000046');seen=set();result=[]
def length(data,start):
 flags=struct.unpack_from('<I',data,start+20)[0];p=start+76
 if flags&1:p+=2+struct.unpack_from('<H',data,p)[0]
 if flags&2:
  n=struct.unpack_from('<I',data,p)[0]
  if n<28:raise ValueError('LinkInfo size')
  p+=n
 for flag in [4,8,16,32,64]:
  if flags&flag:p+=2+struct.unpack_from('<H',data,p)[0]*(2 if flags&128 else 1)
 while p+4<=len(data):
  n=struct.unpack_from('<I',data,p)[0]
  if n==0:return p+4-start
  if n<8 or p+n>len(data):raise ValueError('extra data bounds')
  p+=n
 raise ValueError('LNK incomplete')
for line in (S/'occurrences.jsonl').read_text().splitlines():
 x=json.loads(line)
 if not x.get('fragment'):continue
 data=(S/x['fragment']).read_bytes();at=0;classified=[]
 while True:
  pos=data.find(magic,at)
  if pos<0:break
  at=pos+1
  try:
   n=length(data,pos);raw=data[pos:pos+n];sha=hashlib.sha256(raw).hexdigest()
   if sha in seen:continue
   seen.add(sha);dest=O/(sha+'.lnk');dest.write_bytes(raw)
   f=pylnk.file();f.open(str(dest));target=f.local_path;f.close()
   if target and any(s in target.lower() for s in ['saddedine','iphone13_mini']):
    classified.append({'kind':'recovered_shell_link_not_target_content','target':target,'target_size':struct.unpack_from('<I',raw,52)[0],
                       'bytes':n,'sha256':sha,'artifact':str(dest),'source_scope':x['source_scope'],'source_offset':x['fragment_start']+pos})
  except Exception as ex:classified.append({'kind':'possible_incomplete_link','offset':x['fragment_start']+pos,'error':str(ex)})
 if classified:result.extend(classified)
with (O/'resultats.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
