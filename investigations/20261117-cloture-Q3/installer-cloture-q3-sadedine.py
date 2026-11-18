from pathlib import Path
import hashlib
import json
import os
import shutil

ROOT = Path('/mnt/data/codeProjects/DMMConseils')
STAGE = Path('/tmp/sadedine-cloture-q3-20261117')
ARCHIVE = ROOT / 'investigations/20261117-cloture-Q3'
changes = json.loads((STAGE / 'audit/modifications.json').read_text())
assert not ARCHIVE.exists(), ARCHIVE
for item in changes:
    assert hashlib.sha256((ROOT / item['path']).read_bytes()).hexdigest() == item['before_sha256'], item['path']
    assert hashlib.sha256((STAGE / item['path']).read_bytes()).hexdigest() == item['after_sha256'], item['path']
assert all(not r['layout_issues'] for r in json.loads((STAGE / 'audit/generation.json').read_text()))
ARCHIVE.mkdir(parents=True)
shutil.copytree(STAGE / 'avant', ARCHIVE / 'avant')
(ARCHIVE / 'audit').mkdir()
for p in (STAGE / 'audit').glob('*'):
    if p.is_file() and p.suffix in ['.json', '.diff', '.log']:
        shutil.copy2(p, ARCHIVE / 'audit' / p.name)
for script in ['cloturer-q3-sadedine.py', 'generer-pdf-cloture-q3.py', 'installer-cloture-q3-sadedine.py']:
    shutil.copy2(Path('/tmp') / script, ARCHIVE / script)
for item in changes:
    old = ARCHIVE / 'avant' / item['path']
    assert hashlib.sha256(old.read_bytes()).hexdigest() == item['before_sha256'], old
for item in changes:
    target = ROOT / item['path']
    assert hashlib.sha256(target.read_bytes()).hexdigest() == item['before_sha256'], target
    temporary = target.with_name('.' + target.name + '.cloture-q3-20261117')
    with temporary.open('xb') as handle:
        handle.write((STAGE / item['path']).read_bytes())
    os.chmod(temporary, target.stat().st_mode & 0o777)
    os.replace(temporary, target)
    assert hashlib.sha256(target.read_bytes()).hexdigest() == item['after_sha256'], target

readme = '''# Réponse Q3 sur iCloud et les doublons

Mise à jour du 17 novembre 2026, à la demande du prestataire.

La question Q3 de la note cliente est clôturée sur la base des éléments disponibles, avec une incertitude explicite sur l'origine des doublons et le premier déverrouillage. Les rapports distinguent l'accès au contenu protégé des métadonnées conservées. Une contribution d'iCloud n'est ni confirmée ni exclue ; aucun conflit iCloud précis n'est identifié dans les éléments examinés.

Les compléments sont intégrés au rapport TP-03 (sections 7.3 et 7.6), au rapport B–E (parties B et E) et au point 1.9 du rapport final. Une formulation de la réponse Q1 est harmonisée. Les mentions relatives aux essais envisagés ont été retirées des développements concernés. Les preuves, résultats techniques et protocoles antérieurs restent inchangés.

Les deux PDF principaux ont été régénérés. Les rubriques et numéros de sections existants sont conservés. Les contrôles de contenu et de limites de page sont consignés dans `audit/generation.json`. Les rendus de contrôle ont été inspectés avant installation : ensemble des pages en planches et pages modifiées en détail.

Les versions précédentes sont conservées dans `avant/`, avec leurs empreintes dans `audit/modifications.json`. Les empreintes courantes sont dans `SHA256SUMS.txt`. Les anciens bordereaux d'empreintes restent des relevés historiques de leurs versions ; ils n'ont pas été réécrits.
'''
(ARCHIVE / 'README.md').write_text(readme)
sums = [item['after_sha256'] + '  ' + item['path'] for item in changes]
(ARCHIVE / 'SHA256SUMS.txt').write_text('\n'.join(sums) + '\n')
print('Mise à jour installée :')
print('\n'.join(item['path'] for item in changes))
print('Versions précédentes :', ARCHIVE / 'avant')
