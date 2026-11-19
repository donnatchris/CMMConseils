#!/usr/bin/env python3
"""Inventaire de chemins L16B datables du 28/10/2024 à partir d'extractions Windows.
Aucune lecture ou modification du système Windows source ; aucune écriture sur l'image.
"""
from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import json,csv,re,collections,hashlib,xml.etree.ElementTree as ET,struct,os
ROOT=Path('/mnt/data/codeProjects/DMMConseils')
BASE=ROOT/'ordinateur/recherche-OP-01'
OUT=BASE/'inventaire-L16B-20241028-20261116'
PARIS=ZoneInfo('Europe/Paris');DAY='2024-10-28'
SOURCES=[
 'extractions-acces/l16b-inventory.json','extractions-acces/l16b-mft.jsonl',
 'fichiers-supprimes/mft-deleted-records.jsonl','fichiers-supprimes/mft-summary.json',
 'fichiers-supprimes/recovery-selection.jsonl','fichiers-supprimes/recovery-results.jsonl','fichiers-supprimes/recycle-pairs.json',
 'operations-28oct/interactions-28oct.csv','integrite-evtx/independent/results.jsonl',
 'samsung-almu-20261113/resultats/print-events-day.json',
]
source_paths=[BASE/s for s in SOURCES]+[ROOT/'investigations/20261019-retour-cliente/resultats/sift/events-16-29oct.json']
def canon(s):return s.replace('/','\\').rstrip('\\').casefold()
def full(s):
 s=s.replace('/','\\')
 return s if s.lower().startswith('c:\\') else 'C:\\'+s

def date(s):
 if not s:return None
 d=datetime.fromisoformat(s.replace('Z','+00:00'))
 return d.replace(tzinfo=timezone.utc) if d.tzinfo is None else d

def local(s):return date(s).astimezone(PARIS).isoformat() if s else ''
def onday(s):return bool(s) and date(s).astimezone(PARIS).date().isoformat()==DAY

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 return h.hexdigest()

def blank(path,category,present,size=None):
 return {'path':path,'aliases':[],'category':category,'present_at_original_path_in_image':present,'size':size,'mft_index':None,'mft_sequence':None,'SI':{},'FN':[], 'deletion_utc':'','recovery_sha256':'','recovery_path':'','notes':[],'evidence':[]}

inventory=json.loads((BASE/SOURCES[0]).read_text())
mft={canon(full(r['path'])):(i,r) for i,r in enumerate(map(json.loads,(BASE/SOURCES[1]).open()),1)}
rows={};late=[];uncertain=[];directories=set();scanned=0
for inv in inventory:
 path=full(inv['path']);key=canon(path);line,r=mft[key]
 assert r['allocated'] and 'error' not in r
 candidates=[n for n in r['FN'] if n['namespace']!=2 and canon(n['name'])==canon(path.rsplit('\\',1)[-1])]
 if not candidates:candidates=[n for n in r['FN'] if n['namespace']!=2]
 assert candidates,(path,'FN absent')
 fn=candidates[0];creation=fn['times'].get('creation')
 cat='A — Présent dans l’image ; création FN le 28/10/2024' if onday(creation) else 'D — Création FN postérieure ; non rattaché au 28/10/2024'
 x=blank(path,cat,True,inv['size']);x.update(mft_index=r['mft_index'],mft_sequence=r['sequence'],SI=r['SI'],FN=[dict(n) for n in r['FN']],fn_selected=fn,mtime_inventory_utc=inv['mtime_utc'])
 x['evidence'].append({'source':SOURCES[0],'path':inv['path'],'kind':'Fichier alloué dans l’inventaire de l’image'})
 x['evidence'].append({'source':SOURCES[1],'line':line,'mft_index':r['mft_index'],'kind':'Dates SI et FN de la MFT'})
 if date(x['SI']['modification']).astimezone(PARIS).date().isoformat()>DAY:
  x['notes'].append('Modification SI postérieure au 28/10/2024 : le contenu courant ne peut pas être réputé inchangé depuis cette date.')
 if onday(creation):rows[key]=x
 else:late.append(x)
 p=key
 while '\\' in p:
  p=p.rsplit('\\',1)[0];directories.add(p)
assert len(rows)==1555 and len(late)==3 and len(inventory)==1558

# Scan every selected record of the complete MFT scan, not only recovery candidates.
with (BASE/'fichiers-supprimes/mft-deleted-records.jsonl').open() as f:
 for lineno,line in enumerate(f,1):
  scanned+=1
  if 'l16b' not in line.lower():continue
  r=json.loads(line)
  for fn in r['names']:
   if fn['namespace']==2:continue
   path=full(fn.get('path',''));key=canon(path)
   if not key.startswith('c:\\l16b\\'):continue
   if r['directory']:directories.add(key);continue
   x=blank(path,'E — Chemin MFT reconstruit incertain ; non retenu pour le 28/10/2024',False)
   x.update(mft_index=r['mft_index'],mft_sequence=r['sequence'],SI=r['SI'],FN=[fn],fn_selected=fn)
   x['evidence'].append({'source':'fichiers-supprimes/mft-deleted-records.jsonl','line':lineno,'mft_index':r['mft_index'],'parent_sequence_uncertain':fn['parent_sequence_uncertain'],'kind':'Ancienne entrée MFT non allouée'})
   x['notes'].append('Parent(s) MFT incertain(s) ; les dates conservées précèdent 2024. Le chemin actuel reconstruit ne prouve pas une présence historique sous L16B.')
   if fn['parent_sequence_uncertain']:uncertain.append(x)
   else:raise AssertionError(('Nouvelle ancienne entrée à examiner',path))
assert scanned==json.loads((BASE/'fichiers-supprimes/mft-summary.json').read_text())['selected_records']

selected={r['mft_index']:r for r in map(json.loads,(BASE/'fichiers-supprimes/recovery-selection.jsonl').open())}
for i,pair in enumerate(json.loads((BASE/'fichiers-supprimes/recycle-pairs.json').read_text()),1):
 info=pair['info'];path=info['original_path'];key=canon(path)
 if not key.startswith('c:\\l16b\\'):continue
 matches=pair['R_matches'];assert len(matches)==1
 rm=matches[0];r=selected[rm['mft_index']]
 if onday(info['deletion_utc']):cat='B — Supprimé de L16B le 28/10/2024 ; contenu récupéré en corbeille'
 else:cat='D — Trace de 2026 ; non rattachée au 28/10/2024'
 x=blank(path,cat,False,info['original_size'])
 x.update(mft_index=rm['mft_index'],mft_sequence=r['sequence'],SI=r['SI'],FN=r['names'],fn_selected=next(n for n in r['names'] if n['namespace']!=2),deletion_utc=info['deletion_utc'],recovery_sha256=rm['sha256'],recovery_path=str((BASE/'fichiers-supprimes'/rm['recovered_file']).relative_to(ROOT)))
 assert (ROOT/x['recovery_path']).stat().st_size==x['size']
 x['evidence'].append({'source':'fichiers-supprimes/recycle-pairs.json','array_index_1based':i,'I_mft':pair['I_mft'],'R_mft':rm['mft_index'],'kind':'Chemin d’origine et heure de suppression dans $I ; contenu $R récupéré'})
 if onday(info['deletion_utc']):
  assert key not in rows;rows[key]=x
 else:
  x['notes'].append('Le chemin d’origine n’est attesté par la corbeille qu’en 2026 ; les dates SI/FN du contenu récupéré sont aussi de 2026.')
  late.append(x)

# Add exact print destinations recorded on the requested day, preserving case variants.
for i,e in enumerate(json.loads((BASE/'samsung-almu-20261113/resultats/print-events-day.json').read_text()),1):
 path=e.get('data',{}).get('Param6','');key=canon(path)
 if e['id']!=307 or not key.startswith('c:\\l16b\\') or not onday(e['utc']):continue
 if key not in rows:
  x=blank(path,'C — Chemin de sortie PDF référencé le 28/10/2024 ; fichier absent à ce chemin',False)
  x['notes'].append('Destination consignée dans PrintService et référencée par une Jump List. Ne pas confondre C:\\L16B\\Sage.pdf avec le fichier actuellement présent C:\\L16B\\SAGE\\sage.pdf ; le lien exact entre ces chemins n’est pas établi ici.')
  rows[key]=x
 x=rows[key]
 if path!=x['path'] and path not in x['aliases']:x['aliases'].append(path)
 x['evidence'].append({'source':'samsung-almu-20261113/resultats/print-events-day.json','array_index_1based':i,'kind':'PrintService : impression PDF terminée','event_id':307,'record':e['record'],'utc':e['utc'],'paris':e['paris'],'pages':e['data'].get('Param8'),'path_recorded':path})

# Jump Lists: attach exact file paths and separately retain directory references.
dirrefs=[];unknown=[]
with (BASE/'operations-28oct/interactions-28oct.csv').open(newline='') as f:
 for lineno,e in enumerate(csv.DictReader(f),2):
  key=canon(e['path'])
  if not key.startswith('c:\\l16b\\'):continue
  ev={'source':'operations-28oct/interactions-28oct.csv','line':lineno,'kind':'Jump List : dernière interaction mémorisée','paris':e['lastmodified_paris'],'artifact':e['source'],'entry':e['entry']}
  assert onday(e['lastmodified_paris'])
  if key in rows:rows[key]['evidence'].append(ev)
  elif key in directories:dirrefs.append({'path':e['path'],**ev})
  else:unknown.append({'path':e['path'],**ev})
assert not unknown,unknown

# Recent LNKs: target timestamps and artifact modification are distinct evidence.
all_known={canon(x['path']):x for x in list(rows.values())+late}
for lineno,line in enumerate((BASE/'integrite-evtx/independent/results.jsonl').open(),1):
 if 'l16b' not in line.lower():continue
 e=json.loads(line);path=e.get('target','');key=canon(path)
 if e.get('kind')!='lnk' or not key.startswith('c:\\l16b\\'):continue
 evidence={'source':'integrite-evtx/independent/results.jsonl','line':lineno,'kind':'Raccourci Recent : cible et dates mémorisées','artifact':e['source'],'lnk_file_mtime_utc':e['file_mtime_utc'],'target_creation_utc':e.get('target_creation_utc'),'target_modification_utc':e.get('target_modification_utc'),'target_access_utc':e.get('target_access_utc')}
 if key in all_known:all_known[key]['evidence'].append(evidence)
 elif key in directories:dirrefs.append({'path':path,**evidence})
 elif path=='C:\\L16B\\Nouveau dossier':
  raw=BASE/'integrite-evtx/independent/raw/lnk'/e['source'];attrs=struct.unpack_from('<I',raw.read_bytes(),24)[0]
  assert attrs&0x10
  dirrefs.append({'path':path,'target_attributes_hex':hex(attrs),'is_directory':True,**evidence})
  source_paths.append(raw)
 else:raise AssertionError(('Cible LNK supplémentaire à examiner',path))

# Independent event extraction: extract only file paths from leaf XML values.
rx=re.compile(r'''C:\\L16B\\[^<>\r\n"\x00]*?\.(?:pdf|pst|eml|zip|lnk|docx?|xlsx?|txt|csv|rtf|mbox|7z|png|jpe?g|svg)(?=$|[\s"'<>;,)])''',re.I)
events_source=ROOT/'investigations/20261019-retour-cliente/resultats/sift/events-16-29oct.json'
for i,e in enumerate(json.loads(events_source.read_text()),1):
 xml=e.get('xml','')
 if 'l16b' not in xml.lower():continue
 t=ET.fromstring(xml);timestamp=next(x.attrib['SystemTime'] for x in t.iter() if x.tag.endswith('TimeCreated'))
 if not onday(timestamp):continue
 text='\n'.join(x.text or '' for x in t.iter() if len(x)==0)
 for path in dict.fromkeys(m.group(0) for m in rx.finditer(text)):
  key=canon(path);assert key in rows,('Nouvelle cible événement',path)
  rows[key]['evidence'].append({'source':str(events_source.relative_to(ROOT)),'array_index_1based':i,'kind':'Événement Windows, extraction indépendante','event_id':e.get('id'),'record':e.get('record'),'utc':timestamp,'paris':local(timestamp),'path_recorded':path})

# The two lists deliberately describe paths, not unique contents or distinct file objects.
main=sorted(rows.values(),key=lambda x:canon(x['path']))
excluded=sorted(late+uncertain,key=lambda x:(x['category'],canon(x['path'])))
assert len(main)==1559 and len(late)==4 and len(uncertain)==3
assert collections.Counter(x['category'][0] for x in main)=={'A':1555,'B':3,'C':1}
assert len({canon(x['path']) for x in main})==1559
for i,x in enumerate(main,1):x['id']=f'L{i:04}'
for i,x in enumerate(excluded,1):x['id']=f'X{i:03}'
assert OUT.is_dir() and not (OUT/'inventaire-detaille.json').exists()

fields=['Référence','Chemin complet','Catégorie','Présent au même chemin dans l’image','Taille octets','MFT','Séquence MFT','Création FN Paris','Modification FN Paris','Création SI Paris','Modification SI Paris','Suppression Paris','Contenu récupéré SHA-256','Copie récupérée dans le projet','Autres graphies du chemin','Éléments Windows de contrôle','Observations']
def csvrow(x):
 fn=x.get('fn_selected',{}).get('times',{});si=x['SI'] or {}
 ev=[]
 for e in x['evidence']:
  s=e['source']
  if e.get('line'):s+=':'+str(e['line'])
  if e.get('record'):s+=' ; record '+str(e['record'])
  if e.get('I_mft'):s+=' ; $I MFT '+str(e['I_mft'])+' / $R MFT '+str(e['R_mft'])
  if e.get('paris'):s+=' ; '+e['paris']
  ev.append(s)
 return [x['id'],x['path'],x['category'],'Oui' if x['present_at_original_path_in_image'] else 'Non',x['size'] if x['size'] is not None else '',x['mft_index'] if x['mft_index'] is not None else '',x['mft_sequence'] if x['mft_sequence'] is not None else '',local(fn.get('creation')),local(fn.get('modification')),local(si.get('creation')),local(si.get('modification')),local(x['deletion_utc']),x['recovery_sha256'],x['recovery_path'],' ; '.join(x['aliases']),' | '.join(ev),' '.join(x['notes'])]
for filename,data in [('fichiers-rattaches-au-28oct2024.csv',main),('traces-posterieures-ou-incertaines.csv',excluded)]:
 with (OUT/filename).open('x',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f,delimiter=';');w.writerow(fields);w.writerows(csvrow(x) for x in data)
with (OUT/'liste-chemins-28oct2024.txt').open('x') as f:
 for x in main:f.write(x['path']+'\n')
summary={'created_utc':datetime.now(timezone.utc).isoformat(),'scope':'Fichiers sous C:\\L16B rattachables au 28/10/2024 selon les traces Windows conservées ; liste de chemins, non de contenus uniques.','current_files':len(inventory),'current_FN_28':1555,'recycle_28':3,'print_path_28':1,'main_path_count':len(main),'later_files_excluded':len(late),'uncertain_MFT_paths_excluded':len(uncertain),'MFT_selected_records_scanned':scanned,'MFT_source_sha256':json.loads((BASE/'fichiers-supprimes/mft-summary.json').read_text())['sha256'],'current_FN_28_total_bytes':sum(x['size'] for x in main if x['category'].startswith('A')),'current_FN_28_SI_modification_later':sum(bool(x['SI']) and date(x['SI']['modification']).astimezone(PARIS).date().isoformat()>DAY for x in main if x['category'].startswith('A')),'current_files_by_folder':dict(collections.Counter(x['path'].split('\\')[2] for x in main if x['category'].startswith('A')))}
data={'summary':summary,'files_28':main,'excluded_later_or_uncertain':excluded,'directory_references_not_counted_as_files':dirrefs}
with (OUT/'inventaire-detaille.json').open('x') as f:json.dump(data,f,ensure_ascii=False,indent=2);f.write('\n')

# A readable catalogue contains all names, while the short report explains chronology.
def esc(s):
 s=str(s)
 if s.startswith('`') and s.endswith('`'):return s
 return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n',' ')
def code(s):
 tick='`'*(max([len(x) for x in re.findall(r'`+',s)],default=0)+1)
 return tick+s+tick
catalogue=['# Liste des fichiers rattachables au 28 octobre 2024 — L16B','',
 'Liste de **1 559 chemins** identifiés ou référencés par les traces Windows conservées. Les lettres A/B/C renvoient aux classes expliquées dans le [rapport de méthode](rapport-inventaire-L16B-20241028.md). Les dates FN sont des métadonnées et ne garantissent pas l’identité du contenu courant avec celui de 2024.','',
 '| Réf. | Chemin complet | Classe | Taille (octets) | Création FN Paris | Suppression Paris |','|---|---|---|---:|---|---|']
for x in main:
 fn=x.get('fn_selected',{}).get('times',{})
 catalogue.append('| '+' | '.join(esc(v) for v in [x['id'],code(x['path']),x['category'][0],x['size'] if x['size'] is not None else 'Non déterminée',local(fn.get('creation')),local(x['deletion_utc'])])+' |')
with (OUT/'liste-complete-fichiers-28oct2024.md').open('x') as f:f.write('\n'.join(catalogue)+'\n')

lines=['# Inventaire des fichiers de C:\\L16B d’après les traces Windows — 28 octobre 2024','',
 '**OP-01 — relevé établi le 16 novembre 2026.** La recherche porte sur les chemins des fichiers présents dans l’image acquise et sur les traces historiques conservées. Elle ne représente pas une capture du dossier réalisée le 28 octobre 2024.','',
 '## Résultat','',
 '**1 559 chemins de fichiers sont retenus comme identifiés ou référencés au cours du 28 octobre 2024**, avec trois niveaux de constat :','',
 '| Classe | Nombre | Constat |','|---|---:|---|',
 '| A | **1 555** | Fichiers présents sous L16B dans l’image et portant une création FN le 28/10/2024. |',
 '| B | **3** | Anciens chemins L16B explicitement enregistrés dans la corbeille comme supprimés le 28/10/2024 ; contenus récupérés. |',
 '| C | **1** | Ancien chemin de sortie PDF consigné le 28/10/2024 dans PrintService et une Jump List, sans fichier actuellement à ce chemin. |','',
 '**La liste compte des chemins, pas des fichiers présents simultanément en fin de journée ni des contenus uniques.** Les trois fichiers de classe B ont été retirés avant la fin des opérations ; le chemin de classe C peut avoir porté des versions successives ou être lié à un déplacement.','',
 '## Accès aux listes intégrales','',
 '- [Liste complète lisible : tous les chemins, tailles et dates](liste-complete-fichiers-28oct2024.md).',
 '- [CSV détaillé des 1 559 chemins, avec métadonnées et références](fichiers-rattaches-au-28oct2024.csv).',
 '- [Liste texte : un chemin par ligne](liste-chemins-28oct2024.txt).',
 '- [Traces de 2026 et chemins incertains exclus du total](traces-posterieures-ou-incertaines.csv).',
 '- [Toutes les données et références structurées](inventaire-detaille.json).','',
 'Les CSV sont en UTF-8 avec BOM et séparateur point-virgule ; ils peuvent être ouverts et filtrés dans un tableur.','',
 '## Fichiers présents dans l’image : rattachement FN au 28 octobre','',
 '| Ensemble | Fichiers de classe A |','|---|---:|']
for k,v in summary['current_files_by_folder'].items():lines.append('| '+esc(k)+' | '+str(v)+' |')
lines += ['', '**1 558 fichiers** sont présents sous L16B dans l’inventaire de l’image. Parmi eux, **1 555** ont une création FN le 28/10/2024, pour un total de **'+str(summary['current_FN_28_total_bytes'])+' octets**. Les trois autres portent des créations FN en 2026 et sont présentés séparément. Les archives et les versions développées peuvent contenir les mêmes données ; le total ne mesure pas des données uniques.','',
 '## Anciens chemins du 28 octobre absents du dossier actuel','',
 '| Ancien chemin | Trace Windows datée | État du contenu / limite |','|---|---|---|']
for x in main:
 if x['category'].startswith('B'):
  lines.append('| '+esc(x['path'])+' | $I de la corbeille : suppression '+local(x['deletion_utc'])+' | Contenu $R récupéré, '+str(x['size'])+' octets ; SHA-256 et copie dans le CSV détaillé. |')
 elif x['category'].startswith('C'):
  lines.append('| '+esc(x['path'])+' (aussi consigné `C:\\L16B\\sage.pdf`) | PrintService 307, records **2445** à **15:23:32** (205 pages) et **2450** à **15:28:33** (458 pages) ; Jump List à **15:28:29**. | Chemin de destination référencé ; contenu non retrouvé séparément à ce chemin. Il est distinct du chemin actuel `C:\\L16B\\SAGE\\sage.pdf`. |')
lines += ['', 'Pour les trois fichiers de classe B, les dates FN détaillées sont celles de l’objet `$R` actuellement en corbeille ; l’ancien chemin et la date de suppression proviennent de son `$I`. Elles ne sont pas présentées comme les dates d’une entrée FN encore située au chemin d’origine.','', '`C:\\L16B\\test.pdf` est aussi corroboré par PrintService 307, record 2429 à 15:19:42, et une Jump List à 15:19:49. Les variations de casse `Sage.pdf` / `sage.pdf` à la racine sont regroupées ; le fichier du sous-dossier `SAGE` reste une entrée distincte.','',
 '## Traces exclues du rattachement au 28 octobre 2024','',
 '| Chemin | Motif |','|---|---|']
for x in late:
 fn=x.get('fn_selected',{}).get('times',{})
 reason='Création FN '+local(fn.get('creation'))
 if x['deletion_utc']:reason+=' ; suppression '+local(x['deletion_utc'])+' ; création SI aussi en 2026'
 lines.append('| '+esc(x['path'])+' | '+esc(reason)+' |')
lines += ['', '**Trois anciennes entrées MFT supplémentaires ont des chemins reconstruits incertains** :','']
for x in uncertain:lines.append('- `'+x['path']+'` — MFT '+str(x['mft_index'])+', parent(s) incertain(s), dates conservées en 2022–2023. Aucune présence sous L16B le 28/10/2024 n’en est déduite.')
lines += ['', 'Le raccourci `Nouveau dossier (2).lnk` désigne `C:\\L16B\\Nouveau dossier` et mémorise une création de cible le 28 octobre. Son attribut de cible `0x10` confirme qu’il s’agit d’un **répertoire**, pas d’un fichier ; il n’est pas compté parmi les 1 559 chemins. Les autres cibles de répertoires sont conservées dans le JSON.','',
 '## Méthode, portée et limites','',
 '- Croisement des **1 558 fichiers de l’inventaire L16B** avec leurs enregistrements MFT SI/FN et leurs inodes. Les dates sont converties depuis les UTC des extractions vers **Europe/Paris** ; le 28/10/2024, le décalage est UTC+1.',
 '- Lecture de **'+str(scanned)+' enregistrements sélectionnés lors du scan complet de la MFT** : toutes les entrées non allouées et les objets de corbeille retenus dans ce scan sont examinés pour les chemins L16B. Les alias courts DOS ne sont pas comptés comme des fichiers supplémentaires.',
 '- Croisement avec les métadonnées `$I`, les contenus `$R` récupérés, les Jump Lists, les raccourcis Recent, PrintService et une extraction indépendante des événements Windows. Les timestamps de la cible mémorisés dans un LNK ne sont pas assimilés à la date d’utilisation du raccourci.',
 '- **Une création FN du 28 octobre étaye le rattachement du chemin à cette journée ; elle ne certifie pas à elle seule l’immutabilité de ses octets depuis 2024.** Les dates SI peuvent être conservées d’une copie source. Les traces Windows ne sont pas des signatures inviolables ni un journal historique exhaustif.',
 '- **'+str(summary['current_FN_28_SI_modification_later'])+' fichiers de classe A** ont une modification SI postérieure au 28/10/2024. L’ensemble des champs SI/FN est conservé dans les listes pour permettre leur examen.',
 '- Le PST `dmmconseils93300@hotmail.com.pst` est un exemple connu de distinction entre présence du chemin et identité du contenu : il porte des traces du 28 octobre, mais son SHA-512 courant diverge du CSV d’inventaire. Le PST DMM et le ZIP Takeout concordent avec leurs SHA-512 inventoriés ; voir le [rapport des correspondances et de l’intégrité](../correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md).',
 '- Les noms disparus dont les entrées ont été réutilisées, les chemins dont les parents ne peuvent plus être reconstitués et les anciennes versions écrasées peuvent ne laisser aucune trace exploitable. **La liste couvre toutes les traces retenues dans les sources examinées ; elle ne garantit pas tous les fichiers ayant historiquement existé.**',
 '- Le périmètre est celui des fichiers de `C:\\L16B`, pas celui de chaque message contenu dans un PST ni de chaque membre interne d’une archive. Les flux NTFS nommés ne sont pas comptés comme des fichiers supplémentaires.',
 '- Le document de gestion de mots de passe et le ZIP Drive récupérés sous `C:\\Users\\fintm\\Downloads` ne sont pas ajoutés à L16B par simple rapprochement de contenu avec ses 93 fichiers GDRIVE.',
 '- Ce relevé n’établit pas, à lui seul, la composition du jeu définitivement saisi ou le contenu de l’archive emportée. Aucun contenu de document, message ou mot de passe n’est reproduit.','',
 '## Sources et reproductibilité','']
for p in source_paths:
 lines.append('- ['+str(p.relative_to(ROOT))+']('+os.path.relpath(p,OUT)+').')
lines += ['', '- [Script de production](generer_inventaire.py).', '- [Empreintes des sources et des livrables](empreintes-provenance.json).','']
with (OUT/'rapport-inventaire-L16B-20241028.md').open('x') as f:f.write('\n'.join(lines))
# Verify machine-readable and text output counts and partition; no source evidence is edited.
with (OUT/'fichiers-rattaches-au-28oct2024.csv').open(encoding='utf-8-sig',newline='') as f:
 exported=list(csv.DictReader(f,delimiter=';'));assert len(exported)==1559 and len({canon(x['Chemin complet']) for x in exported})==1559
assert (OUT/'liste-chemins-28oct2024.txt').read_text().splitlines()==[x['path'] for x in main]
provenance={'created_utc':datetime.now(timezone.utc).isoformat(),'sources':[{'path':str(p.relative_to(ROOT)),'size':p.stat().st_size,'sha256':sha(p)} for p in source_paths],'outputs':[]}
for p in sorted(OUT.iterdir()):
 if p.is_file():provenance['outputs'].append({'file':p.name,'size':p.stat().st_size,'sha256':sha(p)})
with (OUT/'empreintes-provenance.json').open('x') as f:json.dump(provenance,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('Rapport et listes : '+str(OUT))
