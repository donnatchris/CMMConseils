from pathlib import Path
import hashlib, json, subprocess, shutil
from PIL import Image, ImageDraw, ImageFont

ROOT=Path('/mnt/data/codeProjects/DMMConseils')
STAGE=Path('/tmp/sadedine-captures-20261117')
STAGE.mkdir(exist_ok=True)
RAW=STAGE/'audit/images-sans-legende'
RAW.mkdir(parents=True,exist_ok=True)
OUT=STAGE/'photos-de-constatation'
OUT.mkdir(exist_ok=True)
VIDEO=ROOT/'cartes_sd/recherche-SD-03/20261016/prive/extraits/714049792_20241015_132449_10_0102.mp4'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
source_hash=sha(VIDEO)
points=[
 (0,'les téléphones sont en possession des agents'),
 (20,'Mme Sadedine quitte le salon'),
 (30,'Manipulation des téléphones'),
 (39,"Intervention de l’agent de PJ"),
 (44,'Apparition du logo Apple sur les téléphones'),
 (80,'Retour de Mme Sadedine dans le salon'),
]
args=['ffprobe','-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time','-of','json',str(VIDEO)]
probe=subprocess.run(args,check=True,capture_output=True,text=True)
frames=json.loads(probe.stdout)['frames']
pts=[float(x['best_effort_timestamp_time']) for x in frames]
chosen=[]
for second,label in points:
 index=next(i for i,t in enumerate(pts) if t>=second)
 chosen.append((index,pts[index],second,label))
assert len(set(x[0] for x in chosen))==6
selection='+'.join('eq(n\\,'+str(x[0])+')' for x in chosen)
argv=['ffmpeg','-hide_banner','-loglevel','error','-i',str(VIDEO),'-vf','select='+selection,'-fps_mode','vfr',str(RAW/'image-%02d.png')]
subprocess.run(argv,check=True)
font_dir=Path('/usr/share/fonts/truetype/dejavu')
title_font=ImageFont.truetype(str(font_dir/'DejaVuSans-Bold.ttf'),46)
meta_font=ImageFont.truetype(str(font_dir/'DejaVuSans.ttf'),34)
file_font=ImageFont.truetype(str(font_dir/'DejaVuSansMono.ttf'),30)
records=[]
for n,(index,actual,second,label) in enumerate(chosen,1):
 raw=RAW/f'image-{n:02}.png'
 with Image.open(raw) as im:
  original=im.convert('RGB')
  w,h=original.size
  annotated=Image.new('RGB',(w,h+200),'#111111')
  annotated.paste(original,(0,0))
  draw=ImageDraw.Draw(annotated)
  draw.rectangle((0,h,w,h+4),fill='#dddddd')
  timecode=f'{second//3600:02}:{second%3600//60:02}:{second%60:02}'
  lines=[(label,title_font,h+20),(f'Timecode vidéo : {timecode}',meta_font,h+86),(f'Fichier : {VIDEO.name}',file_font,h+140)]
  for line,font,y in lines:
   box=draw.textbbox((0,0),line,font=font)
   assert box[2]-box[0]<=w-64,line
   draw.text((32,y),line,font=font,fill='white')
  assert annotated.crop((0,0,w,h)).tobytes()==original.tobytes()
  name=f'constatation-{n:02}-{timecode.replace(":","-")}.png'
  target=OUT/name
  annotated.save(target)
  records.append({'capture':str(target.relative_to(STAGE)),'requested_timecode':timecode,'requested_seconds':second,'frame_index_zero_based':index,'actual_pts_seconds':actual,'label':label,'raw_sha256':sha(raw),'annotated_sha256':sha(target),'source_dimensions':[w,h],'output_dimensions':list(annotated.size)})
assert sha(VIDEO)==source_hash
before={}
for rel in ['NOTE-DE-CONSTATION.md','pdfs/NOTE-DE-CONSTATION.pdf']:
 p=ROOT/rel
 dest=STAGE/'audit/avant'/rel
 dest.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(p,dest)
 before[rel]=sha(p)
old=(ROOT/'NOTE-DE-CONSTATION.md').read_text()
new=old.replace('**Date de rédaction :** 16 novembre 2026','**Date de rédaction :** 16 novembre 2026  \n**Complément photographique :** 17 novembre 2026',1)
new+='''

## Captures de la vidéo du salon

Les six captures ci-après proviennent du fichier `714049792_20241015_132449_10_0102.mp4`. Les timecodes indiquent le temps écoulé depuis le début de ce fichier ; ils sont distincts de l’horloge incrustée dans les images. Les légendes et les références sont ajoutées dans un bandeau sous l’image, sans masquer ni retoucher la scène enregistrée.

'''
for n,record in enumerate(records,1):
 new+=f'### Capture {n} à {record["requested_timecode"]}\n\n'
 new+=f'![{record["label"]}]({record["capture"]})\n\n'
(STAGE/'NOTE-DE-CONSTATION.md').write_text(new)
audit={'date':'2026-11-17','source_video':str(VIDEO.relative_to(ROOT)),'source_sha256_before':source_hash,'source_sha256_after':sha(VIDEO),'method':'Première image dont le PTS est supérieur ou égal au temps demandé ; décodage FFmpeg, PNG sans perte, bandeau ajouté hors du cadre original.','ffmpeg_command':argv,'ffprobe_command':args,'captures':records,'previous_documents':before}
(STAGE/'audit/extraction.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
(STAGE/'audit/frames-probe.json').write_text(probe.stdout)
print('Source conservée :',source_hash)
for record in records:print(record['capture'],record['actual_pts_seconds'],record['label'])
