"""Vérifie le rangement et les anciens manifestes sans modifier les preuves."""
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
AUDIT=Path(__file__).resolve().parent
journal=json.loads((AUDIT/'prive/journal-deplacement.json').read_text())
entries={x['ancien']:x for x in journal['fichiers']}
cache={}
def sha(p):
    if p not in cache:
        with p.open('rb') as f:cache[p]=hashlib.file_digest(f,'sha256').hexdigest()
    return cache[p]
checked=0
if '--historique' not in sys.argv:
    for item in entries.values():
        path=ROOT/item['nouveau']
        assert sha(path)==item['sha256_apres'],f"Contenu courant différent : {item['nouveau']}"
        if item.get('original_conserve'):
            assert sha(ROOT/item['original_conserve'])==item['sha256_avant']
        else:
            assert sha(path)==item['sha256_avant']
        checked+=1
historical=0
for group in ['recherche-Q1-20261114','investigations-B-E-20261114']:
    manifest=ROOT/'inventaire-DNEF/travaux-techniques'/group/'manifest-sha256.txt'
    for line in manifest.read_text().splitlines():
        expected,old=line.split('  ',1)
        item=entries[old]
        path=ROOT/item.get('original_conserve',item['nouveau'])
        assert sha(path)==expected,f"Entrée historique différente : {old}"
        historical+=1
print(json.dumps({'fichiers_deplaces_controles':checked,'entrees_manifestes_historiques_controlees':historical,'conforme':True},ensure_ascii=False))
