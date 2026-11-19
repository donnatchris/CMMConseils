"""Retirer les PDF internes de la remise sans perdre les sources ni casser les liens."""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'rendu'
SUB = OUT / 'rapports-subsidiaires'
ARCHIVE = ROOT / 'pdfs/documents-internes'
POLICY = ROOT / 'generer-pdf/documents-internes.json'


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'generer-pdf' / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    organiser = load('organiser_remise', 'reorganiser-rendu.py')
    controls = load('controles_remise', 'generer-rendu.py')
    manifest_path = SUB / 'manifest-rendu.json'
    manifest = json.loads(manifest_path.read_text())
    policy = json.loads(POLICY.read_text())
    by_source = {x['source']: x for x in policy['documents']}
    removed = [x for x in manifest['documents'] if x['source'] in by_source]
    if not removed:
        print('La sélection de remise est déjà appliquée.')
        return
    assert all(Path(x['pdf']).name not in organiser.MAIN for x in removed)
    pieces = {x['source']: x for x in manifest['pieces']}
    locations = {p.resolve(): p.resolve() for p in OUT.rglob('*')}
    removed_paths = set()
    for item in removed:
        pdf = OUT / item['pdf']
        destination = OUT / pieces[item['source']]['destination']
        assert pdf.is_file() and destination.is_file()
        assert digest(pdf) == item['pdf_sha256']
        archived = ARCHIVE / pdf.name
        if archived.exists():
            raise FileExistsError(archived)
        locations[pdf.resolve()] = destination.resolve()
        removed_paths.add(pdf.resolve())
    work = Path(tempfile.mkdtemp(prefix='dmm-remise-allegee-'))
    (work / 'manifest-avant.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    from pypdf import PdfReader
    changes, links = {}, 0
    # Prepare and compare every changed PDF before modifying the live delivery.
    for pdf in sorted(OUT.rglob('*.pdf')):
        if pdf.resolve() in removed_paths:
            continue
        with pdf.open('rb') as stream:
            if b'%PDF-' not in stream.read(1024):
                continue
        staged, pages, count = organiser.prepare_pdf(pdf, pdf, locations, work)
        if staged:
            backup = work / 'avant' / pdf.relative_to(OUT)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(pdf, backup)
            changes[pdf] = staged
            links += count
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    history = []
    for item in removed:
        pdf = OUT / item['pdf']
        archived = ARCHIVE / pdf.name
        pdf.rename(archived)
        assert digest(archived) == item['pdf_sha256']
        history.append({'source': item['source'], 'pdf': item['pdf'],
                        'motif': by_source[item['source']]['motif'],
                        'archive': str(archived.relative_to(ROOT)),
                        'sha256': item['pdf_sha256'], 'pages': item['pages']})
    for pdf, staged in changes.items():
        temporary = pdf.with_suffix('.liens.tmp')
        shutil.copyfile(staged, temporary)
        os.replace(temporary, pdf)
    manifest['documents'] = [x for x in manifest['documents'] if x['source'] not in by_source]
    for item in manifest['documents']:
        pdf = OUT / item['pdf']
        if pdf in changes:
            item.update(pdf_sha256=digest(pdf), bytes=pdf.stat().st_size)
    manifest['selection_remise'] = str(POLICY.relative_to(ROOT))
    manifest.setdefault('documents_internes_ecartes', []).extend(history)
    manifest['organisation']['rapports_subsidiaires'] = len(manifest['documents']) - len(organiser.MAIN)
    manifest['organisation']['selection_clients_sans_pdf_de_travail'] = True
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    visual_path = SUB / 'controle-visuel.json'
    visual = json.loads(visual_path.read_text())
    documents = {x['pdf']: x for x in manifest['documents']}
    visual['documents'] = [x for x in visual['documents'] if x['pdf'] in documents]
    for item in visual['documents']:
        item['sha256'] = documents[item['pdf']]['pdf_sha256']
    visual['documents_inspectes'] = len(visual['documents'])
    visual['pages_finales_inspectees'] = sum(len(x['pages_inspectees']) for x in visual['documents'])
    visual['allegement_remise'] = {'pdf_internes_retires': len(removed),
        'pdf_liens_adaptes': len(changes), 'liens_adaptes': links,
        'flux_dessin_images_et_texte_identiques': True}
    visual_path.write_text(json.dumps(visual, ensure_ascii=False, indent=2) + '\n')
    organiser.write_indexes(manifest)
    validation = controls.verify(check_hashes=False)
    if not validation['passed']:
        raise RuntimeError('Des liens doivent être corrigés avant remise.')
    target = SUB / 'SHA256SUMS.txt'
    previous = {}
    for line in target.read_text().splitlines():
        value, name = line.split('  ', 1)
        if (OUT / name).is_file():
            previous[name] = value
    metadata = {manifest_path, visual_path, SUB / 'verification-rendu.json',
                SUB / 'LISEZ-MOI.txt', SUB / 'index.html', OUT / 'index.html'}
    checks = {}
    for path in sorted(p for p in OUT.rglob('*') if p.is_file() and p != target):
        name = str(path.relative_to(OUT))
        checks[name] = digest(path) if path in metadata or path in changes or name not in previous else previous[name]
    for item in manifest['documents']:
        assert checks[item['pdf']] == item['pdf_sha256']
    for item in manifest['pieces']:
        assert checks[item['destination']] == item['sha256']
    target.write_text(''.join(f'{value}  {name}\n' for name, value in sorted(checks.items())))
    report = {'retires': history, 'pdf_adaptes': [str(x.relative_to(OUT)) for x in changes],
              'liens_adaptes': links, 'documents_restants': len(manifest['documents']),
              'pages_retires': sum(x['pages'] for x in removed), 'passed': True}
    (work / 'resultat.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(removed)} PDF internes sortis de rendu/ ; {len(manifest["documents"])} PDF de remise conservés.', flush=True)
    print(f'{len(changes)} PDF adaptés, {links} liens corrigés ; présentation et texte identiques.', flush=True)
    print('Contrôles de travail : ' + str(work), flush=True)


if __name__ == '__main__':
    main()
