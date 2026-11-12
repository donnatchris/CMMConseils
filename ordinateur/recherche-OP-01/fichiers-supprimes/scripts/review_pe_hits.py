import pathlib,json,re,pefile
root=pathlib.Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013');static=json.loads((root/'static-checks.json').read_text());out=[]
for row in static['results']:
 if not row.get('target_terms'):continue
 p=root/'recovered'/(str(row['mft_index'])+'.bin');b=p.read_bytes();item={'mft_index':row['mft_index'],'terms':row['target_terms'],'identifiers':[],'version_strings':{}}
 for term in row['target_terms']:
  for enc in ['ascii','utf-16le']:
   needle=term.encode(enc);pos=b.lower().find(needle)
   while pos>=0:
    start=max(0,pos-80);end=min(len(b),pos+len(needle)+80)
    if enc=='utf-16le' and (pos-start)%2:start+=1
    text=b[start:end].decode(enc,'replace');words=re.findall(r'[A-Za-z_.$0-9]*'+re.escape(term)+r'[A-Za-z_.$0-9]*',text,re.I);item['identifiers']+=words;pos=b.lower().find(needle,pos+len(needle))
 try:
  pe=pefile.PE(str(p));
  for group in getattr(pe,'FileInfo',[]):
   for node in group:
    for table in getattr(node,'StringTable',[]):
     for k,v in table.entries.items():
      key=k.decode('utf-8','replace')
      if key in ['CompanyName','FileDescription','FileVersion','InternalName','OriginalFilename','ProductName']:item['version_strings'][key]=v.decode('utf-8','replace')
  pe.close()
 except Exception as ex:item['error']=str(ex)
 out.append(item)
(root/'pe-hit-review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(out,flush=True)
