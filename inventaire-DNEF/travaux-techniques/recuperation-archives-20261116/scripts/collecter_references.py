"""Conserve les raccourcis et contrôle leur taille de cible dans l'en-tête brut."""
import datetime as dt
import hashlib
import json
from pathlib import Path
import pylnk
import shutil
import struct
P=Path('/media/shared/codeProjects/DMMConseils');O=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive/references';O.mkdir(exist_ok=False)
R=Path('/mnt/windows/Users/fintm/AppData/Roaming/Microsoft/Windows/Recent')
rows=[]
def ft(n):return (dt.datetime(1601,1,1,tzinfo=dt.timezone.utc)+dt.timedelta(microseconds=n//10)).isoformat() if n else None
for n in ['Archive_saddedine.lnk','Rejets_saddedine.lnk','Inventaire_saddedine.lnk']:
 p=R/n
 if not p.exists():rows.append({'name':n,'missing':True});continue
 b=p.read_bytes();assert b[:4]==b'\x4c\x00\x00\x00';q=O/n;shutil.copyfile(p,q);assert q.read_bytes()==b
 f=pylnk.file();f.open(str(q));target=f.local_path;f.close()
 rows.append({'source':str(p),'copy':str(q),'sha256':hashlib.sha256(b).hexdigest(),'link_bytes':len(b),'target_path':target,
              'target_size_raw_uint32_at_52':struct.unpack_from('<I',b,52)[0],
              'target_creation_utc':ft(struct.unpack_from('<Q',b,28)[0]),'target_access_utc':ft(struct.unpack_from('<Q',b,36)[0]),'target_modification_utc':ft(struct.unpack_from('<Q',b,44)[0])})
with (O/'raccourcis.json').open('x') as f:json.dump(rows,f,ensure_ascii=False,indent=2)
print(json.dumps(rows,ensure_ascii=False))
