from pathlib import Path
import sys,json,re,unicodedata,collections,hashlib
O=Path(sys.argv[1]);R=O/'recherche';R.mkdir(exist_ok=False)
def norm(t):return ''.join(c for c in unicodedata.normalize('NFKD',t.lower()) if not unicodedata.combining(c))
patterns={'profession':r'\bavocat(?:e)?s?\b|\bbarreau\b|emailavocats|avocat-negrevergne|enkadenn-avocat', 'noms':r'\b(?:soyer|rochere|negrevergne|dress|rubio|pascoet|drie|benveniste|leproux|liwer|meyer|guillou|lalot|khallouki|fakiroff|legrand|wahrheit|wahreit|duffay|coriou)\b','conseil_defense':r'convention d.honoraires|secret professionnel|\bmaitre\b|\bcontentieux\b|\brecours\b','procedure_fiscale':r'proposition de rectification|juge des libertes|\bl[ .-]*16[ .-]*b\b|ordonnance.{0,60}(visite|saisie)|visite.{0,60}domiciliaire'}
rx={k:re.compile(v) for k,v in patterns.items()}
def hits(t):
 s=norm(t);return {k:[{'term':m[0],'context':re.sub(r'\s+',' ',s[max(0,m.start()-140):m.end()+220])} for m in list(r.finditer(s))[:8]] for k,r in rx.items() if r.search(s)}
extract={r['sha256']:r for r in map(json.loads,(O/'extraction.jsonl').open())};docs=[];idx={}
for h,e in sorted(extract.items()):
 t=(O/'extracted'/(h+'.txt')).read_text();hs=hits(t)
 if hs:
  d={'id':'D'+str(len(docs)+1).zfill(4),'sha256':h,'names':e['names'],'hits':hs,'extraction':e};docs.append(d);idx[h]=d['id']
ms=[]
for r in map(json.loads,(O/'messages.jsonl').open()):
 hh=hits('\n'.join(v for k,v in r['headers'].items() if k not in ('Date','Message-ID')));bh=hits(r['text']);ats=[idx[h] for h in r['attachments'] if h in idx]
 if hh or bh or ats:ms.append({'id':r['id'],'source':r['source'],'index':r['index'],'headers':r['headers'],'header_hits':hh,'body_hits':bh,'attachment_candidates':ats})
refs=[r for r in map(json.loads,(O/'references.jsonl').open()) if r['sha256'] in idx]
(R/'documents.json').write_text(json.dumps(docs,ensure_ascii=False,indent=2));(R/'messages.json').write_text(json.dumps(ms,ensure_ascii=False,indent=2));(R/'references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2))
summary={'documents_candidates':len(docs),'messages_candidates':len(ms),'strong_documents':sum('profession' in x['hits'] for x in docs),'strong_messages':sum('profession' in x['header_hits'] or 'profession' in x['body_hits'] for x in ms),'patterns':patterns,'extraction_status':dict(collections.Counter(x['status'] for x in extract.values())),'limits':dict(collections.Counter(v for x in extract.values() for v in x['limitations']))}
(R/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));print(json.dumps(summary,ensure_ascii=False))
