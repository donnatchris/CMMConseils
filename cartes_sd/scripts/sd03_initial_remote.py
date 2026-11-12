"""Identification SD-03 ; crée uniquement une vue EWF en lecture seule."""
import glob,os,subprocess,sys
source='/media/shared/forensic/SADEDINE-2026/ANALYSES/SD-03/SD03.E01';image='/mnt/ewf-sd03/ewf1'
if not os.path.isfile(source):raise FileNotFoundError(source)
if not os.path.exists(image):
 subprocess.run(['mkdir','-p','/mnt/ewf-sd03'],check=True)
 subprocess.run(['ewfmount',source,'/mnt/ewf-sd03'],check=True)
for args in [['date','-u'],['cat','/media/shared/AGENTS.md'],['stat',image],['ewfinfo',source],['mmls',image],['ewfverify','-h']]:
 print('\nCommande : '+repr(args),flush=True);p=subprocess.run(args);print('Code retour : '+str(p.returncode),flush=True)
print('Segments :',flush=True)
for path in sorted(glob.glob(source[:-2]+'[0-9][0-9]')):
 s=os.stat(path);print(path,s.st_size,s.st_mtime_ns,flush=True)
