#!/usr/bin/env python3
"""Exécute le script existant de montage RO ; clé lue localement, jamais journalisée."""
import re,subprocess
from pathlib import Path
import pexpect
R=Path(__file__).resolve().parents[3]
ssh=['ssh','-F','/home/chris/.ssh/config','sift']
remote='/home/sansforensics/analysis/complement-20261017'
subprocess.run(ssh+['umask 077; mkdir -p '+remote+'; test ! -e '+remote+'/remonter.sh && cat > '+remote+'/remonter.sh'],input=(R/'ordinateur/scripts/remonter_op01.sh').read_bytes(),check=True)
keys=re.findall(r'\b\d{6}(?:-\d{6}){7}\b',(R/'docs/codes-d-acces.md').read_text())
if len(keys)!=1:raise SystemExit('Clé de récupération unique non trouvée ; aucune clé affichée.')
child=pexpect.spawn('ssh',['-F','/home/chris/.ssh/config','-tt','sift','sudo -n bash '+remote+'/remonter.sh'],encoding='utf-8',timeout=90)
parts=[];sent=False
try:
 while True:
  i=child.expect([r'(?i)enter[^\r\n]*(?:password|key)[^\r\n]*:',pexpect.EOF,pexpect.TIMEOUT])
  parts.append(child.before)
  if i==0:
   if sent:child.expect(pexpect.EOF);parts.append(child.before);break
   sent=True;child.sendline(keys[0])
  elif i==1:break
  else:child.close();raise RuntimeError('Montage sans réponse dans le délai')
finally:
 text='\n'.join(line for part in parts for line in part.replace('\r','\n').splitlines() if line.startswith(('[1/4]','[2/4]','[3/4]','[4/4]','Montage terminé','OK : System.evtx','Accès :','Source : /dev/')))
 dest=R/'investigations/20261017-recroisements/resultats/montage-sift.txt'
 if dest.exists():raise RuntimeError('Journal déjà présent')
 dest.write_text(text);dest.chmod(0o600)
 print(text)
child.close()
if child.exitstatus not in [0,None]:raise SystemExit(child.exitstatus)
