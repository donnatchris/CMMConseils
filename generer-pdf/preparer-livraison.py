"""Assembler la livraison documentaire validée, sans pièces privées ni secrets."""
from pathlib import Path
import hashlib
import html
import json
import re
import zipfile
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

class Images(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            self.paths.append(dict(attrs)['src'])

def main():
    import markdown
    cfg = json.loads((ROOT / 'generer-pdf/livraison-20261118.json').read_text())
    out = ROOT / cfg['output_directory']
    manifest_path = out / 'manifest-20261118.json'
    manifest = json.loads(manifest_path.read_text())
    controls = ROOT / 'generer-pdf/controles-documentaires'
    validation_path = controls / 'validation-documentaire.json'
    validation = json.loads(validation_path.read_text())
    if not validation['passed']:
        raise RuntimeError('La validation documentaire doit réussir avant assemblage.')
    included = set()
    rows = []
    for item in manifest['rapports']:
        source, pdf = ROOT / item['source'], out / item['pdf']
        if digest(source) != item['source_sha256'] or digest(pdf) != item['pdf_sha256']:
            raise RuntimeError('Manifeste périmé : ' + item['source'])
        included.update([source, pdf])
        if item.get('original_pdf'):
            included.add(ROOT / item['original_pdf'])
        parser = Images()
        parser.feed(markdown.markdown(source.read_text(), extensions=['attr_list', 'fenced_code', 'tables']))
        for value in parser.paths:
            bits = urlsplit(value)
            if bits.scheme:
                raise RuntimeError('Image externe non incorporée : ' + value)
            target = (source.parent / unquote(bits.path)).resolve()
            if not target.is_file() or not target.is_relative_to(ROOT):
                raise RuntimeError('Image absente ou extérieure au projet : ' + value)
            included.add(target)
        title = source.read_text().splitlines()[0].lstrip('# ').strip()
        rows.append(f"| [{title}]({item['pdf']}) | {item['pages']} |")
    index = '''# Livraison documentaire SADEDINE-2026 — 18 novembre 2026

Cette livraison contient 69 PDF : rapports actuels, compléments, annexes techniques, notices et attestation d’origine préservée. La synthèse destinée à l’avocate occupe les trois premières pages du rapport final. Les PDF représentent 925 pages au total ; les deux annexes exhaustives constituent une part importante de ce volume.

Les textes Markdown et leurs illustrations sont joints dans leur arborescence. Les liens entre rapports PDF sont adaptés à cette livraison. Les références aux acquisitions, extractions, résultats bruts et pièces privées nécessitent le dossier technique conservé séparément ; celui-ci n’est pas incorporé à cette archive documentaire. Les codes d’accès, secrets, cours, mémos et correspondance ancienne sont exclus.

Les manifestes historiques restent attachés à leurs versions datées. `manifest-20261118.json` donne les empreintes des sources et PDF actuels ; `manifest-livraison-20261118.sha256` contrôle les fichiers de cet ensemble depuis la racine de l’archive. Les références et empreintes nécessaires aux contrôles sont conservées dans `generer-pdf/controles-documentaires/`. Le PDF original de l’attestation est copié sans régénération ; ses dates et signatures ne sont pas réécrites.

| Document | Pages |
|---|---:|
'''+ '\n'.join(rows) + '\n'
    index = index.replace('925 pages', str(sum(x['pages'] for x in manifest['rapports'])) + ' pages')
    index_path = out / 'INDEX.md'
    index_path.write_text(index)
    included.update([index_path, manifest_path, validation_path])
    for name in ['etat-initial.json', 'suppressions-et-deplacements.json', 'preservation-hors-corpus.json']:
        included.add(controls / name)
    for name in ['generer-rapports.py', 'verifier-livraison.py', 'preparer-livraison.py',
                 'livraison-20261118.json', 'commande.md']:
        included.add(ROOT / 'generer-pdf' / name)
    included.add(ROOT / 'freebox/consulter-freebox.py')
    forbidden = {'s3.md', 'docs/codes-d-acces.md', 'docs/memo.md', 'docs/dd.lesson.md', 'docs/reponse-mail-3.md'}
    if any(str(p.relative_to(ROOT)) in forbidden or 'prive' in p.parts for p in included):
        raise RuntimeError('Fichier exclu de la livraison.')
    checksums = out / 'manifest-livraison-20261118.sha256'
    checksums.write_text(''.join(f'{digest(p)}  {p.relative_to(ROOT)}\n' for p in sorted(included)))
    included.add(checksums)
    archive = ROOT / 'pdfs/livraison-SADEDINE-2026-20261118.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        for p in sorted(included):
            bundle.write(p, p.relative_to(ROOT))
        bundle.writestr('LISEZ-MOI.txt', 'Ouvrir pdfs/livraison-20261118/INDEX.md pour les 69 PDF.\nLes pièces techniques privées sont conservées dans le dossier séparé de la mission.\nContrôle depuis la racine : sha256sum -c pdfs/livraison-20261118/manifest-livraison-20261118.sha256\n')
    with zipfile.ZipFile(archive) as bundle:
        if bundle.testzip():
            raise RuntimeError('Erreur de lecture de l’archive.')
    archive.with_suffix('.zip.sha256').write_text(f'{digest(archive)}  {archive.name}\n')
    print(f'{archive}: {len(included)} fichiers, {archive.stat().st_size} octets')

if __name__ == '__main__':
    main()
