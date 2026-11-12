from pathlib import Path
import json,re,unicodedata,sys
p=Path('/home/sansforensics/analysis/elargi-20261109-final');out=[]
for l in [l for n in ['extraction-initiale.jsonl','extraction-reprise.jsonl'] for l in (p/n).open()]:
 r=json.loads(l);t=(p/'extracted'/(r['sha256']+'.txt')).read_text();s=''.join(c for c in unicodedata.normalize('NFKD',t.lower()) if not unicodedata.combining(c))
 matches=list(re.finditer(r'\bavocats?\b|\bbarreau\b|proposition de rectification|juge des libertes|\bl[ .-]*16[ .-]*b\b',s))
 if matches:out.append({'sha256':r['sha256'],'names':r['names'],'methods':r['method'],'contexts':[re.sub(r'\s+',' ',s[max(0,m.start()-100):m.end()+200]) for m in matches[:4]]})
print(json.dumps(out,ensure_ascii=False))
