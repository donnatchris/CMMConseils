from pathlib import Path
import json,csv,unicodedata,re
B=Path('investigations/20261108-complement-pv')
t=[x for x in json.loads(Path('ordinateur/recherche-OP-01/extractions-acces/l16b-inventory.json').read_text()) if 'mini' in x['path'].lower() and x['path'].lower().endswith('.pdf')]
p=json.loads((B/'prive/manifest-pdfs.json').read_text())
def norm(s):return re.sub(r'[^a-z0-9]','',unicodedata.normalize('NFKD',Path(s).stem).encode('ascii','ignore').decode().lower())
sel=[];matches=[]
for r in p:
 m=[{'target':v['path'],'same_size':r['size']==v['size'],'same_normalized_name':norm(r['relativePath'])==norm(v['path'])} for v in t if r['size']==v['size'] or norm(r['relativePath'])==norm(v['path'])]
 if m:sel.append(r);matches.append({'fileID':r['fileID'],'candidates':m})
with (B/'prive/pdf-selection.csv').open('x') as f:
 w=csv.DictWriter(f,fieldnames=['domain','relativePath','fileID','flags','priority','size']);w.writeheader()
 for r in sel:w.writerow({k:(1 if k in ('flags','priority') else r[k]) for k in w.fieldnames})
(B/'prive/pdf-selection-matches.json').write_text(json.dumps(matches,ensure_ascii=False,indent=2))
print({'selected':len(sel),'bytes':sum(r['size'] for r in sel),'targets':len(t)})
