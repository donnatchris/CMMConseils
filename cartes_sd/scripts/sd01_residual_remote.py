#!/usr/bin/env python3
"""Export borné des seuls clusters libres non nuls du scan vérifié."""
import array
import hashlib
import io
import json
import sys
import tarfile

scan=json.loads(SCAN_VERIFIED)
g=scan['geometry'];cs=g['cluster_bytes'];items=scan['nonzero_clusters']
if len(items)*cs>64*1024**2:raise ValueError('Limite de 64 Mio')
f=open(sys.argv[1],'rb');f.seek((8192+6)*512);fat=array.array('I',f.read(15209*512))
if sys.byteorder!='little':fat.byteswap()
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|') as tar:
    for rec in items:
        c=rec['cluster']
        if fat[c]&0xfffffff:raise ValueError('Cluster devenu alloué')
        f.seek(rec['absolute_offset']);data=f.read(cs)
        if hashlib.sha256(data).hexdigest()!=rec['sha256']:raise ValueError('Hash différent du scan')
        t=tarfile.TarInfo(str(c)+'.bin');t.size=len(data);t.mode=0o600
        tar.addfile(t,io.BytesIO(data))
