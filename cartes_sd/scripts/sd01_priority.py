#!/usr/bin/env python3
"""Contre-vérification locale des neuf extractions cibles et prévisualisations.
Les planches sont des dérivés visuels, pas des vidéos reconstituées.
"""
import hashlib
import json
import pathlib
import subprocess
from PIL import Image, ImageDraw
from sd01_collect import OUT
from sd01_mp4 import inspect

out=OUT/'prive/previsualisations'
out.mkdir(exist_ok=True)
records=[]; panels=[]
for inode in ('41329160','41329304','76861448','76861452','76861456','76861460','20903944','22835208'):
    files=list((OUT/'prive/cibles').glob(inode+'_*.mp4')) or list((OUT/'prive/extraits').glob(inode+'_*.mp4'))
    src=files[0]
    args=['ffprobe','-v','warning','-show_format','-show_streams','-of','json',str(src)]
    p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    meta=json.loads(p.stdout)
    duration=float(meta['format']['duration'])
    rec=dict(inode=inode,path=str(src.relative_to(OUT)),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),ffprobe=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(),metadata=meta),mp4=inspect(src.read_bytes()),previews=[])
    args=['ffmpeg','-v','warning','-threads','2','-i',str(src),'-f','null','-']
    p=subprocess.run(args,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
    rec['decode']=dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode())
    panel=Image.new('RGB',(1440,300),'#fff')
    ImageDraw.Draw(panel).text((8,6),src.name,fill='black')
    for col,t in enumerate((1,duration/2,max(0,duration-2))):
        dest=out/(inode+'_'+str(col)+'.png')
        args=['ffmpeg','-v','warning','-ss',str(t),'-i',str(src),'-frames:v','1','-vf','scale=480:270',str(dest)]
        if dest.exists():
            rec['previews'].append(dict(argv=args,reused_prior_preview=True,time_seconds=t,artifact=str(dest.relative_to(OUT)),exists=True))
        else:
            p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            rec['previews'].append(dict(argv=args,returncode=p.returncode,stderr=p.stderr.decode(),time_seconds=t,artifact=str(dest.relative_to(OUT)),exists=dest.exists()))
        if dest.exists():panel.paste(Image.open(dest),(480*col,30))
    panels.append(panel);records.append(rec)
sheet=Image.new('RGB',(1440,300*len(panels)),'#fff')
for row,panel in enumerate(panels):sheet.paste(panel,(0,row*300))
sheet.save(out/'planche-prioritaire-v3.jpg',quality=95)
tmp=next((OUT/'prive/cibles').glob('1543_*.mp4'));final=next((OUT/'prive/cibles').glob('76861460_*.mp4'))
prefix=tmp.read_bytes()
comparison=dict(temporary_size=len(prefix),final_size=final.stat().st_size,prefix_equal=prefix==final.read_bytes()[:len(prefix)],temporary_sha256=hashlib.sha256(prefix).hexdigest())
for inode in ('1547','1551'):
    p=next(p for p in (OUT/'prive/cibles').glob(inode+'_*') if p.suffix!='.stderr');data=p.read_bytes()
    comparison[inode]=dict(size=len(data),sha256=hashlib.sha256(data).hexdigest(),first_bytes_hex=data[:128].hex(),occurrence_in_final=final.read_bytes().find(data))
with (OUT/'inventaires/verification-prioritaire.json').open('x') as f:json.dump(dict(tools=subprocess.getoutput('ffmpeg -version').splitlines()[:1],videos=records,comparison=comparison),f,ensure_ascii=False,indent=2)
print(json.dumps(comparison,indent=2))
for r in records:print(r['inode'],r['ffprobe']['metadata']['format']['duration'],'decode',r['decode']['returncode'],'stderr',len(r['decode']['stderr']))
