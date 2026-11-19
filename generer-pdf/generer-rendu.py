"""Assembler les rapports actuels et leurs dépendances dans rendu/.

Usage : PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/generer-rendu.py
L'option --audit-only ne crée aucun livrable. --verify contrôle une livraison.
"""
from pathlib import Path
from collections import Counter, deque
from concurrent.futures import ProcessPoolExecutor
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit, quote
import argparse
import hashlib
import html
import importlib.util
import json
import multiprocessing
import os
import re
import shutil
import subprocess
import sys

import markdown
from markdown.extensions.toc import slugify_unicode
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'rendu'
CONFIG = ROOT / 'generer-pdf/livraison-20261118.json'
NOTE = ROOT / 'note-de-constat-technique.md'
LETTER = ROOT / 'lettre-d-accompagnement-du-constat-technique.md'
NOTE_OLD = ROOT / 'pdfs/note-de-constat-technique.pdf'
NOTE_ARCHIVE = OUT / 'pieces/originaux/note-de-constat-technique.pdf'
EXCLUDED = {
    'docs/codes-d-acces.md', 'docs/memo.md', 'docs/dd.lesson.md',
    'docs/reponse-mail-3.md', 's3.md', '.DS_Store',
}
IGNORE_DIRS = {'avant', 'versions-rapports-avant-integration', '__pycache__',
               '.git', '.aws', '.codex', '.agents'}


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.anchors, self.images = [], set(), []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.anchors.add(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'img' and 'src' in attrs:
            self.images.append(attrs['src'])


def parse(path):
    parser = References()
    parser.feed(markdown.markdown(
        path.read_text(), extensions=['tables', 'fenced_code', 'toc', 'attr_list', 'md_in_html'],
        extension_configs={'toc': {'slugify': slugify_unicode}}))
    return parser


def allowed(path):
    rel = path.relative_to(ROOT)
    return (str(rel) not in EXCLUDED and path.name != '.DS_Store'
            and not any(x in IGNORE_DIRS for x in rel.parts))


def client_documents(cfg):
    """Exclure les notices internes et les comptes rendus intermédiaires retirés."""
    excluded = set()
    for name in ['documents-internes.json', 'documents-intermediaires-exclus.json']:
        policy = ROOT / 'generer-pdf' / name
        if policy.exists():
            excluded.update(x['source'] for x in json.loads(policy.read_text())['documents'])
    known = {x['source'] for x in cfg['documents']}
    if excluded - known:
        raise RuntimeError('Sources exclues absentes du corpus : ' + str(sorted(excluded - known)))
    return [item for item in cfg['documents'] if item['source'] not in excluded]


def inventory():
    cfg = json.loads(CONFIG.read_text())
    sources = {ROOT / x['source'] for x in cfg['documents']} | {NOTE}
    if LETTER.is_file():
        sources.add(LETTER)
    files, directories, processed = set(), set(), set()
    pending = deque(sorted(sources))
    missing, forbidden = [], []
    image_paths = set()
    while pending:
        path = pending.popleft().resolve()
        if not path.is_relative_to(ROOT):
            raise RuntimeError('Dépendance extérieure au projet : ' + str(path))
        if not allowed(path):
            forbidden.append(str(path.relative_to(ROOT)))
            continue
        if not path.exists():
            missing.append(str(path.relative_to(ROOT)))
            continue
        if path in processed:
            continue
        processed.add(path)
        if path.is_dir():
            directories.add(path)
            pending.extend(sorted(p for p in path.iterdir() if allowed(p)))
            continue
        files.add(path)
        if path.suffix.lower() != '.md':
            continue
        parser = parse(path)
        for value in parser.links:
            bits = urlsplit(value)
            if bits.scheme or bits.netloc or not bits.path:
                continue
            target = (path.parent / unquote(bits.path)).resolve()
            pending.append(target)
            if value in parser.images:
                image_paths.add(target)
    for item in cfg['documents']:
        if item.get('original_pdf'):
            files.add(ROOT / item['original_pdf'])
    tracked = subprocess.check_output(
        ['git', 'ls-files', '-z', '*.md'], cwd=ROOT).decode().split('\0')
    outside = sorted(x for x in tracked if x and (ROOT / x).is_file() and ROOT / x not in sources)
    expected_outside = EXCLUDED | {
        str(p.relative_to(ROOT)) for p in (ROOT / 'generer-pdf').rglob('*.md') if p not in sources
    }
    unexpected = [x for x in outside if x not in expected_outside]
    if missing or forbidden or unexpected:
        raise RuntimeError(json.dumps({'absents': missing, 'exclus_references': forbidden,
                                       'markdown_non_classes': unexpected}, ensure_ascii=False))
    return cfg, sources, files, directories, image_paths, outside


def copied(path):
    return OUT / 'pieces' / path.relative_to(ROOT)


def portable_markdown(source, destination):
    """Relativiser seulement les liens absolus des copies, sans toucher aux sources."""
    if source.suffix != '.md':
        return False
    original = source.read_text()

    def replace(match):
        bits = urlsplit(match.group(1))
        if bits.scheme or bits.netloc or not bits.path.startswith(str(ROOT) + '/'):
            return match.group(0)
        target = Path(unquote(bits.path)).resolve()
        value = quote(os.path.relpath(copied(target), destination.parent), safe='/')
        if bits.fragment:
            value += '#' + bits.fragment
        return '](' + value + ')'

    result = re.sub(r'\]\((/[^)]+)\)', replace, original)
    if result == original:
        return False
    destination.write_text(result)
    return True


def load_generator():
    spec = importlib.util.spec_from_file_location('generer_rapports', ROOT / 'generer-pdf/generer-rapports.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def rewrite_pdf(source_pdf, destination, source_base, destinations):
    reader = PdfReader(source_pdf)
    writer = PdfWriter(clone_from=reader)
    count = 0
    for page in writer.pages:
        for ref in page.get('/Annots', []):
            action = ref.get_object().get('/A')
            if not action or action.get('/S') != '/URI':
                continue
            bits = urlsplit(str(action.get('/URI', '')))
            if bits.scheme and bits.scheme != 'file' or bits.netloc or not bits.path:
                continue
            target = (Path(unquote(bits.path)) if bits.scheme == 'file'
                      else source_base / unquote(bits.path)).resolve()
            if target not in destinations:
                raise RuntimeError('Cible PDF non assemblée : ' + str(target))
            relative = quote(os.path.relpath(destinations[target], destination.parent), safe='/')
            if bits.fragment:
                relative += '#' + bits.fragment
            action[NameObject('/URI')] = TextStringObject(relative)
            count += 1
    writer.write(destination)
    result = PdfReader(destination)
    if len(result.pages) != len(reader.pages):
        raise RuntimeError('Pagination modifiée : ' + str(destination))
    for old, new in zip(reader.pages, result.pages):
        if old.get_contents().get_data() != new.get_contents().get_data():
            raise RuntimeError('Contenu graphique modifié : ' + str(destination))
        if old.extract_text() != new.extract_text():
            raise RuntimeError('Texte modifié : ' + str(destination))
    return len(result.pages), count


STYLE = '''body{max-width:1100px;margin:40px auto;padding:0 24px;font:16px/1.5 system-ui,sans-serif;color:#17212b}
h1,h2{color:#183b56}a{color:#1b5a78}table{border-collapse:collapse;width:100%}th,td{padding:9px 12px;border-bottom:1px solid #d2dde5;text-align:left}th{background:#e6eef3}td:last-child{white-space:nowrap}li{margin:8px 0}.intro{background:#f1f5f7;padding:20px;border-left:4px solid #24637a}'''


def write_directory_indexes(directories):
    for source in sorted(directories, reverse=True):
        target = copied(source)
        target.mkdir(parents=True, exist_ok=True)
        rows = []
        for path in sorted(target.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower())):
            if path.name == 'INDEX.html':
                continue
            href = path.name + ('/INDEX.html' if path.is_dir() else '')
            rows.append('<li><a href="' + quote(href, safe='/') + '">' + html.escape(path.name) + '</a></li>')
        (target / 'INDEX.html').write_text('<!doctype html><html lang="fr"><meta charset="utf-8"><title>Pièces jointes</title><style>' + STYLE + '</style><h1>' + html.escape(str(source.relative_to(ROOT))) + '</h1><ul>' + ''.join(rows) + '</ul></html>')


def write_index(reports, total_bytes):
    priority = {'RAPPORT-FINAL-SADEDINE-2026.pdf': 0, 'note-de-constat-technique.pdf': 1,
                'NOTE-DE-CONSTATATION-TP-01.pdf': 2, 'NOTE-DE-CONSTATION-téléphones.pdf': 3}
    rows = []
    for item in sorted(reports, key=lambda x: (priority.get(x['pdf'], 9), x['pdf'].lower())):
        source = ROOT / item['source']
        title = next((line[2:].strip() for line in source.read_text().splitlines()
                      if line.startswith('# ')), source.stem)
        rows.append('<tr><td><a href="' + quote(item['pdf']) + '">' + html.escape(title)
                    + '</a><br><small>' + html.escape(item['pdf']) + '</small></td><td>'
                    + str(item['pages']) + '</td></tr>')
    intro = (f'<p>{len(reports)} rapports et documents PDF, '
             f'{sum(x["pages"] for x in reports)} pages au total. Les photos, captures et pièces justificatives '
             'sont réunies dans <a href="pieces/INDEX.html">pieces/</a>.</p>'
             '<p>Commencer par le rapport final et la note de constats techniques. '
             'Les liens locaux des rapports visent les documents et pièces présents dans ce dossier. '
             'Conserver toute l’arborescence lors de la copie ou de la remise.</p>'
             '<p>La note courante et sa lettre sont générées depuis leurs textes Markdown. '
             'Le <a href="pieces/originaux/note-de-constat-technique.pdf">PDF original de la note du 18 novembre</a> '
             'est également joint à l’identique. L’attestation de remise est son PDF original.</p>')
    text = ('<!doctype html><html lang="fr"><meta charset="utf-8"><title>Livraison SADEDINE-2026</title><style>'
            + STYLE + '</style><h1>Livraison documentaire SADEDINE-2026</h1><p>Préparée le 19 novembre 2026</p>'
            + '<div class="intro">' + intro + '</div><h2>Documents</h2><table><thead><tr><th>Document</th><th>Pages</th></tr></thead><tbody>'
            + ''.join(rows) + '</tbody></table><p><a href="SHA256SUMS.txt">Empreintes SHA-256</a> · '
            '<a href="manifest-rendu.json">Inventaire détaillé</a></p></html>')
    (OUT / 'INDEX.html').write_text(text)
    (OUT / 'LISEZ-MOI.txt').write_text(
        'LIVRAISON DOCUMENTAIRE SADEDINE-2026 — 19 novembre 2026\n\n'
        'Ouvrir INDEX.html, puis le rapport final et la note de constats techniques.\n'
        f'{len(reports)} PDF principaux ; {sum(x["pages"] for x in reports)} pages.\n'
        'Le dossier pieces/ contient les illustrations et les justificatifs cités.\n'
        'Conserver ensemble les PDF et le dossier pieces/ pour préserver les liens.\n'
        'Selon le lecteur PDF, l’ouverture des pièces locales peut demander une confirmation.\n'
        'Les liens internet nécessitent une connexion.\n\n'
        'Les textes et données de preuve d’origine n’ont pas été réécrits.\n'
        'Les liens absolus des copies Markdown ont été rendus relatifs ; les originaux restent inchangés.\n'
        'L’original de la note est dans pieces/originaux/ ; la version principale adapte uniquement ses liens.\n'
        'Les acquisitions complètes restent distinctes de cette livraison de rapports et de pièces citées.\n\n'
        'Vérification depuis ce dossier : sha256sum -c SHA256SUMS.txt\n')


def support_file(name):
    direct = OUT / name
    return direct if direct.exists() else OUT / 'rapports-subsidiaires' / name


def verify(check_hashes=True):
    manifest = json.loads(support_file('manifest-rendu.json').read_text())
    errors, links = [], 0
    for item in manifest['documents']:
        pdf = OUT / item['pdf']
        reader = PdfReader(pdf)
        if len(reader.pages) != item['pages'] or digest(pdf) != item['pdf_sha256']:
            errors.append({'pdf_modifie': item['pdf']})
        errors.extend({'mise_en_page': item['pdf'], **issue} for issue in item.get('layout_issues', []))
    checked_pdf = 0
    non_pdf_evidence = []
    for pdf in sorted(OUT.rglob('*.pdf')):
        with pdf.open('rb') as stream:
            header = stream.read(1024)
        if b'%PDF-' not in header:
            # NTFS $I records retain the deleted document's extension, but are metadata.
            non_pdf_evidence.append(str(pdf.relative_to(OUT)))
            continue
        checked_pdf += 1
        for page in PdfReader(pdf).pages:
            for ref in page.get('/Annots', []):
                action = ref.get_object().get('/A')
                if not action or action.get('/S') != '/URI':
                    continue
                value = str(action.get('/URI', ''))
                bits = urlsplit(value)
                if bits.scheme and bits.scheme != 'file' or bits.netloc or not bits.path:
                    continue
                links += 1
                target = (pdf.parent / unquote(bits.path)).resolve()
                if not target.is_relative_to(OUT) or not target.exists():
                    errors.append({'lien_pdf': str(pdf.relative_to(OUT)), 'cible': value})
    anchors = {}
    for path in sorted(OUT.rglob('*')):
        if path.suffix.lower() not in ['.md', '.html'] or not path.is_file():
            continue
        parser = parse(path) if path.suffix == '.md' else References()
        if path.suffix == '.html':
            parser.feed(path.read_text())
        for value in parser.links:
            bits = urlsplit(value)
            if bits.scheme or bits.netloc:
                continue
            target = (path.parent / unquote(bits.path)).resolve() if bits.path else path.resolve()
            links += 1
            if not target.is_relative_to(OUT) or not target.exists():
                errors.append({'lien_piece': str(path.relative_to(OUT)), 'cible': value})
            elif bits.fragment and target.suffix == '.md':
                if target not in anchors:
                    anchors[target] = parse(target).anchors
                if unquote(bits.fragment) not in anchors[target]:
                    errors.append({'ancre_piece': str(path.relative_to(OUT)), 'cible': value})
    # Compare the evidence hashes and the exhaustive file inventory to the source.
    exhaustive = next(x for x in manifest['documents'] if 'SHA512-exhaustive' in x['source'])
    text = re.sub(r'\s+', '', '\n'.join(p.extract_text() for p in PdfReader(OUT / exhaustive['pdf']).pages))
    values = set(re.findall(r'\b[0-9a-f]{128}\b', (ROOT / exhaustive['source']).read_text()))
    absent = [x for x in values if x not in text]
    if absent:
        errors.append({'empreintes_sha512_absentes': len(absent)})
    final = PdfReader(OUT / 'RAPPORT-FINAL-SADEDINE-2026.pdf')
    section_two = next((i + 1 for i, p in enumerate(final.pages)
                        if '2. Comprendre la mission' in p.extract_text()), None)
    if section_two != 4:
        errors.append({'premiere_page_section_2': section_two})
    if check_hashes:
        for item in manifest['pieces']:
            if digest(OUT / item['destination']) != item['sha256']:
                errors.append({'piece_modifiee': item['destination']})
    main_documents = [x for x in manifest['documents'] if '/' not in x['pdf']]
    result = {'passed': not errors, 'documents_principaux': len(main_documents),
              'rapports_subsidiaires': len(manifest['documents']) - len(main_documents),
              'documents_pdf_total': len(manifest['documents']),
              'pages_principales': sum(x['pages'] for x in main_documents),
              'pages_total': sum(x['pages'] for x in manifest['documents']),
              'pdf_verifies_avec_pieces': checked_pdf, 'liens_locaux_verifies': links,
              'artefacts_non_pdf_extension_pdf': non_pdf_evidence,
              'pieces': len(manifest['pieces']), 'sha512_complets_verifies': len(values) - len(absent),
              'synthese_pages': 3 if section_two == 4 else None, 'errors': errors}
    support_file('verification-rendu.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2), flush=True)
    return result


def checksums():
    target = support_file('SHA256SUMS.txt')
    paths = sorted(p for p in OUT.rglob('*') if p.is_file() and p != target)
    target.write_text(''.join(f'{digest(p)}  {p.relative_to(OUT)}\n' for p in paths))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit-only', action='store_true')
    parser.add_argument('--verify', action='store_true')
    parser.add_argument('--note-original', type=Path, default=NOTE_OLD,
                        help='PDF original du 18 novembre à préserver lors d’un nouvel assemblage.')
    args = parser.parse_args()
    if args.verify:
        result = verify()
        if result['passed']:
            checksums()
        return 0 if result['passed'] else 1
    cfg, sources, files, directories, images, outside = inventory()
    selected_items = client_documents(cfg)
    print(json.dumps({'sources_documentaires': len(sources),
                      'pdf_remis': len(selected_items) + 1 + int(LETTER.is_file()), 'pieces_source': len(files),
                      'volume_pieces_octets': sum(p.stat().st_size for p in files),
                      'images_incorporees_uniques': len(images), 'markdown_hors_selection': outside},
                     ensure_ascii=False, indent=2), flush=True)
    if args.audit_only:
        return 0
    if OUT.exists():
        raise RuntimeError('rendu/ existe déjà : refus de remplacer la livraison.')
    original_input = args.note_original.resolve()
    if not original_input.is_file():
        raise FileNotFoundError(original_input)
    OUT.mkdir()
    pieces = []
    for i, source in enumerate(sorted(files), 1):
        destination = copied(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        before = digest(source)
        shutil.copy2(source, destination)
        if digest(destination) != before:
            raise RuntimeError('Copie non conforme : ' + str(source))
        relocated = portable_markdown(source, destination)
        pieces.append({'source': str(source.relative_to(ROOT)), 'destination': str(destination.relative_to(OUT)),
                       'source_sha256': before, 'sha256': digest(destination) if relocated else before,
                       'liens_absolus_relativises': relocated, 'bytes': destination.stat().st_size})
        if i % 100 == 0:
            print(f'Pièces copiées et vérifiées : {i}/{len(files)}', flush=True)
    NOTE_ARCHIVE.parent.mkdir(parents=True)
    original_hash = digest(original_input)
    shutil.copy2(original_input, NOTE_ARCHIVE)
    assert digest(NOTE_ARCHIVE) == original_hash
    pieces.append({'source': str(NOTE_OLD.relative_to(ROOT)), 'destination': str(NOTE_ARCHIVE.relative_to(OUT)),
                   'sha256': original_hash, 'bytes': NOTE_ARCHIVE.stat().st_size})
    # Include directory indexes for portable navigation of folder references.
    all_directories = set(directories)
    for path in files:
        all_directories.update(p for p in path.parents if p != ROOT and p.is_relative_to(ROOT))
    write_directory_indexes(all_directories)
    piece_root = OUT / 'pieces'
    rows = ['<li><a href="' + quote(p.name + ('/INDEX.html' if p.is_dir() else ''), safe='/')
            + '">' + html.escape(p.name) + '</a></li>' for p in sorted(piece_root.iterdir())]
    (piece_root / 'INDEX.html').write_text('<!doctype html><html lang="fr"><meta charset="utf-8"><title>Pièces de la livraison</title><style>' + STYLE + '</style><h1>Pièces de la livraison</h1><ul>' + ''.join(rows) + '</ul></html>')
    (NOTE_ARCHIVE.parent / 'INDEX.html').write_text('<!doctype html><html lang="fr"><meta charset="utf-8"><title>Original</title><a href="note-de-constat-technique.pdf">Note de constats techniques — PDF original</a></html>')
    destinations = {p.resolve(): copied(p) for p in files | directories}
    destinations.update({(ROOT / item['source']).resolve(): OUT / item['pdf'] for item in selected_items})
    destinations[NOTE.resolve()] = OUT / 'note-de-constat-technique.pdf'
    destinations[NOTE_OLD.resolve()] = OUT / 'note-de-constat-technique.pdf'
    generator = load_generator()
    generator.OUT = OUT
    generator.DESTINATIONS = destinations
    selected = [Path(x['source']) for x in selected_items]
    with ProcessPoolExecutor(max_workers=3, mp_context=multiprocessing.get_context('fork')) as pool:
        reports = list(pool.map(generator.generate, selected))
    note_pdf = OUT / 'note-de-constat-technique.pdf'
    if LETTER.is_file():
        # Supply the generated report map before rendering the two current texts.
        provisional = {'documents': reports, 'pieces': pieces}
        (OUT / 'manifest-rendu.json').write_text(json.dumps(provisional, ensure_ascii=False, indent=2) + '\n')
        subprocess.run([sys.executable, str(ROOT / 'generer-pdf/generer-documents-constat.py')], check=True)
        working = Path('/tmp/dmm-documents-constat')
        updated = json.loads((working / 'generation.json').read_text())['documents']
        for item in updated:
            shutil.copy2(working / item['pdf'], OUT / item['pdf'])
            reports.append(item)
            source = ROOT / item['source']
            shutil.copy2(source, copied(source))
            entry = next(x for x in pieces if x['source'] == item['source'])
            entry.update(source_sha256=digest(source), sha256=digest(source), bytes=source.stat().st_size)
    else:
        pages, changed_links = rewrite_pdf(NOTE_ARCHIVE, note_pdf, NOTE_OLD.parent, destinations)
        reports.append({'source': str(NOTE.relative_to(ROOT)), 'pdf': note_pdf.name,
                        'pages': pages, 'source_sha256': digest(NOTE), 'pdf_sha256': digest(note_pdf),
                        'bytes': note_pdf.stat().st_size, 'layout_issues': [],
                        'original_pdf_sha256': original_hash, 'liens_adaptes': changed_links,
                        'contenu_pages_identique_original': True})
    write_index(reports, sum(x['bytes'] for x in pieces))
    manifest = {'date_preparation': '2026-11-19', 'selection': str(CONFIG.relative_to(ROOT)),
                'documents': reports, 'pieces': pieces, 'exclusions': sorted(EXCLUDED),
                'note_originale': str(NOTE_ARCHIVE.relative_to(OUT)),
                'selection_remise': 'generer-pdf/documents-internes.json',
                'journaux_generation': str(generator.TMP)}
    (OUT / 'manifest-rendu.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    (OUT / 'SHA256SUMS.txt').touch()
    result = verify()
    if not result['passed']:
        raise RuntimeError('La livraison doit être corrigée avant remise.')
    # Only remove the former location after validating the preserved original and all links.
    assert digest(original_input) == digest(NOTE_ARCHIVE) == original_hash
    if original_input == NOTE_OLD.resolve():
        NOTE_OLD.unlink()
    checksums()
    print('Livraison assemblée : ' + str(OUT), flush=True)
    print('Journaux de rendu : ' + str(generator.TMP), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
