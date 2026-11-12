#!/usr/bin/env python3
"""Petite collecte prioritaire, bornée à neuf entrées déjà inventoriées."""
import json
import pathlib
import re
from sd01_collect import OUT, IMAGE, remote

targets=[]
for line in (OUT/'inventaires/fls.txt').read_text().splitlines():
    if any(s in line for s in ('/20241028/','20241015_121454','20241015_224117','/.record_tmp/')):
        m=re.match(r'r/r\s+(\*\s+)?(\d+):\s+(.*)',line)
        if m:targets.append(m.groups())
assert len(targets)==9, len(targets)
for deleted,inode,path in targets:
    command='sudo -n icat '+('-r ' if deleted else '')+'-o 8192 '+IMAGE+' '+inode
    remote(command,'prive/cibles/'+inode+'_'+path.rsplit('/',1)[-1])
