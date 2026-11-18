from pathlib import Path
import hashlib,json,shutil,sys
from urllib.parse import quote
from pypdf import PdfReader,PdfWriter
from pypdf.generic import NameObject,TextStringObject

ROOT=Path('/mnt/data/codeProjects/DMMConseils')
STAGE=Path('/tmp/sadedine-renommage-note-20261117')
OLD='NOTE-DE-CONSTATION.md'
NEW='NOTE-DE-CONSTATION-téléphones.md'
STAGE.mkdir(exist_ok=True)
assert (ROOT/OLD).is_file()
assert not (ROOT/NEW).exists()

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
before={}
def backup(rel):
 p=ROOT/rel
 if rel not in before:
  target=STAGE/'avant'/rel
  target.parent.mkdir(parents=True,exist_ok=True)
  shutil.copy2(p,target)
  before[rel]=sha(p)
def put(rel,content):
 p=STAGE/rel
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(content)

backup(OLD)
shutil.copy2(ROOT/OLD,STAGE/NEW)
updates=[]
sources=[
 'RAPPORT-FINAL-SADEDINE-2026.md',
 'telephones/analyse-TP-01.md',
 'telephones/analyse-TP-02.md',
 'telephones/analyse-TP-03.md',
 'cartes_sd/analyse-cartes_sd-SD-03.md',
 'inventaire-DNEF/documents-recus/verification-20241015-1325-1351/Note_reponse_TP02_TP03_15oct2024.md',
]
for rel in sources:
 p=ROOT/rel
 text=p.read_text()
 assert OLD in text,rel
 backup(rel)
 put(rel,text.replace(OLD,NEW))
 updates.append({'file':rel,'replacements':text.count(OLD)})

pdfchanges=[]
for p in sorted((ROOT/'pdfs').glob('*.pdf')):
 reader=PdfReader(p)
 refs=[]
 for n,page in enumerate(reader.pages,1):
  for ref in page.get('/Annots',[]):
   action=ref.get_object().get('/A')
   if action and OLD in str(action.get('/URI','')):refs.append(n)
 if not refs:continue
 rel=str(p.relative_to(ROOT))
 backup(rel)
 writer=PdfWriter(clone_from=reader)
 count=0
 for page in writer.pages:
  for ref in page.get('/Annots',[]):
   action=ref.get_object().get('/A')
   if not action:continue
   value=str(action.get('/URI',''))
   if OLD in value:
    action[NameObject('/URI')]=TextStringObject(value.replace(OLD,quote(NEW)))
    count+=1
 target=STAGE/rel
 target.parent.mkdir(parents=True,exist_ok=True)
 writer.write(target)
 after=PdfReader(target)
 assert len(reader.pages)==len(after.pages)
 for orig,new in zip(reader.pages,after.pages):
  assert orig.get_contents().get_data()==new.get_contents().get_data()
 pdfchanges.append({'file':rel,'links_updated':count,'pages':sorted(set(refs)),'page_content_unchanged':True})

# Keep the current delivery checksum list aligned with the updated files.
rel='remise-documents/empreintes-controle-remise-20261117.sha256'
backup(rel)
lines=[]
checksum_updates=[]
for line in (ROOT/rel).read_text().splitlines():
 if line.startswith('#') or not line:
  lines.append(line);continue
 digest,path=line.split('  ',1)
 if (STAGE/path).is_file():
  value=sha(STAGE/path)
  if value!=digest:checksum_updates.append(path)
  line=value+'  '+path
 lines.append(line)
put(rel,'\n'.join(lines)+'\n')
manifest={'date':'2026-11-17','rename':{'from':OLD,'to':NEW,'sha256':sha(ROOT/OLD)},'text_updates':updates,'pdf_updates':pdfchanges,'checksum_updates':checksum_updates,'before':before}
outputs=[NEW]+sources+[x['file'] for x in pdfchanges]+[rel]
manifest['after']={rel:sha(STAGE/rel) for rel in outputs}
put('renommage.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
assert sha(STAGE/NEW)==sha(ROOT/OLD)
print('Renommage préparé ; contenu de la note inchangé.')
print(len(sources),'fichiers texte mis à jour ;',sum(x['links_updated'] for x in pdfchanges),'liens PDF corrigés ;',len(checksum_updates),'empreintes actualisées.')

if '--apply' not in sys.argv:raise SystemExit(0)
AUDIT=ROOT/'investigations/20261117-renommage-note-telephones'
assert not AUDIT.exists()
for rel,digest in before.items():assert sha(ROOT/rel)==digest,rel
AUDIT.mkdir(parents=True)
shutil.copytree(STAGE/'avant',AUDIT/'avant')
shutil.copy2(STAGE/'renommage.json',AUDIT/'renommage.json')
shutil.copy2(Path(__file__),AUDIT/Path(__file__).name)
(AUDIT/'README.md').write_text('''# Renommage de la note de constatation des téléphones

Le 17 novembre 2026, à la demande du prestataire, le fichier racine NOTE-DE-CONSTATION.md est renommé NOTE-DE-CONSTATION-téléphones.md. Son contenu et son empreinte restent inchangés. Les liens dans les six documents courants concernés et les huit liens du PDF final sont corrigés. Les pages du PDF ne sont pas recomposées ; leurs contenus graphiques restent identiques. La liste courante des empreintes de remise est actualisée pour les fichiers modifiés.

Les archives datées, copies avant modification, scripts et relevés d’empreintes des opérations antérieures conservent les noms en vigueur au moment de leur création. Le présent dossier documente la correspondance de noms pour ces références historiques. Le PDF de la note garde son nom NOTE-DE-CONSTATION.pdf ; le renommage demandé porte sur le fichier Markdown.

Les versions précédentes des documents modifiés sont conservées dans avant/. Le fichier renommage.json contient les empreintes avant et après, les fichiers et les liens modifiés.
''')
(ROOT/OLD).rename(ROOT/NEW)
for rel in outputs:
 if rel==NEW:continue
 shutil.copy2(STAGE/rel,ROOT/rel)
for rel,digest in manifest['after'].items():assert sha(ROOT/rel)==digest,rel
assert not (ROOT/OLD).exists()
print('Renommage et mises à jour enregistrés dans le projet.')
