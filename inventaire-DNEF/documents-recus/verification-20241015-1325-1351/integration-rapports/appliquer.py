"""Applique uniquement les deux versions préparées si les sources sont inchangées."""
from pathlib import Path
import hashlib
import json

base = Path(__file__).resolve().parent
manifest = json.loads((base/'manifest.json').read_text())
allowed = {
    '/mnt/data/codeProjects/DMMConseils/telephones/analyse-TP-03.md',
    '/mnt/data/codeProjects/DMMConseils/RAPPORT-FINAL-SADEDINE-2026.md',
}
assert {x['target'] for x in manifest} == allowed
def sha(data):
    return hashlib.sha256(data).hexdigest()
for x in manifest:
    assert sha(Path(x['target']).read_bytes()) == x['before_sha256'], 'Rapport modifié depuis la préparation : '+x['target']
    assert sha((base/x['after']).read_bytes()) == x['after_sha256']
for x in manifest:
    target = Path(x['target'])
    target.write_bytes((base/x['after']).read_bytes())
    assert sha(target.read_bytes()) == x['after_sha256']
    print('Mis à jour : '+str(target))
