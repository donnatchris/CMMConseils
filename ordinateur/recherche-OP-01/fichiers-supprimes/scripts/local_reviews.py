import pathlib,json,zipfile,xml.etree.ElementTree as E,re,collections,sqlite3
root=pathlib.Path(__file__).resolve().parents[1]
# No credential values are written to this structural summary.
with zipfile.ZipFile(root/'recovered/77995.bin') as z:t=E.fromstring(z.read('word/document.xml'))
summary=[];labels=['mot de passe','mots de passe','identifiant','adresse','site','nom','utilisateur','mdp']
for ti,table in enumerate(t.findall('.//{*}tbl')):
 rows=[]
 for ri,row in enumerate(table.findall('./{*}tr')):
  cells=[''.join(n.text or '' for n in c.findall('.//{*}t')) for c in row.findall('./{*}tc')];rows.append({'row':ri,'nonempty_cells':sum(bool(c.strip()) for c in cells),'cell_lengths':[len(c) for c in cells],'recognized_labels':sorted(set(k for k in labels if any(k in c.lower() for c in cells)))})
 summary.append({'table':ti,'rows':rows})
(root/'credential-document-structure-redacted.json').write_text(json.dumps(summary,indent=2))
result=[]
for idx in [276584,356721,356724,356722,276662]:
 b=(root/'recovered'/f'{idx}.bin').read_bytes();r={'mft_index':idx,'prefix_hex':b[:32].hex()}
 try:t=E.fromstring(b);r['xml_root']=t.tag;r['tags']=collections.Counter(n.tag for n in t.iter())
 except Exception as ex:r['xml_parse_error']=str(ex)
 result.append(r)
(root/'ciel-structure.json').write_text(json.dumps(result,indent=2))
b=(root/'recovered/760041.bin').read_bytes();pos=b.find(b'/OpenAction');m=re.search(rb'/OpenAction\s+(\d+)\s+\d+\s+R',b);obj=re.search(rb'\b'+m[1]+rb'\s+\d+\s+obj\s*(.*?)endobj',b,re.S) if m else None
(root/'pdf-openaction-review.json').write_text(json.dumps({'mft_index':760041,'allocation_warning':True,'openaction_reference':m[1].decode() if m else None,'nearby_name_tokens':[x.decode() for x in re.findall(rb'/[A-Za-z]+',b[pos:pos+180])],'referenced_object_name_tokens':[x.decode() for x in re.findall(rb'/[A-Za-z]+',obj[1])] if obj else [],'direct_XYZ_destination':bool(re.search(rb'/OpenAction\s*\[[^\]]*/XYZ',b))},indent=2))
c=sqlite3.connect('file:'+str(root/'recovered/439945.bin')+'?mode=ro&immutable=1',uri=True);domains=collections.Counter()
for (v,) in c.execute('select value from Config'):
 if isinstance(v,bytes):v=v.decode('utf-8','ignore')
 if isinstance(v,str):domains.update(re.findall(r'https?://([a-zA-Z0-9.-]+)',v))
r={'mft_index':439945,'schema':c.execute('select sql from sqlite_master').fetchall(),'records':c.execute('select count(*) from Config').fetchone()[0],'url_domains':domains};c.close();(root/'sqlite-configuration-summary.json').write_text(json.dumps(r,indent=2))
print('Local reviews complete; no credential values displayed.')
