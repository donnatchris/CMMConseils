"""Contrôles finaux des sources et empreintes des livrables B à E."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
P=Path('/media/shared/codeProjects/DMMConseils')
B=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114'
REPORT=P/'inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md'
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def historical_source(value, expected):
    marker='/inventaire-DNEF/'
    if marker not in value:return Path(value)
    relative='inventaire-DNEF/'+value.split(marker,1)[1]
    journal=json.loads((P/'inventaire-DNEF/travaux-techniques/reorganisation-20261114/prive/journal-deplacement.json').read_text())
    for item in journal['fichiers']:
        if item['ancien']==relative:
            return P/item['original_conserve'] if item.get('original_conserve') and item['sha256_avant']==expected else P/item['nouveau']
    return Path(value)

checks=[];seen=set()
for rel in ['telephones-passe1/sources.json','telephones-passe2/sources.json','op01-artefacts/sources.json','attributs/sources.json']:
    for x in json.loads((B/'prive'/rel).read_text()):
        if not x.get('source') or not x.get('sha256') or x['source'].endswith('-shm'):continue
        key=(x['source'],x['sha256'])
        if key in seen:continue
        seen.add(key);p=historical_source(x['source'],x['sha256'])
        checks.append({'source':str(p),'expected':x['sha256'],'actual':sha(p),'ok':sha(p)==x['sha256']})
for x in json.loads((B/'prive/complement-natif-v2/collection.json').read_text()):
    src=Path('/media/shared/forensic/SADEDINE-2026/TP-03/00008110-001249321444801E')/x['fileID'][:2]/x['fileID']
    dst=B/'prive/complement-natif-v2/files'/x['domain']/x['relativePath']
    for path,h in [(src,x['ciphertext_sha256']),(dst,x['sha256'])]:checks.append({'source':str(path),'expected':h,'actual':sha(path),'ok':sha(path)==h})
assert all(x['ok'] for x in checks)
links=re.findall(r'\]\(([^)]+)\)',REPORT.read_text())
local=[x.split('#')[0] for x in links if not x.startswith('http')]
# Self-generated verification and manifest are created below.
assert all((REPORT.parent/x).exists() or x.endswith(('verification-finale.json','manifest-sha256.txt')) for x in local)
q1=subprocess.run(['python3',str(P/'inventaire-DNEF/travaux-techniques/reorganisation-20261114/verifier.py'),'--historique'],cwd=P,capture_output=True,text=True)
assert q1.returncode==0
ips=json.loads((P/'telephones/recherche-TP-03/final-checks/ips-metadata.json').read_text())
result={'source_checks':checks,'checked_count':len(checks),'all_source_hashes_ok':True,'q1_originals_preserved':True,
        'tp03_ips_inventory_count':len(ips),'ips_entries_mentioning_2024_10_15':[x['path'] for x in ips if '2024-10-15' in json.dumps(x)],
        'report_local_links_checked':len(local),
        'mount':subprocess.check_output(['findmnt','-n','-o','SOURCE,OPTIONS','/mnt/windows'],text=True).strip()}
with (B/'verification-finale.json').open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2)
lines=[]
for p in sorted(B.rglob('*')):
    if not p.is_file() or p.name=='manifest-sha256.txt' or '__pycache__' in p.parts:continue
    lines.append(sha(p)+'  '+str(p.relative_to(P)))
lines.append(sha(REPORT)+'  '+str(REPORT.relative_to(P)))
with (B/'manifest-sha256.txt').open('x') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps({'source_checks':len(checks),'all_ok':True,'manifest_entries':len(lines),'ips_count':len(ips),'ips_15_oct':len(result['ips_entries_mentioning_2024_10_15']),'q1_originals_preserved':True}))
