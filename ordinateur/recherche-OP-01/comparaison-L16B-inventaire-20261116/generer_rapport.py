from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import json,hashlib,csv,collections
ROOT=Path('/mnt/data/codeProjects/DMMConseils')
BASE=ROOT/'ordinateur/recherche-OP-01'
OUT=BASE/'comparaison-L16B-inventaire-20261116'
DATA=OUT/'resultats-comparaison-L16B-inventaire.json'
r=json.loads(DATA.read_text())
h=json.loads((BASE/'inventaire-L16B-20241028-20261116/inventaire-detaille.json').read_text())
recover=json.loads(Path('/tmp/comparaison-recupere-l16b-SHA512.json').read_text())
summary=r['summary'];assert summary['hash_status_counts']=={'IDENTIQUE':1552,'DIVERGENT':3}
assert summary['inventory_paths_absent_from_L16B']==0
assert len(r['different_contents'])==3 and len(r['current_only'])==3 and len(r['historical_28_paths_absent_from_CSV'])==4
assert all(x.get('stat_unchanged') for x in r['comparisons'])
old3=json.loads((BASE/'extraction-messageries-20261116/comparaison-inventaire-SHA512-20261116.json').read_text())
current_byname={Path(x['path'].replace('\\','/')).name:x for x in r['comparisons']}
for x in old3['entries']:assert current_byname[Path(x['file']).name]['sha512_computed']==x['sha512_computed']
independent={
 'C:\\L16B\\LOCAL\\cle usb\\USB2 (D) - Raccourci.lnk':'54da56d32e0f1a700fa3c2c20ff918884e9054cfcb74d45b6c1aff1eea4a9660158391872994e1352d1e66f33e77d6bdc1da1c90a19835db7ec59a3ed51948a3',
 'C:\\L16B\\LOCAL\\FACT 2018 SUITE.pdf':'dd4705eb6ca387aeef77eae149b758c11bfbc7e7d97d1c235adb14c17fd3df31e01a996716cfc91f06022f381fadaf666039f9b3fb60c5775329f082ccd95084',
 'C:\\L16B\\MESSAGERIES\\dmmconseils93300@hotmail.com.pst':'1949987f20fced4a2b0a3c6c4000e5afb8a54e5ec8b08c667ed5397feab60ad18b87fe0a78348ee4b992306cfd8773eb53a3560e6ba82bd6d86e79523ec03361',
}
for x in r['different_contents']:assert independent[x['path']]==x['sha512_computed']
with (OUT/'confirmations-independantes.json').open('x') as f:json.dump({'sha512sum_confirmed':independent,'notes':'Deux nouveaux écarts confirmés avec sha512sum sur SIFT ; le PST 93300 avait déjà été confirmé indépendamment et la nouvelle valeur est identique.','recovered_history_files':recover},f,ensure_ascii=False,indent=2);f.write('\n')
canon=lambda s:s.replace('/','\\').rstrip('\\').casefold()
byhist={canon(x['path']):x for x in h['files_28']+h['excluded_later_or_uncertain']}
byrecover={x['path']:x for x in recover}
def paris(s):return datetime.fromisoformat(s).astimezone(ZoneInfo('Europe/Paris')).isoformat() if s else ''
def code(s):return '`'+s+'`'
def clean(s):return str(s).replace('|','&#124;').replace('\n',' ')
# Compact CSV of path differences, kept separate from the exhaustive content comparison.
with (OUT/'ecarts-de-chemins.csv').open('x',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['Chemin','Type d’écart','Datation Windows','Portée'])
 for x in r['current_only']:
  t=byhist[canon(x['path'])];dt=t['fn_selected']['times']['creation']
  w.writerow([x['path'],'Présent dans L16B, absent du CSV',paris(dt),'Création FN en 2026 ; pas une preuve de rejet en 2024'])
 for x in r['historical_28_paths_absent_from_CSV']:
  w.writerow([x['path'],'Ancien chemin du 28/10/2024, absent du CSV',paris(x['deletion_utc']) if x['deletion_utc'] else '2024-10-28 15:23–15:28 Paris','Suppression ou chemin intermédiaire référencé ; décision de filtrage non démontrée'])
lines=['# Comparaison exhaustive de L16B et de l’inventaire DNEF','',
 '**OP-01 — 16 novembre 2026.** Comparaison des chemins dans les deux sens, puis lecture et calcul SHA-512 de chaque fichier inventorié dans l’image montée en lecture seule sur SIFT.','',
 '## Réponse','',
 '**Aucun fichier du CSV n’est absent de L16B par son chemin : les 1 555 chemins de l’inventaire sont tous présents dans l’image.** Ces chemins correspondent exactement au groupe des 1 555 fichiers actuels portant une création FN du 28/10/2024 dans le relevé Windows précédent.','',
 '**L16B contient trois fichiers supplémentaires**, dont les créations FN sont datées de 2026. Les traces Windows du 28/10/2024 identifient en outre **quatre anciens chemins** absents du CSV. **Ces écarts ne constituent pas une liste officielle de fichiers écartés lors du filtrage.**','',
 '**Sur les 1 555 contenus contrôlés, 1 552 SHA-512 sont identiques au CSV et 3 divergent.** Les trois fichiers divergents existent au chemin inventorié, mais leurs octets actuels ne correspondent pas à l’empreinte qui figure dans cet inventaire.','',
 '| Contrôle | Résultat |','|---|---:|',
 '| Lignes de fichiers dans le CSV / chemins distincts | **1 555 / 1 555** |',
 '| Fichiers actuellement présents sous L16B dans l’image | **1 558** |',
 '| Chemins communs au CSV et à L16B | **1 555** |',
 '| Chemins du CSV absents de L16B | **0** |',
 '| Fichiers actuels de L16B absents du CSV | **3** |',
 '| Anciens chemins du 28/10/2024 absents du CSV | **4** |',
 '| SHA-512 identiques / divergents / erreurs de lecture | **1 552 / 3 / 0** |','',
 '## 1. Fichiers actuellement dans L16B mais absents du CSV','',
 '| Chemin | Taille (octets) | Création FN, heure de Paris |','|---|---:|---|']
for x in r['current_only']:
 t=byhist[canon(x['path'])]
 lines.append('| '+code(x['path'])+' | '+str(x['size'])+' | '+paris(t['fn_selected']['times']['creation'])+' |')
lines += ['', '**Ces trois chemins portent des créations FN en 2026.** Leur absence d’un inventaire daté du 28 octobre 2024 ne permet donc pas de les présenter comme des fichiers rejetés en 2024. Les deux ZIP GDRIVE sont distincts du dossier développé GDRIVE, dont les 93 fichiers figurent dans le CSV.','',
 '## 2. Anciens chemins du 28 octobre 2024 absents du CSV','',
 '| Ancien chemin | Trace Windows | Contenu et portée |','|---|---|---|']
for x in r['historical_28_paths_absent_from_CSV']:
 if x['category'].startswith('B'):
  rec=byrecover[x['path']];assert not rec['exact_contents_listed_elsewhere']
  text='Suppression vers la corbeille '+paris(x['deletion_utc'])
  detail='Contenu récupéré ; son SHA-512 ne correspond à aucune des 1 555 empreintes du CSV.'
 else:
  text='PrintService 307 : 205 pages à 15:23:32, 458 pages à 15:28:33 ; Jump List à 15:28:29.'
  detail='Chemin intermédiaire référencé ; contenu non récupéré séparément à cette racine.'
 lines.append('| '+code(x['path'])+' | '+text+' | '+detail+' |')
lines += ['', 'Les deux raccourcis supprimés ont un contenu binaire identique entre eux ; leurs deux chemins sont distincts. `test.pdf` est un PDF de deux factures dont le texte est repris dans le PDF Sage final, selon le contrôle déjà documenté : l’absence de ce fichier autonome dans le CSV ne prouve pas l’absence de ces factures dans les données conservées.','',
 '**Ne pas confondre** `C:\\L16B\\Sage.pdf` avec `C:\\L16B\\SAGE\\sage.pdf`. Le second figure dans le CSV et son SHA-512 est concordant. Les graphies `Sage.pdf` / `sage.pdf` à la racine sont regroupées comme un même chemin Windows ; le mécanisme exact reliant ce chemin intermédiaire au fichier du sous-dossier n’est pas établi ici.','',
 'Une suppression dans le dossier de travail, un doublon ou un changement de chemin peut expliquer un écart de liste sans correspondre à une décision de filtrage. Le fichier `Rejets_saddedine.txt` et l’archive finale n’ont pas été récupérés. **Le motif de l’absence de ces quatre chemins du CSV n’est pas déterminé.**','',
 '## 3. Fichiers inventoriés présents au chemin attendu mais de contenu divergent','',
 '| Chemin inventorié | Ligne du CSV | Taille actuelle (octets) | SHA-512 |','|---|---:|---:|---|']
for x in r['different_contents']:lines.append('| '+code(x['path'])+' | '+str(x['csv_line'])+' | '+str(x['size'])+' | **DIVERGENT** |')
lines += ['', 'Les deux nouveaux écarts, le raccourci USB2 et le PDF FACT 2018 SUITE, sont confirmés par un calcul indépendant `sha512sum` sur SIFT. Le PST 93300 avait déjà été confirmé indépendamment ; son empreinte actuelle est inchangée par rapport à ce contrôle. La date, la cause et l’auteur des différences ne sont pas déterminés par cette comparaison.','',
 '**Il n’y a donc aucun chemin manquant dans L16B, mais trois contenus actuels qui ne correspondent pas à leur version inventoriée.** Cela ne prouve pas que les versions inventoriées sont absentes de toute l’image ou d’un autre support ; elles ne sont pas retrouvées à l’identique dans les fichiers actuellement présents à ces trois chemins.','',
 '### Empreintes complètes des trois divergences','']
for x in r['different_contents']:
 lines += ['#### '+x['path'],'','Inventaire :','','```text',x['sha512_inventory'],'```','','Fichier dans l’image :','','```text',x['sha512_computed'],'```','']
lines += ['## 4. Autres traces qui ne démontrent pas un écart de 2024','',
 '- Le chemin historique `C:\\L16B\\MESSAGERIES\\misssmalika@hotmail.com\\FA0004 ET FA0005 DE LADMINISTRATION.pdf`, également absent du CSV, est connu par une création et une suppression **du 2 octobre 2026**. Il est conservé dans le relevé Windows, mais pas présenté comme un fichier de L16B du 28/10/2024.',
 '- Trois anciens chemins reconstruits à partir de parents MFT incertains (`Square44x44Logo.targetsize-24_altform-unplated.png`, `Paste.svg`, `Resize.svg`) ne sont pas retenus comme fichiers L16B établis en 2024.','',
 '## 5. Méthode et limites','',
 '- CSV fourni : `inventaire-DNEF/documents-recus/Inventaire_saddedine.csv`, **1 555 lignes de fichiers**, sans doublon de chemin. SHA-256 du CSV : `'+r['inventory_sha256']+'`.',
 '- Comparaison de tous les chemins Windows, sans tenir compte de leur casse ; les séparateurs sont harmonisés. Les chaînes de chemins du CSV sont également identiques à celles des 1 555 entrées de classe A du relevé Windows.',
 '- Inventaire direct du dossier `L16B` de l’image montée : **1 558 fichiers**. Contrôle du montage NTFS **en lecture seule** et de la boucle EWF **en lecture seule** avant tout calcul.',
 '- Lecture intégrale et SHA-512 de chacun des **1 555 fichiers inventoriés**, soit **'+str(summary['total_bytes_hashed'])+' octets**. Les tailles, inodes et dates de modification restent identiques pendant la lecture ; **aucune erreur** n’est enregistrée.',
 '- Le CSV a la même empreinte avant et après le contrôle. Les trois SHA-512 de messageries déjà contrôlés concordent avec la nouvelle passe exhaustive.',
 '- Pour les trois fichiers de corbeille du 28/10/2024, SHA-512 des copies récupérées et comparaison à toutes les empreintes du CSV : aucune correspondance exacte ailleurs dans cet inventaire.',
 '- Le rapprochement porte sur les fichiers et les empreintes de **l’inventaire fourni**. Il ne certifie pas à lui seul l’authentification du support d’origine du CSV, la composition ou la conservation actuelle de l’archive finale, ni les raisons du filtrage.','',
 '## 6. Références et livrables','',
 '- [CSV d’inventaire fourni](../../../inventaire-DNEF/documents-recus/Inventaire_saddedine.csv).',
 '- [Comparaison exhaustive des 1 555 SHA-512 — CSV filtrable](comparaison-SHA512-tous-les-fichiers.csv).',
 '- [Écarts de chemins — CSV](ecarts-de-chemins.csv).',
 '- [Résultats complets et paramètres du montage](resultats-comparaison-L16B-inventaire.json).',
 '- [Calculs individuels journalisés](comparaison-SHA512-complete.jsonl).',
 '- [Confirmations indépendantes et contenus récupérés](confirmations-independantes.json).',
 '- [Relevé des fichiers datables du 28 octobre et exclusions](../inventaire-L16B-20241028-20261116/rapport-inventaire-L16B-20241028.md).',
 '- [Rapport des correspondances et de leur concordance à l’inventaire](../correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md).',
 '- [Analyse OP-01, suppressions et PDF Sage](../../analyse-ordinateur.md).',
 '- [Recherche de récupération de l’archive finale et des rejets](../../../inventaire-DNEF/rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md).',
 '- [Script de comparaison sur SIFT](comparer_sift.py).','']
with (OUT/'rapport-comparaison-L16B-inventaire.md').open('x') as f:f.write('\n'.join(lines))
with (OUT/'generer_rapport.py').open('x') as f:f.write(Path(__file__).read_text())
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'inventory_sha256':r['inventory_sha256'],'outputs':[]}
for p in sorted(OUT.iterdir()):
 if p.is_file():manifest['outputs'].append({'file':p.name,'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
with (OUT/'empreintes-livrables.json').open('x') as f:json.dump(manifest,f,ensure_ascii=False,indent=2);f.write('\n')
print(OUT/'rapport-comparaison-L16B-inventaire.md')
print('1 555 chemins retrouvés ; 1 552 SHA-512 identiques ; 3 divergents ; 3 fichiers actuels supplémentaires et 4 anciens chemins du 28 absents du CSV.')
