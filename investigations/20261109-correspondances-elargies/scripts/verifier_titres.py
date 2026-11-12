from pathlib import Path
import json,subprocess,tempfile,os
O=Path('/home/sansforensics/analysis/elargi-20261109-v2');out=O/'titres-prioritaires';out.mkdir(exist_ok=False)
for x in json.loads((O/'blobs-expanded.json').read_text()):
 if not x['sha256'].startswith(('df165f','cadbeb','735e02')):continue
 h=x['sha256'];q=out/h
 subprocess.run(['pdftoppm','-f','1','-l','1','-singlefile','-scale-to','1800','-png',str(O/'blobs'/h),str(q)],check=True,capture_output=True)
 r=subprocess.run(['tesseract',str(q)+'.png','stdout','-l','fra+eng'],env=dict(os.environ,OMP_THREAD_LIMIT='1'),capture_output=True,check=True)
 (out/(h+'.txt')).write_bytes(r.stdout)
print('titles_checked')
