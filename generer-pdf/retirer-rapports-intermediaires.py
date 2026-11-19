"""Préparer puis publier le retrait des PDF intermédiaires approuvés.

Sans argument : préparer les corrections de liens dans /tmp, sans toucher à rendu.
--publish DOSSIER : appliquer après contrôle visuel et vérifier la remise.
"""
from pathlib import Path
from urllib.parse import unquote
import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'rendu'
SUB = OUT / 'rapports-subsidiaires'
POLICY = ROOT / 'generer-pdf/documents-intermediaires-exclus.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'generer-pdf' / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def stage():
    organiser = load('organiser_retrait', 'reorganiser-rendu.py')
    manifest = json.loads((SUB / 'manifest-rendu.json').read_text())
    sources = {x['source'] for x in json.loads(POLICY.read_text())['documents']}
    removed = [x for x in manifest['documents'] if x['source'] in sources]
    if not removed:
        print('Les retraits sont déjà appliqués.')
        return
    assert len(removed) == 17 and sum(x['pages'] for x in removed) == 65
    assert all(Path(x['pdf']).name not in organiser.MAIN for x in removed)
    work = Path(tempfile.mkdtemp(prefix='dmm-retrait-intermediaires-'))
    (work / 'manifest-avant.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    pieces = {x['source']: x for x in manifest['pieces']}
    locations = {p.resolve(): p.resolve() for p in OUT.rglob('*')}
    retired = {OUT / x['pdf'] for x in removed}
    for item in removed:
        path = OUT / item['pdf']
        target = OUT / pieces[item['source']]['destination']
        assert digest(path) == item['pdf_sha256'] and target.is_file()
        locations[path.resolve()] = target.resolve()
    changes = []
    for pdf in sorted(OUT.rglob('*.pdf')):
        if pdf in retired:
            continue
        with pdf.open('rb') as stream:
            if b'%PDF-' not in stream.read(1024):
                continue
        staged, pages, count = organiser.prepare_pdf(pdf, pdf, locations, work)
        if staged:
            before = work / 'avant' / pdf.relative_to(OUT)
            before.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(pdf, before)
            changes.append({'pdf': str(pdf.relative_to(OUT)), 'staged': str(staged),
                            'before_sha256': digest(pdf), 'sha256': digest(staged),
                            'pages': pages, 'liens_adaptes': count})
    state = {'retires': removed, 'adaptes': changes,
             'manifest_avant_sha256': digest(SUB / 'manifest-rendu.json'),
             'flux_dessin_images_et_texte_identiques': True}
    (work / 'preparation.json').write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    Path('/tmp/dmm-retrait-intermediaires-travail.json').write_text(json.dumps({'work': str(work)}) + '\n')
    print(f'{len(removed)} retraits préparés ; {len(changes)} PDF adaptés ; '
          f'{sum(x["liens_adaptes"] for x in changes)} liens redirigés.', flush=True)
    print('Dossier de travail : ' + str(work), flush=True)


def publish(work):
    state = json.loads((work / 'preparation.json').read_text())
    assert json.loads((work / 'controle-visuel.json').read_text())['passed']
    manifest_path = SUB / 'manifest-rendu.json'
    assert digest(manifest_path) == state['manifest_avant_sha256']
    manifest = json.loads(manifest_path.read_text())
    retired = {x['pdf'] for x in state['retires']}
    names = {Path(x).name for x in retired}
    changes = {x['pdf']: x for x in state['adaptes']}
    for item in state['retires']:
        assert digest(OUT / item['pdf']) == item['pdf_sha256']
    for item in changes.values():
        assert digest(OUT / item['pdf']) == item['before_sha256']
        assert digest(Path(item['staged'])) == item['sha256']

    # Keep rollback copies outside the delivery; no evidence/source file is removed.
    for item in state['retires']:
        path = OUT / item['pdf']
        backup = work / 'retires' / path.name
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, backup)
        path.unlink()
    for item in changes.values():
        path = OUT / item['pdf']
        temporary = path.with_suffix('.liens.tmp')
        shutil.copyfile(item['staged'], temporary)
        os.replace(temporary, path)

    def mentions(value):
        return isinstance(value, str) and any(n in unquote(value) for n in names)

    def prune(value):
        if isinstance(value, dict):
            return {k: prune(v) for k, v in value.items() if not mentions(k) and not mentions(v)}
        if isinstance(value, list):
            return [prune(x) for x in value
                    if not mentions(x) and not (isinstance(x, dict) and mentions(x.get('pdf')))]
        return value

    manifest['documents'] = [x for x in manifest['documents'] if x['pdf'] not in retired]
    for item in manifest['documents']:
        if item['pdf'] in changes:
            path = OUT / item['pdf']
            item.update(pdf_sha256=digest(path), bytes=path.stat().st_size)
    manifest['organisation']['rapports_subsidiaires'] = 20
    manifest['selections_remise'] = ['generer-pdf/documents-internes.json', str(POLICY.relative_to(ROOT))]
    manifest['retrait_comptes_rendus_intermediaires'] = {
        'pdf_retires': 17, 'pages_retires': 65, 'pdf_liens_adaptes': len(changes),
        'liens_adaptes': sum(x['liens_adaptes'] for x in changes.values()),
        'sources_et_pieces_conservees': True}
    manifest = prune(manifest)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    visual_path = SUB / 'controle-visuel.json'
    visual = prune(json.loads(visual_path.read_text()))
    for item in visual['documents']:
        if item['pdf'] in changes:
            item['sha256'] = changes[item['pdf']]['sha256']
    visual['documents_inspectes'] = len(visual['documents'])
    visual['pages_finales_inspectees'] = sum(len(x['pages_inspectees']) for x in visual['documents'])
    visual['retrait_comptes_rendus_intermediaires'] = {
        **manifest['retrait_comptes_rendus_intermediaires'],
        'flux_dessin_images_et_texte_identiques': True,
        'controle_visuel': json.loads((work / 'controle-visuel.json').read_text())}
    visual_path.write_text(json.dumps(visual, ensure_ascii=False, indent=2) + '\n')
    organiser = load('organiser_publication_retrait', 'reorganiser-rendu.py')
    organiser.write_indexes(manifest)
    controls = load('controles_publication_retrait', 'generer-rendu.py')
    assert controls.verify(check_hashes=False)['passed']

    # Remove old entries and rehash only changed files; evidence is byte-for-byte unchanged.
    target = SUB / 'SHA256SUMS.txt'
    checks = {}
    for line in target.read_text().splitlines():
        value, name = line.split('  ', 1)
        if name not in retired:
            checks[name] = value
    modified = {manifest_path, visual_path, SUB / 'verification-rendu.json',
                SUB / 'LISEZ-MOI.txt', SUB / 'index.html', OUT / 'index.html'}
    modified.update(OUT / name for name in changes)
    for path in modified:
        checks[str(path.relative_to(OUT))] = digest(path)
    assert set(checks) == {str(p.relative_to(OUT)) for p in OUT.rglob('*') if p.is_file() and p != target}
    for item in manifest['documents']:
        assert checks[item['pdf']] == item['pdf_sha256']
    for item in manifest['pieces']:
        assert checks[item['destination']] == item['sha256']
    target.write_text(''.join(f'{value}  {name}\n' for name, value in sorted(checks.items())))
    patterns = work / 'noms-retires.txt'
    patterns.write_text('\n'.join(sorted(names)) + '\n')
    check = subprocess.run(['rg', '-l', '-F', '-f', str(patterns), str(OUT)], capture_output=True, text=True)
    assert check.returncode == 1, check.stdout + check.stderr
    assert not any(p.name in names for p in OUT.rglob('*'))
    for entry in manifest['documents']:
        assert (OUT / entry['pdf']).is_file()
    assert len(manifest['documents']) == 36
    state['passed'] = True
    (work / 'resultat.json').write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
    print('17 PDF retirés ; 36 documents conservés (16 principaux et 20 subsidiaires).', flush=True)
    print('Index, métadonnées et empreintes mis à jour ; aucune référence textuelle aux PDF retirés.', flush=True)
    print('Contrôles : ' + str(work), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', type=Path)
    arguments = parser.parse_args()
    if arguments.publish:
        publish(arguments.publish)
    else:
        stage()
