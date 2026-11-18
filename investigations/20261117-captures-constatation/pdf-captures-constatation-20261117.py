from pathlib import Path
import hashlib,json,subprocess,sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader,PdfWriter

ROOT=Path('/mnt/data/codeProjects/DMMConseils')
STAGE=Path('/tmp/sadedine-captures-20261117')
text=(STAGE/'NOTE-DE-CONSTATION.md').read_text()
main,annex=text.split('## Captures de la vidéo du salon',1)
(STAGE/'audit/note-sans-annexe.md').write_text(main)
builder=Path('/tmp/dmm-generer-note.py').read_text()
builder=builder.replace("source = root / 'NOTE-DE-CONSTATION.md'", "source = Path('/tmp/sadedine-captures-20261117/audit/note-sans-annexe.md')")
builder=builder.replace("output = Path('/tmp/dmm-note-regenerated.pdf')", "output = Path('/tmp/sadedine-captures-20261117/audit/note-main.pdf')")
(STAGE/'audit/generer-note-principale.py').write_text(builder)
subprocess.run([sys.executable,str(STAGE/'audit/generer-note-principale.py')],check=True)

for name,file in [('Constat','DejaVuSans.ttf'),('Constat-Bold','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
data=json.loads((STAGE/'audit/extraction.json').read_text())
intro=annex.split('### Capture',1)[0].strip().replace('`','')
para_style=ParagraphStyle('explanation',fontName='Constat',fontSize=8.6,leading=11.8)
out=STAGE/'audit/annexe-captures.pdf'
c=canvas.Canvas(str(out),pagesize=A4,pageCompression=1)
c.setTitle('Captures de la vidéo du salon du 15 octobre 2024')
c.setAuthor('Christophe Donnat - Donnat Dev')
w,h=A4
for pageidx in range(3):
 c.setFillColorRGB(0,0,0)
 c.setFont('Constat-Bold',14)
 c.drawString(40,h-42,'Captures de la vidéo du salon')
 y=h-62
 if pageidx==0:
  p=Paragraph(intro,para_style)
  _,height=p.wrap(w-80,150)
  p.drawOn(c,40,y-height)
  y-=height+15
 else:
  c.setFont('Constat',8.6)
  c.drawString(40,y,'Complément photographique du 17 novembre 2026')
  y-=22
 for record in data['captures'][pageidx*2:pageidx*2+2]:
  number=data['captures'].index(record)+1
  c.setFont('Constat-Bold',9)
  c.drawString(40,y,f'Capture {number} à {record["requested_timecode"]}')
  y-=9
  imagew=470
  imageh=imagew*record['output_dimensions'][1]/record['output_dimensions'][0]
  assert y-imageh>=37,(pageidx,y,imageh)
  c.drawImage(str(STAGE/record['capture']),(w-imagew)/2,y-imageh,width=imagew,height=imageh,mask='auto')
  y-=imageh+22
 c.setFont('Constat',7)
 c.setFillColorRGB(.35,.4,.45)
 c.drawString(40,23,'SADEDINE-2026 | Note de constatation | Captures vidéo')
 c.drawRightString(w-40,23,str(pageidx+2))
 c.showPage()
c.save()
writer=PdfWriter()
for path in [STAGE/'audit/note-main.pdf',out]:
 writer.append(PdfReader(path))
writer.add_metadata({'/Title':'NOTE DE CONSTATATION - SADEDINE-2026','/Author':'Christophe Donnat - Donnat Dev','/Subject':'Note du 16 novembre et captures ajoutées le 17 novembre 2026'})
output=STAGE/'pdfs/NOTE-DE-CONSTATION.pdf'
output.parent.mkdir(exist_ok=True)
writer.write(output)
reader=PdfReader(output)
assert len(reader.pages)==4
assert sum(len(p.images) for p in reader.pages)==6
source_video=ROOT/data['source_video']
assert hashlib.sha256(source_video.read_bytes()).hexdigest()==data['source_sha256_before']
for i,record in enumerate(data['captures']):
 page=reader.pages[1+i//2]
 assert record['requested_timecode'] in page.extract_text()
hashes={}
for rel in ['NOTE-DE-CONSTATION.md','pdfs/NOTE-DE-CONSTATION.pdf']+[x['capture'] for x in data['captures']]:
 hashes[rel]=hashlib.sha256((STAGE/rel).read_bytes()).hexdigest()
(STAGE/'audit/fichiers-apres.json').write_text(json.dumps(hashes,ensure_ascii=False,indent=2)+'\n')
(STAGE/'photos-de-constatation/empreintes-captures.sha256').write_text(''.join(f'{v}  {Path(k).name}\n' for k,v in hashes.items() if k.startswith('photos-de-constatation/')))
print('Note PDF : 4 pages, 6 captures. Source vidéo conservée à l’identique.')
