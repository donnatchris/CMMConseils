#!/usr/bin/env python3
"""Extraction ciblée depuis le montage RO d'OP-01 ; aucun écrasement."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
from datetime import datetime, timezone
import zipfile

BASE = Path(__file__).resolve().parent
SOURCE = Path('/mnt/windows')
TARGETS = [
    ('L16B/MESSAGERIES/dmmconseils@hotmail.com.pst', 2143626240, 'cbc13b5a409585309db8edd7f9532fd69c58c1a48cf66355124a78f11950e8f9'),
    ('L16B/MESSAGERIES/dmmconseils93300@hotmail.com.pst', 1156260864, '06a98a15fe1c9b77a3c1eee0709fd1f5f9bd3f983d7342169e527e61a688d18a'),
    ('L16B/MESSAGERIES/rct93300@gmail.com/takeout-20241028T114105Z-001.zip', 41828775, 'bf97c84b9263faf1bff5f6b23af6e8b1facb125ecce764a5e95105fc885ea66c'),
]

def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(8 * 1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()

def main():
    mount = subprocess.check_output(['findmnt', '-J', '--mountpoint', str(SOURCE), '-o', 'SOURCE,TARGET,FSTYPE,OPTIONS'], text=True)
    filesystem = json.loads(mount)['filesystems'][0]
    assert 'ro' in filesystem['options'].split(','), 'Montage non RO : arrêt'
    assert filesystem['source'] == '/mnt/dislocker/dislocker-file', 'Source inattendue'
    loop = subprocess.check_output(['sudo', '-n', 'losetup', '-J'], text=True)
    loops = [d for d in json.loads(loop)['loopdevices'] if d.get('back-file') == '/mnt/ewf/ewf1']
    assert len(loops) == 1 and loops[0]['ro'] in (True, 1, '1'), 'Loop non RO ou ambigu'
    report = {
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'image': '/media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01 (ensemble segmenté E01–E74)',
        'mount': filesystem, 'loop': loops[0],
        'method': 'Lecture des fichiers alloués ; copie sans écrasement, SHA-256 du flux source et relecture SHA-256 de chaque copie ; comparaison aux empreintes antérieures.',
        'files': [],
    }
    for relative, expected_size, expected_hash in TARGETS:
        source, destination = SOURCE / relative, BASE / 'fichiers' / relative
        entry = {'source': str(source), 'relative_path': relative, 'destination_relative': str(destination.relative_to(BASE)), 'exists': source.is_file(), 'expected_sha256': expected_hash}
        report['files'].append(entry)
        assert source.is_file(), f'Fichier absent : {relative}'
        before = source.stat()
        assert before.st_size == expected_size, f'Taille inattendue : {relative}'
        print('Présent ; extraction : ' + relative, flush=True)
        destination.parent.mkdir(parents=True, exist_ok=True)
        h = hashlib.sha256()
        with source.open('rb') as src, destination.open('xb') as dst:
            for block in iter(lambda: src.read(8 * 1024 * 1024), b''):
                h.update(block)
                dst.write(block)
            dst.flush()
            os.fsync(dst.fileno())
        shutil.copystat(source, destination)
        after = source.stat()
        entry.update(size=before.st_size, inode=before.st_ino, source_mtime_ns=before.st_mtime_ns,
                     source_sha256=h.hexdigest(), exported_sha256=digest(destination),
                     source_stat_unchanged=(before.st_size, before.st_mtime_ns, before.st_ino) == (after.st_size, after.st_mtime_ns, after.st_ino))
        entry['hashes_match'] = entry['source_sha256'] == entry['exported_sha256'] == expected_hash
        assert entry['hashes_match'] and entry['source_stat_unchanged'], f'Contrôle échoué : {relative}'
        if destination.suffix == '.pst':
            with destination.open('rb') as f:
                entry['header_hex'] = f.read(4).hex()
            assert entry['header_hex'] == '2142444e', 'Signature PST inattendue'
        else:
            entry['members'] = []
            with zipfile.ZipFile(destination) as archive:
                for info in archive.infolist():
                    mh = hashlib.sha256()
                    with archive.open(info) as member:
                        for block in iter(lambda: member.read(1024 * 1024), b''):
                            mh.update(block)
                    entry['members'].append({'name': info.filename, 'size': info.file_size, 'crc32': f'{info.CRC:08x}', 'sha256': mh.hexdigest(), 'decompression_crc_ok': True})
        print('Copie vérifiée ; SHA-256 identique au contrôle antérieur : ' + destination.name, flush=True)
    report['finished_utc'] = datetime.now(timezone.utc).isoformat()
    report['status'] = 'Trois fichiers présents, alloués et extraits ; toutes les empreintes concordent.'
    report['deleted_file_search'] = 'Non nécessaire pour récupérer ces trois fichiers : tous sont présents dans le système de fichiers monté. Aucune recherche exhaustive des versions supprimées effectuée.'
    with (BASE / 'verification-extraction.json').open('x') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write('\n')
    with (BASE / 'SHA256SUMS').open('x') as f:
        for entry in report['files']:
            f.write(entry['exported_sha256'] + '  ' + entry['destination_relative'] + '\n')
    print(report['status'], flush=True)

if __name__ == '__main__':
    main()
