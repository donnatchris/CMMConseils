import pathlib,subprocess,json,hashlib,re
B=pathlib.Path(__file__).resolve().parents[1];out=B/'resultats';pdfs={'test_bureau':B/'preuves/mft-181043-test.pdf','sage':B/'preuves/L16B/SAGE/sage.pdf','test':B/'preuves/$Recycle.Bin/S-1-5-21-1394434332-468722268-2897565647-1001/$R2RYNYS.pdf'};results={};pages={}
for name,p in pdfs.items():
 info=subprocess.check_output(['pdfinfo',str(p)],text=True);text=subprocess.check_output(['pdftotext','-layout',str(p),'-'],text=True);ls=text.split('\f')
 if ls and not ls[-1].strip():ls.pop()
 pages[name]=ls;rows=[]
 for i,t in enumerate(ls,1):
  ids=sorted(set(re.findall(r'\b(?:FA|DE|BC|BL|AV)\d{3,6}\b',t)))
  rows.append({'page':i,'text_sha256':hashlib.sha256(t.encode()).hexdigest(),'contains_ALMU':bool(re.search(r'\bALMU\b',t,re.I)),'piece_ids':ids,'text':t})
 results[name]={'path':str(p.relative_to(B)),'size':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'pdfinfo':info,'pages':len(ls),'pages_ALMU':sum(r['contains_ALMU'] for r in rows),'page_rows':rows}
(out/'pdf-content.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
normal=lambda s:re.sub(r'\s+','',s)
matches=[]
for name in ['test','test_bureau']:
 for i,t in enumerate(pages[name],1):
  matches.append({'source':name,'test_page':i,'exact_text_after_whitespace_removal':[j for j,u in enumerate(pages['sage'],1) if normal(t)==normal(u)]})
(out/'pdf-page-comparison.json').write_text(json.dumps(matches,indent=2));print({n:{k:v for k,v in r.items() if k!='page_rows'} for n,r in results.items()});print(matches)
