from pathlib import Path
import json,subprocess,re,unicodedata,sys
p=Path(sys.argv[1]);out=p/'native-prioritaire';out.mkdir(exist_ok=False);hits=[]
for x in json.loads((p/'blobs-expanded.json').read_text()):
 q=p/'blobs'/x['sha256']
 with q.open('rb') as f:sig=f.read(5)
 if sig!=b'%PDF-':continue
 try:r=subprocess.run(['pdftotext','-layout',str(q),'-'],capture_output=True,timeout=30)
 except subprocess.TimeoutExpired:continue
 if r.returncode:continue
 t=r.stdout.decode(errors='replace');s=''.join(c for c in unicodedata.normalize('NFKD',t.lower()) if not unicodedata.combining(c))
 ms=list(re.finditer(r'\bavocats?\b|\bbarreau\b|proposition de rectification|juge des libertes|\bl[ .-]*16[ .-]*b\b',s))
 if ms:
  (out/(x['sha256']+'.txt')).write_text(t);hits.append({'sha256':x['sha256'],'names':x['names'],'contexts':[re.sub(r'\s+',' ',s[max(0,m.start()-100):m.end()+200]) for m in ms[:4]]})
(out/'hits.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2));print('native_candidates',len(hits),flush=True)
