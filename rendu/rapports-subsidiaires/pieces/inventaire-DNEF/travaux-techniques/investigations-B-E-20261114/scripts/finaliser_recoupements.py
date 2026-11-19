#!/usr/bin/env python3
"""Identités de copies PC, archives et datation SI/FN, sans modifier les preuves."""
import collections
import datetime as dt
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import plistlib
import re
import sqlite3
import zipfile
from zoneinfo import ZoneInfo
P=Path('/media/shared/codeProjects/DMMConseils');B=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive'
O=B/'recoupements-finaux';O.mkdir(exist_ok=False);W=Path('/mnt/windows');TZ=ZoneInfo('Europe/Paris')
rows=[json.loads(x) for x in (B/'op01-mft-tailles/records.jsonl').read_text().splitlines()]
q1=json.loads((P/'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/resultats.json').read_text());targethashes={x['sha512'] for x in q1['inventory']}
def digest(p,alg='sha256'):
    with p.open('rb') as f:return hashlib.file_digest(f,alg).hexdigest()
res={'mft_size_candidates':0,'candidate_files':[],'zip_candidates':[],'mini_files':[],'directories':[]};errors=[]
for x in rows:
    fn=next((v for v in x['FN'] if v['namespace']!=2),x['FN'][0] if x['FN'] else None)
    if not fn:continue
    path=fn['path'];p=W.joinpath(*path.split('\\'))
    if x['directory'] and path in ['L16B','L16B\\TELEPHONES','L16B\\TELEPHONES\\IPHONE13_MINI']:
        res['directories'].append({'index':x['index'],'path':path,'SI':x['SI'],'FN':fn['times']})
    if x.get('pdf_size_candidate'):
        res['mft_size_candidates']+=1
        if not fn['parent_uncertain'] and p.is_file() and p.stat().st_ino==x['index']:
            with p.open('rb') as f:signature=f.read(8)
            h=digest(p,'sha512')
            row={'index':x['index'],'path':path,'bytes':p.stat().st_size,'pdf_signature':signature.startswith(b'%PDF-'),'sha512':h,'target_content':h in targethashes,'SI':x['SI'],'FN':fn['times']}
            res['candidate_files'].append(row)
            if path.startswith('L16B\\TELEPHONES\\IPHONE13_MINI\\'):
                iv=next(v for v in q1['inventory'] if v['path']=='C:\\'+path)
                value=Decimal(row['SI']['creation']['filetime']-116444736000000000)/Decimal(10000000)
                text=iv['creation'].split('[')[0];d=dt.datetime.fromisoformat(text);fraction=re.search(r'\.(\d+)',text)
                csvvalue=Decimal(int(d.replace(microsecond=0).timestamp()))+(Decimal('0.'+fraction.group(1)) if fraction else Decimal(0))
                row['csv_creation_equals_SI']=value==csvvalue
                row['FN_creation_paris']=dt.datetime.fromisoformat(row['FN']['creation']['utc']).astimezone(TZ).isoformat()
                row['named_streams']=[s for s in x['streams'] if s['name']]
                res['mini_files'].append(row)
    if x['zip_day_candidate'] and x['allocated'] and not fn['parent_uncertain'] and p.is_file() and path.lower().endswith('.zip'):
        row={'index':x['index'],'path':path,'bytes':p.stat().st_size,'members':[]}
        try:
            with zipfile.ZipFile(p) as z:
                for info in z.infolist():
                    name=info.filename;matched=False;h=None
                    # Bound decompression to the known PDF sizes, at most 2 MiB each.
                    sizes={v['bytes'] for rr in q1['phones'].values() for v in rr}
                    if info.file_size in sizes and info.file_size<=2*1024*1024:
                        h=hashlib.sha512(z.read(info)).hexdigest();matched=h in targethashes
                    row['members'].append({'name':name,'size':info.file_size,'date_fields':info.date_time,'matching_pdf_content':matched,'sha512_if_tested':h})
        except Exception as e:row['error']=str(e);errors.append({'path':path,'error':str(e)})
        res['zip_candidates'].append(row)
for ph in ['TP-03','TP-02']:
    man=P/f'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/{ph}/Manifest.db'
    c=sqlite3.connect(man.as_uri()+'?mode=ro&immutable=1',uri=True)
    pats={'knowledgeC':r'(^|/)knowledgeC\.db$', 'Powerlog_DB':r'(powerlog|powerlogs|PLStorage).*(\.db|\.sqlite)$',
          'unified_tracev3':r'\.tracev3$', 'logarchive':r'\.logarchive(/|$)', 'Biome_files':r'(^|/)Biome/',
          'lockstate_named':r'(^|/)(lockstate|keybag|lockdownd).*\.(log|db|sqlite)$', 'firstunlock_markers':r'\.FirstUnlock$'}
    covered={k:[] for k in pats}
    for fid,domain,rel,blob in c.execute('select fileID,domain,relativePath,file from Files where flags=1'):
        for key,pat in pats.items():
            if re.search(pat,rel,re.I):
                pl=plistlib.loads(blob);v=pl['$objects'][pl['$top']['root'].data]
                covered[key].append({'fileID':fid,'domain':domain,'relativePath':rel,**{k:v.get(k) for k in ['Birth','LastModified','LastStatusChange','ProtectionClass','Size']}})
    c.close();res[ph+'_availability']=covered
res['summary']={'mini_files':len(res['mini_files']),'all_csv_creation_equal_SI':all(x['csv_creation_equals_SI'] for x in res['mini_files']),
                'mini_FN_first':min(x['FN_creation_paris'] for x in res['mini_files']),
                'mini_FN_last':max(x['FN_creation_paris'] for x in res['mini_files']),
                'matched_outside_mini':[x for x in res['candidate_files'] if x['target_content'] and not x['path'].startswith('L16B\\TELEPHONES\\IPHONE13_MINI\\')],
                'zip_members_matched':sum(y['matching_pdf_content'] for x in res['zip_candidates'] for y in x['members'])}
with (O/'resultats.json').open('x') as f:json.dump(res,f,ensure_ascii=False,indent=2)
with (O/'erreurs.json').open('x') as f:json.dump(errors,f,ensure_ascii=False,indent=2)
print(json.dumps({'summary':{k:v for k,v in res['summary'].items() if k!='matched_outside_mini'},'matched_outside_mini':[(x['path'],x['bytes']) for x in res['summary']['matched_outside_mini']],
                  'candidates_read':len(res['candidate_files']),'zip_containers':len(res['zip_candidates']),'errors':len(errors),
                  'availability':{ph:{k:len(v) for k,v in res[ph+'_availability'].items()} for ph in ['TP-03','TP-02']}},ensure_ascii=False))
