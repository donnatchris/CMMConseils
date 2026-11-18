"""Candidats supprimés par noms, taille et corbeille ; lectures d'en-têtes sur SIFT."""
import collections
import hashlib
import json
import os
from pathlib import Path
import pyfsntfs
import re
import subprocess
P=Path('/media/shared/codeProjects/DMMConseils');O=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive/metadata';os.umask(0o077);O.mkdir(parents=True,exist_ok=False)
R=Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013')
selected=[];counts=collections.Counter();digest=hashlib.sha256()
with (R/'mft-deleted-records.jsonl').open('rb') as f:
 for line in f:
  digest.update(line);x=json.loads(line);counts['rows']+=1
  sizes=[a.get('logical_size',0) for a in x['data_attributes'] if not a.get('stream')]
  names=' '.join(n['name'] for n in x['names'])
  reasons=[]
  if re.search(r'archiv[e]?[_ -]*sadd?edine|rejets?[_ -]*sadd?edine|inventaire[_ -]*sadd?edine',names,re.I):reasons.append('target_name')
  if 3525227798 in sizes:reasons.append('exact_archive_size')
  if any(3*1024**3<=v<=4*1024**3 for v in sizes):reasons.append('archive_size_range_3_4_GiB')
  if 527208 in sizes:reasons.append('exact_inventory_size')
  if re.search(r'\.zip$',names,re.I) and not x['allocated']:reasons.append('deleted_zip_name')
  if reasons:selected.append(dict(x,reasons=reasons))
v=pyfsntfs.volume();v.open('/mnt/dislocker/dislocker-file');results=[]
bitmap=v.get_file_entry(6);bits=bitmap.read_buffer_at_offset(bitmap.size,0);cluster=v.cluster_block_size
for x in selected:
 row={'mft_index':x['mft_index'],'allocated':x['allocated'],'directory':x['directory'],'names':x['names'],'data_attributes':x['data_attributes'],'reasons':x['reasons']}
 try:
  e=v.get_file_entry(x['mft_index']);row['size']=e.size;row['extents']=[e.get_extent(i) for i in range(e.number_of_extents)]
  head=e.read_buffer_at_offset(min(e.size,65536),0);tail=e.read_buffer_at_offset(min(e.size,65557),max(0,e.size-65557)) if e.size else b''
  row.update(header_hex=head[:64].hex(),header_zero=not head.strip(b'\0'),tail_zero=not tail.strip(b'\0'),zip_header=head.startswith(b'PK'),eocd_in_tail=tail.rfind(b'PK\x05\x06'))
  if row['zip_header'] or row['eocd_in_tail']>=0 or 'target_name' in row['reasons']:
   (O/f"{x['mft_index']}-head.bin").write_bytes(head);(O/f"{x['mft_index']}-tail.bin").write_bytes(tail)
  n=alloc=0
  for offset,length,flags in row['extents']:
   if flags or offset<0:continue
   for c in range(offset//cluster,(offset+length+cluster-1)//cluster):
    n+=1;alloc+=(bits[c//8]>>(c%8))&1
  row.update(extent_clusters=n,currently_allocated_clusters=alloc)
 except Exception as ex:row['error']=str(ex)
 results.append(row)
v.close()
prior=[]
for line in (R/'recovery-results.jsonl').read_text().splitlines():
 x=json.loads(line)
 if 'recycle_info' in x and re.search(r'archiv[e]?[_ -]*sadd?edine|rejets?[_ -]*sadd?edine|inventaire[_ -]*sadd?edine',x['recycle_info']['original_path'],re.I):prior.append(x)
summary={'source_export':str(R/'mft-deleted-records.jsonl'),'source_sha256':digest.hexdigest(),'rows':counts['rows'],'selected':len(results),'bitmap_sha256':hashlib.sha256(bits).hexdigest(),'cluster_size':cluster,'target_recycle_entries':prior,'mount':subprocess.check_output(['findmnt','-n','-o','OPTIONS','/mnt/windows'],text=True).strip()}
for name,data in [('candidats.json',results),('synthese.json',summary)]:
 with (O/name).open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2)
print(json.dumps({'rows':counts['rows'],'selected':len(results),'reasons':dict(collections.Counter(s for x in results for s in x['reasons'])),'read_errors':sum('error' in x for x in results),'target_recycle_entries':len(prior)}))
