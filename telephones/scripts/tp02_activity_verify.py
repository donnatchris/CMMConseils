#!/usr/bin/env python3
"""Verify targeted outputs against a separate reproduction and check redaction/time/source invariants."""
import argparse,csv,json,hashlib,plistlib,sys,os,datetime as dt
from pathlib import Path
sys.path.insert(0,'telephones/scripts');import tp02_forensic as c
parser=argparse.ArgumentParser();parser.add_argument('--out',required=True);parser.add_argument('--reproduction',required=True);args=parser.parse_args();out=Path(args.out);rep=Path(args.reproduction);os.umask(0o077)
comparison=[]
for f in rep.iterdir():
 if f.suffix not in ['.csv','.json']:continue
 if f.name in ['operations.json','correlation-operations.json']:continue
 if f.suffix=='.json':same=json.loads(f.read_text())==json.loads((out/f.name).read_text())
 else:same=f.read_bytes()==(out/f.name).read_bytes()
 comparison.append({'file':f.name,'identical':same})

checks=[]
with (out/'timeline-correlated.csv').open() as f:
 reader=csv.DictReader(f);timeline=list(reader)
for n,v in enumerate(timeline,2):
 utc=dt.datetime.fromisoformat(v['utc']);paris=dt.datetime.fromisoformat(v['paris']);assert utc==paris,(n,v['locator']);assert v['sha256'];assert v['raw_value']
checks.append({'check':'timeline UTC/Paris equality, raw values and hashes present','rows':len(timeline),'status':'ok'})
for name in ['source-verification.json','additional-source-verification.json']:
 data=json.loads((out/name).read_text());assert all(v.get('plaintext_matches') and v.get('ciphertext_matches') for v in data);checks.append({'check':name,'objects':len(data),'status':'ok'})
assert all(v['unchanged_during_run'] for v in json.loads((out/'source-verification.json').read_text()))
# No known network identifier / rotation key leaks into any new report/result/script.
r=Path('telephones/recherche-TP-02/extraction-systeme-20261014/files/SystemPreferencesDomain');v=plistlib.loads((r/'com.apple.wifi.known-networks.plist').read_bytes())['wifi.network.ssid.ASUS_Z01RD'];w=plistlib.loads((r/'SystemConfiguration/com.apple.wifi-private-mac-networks.plist').read_bytes());pr=next(x for x in w['List of scanned networks with private mac'] if x.get('SSID_STR')=='ASUS_Z01RD')
sensitive=[x['BSSID'].lower() for x in v['BSSList']]+[pr['BSSID'].lower(),pr['RotationKeyUsed'].hex(),pr['PRIVATE_MAC_ADDRESS']['PRIVATE_MAC_ADDRESS_VALUE'].hex()]
for f in list(out.glob('*.md'))+list(out.glob('*.json'))+list(out.glob('*.csv')):
 text=f.read_text().lower();assert not any(secret in text for secret in sensitive),f.name
checks.append({'check':'known network identifiers/rotation key absent from new outputs','status':'ok'})
required=['wifi-analysis.md','health-analysis.md','october28-analysis.md','calls-analysis.md','backup-consistency.md','timeline-correlated.csv','findings-summary.md'];assert all((out/n).stat().st_size for n in required)
# Every relative markdown link to an artifact must resolve (external links excluded).
import re
for f in out.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  if not target.startswith('http'):assert (f.parent/target).exists(),(f.name,target)
checks.append({'check':'required outputs and local Markdown links','status':'ok'})
assert all(x['identical'] for x in comparison)
result={'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'reproduction_comparisons':comparison,'checks':checks,'published_scripts':[{'path':str(p),'sha256':c.sha(p)} for p in [Path('telephones/scripts/tp02_activity_oct2024.py'),Path('telephones/scripts/tp02_activity_correlations.py')]],'operations_note':'Operation logs preserve executed-version digests. Published scripts additionally mask opaque meta bytes, exclude campaign outputs from prior-results review and expose UTC for ancillary Photos lifecycle/migrations. Final result equality verified.','limits':['Reproduction uses same extracted evidence; not an independent acquisition','No full-backup hash recomputation','Sources read-only; no decryption']}
(out/'verification-new-campaign.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'comparisons':len(comparison),'timeline_rows':len(timeline),'checks':'ok'}))
