"""Montage avec script existant RO, saisie masquée, aucun secret journalisé."""
import re
from pathlib import Path
import pexpect

project = Path(__file__).resolve().parents[4]
keys = re.findall(r'\b\d{6}(?:-\d{6}){7}\b', (project / 'docs/codes-d-acces.md').read_text())
assert len(keys) == 1, 'Clé unique attendue ; aucune clé affichée'
cmd = 'sudo -n bash /media/shared/codeProjects/DMMConseils/ordinateur/scripts/remonter_op01.sh'
child = pexpect.spawn('ssh', ['-F', '/home/chris/.ssh/config', '-tt', 'sift', cmd], encoding='utf-8', timeout=50)
parts = []
sent = False
try:
    while True:
        i = child.expect([r'(?i)enter[^\r\n]*(?:password|key)[^\r\n]*:', pexpect.EOF, pexpect.TIMEOUT])
        parts.append(child.before)
        if i == 0:
            assert not sent, 'Second prompt inattendu'
            child.waitnoecho(timeout=5)
            child.sendline(keys[0])
            sent = True
        elif i == 1:
            break
        else:
            raise RuntimeError('Délai de montage dépassé')
finally:
    log = '\n'.join(line for part in parts for line in part.replace('\r', '\n').splitlines()
                    if line.startswith(('[1/4]', '[2/4]', '[3/4]', '[4/4]', 'Montage terminé', 'OK :', 'Accès :', 'Source : /dev/')))
    dest = project / 'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/montage-sift.txt'
    with dest.open('x') as f:
        f.write(log + '\n')
    print(log)
    child.close()
