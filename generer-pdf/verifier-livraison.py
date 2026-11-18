"""Contrôles documentaires de la sélection approuvée, sans accès aux supports."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import argparse
import hashlib
import json
import re
import subprocess
import markdown
from markdown.extensions.toc import slugify_unicode

ROOT = Path(__file__).resolve().parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.anchors = [], set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.anchors.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag == 'img' and 'src' in attrs:
            self.links.append(attrs['src'])

def rendered(path):
    parser = Links()
    parser.feed(markdown.markdown(path.read_text(), extensions=['tables', 'fenced_code', 'toc', 'attr_list'],
                                 extension_configs={'toc': {'slugify': slugify_unicode}}))
    return parser

def check(skip_pdf=False):
    selection = json.loads((ROOT / 'generer-pdf/livraison-20261118.json').read_text())
    sources = [ROOT / x['source'] for x in selection['documents']]
    scope = sources + [ROOT / 'revision-documentaire-20261118/README.md',
                       ROOT / 'revision-documentaire-20261118/controles-historiques.md']
    errors, counts, parsed = [], {}, {}
    for p in scope:
        parsed[p.resolve()] = rendered(p)
    link_count = 0
    for p in scope:
        for value in parsed[p.resolve()].links:
            bits = urlsplit(value)
            if bits.scheme or bits.netloc:
                continue
            target = (p.parent / unquote(bits.path)).resolve() if bits.path else p.resolve()
            link_count += 1
            if not target.exists():
                errors.append({'source': str(p.relative_to(ROOT)), 'missing': value})
            elif bits.fragment and target.suffix == '.md':
                if target not in parsed:
                    parsed[target] = rendered(target)
                if unquote(bits.fragment) not in parsed[target].anchors:
                    errors.append({'source': str(p.relative_to(ROOT)), 'anchor': value})
        # Do not let a malformed Markdown table silently drop extra cells in rendering.
        width = None
        for number, line in enumerate(p.read_text().splitlines(), 1):
            if not line.startswith('|'):
                width = None
                continue
            cells = len(re.split(r'(?<!\\)\|', line)) - 2
            if width is None:
                width = cells
            if cells != width:
                errors.append({'source': str(p.relative_to(ROOT)), 'table_line': number})
    counts['local_links'] = link_count
    # Proof rows must remain byte-for-byte identical to the committed pre-revision source.
    initial = json.loads((ROOT / 'revision-documentaire-20261118/etat-initial.json').read_text())
    head = initial['commit_recuperation']
    proof_paths = [
        'ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/rapport-comparaison-SHA512-exhaustive-1555-fichiers.md',
        'ordinateur/recherche-OP-01/inventaire-L16B-20241028-20261116/liste-complete-fichiers-28oct2024.md',
        'inventaire-DNEF/rapports/rapport-repartition-sage-458-pages.md',
    ]
    for name in proof_paths:
        old = subprocess.check_output(['git', 'show', f'{head}:{name}'], cwd=ROOT).decode()
        rows = lambda s: [l for l in s.splitlines() if l.startswith('|')]
        before, after = rows(old), rows((ROOT / name).read_text())
        if before != after:
            errors.append({'changed_proof_rows': name})
        counts[name] = {'proof_rows_preserved': before == after, 'rows_including_headers': len(after)}
        if 'SHA512-exhaustive' in name:
            # This annex stores the 1,555 individual results in headings and fenced blocks.
            individual = lambda s: [l for l in s.splitlines()
                                    if l.startswith(('#### F', '**IDENTIQUE**', '**DIVERGENT**', 'SHA-512 inventaire', 'SHA-512 image'))]
            old_records, new_records = individual(old), individual((ROOT / name).read_text())
            if old_records != new_records:
                errors.append({'changed_individual_comparisons': name})
            counts[name]['individual_comparisons_preserved'] = old_records == new_records
            counts[name]['individual_files'] = sum(l.startswith('#### F') for l in new_records)
    deletions = json.loads((ROOT / 'revision-documentaire-20261118/suppressions-et-deplacements.json').read_text())
    for item in deletions:
        ref = f"{item['commit']}:{item['chemin_supprime']}"
        actual = subprocess.check_output(['git', 'rev-parse', ref], cwd=ROOT).decode().strip()
        if actual != item['blob'] or (ROOT / item['chemin_supprime']).exists():
            errors.append({'deletion_record': item['chemin_supprime']})
    counts['historical_copies_removed'] = sum(x['nature'] == 'copie historique' for x in deletions)
    counts['other_merges_or_moves'] = sum(x['nature'] != 'copie historique' for x in deletions)
    preservation = json.loads((ROOT / 'revision-documentaire-20261118/preservation-hors-corpus.json').read_text())
    for item in preservation['restored']:
        if digest(ROOT / item['path']) != item['sha256_restored']:
            errors.append({'outside_scope_changed': item['path']})
    counts['outside_scope_preserved'] = len(preservation['restored'])
    if preservation['unmatched']:
        errors.append({'unrestored': preservation['unmatched']})
    # The original handover act differs only in relative photo links from its Git version.
    name = 'remise-documents/attestation-de-remise.md'
    original = subprocess.check_output(['git', 'show', f'{head}:{name}'], cwd=ROOT).decode()
    if original.replace('(remise-documents/photos/', '(photos/').rstrip() != (ROOT / name).read_text().rstrip():
        errors.append({'original_act_changed': name})
    if not skip_pdf:
        from pypdf import PdfReader
        out = ROOT / selection['output_directory']
        manifest = json.loads((out / 'manifest-20261118.json').read_text())
        if len(manifest['rapports']) != len(selection['documents']):
            errors.append({'pdf_count': len(manifest['rapports'])})
        for item in manifest['rapports']:
            pdf = out / item['pdf']
            if digest(ROOT / item['source']) != item['source_sha256'] or digest(pdf) != item['pdf_sha256']:
                errors.append({'manifest_hash': item['source']})
            if item['layout_issues']:
                errors.append({'layout': item['source'], 'issues': item['layout_issues']})
            reader = PdfReader(pdf)
            if len(reader.pages) != item['pages']:
                errors.append({'pdf_pages': item['pdf']})
            if 'SHA512-exhaustive' in item['source']:
                source_text = (ROOT / item['source']).read_text()
                pdf_text = re.sub(r'\s+', '', '\n'.join(p.extract_text() for p in reader.pages))
                expected_hashes = set(re.findall(r'\b[0-9a-f]{128}\b', source_text))
                absent = [value for value in expected_hashes if value not in pdf_text]
                if absent:
                    errors.append({'missing_complete_sha512_in_pdf': len(absent)})
                counts['complete_sha512_values_in_pdf'] = len(expected_hashes) - len(absent)
            for page in reader.pages:
                for ref in page.get('/Annots', []):
                    a = ref.get_object().get('/A')
                    if not a or a.get('/S') != '/URI':
                        continue
                    uri = str(a.get('/URI', ''))
                    bits = urlsplit(uri)
                    if bits.scheme or not bits.path:
                        continue
                    if not (out / unquote(bits.path)).resolve().exists():
                        errors.append({'pdf_link': item['pdf'], 'target': uri})
        final = PdfReader(out / 'RAPPORT-FINAL-SADEDINE-2026.pdf')
        section_two = next((i + 1 for i, p in enumerate(final.pages)
                            if '2. Comprendre la mission' in p.extract_text()), None)
        if section_two != 4:
            errors.append({'summary_pages': None if section_two is None else section_two - 1})
        counts['summary_pages'] = 3 if section_two == 4 else None
        counts['pdfs'] = len(manifest['rapports'])
        counts['pages'] = sum(x['pages'] for x in manifest['rapports'])
    result = {'revision': '2026-11-18', 'scope': 'Sélection documentaire explicite, sources techniques hors corpus vérifiées sans réécriture',
              'counts': counts, 'errors': errors, 'passed': not errors}
    (ROOT / 'revision-documentaire-20261118/validation-documentaire.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return not errors

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-pdf', action='store_true')
    raise SystemExit(0 if check(parser.parse_args().skip_pdf) else 1)
