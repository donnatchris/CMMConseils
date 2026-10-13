import pyfsntfs,json,datetime,pathlib
root=pathlib.Path('/tmp/OP-01-integrite-20261013/ntfs');rows=[json.loads(s) for s in (root/'mft-gap-records.jsonl').read_text().splitlines()];v=pyfsntfs.volume();v.open('/mnt/dislocker/dislocker-file');result=[]
for idx in [118,15292,26217,56416]:
 r=next(r for r in rows if r['mft_index']==idx);f=v.get_file_entry(idx);times={k:(datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=getter()//10)).isoformat() for k,getter in [('creation',f.get_creation_time_as_integer),('modification',f.get_modification_time_as_integer),('mft_change',f.get_entry_modification_time_as_integer),('access',f.get_access_time_as_integer)]};result.append({'mft_index':idx,'SI_from_binary_scan':r['SI'],'SI_from_libfsntfs':times,'equal':times==r['SI']})
(root/'mft-crosscheck.json').write_text(json.dumps(result,indent=2));v.close();print('equal',all(r['equal'] for r in result))
