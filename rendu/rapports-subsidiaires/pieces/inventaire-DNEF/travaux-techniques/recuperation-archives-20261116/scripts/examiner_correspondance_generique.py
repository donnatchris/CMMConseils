"""Contrôle manuel assisté du seul nom commun aux répertoires ZIP et L16B."""
import hashlib
import io
import json
import os
from pathlib import Path
import zipfile

B=Path('/media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive')
O=B/'qualification-zip-generique';O.mkdir(exist_ok=False)
r=json.loads((B/'comparaison-zip-L16B-finale/resultats.json').read_text())
assert len(r['matching_directories'])==1
x=r['matching_directories'][0];assert x['bytes']==28760933 and x['start']==344715116544
fd=os.open('/mnt/dislocker/dislocker-file',os.O_RDONLY)
data=os.pread(fd,x['bytes'],x['start']);os.close(fd);assert len(data)==x['bytes']
bitmap=(B/'balayage-v3/bitmap.bin').read_bytes();first=x['start']//4096;last=(x['start']+x['bytes']+4095)//4096
result={'source_start':x['start'],'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),
 'clusters':last-first,'allocated_clusters':sum((bitmap[i//8]>>(i%8))&1 for i in range(first,last)),
 'matches_recorded_archive_size':len(data)==3525227798,'member_matches':[]}
with zipfile.ZipFile(io.BytesIO(data)) as z:
 result['members']=len(z.infolist());result['crc_check_bad_member']=z.testzip();result['all_names']=z.namelist()
 for match in x['matches']:
  raw=z.read(match['member']);row={'member':match['member'],'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'L16B_files':[]}
  for p in match['known_paths']:
   content=(Path('/mnt/windows/L16B')/p).read_bytes()
   row['L16B_files'].append({'path':p,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),'identical':raw==content})
  result['member_matches'].append(row)
assert all(Path(x['member']).name=='loading.gif' for x in result['member_matches'])
result['review_conclusion']='Répertoire de composants logiciels Sage, 28,76 Mo et 2687 membres ; seules cinq occurrences du nom générique loading.gif correspondent à L16B. Aucun nom des PDF Mini. Ce conteneur n’est pas identifié comme Archive_saddedine.zip.'
with (O/'resultats.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps({k:v for k,v in result.items() if k!='all_names'},ensure_ascii=False))
