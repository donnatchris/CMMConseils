#!/usr/bin/env python3
"""Reçoit au plus 64 Mio de résidus vérifiés, uniquement dans le projet."""
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import tarfile
from sd01_collect import OUT, ROOT, SSH, IMAGE

scanpath=OUT/'inventaires/scan-non-alloue-v2.json';scan=json.loads(scanpath.read_text());expected={str(r['cluster'])+'.bin':r['sha256'] for r in scan['nonzero_clusters']}
limit=len(expected)*scan['geometry']['cluster_bytes']
assert limit<=64*1024**2 and shutil.disk_usage(OUT).free>limit+8*1024**3
dest=OUT/'prive/residus';dest.mkdir(exist_ok=True)
script=ROOT/'cartes_sd/scripts/sd01_residual_remote.py'
payload=b'SCAN_VERIFIED = '+repr(scanpath.read_bytes()).encode()+b'\n'+script.read_bytes()
argv=SSH+['sudo -n python3 - '+IMAGE];start=dt.datetime.now(dt.timezone.utc).isoformat();received=0;names=set()
with (OUT/'journaux/residus-export.stderr').open('xb') as err:
    p=subprocess.Popen(argv,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=err)
    p.stdin.write(payload);p.stdin.close()
    with tarfile.open(fileobj=p.stdout,mode='r|') as tar:
        for member in tar:
            if member.name not in expected or member.name in names or not member.isfile() or member.size!=16384:raise ValueError(member.name)
            content=tar.extractfile(member).read();received+=len(content)
            if received>limit or hashlib.sha256(content).hexdigest()!=expected[member.name]:raise ValueError('Borne ou empreinte')
            with (dest/member.name).open('xb') as f:f.write(content)
            names.add(member.name)
    rc=p.wait()
with (OUT/'journaux/commandes.jsonl').open('a') as f:f.write(json.dumps(dict(start_utc=start,end_utc=dt.datetime.now(dt.timezone.utc).isoformat(),argv=argv,stdin_script=str(script.relative_to(ROOT)),scan_sha256=hashlib.sha256(scanpath.read_bytes()).hexdigest(),returncode=rc,received_files=len(names),received_bytes=received))+'\n')
assert rc==0 and names==set(expected)
print('Clusters vérifiés reçus',len(names),'octets',received)
