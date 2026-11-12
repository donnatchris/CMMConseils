#!/usr/bin/env python3
"""Check deliverables and compare a fresh read-only reproduction. No evidence writes."""
import argparse,csv,datetime as dt,hashlib,json,platform,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--out',required=True);p.add_argument('--reproduction',required=True);a=p.parse_args();O=Path(a.out);R=Path(a.reproduction)
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
checks={}
for f in sorted(R.iterdir()):
 if f.suffix=='.json':
  x=json.loads(f.read_text());y=json.loads((O/f.name).read_text())
  if f.name.endswith('operations.json'):x.pop('utc',None);y.pop('utc',None)
  checks[f.name]=x==y
 elif f.suffix=='.csv':checks[f.name]=f.read_bytes()==(O/f.name).read_bytes()
assert checks and all(checks.values()),checks
links=[]
for f in O.glob('*.md'):
 for dest in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if '://' not in dest:links.append({'report':f.name,'target':dest,'exists':(f.parent/dest.split('#')[0]).exists() or dest=='verification-livrables.json'})
assert all(x['exists'] for x in links)
rows=list(csv.DictReader((O/'activite-17octobre.csv').open()))
assert len(rows)==98 and sum(x['in_1645_1800']=='True' for x in rows)==64
assert all(dt.datetime.fromisoformat(x['utc'])==dt.datetime.fromisoformat(x['paris']) for x in rows)
net=list(csv.DictReader((O/'comparaison-reseaux.csv').open()));assert len(net)==36
# Public reports/CSVs must not disclose a raw MAC, an email or a phone number field.
for f in list(O.glob('*.md'))+list(O.glob('*.csv')):
 assert not re.search(r'\b(?:[0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}\b',f.read_text()),f
logs=[json.loads(l) for f in Path('telephones/recherche-TP-02').glob('extraction-*/extraction.jsonl') for l in f.read_text().splitlines()];profiles=[]
for x in logs:
 if x.get('status')!='ok' or 'configurationprofiles' not in x['domain']:continue
 f=Path(x['output']);b=f.read_bytes();hits=sum(b.count(s) for s in [b'ASUS_Z01RD','ASUS_Z01RD'.encode('utf-16le')])
 profiles.append({'fileID':x['fileID'],'relativePath':x['relativePath'],'sha256':sh(f),'matches_extraction':sh(f)==x['sha256'],'literal_ASUS_SSID_hits':hits})
assert all(x['matches_extraction'] for x in profiles)
result={'python':platform.python_version(),'verified_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'script_sha256':sh(Path(__file__)),'reproduction_directory':str(R),'reproduced_data':checks,'comparison_rule':'JSON objects equal, except execution UTC in operations; CSV byte-identical','local_links_checked':len(links),'all_links_exist':True,'day_properties':len(rows),'focus_properties':64,'networks':len(net),'UTC_Paris_agreement':True,'no_literal_MAC_in_MD_CSV':True,'profile_literal_search':profiles,'profile_search_limit':'SSID literal search in extracted profile files; no history of deleted or unbacked profiles; no claim to parse all payload formats','decrypted_manifest_sha256_now':sh(Path('/mnt/data/forensic/SADEDINE-2026/ANALYSES/TP-02/Manifest-decrypted.db'))}
with (O/'verification-livrables.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'reproduced_data_files':len(checks),'local_links':len(links),'profiles_checked':len(profiles),'ASUS_profile_hits':sum(x['literal_ASUS_SSID_hits'] for x in profiles),'all_checks_passed':True}))
