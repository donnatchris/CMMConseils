import pexpect,re,pathlib
s=pathlib.Path('docs/codes-d-acces.md').read_text();key=re.search(r'\b\d{6}(?:-\d{6}){7}\b',s).group()
p=pexpect.spawn('ssh',['-tt','-F','/home/chris/.ssh/config','sift','sudo -n bash /media/shared/codeProjects/CMMConseils/ordinateur/scripts/remonter_op01.sh'],encoding='utf-8',timeout=120)
p.expect(['recovery password', 'recovery key', 'Déjà monté',pexpect.EOF],timeout=120)
if p.isalive():
 if 'Déjà monté' not in p.after:p.sendline(key)
 p.expect(pexpect.EOF,timeout=120)
p.close();print('mount_exit',p.exitstatus)
