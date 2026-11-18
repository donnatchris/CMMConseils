from pathlib import Path
import hashlib
import html
import importlib.util
import json
import logging
import os
import re
from urllib.parse import unquote, urlsplit
import markdown
from weasyprint import HTML, CSS
from weasyprint.urls import URLFetcher
from pypdf import PdfReader, PdfWriter
from pypdf.generic import TextStringObject, NameObject

ROOT = Path('/mnt/data/codeProjects/DMMConseils')
STAGE = Path('/tmp/sadedine-cloture-q3-20261117')
spec = importlib.util.spec_from_file_location('rapport_style', ROOT / 'generer-pdf/generer-rapports.py')
style = importlib.util.module_from_spec(spec)
spec.loader.exec_module(style)
items = {
    'telephones/analyse-TP-03.md': 'pdfs/analyse-TP-03.pdf',
    'RAPPORT-FINAL-SADEDINE-2026.md': 'pdfs/RAPPORT-FINAL-SADEDINE-2026.pdf',
}
results = []
for src, dest in items.items():
    source = STAGE / src
    final_source = ROOT / src
    final_dest = ROOT / dest
    output = STAGE / dest
    output.parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(STAGE / 'audit' / (source.stem + '.log'))
    logging.getLogger('weasyprint').addHandler(handler)
    logging.getLogger('weasyprint').setLevel(logging.WARNING)
    text = source.read_text()
    body = markdown.markdown(text, extensions=['tables', 'fenced_code', 'sane_lists', 'toc', 'attr_list'])
    def image_url(match):
        value = html.unescape(match[1])
        if urlsplit(value).scheme:
            return match[0]
        path = (final_source.parent / unquote(value)).resolve()
        assert path.is_file(), path
        return 'src="' + html.escape(path.as_uri(), quote=True) + '"'
    body = re.sub(r'src="([^"]+)"', image_url, body)
    document = '<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>'
    document += html.escape(text.splitlines()[0].lstrip('# '))
    document += '</title><meta name="author" content="Christophe Donnat - Donnat Dev"></head><body>'
    document += '<div class="short-title">' + html.escape(source.stem) + '</div>' + body + '</body></html>'
    (STAGE / 'audit' / (source.stem + '.html')).write_text(document)
    rendered = HTML(string=document, base_url=str(final_source.parent),
                    url_fetcher=URLFetcher(allowed_protocols=['file', 'data'], fail_on_errors=True)).render(stylesheets=[CSS(string=style.CSS_TEXT)])
    issues = []
    for number, page in enumerate(rendered.pages, 1):
        for box in page._page_box.descendants():
            if type(box).__name__ == 'TextBox' and getattr(box, 'text', '').strip():
                if box.position_x < 62 or box.position_x + box.width > page.width - 62:
                    issues.append({'page': number, 'type': 'horizontal', 'text': box.text[:100]})
                if box.position_y < 0 or box.position_y + box.height > page.height:
                    issues.append({'page': number, 'type': 'vertical', 'text': box.text[:100]})
    raw = STAGE / 'audit' / (output.stem + '-raw.pdf')
    rendered.write_pdf(raw)
    writer = PdfWriter(clone_from=PdfReader(raw))
    for page in writer.pages:
        for ref in page.get('/Annots', []):
            action = ref.get_object().get('/A')
            if not action or action.get('/S') != '/URI':
                continue
            parsed = urlsplit(str(action.get('/URI', '')))
            if parsed.scheme != 'file':
                continue
            target = Path(unquote(parsed.path)).resolve()
            target = style.DESTINATIONS.get(target, target)
            value = os.path.relpath(target, final_dest.parent)
            if parsed.fragment:
                value += '#' + parsed.fragment
            action[NameObject('/URI')] = TextStringObject(value)
    writer.write(output)
    reader = PdfReader(output)
    pages = [page.extract_text() for page in reader.pages]
    complete = '\n'.join(pages)
    assert 'Réponse à Q3' in complete
    assert 'origine exacte des doublons reste indéterminée' in re.sub(r'\s+', ' ', complete)
    assert not any(term in complete.lower() for term in ['iphone de test', 'matériel de test', 'validées expérimentalement'])
    q3_pages = [n for n, value in enumerate(pages, 1) if 'Réponse à Q3' in value]
    result = {'source': src, 'pdf': dest, 'pages': len(pages), 'q3_pages': q3_pages,
              'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'pdf_sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
              'bytes': output.stat().st_size, 'layout_issues': issues}
    results.append(result)
    logging.getLogger('weasyprint').removeHandler(handler)
    handler.close()
    print(json.dumps(result, ensure_ascii=False), flush=True)
    assert not issues, issues

(STAGE / 'audit' / 'generation.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
changes = json.loads((STAGE / 'audit' / 'modifications.json').read_text())
for entry in changes:
    entry['after_sha256'] = hashlib.sha256((STAGE / entry['path']).read_bytes()).hexdigest()
(STAGE / 'audit' / 'modifications.json').write_text(json.dumps(changes, ensure_ascii=False, indent=2) + '\n')
