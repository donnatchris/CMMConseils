"""Rendre la note de constats et sa lettre depuis leurs Markdown courants.

Sans --publish : rendu de travail dans /tmp/dmm-documents-constat/.
Avec --publish : remplacer les deux PDF dans rendu/ et actualiser la livraison.
"""
from pathlib import Path
from urllib.parse import urlsplit, unquote, quote
import argparse
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
import sys

import markdown
from markdown.extensions.toc import slugify_unicode
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject
from weasyprint import HTML, CSS
from weasyprint.urls import URLFetcher

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'rendu'
SUB = OUT / 'rapports-subsidiaires'
WORK = Path('/tmp/dmm-documents-constat')
NOTE = ROOT / 'note-de-constat-technique.md'
LETTER = ROOT / 'lettre-d-accompagnement-du-constat-technique.md'
DATA = ROOT / 'inventaire-DNEF/travaux-techniques/complements-note-20261119/complements.json'


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'generer-pdf' / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_path():
    path = SUB / 'manifest-rendu.json'
    return path if path.exists() else OUT / 'manifest-rendu.json'


def piece_root():
    return SUB / 'pieces' if (SUB / 'pieces').exists() else OUT / 'pieces'


EXTRA_CSS = '''
@page {
  @top-left { content: "Donnat Dev | SADEDINE-2026"; }
}
@page presentation {
  @top-left { content: none; }
  @bottom-left { content: "Note de constats techniques | Version du 19 novembre 2026"; }
}
html { font-size: 9pt; }
body { line-height: 1.42; }
.coordonnees { display: table; width: 100%; font-size: 8.5pt; line-height: 1.5; }
.prestataire, .cliente { display: table-cell; width: 50%; vertical-align: top; box-sizing: border-box; }
.cliente { padding-left: 8mm; }
.page-presentation { page: presentation; break-after: page;
  string-set: short-title "Note de constats techniques"; }
.page-presentation h1 { text-align: center; border: 0; padding: 0;
  font-size: 22pt; margin: 23mm 0 9mm; }
.page-presentation h2 { font-size: 12pt; }
.date-presentation { text-align: center; margin: 0 0 12mm; }
.page-recapitulative { break-after: page; }
.page-recapitulative h2 { margin-top: 0; }
.page-recapitulative table { font-size: 8pt; line-height: 1.3; }
.page-recapitulative td, .page-recapitulative th { padding: 1.8mm 1.4mm; box-sizing: border-box; }
.page-recapitulative th:nth-child(1) { width: 4%; }
.page-recapitulative th:nth-child(2) { width: 25%; }
.page-recapitulative th:nth-child(3) { width: 71%; }
.table-modifications, .table-objets { break-inside: avoid; }
.table-objets table { font-size: 7pt; line-height: 1.3; }
.table-objets td, .table-objets th { padding: 1.2mm 1.1mm; box-sizing: border-box; }
.table-objets th:nth-child(1) { width: 32%; }
.table-objets th:nth-child(2) { width: 17%; }
.table-objets th:nth-child(3) { width: 14%; }
.table-objets th:nth-child(4) { width: 7%; }
.table-objets th:nth-child(5) { width: 15%; }
.table-objets th:nth-child(6) { width: 15%; }
.lettre { font-size: 10pt; line-height: 1.55; }
.lettre h1 { font-size: 17pt; margin: 8mm 0 6mm; }
.date-lettre { text-align: right; margin: 9mm 0 7mm; }
.signature-lettre { margin: 9mm 0 25mm; break-inside: avoid; }
img { max-height: 160mm; }
.constat-9, .identification-mini { break-inside: avoid; }
.constat-15 { break-before: page; font-size: 8.5pt; line-height: 1.35; }
.constat-15 h2 { margin-top: 0; font-size: 13pt; }
.constat-15 p { margin-bottom: 2mm; }
.constat-15 table { font-size: 7.1pt; line-height: 1.35; }
.constat-15 td, .constat-15 th { padding: 1.2mm; }
.signature-finale { break-inside: avoid; font-size: 8.5pt; }
.signature-finale hr { margin: 2mm 0; }
'''


def destinations():
    manifest = json.loads(manifest_path().read_text())
    result = {(ROOT / item['source']).resolve(): OUT / item['pdf'] for item in manifest['documents']}
    result.update({(ROOT / item['source']).resolve(): OUT / item['destination'] for item in manifest['pieces']})
    # Reports must point to the readable PDF rather than to the Markdown copy.
    result.update({(ROOT / item['source']).resolve(): OUT / item['pdf'] for item in manifest['documents']})
    result[NOTE] = OUT / 'note-de-constat-technique.pdf'
    result[LETTER] = OUT / 'lettre-d-accompagnement-du-constat-technique.pdf'
    result[DATA] = piece_root() / DATA.relative_to(ROOT)
    return result


def layout(source, css):
    body = markdown.markdown(source.read_text(),
        extensions=['tables', 'fenced_code', 'sane_lists', 'toc', 'attr_list', 'md_in_html'],
        extension_configs={'toc': {'slugify': slugify_unicode}})

    def image(match):
        value = html.unescape(match.group(1))
        if urlsplit(value).scheme:
            return match.group(0)
        path = (source.parent / unquote(value)).resolve()
        if not path.is_file():
            raise FileNotFoundError(path)
        return 'src="' + html.escape(path.as_uri(), quote=True) + '"'

    body = re.sub(r'src="([^"]+)"', image, body)
    short = 'Note de constats techniques' if source == NOTE else 'Lettre d’accompagnement'
    document = ('<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">'
                '<meta name="author" content="Christophe Donnat — Donnat Dev">'
                '<title>' + short + ' — SADEDINE-2026</title></head><body>'
                + ('' if source == NOTE else '<div class="short-title">' + short + '</div>')
                + body + '</body></html>')
    (WORK / (source.stem + '.html')).write_text(document)
    rendered = HTML(string=document, base_url=str(source.parent),
        url_fetcher=URLFetcher(allowed_protocols=['file', 'data'], fail_on_errors=True)).render(stylesheets=[CSS(string=css)])
    issues = []
    for number, page in enumerate(rendered.pages, 1):
        for box in page._page_box.descendants():
            if type(box).__name__ != 'TextBox' or not getattr(box, 'text', '').strip():
                continue
            if box.position_x < 63 or box.position_x + box.width > page.width - 63:
                issues.append({'page': number, 'type': 'horizontal', 'text': box.text[:100]})
            if box.position_y < 0 or box.position_y + box.height > page.height:
                issues.append({'page': number, 'type': 'vertical', 'text': box.text[:100]})
    return rendered, issues, body.count('<img ')


def write_pdf(source, rendered, mapping):
    path = WORK / (source.stem + '.pdf')
    raw = WORK / (source.stem + '-brut.pdf')
    rendered.write_pdf(raw)
    writer = PdfWriter(clone_from=PdfReader(raw))
    final = OUT / path.name
    for page in writer.pages:
        for ref in page.get('/Annots', []):
            action = ref.get_object().get('/A')
            if not action or action.get('/S') != '/URI':
                continue
            bits = urlsplit(str(action.get('/URI', '')))
            if bits.scheme != 'file':
                continue
            target = Path(unquote(bits.path)).resolve()
            if target not in mapping:
                if target.is_relative_to(ROOT) and target.is_file():
                    mapping[target] = piece_root() / target.relative_to(ROOT)
                else:
                    raise RuntimeError('Lien non assemblable : ' + str(target))
            value = quote(os.path.relpath(mapping[target], final.parent), safe='/')
            if bits.fragment:
                value += '#' + bits.fragment
            action[NameObject('/URI')] = TextStringObject(value)
    writer.write(path)
    return path


def render():
    WORK.mkdir(exist_ok=True)
    generator = load_module('generer_rapports_constat', 'generer-rapports.py')
    css = generator.CSS_TEXT + EXTRA_CSS
    mapping = destinations()
    for _ in range(4):
        note, issues, images = layout(NOTE, css)
        number = len(note.pages)
        text = NOTE.read_text()
        updated = re.sub(r'(\*\*Nombre de pages :\*\* )\d+', r'\g<1>' + str(number), text)
        if updated == text:
            break
        NOTE.write_text(updated)
    else:
        raise RuntimeError('Pagination instable')
    letter = re.sub(r'\*\*\d+ pages\*\*', '**' + str(number) + ' pages**', LETTER.read_text())
    LETTER.write_text(letter)
    items = []
    for source, rendered, errors, count in [(NOTE, note, issues, images)]:
        path = write_pdf(source, rendered, mapping)
        items.append({'source': str(source.relative_to(ROOT)), 'pdf': path.name,
                      'pages': len(rendered.pages), 'source_sha256': digest(source),
                      'pdf_sha256': digest(path), 'bytes': path.stat().st_size,
                      'layout_issues': errors, 'images_in_source': count,
                      'version': '2026-11-19', 'type': 'version complétée depuis le Markdown'})
    rendered, errors, images = layout(LETTER, css)
    path = write_pdf(LETTER, rendered, mapping)
    items.append({'source': str(LETTER.relative_to(ROOT)), 'pdf': path.name,
                  'pages': len(rendered.pages), 'source_sha256': digest(LETTER),
                  'pdf_sha256': digest(path), 'bytes': path.stat().st_size,
                  'layout_issues': errors, 'images_in_source': images,
                  'version': '2026-11-19', 'signature': 'Nom imprimé ; signature manuscrite à apposer par le prestataire'})
    check = PdfReader(WORK / items[0]['pdf'])
    assert 'Note de constats techniques' in check.pages[0].extract_text()
    assert 'Tableau récapitulatif des constats' in check.pages[1].extract_text()
    assert 'Cette note reprend' in check.pages[2].extract_text(), 'Le tableau doit occuper une seule page'
    assert len(PdfReader(path).pages) == 1, 'La lettre doit tenir sur une page'
    if any(x['layout_issues'] for x in items):
        raise RuntimeError(json.dumps(items, ensure_ascii=False))
    (WORK / 'generation.json').write_text(json.dumps({'documents': items,
        'renderer_sha256': digest(Path(__file__)), 'data_sha256': digest(DATA),
        'mapping': {str(k): str(v) for k, v in mapping.items()}}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(items, ensure_ascii=False, indent=2), flush=True)
    return items, mapping


def publish(items, mapping):
    reviewed = json.loads((WORK / 'controle-visuel.json').read_text())
    for item in items:
        assert reviewed['pdf_sha256'][item['pdf']] == item['pdf_sha256']
    tools = load_module('rendu_constat', 'generer-rendu.py')
    organiser = load_module('organisation_constat', 'reorganiser-rendu.py')
    manifest = json.loads(manifest_path().read_text())
    for item in items:
        shutil.copy2(WORK / item['pdf'], OUT / item['pdf'])
    previous = {x['source']: x for x in manifest['documents']}
    previous.update({x['source']: x for x in items})
    manifest['documents'] = list(previous.values())
    pieces = {x['source']: x for x in manifest['pieces']}
    for source in [NOTE, LETTER, DATA]:
        target = SUB / 'pieces' / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        pieces[str(source.relative_to(ROOT))] = {'source': str(source.relative_to(ROOT)),
            'destination': str(target.relative_to(OUT)), 'source_sha256': digest(source),
            'sha256': digest(target), 'bytes': target.stat().st_size, 'liens_absolus_relativises': False}
    manifest['pieces'] = list(pieces.values())
    manifest['organisation']['principaux_racine'] = organiser.MAIN
    manifest['organisation']['pages_conservees'] = False
    manifest['mise_a_jour_constats'] = {'date': '2026-11-19', 'constats': 15,
        'sources_modifiees': [x['source'] for x in items],
        'original_20261118_preserve': manifest['note_originale']}
    manifest_path().write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    for directory in [SUB / 'pieces', SUB / 'pieces' / DATA.relative_to(ROOT).parent,
                      SUB / 'pieces/inventaire-DNEF/travaux-techniques']:
        entries = []
        for p in sorted(directory.iterdir()):
            if p.name == 'INDEX.html':
                continue
            url = p.name + ('/INDEX.html' if p.is_dir() else '')
            entries.append('<li><a href="' + quote(url, safe='/') + '">' + html.escape(p.name) + '</a></li>')
        (directory / 'INDEX.html').write_text('<!DOCTYPE html><html lang="fr"><meta charset="utf-8"><title>Pièces justificatives</title><style>' + tools.STYLE + '</style><h1>Pièces justificatives</h1><ul>' + ''.join(entries) + '</ul></html>')
    organiser.write_indexes(manifest)
    visual_path = SUB / 'controle-visuel.json'
    visual = json.loads(visual_path.read_text())
    inspected = {x['pdf']: x for x in visual['documents']}
    for item in items:
        assert reviewed['pdf_sha256'][item['pdf']] == item['pdf_sha256']
        inspected[item['pdf']] = {'pdf': item['pdf'], 'sha256': item['pdf_sha256'],
                                  'pages_inspectees': list(range(1, item['pages'] + 1))}
    visual['documents'] = list(inspected.values())
    visual['documents_inspectes'] = len(inspected)
    visual['pages_finales_inspectees'] = sum(len(x['pages_inspectees']) for x in inspected.values())
    visual['mise_a_jour_constats_20261119'] = reviewed
    if 'note_originale' in visual:
        visual['controle_historique_note_20261118'] = visual.pop('note_originale')
    visual['reorganisation_sans_modification_visuelle'] = 'Contrôle historique ; les deux documents complétés sont contrôlés séparément.'
    visual_path.write_text(json.dumps(visual, ensure_ascii=False, indent=2) + '\n')
    result = tools.verify(check_hashes=False)
    assert result['passed']
    # The untouched large evidence files keep the checksums already validated.
    checks_path = SUB / 'SHA256SUMS.txt'
    checks = {}
    for line in checks_path.read_text().splitlines():
        value, name = line.split('  ', 1)
        if (OUT / name).is_file():
            checks[name] = value
    changed = {str((SUB / n).relative_to(OUT)) for n in ['manifest-rendu.json', 'verification-rendu.json', 'controle-visuel.json', 'LISEZ-MOI.txt', 'index.html']}
    changed.add('index.html')
    changed.update(x['pdf'] for x in items)
    changed.update(pieces[str(s.relative_to(ROOT))]['destination'] for s in [NOTE, LETTER, DATA])
    changed.update(str(p.relative_to(OUT)) for p in [SUB / 'pieces/INDEX.html', SUB / 'pieces' / DATA.relative_to(ROOT).parent / 'INDEX.html', SUB / 'pieces/inventaire-DNEF/travaux-techniques/INDEX.html'])
    for path in OUT.rglob('*'):
        if path.is_file() and path != checks_path:
            name = str(path.relative_to(OUT))
            if name not in checks or name in changed:
                checks[name] = digest(path)
    checks_path.write_text(''.join(f'{checks[k]}  {k}\n' for k in sorted(checks)))
    print('PDF remplacés et livraison actualisée : ' + str(OUT), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', action='store_true')
    args = parser.parse_args()
    cached = json.loads((WORK / 'generation.json').read_text()) if (WORK / 'generation.json').exists() else {}
    ready = (cached.get('renderer_sha256') == digest(Path(__file__))
             and cached.get('data_sha256') == digest(DATA)
             and all(digest(ROOT / x['source']) == x['source_sha256']
                     and digest(WORK / x['pdf']) == x['pdf_sha256'] for x in cached.get('documents', [])))
    if args.publish and ready:
        documents = cached['documents']
        paths = {Path(k): Path(v) for k, v in cached['mapping'].items()}
    else:
        documents, paths = render()
    if args.publish:
        publish(documents, paths)
