import pathlib,json,mailbox,re
out=pathlib.Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014');result=[]
for s in json.loads((out/'pst-summary.json').read_text()):
 for row in s['folders']:
  if not row['target_hits'] and 'synchronisation' not in row['path']:continue
  box=mailbox.mbox(out/row['path'],create=False)
  indexes=[h['index'] for h in row['target_hits']]
  if 'synchronisation' in row['path']:indexes=[1]
  for index in indexes:
   m=box[index-1];hits=[]
   for part in m.walk():
    if part.get_content_maintype()!='text':continue
    b=part.get_payload(decode=True)
    if not b:continue
    t=b.decode(part.get_content_charset() or 'utf-8',errors='replace')
    for match in re.finditer('l16b',t,re.I):hits.append(t[max(0,match.start()-90):match.end()+90])
    if 'synchronisation' in row['path']:hits.append(t[:12000])
   result.append({'path':row['path'],'index':index,'subject':str(m.get('Subject','')),'date':str(m.get('Date','')),'contexts':hits})
(out/'pst-contexts.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
for r in result:print(json.dumps(r,ensure_ascii=False))
