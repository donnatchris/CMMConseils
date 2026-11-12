import pathlib,json,subprocess,hashlib
root=pathlib.Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013');dest=root/'tsk-retry';dest.mkdir(exist_ok=True);rows=[json.loads(l) for l in (root/'recovery-results.jsonl').read_text().splitlines() if 'decompress' in json.loads(l).get('error','')];out=[]
for r in rows:
 x={'mft_index':r['mft_index'],'nominal_path':r['preferred_path'],'expected_size':r['native_size']}
 try:
  p=subprocess.run(['icat','-r','/mnt/dislocker/dislocker-file',str(r['mft_index'])],capture_output=True,timeout=60);b=p.stdout;x.update({'returncode':p.returncode,'stderr':p.stderr.decode('utf-8','replace')[:2000],'read_bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'nonzero_bytes':len(b)-b.count(0),'header_hex':b[:64].hex(),'size_equals_expected':len(b)==r['native_size']})
  if b and b.strip(b'\0'):(dest/(str(r['mft_index'])+'.bin')).write_bytes(b)
 except Exception as ex:x['error']=str(ex)
 out.append(x);print(r['mft_index'],x.get('returncode'),x.get('read_bytes'),flush=True)
(root/'tsk-compressed-retry.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print('retry completed',len(out),flush=True)
