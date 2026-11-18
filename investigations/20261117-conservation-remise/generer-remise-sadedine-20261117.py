from pathlib import Path
import hashlib, html, importlib.util, json, logging, os, re
from urllib.parse import unquote, urlsplit
import markdown
from weasyprint import HTML, CSS
from weasyprint.urls import URLFetcher
from pypdf import PdfReader, PdfWriter
from pypdf.generic import TextStringObject, NameObject

ROOT = Path('/mnt/data/codeProjects/DMMConseils')
STAGE = Path('/tmp/sadedine-remise-20261117')
spec = importlib.util.spec_from_file_location('rapport_style', ROOT/'generer-pdf/generer-rapports.py')
style = importlib.util.module_from_spec(spec)
spec.loader.exec_module(style)
items = {
 'RAPPORT-FINAL-SADEDINE-2026.md': 'pdfs/RAPPORT-FINAL-SADEDINE-2026.pdf',
 'cartes_sd/analyse-cartes_sd.md': 'pdfs/analyse-cartes_sd.pdf',
 'remise-documents/bordereau-mise-a-disposition-donnees-20261117.md': 'remise-documents/bordereau-mise-a-disposition-donnees-20261117.pdf',
 'remise-documents/rectificatif-attestation-remise-20261117.md': 'remise-documents/rectificatif-attestation-remise-20261117.pdf',
}
targets = dict(style.DESTINATIONS)
targets.update({(ROOT/a).resolve(): ROOT/b for a,b in items.items()})
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
results = []
for src, dest in items.items():
    source = STAGE/src
    final_source = ROOT/src
    final_dest = ROOT/dest
    output = STAGE/dest
    output.parent.mkdir(parents=True, exist_ok=True)
    log = STAGE/'audit'/(source.stem+'.log')
    handler = logging.FileHandler(log)
    logging.getLogger('weasyprint').addHandler(handler)
    logging.getLogger('weasyprint').setLevel(logging.WARNING)
    text = source.read_text()
    title = text.splitlines()[0].lstrip('# ')
    body = markdown.markdown(text, extensions=['tables','fenced_code','sane_lists','toc','attr_list'])
    def image_url(m):
        val = html.unescape(m[1])
        if urlsplit(val).scheme: return m[0]
        path = (final_source.parent/unquote(val)).resolve()
        assert path.exists(), path
        return 'src="'+html.escape(path.as_uri(),quote=True)+'"'
    body = re.sub(r'src="([^"]+)"', image_url, body)
    doc = '<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>'+html.escape(title)+'</title><meta name="author" content="Christophe Donnat - Donnat Dev"></head><body><div class="short-title">'+html.escape(source.stem)+'</div>'+body+'</body></html>'
    css = style.CSS_TEXT
    if src.startswith('remise-documents/'):
        css += '''
        html { font-size: 9pt; color: #111; }
        h1 { font-size: 19pt; color: #000; border: none; padding-bottom: 0; margin-bottom: 5mm; }
        h2 { font-size: 12pt; color: #000; border: none; padding-bottom: 0; margin-top: 5mm; }
        h3 { color: #000; }
        pre { font-size: 8pt; background: none; padding: 0; margin: 1mm 0 3mm; }
        table { font-size: 8.5pt; }
        th, td { border-color: #d9d9d9; padding: 2mm; }
        th { color: #000; background: #eee; }
        '''
    rendered = HTML(string=doc, base_url=str(final_source.parent), url_fetcher=URLFetcher(allowed_protocols=['file','data'], fail_on_errors=True)).render(stylesheets=[CSS(string=css)])
    issues=[]
    for n,page in enumerate(rendered.pages,1):
        for box in page._page_box.descendants():
            if type(box).__name__=='TextBox' and getattr(box,'text','').strip():
                if box.position_x < 62 or box.position_x+box.width > page.width-62:
                    issues.append({'page':n,'text':box.text[:80],'type':'horizontal'})
                if box.position_y < 0 or box.position_y+box.height > page.height:
                    issues.append({'page':n,'text':box.text[:80],'type':'vertical'})
    raw = STAGE/'audit'/(output.stem+'-raw.pdf')
    rendered.write_pdf(raw)
    writer=PdfWriter(clone_from=PdfReader(raw))
    for page in writer.pages:
        for ref in page.get('/Annots',[]):
            a=ref.get_object().get('/A')
            if not a or a.get('/S')!='/URI': continue
            u=urlsplit(str(a.get('/URI','')))
            if u.scheme!='file': continue
            path=Path(unquote(u.path)).resolve()
            path=targets.get(path,path)
            value=os.path.relpath(path,final_dest.parent)
            if u.fragment: value+='#'+u.fragment
            a[NameObject('/URI')]=TextStringObject(value)
    writer.write(output)
    logging.getLogger('weasyprint').removeHandler(handler)
    handler.close()
    results.append({'source':src,'pdf':dest,'pages':len(rendered.pages),'source_sha256':sha(source),'pdf_sha256':sha(output),'bytes':output.stat().st_size,'layout_issues':issues,'images_in_source':body.count('<img ')})
    print(dest,len(rendered.pages),'pages',len(issues),'layout issues')

# Update only manifest entries for the two regenerated reports.
if (ROOT/'pdfs/manifest.json').exists():
    manifest=json.loads((ROOT/'pdfs/manifest.json').read_text())
    for result in results[:2]:
        entry={**result,'pdf':Path(result['pdf']).name}
        matches=[i for i,x in enumerate(manifest['rapports']) if x['source']==entry['source']]
        assert len(matches)==1,matches
        manifest['rapports'][matches[0]]=entry
    (STAGE/'pdfs/manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

reference_manifests = [
 'cartes_sd/recherche-SD-01/20261015/journaux/segments-sha256-fin.txt',
 'cartes_sd/recherche-SD-02/20261016/journaux/segments-sha256-fin.txt',
 'cartes_sd/recherche-SD-03/20261016/journaux/segments-sha256-fin.txt',
 'cartes_sd/recherche-SD-01/20261015/manifest-sha256.csv',
 'cartes_sd/recherche-SD-02/20261016/manifest-sha256.txt',
 'cartes_sd/recherche-SD-03/20261016/manifest-sha256.txt',
 'telephones/recherche-TP-01/collection.json',
 'telephones/recherche-TP-02/controle-manifeste.json',
 'telephones/recherche-TP-02/verification-empreintes-20261014.json',
 'ordinateur/recherche-OP-01/SHA256SUMS',
]
files=set(items)|set(items.values())|set(reference_manifests)
for p in (ROOT/'pdfs').glob('analyse*.pdf'): files.add(str(p.relative_to(ROOT)))
lines=['# SHA-256 des documents et des inventaires de contrôle associés au bordereau du 17/11/2026.',
       '# Chemins relatifs à la racine du dossier de travail DMMConseils.',
       '# Ce fichier identifie ces pièces ; les empreintes de chaque donnée extraite figurent dans les inventaires techniques associés.']
for rel in sorted(files):
    p=STAGE/rel if (STAGE/rel).exists() else ROOT/rel
    assert p.is_file(),p
    lines.append(sha(p)+'  '+rel)
(STAGE/'remise-documents/empreintes-controle-remise-20261117.sha256').write_text('\n'.join(lines)+'\n')
(STAGE/'audit/generation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('Empreintes de contrôle :',len(files),'documents et inventaires')
assert all(not x['layout_issues'] for x in results),results
