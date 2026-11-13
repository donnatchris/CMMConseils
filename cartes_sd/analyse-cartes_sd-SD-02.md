# Rapport d’analyse technique de la carte SD-02 — terrasse

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev

**Support :** image de la carte SD-02, arborescence `CAMERA TERRASSE`

## 1. Objet et périmètre

Ce rapport présente les enregistrements conservés sur SD-02, les suppressions et récupérations possibles, les anomalies de fichiers et de dates, ainsi que les conclusions relatives aux événements signalés par la cliente. Il distingue les mesures sur l’image, les interprétations étayées et les causes non déterminées.

La cliente déclare que la **caméra de la terrasse fonctionne en continu, 24 h/24 et 7 j/7**, et qu’une interruption ou un effacement ne correspond pas à son usage habituel. Le corpus conservé est confronté à cette déclaration, sans assimiler ses lacunes à des arrêts normaux démontrés. Le signalement de réinitialisation en **février 2024 concerne la chambre**, donc SD-01 ; SD-02 apporte une comparaison technique sans en devenir la source.

Les [mails de mission](../docs/mail.txt) et [complémentaires](../docs/mail-2.txt), l’[attestation](../remise-documents/attestation-de-remise.md) et le [dossier d’acquisition](analyse-cartes_sd.md) documentent le contexte. **Les caméras et cartes n’étaient pas sous scellés.** Les enregistrements postérieurs à la perquisition ne constituent pas, à eux seuls, une anomalie. L’analyse est une investigation privée, sans désignation comme expertise judiciaire.

## 2. Synthèse des conclusions

| Question | Résultat | Portée et limite |
|---|---|---|
| Quel corpus subsiste ? | **3 300 MP4 finalisés** et **un MP4 temporaire non finalisé**. Les noms valides des finalisés vont du **5 au 12 novembre 2024**. | Un fichier au nom impossible est daté séparément du **21 octobre par ses images** ; les vestiges supprimés comportent aussi des noms du 4 novembre. |
| Des vidéos effacées sont-elles récupérées ? | **Onze vidéos complètes**, soit **44 min 36,096 s**, et **126,464 s de la fin d’une douzième**, nominalement du **5 novembre**. | Les reconstructions reposent sur les données survivantes et un ordre de clusters documenté ; le fragment n’est pas un fichier original complet. |
| Les emplacements ont-ils été réutilisés ? | **326 entrées de fichiers supprimés** ; **315 premiers clusters** se trouvent désormais dans des chaînes actives. Carte occupée à environ **99,11 %**. | L’ensemble étaye fortement une gestion circulaire du stockage, sans expliquer chaque lacune ni dater les suppressions. |
| Le corpus est-il continu ? | Non : les journées intérieures du **6 au 11 novembre** ne couvrent nominalement que **48,892–64,937 % de 24 h**. | Ce taux décrit les fichiers conservés, pas le temps certain d’alimentation de la caméra ou la cause des absences. |
| Des anomalies sont-elles confirmées ? | Un ancien dossier à création FAT **01/01/2000**, un nom impossible **`20242010`**, des allocations sans référence et un temporaire non finalisé. | Aucune modification malveillante du contenu ou origine individuelle n’est démontrée. |
| Le 15 octobre peut-il être examiné en vidéo ? | **Aucune vidéo du 15 octobre récupérée.** Un ancien slot de dossier compatible avec ce jour subsiste, mais ses données ont été remplacées. | Impossible de tester une coupure, un geste ou une reprise de caméra autour de la perquisition. |
| Une réinitialisation ou intervention malveillante est-elle établie ? | **Non.** Aucun formatage daté, reset, accès distant ou auteur n’est identifié. | L’absence de preuve ne garantit pas l’absence d’intervention ancienne. |

## 3. Identification, intégrité et méthode

### 3.1. Support et image

L’attestation décrit une carte de **32 Go**, marque transcrite « ScanDisk », sans série matérielle individuelle. Le numéro **`121220160204`** désigne le lecteur USB. L’identification de SD-02 repose sur les références d’acquisition, la pièce EWF et sa description « terrasse », concordantes avec l’arborescence et les scènes extérieures des aperçus. Le modèle physique et le firmware de caméra ne sont pas identifiés.

L’image acquise en octobre 2026 comporte **quinze segments `SD02.E01` à `SD02.E15`**, représentant **31 914 983 424 octets** décompressés. La photo `SD-02-1.jpg` référencée à la remise n’est pas disponible au chemin indiqué dans ce projet ; aucun rapprochement physique fondé sur cette photographie n’est établi.

### 3.2. Intégrité et préservation

Le contrôle libewf termine avec **SUCCESS**. Les empreintes du flux décompressé sont :

```text
MD5     d15c25a454693c2140a00c9da951e63d
SHA-256 ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d
```

Le MD5 concorde avec celui stocké dans l’EWF. Le SHA-256 est recalculé et concorde avec le document d’acquisition, sans être stocké dans les segments. Les **quinze SHA-256 des conteneurs sont identiques avant et après les lectures**. Guymager indique vérification de l’image activée, vérification de source désactivée et aucun secteur défectueux. **La vérification d’image ne constitue pas une seconde lecture indépendante de la carte physique.**

Les accès utilisent la vue EWF en mode `0444`, sans montage FAT, réparation ou écriture dans l’image. Le partage source ne constitue pas un bloqueur matériel ; les commandes de lecture et empreintes étayent la préservation. Les reconstructions sont des fichiers dérivés séparés et ne modifient aucun secteur source.

### 3.3. Couverture des contrôles

Les analyses utilisent SIFT, Sleuth Kit, une lecture indépendante des slots et chaînes FAT32, FFprobe/FFmpeg et des scripts MP4. L’inventaire FAT et TSK concorde **sans écart**, y compris les **108 entrées orphelines** contre-vérifiées dans leurs slots bruts. Le chemin virtuel `$OrphanFiles` ne désigne pas un dossier réellement présent sur la carte.

Tous les fichiers actifs sont lus et empreintés ; les vidéos analysables reçoivent un examen de métadonnées, tables et temps de paquets. Le décodage intégral actif est **ciblé sur 20 fichiers distincts**, avec contrôles prioritaires du nom impossible et du temporaire. Les onze récupérations, le fragment et les essais du temporaire ont aussi des contrôles de décodage.

L’examen visuel documenté porte sur **seize images**, sans visionnage humain complet ni analyse sémantique de l’audio. La réussite d’un décodage ou d’un contrôle de structure n’authentifie pas l’histoire du fichier avant acquisition.

## 4. Structure FAT32 et état du stockage

### 4.1. Géométrie et inventaire

| Paramètre | Valeur vérifiée |
|---|---|
| Partition FAT32 | Secteurs absolus **8 192–62 333 951**, jusqu’à la fin de l’image |
| Offset / secteur / cluster | **4 194 304 octets / 512 octets / 16 384 octets** |
| Début des clusters | **19 771 392 octets**, cluster 2 |
| Clusters de données | **1 946 729** |
| Libres / non libres | **17 288 / 1 929 441** |
| Référencés / alloués sans référence active | **1 929 373 / 68** |
| FAT | Deux copies de **15 209 secteurs** chacune |
| Identifiant de volume / OEM | **`0x386d4397` / `mkdosfs`** |

| Inventaire hors racine, alias et objets virtuels | Nombre |
|---|---:|
| Fichiers actifs | **3 306** |
| Dont MP4 | **3 301** : 3 300 finalisés et un temporaire |
| Autres fichiers actifs | **5** : `.rw`, deux auxiliaires temporaires et deux fichiers `System Volume Information` |
| Répertoires actifs | **13** |
| Entrées de fichiers supprimés | **326**, dont 108 présentées sous `$OrphanFiles` |
| Entrées de répertoires supprimés | **115** |

Les anciens noms de dossiers sont compatibles avec des jours d’avril à novembre 2024, sans restituer leurs vidéos. Un nombre d’entrées supprimées n’est pas un nombre de fichiers récupérables. Aucun fichier vidéo de février/mars n’est identifié.

### 4.2. Cohérence et anomalies d’allocation

Les deux FAT sont identiques, avec le SHA-256 :

```text
f55dd2becbbd17fe60c010570db3a36db049a1d66734b99e445c99a4fd4b60d2
```

Le compteur FSInfo principal retrouve exactement **17 288 clusters libres**, prochain suggéré **1 245 116**. La sauvegarde indique **1 946 728 libres**, prochain 2, compatible avec des valeurs initiales non actualisées. Le boot et sa sauvegarde ne diffèrent qu’à **`0x41`**, valeur 1 contre 0 ; ce champ d’état ne date pas un événement.

Aucune chaîne active trop courte ou superposition entre propriétaires actifs n’est relevée. **68 clusters alloués sans référence active** forment trois chaînes de **66, 1 et 1 clusters**, racines 309 402, 309 403 et 309 404. Ils sont non nuls, mais ne livrent aucune vidéo complète ni signature MP4 cible. Leur origine et leur date restent inconnues.

L’identifiant de volume est identique à celui de SD-01 ; il n’est ni une série physique unique ni une date fiable de formatage. Le champ BPB « secteurs cachés » vaut zéro malgré le début à 8 192. Ces particularités et la cohérence générale ne démontrent pas une altération intentionnelle. **Aucun formatage daté n’est établi**, sans exclusion de toute opération antérieure dont les traces auraient disparu.

## 5. Corpus vidéo, couverture et lacunes

### 5.1. Vidéos actives datables

Les heures des noms et les incrustations sont celles déclarées par la caméra. FAT ne stocke pas de fuseau : la convention UTC de TSK ne constitue pas un étalonnage civil. Les fins estimées additionnent un début nominal et la durée du conteneur.

| Jour nominal | MP4 finalisés à nom valide | Premier début | Dernier début | Plus grande lacune interne estimée |
|---|---:|---|---|---:|
| 05/11/2024 | 155 | 07:06:23 | 23:57:00 | 30 707,696 s |
| 06/11/2024 | 346 | 00:00:00 | 23:57:30 | 21 429,952 s |
| 07/11/2024 | 489 | 00:00:00 | 23:57:41 | 5 624,352 s |
| 08/11/2024 | 372 | 00:00:02 | 23:56:11 | 2 931,056 s |
| 09/11/2024 | 511 | 00:00:02 | 23:58:32 | 24 906,696 s |
| 10/11/2024 | 499 | 00:00:02 | 23:55:07 | 14 269,184 s |
| 11/11/2024 | 451 | 00:00:01 | 23:59:19 | 8 440,507 s |
| 12/11/2024 | 476 | 00:00:01 | 19:48:21 | 1 771,464 s |

Ces **3 299 fichiers** sont distingués du clip au nom impossible et du temporaire. La plus grande lacune interne nominale va du **5 novembre à 09:15:31,304 au même jour à 17:47:19**. Sa cause n’est pas établie.

### 5.2. Fonctionnement continu déclaré et couverture conservée

L’union des intervalles évite de compter deux fois les recouvrements. Elle porte sur les **MP4 actifs à nom datable**, sans les supprimés récupérés, le temporaire ou le nom impossible.

| Journée intérieure du corpus | Union nominale des intervalles | Part de 24 heures |
|---|---:|---:|
| 06/11/2024 | 53 970,978 s | **62,466 %** |
| 07/11/2024 | 54 133,853 s | **62,655 %** |
| 08/11/2024 | 56 105,481 s | **64,937 %** |
| 09/11/2024 | 42 242,422 s | **48,892 %** |
| 10/11/2024 | 44 056,889 s | **50,992 %** |
| 11/11/2024 | 45 221,529 s | **52,340 %** |

**Le corpus est discontinu même hors des journées de début et de fin.** Ces taux ne mesurent pas le temps où la caméra était éteinte. Réglages, déclenchement, arrêt manuel ou électrique, perte, écrasement, suppression et défaut de production ou de datation restent à distinguer.

La gestion circulaire explique fortement la réutilisation des anciens emplacements, mais ne démontre pas la cause de chaque intervalle manquant. Le fonctionnement continu déclaré justifie une vérification du réglage historique ; il ne constitue pas un journal technique de continuité.

### 5.3. Recouvrements et qualité des finalisés

Le corpus présente **360 petits chevauchements**, de **0,008 à 3,888 s**. Les deux fichiers du cas maximal passent le décodage et leurs incrustations se recouvrent également. Ce n’est donc pas seulement un effet de durée audio. Pré-enregistrement, segmentation ou comportement d’horloge sont compatibles, sans cause unique démontrée ni preuve de falsification.

Les 3 300 finalisés ont des descriptions de pistes identiques : H.264 **1 920 × 1 080** et AAC. Les contrôles ne retiennent **aucune anomalie de tables, de structure des boîtes ou de progression des paquets** dans ces fichiers. Le MP4 temporaire, non analysable tel quel, reste séparé.

Les dates FAT d’écriture sont à **−2,072 à +1,960 s** des fins estimées pour les noms valides. Le suffixe final est compatible avec une durée approchée, pas avec une séquence numérotée. Les dates internes MP4 répètent **01/01/1970**, valeur conventionnelle sans portée chronologique discriminante. Aucun de ces contrôles ne garantit l’absence d’un montage vidéo antérieur techniquement cohérent.

## 6. Suppressions et récupérations

### 6.1. Réutilisation des anciens emplacements

Les **326 entrées de fichiers supprimés** ont des créations FAT réparties entre le **4 novembre, 234 entrées**, et le **5 novembre, 92 entrées**. Ce ne sont pas des dates de suppression. **315 premiers clusters** se trouvent désormais à l’intérieur de chaînes actives. Les octets lus à ces endroits peuvent appartenir à des fichiers plus récents et ne sont pas attribués automatiquement aux anciens noms.

La saturation, les suppressions groupées de contenus anciens et la réutilisation étayent fortement un stockage circulaire. Une suppression manuelle ou ciblée ne peut être déduite de ce seul mécanisme.

### 6.2. Onze vidéos complètes du 5 novembre

| Nom du fichier supprimé | Durée récupérée | TSK |
|---|---:|---:|
| `20241105_061941_10_0300.mp4` | 300,544 s | 575101256 |
| `20241105_062453_10_0300.mp4` | 300,544 s | 575101260 |
| `20241105_063005_10_0163.mp4` | 163,968 s | 575101264 |
| `20241105_063247_10_0300.mp4` | 300,544 s | 575101268 |
| `20241105_063759_10_0033.mp4` | 33,536 s | 575101272 |
| `20241105_063835_10_0300.mp4` | 300,544 s | 575101276 |
| `20241105_064347_10_0074.mp4` | 74,368 s | 575101280 |
| `20241105_064508_10_0300.mp4` | 300,416 s | 575101284 |
| `20241105_065032_10_0300.mp4` | 300,544 s | 575101288 |
| `20241105_065547_10_0300.mp4` | 300,544 s | 575101292 |
| `20241105_070105_10_0300.mp4` | 300,544 s | 575101296 |

Les chaînes historiques sont effacées. La reconstruction ordonne les clusters libres de contenu physiquement, exclut les auxiliaires reconnus et les clusters actifs, et se borne au fichier suivant. Chaque inclusion et exclusion est documentée ; aucun média n’est inventé.

Les onze récupérations atteignent la taille déclarée, ont des tables cohérentes et passent le décodage intégral **sans avertissement**, pour **2 676,096 s**, soit **44 min 36,096 s**. Dix sont identiques à `icat -r`. Pour la dernière, l’exclusion d’un fragment de journal à l’offset logique **14 073 856** rétablit la cohérence et le décodage. Ces résultats étayent fortement l’ordre retenu, sans restituer une chaîne historique indépendante ou une signature d’authenticité antérieure.

### 6.3. Portion terminale d’une douzième vidéo

L’entrée **575101252**, `20241105_061426_10_0300.mp4`, déclare **26 289 617 octets**. Son début est remplacé, mais **688 clusters libres** conservent sa fin et le `moov` original. Sous l’hypothèse d’ordre physique documentée, le début manquant représente **15 024 128 octets**.

Un **conteneur dérivé** conserve les échantillons complets à partir d’une image clé au temps initial **173,968 s**. La portion dure **126,464 s** et se décode sans avertissement. Les aperçus affichent **5 novembre à 06:17:20 et 06:18:20**. Il s’agit d’une fin de vidéo récupérée, pas du fichier original complet. Les pistes remises séparément à zéro peuvent présenter un léger décalage audio/vidéo.

### 6.4. Temporaire non finalisé du 12 novembre

Trois fichiers **encore alloués** subsistent sous `.record_tmp` :

| TSK | Fichier | Taille |
|---|---|---:|
| **1543** | `20241112_234855_10.mp4` | **6 135 808 octets** |
| **1547** | Même base, `.mp4.moov` | **1 006 octets** |
| **1551** | Même base, `.mp4.stbl` | **24 824 octets** |

Le MP4 contient les données mais pas de `moov` final. Le modèle et le journal permettent de construire des tables pour les seuls échantillons complets **dans la taille logique** : **690 images vidéo et 539 échantillons audio**, durée **68,992 s**, décodage sans avertissement.

La chaîne comporte **380 clusters pour 375 nécessaires**. Un prolongement à toute la chaîne donne une durée apparente de **70,788 s**, mais des erreurs H.264/AAC : **ces octets excédentaires ne sont pas validés comme une suite de l’enregistrement**.

Une finalisation interrompue ou défaillante est fortement compatible avec cet état. Coupure, retrait et défaut logiciel restent possibles, sans auteur ou cause établi. Ce n’est ni une vidéo supprimée ni un événement du 15 octobre.

## 7. Espaces libres et données résiduelles

Les **283 246 592 octets libres** sont intégralement lus ; les **17 288 clusters libres sont tous non nuls**. L’empreinte de leur concaténation en ordre croissant est :

```text
SHA-256 2a01201b12dad7c859de37f8d4ba18e26a1ed48ec2c56e3426fe0d10bc8c793e
```

| Contenu caractérisé | Résultat |
|---|---:|
| Signatures `ftyp` / `mdat` | **11 / 11** |
| Signatures `moov` | **629** |
| Modèles `moov` complets de 1 006 octets | **617**, identiques entre eux et au modèle SD-01 |
| Journaux auxiliaires / fragments de journaux | **1 025 / 616** |
| Clusters de contenu utilisés pour les onze fichiers | **14 292** |
| Clusters utilisés pour la portion terminale | **688** |
| Slots MP4 supplémentaires valides hors inventaire | **0** |

Les modèles et journaux ne représentent pas des vidéos supplémentaires. Les autres clusters ne fournissent pas de nouvelle vidéo validée. Les signatures H.264 isolées ou une occurrence ASCII `2000` dans des données compressées ne sont pas des preuves de fichier ou de date.

L’audit du slack porte sur **27 156 879 octets**, dont **26 001 641 non nuls**. Les régions avant partition, réservées et terminales sont également inspectées, sans ancien système de fichiers identifié selon les motifs recherchés. Les octets hors taille logique ne sont pas assimilés automatiquement au contenu actuel.

Aucun PhotoRec propre à SD-02 n’est exécuté ; la recherche spécialisée couvre intégralement le libre selon les critères documentés. Les données écrasées, non adressables ou fragmentées sans métadonnées peuvent rester irrécupérables. Le résultat PhotoRec d’une autre carte ne vaut pas pour SD-02.

## 8. Anomalies de dates et événements signalés

### 8.1. Ancien dossier avec création FAT en 2000

L’entrée supprimée **1072**, nom partiel **`_0241013`**, conserve une création brute au **01/01/2000 à 00:00:27**, une écriture au **27/10/2024 à 22:46:28** et un accès au même jour. L’affichage à 00:00:26 de `istat` ne rend pas la seconde supplémentaire du champ de précision ; il ne s’agit pas d’un deuxième événement.

Le premier cluster **1 296 303** est maintenant le **75e cluster** de `20241110_072906_10_0079.mp4`. Le contenu ancien du dossier n’est plus disponible. La date incohérente est certaine ; ni son origine ni un reset ne sont établis. Aucune date FAT explicite de 1999 n’est identifiée.

Une valeur naïve `2000-01-01 00:00:26`, interprétée comme locale à Paris puis convertie en UTC, devient **31/12/1999 à 23:00:26 UTC**. Le sens inverse, UTC vers Paris, reste en 2000. Cette possibilité d’affichage est distincte de la cause de la valeur stockée et n’authentifie pas l’interface observée par la cliente.

### 8.2. Fichier au nom impossible `20242010`

Le fichier **273341448**, `record/20242010/20242010_060029_10_0032.mp4`, mesure **2 572 714 octets** et dure **32,768 s**. Le nom est calendairement impossible ; sa création/écriture FAT indique le **21/10/2024 à 06:01:02** et les images examinées affichent **21/10/2024 à 06:00:29 et 06:00:44**. Le décodage prioritaire réussit.

**Une anomalie de nom est établie, pas une modification malveillante du contenu.** Défaut de génération et renommage ultérieur sont compatibles. La survie de ce dossier isolé pourrait être liée à un nettoyage fondé sur des dates valides, mais ce comportement du firmware n’est pas démontré.

### 8.3. Portée pour février et le 15 octobre

Le signalement de février concerne SD-01. Sur SD-02, aucun enregistrement de février/mars n’est identifié ou récupéré ; l’ancien slot de 2000 est compatible avec un dossier d’octobre, sans lien établi avec février.

L’entrée supprimée **1074**, **`_0241015`**, porte une création au **15/10/2024 à 23:57:59** et une écriture au **28/10 à 00:28:18**. Son premier cluster **1 328 191** est réutilisé comme 53e cluster d’une vidéo du 10 novembre. Le dossier voisin **1073**, `_0241014`, porte aussi des dates d’octobre et pointe dans un fichier ultérieur. **Ces dates ne sont pas des heures d’effacement.**

Aucun flux du 15 octobre n’est disponible pour tester une interruption, un geste, un codec ou une reprise pendant la perquisition. Le fichier `20242010` se rattache aux images du 21, pas au 15. La présence rapportée d’une inspectrice sur la terrasse n’établit aucun lien technique avec les suppressions.

**Aucune réinitialisation le 15 octobre n’est établie ou exclue.** La perte des contenus anciens sur une carte fortement réutilisée ne démontre pas un effacement ciblé ce jour-là.

## 9. Traitements ultérieurs, limites et conclusion

Les auxiliaires `WPSettings.dat` et `IndexerVolumeGuid` ont des créations FAT au **12/11/2024 à 23:51:46,33 et 23:51:46,49**. Ils sont compatibles avec un traitement Windows. Leur proximité nominale avec le dernier temporaire ne démontre pas une séquence causale de retrait ou d’arrêt : les horloges ne sont pas étalonnées. Une personne ou partie de corps visible dans les aperçus du 12 novembre ne permet pas d’identifier un retrait de carte, une intention ou un opérateur.

Les recherches dans OP-01 n’identifient pas le poste ayant traité les cartes. Les concordances de fichiers avec SD-01/SD-03 concernent seulement **`.rw` vide**, aucune vidéo active commune. Les descriptions de pistes, auxiliaires et géométries semblables ne démontrent ni matériel identique ni incident commun.

L’image de 2026 conserve aussi des dates d’accès de 2025/2026, sans journal des lectures ou suppressions. Aucun modèle/firmware exact, réglage historique, historique complet de partages ou journal de compte caméra n’est obtenu. Les contrôles vidéo sont automatisés sur tous les finalisés, avec décodage actif et examen visuel ciblés. Aucune référence signée avant acquisition ne garantit l’absence de traitement vidéo antérieur.

**SD-02 établit des suppressions et une importante réutilisation, avec onze récupérations complètes et une portion terminale du 5 novembre. Le stockage circulaire est fortement étayé. Le corpus conservé présente cependant des lacunes que ce seul mécanisme n’explique pas individuellement, face au fonctionnement continu déclaré.** Le temporaire inachevé, la date FAT de 2000, le nom impossible et les allocations sans référence sont des anomalies distinctes. Aucun reset daté, formatage daté, accès distant ou acte malveillant n’est démontré ; les événements du 15 octobre ne peuvent pas être reconstitués en vidéo.

Les éléments discriminants seraient les réglages et journaux historiques, la source originale des affichages signalés, les traces du poste Windows concerné et des essais contrôlés sur une autre carte. Leur existence ou disponibilité n’est pas présumée.

## 10. Pièces techniques et termes de lecture

### 10.1. Références des constats

| Domaine | Pièces de contrôle |
|---|---|
| Acquisition et intégrité | [Rapport d’acquisition](analyse-cartes_sd.md), [ewfverify](recherche-SD-02/20261016/journaux/ewfverify-sha256.txt), [empreintes des segments](recherche-SD-02/20261016/journaux/segments-sha256-fin.txt) |
| Inventaire et allocation | [Inventaire CSV](recherche-SD-02/20261016/inventaires/inventaire.csv), [FAT indépendante](recherche-SD-02/20261016/inventaires/lecture-fat-v2.json), [allocation](recherche-SD-02/20261016/inventaires/allocation.json), [réutilisation](recherche-SD-02/20261016/inventaires/reutilisation-synthese.json) |
| Couverture et chronologie | [Par jour](recherche-SD-02/20261016/inventaires/par-jour.csv), [chronologie](recherche-SD-02/20261016/inventaires/chronologie.csv), [couverture nominale recalculée](../investigations/20261019-retour-cliente/resultats/local-v2/sd-daily-nominal-coverage.json) |
| Qualité des médias | [Synthèse](recherche-SD-02/20261016/inventaires/synthese-medias.json), [anomalies](recherche-SD-02/20261016/inventaires/anomalies-medias.json), [recouvrements](recherche-SD-02/20261016/inventaires/ecarts-index.json) |
| Vidéos supprimées | [Onze récupérations](recherche-SD-02/20261016/inventaires/recuperations.json), [portion terminale](recherche-SD-02/20261016/inventaires/recuperation-fragment-final.json) |
| Temporaire et essais non validés | [Reconstructions](recherche-SD-02/20261016/inventaires/reconstructions-temporaires.json), [compléments](recherche-SD-02/20261016/inventaires/complements-index.json) |
| Zones libres et résidus | [Scan complet](recherche-SD-02/20261016/inventaires/espace-libre.json), [classification](recherche-SD-02/20261016/inventaires/residus-classes.json), [synthèse](recherche-SD-02/20261016/inventaires/residus-synthese.json) |
| Dates et recoupements | [Analyse transversale](analyse-cartes_sd-transversale.md), [sens de conversion 1999/2000](recherche-transversale/20261016/inventaires/conversion-1999.json), [retour de la cliente](../investigations/20261019-retour-cliente/compte-rendu.md), [poste Windows](../investigations/20261017-recroisements/compte-rendu.md) |
| Reproduction | [Guide technique](recherche-SD-02/20261016/REPRODUCTION.md), [commandes et retours](recherche-SD-02/20261016/journaux/commandes.jsonl) |

Les tailles, SHA-256 et cartes de clusters sont conservés dans les index. Les reconstructions sont des preuves dérivées ; les médias et blocs privés sont exclus de Git et doivent accompagner une remise technique pour rendre tous les contrôles possibles. Les essais non validés restent identifiés dans les journaux.

### 10.2. Termes techniques

| Terme | Sens dans ce rapport |
|---|---|
| EWF / empreinte | Image d’acquisition / valeur permettant de comparer des contenus, sans certifier leur histoire avant acquisition. |
| FAT32 / cluster | Système de fichiers / unité d’allocation. Un ancien nom peut subsister après remplacement des données qu’il référençait. |
| FSInfo | Informations de gestion de l’espace libre, sans journal historique des formatages. |
| `moov` / `mdat` / `.stbl` | Métadonnées du MP4 / médias / journal auxiliaire de production. Un modèle ou un index n’est pas une vidéo supplémentaire. |
| Conteneur dérivé | Nouveau fichier structurant des médias récupérés avec des tables adaptées. Il est distinct de l’original et ne remplace pas les octets manquants. |
| PTS / DTS | Temps internes de présentation / décodage, distincts d’heures civiles certifiées. |
| Slack / taille logique | Octets restant dans l’allocation après la fin déclarée du fichier / nombre d’octets appartenant au fichier selon son entrée. Leur lecture ne valide pas automatiquement une continuation. |
