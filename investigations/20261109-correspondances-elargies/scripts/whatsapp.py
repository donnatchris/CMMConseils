from pathlib import Path
import zipfile,json,hashlib,re,unicodedata
O=Path('/home/sansforensics/analysis/elargi-20261109-final/whatsapp');O.mkdir(exist_ok=False);r=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rx=re.compile(r'\bavocats?\b|\bbarreau\b|\bmaitre\b|\b(?:soyer|rochere|negrevergne|dress|rubio|pascoet|drie|benveniste|leproux|liwer|meyer|guillou|lalot|khallouki|fakiroff|wahrheit|duffay|coriou)\b')
for p in sorted(Path('/mnt/windows/L16B/TELEPHONES').rglob('*.zip')):
 before=sha(p)
 with zipfile.ZipFile(p) as z:
  for n in z.namelist():
   if not n.lower().endswith('.txt'):continue
   d=z.read(n);h=hashlib.sha256(d).hexdigest();t=d.decode('utf8',errors='replace');s=''.join(c for c in unicodedata.normalize('NFKD',t.lower()) if not unicodedata.combining(c));ms=list(rx.finditer(s));(O/(h+'.txt')).write_text(t)
   r.append({'source':str(p),'member':n,'sha256':h,'matches':[{'term':m[0],'context':s[max(0,m.start()-100):m.end()+180]} for m in ms],'archive_sha256_before':before,'archive_sha256_after':sha(p)})
(O/'results.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(json.dumps({'texts':len(r),'texts_with_hits':sum(bool(x['matches']) for x in r),'sources_unchanged':all(x['archive_sha256_before']==x['archive_sha256_after'] for x in r)}))
