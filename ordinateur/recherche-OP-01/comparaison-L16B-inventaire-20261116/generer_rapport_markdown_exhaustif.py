#!/usr/bin/env python3
"""Rapport Markdown exhaustif à partir des contrôles SHA-512 déjà réalisés."""
from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import csv,json,hashlib,collections,re
BASE=Path('/mnt/data/codeProjects/DMMConseils/ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116')
ROOT=BASE.parents[2]
SOURCE=BASE/'comparaison-SHA512-tous-les-fichiers.csv'
RESULTS=BASE/'resultats-comparaison-L16B-inventaire.json'
INVENTORY=ROOT/'inventaire-DNEF/documents-recus/Inventaire_saddedine.csv'
TARGET=BASE/'rapport-comparaison-SHA512-exhaustive-1555-fichiers.md'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inline(s):
 fence='`'*(max([len(x) for x in re.findall(r'`+',s)],default=0)+1)
 return fence+s+fence
with SOURCE.open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f,delimiter=';'))
with INVENTORY.open(encoding='utf-8-sig',newline='') as f:
 expected={x[0]:x[4].lower() for x in csv.reader(f,delimiter=';') if x and x[0].lower().startswith('c:\\')}
result=json.loads(RESULTS.read_text())
assert len(rows)==len(expected)==1555
assert {r['Chemin inventorié'] for r in rows}==set(expected)
assert sha(INVENTORY)==result['inventory_sha256']
for i,r in enumerate(rows,1):
 assert r['SHA-512 inventaire']==expected[r['Chemin inventorié']]
 assert r['Présent dans L16B']=='Oui' and not r['Erreur éventuelle']
 for k in ['SHA-512 inventaire','SHA-512 calculé']:assert re.fullmatch('[a-f0-9]{128}',r[k])
 assert r['Résultat SHA-512']==('IDENTIQUE' if r['SHA-512 inventaire']==r['SHA-512 calculé'] else 'DIVERGENT')
 r['reference']=f'F{i:04}'
counts=collections.Counter(x['Résultat SHA-512'] for x in rows)
assert counts=={'IDENTIQUE':1552,'DIVERGENT':3}
groups=collections.OrderedDict()
for r in rows:groups.setdefault(r['Chemin inventorié'].split('\\')[2],[]).append(r)
anchors={name:'ensemble-'+str(i) for i,name in enumerate(groups,1)}
def local(s):return datetime.fromisoformat(s).astimezone(ZoneInfo('Europe/Paris')).strftime('%d/%m/%Y à %H:%M:%S %z')
lines=['# Rapport exhaustif de comparaison SHA-512 — 1 555 fichiers de L16B','',
 '**OP-01 — 16 novembre 2026.** Ce document contient la comparaison individuelle de **toutes les empreintes SHA-512 du CSV d’inventaire fourni**, avec les fichiers correspondants du dossier `C:\\L16B` dans l’image disque analysée.','',
 '## Sources comparées et portée','',
 'L’[inventaire de saisie fourni](../../../inventaire-DNEF/documents-recus/Inventaire_saddedine.csv), daté du **28 octobre 2024**, décrit 1 555 fichiers par leur chemin Windows, leurs dates et une empreinte **SHA-512**. `C:\\L16B` est le dossier de regroupement laissé sur OP-01 lors des opérations ; les fichiers comparés sont ceux présents dans l’**image acquise en 2026**.','',
 'Les résultats repris ici proviennent de la lecture intégrale des fichiers sur SIFT, avec montage NTFS et boucle EWF en lecture seule, du **'+local(result['started_utc'])+'** au **'+local(result['finished_utc'])+'**. Le [rapport de synthèse](rapport-comparaison-L16B-inventaire.md) explique le contexte, les écarts de chemins et les limites.','',
 '**IDENTIQUE** signifie que le SHA-512 du fichier de l’image est égal à celui du CSV. **DIVERGENT** signifie que le chemin est présent, mais que le contenu actuel ne correspond pas à l’empreinte inventoriée. Cette différence ne détermine ni la date, ni la cause, ni l’auteur d’une modification. La concordance avec le CSV fourni ne démontre pas une lecture humaine ou une utilisation ultérieure du fichier.','',
 '## Résultats globaux','',
 '| Contrôle | Résultat |','|---|---:|',
 '| Fichiers de l’inventaire comparés | **1 555** |',
 '| Chemins retrouvés dans L16B | **1 555** |',
 '| Chemins absents de L16B | **0** |',
 '| SHA-512 identiques | **1 552** |',
 '| SHA-512 divergents | **3** |',
 '| Erreurs de lecture | **0** |',
 '| Octets lus pour les calculs | **'+f"{result['summary']['total_bytes_hashed']:,}".replace(',',' ')+'** |','',
 'Chaque fichier est détaillé plus bas avec sa référence, sa ligne dans le CSV d’origine, son chemin, sa taille et **les deux SHA-512 complets**.','',
 '## Les trois divergences','',
 '| Référence | Ligne du CSV d’origine | Fichier | Résultat |','|---|---:|---|---|']
for r in rows:
 if r['Résultat SHA-512']=='DIVERGENT':
  lines.append('| ['+r['reference']+'](#'+r['reference'].lower()+') | '+r['Ligne CSV']+' | '+inline(r['Chemin inventorié'])+' | **DIVERGENT** |')
lines += ['', 'Les divergences du raccourci USB2 et du PDF FACT 2018 SUITE ont été confirmées indépendamment avec `sha512sum` sur SIFT. Le PST 93300 avait déjà fait l’objet d’une confirmation indépendante ; la nouvelle empreinte est identique à celle de ce contrôle. Voir les [confirmations conservées](confirmations-independantes.json).','',
 '## Accès aux ensembles','',
 '| Ensemble | Fichiers | Identiques | Divergents |','|---|---:|---:|---:|']
for name,rs in groups.items():
 c=collections.Counter(r['Résultat SHA-512'] for r in rs)
 lines.append('| ['+name+'](#'+anchors[name]+') | '+str(len(rs))+' | '+str(c['IDENTIQUE'])+' | '+str(c['DIVERGENT'])+' |')
lines += ['', '## Comparaison exhaustive, fichier par fichier','',
 'L’ordre suit celui du CSV. Les numéros de ligne renvoient au **CSV d’origine**, dont les six premières lignes sont des informations d’en-tête. Les deux valeurs de chaque bloc sont reproduites intégralement, sans troncature.','']
for name,rs in groups.items():
 lines += ['<a id="'+anchors[name]+'"></a>','', '### '+name+' — '+str(len(rs))+' fichiers','']
 for r in rs:
  lines += ['<a id="'+r['reference'].lower()+'"></a>','',
   '#### '+r['reference']+' — '+inline(r['Chemin inventorié']),'',
   '**'+r['Résultat SHA-512']+'** · Présent dans L16B : **oui** · Ligne du CSV : **'+r['Ligne CSV']+'** · Taille : **'+f"{int(r['Taille octets']):,}".replace(',',' ')+' octets** · Entrée MFT : **'+r['Inode']+'**.','',
   '```text',
   'SHA-512 inventaire : '+r['SHA-512 inventaire'],
   'SHA-512 image     : '+r['SHA-512 calculé'],
   '```','']
lines += ['## Références et traçabilité','',
 '- [Inventaire CSV d’origine](../../../inventaire-DNEF/documents-recus/Inventaire_saddedine.csv).',
 '- [Comparaison exhaustive au format CSV](comparaison-SHA512-tous-les-fichiers.csv).',
 '- [Résultats structurés et contrôle du montage en lecture seule](resultats-comparaison-L16B-inventaire.json).',
 '- [Journal des 1 555 calculs](comparaison-SHA512-complete.jsonl).',
 '- [Rapport de synthèse et écarts de chemins](rapport-comparaison-L16B-inventaire.md).',
 '- [Confirmations indépendantes](confirmations-independantes.json).',
 '- [Provenance et empreinte de ce rapport](rapport-comparaison-SHA512-exhaustive-1555-fichiers.provenance.json).','',
 'SHA-256 du CSV d’inventaire utilisé :','','```text',result['inventory_sha256'],'```','',
 'Les tailles, inodes et dates de modification des fichiers sont restés identiques pendant leur lecture. Le CSV conserve la même empreinte avant et après le contrôle. La comparaison porte sur les fichiers inventoriés ; les fichiers supplémentaires non inscrits au CSV sont traités dans le rapport de synthèse.','']
text='\n'.join(lines)
assert len(re.findall(r'^#### F\d{4} — ',text,re.M))==1555
assert len(re.findall(r'^SHA-512 inventaire : [a-f0-9]{128}$',text,re.M))==1555
assert len(re.findall(r'^SHA-512 image     : [a-f0-9]{128}$',text,re.M))==1555
for r in rows:
 assert text.count('id="'+r['reference'].lower()+'"')==1
 assert r['SHA-512 inventaire'] in text and r['SHA-512 calculé'] in text
with TARGET.open('x') as f:f.write(text)
provenance={'created_utc':datetime.now(timezone.utc).isoformat(),'report':TARGET.name,'report_sha256':sha(TARGET),'comparison_count':len(rows),'results':dict(counts),'sources':[{'path':str(p),'sha256':sha(p)} for p in [INVENTORY,SOURCE,RESULTS]],'builder_sha256':sha(Path(__file__))}
with (BASE/'rapport-comparaison-SHA512-exhaustive-1555-fichiers.provenance.json').open('x') as f:json.dump(provenance,f,ensure_ascii=False,indent=2);f.write('\n')
print(TARGET)
print('1 555 fichiers ; 3 110 SHA-512 complets ; 1 552 concordances et 3 divergences ; tous les fichiers présents.')
print('Taille du rapport : '+str(TARGET.stat().st_size)+' octets')
