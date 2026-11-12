#!/usr/bin/env python3
"""Decrypt exact explicitly selected fileIDs into a new SIFT directory.

Usage SOURCE NEW_OUTPUT SELECTION_JSON. Password only via getpass.
"""
import contextlib
import getpass
import json
import os
from pathlib import Path
import re
import sys

from tp01_inventory import sha, dump


def main():
    source, out, selection = map(Path, sys.argv[1:4])
    os.umask(0o077)
    out.mkdir(parents=True, exist_ok=False)
    selected = json.loads(selection.read_text())
    if sum(x['Size'] for x in selected) > 32 * 1024**2:
        raise ValueError('Selection exceeds 32 MiB')
    from iphone_backup_decrypt import EncryptedBackup, utils
    password = getpass.getpass('Mot de passe TP-03 : ')
    backup = EncryptedBackup(backup_directory=str(source), passphrase=password)
    del password
    backup.test_decryption()
    results = []
    with backup.manifest_db_cursor() as cursor, (out / 'library.log').open('x') as log:
        for x in selected:
            fid, domain, rel = x['fileID'], x['domain'], x['relativePath']
            if not re.fullmatch('[0-9a-f]{40}', fid) or '/' in domain or '..' in Path(rel).parts or rel.startswith('/'):
                raise ValueError('Invalid path')
            found = cursor.execute('select domain,relativePath,file from Files where fileID=? and flags=1', (fid,)).fetchall()
            if len(found) != 1 or found[0][:2] != (domain, rel):
                raise ValueError('Manifest mismatch')
            src = source / fid[:2] / fid
            before = sha(src)
            dst = out / 'files' / domain / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            metadata = utils.FilePlist(found[0][2])
            key = backup.keybag.unwrap_key_for_class(metadata.protection_class, metadata.encryption_key)
            with contextlib.redirect_stdout(log):
                backup._decrypt_file_to_disk(file_id=fid, key=key, file_plist=metadata, output_filepath=str(dst))
            after = sha(src)
            if before != after:
                raise ValueError('Source changed')
            results.append(dict(x, ciphertext_sha256=before, ciphertext_after=after,
                                sha256=sha(dst), bytes=dst.stat().st_size))
    dump(out / 'collection.json', results)
    print(json.dumps({'copied': len(results), 'clear_bytes': sum(x['bytes'] for x in results)}))


if __name__ == '__main__':
    main()
