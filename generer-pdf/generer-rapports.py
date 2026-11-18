from pathlib import Path
import concurrent.futures
import hashlib
import html
import json
import logging
import multiprocessing
import os
import re
import tempfile
import argparse
import shutil
import fcntl
from urllib.parse import unquote, urlsplit

import markdown
from weasyprint import HTML, CSS
from weasyprint.urls import URLFetcher
from pypdf import PdfReader, PdfWriter
from pypdf.generic import TextStringObject, NameObject
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parents[1]
SELECTION = json.loads((ROOT / 'generer-pdf/livraison-20261118.json').read_text())
OUT = ROOT / SELECTION['output_directory']
TMP = Path(tempfile.mkdtemp(prefix='dmm-pdf-qa-'))
SOURCES = [Path(item['source']) for item in SELECTION['documents']]
ITEMS = {item['source']: item for item in SELECTION['documents']}
DESTINATIONS = {(ROOT / item['source']).resolve(): OUT / item['pdf']
                for item in SELECTION['documents']}
assert len(set(DESTINATIONS.values())) == len(SOURCES), 'Duplicate output names'

CSS_TEXT = '''
@page {
  size: A4;
  margin: 19mm 17mm 18mm;
  @top-left {
    content: "DMMConseils | SADEDINE-2026";
    font-family: "DejaVu Sans"; font-size: 7pt; color: #64748b;
    vertical-align: bottom; padding-bottom: 4mm;
  }
  @bottom-left {
    content: string(short-title);
    font-family: "DejaVu Sans"; font-size: 6.5pt; color: #64748b;
  }
  @bottom-right {
    content: counter(page) " / " counter(pages);
    font-family: "DejaVu Sans"; font-size: 7pt; color: #64748b;
  }
}
html { font-family: "DejaVu Sans"; font-size: 9.3pt; color: #17212b; }
body { margin: 0; line-height: 1.47; }
.short-title { string-set: short-title content(); height: 0; font-size: 0; }
h1 { font-size: 22pt; line-height: 1.2; color: #183b56;
     margin: 0 0 7mm; padding-bottom: 5mm; border-bottom: 1.5pt solid #24637a;
     bookmark-level: 1; }
h2 { font-size: 14pt; line-height: 1.25; color: #183b56;
     margin: 7mm 0 3mm; padding-bottom: 1.5mm; border-bottom: .5pt solid #d2dde5; }
h3 { font-size: 11pt; line-height: 1.3; color: #214d65; margin: 5mm 0 2mm; }
h4, h5, h6 { font-size: 9.5pt; margin: 4mm 0 1.5mm; }
h1, h2, h3, h4, h5, h6 { break-after: avoid; overflow-wrap: anywhere; }
p { margin: 0 0 2.8mm; orphans: 3; widows: 3; overflow-wrap: anywhere; }
a { color: #1b5a78; text-decoration: none; overflow-wrap: anywhere; }
strong { font-weight: 700; }
ul, ol { padding-left: 5.5mm; margin: 1mm 0 3mm; }
li { margin-bottom: 1.2mm; overflow-wrap: anywhere; }
li > p { margin-bottom: 1.5mm; }
blockquote { margin: 3mm 0; padding: 3mm 4mm; background: #f1f5f7;
             border-left: 2pt solid #7f9cab; }
blockquote > p:last-child { margin-bottom: 0; }
code { font-family: "DejaVu Sans Mono"; font-size: .85em; overflow-wrap: anywhere; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; font-size: 7.4pt;
      line-height: 1.4; padding: 3mm; background: #f3f5f7; margin: 3mm 0; }
pre code { font-size: 1em; }
table { border-collapse: collapse; width: 100%; table-layout: fixed;
        font-size: 7.7pt; line-height: 1.4; margin: 3mm 0 4mm; }
thead { display: table-header-group; }
th, td { border: .5pt solid #ccd7df; padding: 2mm; vertical-align: top;
         overflow-wrap: anywhere; }
th { background: #e6eef3; text-align: left; color: #183b56; font-weight: 700; }
tbody tr:nth-child(even) { background: #f7f9fb; }
tr { break-inside: avoid; }
.summary-point { break-inside: avoid; }
.proof-record { break-inside: avoid; }
.signature { break-inside: avoid; break-before: avoid; }
.keep-end { break-inside: avoid; }
td p { margin-bottom: 1mm; }
img { max-width: 100%; max-height: 220mm; object-fit: contain; display: block;
      margin: 3mm auto; break-inside: avoid; }
hr { border: 0; border-top: .5pt solid #ccd7df; margin: 5mm 0; }
'''

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def expand_long_table_fields(body):
    """Keep full recipient fields readable without a multi-page narrow table cell."""
    expanded = []
    def row(match):
        cells = re.findall(r'<td\b[^>]*>(.*?)</td>', match.group(0), flags=re.S)
        if not cells:
            return match.group(0)
        reference = ' / '.join(re.sub('<[^>]*>', '', c) for c in cells[:2])
        def cell(field):
            content = field.group(1)
            if len(html.unescape(re.sub('<[^>]*>', '', content))) <= 600:
                return field.group(0)
            anchor = 'champ-long-' + str(len(expanded) + 1)
            expanded.append('<h3 id="' + anchor + '">Champ ' + str(len(expanded) + 1)
                            + ' — ' + reference + '</h3><p>' + content + '</p>')
            return '<td><a href="#' + anchor + '">Destinataires complets : annexe, champ ' + str(len(expanded)) + '</a></td>'
        return re.sub(r'<td\b[^>]*>(.*?)</td>', cell, match.group(0), flags=re.S)
    body = re.sub(r'<tr\b[^>]*>.*?</tr>', row, body, flags=re.S)
    if expanded:
        appendix = '<h2>Annexe de lecture — champs longs des tableaux</h2>'
        appendix += '<p>Les listes suivantes reprennent intégralement les destinataires du champ indiqué, sans troncature. Le renvoi depuis la ligne du tableau conserve leur rattachement au message.</p>'
        # Keep the author's final signature at the end of the document.
        before, separator, signature = body.rpartition('<hr />')
        body = before + appendix + ''.join(expanded) + separator + signature
    return body

def keep_final_signature(body):
    before, separator, signature = body.rpartition('<hr />')
    if not separator or 'Révision documentaire :' not in signature:
        return body
    signature = '<div class="signature">' + separator + signature + '</div>'
    # Keep a short final paragraph, image, glossary or code block with the signature.
    blocks = list(re.finditer(r'<(p|table|pre|ul|ol)\b[^>]*>.*?</\1>', before, flags=re.S))
    if blocks:
        last = blocks[-1]
        if not before[last.end():].strip() and len(last.group(0)) < 8000:
            return before[:last.start()] + '<section class="keep-end">' + last.group(0) + signature + '</section>'
    return before + signature

def generate(rel):
    source = ROOT / rel
    destination = DESTINATIONS[source.resolve()]
    initial_hash = digest(source)
    item = ITEMS[str(rel)]
    if item['mode'] == 'original':
        original = ROOT / item['original_pdf']
        shutil.copyfile(original, destination)
        return {'source': str(rel), 'pdf': destination.name,
                'mode': 'original préservé, non régénéré',
                'original_pdf': item['original_pdf'],
                'source_sha256': initial_hash, 'pdf_sha256': digest(destination),
                'pages': len(PdfReader(destination).pages),
                'bytes': destination.stat().st_size, 'layout_issues': [],
                'images_in_source': 0}
    text = source.read_text()
    title = text.splitlines()[0].lstrip('# ').strip()
    log_path = TMP / (destination.stem + '.log')
    handler = logging.FileHandler(log_path)
    logging.getLogger('weasyprint').addHandler(handler)
    logging.getLogger('weasyprint').setLevel(logging.WARNING)
    body = markdown.markdown(text, extensions=['tables', 'fenced_code', 'sane_lists', 'toc', 'attr_list'],
                             extension_configs={'toc': {'slugify': slugify_unicode}})
    if source.parent.name == 'correspondances-avocats-20261116':
        body = expand_long_table_fields(body)
    if source.name == 'rapport-comparaison-SHA512-exhaustive-1555-fichiers.md':
        body = re.sub(r'(<h4\b[^>]*>F\d{4}\b.*?</h4>\s*<p>.*?</p>\s*<pre>.*?</pre>)',
                      r'<section class="proof-record">\1</section>', body, flags=re.S)
    body = keep_final_signature(body)

    def image_url(match):
        value = html.unescape(match.group(1))
        if urlsplit(value).scheme:
            return match.group(0)
        target = (source.parent / unquote(value)).resolve()
        if not target.is_file():
            raise FileNotFoundError(target)
        return 'src="' + html.escape(target.as_uri(), quote=True) + '"'

    body = re.sub(r'src="([^"]+)"', image_url, body)
    if source.name == 'RAPPORT-FINAL-SADEDINE-2026.md':
        # Keep each of the seven opening points together for a balanced 3-page summary.
        opening, remainder = body.split('<h2 id="2-comprendre-la-mission-et-les-appareils">', 1)
        opening = re.sub(r'(<h3\b.*?)(?=<h3\b|\Z)',
                         r'<section class="summary-point">\1</section>', opening, flags=re.S)
        body = opening + '<h2 id="2-comprendre-la-mission-et-les-appareils">' + remainder
        body = body.replace('<h2 id="2-comprendre-la-mission-et-les-appareils">',
                            '<h2 style="break-before:page" id="2-comprendre-la-mission-et-les-appareils">')
    short_title = source.stem.replace('analyse-', '').replace('RAPPORT-FINAL-', 'Rapport final - ')
    document = '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
    document += '<title>' + html.escape(title) + '</title>'
    document += '<meta name="author" content="Christophe DOnnat — Donnat Dev"></head><body>'
    document += '<div class="short-title">' + html.escape(short_title) + '</div>' + body + '</body></html>'
    (TMP / (destination.stem + '.html')).write_text(document)
    css = CSS_TEXT
    if source.name == 'liste-complete-fichiers-28oct2024.md':
        css += '\nth, td { box-sizing: border-box; }'
        for column, width in enumerate([9, 35, 8, 10, 20, 18], 1):
            css += f'\nth:nth-child({column}), td:nth-child({column}) {{ width: {width}%; }}'
    rendered = HTML(string=document, base_url=str(source.parent), url_fetcher=URLFetcher(allowed_protocols=['file', 'data'], fail_on_errors=True)).render(stylesheets=[CSS(string=css)])
    issues = []
    for n, page in enumerate(rendered.pages, 1):
        for box in page._page_box.descendants():
            if type(box).__name__ == 'TextBox' and getattr(box, 'text', '').strip():
                if box.position_x < 63 or box.position_x + box.width > page.width - 63:
                    issues.append({'page': n, 'type': 'horizontal', 'x': round(box.position_x, 1),
                                   'width': round(box.width, 1), 'text': box.text[:120]})
                if box.position_y < 0 or box.position_y + box.height > page.height:
                    issues.append({'page': n, 'type': 'vertical', 'text': box.text[:120]})
    raw_path = TMP / destination.name
    rendered.write_pdf(raw_path)
    reader = PdfReader(raw_path)
    writer = PdfWriter(clone_from=reader)
    for page in writer.pages:
        for ref in page.get('/Annots', []):
            annotation = ref.get_object()
            action = annotation.get('/A')
            if not action or action.get('/S') != '/URI':
                continue
            value = str(action.get('/URI', ''))
            parsed = urlsplit(value)
            if parsed.scheme != 'file':
                continue
            target = Path(unquote(parsed.path)).resolve()
            if target in DESTINATIONS:
                target = DESTINATIONS[target]
            relative = os.path.relpath(target, OUT)
            if parsed.fragment:
                relative += '#' + parsed.fragment
            action[NameObject('/URI')] = TextStringObject(relative)
    writer.write(destination)
    assert digest(source) == initial_hash, 'Source changed during conversion'
    result = {'source': str(rel), 'pdf': destination.name, 'pages': len(reader.pages),
              'source_sha256': initial_hash, 'pdf_sha256': digest(destination),
              'bytes': destination.stat().st_size, 'layout_issues': issues,
              'images_in_source': body.count('<img ')}
    (TMP / (destination.stem + '.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(f'{destination.name}: {result["pages"]} pages, {len(issues)} layout issues', flush=True)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Générer la sélection documentaire du 18 novembre, sans toucher aux PDF historiques.')
    parser.add_argument('--replace', action='store_true', help='Régénérer uniquement les sorties de cette sélection dans le dossier daté.')
    parser.add_argument('--only', nargs='+', help='Sources de la sélection à régénérer après correction ; nécessite --replace.')
    args = parser.parse_args()
    if args.only and not args.replace:
        parser.error('--only nécessite --replace')
    selected = SOURCES if not args.only else [Path(s) for s in args.only]
    if not set(selected).issubset(set(SOURCES)):
        parser.error('Source absente de la sélection')
    if not args.replace and any(DESTINATIONS[(ROOT / s).resolve()].exists() for s in selected):
        parser.error('Sorties existantes : utiliser --replace pour cette livraison datée')
    OUT.mkdir(exist_ok=True, parents=True)
    generation_lock = (OUT / '.generation.lock').open('a')
    try:
        fcntl.flock(generation_lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        parser.error('Une génération de cette livraison est déjà en cours')
    TMP.mkdir(exist_ok=True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=3, mp_context=multiprocessing.get_context('fork')) as pool:
        results = list(pool.map(generate, selected))
    manifest = OUT / 'manifest-20261118.json'
    if args.only and manifest.exists():
        previous = {r['source']: r for r in json.loads(manifest.read_text())['rapports']}
        previous.update({r['source']: r for r in results})
        results = [previous[str(s)] for s in SOURCES]
    manifest.write_text(json.dumps({'date_revision': SELECTION['date'], 'selection': 'generer-pdf/livraison-20261118.json', 'rapports': results}, ensure_ascii=False, indent=2) + '\n')
    print('TOTAL:', len(results), 'PDFs,', sum(r['pages'] for r in results), 'pages')
    print('Journaux et contrôles de mise en page :', TMP)
