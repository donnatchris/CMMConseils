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
from urllib.parse import unquote, urlsplit

import markdown
from weasyprint import HTML, CSS
from weasyprint.urls import URLFetcher
from pypdf import PdfReader, PdfWriter
from pypdf.generic import TextStringObject, NameObject

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'pdfs'
TMP = Path(tempfile.mkdtemp(prefix='dmm-pdf-qa-'))
SOURCES = [Path('RAPPORT-FINAL-SADEDINE-2026.md')]
for folder in ['cartes_sd', 'freebox', 'ordinateur', 'telephones']:
    SOURCES += [p.relative_to(ROOT) for p in sorted((ROOT / folder).glob('analyse*.md'))]
DESTINATIONS = {(ROOT / p).resolve(): OUT / p.with_suffix('.pdf').name for p in SOURCES}

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
td p { margin-bottom: 1mm; }
img { max-width: 100%; max-height: 220mm; object-fit: contain; display: block;
      margin: 3mm auto; break-inside: avoid; }
hr { border: 0; border-top: .5pt solid #ccd7df; margin: 5mm 0; }
'''

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def generate(rel):
    source = ROOT / rel
    destination = DESTINATIONS[source.resolve()]
    initial_hash = digest(source)
    text = source.read_text()
    title = text.splitlines()[0].lstrip('# ').strip()
    log_path = TMP / (source.stem + '.log')
    handler = logging.FileHandler(log_path)
    logging.getLogger('weasyprint').addHandler(handler)
    logging.getLogger('weasyprint').setLevel(logging.WARNING)
    body = markdown.markdown(text, extensions=['tables', 'fenced_code', 'sane_lists', 'toc', 'attr_list'])

    def image_url(match):
        value = html.unescape(match.group(1))
        if urlsplit(value).scheme:
            return match.group(0)
        target = (source.parent / unquote(value)).resolve()
        if not target.is_file():
            raise FileNotFoundError(target)
        return 'src="' + html.escape(target.as_uri(), quote=True) + '"'

    body = re.sub(r'src="([^"]+)"', image_url, body)
    short_title = source.stem.replace('analyse-', '').replace('RAPPORT-FINAL-', 'Rapport final - ')
    document = '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
    document += '<title>' + html.escape(title) + '</title>'
    document += '<meta name="author" content="Christophe Donnat - Donnat Dev"></head><body>'
    document += '<div class="short-title">' + html.escape(short_title) + '</div>' + body + '</body></html>'
    (TMP / (source.stem + '.html')).write_text(document)
    rendered = HTML(string=document, base_url=str(source.parent), url_fetcher=URLFetcher(allowed_protocols=['file', 'data'], fail_on_errors=True)).render(stylesheets=[CSS(string=CSS_TEXT)])
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
    (TMP / (source.stem + '.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(f'{destination.name}: {result["pages"]} pages, {len(issues)} layout issues', flush=True)
    return result

if __name__ == '__main__':
    OUT.mkdir(exist_ok=True)
    TMP.mkdir(exist_ok=True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=3, mp_context=multiprocessing.get_context('fork')) as pool:
        results = list(pool.map(generate, SOURCES))
    (OUT / 'manifest.json').write_text(json.dumps({'rapports': results}, ensure_ascii=False, indent=2) + '\n')
    print('TOTAL:', len(results), 'PDFs,', sum(r['pages'] for r in results), 'pages')
    print('Journaux et contrôles de mise en page :', TMP)
