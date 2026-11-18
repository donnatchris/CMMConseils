# Recherche de récupération des fichiers de saisie dans OP-01

**Mission SADEDINE-2026 — 16 novembre 2026.** Recherche de `Archive_saddedine.zip` et `Rejets_saddedine.txt`, avec recherche complémentaire de `Inventaire_saddedine.csv`, dans l’image du disque interne d’OP-01.

Source : segments EWF `OP01.E01` à `OP01.E74`, sous `/media/shared/forensic/SADEDINE-2026/OP-01/` dans SIFT. Les recherches portent sur le volume NTFS déchiffré présenté en lecture seule sous `/mnt/dislocker/dislocker-file`, monté sous `/mnt/windows`.

## Résultat

**Aucun fichier correspondant à l’archive ou au fichier de rejets n’a été récupéré par cette recherche.** Ce résultat dépasse la recherche des seuls noms : il comprend le contrôle des candidats supprimés, de la corbeille, des fichiers mémoire et le balayage de tous les clusters NTFS actuellement non alloués.

Les traces conservées désignent les cibles `E:\saddedine\Archive_saddedine.zip`, `E:\saddedine\Rejets_saddedine.txt` et `E:\saddedine\Inventaire_saddedine.csv`, sur un support externe. Leur présence passée comme fichiers complets sur le volume interne `C:` n’est pas établie. L’absence de récupération ne prouve pas qu’ils n’y ont jamais existé.

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

Une nouvelle recherche des trois noms a été effectuée sur les **1,071,120,384 octets de toute la MFT courante**, sans se limiter aux enregistrements supprimés. Elle ne retrouve que les trois raccourcis `.lnk` actifs et leurs noms courts. Aucun enregistrement du ZIP, du TXT ou du CSV cible n’est identifié par son nom.

Le recensement complet déjà conservé contient **380,566 enregistrements**, comprenant les entrées MFT non allouées et des entrées de corbeille. Son utilisation est corroborée par la nouvelle lecture intégrale de `$MFT`, dont le SHA-256 est identique à celui des analyses antérieures.

La recherche a porté sur les variantes de noms, la taille exacte de l’archive, les tailles voisines de 3 à 4 Gio, la taille connue du CSV et tous les noms ZIP supprimés de ce recensement. **18 candidats** ont été retenus : 17 noms ZIP supprimés et un autre fichier de taille voisine. Aucun n’a le nom cible ni la taille exacte de l’archive. La recherche dans les métadonnées de corbeille déjà extraites ne fournit aucune entrée cible.

Les débuts et fins de tous les candidats ont été effectivement lus, sans erreur. Aucun ne présente un début ZIP ou une fin de répertoire ZIP cohérente. Le seul candidat voisin de 3–4 Gio est un fichier de `System Volume Information`, avec début et fin nuls, pas une archive identifiée. Plusieurs anciennes allocations de fichiers supprimés sont actuellement attribuées à d’autres fichiers : leurs octets actuels ne peuvent pas être assimilés automatiquement à leurs anciens contenus.

La campagne antérieure de récupération limitait les lectures à 64 Mio par candidat. Cette limite antérieure ne suffit pas à trancher pour une archive de 3,53 Go ; la présente recherche ajoute donc une approche par structures ZIP et ZIP64 dans les résidus, indépendante du nom et de cette ancienne limite.

## Clichés VSS

Le catalogue contient deux clichés datés du 2 octobre 2026. La lecture ordinaire échoue sur l’en-tête du second cliché. Une **vue dérivée en mémoire** a été construite pour exclure ses deux entrées de catalogue ; les octets sources restent inchangés et les substitutions de cette vue sont consignées avec les blocs originaux. Cette méthode permet de lire le premier cliché, identifié par `b764a044-a79c-11f1-8dc9-50e08563415f`.

La MFT du cliché a été extraite intégralement : **1,071,120,384 octets**, SHA-256 `455a75d80df4c199fa7b72ea005ec774f7feabcb785473cf426437512140994e`. La recherche des trois noms y fournit trois enregistrements. Une contre-lecture des attributs NTFS `$FILE_NAME`, après contrôle des corrections de secteurs, établit qu’il s’agit exclusivement de `Rejets_saddedine.lnk`, `Inventaire_saddedine.lnk` et `Archive_saddedine.lnk` (ainsi que leurs noms courts). **Aucun des trois fichiers cibles n’est retrouvé par son nom dans cette MFT.**

Ce résultat concerne le premier cliché accessible dans cette vue dérivée. Il ne constitue pas une garantie d’intégrité ou de reconstruction exhaustive des clichés d’origine après exclusion d’une partie du catalogue. Le second cliché n’est pas déclaré exploitable ; les données libres propres aux clichés n’ont pas fait l’objet d’une reconstruction générale. Un cliché de 2026 ne restitue pas nécessairement des fichiers supprimés depuis 2024.

## Lecture des résidus

L’image a été montée avec EWF/loop en lecture seule, Dislocker `-r`, puis NTFS `ro,norecover`. Aucun rejeu de journal ni écriture sur la source n’a été effectué.

Le bitmap d’allocation NTFS correspond à l’empreinte déjà conservée :

```text
15234c950cd3cd6eea93534c0adf6bf529d1915806c4b0f698d4da20f2a3bf09
```

Le balayage a lu **357,162,754,048 octets non alloués**, répartis sur **73,355 intervalles**, soit environ 332.63 Gio. Il a également lu intégralement les fichiers suivants :

| Source logique | Octets lus | SHA-256 |
| --- | --- | --- |
| `/mnt/windows/pagefile.sys` | 5,637,144,576 | `20c7948d317d2d7a41bb9cc62dcbcc59aed9304ea92118d09f27eb9fe0f5f1e5` |
| `/mnt/windows/swapfile.sys` | 16,777,216 | `851f548cc9c67f15a835752a7712734bc232544597c5aaa76cac1bae59a74889` |
| `/mnt/windows/hiberfil.sys` | 8,395,575,296 | `3f3a1ee710d894235f973bd6c1511ddf0919da34a23aaff1024bae208a117876` |
| `/mnt/windows/$MFT` | 1,071,120,384 | `4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b` |
| `/mnt/windows/$LogFile` | 67,108,864 | `98c2cce814a1b29a6cb957a9eb1ac73fb43e43bced5c63d06a83e1e67a5b8d29` |

Les motifs recherchés comprennent les trois noms complets, `IPHONE13_MINI`, `Dossier bourarach`, `inventaire de saisie` et `nombre de fichiers saisis`, en UTF-8 et UTF-16LE, ainsi que les fins de structures ZIP et ZIP64. Les signatures ZIP ont fait l’objet d’un contrôle de cohérence des champs, du répertoire central et des noms de membres ; une simple suite d’octets `PK` n’est pas considérée comme une archive récupérée.

Le moteur compilé a été vérifié contre une recherche littérale de référence sur des données synthétiques, y compris casse, UTF-16 et motifs imbriqués. Les calculs de début et fin ZIP/ZIP64 ont été comparés à `zipfile` sur des archives synthétiques avec préfixe et commentaire. Deux premières passes partielles ont été conservées mais ne sont pas utilisées pour annoncer une couverture complète : la première a été remplacée pour des raisons de débit, la deuxième pour inclure la validation ZIP64. Seule la passe `balayage-v3` fournit le bilan final.

Le total lu par cette passe est de **372,350,480,384 octets**, fichiers logiques et clusters libres réunis. Des occurrences textuelles ont été conservées dans les catégories suivantes ; **elles sont des fragments ou références à qualifier, pas les fichiers cibles récupérés** :

| Zone | Occurrences textuelles |
| --- | --- |
| $MFT | 3 |
| unallocated | 20 |

Aucune structure validée ne fournit un candidat à la taille enregistrée de l’archive ou un répertoire central pertinent permettant sa reconstruction. Les fragments enregistrés et les détections brutes restent disponibles pour contre-lecture.

Les **982 répertoires centraux ZIP cohérents** ont en outre été comparés aux noms des **1 558 fichiers actuellement présents sous `C:\L16B`**, soit 1433 noms distincts. La normalisation Unicode et de la casse fournit une seule correspondance nominale générique : cinq membres `loading.gif` dans un conteneur de composants Sage de **28 760 933 octets**, comportant 2 687 membres. Ce conteneur, entièrement situé dans des clusters actuellement libres, est lisible et son contrôle CRC réussit. **Les cinq GIF ont des contenus différents du fichier de même nom dans L16B**, comparaison directe et SHA-256 à l’appui ; aucun nom des PDF Mini n’y figure. Ce résultat n’identifie pas l’archive cible de 3,53 Go.

Ce contrôle ne dépend pas de la présence du nom `Archive_saddedine.zip` dans les résidus. Il porte sur les répertoires centraux demeurés cohérents, sans garantir la lecture de fragments ZIP incomplets. Un répertoire central cohérent ne vaut pas, à lui seul, validation CRC de tous les membres de chacune des 982 structures.

Des fenêtres supplémentaires de 64 Kio ont été conservées autour des premières mentions physiques des trois cibles. Deux occurrences de `Archive_saddedine.zip` y correspondent à **deux copies identiques d’un Shell Item de 128 octets** : structure descriptive Windows comportant le nom et la taille de 3 525 227 798 octets. Leur empreinte est `d043ae3264018d38f5394e0314ececb7200f2afdcd3d30c6438bc7f1898d86de`. Ces structures confortent l’identification de la cible historique, mais **ne contiennent pas les données compressées de l’archive**. D’autres fragments associent les noms des cibles à leurs noms `.lnk`, sans fournir le contenu du ZIP, du TXT ou du CSV.

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
