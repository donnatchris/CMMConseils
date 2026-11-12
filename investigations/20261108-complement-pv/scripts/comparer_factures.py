from pathlib import Path
import subprocess,re,json,hashlib
B=Path('investigations/20261108-complement-pv');test=Path('ordinateur/recherche-OP-01/fichiers-supprimes/recovered/166334.bin');sage=B/'prive/sift-recupere/prive/sage.txt'
t=subprocess.run(['pdftotext','-layout',str(test),'-'],capture_output=True,check=True).stdout.decode();s=sage.read_text();tp=[p for p in t.split('\f') if p.strip()];sp=[p for p in s.split('\f') if p.strip()]
def norm(t):return re.sub(r'\s+','',t)
r=[]
for i,p in enumerate(tp,1):
 ids=re.findall(r'\bFA\d+\b',p)
 r.append({'test_page':i,'invoice_ids':ids,'identical_normalized_text_pages':[j for j,q in enumerate(sp,1) if norm(p)==norm(q)],'same_invoice_id_pages':[j for j,q in enumerate(sp,1) if any(v in q for v in ids)]})
out={'method':'pdftotext -layout; all whitespace removed; case and punctuation preserved','test_sha256':hashlib.sha256(test.read_bytes()).hexdigest(),'sage_text_sha256':hashlib.sha256(sage.read_bytes()).hexdigest(),'test_pages':len(tp),'sage_text_pages':len(sp),'results':r}
(B/'resultats/comparaison-factures.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
