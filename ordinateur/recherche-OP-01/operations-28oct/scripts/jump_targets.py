import pathlib,csv,json,collections
p=pathlib.Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014')
rows=[];counts={}
for f in (p/'jumplists-standard').glob('*.csv'):
 data=list(csv.DictReader(f.open(encoding='utf-8-sig')));counts[f.name]=len(data)
 for x in data:
  hits={k:v for k,v in x.items() if v and ('2024-10-28' in v or 'l16b' in v.lower() or '.pst' in v.lower() or 'kingston' in v.lower())}
  if hits:rows.append({'csv':f.name,'hits':hits,'row':x})
result={'counts':counts,'matches':rows,'caution':'SourceCreated/Modified/Accessed décrivent la copie de travail ; les dates Target décrivent les métadonnées de cible, pas nécessairement une consultation.'}
(p/'jumplists-targets-standard.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(counts,'matches',len(rows))
for r in rows:
 x=r['row']
 if any(x.get(k,'').startswith('2024-10-28') for k in ['CreationTime','LastModified']): print(json.dumps({k:x.get(k) for k in ['AppIdDescription','CreationTime','LastModified','Path','LocalPath','VolumeSerialNumber','VolumeLabel','DriveType']},ensure_ascii=False))
print('PST',sum(any('.pst' in str(v).lower() for v in r['hits'].values()) for r in rows))
