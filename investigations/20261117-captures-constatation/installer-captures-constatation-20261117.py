from pathlib import Path
import hashlib,json,shutil,sys
from PIL import Image

ROOT=Path('/mnt/data/codeProjects/DMMConseils')
STAGE=Path('/tmp/sadedine-captures-20261117')
AUDIT=ROOT/'investigations/20261117-captures-constatation'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
data=json.loads((STAGE/'audit/extraction.json').read_text())
hashes=json.loads((STAGE/'audit/fichiers-apres.json').read_text())
for rel,digest in data['previous_documents'].items():
 assert sha(ROOT/rel)==digest, f'Fichier modifié depuis la préparation : {rel}'
assert sha(ROOT/data['source_video'])==data['source_sha256_before']
assert not AUDIT.exists()
for rel,digest in hashes.items():
 assert sha(STAGE/rel)==digest
 if rel not in data['previous_documents']:assert not (ROOT/rel).exists(),rel
for n,record in enumerate(data['captures'],1):
 raw=Image.open(STAGE/f'audit/images-sans-legende/image-{n:02}.png').convert('RGB')
 annotated=Image.open(STAGE/record['capture']).convert('RGB')
 assert annotated.crop((0,0,*raw.size)).tobytes()==raw.tobytes()
text=(STAGE/'NOTE-DE-CONSTATION.md').read_text()
assert sum(f'({r["capture"]})' in text for r in data['captures'])==6
assert [r['requested_seconds'] for r in data['captures']]==[0,20,30,39,44,80]
print('Contrôles réussis : 6 captures, pixels originaux préservés, 6 liens Markdown, vidéo source inchangée.')
if '--apply' not in sys.argv:
 print('Aucun fichier du projet modifié.')
 raise SystemExit(0)
AUDIT.mkdir(parents=True)
for folder in ['avant','images-sans-legende']:
 shutil.copytree(STAGE/'audit'/folder,AUDIT/folder)
for name in ['extraction.json','frames-probe.json','fichiers-apres.json','generer-note-principale.py']:
 shutil.copy2(STAGE/'audit'/name,AUDIT/name)
for name in ['captures-constatation-20261117.py','pdf-captures-constatation-20261117.py','installer-captures-constatation-20261117.py']:
 shutil.copy2(Path('/tmp')/name,AUDIT/name)
(AUDIT/'README.md').write_text('''# Captures de constatation ajoutées le 17 novembre 2026

Six captures ont été demandées aux timecodes 00:00:00, 00:00:20, 00:00:30, 00:00:39, 00:00:44 et 00:01:20 du fichier 714049792_20241015_132449_10_0102.mp4.

Le décodage FFmpeg sélectionne pour chaque temps la première image dont le PTS est supérieur ou égal au temps demandé. Les PTS réellement retenus et les numéros d’images figurent dans extraction.json. La différence maximale avec le temps demandé est de 0,062 seconde. Les captures PNG comportent un bandeau de 200 pixels ajouté sous l’image native 1920 × 1080 ; les pixels de la scène sont préservés à l’identique. Les images sans légende sont conservées ici et les six images légendées sont dans photos-de-constatation/.

Chaque bandeau contient la légende demandée, le timecode relatif au début du fichier et son nom. Les coquilles « apple » et « dasn » ont été corrigées en « Apple » et « dans ». L’horloge caméra reste visible dans la scène et est distincte du timecode relatif.

Les identités et qualités des personnes restent soumises aux précisions de la note. Le texte antérieur de la note est conservé ; un complément photographique daté du 17 novembre et les six images ont été ajoutés. Le PDF comporte quatre pages, toutes rendues et inspectées. Aucune signature n’a été ajoutée.

Les empreintes avant/après de la vidéo source concordent. La note et le PDF précédents sont conservés dans avant/. Les scripts et les empreintes sont joints pour permettre la reproduction.
''')
for rel in list(hashes)+['photos-de-constatation/empreintes-captures.sha256']:
 p=ROOT/rel
 p.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(STAGE/rel,p)
 assert sha(p)==sha(STAGE/rel)
assert sha(ROOT/data['source_video'])==data['source_sha256_before']
print('Captures installées dans',ROOT/'photos-de-constatation')
print('Note Markdown et PDF mis à jour. Traçabilité :',AUDIT)
