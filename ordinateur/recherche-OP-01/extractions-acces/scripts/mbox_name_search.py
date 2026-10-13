import pathlib,zipfile,json,hashlib
base=pathlib.Path('/mnt/windows');out=pathlib.Path('/home/sansforensics/analysis/OP-01/extractions-acces-20261013');source='L16B/MESSAGERIES/rct93300@gmail.com/takeout-20241028T114105Z-001.zip';member='Takeout/Mail/L16.mbox'
with zipfile.ZipFile(base/source) as z:
 with z.open(member) as f:
  digest=hashlib.sha256();count=0;hits=[];tail=b'';offset=0;needle=b'appleid-977451'
  while True:
   b=f.read(1024*1024)
   if not b:break
   digest.update(b);data=tail+b;start=0
   while True:
    n=data.lower().find(needle,start)
    if n<0:break
    hits.append(offset-len(tail)+n);start=n+len(needle)
   offset+=len(b);tail=data[-(len(needle)-1):]
result={'archive':source,'member':member,'uncompressed_bytes':offset,'sha256':digest.hexdigest(),'ascii_case_insensitive_needle':needle.decode(),'offsets':hits,'limit':'Recherche textuelle ciblée du nom ; ne valide pas chaque message, encodage MIME ou contenu de pièce jointe.'};(out/'mbox-pdf-name-search.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print('MBOX name search',offset,'hits',len(hits),flush=True)
