"""Relire les résultats existants et calculer les compléments factuels de la note.

Aucune acquisition ni modification de preuve : lectures de dérivés locaux et
soustractions de dates. Les identifiants et les empreintes des sources sont joints.
"""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo
import hashlib
import json
import struct

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'inventaire-DNEF/travaux-techniques/complements-note-20261119/complements.json'
PARIS = ZoneInfo('Europe/Paris')
SOURCES = {
    'comparaison': 'ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/resultats-comparaison-L16B-inventaire.json',
    'mft': 'ordinateur/recherche-OP-01/extractions-acces/l16b-mft.jsonl',
    'objets': 'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/attributs-et-chronologie.json',
    'verification': 'inventaire-DNEF/documents-recus/verification-20241015-1325-1351/resultats-sift-v2.json',
    'fichiers': 'inventaire-DNEF/documents-recus/verification-20241015-1325-1351/complement-fichiers-sift.json',
    'preferences': 'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/telephones-passe2/resultats.json',
    'reseau': 'ordinateur/recherche-OP-01/sage-reseaux-20261113/resultats/chronologie-reseau-28oct.json',
    'samsung': 'ordinateur/recherche-OP-01/samsung-almu-20261113/resultats/samsung-events.json',
    'csv': 'inventaire-DNEF/documents-recus/Inventaire_saddedine.csv',
}


def read(name):
    return json.loads((ROOT / SOURCES[name]).read_text())


def epoch(value):
    """Secondes Unix en décimal, sans conversion des fractions par un float."""
    value = value.split('[')[0]
    date = datetime.fromisoformat(value)
    seconds = int(date.replace(microsecond=0).timestamp())
    fraction = value.split('T')[1][8:]
    digits = fraction[1:].split('+')[0].split('-')[0].rstrip('Z') if fraction.startswith('.') else '0'
    return Decimal(seconds) + Decimal('0.' + digits)


def modification_si(record):
    """FILETIME de modification de l'attribut résident $STANDARD_INFORMATION."""
    raw = bytes.fromhex(record['raw_record_hex'])
    pos = struct.unpack_from('<H', raw, 20)[0]
    while pos < len(raw) - 24:
        kind, length = struct.unpack_from('<II', raw, pos)
        if kind == 0xffffffff or length == 0:
            break
        if kind == 0x10:
            assert raw[pos + 8] == 0, 'Attribut SI non résident inattendu'
            value_offset = struct.unpack_from('<H', raw, pos + 20)[0]
            ticks = struct.unpack_from('<Q', raw, pos + value_offset + 8)[0]
            seconds, fraction = divmod(ticks - 116444736000000000, 10000000)
            date = datetime.fromtimestamp(seconds, timezone.utc).astimezone(PARIS)
            return date.strftime('%Y-%m-%dT%H:%M:%S') + f'.{fraction:07d}' + date.strftime('%z')[:3] + ':' + date.strftime('%z')[3:]
        pos += length
    raise ValueError('Attribut SI absent')


def calculate():
    comparison, objects, check = read('comparaison'), read('objets'), read('verification')
    assert comparison['inventory_sha256'] == objects['inventory_sha256']
    inventory_sha = hashlib.sha256((ROOT / SOURCES['csv']).read_bytes()).hexdigest()
    assert inventory_sha == 'f2a4e9d05cca5c7b8082da42df76fca45e870f3e3acbbdf6ff03c07e68293c40'
    divergent = {x['inode']: x for x in comparison['different_contents']}
    added = {x['inode']: x for x in comparison['current_only']}
    files = []
    with (ROOT / SOURCES['mft']).open() as stream:
        for line in stream:
            item = json.loads(line)
            index = item['mft_index']
            if index not in divergent and index not in added:
                continue
            reference = divergent.get(index) or added[index]
            files.append({'path': reference['path'], 'mft_index': index,
                          'statut': 'empreinte divergente' if index in divergent else 'absent du CSV',
                          'modification_si_paris': modification_si(item),
                          'modification_csv': reference.get('modification_inventory'),
                          'ligne_csv': reference.get('csv_line')})
    assert len(files) == 6
    inventory = {x['line']: x for x in objects['inventory']}
    direct = {x['fileID']: x for x in check['phones']['TP-03']['pdf_objects']}
    selected = []
    for item in objects['phones']['TP-03']:
        last = item.get('lastused')
        if not last or not last['paris'].startswith('2024-10-15'):
            continue
        assert direct[item['fileID']]['lastused_in_window']
        assert direct[item['fileID']]['LastStatusChange'] == item['mbfile']['LastStatusChange']
        last_epoch = Decimal(last['seconds']) + Decimal(last['nanoseconds']) / Decimal(1000000000)
        last_text = last['paris'][:19] + f'.{last["nanoseconds"]:09d}' + '+02:00'
        assert last_text == direct[item['fileID']]['lastused_paris']
        matches = []
        for number in item['dnef_lines']:
            row = inventory[number]
            assert row['sha512'] == item['sha512']
            delta = epoch(row['creation']) - last_epoch
            matches.append({'ligne': number, 'path': row['path'], 'creation': row['creation'],
                            'ecart_creation_moins_derniere_utilisation_secondes': str(delta)})
        selected.append({'content_id': item['content_id'], 'fileID': item['fileID'],
                         'relativePath': item['relativePath'], 'sha512': item['sha512'],
                         'lastused_paris': last_text, 'LastStatusChange': item['mbfile']['LastStatusChange'],
                         'LastStatusChange_paris': item['status_change_paris'], 'inventaire': matches})
    selected.sort(key=lambda x: x['lastused_paris'])
    assert len(selected) == 17 and len({x['sha512'] for x in selected}) == 17
    network, samsung = read('reseau'), read('samsung')
    driver = next(x for x in samsung if x['record'] == 897 and 'Kernel-PnP' in x['source'])
    connected = next(x for x in network if x['record'] == 7020)
    removed = next(x for x in samsung if x['record'] == 1493 and x['id'] == 1010)
    disconnected = next(x for x in network if x['record'] == 7045)
    intervals = []
    for label, start, end in [('configuration_RNDIS_vers_etat_connecte', driver, connected),
                              ('retrait_Samsung_vers_deconnexion_Reseau3', removed, disconnected)]:
        intervals.append({'objet': label, 'debut': start['paris'], 'fin': end['paris'],
                          'record_debut': start['record'], 'record_fin': end['record'],
                          'ecart_secondes': str(epoch(end['paris']) - epoch(start['paris']))})
    preferences = read('preferences')['TP-03']['preferences']
    dated_preferences = []
    for filename, values in preferences.items():
        if not isinstance(values, dict):
            continue
        for key, value in values.items():
            if isinstance(value, str) and value.startswith('2024-10-15T11:'):
                date = datetime.fromisoformat(value).replace(tzinfo=timezone.utc).astimezone(PARIS)
                if '13:25:00' <= date.strftime('%H:%M:%S') <= '13:51:00':
                    dated_preferences.append({'fichier': filename, 'champ': key,
                                               'date_paris': date.isoformat()})
    return {'date_relecture': '2026-11-19',
            'script': {'path': str(Path(__file__).relative_to(ROOT)), 'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
            'methode': 'Relecture de résultats existants ; conversions de champs datés et soustractions. Aucune nouvelle acquisition.',
            'sources': {k: {'path': path, 'sha256': hashlib.sha256((ROOT / path).read_bytes()).hexdigest()} for k, path in SOURCES.items()},
            'csv_sha256': inventory_sha, 'fichiers_constat1': files,
            'intervalles_constat6': intervals, 'objets_constat10': selected,
            'evenements_tcc_constat15': check['phones']['TP-03']['tcc'],
            'preferences_constat15': dated_preferences}


if __name__ == '__main__':
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(calculate(), ensure_ascii=False, indent=2) + '\n')
    print(OUTPUT)
