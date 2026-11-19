"""Saisie unique du secret via PTY, sortie filtrée et journal neuf."""
from pathlib import Path
import re
import pexpect
project=Path(__file__).resolve().parents[4]
keys=re.findall(r'\b\d{6}(?:-\d{6}){7}\b',(project/'docs/codes-d-acces.md').read_text())
assert len(keys)==1
child=pexpect.spawn('ssh',['-F','/home/chris/.ssh/config','-tt','sift','sudo -n bash /media/shared/codeProjects/DMMConseils/ordinateur/scripts/remonter_op01.sh'],encoding='utf-8',timeout=45)
parts=[];sent=False
while True:
    i=child.expect([r'(?i)enter[^\r\n]*(?:password|key)[^\r\n]*:',pexpect.EOF,pexpect.TIMEOUT])
    parts.append(child.before)
    if i==0:
        if sent:
            parts.append('[second prompt observed; no second secret sent]')
            child.sendline('')
            child.expect(pexpect.EOF,timeout=10)
            parts.append(child.before)
            break
        child.sendline(keys[0]);sent=True
    elif i==1:break
    else:
        parts.append('[timeout]');break
child.close()
joined='\n'.join(parts).replace(keys[0],'[REDACTED]')
joined=re.sub(r'\b\d{6}(?:-\d{6}){7}\b','[REDACTED]',joined)
filtered='\n'.join(x for x in joined.replace('\r','\n').splitlines()
                   if not re.search(r'\d{6}|recovery password|^\s*\d+\s*$|second prompt',x,re.I))
with (project/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/montage-sift-v2.txt').open('x') as f:f.write(filtered+'\n')
print(filtered)
