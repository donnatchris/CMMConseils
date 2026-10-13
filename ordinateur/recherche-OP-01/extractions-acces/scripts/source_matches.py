import pathlib,json,hashlib,datetime
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/home/sansforensics/analysis/OP-01/extractions-acces-20261013');inv=json.loads((out/'l16b-inventory.json').read_text());candidates=[r for r in inv if r['path'].startswith('L16B/LOCAL/') and 0<r['size']<=4*1024*1024 and pathlib.Path(r['path']).suffix.lower() in ['.pdf','.docx','.xlsx','.doc','.xls']];chosen=[candidates[i] for i in range(0,len(candidates),max(1,len(candidates)//40))][:40];rows=[]
for r in chosen:
 rel=pathlib.Path(r['path']).relative_to('L16B/LOCAL');roots=[base/'Users/fintm/Desktop',base/'Users/fintm/Documents',base/'Users/fintm/Downloads'];paths=[p/rel for p in roots]
 if rel.parts[0]=='Téléchargement':paths.append(base/'Users/fintm/Downloads'/pathlib.Path(*rel.parts[1:]))
 row={'staging_path':r['path'],'size':r['size'],'source_candidates':[str(p.relative_to(base)) for p in paths],'matches':[]}
 for p in paths:
  if p.is_file():
   a=hashlib.sha256((base/r['path']).read_bytes()).hexdigest();b=hashlib.sha256(p.read_bytes()).hexdigest();row['staging_sha256']=a;row['matches'].append({'source':str(p.relative_to(base)),'size':p.stat().st_size,'sha256':b,'equal':a==b,'mtime_utc':datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat()})
 rows.append(row)
(out/'local-source-sample.json').write_text(json.dumps({'eligible':len(candidates),'sample':len(chosen),'maximum_staging_bytes':4*1024*1024,'rows':rows},ensure_ascii=False,indent=2));print('sample',len(rows),'existing',sum(bool(r['matches']) for r in rows),'same',sum(any(m['equal'] for m in r['matches']) for r in rows),flush=True)
