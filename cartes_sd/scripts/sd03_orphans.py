#!/usr/bin/env python3
"""Détecte les écarts de couverture TSK/FAT et relit uniquement leurs slots."""
import json,pathlib,re
from sd03_collect import OUT,remote
raw=json.loads((OUT/'inventaires/lecture-fat.json').read_text());data=raw['geometry']['data_absolute_offset'];known={str(3+(e['absolute_entry_offset']-data)//32) for e in raw['entries'] if not e['after_end_marker'] and e['name'] not in ('.','..')};targets=[]
for line in (OUT/'inventaires/fls.txt').read_text().splitlines():
 m=re.match(r'(\S+)\s+(\*\s+)?(\d+):\s+(.*)',line)
 if m:
  typ,deleted,inode,path=m.groups()
  if not typ.lower().startswith('v') and inode not in known:targets.append(dict(inode=inode,type=typ,deleted=bool(deleted),path=path))
if targets:
 code=('TARGETS = '+repr(targets)+'\n').encode()+pathlib.Path(__file__).with_name('sd03_orphans_remote.py').read_bytes();remote('sudo -n python3 - /mnt/ewf-sd03/ewf1','inventaires/orphelins-slots.json',code)
else:
 with (OUT/'inventaires/orphelins-slots.json').open('x') as f:json.dump(dict(entries=[],blocks=[]),f)
 print('Aucun écart de couverture TSK/FAT')
