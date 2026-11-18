"""Compare tous les répertoires ZIP validés aux noms L16B déjà extraits.

Une correspondance nominale sélectionne un candidat ; elle ne prouve pas l'identité.
Peut se lancer provisoirement ; chaque exécution utilise un nouveau dossier.
"""
import collections
import hashlib
import json
from pathlib import Path, PureWindowsPath
import sys
import os
import unicodedata

P=Path('/media/shared/codeProjects/DMMConseils');B=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116'
O=B/'prive'/sys.argv[1];O.mkdir(exist_ok=False)
source=Path('/mnt/windows/L16B')
def norm(s):return unicodedata.normalize('NFC',s).casefold()
known=collections.defaultdict(set);listing=[];errors=[]
def onerror(e):errors.append(str(e))
for root,dirs,files in os.walk(source,onerror=onerror):
 for name in files:
  path=Path(root)/name;relative=str(path.relative_to(source))
  known[norm(name)].add(relative);listing.append({'path':relative,'size':path.stat().st_size})
listing.sort(key=lambda x:x['path'])
listing_file=O/'fichiers-L16B.json'
with listing_file.open('x') as f:json.dump(listing,f,ensure_ascii=False,indent=2)
assert not errors and len(listing)==1558,(len(listing),errors)
zips=[];hits=[]
with (B/'prive/balayage-v3/zip-candidats.jsonl').open() as f:
 for line in f:
  z=json.loads(line);zips.append(z)
  matches=[]
  for member in z['all_names']:
   name=norm(PureWindowsPath(member).name)
   if name in known:matches.append({'member':member,'known_paths':sorted(known[name])})
  if matches:hits.append({'start':z['start'],'bytes':z['bytes'],'members':z['members'],'header_valid':z['header_valid'],'matches':matches})
result={'source':str(source),'listing_sha256':hashlib.sha256(listing_file.read_bytes()).hexdigest(),'known_L16B_files':len(listing),'known_distinct_names':len(known),
 'zip_directories_compared':len(zips),'largest_member_count':max((z['members'] for z in zips),default=0),'matching_directories':hits,
 'scan_complete':(B/'prive/balayage-v3/synthese.json').exists(),'caveat':'Name matches alone do not establish content identity.'}
with (O/'resultats.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
print(json.dumps(result,ensure_ascii=False))
