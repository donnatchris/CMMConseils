"""Remonte OP-01 RO avec saisie masquée, sans conserver de secret."""
from pathlib import Path
import json
import re
import pexpect
P=Path(__file__).resolve().parents[4]
keys=re.findall(r'\b\d{6}(?:-\d{6}){7}\b',(P/'docs/codes-d-acces.md').read_text())
assert len(keys)==1
c=pexpect.spawn('ssh',['-F','/home/chris/.ssh/config','-tt','sift','sudo -n bash /media/shared/codeProjects/DMMConseils/ordinateur/scripts/remonter_op01.sh'],encoding='utf-8',timeout=50)
i=c.expect([r'(?i)enter[^\r\n]*password[^\r\n]*:',pexpect.EOF,pexpect.TIMEOUT])
if i==0:c.sendline(keys[0]);c.expect(pexpect.EOF,timeout=50)
c.close()
result={'ssh_exit_status':c.exitstatus,'secret_recorded':False,'method':'existing remonter_op01.sh, EWF and loop RO, dislocker -r, NTFS ro,norecover'}
out=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/montage.json'
with out.open('x') as f:json.dump(result,f,indent=2)
print(json.dumps(result))
