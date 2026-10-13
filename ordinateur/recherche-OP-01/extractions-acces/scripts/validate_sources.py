import pathlib,json,hashlib
root=pathlib.Path(__file__).resolve().parents[1];checks=[]
for manifest,prefix in [('sources.json','raw'),('additional/sources.json','additional/raw'),('followup-sources.json','raw')]:
 for r in json.loads((root/manifest).read_text()):
  p=root/prefix/r['source']
  if p.exists():
   actual=hashlib.sha256(p.read_bytes()).hexdigest();checks.append({'manifest':manifest,'source':r['source'],'equal':actual==r['sha256'],'sha256':actual});assert checks[-1]['equal'],str(p)
  else:checks.append({'manifest':manifest,'source':r['source'],'raw_not_copied':True})
(root/'source-verification.json').write_text(json.dumps(checks,indent=2));print('verified',sum(r.get('equal',False) for r in checks),'source hashes without raw copy',sum(r.get('raw_not_copied',False) for r in checks))
