"""Bilan après terminaison du balayage et conservation des empreintes."""
import collections
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess

P=Path('/media/shared/codeProjects/DMMConseils')
B=P/'inventaire-DNEF/travaux-techniques/recuperation-archives-20261116'
S=B/'prive/balayage-v3'
summary=json.loads((S/'synthese.json').read_text())
metadata=json.loads((B/'prive/metadata/synthese.json').read_text())
candidates=json.loads((B/'prive/metadata/candidats.json').read_text())
references=json.loads((B/'prive/references/raccourcis.json').read_text())
geometry=json.loads((S/'geometrie.json').read_text())
logical=json.loads((S/'fichiers-logiques.json').read_text())
vss=json.loads((B/'prive/vss/resultats.json').read_text())
vss_names=json.loads((B/'prive/vss/qualification-noms.json').read_text())
shell_items=json.loads((B/'prive/contextes-etendus/shell-items-v2.json').read_text())
mft_names=json.loads((B/'prive/mft-noms-complets/resultats.json').read_text())
assert mft_names['sha256']=='4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b'
assert all(n['name'].lower().endswith('.lnk') for row in mft_names['records'] for n in row['names'])
zip_comparison=json.loads((B/'prive/comparaison-zip-L16B-finale/resultats.json').read_text())
generic_zip=json.loads((B/'prive/qualification-zip-generique/resultats.json').read_text())
assert zip_comparison['scan_complete'] and zip_comparison['known_L16B_files']==1558
assert len(zip_comparison['matching_directories'])==1
assert generic_zip['source_start']==zip_comparison['matching_directories'][0]['start']
assert generic_zip['crc_check_bad_member'] is None and not generic_zip['matches_recorded_archive_size']
assert all(not y['identical'] for x in generic_zip['member_matches'] for y in x['L16B_files'])
assert not vss.get('error')
assert len(vss['stores'])==1 and not vss['stores'][0].get('error')
assert all(n['name'].lower().endswith('.lnk') for row in vss_names for n in row['names'])
assert summary['free_bytes_scanned']==geometry['free_bytes']
assert summary['free_runs_scanned']==geometry['free_runs']
assert not summary['errors'], 'Des erreurs de lecture ou de validation nécessitent une revue.'
assert next(x['sha256'] for x in logical if x['source'].endswith('/$MFT'))=='4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b'
assert summary['total_bytes_scanned']==summary['free_bytes_scanned']+sum(x['bytes'] for x in logical)
occurrences=[json.loads(l) for l in (S/'occurrences.jsonl').read_text().splitlines()]
zips=[json.loads(l) for l in (S/'zip-candidats.jsonl').read_text().splitlines()]
by_scope=collections.Counter(x['source_scope'] for x in occurrences)
interesting_zips=[x for x in zips if x['interesting_names'] or x['matches_recorded_archive_size']]
if summary['archives_candidates_saved'] or interesting_zips:
    raise RuntimeError('Des candidats existent : les examiner avant de conclure à une absence de récupération.')
checks=[]
for x in references:
    if x.get('missing'):continue
    p=Path(x['copy']);actual=hashlib.sha256(p.read_bytes()).hexdigest();assert actual==x['sha256'];checks.append({'file':str(p),'sha256':actual,'ok':True})
hours=summary['elapsed_seconds']/3600
scope_table='\n'.join(f"| `{x['source']}` | {x['bytes']:,} | `{x['sha256']}` |" for x in logical)
occ_table='\n'.join(f'| {k} | {v} |' for k,v in sorted(by_scope.items())) or '| Aucun | 0 |'
body=f'''# Recherche de récupération des fichiers de saisie dans OP-01

**Mission SADEDINE-2026 — 16 novembre 2026.** Recherche de `Archive_saddedine.zip` et `Rejets_saddedine.txt`, avec recherche complémentaire de `Inventaire_saddedine.csv`, dans l’image du disque interne d’OP-01.

Source : segments EWF `OP01.E01` à `OP01.E74`, sous `/media/shared/forensic/SADEDINE-2026/OP-01/` dans SIFT. Les recherches portent sur le volume NTFS déchiffré présenté en lecture seule sous `/mnt/dislocker/dislocker-file`, monté sous `/mnt/windows`.

## Résultat

**Aucun fichier correspondant à l’archive ou au fichier de rejets n’a été récupéré par cette recherche.** Ce résultat dépasse la recherche des seuls noms : il comprend le contrôle des candidats supprimés, de la corbeille, des fichiers mémoire et le balayage de tous les clusters NTFS actuellement non alloués.

Les traces conservées désignent les cibles `E:\\saddedine\\Archive_saddedine.zip`, `E:\\saddedine\\Rejets_saddedine.txt` et `E:\\saddedine\\Inventaire_saddedine.csv`, sur un support externe. Leur présence passée comme fichiers complets sur le volume interne `C:` n’est pas établie. L’absence de récupération ne prouve pas qu’ils n’y ont jamais existé.

**Le CSV n’a pas non plus été récupéré dans ces résidus.** Le CSV fourni séparément par la cliente reste une pièce reçue ; il n’est pas présenté comme une extraction de l’image.

## Taille des cibles et portée des raccourcis

Les copies des trois raccourcis ont été conservées et analysées. Le champ de taille de cible a été relu directement à l’offset 52 de l’en-tête Shell Link, indépendamment des anciens exports Jump Lists :

| Cible externe | Taille mémorisée |
| --- | --- |
| `Archive_saddedine.zip` | **3 525 227 798 octets**, environ 3,53 Go décimaux |
| `Rejets_saddedine.txt` | **0 octet** |
| `Inventaire_saddedine.csv` | **527 208 octets** |

La taille nulle du fichier de rejets est compatible avec un fichier vide au moment représenté par le raccourci. **Elle ne certifie pas son contenu définitif et ne prouve pas l’absence de fichiers écartés.** Aucun fichier vide n’a été créé artificiellement puis présenté comme une récupération : une empreinte de contenu vide ne permettrait pas de l’authentifier comme la cible historique.

## Recherche parmi les fichiers supprimés

Une nouvelle recherche des trois noms a été effectuée sur les **{mft_names['bytes_scanned']:,} octets de toute la MFT courante**, sans se limiter aux enregistrements supprimés. Elle ne retrouve que les trois raccourcis `.lnk` actifs et leurs noms courts. Aucun enregistrement du ZIP, du TXT ou du CSV cible n’est identifié par son nom.

Le recensement complet déjà conservé contient **{metadata['rows']:,} enregistrements**, comprenant les entrées MFT non allouées et des entrées de corbeille. Son utilisation est corroborée par la nouvelle lecture intégrale de `$MFT`, dont le SHA-256 est identique à celui des analyses antérieures.

La recherche a porté sur les variantes de noms, la taille exacte de l’archive, les tailles voisines de 3 à 4 Gio, la taille connue du CSV et tous les noms ZIP supprimés de ce recensement. **{metadata['selected']} candidats** ont été retenus : 17 noms ZIP supprimés et un autre fichier de taille voisine. Aucun n’a le nom cible ni la taille exacte de l’archive. La recherche dans les métadonnées de corbeille déjà extraites ne fournit aucune entrée cible.

Les débuts et fins de tous les candidats ont été effectivement lus, sans erreur. Aucun ne présente un début ZIP ou une fin de répertoire ZIP cohérente. Le seul candidat voisin de 3–4 Gio est un fichier de `System Volume Information`, avec début et fin nuls, pas une archive identifiée. Plusieurs anciennes allocations de fichiers supprimés sont actuellement attribuées à d’autres fichiers : leurs octets actuels ne peuvent pas être assimilés automatiquement à leurs anciens contenus.

La campagne antérieure de récupération limitait les lectures à 64 Mio par candidat. Cette limite antérieure ne suffit pas à trancher pour une archive de 3,53 Go ; la présente recherche ajoute donc une approche par structures ZIP et ZIP64 dans les résidus, indépendante du nom et de cette ancienne limite.

## Clichés VSS

Le catalogue contient deux clichés datés du 2 octobre 2026. La lecture ordinaire échoue sur l’en-tête du second cliché. Une **vue dérivée en mémoire** a été construite pour exclure ses deux entrées de catalogue ; les octets sources restent inchangés et les substitutions de cette vue sont consignées avec les blocs originaux. Cette méthode permet de lire le premier cliché, identifié par `b764a044-a79c-11f1-8dc9-50e08563415f`.

La MFT du cliché a été extraite intégralement : **{vss['stores'][0]['mft_size']:,} octets**, SHA-256 `{vss['stores'][0]['mft_sha256']}`. La recherche des trois noms y fournit trois enregistrements. Une contre-lecture des attributs NTFS `$FILE_NAME`, après contrôle des corrections de secteurs, établit qu’il s’agit exclusivement de `Rejets_saddedine.lnk`, `Inventaire_saddedine.lnk` et `Archive_saddedine.lnk` (ainsi que leurs noms courts). **Aucun des trois fichiers cibles n’est retrouvé par son nom dans cette MFT.**

Ce résultat concerne le premier cliché accessible dans cette vue dérivée. Il ne constitue pas une garantie d’intégrité ou de reconstruction exhaustive des clichés d’origine après exclusion d’une partie du catalogue. Le second cliché n’est pas déclaré exploitable ; les données libres propres aux clichés n’ont pas fait l’objet d’une reconstruction générale. Un cliché de 2026 ne restitue pas nécessairement des fichiers supprimés depuis 2024.

## Lecture des résidus

L’image a été montée avec EWF/loop en lecture seule, Dislocker `-r`, puis NTFS `ro,norecover`. Aucun rejeu de journal ni écriture sur la source n’a été effectué.

Le bitmap d’allocation NTFS correspond à l’empreinte déjà conservée :

```text
{geometry['bitmap_sha256']}
```

Le balayage a lu **{summary['free_bytes_scanned']:,} octets non alloués**, répartis sur **{summary['free_runs_scanned']:,} intervalles**, soit environ {summary['free_bytes_scanned']/1024**3:.2f} Gio. Il a également lu intégralement les fichiers suivants :

| Source logique | Octets lus | SHA-256 |
| --- | --- | --- |
{scope_table}

Les motifs recherchés comprennent les trois noms complets, `IPHONE13_MINI`, `Dossier bourarach`, `inventaire de saisie` et `nombre de fichiers saisis`, en UTF-8 et UTF-16LE, ainsi que les fins de structures ZIP et ZIP64. Les signatures ZIP ont fait l’objet d’un contrôle de cohérence des champs, du répertoire central et des noms de membres ; une simple suite d’octets `PK` n’est pas considérée comme une archive récupérée.

Le moteur compilé a été vérifié contre une recherche littérale de référence sur des données synthétiques, y compris casse, UTF-16 et motifs imbriqués. Les calculs de début et fin ZIP/ZIP64 ont été comparés à `zipfile` sur des archives synthétiques avec préfixe et commentaire. Deux premières passes partielles ont été conservées mais ne sont pas utilisées pour annoncer une couverture complète : la première a été remplacée pour des raisons de débit, la deuxième pour inclure la validation ZIP64. Seule la passe `balayage-v3` fournit le bilan final.

Le total lu par cette passe est de **{summary['total_bytes_scanned']:,} octets**, fichiers logiques et clusters libres réunis. Des occurrences textuelles ont été conservées dans les catégories suivantes ; **elles sont des fragments ou références à qualifier, pas les fichiers cibles récupérés** :

| Zone | Occurrences textuelles |
| --- | --- |
{occ_table}

Aucune structure validée ne fournit un candidat à la taille enregistrée de l’archive ou un répertoire central pertinent permettant sa reconstruction. Les fragments enregistrés et les détections brutes restent disponibles pour contre-lecture.

Les **{zip_comparison['zip_directories_compared']} répertoires centraux ZIP cohérents** ont en outre été comparés aux noms des **1 558 fichiers actuellement présents sous `C:\\L16B`**, soit {zip_comparison['known_distinct_names']} noms distincts. La normalisation Unicode et de la casse fournit une seule correspondance nominale générique : cinq membres `loading.gif` dans un conteneur de composants Sage de **28 760 933 octets**, comportant 2 687 membres. Ce conteneur, entièrement situé dans des clusters actuellement libres, est lisible et son contrôle CRC réussit. **Les cinq GIF ont des contenus différents du fichier de même nom dans L16B**, comparaison directe et SHA-256 à l’appui ; aucun nom des PDF Mini n’y figure. Ce résultat n’identifie pas l’archive cible de 3,53 Go.

Ce contrôle ne dépend pas de la présence du nom `Archive_saddedine.zip` dans les résidus. Il porte sur les répertoires centraux demeurés cohérents, sans garantir la lecture de fragments ZIP incomplets. Un répertoire central cohérent ne vaut pas, à lui seul, validation CRC de tous les membres de chacune des 982 structures.

Des fenêtres supplémentaires de 64 Kio ont été conservées autour des premières mentions physiques des trois cibles. Deux occurrences de `Archive_saddedine.zip` y correspondent à **deux copies identiques d’un Shell Item de 128 octets** : structure descriptive Windows comportant le nom et la taille de 3 525 227 798 octets. Leur empreinte est `{shell_items['items'][0]['sha256']}`. Ces structures confortent l’identification de la cible historique, mais **ne contiennent pas les données compressées de l’archive**. D’autres fragments associent les noms des cibles à leurs noms `.lnk`, sans fournir le contenu du ZIP, du TXT ou du CSV.

## Limites et conclusion utilisable

Cette recherche ne garantit pas la récupération d’une archive fragmentée dont les chaînes d’allocation ont disparu, d’un conteneur chiffré non reconnu, ni de données écrasées ou absentes de l’image. Les espaces non alloués ont été intégralement parcourus avec les motifs indiqués ; tous les contenus du volume ne sont pas pour autant décodés sémantiquement. Les formats de compression mémoire Windows n’ont pas fait l’objet d’une décompression générale de l’hibernation et du fichier d’échange.

Le balayage vise les clusters libres du volume NTFS interne, complétés par les fichiers logiques indiqués. Il n’inclut pas un balayage général du slack interne aux fichiers alloués, de tous les fichiers conteneurs alloués, ni de l’espace situé hors de ce volume. Un éventuel fichier vide ne possède aucune signature de contenu permettant de le retrouver et de l’attribuer à la cible.

**Conclusion : l’image d’OP-01 ne fournit actuellement pas de copie récupérée de `Archive_saddedine.zip` ou de `Rejets_saddedine.txt`.** Les raccourcis conservés permettent de documenter leurs chemins externes et leurs tailles mémorisées, sans restituer leur contenu. Le support externe de l’administration, son image ou une copie conservée de ces fichiers demeure la source la plus directe pour les obtenir.

## Pièces techniques

- [Candidats supprimés et lectures](../travaux-techniques/recuperation-archives-20261116/prive/metadata/candidats.json).
- [Recherche des noms dans la MFT courante complète](../travaux-techniques/recuperation-archives-20261116/prive/mft-noms-complets/resultats.json).
- [Raccourcis et tailles décodées](../travaux-techniques/recuperation-archives-20261116/prive/references/raccourcis.json).
- [Lecture VSS et vue dérivée](../travaux-techniques/recuperation-archives-20261116/prive/vss/resultats.json), [contre-lecture des noms NTFS](../travaux-techniques/recuperation-archives-20261116/prive/vss/qualification-noms.json).
- [Contextes étendus](../travaux-techniques/recuperation-archives-20261116/prive/contextes-etendus/resultats.json), [Shell Items qualifiés](../travaux-techniques/recuperation-archives-20261116/prive/contextes-etendus/shell-items-v2.json). La première sortie `shell-items.json` est conservée pour traçabilité ; son ordre de décodage date/heure DOS est corrigé dans `shell-items-v2.json`, seule version retenue.
- [Comparaison aux 1 558 fichiers L16B](../travaux-techniques/recuperation-archives-20261116/prive/comparaison-zip-L16B-finale/resultats.json).
- [Qualification de la correspondance générique loading.gif](../travaux-techniques/recuperation-archives-20261116/prive/qualification-zip-generique/resultats.json).
- [Bilan du balayage complet](../travaux-techniques/recuperation-archives-20261116/prive/balayage-v3/synthese.json), [occurrences et fragments](../travaux-techniques/recuperation-archives-20261116/prive/balayage-v3/occurrences.jsonl), [structures ZIP contrôlées](../travaux-techniques/recuperation-archives-20261116/prive/balayage-v3/zip-candidats.jsonl).
- [Scripts](../travaux-techniques/recuperation-archives-20261116/scripts/), [contrôle final](../travaux-techniques/recuperation-archives-20261116/verification-finale.json) et [empreintes](../travaux-techniques/recuperation-archives-20261116/manifest-sha256.txt).
'''
report=P/'inventaire-DNEF/rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md'
with report.open('x') as f:f.write(body)
verification={'completed_scan':True,'bytes_accounting_ok':True,'mft_sha256_matches_previous':True,'reference_copy_checks':checks,'raw_zip_candidates_review_required':bool(interesting_zips),'archives_saved':summary['archives_candidates_saved'],'read_errors':summary['errors'],'elapsed_hours':hours,'vss_derived_first_store_only':True,'vss_target_name_hits_are_lnk':True,'shell_items_are_metadata_not_content':True}
with (B/'verification-finale.json').open('x') as f:json.dump(verification,f,ensure_ascii=False,indent=2)
lines=[]
for p in sorted(B.rglob('*')):
 if not p.is_file() or p.name=='manifest-sha256.txt':continue
 with p.open('rb') as f:h=hashlib.file_digest(f,'sha256').hexdigest()
 lines.append(h+'  '+str(p.relative_to(P)))
lines.append(hashlib.sha256(report.read_bytes()).hexdigest()+'  '+str(report.relative_to(P)))
for relative in ['telephones/analyse-TP-03.md','RAPPORT-FINAL-SADEDINE-2026.md','inventaire-DNEF/README.md']:
 p=P/relative;lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+relative)
with (B/'manifest-sha256.txt').open('x') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps({'report':str(report),'free_bytes_scanned':summary['free_bytes_scanned'],'scope_counts':dict(by_scope),'valid_zip_directories':len(zips),'manifest_entries':len(lines)},ensure_ascii=False))
