# À exécuter dans SIFT ; seule la copie de travail reçoit des écritures.
import pyfsntfs,pathlib,json,hashlib
v=pyfsntfs.volume();v.open('/mnt/dislocker/dislocker-file');O=pathlib.Path('/home/sansforensics/analysis/OP-01/samsung-almu-20261113');rows=[]
for idx in [181043,30590,166334]:
 f=v.get_file_entry(idx);r={'mft_index':idx,'size':f.size,'file_flags':f.file_attribute_flags,'is_allocated':f.is_allocated(),'streams':f.number_of_alternate_data_streams}
 if idx==181043:
  data=f.read_buffer();(O/'raw/mft-181043-test.pdf').write_bytes(data);r.update({'read_size':len(data),'header_hex':data[:32].hex(),'sha256':hashlib.sha256(data).hexdigest()})
 rows.append(r)
(O/'ntfs-direct-check.json').write_text(json.dumps(rows,indent=2));v.close()
