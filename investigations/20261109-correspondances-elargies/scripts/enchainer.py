import time,pathlib,subprocess,sys
root=pathlib.Path('/home/sansforensics/analysis/elargi-20261109-v2');scripts=pathlib.Path(__file__).resolve().parent
for _ in range(240):
 if (root/'sources.json').exists():break
 time.sleep(5)
else:raise SystemExit('collection_not_completed')
for name in ['extraire.py','rechercher.py']:
 subprocess.run([sys.executable,str(scripts/name),str(root)],check=True)
