"""Corriger les signatures courantes et préparer les seuls PDF de remise concernés.

Sans argument : correction des Markdown et rendu de travail dans /tmp/.
--publish DOSSIER : publier les PDF contrôlés de ce dossier de travail.
"""
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from urllib.parse import urlsplit, unquote, quote
import argparse
import hashlib
import html
import importlib.util
import json
import multiprocessing
import os
import re
import shutil
import sys
import tempfile

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'rendu'
SUB = OUT / 'rapports-subsidiaires'
AUTHOR = 'Christophe Donnat — Donnat Dev'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def corrected(text):
    text = text.replace('Christophe DOnnat', 'Christophe Donnat')
    return re.sub(r'Christophe Donnat\s*[—–-]\s*Donnat De\b', AUTHOR, text)


def canonical(text):
    return re.sub(r'\s+', '', corrected(text))


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'generer-pdf' / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def stage():
    manifest = json.loads((SUB / 'manifest-rendu.json').read_text())
    cfg = json.loads((ROOT / 'generer-pdf/livraison-20261118.json').read_text())
    source_paths = {x['source'] for x in cfg['documents'] if x.get('mode') != 'original'}
    source_paths.update(x['source'] for x in manifest['documents'] if not x.get('original_pdf'))
    changed = [name for name in sorted(source_paths)
               if corrected((ROOT / name).read_text()) != (ROOT / name).read_text()]
    documents = [x for x in manifest['documents'] if x['source'] in changed]
    if not documents:
        raise RuntimeError('Aucune signature à corriger dans les documents de remise.')
    work = Path(tempfile.mkdtemp(prefix='dmm-signatures-'))
    (work / 'manifest-avant.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    for name in changed:
        source = ROOT / name
        backup = work / 'sources-avant' / name
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, backup)
        source.write_text(corrected(source.read_text()))
        assert corrected(backup.read_text()) == source.read_text()
    command = ROOT / 'generer-pdf/commande.md'
    command.write_text(corrected(command.read_text()))
    rendered = work / 'rendu'
    mapping = {}
    for item in manifest['pieces']:
        source = ROOT / item['source']
        target = rendered / item['destination']
        mapping[source.resolve()] = target
        while source.parent.is_relative_to(ROOT):
            source, target = source.parent, target.parent
            mapping[source.resolve()] = target
            if source == ROOT:
                break
    mapping.update({(ROOT / x['source']).resolve(): rendered / x['pdf'] for x in manifest['documents']})
    for item in documents:
        destination = rendered / item['pdf']
        destination.parent.mkdir(parents=True, exist_ok=True)
        backup = work / 'pdf-avant' / item['pdf']
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(OUT / item['pdf'], backup)
    generator = load('generer_rapports_signatures', 'generer-rapports.py')
    generator.OUT, generator.DESTINATIONS = rendered, mapping
    with ProcessPoolExecutor(max_workers=3, mp_context=multiprocessing.get_context('fork')) as pool:
        generated = list(pool.map(generator.generate, [Path(x['source']) for x in documents]))
    results = []
    for previous, result in zip(documents, generated):
        result['pdf'] = previous['pdf']
        path = rendered / result['pdf']
        before = PdfReader(work / 'pdf-avant' / result['pdf'])
        after = PdfReader(path)
        assert len(after.pages) == len(before.pages) == result['pages'], result['pdf']
        assert not result['layout_issues'], result['pdf']
        old_text = '\n'.join(p.extract_text() for p in before.pages)
        new_text = '\n'.join(p.extract_text() for p in after.pages)
        assert canonical(old_text) == canonical(new_text), 'Texte hors signature modifié : ' + result['pdf']
        assert 'Christophe DOnnat' not in new_text and not re.search(r'Donnat De\b', new_text)
        assert AUTHOR in new_text, result['pdf']
        assert after.metadata.author == AUTHOR, result['pdf']
        results.append(result)
    state = {'sources_corrigees': changed, 'documents': results,
             'source_generation': 'generer-pdf/generer-rapports.py',
             'renderer_sha256': digest(ROOT / 'generer-pdf/generer-rapports.py'),
             'pagination_et_texte_hors_signature_identiques': True}
    (work / 'generation.json').write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    Path('/tmp/dmm-signatures-travail.json').write_text(json.dumps({'work': str(work)}) + '\n')
    print(f'{len(changed)} Markdown corrigés ; {len(results)} PDF préparés.', flush=True)
    print('Pagination et texte hors signature identiques ; métadonnées auteur corrigées.', flush=True)
    print('Dossier de travail : ' + str(work), flush=True)


def portable_copy(source, destination, piece_map):
    text = source.read_text()
    relocated = False

    def replace(match):
        nonlocal relocated
        value = urlsplit(match.group(1))
        target = Path(unquote(value.path)).resolve()
        if not target.is_relative_to(ROOT):
            return match.group(0)
        assert target in piece_map, target
        url = quote(os.path.relpath(piece_map[target], destination.parent), safe='/')
        if value.fragment:
            url += '#' + value.fragment
        relocated = True
        return '](' + url + ')'

    text = re.sub(r'\]\((/[^)]+)\)', replace, text)
    destination.write_text(text)
    return relocated


def publish(work):
    state = json.loads((work / 'generation.json').read_text())
    review = json.loads((work / 'controle-visuel.json').read_text())
    assert review['passed']
    for item in state['documents']:
        assert digest(ROOT / item['source']) == item['source_sha256']
        assert digest(work / 'rendu' / item['pdf']) == item['pdf_sha256']
        assert review['pdf_sha256'][item['pdf']] == item['pdf_sha256']
    manifest_path = SUB / 'manifest-rendu.json'
    manifest = json.loads(manifest_path.read_text())
    replacements = {x['source']: x for x in state['documents']}
    for item in manifest['documents']:
        if item['source'] in replacements:
            updated = replacements[item['source']]
            shutil.copy2(work / 'rendu' / updated['pdf'], OUT / updated['pdf'])
            item.update(updated)
    piece_map = {(ROOT / x['source']).resolve(): OUT / x['destination'] for x in manifest['pieces']}
    changed = set(state['sources_corrigees'])
    copied = []
    for item in manifest['pieces']:
        if item['source'] not in changed:
            continue
        source, destination = ROOT / item['source'], OUT / item['destination']
        relocated = portable_copy(source, destination, piece_map)
        item.update(source_sha256=digest(source), sha256=digest(destination),
                    bytes=destination.stat().st_size, liens_absolus_relativises=relocated)
        copied.append(item['destination'])
    manifest['correction_signature'] = {'signature': AUTHOR,
        'sources_corrigees': len(changed), 'pdf_regeneres': len(replacements),
        'pagination_et_texte_hors_signature_identiques': True}
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    visual_path = SUB / 'controle-visuel.json'
    visual = json.loads(visual_path.read_text())
    updates = {x['pdf']: x for x in replacements.values()}
    for item in visual['documents']:
        if item['pdf'] in updates:
            item['sha256'] = updates[item['pdf']]['pdf_sha256']
            item['pages_inspectees'] = sorted(set(item['pages_inspectees']) | set(review['pages_inspectees'][item['pdf']]))
    visual['correction_signature'] = review
    visual['pages_finales_inspectees'] = sum(len(x['pages_inspectees']) for x in visual['documents'])
    visual_path.write_text(json.dumps(visual, ensure_ascii=False, indent=2) + '\n')
    organiser = load('organisation_signatures', 'reorganiser-rendu.py')
    organiser.write_indexes(manifest)
    controls = load('controles_signatures', 'generer-rendu.py')
    assert controls.verify(check_hashes=False)['passed']
    target = SUB / 'SHA256SUMS.txt'
    checks = {}
    for line in target.read_text().splitlines():
        value, name = line.split('  ', 1)
        checks[name] = value
    modified = {str(p.relative_to(OUT)) for p in [manifest_path, visual_path,
        SUB / 'verification-rendu.json', SUB / 'LISEZ-MOI.txt', SUB / 'index.html', OUT / 'index.html']}
    modified.update(updates)
    modified.update(copied)
    for name in modified:
        checks[name] = digest(OUT / name)
    assert set(checks) == {str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file() and p != target}
    for item in manifest['documents']:
        assert checks[item['pdf']] == item['pdf_sha256']
    for item in manifest['pieces']:
        assert checks[item['destination']] == item['sha256']
    target.write_text(''.join(f'{value}  {name}\n' for name, value in sorted(checks.items())))
    print(f'{len(replacements)} PDF remplacés dans rendu/ ; copies sources et empreintes mises à jour.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', type=Path)
    arguments = parser.parse_args()
    if arguments.publish:
        publish(arguments.publish)
    else:
        stage()
