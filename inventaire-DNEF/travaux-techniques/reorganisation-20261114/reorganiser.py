from pathlib import Path
import ast
import datetime as dt
import hashlib
import json
import os
import re
import shutil

ROOT=Path('/mnt/data/codeProjects/DMMConseils')
BASE=ROOT/'inventaire-DNEF'
AUDIT=BASE/'travaux-techniques/reorganisation-20261114'
assert not AUDIT.exists(), 'Journal déjà existant'
sources=[p for p in BASE.iterdir() if p.is_file() and p.suffix.lower() in {'.csv','.docx','.pdf','.xlsx','.jpeg'}]
reports=[p for p in BASE.iterdir() if p.is_file() and p.suffix=='.md']
assert len(sources)==7 and len(reports)==2
moves=[(p,BASE/'documents-recus'/p.name) for p in sources]
moves += [(p,BASE/'rapports'/p.name) for p in reports]
moves += [(BASE/'recherche-Q1-20261114',BASE/'travaux-techniques/recherche-Q1-20261114'),
          (BASE/'investigations-B-E-20261114',BASE/'travaux-techniques/investigations-B-E-20261114'),
          (BASE/'scripts',BASE/'travaux-techniques/recherche-Q1-20261114/scripts')]
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def relocated(p):
    for old,new in moves:
        if p==old:return new
        if old.is_dir() and p.is_relative_to(old):return new/p.relative_to(old)
    return p
entries=[]
for old,new in moves:
    files=[old] if old.is_file() else sorted(p for p in old.rglob('*') if p.is_file())
    for p in files:
        dest=new if old.is_file() else new/p.relative_to(old)
        entries.append({'ancien':str(p.relative_to(ROOT)),'nouveau':str(dest.relative_to(ROOT)),
                        'sha256_avant':sha(p),'taille':p.stat().st_size})
AUDIT.mkdir(parents=True)
(AUDIT/'prive').mkdir(mode=0o700)
(AUDIT/'.gitignore').write_text('prive/\n')
for old,new in moves:
    new.parent.mkdir(parents=True,exist_ok=True)
    assert not new.exists(),str(new)
    old.rename(new)
assert all(sha(ROOT/e['nouveau'])==e['sha256_avant'] for e in entries)
mapping={str(ROOT/e['ancien']):ROOT/e['nouveau'] for e in entries}
def update_links(text):
    old_parent=BASE;new_parent=BASE/'rapports'
    def replace(m):
        value=m.group(1)
        if value.startswith(('http:','https:','#')):return m.group(0)
        path,sep,anchor=value.partition('#')
        old=(old_parent/path).resolve()
        dest=mapping.get(str(old))
        if dest is None:
            dest=old
            for source,target in moves:
                if old==source or old.is_relative_to(source):dest=target/old.relative_to(source);break
        return ']('+os.path.relpath(dest,new_parent)+(sep+anchor if sep else '')+')'
    return re.sub(r'\]\(([^)]+)\)',replace,text)
prefixes=[('inventaire-DNEF/scripts/','inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/scripts/'),
          ('inventaire-DNEF/recherche-Q1-20261114','inventaire-DNEF/travaux-techniques/recherche-Q1-20261114'),
          ('inventaire-DNEF/investigations-B-E-20261114','inventaire-DNEF/travaux-techniques/investigations-B-E-20261114')]
for name in ['Inventaire_saddedine.csv','Note_analyse_inventaire_DNEF_SADEDINE-2026.docx']:
    prefixes.append(('inventaire-DNEF/'+name,'inventaire-DNEF/documents-recus/'+name))
for name in [p.name for p in reports]:prefixes.append(('inventaire-DNEF/'+name,'inventaire-DNEF/rapports/'+name))
for e in entries:
    p=ROOT/e['nouveau'];original=p.read_bytes()
    is_report=e['ancien'] in {str(x.relative_to(ROOT)) for x in reports}
    is_script=p.suffix=='.py' and 'scripts' in p.parts
    if not(is_report or is_script):continue
    text=original.decode()
    if is_report or p.name=='rediger_q1.py':text=update_links(text)
    for old,new in prefixes:text=text.replace(old,new)
    if p.name=='rediger_q1.py':
        text=text.replace("work = base / 'recherche-Q1-20261114'","work = base / 'travaux-techniques/recherche-Q1-20261114'")
        for name in ['Inventaire_saddedine.csv','Note_analyse_inventaire_DNEF_SADEDINE-2026.docx']:
            text=text.replace("base / '"+name+"'","base / 'documents-recus/"+name+"'")
        text=text.replace("base / 'Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md'","base / 'rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md'")
        text=text.replace("base / 'scripts/verifier_q1.py'","work / 'scripts/verifier_q1.py'")
    if p.name in ['monter_op01.py','monter_op01_v2.py','dechiffrer_complement.py']:
        text=text.replace('parents[3]','parents[4]')
    if p.name=='verifier_cloture.py':
        text=text.replace("p=Path(x['source'])","p=historical_source(x['source'],x['sha256'])")
        at="checks=[];seen=set()"
        helper="""def historical_source(value, expected):
    marker='/inventaire-DNEF/'
    if marker not in value:return Path(value)
    relative='inventaire-DNEF/'+value.split(marker,1)[1]
    journal=json.loads((P/'inventaire-DNEF/travaux-techniques/reorganisation-20261114/prive/journal-deplacement.json').read_text())
    for item in journal['fichiers']:
        if item['ancien']==relative:
            return P/item['original_conserve'] if item.get('original_conserve') and item['sha256_avant']==expected else P/item['nouveau']
    return Path(value)

"""
        text=text.replace(at,helper+at)
        old="q1=subprocess.run(['sha256sum','-c',str(P/'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/manifest-sha256.txt')],cwd=P,capture_output=True,text=True)"
        new="q1=subprocess.run(['python3',str(P/'inventaire-DNEF/travaux-techniques/reorganisation-20261114/verifier.py'),'--historique'],cwd=P,capture_output=True,text=True)"
        assert old in text;text=text.replace(old,new)
        text=text.replace('q1_previous_files_unchanged','q1_originals_preserved').replace("'q1_unchanged'","'q1_originals_preserved'")
    if text.encode()!=original:
        archive=AUDIT/'prive/avant'/e['ancien'];archive.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(p,archive)
        e['original_conserve']=str(archive.relative_to(ROOT))
        p.write_text(text)
    if is_script:ast.parse(p.read_text(),filename=str(p))
for e in entries:
    e['sha256_apres']=sha(ROOT/e['nouveau'])
    if '/documents-recus/' in e['nouveau'] or '/prive/' in e['ancien'] or (ROOT/e['nouveau']).name in ['manifest-sha256.txt','verification-finale.json']:
        assert e['sha256_apres']==e['sha256_avant']
journal={'date_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
         'objet':'Séparation des documents reçus, des rapports et des travaux techniques ; aucun résultat brut réécrit.',
         'fichiers':entries}
with (AUDIT/'prive/journal-deplacement.json').open('x') as f:json.dump(journal,f,ensure_ascii=False,indent=2)
shutil.copy2(Path(__file__),AUDIT/'reorganiser.py')
print(json.dumps({'documents_recus':len(sources),'rapports':len(reports),'fichiers_deplaces':len(entries),
                  'rapports_ou_scripts_adaptes':sum('original_conserve' in e for e in entries),
                  'sources_et_resultats_bruts_inchanges':True},ensure_ascii=False))
