"""Essai unique du code TP-03 conservé au dossier, sans journaliser ce code."""
from pathlib import Path
import json
import pexpect
P=Path(__file__).resolve().parents[4]
part=(P/'docs/codes-d-acces.md').read_text().split('## Téléphone portable TP-03',1)[1].split('\n## ',1)[0].strip()
assert len(part.splitlines())==1
command=('PYTHONPATH=/home/sansforensics/analysis/tp03-dependencies-20261110 python3 '
 '/media/shared/codeProjects/DMMConseils/telephones/scripts/tp03_collect_selected.py '
 '/media/shared/forensic/SADEDINE-2026/TP-03/00008110-001249321444801E '
 '/media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/complement-natif '
 '/media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/selection-complement.json')
c=pexpect.spawn('ssh',['-F','/home/chris/.ssh/config','-tt','sift',command],encoding='utf-8',timeout=50)
i=c.expect(['Mot de passe TP-03 :',pexpect.EOF,pexpect.TIMEOUT])
if i==0:
    c.sendline(part)
    c.expect(pexpect.EOF,timeout=50)
    output=c.before
else:output='initialization_without_expected_prompt'
c.close()
safe=[line for line in output.splitlines() if line.startswith('{"copied":')]
status={'completed':bool(safe),'exit_status':c.exitstatus,'credential_source':'existing TP-03 section','credential_recorded':False,'attempts':1}
dest=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive/complement-dechiffrement-status.json'
with dest.open('x') as f:json.dump(status,f,indent=2)
print(json.dumps(status))
for line in safe:print(line)
