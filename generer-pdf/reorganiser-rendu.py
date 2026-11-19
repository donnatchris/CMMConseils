"""Garder les rapports principaux à la racine ; regrouper les autres livrables.

Les liens sont adaptés sans régénérer les pages des PDF. Les pièces sont déplacées
par renommage, en conservant leurs octets et leurs empreintes déjà vérifiées.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote, quote
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile
from textwrap import indent

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'rendu'
SUB = OUT / 'rapports-subsidiaires'
MAIN = [
    'RAPPORT-FINAL-SADEDINE-2026.pdf',
    'note-de-constat-technique.pdf',
    'lettre-d-accompagnement-du-constat-technique.pdf',
    'analyse-ordinateur.pdf',
    'analyse-TP-01.pdf', 'analyse-TP-02.pdf', 'analyse-TP-03.pdf',
    'analyse-freebox.pdf',
    'analyse-cartes_sd-SD-01.pdf', 'analyse-cartes_sd-SD-02.pdf', 'analyse-cartes_sd-SD-03.pdf',
    'analyse-cartes_sd-transversale.pdf', 'analyse-cartes_sd.pdf',
    'NOTE-DE-CONSTATATION-TP-01.pdf', 'NOTE-DE-CONSTATION-téléphones.pdf',
    'Note_reponse_TP02_TP03_15oct2024.pdf',
]


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def final_path(path):
    rel = path.relative_to(OUT)
    if len(rel.parts) == 1 and path.name in MAIN:
        return path
    if rel == Path('INDEX.html'):
        return OUT / 'index.html'
    return SUB / rel


def graphics(reader):
    """Comparer les flux de dessin et d'images sans décompresser les JPEG en pixels."""
    result = []
    for page in reader.pages:
        contents = page.get_contents()
        page_data = [hashlib.sha256(contents.get_data() if contents else b'').hexdigest()]
        resources = page.get('/Resources', {}).get_object()
        objects = resources.get('/XObject', {})
        if hasattr(objects, 'get_object'):
            objects = objects.get_object()
        for name, ref in sorted(objects.items()):
            obj = ref.get_object()
            page_data.append((name, str(obj.get('/Subtype')), str(obj.get('/Width')),
                              str(obj.get('/Height')), hashlib.sha256(obj.get_data()).hexdigest()))
        result.append(page_data)
    return result


def prepare_pdf(source, destination, locations, staging):
    reader = PdfReader(source)
    writer = None
    changes = []
    for number, page in enumerate(reader.pages):
        for position, ref in enumerate(page.get('/Annots', [])):
            action = ref.get_object().get('/A')
            if not action or action.get('/S') != '/URI':
                continue
            old_uri = str(action.get('/URI', ''))
            bits = urlsplit(old_uri)
            if bits.scheme and bits.scheme != 'file' or bits.netloc or not bits.path:
                continue
            target = ((Path(unquote(bits.path)) if bits.scheme == 'file'
                       else source.parent / unquote(bits.path))).resolve()
            if target not in locations:
                raise RuntimeError('Lien local absent de la livraison : ' + str(target))
            uri = quote(os.path.relpath(locations[target], destination.parent), safe='/')
            if bits.query:
                uri += '?' + bits.query
            if bits.fragment:
                uri += '#' + bits.fragment
            # Preserve the exact original when only URI escaping would differ.
            # The entire pieces/ tree moves together, so its relative links stay valid.
            if unquote(uri) != unquote(old_uri):
                changes.append((number, position, uri))
    if not changes:
        return None, len(reader.pages), 0
    writer = PdfWriter(clone_from=reader)
    for number, position, uri in changes:
        action = writer.pages[number]['/Annots'][position].get_object()['/A']
        action[NameObject('/URI')] = TextStringObject(uri)
    target = staging / f'{len(list(staging.glob("*.pdf"))):03d}.pdf'
    writer.write(target)
    checked = PdfReader(target)
    assert len(reader.pages) == len(checked.pages)
    assert graphics(reader) == graphics(checked), source
    assert [p.extract_text() for p in reader.pages] == [p.extract_text() for p in checked.pages], source
    return target, len(reader.pages), len(changes)


STYLE = '''body {
  max-width: 1100px;
  margin: 40px auto;
  padding: 0 24px;
  font: 16px/1.5 system-ui,sans-serif;
  color: #17212b;
}
h1, h2 {
  color: #183b56;
}
a {
  color: #1b5a78;
}
table {
  border-collapse: collapse;
  width: 100%;
}
th, td {
  padding: 10px 12px;
  border-bottom: 1px solid #d2dde5;
  text-align: left;
}
th {
  background: #e6eef3;
}
td:last-child {
  white-space: nowrap;
}
.intro {
  background: #f1f5f7;
  padding: 20px;
  border-left: 4px solid #24637a;
}'''


def format_page(title, body):
    """Indenter les blocs en gardant les liens et la ponctuation sur leur ligne."""
    block = r'</?(?:div|p|h1|h2|table|thead|tbody|tr|td|th)\b[^>]*>'
    lines = re.sub('(' + block + ')', r'\n\1\n', body).splitlines()
    formatted, level = [], 2
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if re.fullmatch(block, line) and line.startswith('</'):
            level -= 1
        formatted.append('  ' * level + line)
        if re.fullmatch(block, line) and not line.startswith('</'):
            level += 1
    return ('<!DOCTYPE html>\n<html lang="fr">\n  <head>\n'
            '    <meta charset="utf-8">\n    <title>' + html.escape(title) + '</title>\n'
            '    <style>\n' + indent(STYLE, '      ') + '\n    </style>\n'
            '  </head>\n  <body>\n' + '\n'.join(formatted)
            + '\n  </body>\n</html>\n')


def write_indexes(manifest):
    def table(items, base):
        rows = []
        for item in items:
            lines = (ROOT / item['source']).read_text().splitlines()
            title = next((x[2:].strip() for x in lines if x.startswith('# ')), Path(item['pdf']).stem)
            if Path(item['pdf']).name == 'NOTE-DE-CONSTATION-téléphones.pdf':
                title = 'Note de constatation — téléphones et captures du salon'
            uri = quote(os.path.relpath(OUT / item['pdf'], base), safe='/')
            rows.append('<tr><td><a href="' + uri + '">' + html.escape(title)
                        + '</a></td><td>' + str(item['pages']) + '</td></tr>')
        return '<table><thead><tr><th>Document</th><th>Pages</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table>'

    def page(title, body):
        return format_page(title, '<h1>' + html.escape(title) + '</h1>' + body)

    by_name = {Path(x['pdf']).name: x for x in manifest['documents']}
    main = [by_name[x] for x in MAIN]
    other = sorted((x for x in manifest['documents'] if Path(x['pdf']).name not in MAIN), key=lambda x: x['pdf'].lower())
    body = ('<div class="intro"><p>Rapports principaux, analyses par équipement et notes de constat.</p>'
            f'<p>Les <a href="rapports-subsidiaires/index.html">{len(other)} rapports complémentaires, annexes et documents de remise</a> '
            'sont regroupés dans <strong>rapports-subsidiaires/</strong>, avec '
            'les <a href="rapports-subsidiaires/pieces/INDEX.html">photos et pièces justificatives</a>.</p>'
            '<p>Conserver toute l’arborescence pour préserver les liens.</p></div>'
            '<h2>Rapports principaux et notes</h2>' + table(main, OUT)
            + '<p><a href="rapports-subsidiaires/index.html">Consulter les rapports subsidiaires et les pièces</a></p>')
    (OUT / 'index.html').write_text(page('Livraison documentaire SADEDINE-2026', body))
    body = ('<p><a href="../index.html">Retour aux rapports principaux</a></p>'
            '<div class="intro"><p>Compléments d’investigation, annexes de preuve et documents de remise.</p>'
            '<p><a href="pieces/INDEX.html">Photos et pièces justificatives</a> · '
            '<a href="pieces/originaux/note-de-constat-technique.pdf">PDF original de la note de constat</a></p></div>'
            '<h2>Rapports et documents complémentaires</h2>' + table(other, SUB)
            + '<p><a href="LISEZ-MOI.txt">Notice de lecture</a> · <a href="SHA256SUMS.txt">Empreintes SHA-256</a> · '
            '<a href="manifest-rendu.json">Inventaire détaillé</a> · <a href="verification-rendu.json">Contrôles</a></p>')
    (SUB / 'index.html').write_text(page('Rapports subsidiaires et pièces justificatives', body))
    (SUB / 'LISEZ-MOI.txt').write_text(
        'LIVRAISON DOCUMENTAIRE SADEDINE-2026\n\n'
        f'Ouvrir ../index.html pour les {len(main)} rapports principaux, notes et courriers.\n'
        f'Ouvrir index.html dans ce sous-dossier pour les {len(other)} autres PDF et les pièces.\n'
        f'La livraison compte {len(manifest["documents"])} documents PDF, soit {sum(x["pages"] for x in manifest["documents"])} pages, et leurs justificatifs.\n'
        'Les photos et pièces sont dans pieces/. Conserver toute l’arborescence.\n'
        'Les liens internet nécessitent une connexion.\n\n'
        'Les liens locaux des PDF sont adaptés à cette arborescence.\n'
        'La note principale porte sa date de version ; sa lettre d’accompagnement doit être signée par le prestataire.\n'
        'Le PDF original de la note du 18 novembre est préservé à l’identique dans pieces/originaux/.\n'
        'Les acquisitions complètes restent distinctes de la livraison des rapports et pièces citées.\n\n'
        'Contrôle depuis la racine rendu/ : sha256sum -c rapports-subsidiaires/SHA256SUMS.txt\n')


def main():
    if SUB.exists():
        raise RuntimeError('rapports-subsidiaires/ existe déjà ; refus de réorganiser deux fois.')
    manifest = json.loads((OUT / 'manifest-rendu.json').read_text())
    assert len(manifest['documents']) >= len(MAIN)
    assert set(MAIN) <= {x['pdf'] for x in manifest['documents']}
    old_paths = sorted(OUT.rglob('*'))
    locations = {p.resolve(): final_path(p) for p in old_paths}
    old_stats = {p: (p.stat().st_dev, p.stat().st_ino, p.stat().st_size, p.stat().st_mtime_ns)
                 for p in old_paths if p.is_file()}
    cached_hashes = {}
    for line in (OUT / 'SHA256SUMS.txt').read_text().splitlines():
        value, name = line.split('  ', 1)
        cached_hashes[locations[(OUT / name).resolve()]] = value
    staging = Path(tempfile.mkdtemp(prefix='dmm-rendu-reorganisation-'))
    (staging / 'manifest-avant.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    shutil.copy2(OUT / 'INDEX.html', staging / 'index-avant.html')
    edits, total_links = {}, 0
    for source in old_paths:
        if source.suffix.lower() != '.pdf' or not source.is_file():
            continue
        with source.open('rb') as stream:
            if b'%PDF-' not in stream.read(1024):
                continue
        staged, pages, links = prepare_pdf(source, locations[source.resolve()], locations, staging)
        if staged:
            backup = staging / 'avant' / source.relative_to(OUT)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, backup)
            edits[source] = staged
            total_links += links
        print(f'Liens préparés : {source.relative_to(OUT)} ({links})', flush=True)
    # All replacement PDFs have been checked before the first move.
    SUB.mkdir()
    for path in sorted(OUT.iterdir()):
        if path == SUB or path.name in MAIN:
            continue
        path.rename(final_path(path))
    for old, staged in edits.items():
        destination = locations[old.resolve()]
        temporary = destination.with_suffix('.reorganisation.tmp')
        shutil.copyfile(staged, temporary)
        os.replace(temporary, destination)
        cached_hashes[destination] = digest(destination)
    for old, stat in old_stats.items():
        if old in edits:
            continue
        current = locations[old.resolve()].stat()
        assert stat == (current.st_dev, current.st_ino, current.st_size, current.st_mtime_ns), old
    for item in manifest['documents']:
        destination = locations[(OUT / item['pdf']).resolve()]
        item['pdf'] = str(destination.relative_to(OUT))
        item['pdf_sha256'] = digest(destination)
        item['bytes'] = destination.stat().st_size
    for item in manifest['pieces']:
        item['destination'] = str(locations[(OUT / item['destination']).resolve()].relative_to(OUT))
    manifest['note_originale'] = str(locations[(OUT / manifest['note_originale']).resolve()].relative_to(OUT))
    manifest['controle_visuel'] = 'rapports-subsidiaires/controle-visuel.json'
    manifest['organisation'] = {'principaux_racine': MAIN,
                                'rapports_subsidiaires': len(manifest['documents']) - len(MAIN),
                                'index': 'index.html', 'index_subsidiaires': 'rapports-subsidiaires/index.html',
                                'liens_adaptes': total_links, 'pages_conservees': True}
    visual_path = SUB / 'controle-visuel.json'
    visual = json.loads(visual_path.read_text())
    visual['reorganisation_sans_modification_visuelle'] = True
    by_name = {Path(x['pdf']).name: x for x in manifest['documents']}
    for item in visual['documents']:
        current = by_name[Path(item['pdf']).name]
        item['pdf'], item['sha256'] = current['pdf'], current['pdf_sha256']
    visual_path.write_text(json.dumps(visual, ensure_ascii=False, indent=2) + '\n')
    write_indexes(manifest)
    (SUB / 'manifest-rendu.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    # Reuse the link, anchor, pagination and data-preservation checks from the assembler.
    spec = importlib.util.spec_from_file_location('rendu_tools', ROOT / 'generer-pdf/generer-rendu.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    result = module.verify(check_hashes=False)
    if not result['passed']:
        raise RuntimeError('Contrôle de la réorganisation en échec.')
    # Large pieces have only been renamed; their file identities above prove no rewrite.
    target = SUB / 'SHA256SUMS.txt'
    hashes = {}
    for path in sorted(p for p in OUT.rglob('*') if p.is_file() and p != target):
        hashes[path] = cached_hashes[path] if path in cached_hashes and path not in {
            SUB / 'manifest-rendu.json', visual_path, SUB / 'verification-rendu.json', SUB / 'LISEZ-MOI.txt',
            OUT / 'index.html', SUB / 'index.html',
        } else digest(path)
    for item in manifest['documents']:
        assert hashes[OUT / item['pdf']] == item['pdf_sha256']
    for item in manifest['pieces']:
        assert hashes[OUT / item['destination']] == item['sha256']
    target.write_text(''.join(f'{value}  {path.relative_to(OUT)}\n' for path, value in sorted(hashes.items())))
    assert set(p.name for p in OUT.iterdir()) == set(MAIN) | {'index.html', 'rapports-subsidiaires'}
    print(f'Réorganisation terminée : {len(MAIN)} PDF principaux, {len(manifest["documents"]) - len(MAIN)} subsidiaires, {total_links} liens adaptés.', flush=True)
    print('Sauvegarde des PDF avant adaptation : ' + str(staging), flush=True)


if __name__ == '__main__':
    main()
