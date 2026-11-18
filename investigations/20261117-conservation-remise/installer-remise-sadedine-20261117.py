from pathlib import Path
import hashlib, json, re, shutil, sys

ROOT=Path('/mnt/data/codeProjects/DMMConseils')
STAGE=Path('/tmp/sadedine-remise-20261117')
AUDIT_DEST=ROOT/'investigations/20261117-conservation-remise'

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

before=json.loads((STAGE/'audit/sources-avant.json').read_text())
for rel, digest in before.items():
    assert sha(ROOT/rel)==digest, f'Le fichier a changé pendant la préparation : {rel}'

report=(STAGE/'RAPPORT-FINAL-SADEDINE-2026.md').read_text()
old=(ROOT/'RAPPORT-FINAL-SADEDINE-2026.md').read_text()
annexe=report.split('### Annexe D')[1].split('<a id="annexe-e">')[0]
assert 'stockage S3 est complet' in annexe
assert '165,22' not in annexe
assert 'inventaire cloud incomplet' not in annexe
assert 'Aucun disque dur n’a été remis' in annexe
assert 'clé d’accès' in annexe
assert '7 octobre 2026' in annexe
assert re.findall(r'(?m)^#{1,3} .+',old)==re.findall(r'(?m)^#{1,3} .+',report), 'Structure du rapport modifiée'
assert re.findall(r'```.*?```',old,re.S)==re.findall(r'```.*?```',report,re.S), 'Blocs techniques modifiés'
assert sorted(re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])',old))==sorted(re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])',report)), 'Empreintes historiques modifiées'
generation=json.loads((STAGE/'audit/generation.json').read_text())
assert len(generation)==4
assert all(not item['layout_issues'] for item in generation)
outputs=[]
for entry in generation:
    assert sha(STAGE/entry['source'])==entry['source_sha256']
    assert sha(STAGE/entry['pdf'])==entry['pdf_sha256']
    outputs.extend([entry['source'],entry['pdf']])
outputs.append('remise-documents/empreintes-controle-remise-20261117.sha256')
if (STAGE/'pdfs/manifest.json').exists(): outputs.append('pdfs/manifest.json')
control_count=0
for line in (STAGE/outputs[-1] if outputs[-1].endswith('.sha256') else STAGE/'remise-documents/empreintes-controle-remise-20261117.sha256').read_text().splitlines():
    if not line or line.startswith('#'):continue
    digest,rel=line.split('  ',1)
    p=STAGE/rel if (STAGE/rel).exists() else ROOT/rel
    assert sha(p)==digest,rel
    control_count+=1
for rel in outputs:
    if rel not in before:
        assert not (ROOT/rel).exists(),f'Nouvelle destination déjà présente : {rel}'
assert not AUDIT_DEST.exists(),'Le dossier de traçabilité existe déjà'
print(f'Contrôles réussis : {control_count} empreintes, 4 PDF, sections et blocs techniques conservés.')
if '--apply' not in sys.argv:
    print('Préparation vérifiée. Aucun fichier du projet modifié.')
    raise SystemExit(0)

AUDIT_DEST.mkdir(parents=True)
shutil.copytree(STAGE/'audit/avant',AUDIT_DEST/'avant')
for name in ['sources-avant.json','generation.json','empreintes-reference.json']:
    shutil.copy2(STAGE/'audit'/name,AUDIT_DEST/name)
for name in ['preparer-remise-sadedine-20261117.py','generer-remise-sadedine-20261117.py','installer-remise-sadedine-20261117.py']:
    shutil.copy2(Path('/tmp')/name,AUDIT_DEST/name)
(AUDIT_DEST/'README.md').write_text('''# Actualisation de la conservation et de la remise du 17 novembre 2026

Le prestataire confirme dans la conversation du 17 novembre que le stockage S3 est complet et que la cliente possède un accès par clé pour télécharger les données. Il précise qu’aucun disque dur ne lui a encore été remis. L’annexe D est actualisée sur cette base, sans nouveau contrôle intégral du stockage distant.

Le bordereau concerne la mise à disposition sur S3 et comporte les empreintes de référence déjà consignées dans la mission. Le fichier SHA-256 associé identifie les documents remis et les principaux inventaires techniques ; il ne remplace pas un inventaire exhaustif recalculé de tous les objets S3.

La date de remise initiale est rectifiée au 7 octobre 2026, conformément aux notes de remise indiquant 16 h 15. Un rectificatif séparé est établi le 17 novembre pour être joint à l’attestation d’origine. L’original et ses signatures restent inchangés.

Les versions précédentes des deux rapports et de leurs PDF sont conservées dans `avant/`. Les copies de l’attestation dans ce dossier permettent aussi de contrôler son maintien à l’identique. Les analyses, données sources, résultats et comptes rendus historiques ne sont pas réécrits.

Les scripts de préparation, génération et installation sont joints. Les PDF ont été rendus et leurs pages modifiées inspectées : bordereau sur deux pages, rectificatif sur une page, annexes modifiées des deux rapports sans débordement. Les signatures restent à apposer.
''')
for rel in outputs:
    destination=ROOT/rel
    destination.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(STAGE/rel,destination)
    assert sha(destination)==sha(STAGE/rel)
for rel in ['remise-documents/attestation-de-remise.md','remise-documents/attestation-de-remise.pdf']:
    assert sha(ROOT/rel)==before[rel]
(AUDIT_DEST/'fichiers-apres.json').write_text(json.dumps({rel:sha(ROOT/rel) for rel in outputs},indent=2)+'\n')
print('Fichiers installés :',*outputs,sep='\n')
print('Attestation d’origine conservée à l’identique. Traçabilité :',AUDIT_DEST)
