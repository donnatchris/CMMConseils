import pexpect,re,pathlib,os,shlex
projet=pathlib.Path(__file__).resolve().parents[3]
s=(projet/'docs/codes-d-acces.md').read_text();key=re.search(r'\b\d{6}(?:-\d{6}){7}\b',s).group()
projet_distant=os.environ.get('DMMCONSEILS_PROJET_DISTANT',str(pathlib.PurePosixPath('/media/shared/codeProjects')/projet.name))
commande='sudo -n bash '+shlex.quote(str(pathlib.PurePosixPath(projet_distant)/'ordinateur/scripts/remonter_op01.sh'))
p=pexpect.spawn('ssh',['-tt','-F','/home/chris/.ssh/config','sift',commande],encoding='utf-8',timeout=120)
p.expect(['recovery password', 'recovery key', 'Déjà monté',pexpect.EOF],timeout=120)
if p.isalive():
 if 'Déjà monté' not in p.after:p.sendline(key)
 p.expect(pexpect.EOF,timeout=120)
p.close();print('mount_exit',p.exitstatus)
