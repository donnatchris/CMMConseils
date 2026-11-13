# Rapport d’analyse technique de la carte SD-01 — chambre

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev

**Support :** image de la carte SD-01, arborescence `CAMERA CHAMBRE`

## 1. Objet et périmètre

Ce rapport présente l’état technique de SD-01, les possibilités de récupération de vidéos effacées, les anomalies de fichiers et de dates, ainsi que les conclusions relatives aux événements signalés en **février 2024** et le **15 octobre 2024**. Il repose sur l’image de la carte et les pièces techniques conservées, sans assimilation des hypothèses aux faits établis.

La cliente situe une réinitialisation de la **caméra de la chambre en février 2024**, après une installation déclarée des caméras à partir de mars 2023. Elle rapporte aussi un affichage « 31/12/1999 » et un autre événement au 15 octobre. L’application, le libellé et le fichier à l’origine de ces observations ne sont pas authentifiés. Les [mails de mission](../docs/mail.txt) et [complémentaires](../docs/mail-2.txt) documentent ces déclarations ; ils ne constituent pas des journaux de réinitialisation.

**Les caméras et les cartes n’étaient pas sous scellés.** Leurs enregistrements après la perquisition ne constituent donc pas, à eux seuls, une anomalie. L’analyse est une investigation informatique privée, sans désignation comme expertise judiciaire.

## 2. Synthèse des conclusions

| Question | Résultat | Portée et limite |
|---|---|---|
| Quels enregistrements subsistent ? | **674 vidéos actives**, réparties sur **81 jours représentés**, du **2 décembre 2023 au 28 octobre 2024** selon les noms. | Le corpus ne couvre pas toute la période depuis mars 2023 et ne constitue pas une surveillance continue. |
| Des vidéos supprimées ont-elles été récupérées ? | Trois temporaires supprimés sont reliés à une vidéo finalisée toujours présente. **Aucune vidéo effacée distincte supplémentaire n’est récupérée.** | L’absence de récupération ne prouve pas l’absence d’effacement historique. |
| Existe-t-il des anomalies techniques ? | **Sept vidéos** présentent des incohérences de tables MP4 ; celle du **1er mars** est partiellement corrompue. | Un état défectueux ne démontre pas une modification ultérieure ou une intention malveillante. |
| Que signifient les dates de 2000 ? | Deux vidéos, nommées du **21 février et du 1er mars 2024**, et leurs dossiers ont des dates FAT de janvier 2000, malgré des incrustations de 2024. | La contradiction est confirmée ; son origine et la date réelle d’écriture de ces métadonnées restent inconnues. |
| Une réinitialisation est-elle établie en février ? | **Non.** Les défauts sont compatibles avec un problème de finalisation ou d’horodatage. | Aucun journal de démarrage, retour aux réglages usine, formatage ou changement de compte ne tranche. |
| Une réinitialisation est-elle établie le 15 octobre ? | **Aucun indice positif spécifique.** Les **37 clips** de cette journée sont cohérents dans les contrôles réalisés. | Une opération entre deux clips ou sans trace conservée ne peut pas être exclue. |
| Une intervention extérieure est-elle identifiée ? | **Aucune intervention intentionnelle, malveillante ou distante n’est démontrée.** | Ni auteur, ni outil, ni commande de caméra ne sont identifiés par les données de la carte. |

**Le résultat central est un fonctionnement récurrent de finalisation avec retrait des temporaires, associé à des défauts réels mais non attribués de dates et d’index vidéo. Aucun des événements signalés n’est confirmé comme une réinitialisation effective.**

## 3. Identification, intégrité et méthode

### 3.1. Identification du support et de l’image

L’[attestation de remise](../remise-documents/attestation-de-remise.md) décrit une carte de **32 Go**, marque transcrite « ScanDisk », sans numéro de série individuel. Le numéro USB **`121220160204`** identifie le lecteur, pas la carte. Le rattachement à SD-01 repose sur les références d’acquisition et la pièce EWF `SD-01` ; la photographie documentaire ne permet pas de distinguer les trois cartes par une série matérielle.

L’image acquise en octobre 2026 comprend **`SD01.E01` et `SD01.E02`**. Le flux disque décompressé mesure **31 914 983 424 octets**. La description « chambre » concorde avec l’arborescence et les scènes des aperçus examinés, sans identifier le modèle physique ou le firmware de la caméra.

### 3.2. Contrôles d’intégrité

`ewfverify` termine avec **SUCCESS**. Le MD5 enregistré et recalculé est identique ; le SHA-256 recalculé sur le flux complet concorde avec le document d’acquisition :

```text
MD5     cf7837b9d9a3907f1a8db5b7d0b06922
SHA-256 42fa8f6d3351a4ba2446b267637f51a0c1e44df4abd31b002a1ac2212c023c09
```

| Segment | Taille, octets | SHA-256 du conteneur |
|---|---:|---|
| `SD01.E01` | 2 146 400 796 | `95f0a1eb5058bd9134e1136f53d95d735ba23ea2f3216adfa66308bcc4eba621` |
| `SD01.E02` | 312 683 347 | `76215335e6acadfdde8ef424ce277e5391bddbb6898f455066f1184f3d42f444` |

Les empreintes des segments sont inchangées après les lectures de contrôle. Le journal Guymager indique une vérification d’image activée, une vérification de source désactivée et aucun secteur défectueux. **La concordance acquisition/image ne constitue pas une seconde lecture indépendante de la carte physique**, ni une authentification de son histoire avant acquisition.

### 3.3. Méthode et couverture effective

La vue EWF est lue en mode `0444`, sans montage FAT, réparation ou écriture sur l’image. Le partage hébergeant les segments reste monté en écriture ; il ne constitue pas un bloqueur matériel. La préservation est étayée par les commandes de lecture et les contrôles d’empreintes. Les extractions et essais portent sur des données dérivées distinctes.

Les contrôles utilisent notamment Sleuth Kit, une lecture indépendante des structures FAT32, FFprobe/FFmpeg et des scripts d’analyse des tables MP4. Ils couvrent l’inventaire, les chaînes de clusters, les entrées supprimées, **tous les clusters libres**, les fins de fichiers et les structures du volume.

Les **674 vidéos actives** sont extraites, empreintées, ouvertes par FFprobe et intégralement soumises au décodage FFmpeg. Ce décodage automatisé est distinct d’un visionnage humain. L’examen visuel documenté porte sur **23 images obtenues sur 24 demandées**, prises dans huit clips ciblés. L’audio ne fait pas l’objet d’une interprétation sémantique exhaustive.

## 4. Organisation du volume et inventaire

### 4.1. Structure FAT32

| Paramètre | Valeur vérifiée |
|---|---|
| Partition FAT32 | Secteurs absolus **8 192–62 333 951**, jusqu’à la fin de l’image |
| Offset de partition | **4 194 304 octets**, secteurs de 512 octets |
| Taille de cluster | **16 384 octets** |
| Début de la zone de clusters | **19 771 392 octets**, cluster 2 |
| Clusters de données | **1 946 729** |
| Libres / non libres | **1 797 391 / 149 338** |
| FAT | Deux copies de **7 787 008 octets**, identiques |
| Identifiant de volume / OEM | **`0x386d4397` / `mkdosfs`** |

L’inventaire indépendant concorde avec les **770 lignes TSK** : **766 entrées** et quatre objets virtuels de l’outil. Il comprend **677 fichiers alloués**, dont 674 MP4 et trois auxiliaires (`.rw`, `WPSettings.dat`, `IndexerVolumeGuid`), **85 répertoires alloués**, **trois fichiers supprimés** et **une entrée de répertoire supprimée**.

L’entrée supprimée **`_CIM`** et le répertoire actif **`CAMERA CHAMBRE`** pointent tous deux au **cluster 3**, avec des métadonnées courtes identiques hors nom et marque de suppression. **Un vestige de renommage du même répertoire est fortement étayé.** Le premier caractère ancien et la date de l’opération ne sont pas établis ; ce n’est pas la preuve de la disparition d’un autre ensemble de vidéos.

### 4.2. Cohérence et limites de datation du système de fichiers

Les chaînes actives ne présentent ni cycle, ni chaîne trop courte, ni partage de cluster entre propriétaires actifs, ni cluster alloué perdu ou marqué mauvais. Les **149 338 clusters alloués** ont un propriétaire retrouvé. Cette cohérence décrit l’état actuel du volume, sans reconstituer son histoire.

Le compteur FSInfo principal est exactement cohérent avec les **1 797 391 clusters libres**. Sa sauvegarde indique **1 946 728 libres**, avec un prochain cluster suggéré à 2 : valeurs compatibles avec un état initial non actualisé. Le pointeur de recherche principal **150 934** désigne actuellement un cluster alloué ; il ne garantit pas que ce cluster soit libre et ne porte aucune date.

Le boot et sa sauvegarde ne diffèrent qu’à l’octet **`0x41`**, valeur 1 contre 0, compatible avec un indicateur de volume non démonté proprement selon la convention du pilote FAT Linux. Le champ BPB « secteurs cachés » vaut zéro malgré la partition à 8 192. Ces particularités ne datent ni un incident ni un repartitionnement. L’OEM et l’identifiant de volume ne désignent pas un opérateur et ne fournissent pas une date fiable de formatage.

**Aucune trace positive ne date un formatage, une reconstruction du volume ou une réinitialisation aux dates recherchées.** Une FAT cohérente, des blocs nuls, un FSInfo ancien ou un indicateur d’état ne suffisent pas à établir ou exclure un formatage antérieur.

## 5. Enregistrements conservés et lacunes

### 5.1. Couverture générale et portée des horloges

Les noms des **674 MP4** vont du **02/12/2023 à 18:15:46** au **28/10/2024 à 23:25:03**, sur **81 jours représentés**. La somme des durées déclarées est de **7 h 50 min 38,066 s** ; les **339 vidéos du 15 au 28 octobre** totalisent **3 h 44 min 05,254 s**. Ces sommes ne mesurent pas un temps civil de surveillance continue.

Les heures FAT, les noms et les incrustations sont des indications des systèmes producteurs, **sans étalonnage civil indépendant**. FAT ne stocke pas de fuseau ; l’écriture a une précision de deux secondes et le dernier accès une précision d’un jour. La convention UTC des sorties TSK n’authentifie pas le fuseau réel. Les 2 298 champs temporels contre-vérifiés concordent avec les valeurs FAT brutes, sous réserve des fractions de création non rendues par TSK.

Tous les noms actifs suivent `AAAAMMJJ_HHMMSS_10_DDDD.mp4` et correspondent à la date du dossier. Le suffixe `DDDD` représente une durée approchée, **pas un compteur de séquence** : un écart entre suffixes n’indique pas une vidéo manquante. Les 674 contenus ont des SHA-256 distincts.

### 5.2. Répartition du 15 au 28 octobre 2024

Les débuts et fins ci-dessous sont nominaux : début tiré du nom, fin calculée à partir de la durée du conteneur.

| Jour | Vidéos | Premier début | Dernier début | Fin estimée du dernier clip |
|---|---:|---|---|---|
| 15/10 | 37 | 12:14:54 | 22:41:17 | 22:46:17,416 |
| 16/10 | 8 | 03:18:36 | 21:25:00 | 21:25:33,280 |
| 17/10 | 9 | 03:44:17 | 09:50:32 | 09:51:05,408 |
| 18/10 | 55 | 00:55:05 | 22:50:47 | 22:51:12,029 |
| 19/10 | 7 | 04:02:37 | 20:40:16 | 20:40:50,337 |
| 20/10 | 19 | 00:02:34 | 18:15:53 | 18:16:25,128 |
| 21/10 | 68 | 00:57:59 | 21:52:50 | 21:54:34,576 |
| 22/10 | 60 | 01:07:54 | 20:25:34 | 20:26:26,096 |
| 23/10 | 9 | 01:03:02 | 21:56:09 | 21:56:49,192 |
| 24/10 | 5 | 02:53:36 | 20:30:58 | 20:31:31,024 |
| 25/10 | 4 | 00:49:52 | 10:45:01 | 10:45:57,960 |
| 26/10 | 36 | 03:18:01 | 22:54:11 | 22:54:52,984 |
| 27/10 | 18 | 02:45:53 | 17:14:44 | 17:15:17,920 |
| 28/10 | 4 | 02:53:48 | 23:25:03 | 23:25:39,864 |

Aucun jour n’est entièrement absent entre le 15 et le 28, mais des plages de plusieurs heures ne comportent aucun clip référencé. Les 8–14 octobre sont absents ; des lacunes plus anciennes atteignent environ 25 jours. Les absences ne sont donc pas propres à la perquisition.

Le 28, les quatre clips commencent à **02:53:48, 06:16:51, 23:22:34 et 23:25:03**. Entre la fin du deuxième et le début du troisième, la lacune nominale est de **17 h 05 min 03,960 s**. Aucun nom ne situe une vidéo pendant la séance administrative de journée. Cela ne prouve ni un arrêt, ni une consultation, ni un effacement.

L’organisation en clips variables est compatible avec un enregistrement intermittent ou événementiel, sans réglage historique vérifié. La cliente déclare ne déclencher elle-même que les interruptions ; cette déclaration ne permet pas d’identifier techniquement la cause de chaque lacune. Les petits recouvrements estimés, de **0,043 à 2,056 s**, ne démontrent pas davantage une modification.

## 6. Suppressions, récupération et données résiduelles

### 6.1. Temporaires associés à une vidéo toujours présente

| Entrée TSK supprimée | Objet sous `.record_tmp` | Taille déclarée | Octets récupérés |
|---|---|---:|---:|
| **1543** | `20241028_232503_10.mp4` | 3 182 592 | 16 384 |
| **1547** | Même base, `.mp4.moov` | 1 006 | 1 006 |
| **1551** | Même base, `.mp4.stbl` | 11 888 | 11 888 |

Le MP4 final actif **76861460**, `20241028_232503_10_0036.mp4`, mesure **3 441 753 octets**, dure **36,864 s** et se décode sans avertissement. Son SHA-256 est `983b95a6023069cc78f46e73519eb01ded13673e0b49372927cfb4803fb56d39`.

L’ancien temporaire et le fichier final commencent au **même cluster 150 722**. Les 16 384 octets récupérés sont identiques au préfixe du final. La chaîne active existe à ce départ ; la courte extraction ne démontre donc pas une disparition générale de la chaîne. Les deux clusters auxiliaires suivants sont libres.

Le journal `.stbl` concorde intégralement avec le début de cinq séries de tables du final : **360 tailles vidéo, 259 tailles audio, 38 positions vidéo, 37 positions audio et 12 images clés**. Le modèle `.moov` est une structure de production, pas un enregistrement distinct.

**L’association des trois temporaires à la fabrication de la vidéo conservée est fortement étayée.** Leur retrait après finalisation est très vraisemblablement un fonctionnement habituel. Il n’établit ni trois vidéos perdues, ni une suppression manuelle, ni une date de suppression : FAT ne conserve pas cette dernière information.

### 6.2. Recherche dans les espaces libres

Les **1 797 391 clusters libres**, soit **29 448 454 144 octets**, sont intégralement lus. **1 480 clusters** contiennent des données non nulles ; les autres sont entièrement nuls. L’empreinte du flux libre concaténé dans l’ordre croissant est :

```text
SHA-256 52126d236bbfa9192e7602be7c584528c97a0d8fbe8d126c1fa1f0c9a5026b78
```

Les 1 480 clusters comprennent **624 modèles `moov`** identiques et **856 fragments compatibles avec les journaux `.stbl`**. Aucune signature `ftyp` ou `mdat` n’est retrouvée dans le libre. Les modèles et journaux ne sont pas autant de vidéos : ils décrivent des auxiliaires de finalisation sans fournir de nouvelles images indépendantes.

Sur **625 journaux candidats** comparés au fichier actif voisin, **613** concordent sur les cinq séries testées ; onze concordent jusqu’à une dernière valeur résiduelle nulle. Le cas restant concerne le 1er mars : **185 tailles vidéo dans le final contre 188 dans le journal**. Ce désaccord renforce l’anomalie d’indexation de ce fichier, sans révéler une vidéo distincte.

La répétition des auxiliaires sur des centaines de clips renforce l’explication d’un processus courant de finalisation. Leur grammaire est inférée ; certains octets de fragments restent non interprétés et aucune signature H.264 isolée n’est assimilée à un flux vidéo validé.

### 6.3. Fins de fichiers et autres régions

L’audit lit **5 499 840 octets de slack**, dont 6 954 non nuls, sans signature MP4 cible. Le clip du 21 février a **cinq clusters excédentaires, soit 81 920 octets entièrement nuls**. Les régions avant partition sont nulles hors MBR ; la fin hors clusters ne livre pas de vidéo ni d’ancien boot identifié. Le journal PhotoRec conservé indique également zéro fichier récupéré, avec des paramètres historiques partiellement documentés.

**Aucune vidéo effacée supplémentaire, complète ou partiellement décodable, n’est récupérée dans ces zones.** Les données écrasées, remises à zéro, fragmentées sans métadonnées ou non exposées par le contrôleur peuvent ne plus être accessibles.

## 7. Anomalies vidéo et horodatages

### 7.1. Qualité des MP4 et limites du décodage

Les 674 MP4 contiennent H.264 **1 920 × 1 080** et AAC ; leurs durées déclarées vont de **1,199 à 300,544 s**. Tous terminent le décodage avec code 0, mais certains produisent des erreurs : **un code de retour nul ne garantit pas l’intégrité d’une vidéo**.

| Entrées TSK avec incohérence de tables | Date nominale | Qualification |
|---|---|---|
| **11500564** | 11/01/2024, 00:07:26 | Défaut terminal de compte d’échantillons |
| **20903944** | 21/02/2024, 23:39:14 | Compteurs audio/vidéo incohérents, données vidéo non indexées |
| **22835208** | 01/03/2024, 04:05:05 | Compteurs incohérents, références hors données et corruption H.264 |
| **36542512** | 14/09/2024, 19:47:25 | Défaut terminal de compte d’échantillons |
| **49060412** | 18/10/2024, 01:09:43 | Même famille de défaut terminal |
| **63907420 / 63907540** | 22/10/2024, 08:52:39 et 13:59:40 | Même famille de défaut terminal |

Les avertissements de DTS non croissants produits au muxeur de sortie sur soixante clips sont distingués de ces défauts : les PTS/DTS des paquets d’origine sont strictement croissants. Les essais de sortie adaptés font disparaître l’avertissement sur les témoins contrôlés, ce qui soutient un effet de traitement des temps plutôt qu’une preuve d’altération de la source.

### 7.2. Dates FAT de 2000 et images de 2024

Deux vidéos et leurs dossiers portent des dates de création/écriture de janvier 2000 :

| Fichier | Durée déclarée | Dates et contenu contrôlés |
|---|---:|---|
| `20240221_233914_10_0151.mp4`, **20903944** | **151,924 s** | FAT du 01/01/2000 ; aperçu à une seconde affichant **21/02/2024 23:39:15** |
| `20240301_040505_10_0012.mp4`, **22835208** | **12,950 s** | FAT du 01/01/2000 ; aperçu affichant **01/03/2024 04:05:06** ; lecture indexée limitée à **134 images sur 185**, dernière PTS **9,309 s** |

Neuf slots bruts portent au moins une date de 2000 : **cinq objets** (deux vidéos, deux dossiers et `.rw`) et **quatre alias `.`/`..`**. Ce ne sont pas neuf événements indépendants. Les mots de date valent réellement `0x2821` : la date n’est pas un simple affichage de champ nul. Aucune date FAT explicite de 1999 n’est identifiée.

Les fichiers voisins de février/mars ont des dates cohérentes avec leurs noms, dont douze vidéos du 29 février. Il ne s’agit donc pas d’un retour continu d’horloge démontré entre le 21 février et le 1er mars. Les descriptions de codecs des fichiers anormaux sont identiques à celles des témoins ; aucune rupture d’encodage spécifique n’est identifiée.

### 7.3. Défaut de finalisation commun et données non indexées

Les deux clips aux dates de 2000 portent une erreur audio précise : le dernier compteur `stsc` reprend le **cumul précédent au lieu des sept échantillons restants**. Ce même défaut existe dans neuf clips de SD-03, dès novembre 2023. Leurs compteurs vidéo sont aussi incohérents. Les corrections expérimentales sur des copies en mémoire suppriment l’avertissement de compte, sans garantir les médias ni restaurer les temps manquants.

Le clip du 21 février contient en outre une zone non indexée : un test borné permet de décoder **trois images supplémentaires**, de 2 170 à 2 173 images, sans ajouter de date de présentation. **Il ne s’agit pas d’une nouvelle vidéo complète récupérée, ni d’une fin datée restaurée.** Le reste de cette zone n’est pas automatiquement attribué à une continuation vidéo.

**Un mécanisme récurrent défectueux de finalisation ou de reconstruction est fortement étayé.** Une interruption, une reprise avec date par défaut, un problème d’horloge ou un traitement ultérieur sont compatibles. Le logiciel, le déclencheur, le moment de l’écriture et le caractère humain ou automatique ne sont pas déterminés.

### 7.4. Dates internes MP4 et affichage « 31/12/1999 »

Les **674 MP4** portent la même date interne **01/01/1970**. Les **3 370 champs bruts** de création contrôlés valent 2 082 844 800 dans le repère MP4. Cette répétition est fortement compatible avec une valeur conventionnelle du logiciel, sans valeur de date effective de captation. Elle est distincte des dates FAT de 2000.

Une date FAT naïve `2000-01-01 00:00:26`, interprétée comme locale à Paris puis convertie en UTC, devient **`1999-12-31 23:00:26Z`**. Le sens inverse, UTC vers Paris, reste au 1er janvier. **Le calcul explique une possibilité d’affichage de 1999, pas la cause de la valeur stockée ni l’interface réellement consultée par la cliente.**

## 8. Événements signalés et rapprochements

### 8.1. Chambre en février 2024

Les anomalies du 21 février et du 1er mars sont des candidats au rapprochement avec le signalement, sans provenance authentifiée de l’affichage. Le défaut commun à onze vidéos sur deux cartes existe avant février ; il n’est pas un marqueur spécifique de retour aux réglages usine, de changement de compte ou de réappairage.

Les fins de deux fichiers du 21 février sur SD-01 et SD-03 sont proches, mais les mesures ne sont pas interchangeables : **1,828 s entre dernières PTS indexées produites**, **1,177 s entre fins vidéo de tables, dans l’autre ordre**. Les images non indexées de SD-01 et les images manquantes de SD-03 empêchent de transformer cette proximité en heure de coupure commune. **Un incident commun est plausible ; ni sa simultanéité civile ni sa cause ne sont établies.**

### 8.2. Journée du 15 octobre 2024

Les **37 clips du jour** ont des noms, formats, descriptions de pistes et dates FAT cohérents. Aucun ne porte la date FAT 2000 ou les incohérences de tables identifiées sur les sept autres fichiers. Leurs PTS/DTS d’origine sont croissants ; l’intervalle maximal entre paquets vidéo consécutifs dans un clip est de **0,138 s**. Ces résultats ne décrivent pas ce qui se passe entre deux fichiers.

Une lacune nominale de **1 h 26 min 06,400 s** sépare la fin du clip de 13:23:20 et le début de 14:49:52. La plus longue lacune interne du jour est de **5 h 14 min 51,760 s**, entre 17:25:30,240 et 22:40:22. Ni l’une ni l’autre ne démontre un effacement, un arrêt ou une réinitialisation. L’heure de 13:30 rapportée pour les téléphones ne date pas un événement de caméra.

Le dossier `20241015` porte une création/écriture à **22:46:18**, alors que ses alias internes gardent **12:15:28**. Ces valeurs sont voisines des fins du dernier et du premier clip. Le même schéma est retrouvé, à deux secondes près, dans **79 des 81 dossiers journaliers**, les exceptions étant les deux ensembles de 2000. **La date dite de création du dossier n’est donc pas un indicateur fiable de première initialisation ou de réinitialisation de la carte.**

**Aucune réinitialisation le 15 n’est établie.** Le bon état des clips n’exclut pas une opération ou un redémarrage entre enregistrements.

### 8.3. Traitements ultérieurs et autres équipements

`.rw` porte une création/écriture au **1er novembre 2024** ; les auxiliaires `System Volume Information` ont des créations proches du **12 novembre 2024 à 23:35:28**. Des derniers accès vidéo vont jusqu’en octobre 2026. Ces dates témoignent d’une histoire postérieure aux scènes, sans prouver un visionnage.

Les noms des auxiliaires sont compatibles avec un traitement sous Windows. La recherche des identifiants dans OP-01 n’a pas identifié le poste ayant traité les cartes ; elle n’exclut pas OP-01 si ses traces anciennes ont disparu. Les correspondances de fichiers entre les trois cartes ne concernent que **`.rw` vide**, pas des vidéos identiques.

Les traces LSC des téléphones ne sont pas reliées directement à une commande sur SD-01 par un identifiant matériel, une session ou une empreinte vidéo. Aucun historique complet de partages, réappairages ou changements de compte n’est reconstitué ; le modèle exact et le firmware restent inconnus. Les états applicatifs tardifs ne remplacent pas un journal de 2024.

## 9. Limites et conclusion technique

L’image est acquise en 2026 et ne constitue pas un instantané de 2024. La chaîne de conservation depuis les faits, les horloges, les paramètres historiques et le firmware ne sont pas vérifiés de bout en bout. FAT32 ne fournit pas ici de journal des accès et suppressions. Les dates peuvent être conservées ou modifiées lors de copies ; les contenus écrasés ou inaccessibles au contrôleur ne sont pas reconstruits.

Les propriétés, valeurs brutes, empreintes et correspondances sont directement contrôlables. Leur interprétation ne permet pas de désigner un acteur, une intention ou un caractère autorisé. Le décodage automatisé complet ne vaut pas visionnage humain intégral ; les aperçus ne décrivent que les instants échantillonnés. Aucun état vidéo antérieur signé ne permet de garantir l’absence de traitement avant acquisition.

**SD-01 conserve 674 vidéos et des auxiliaires dont la suppression est fortement liée à la finalisation habituelle des clips. Aucune vidéo effacée distincte supplémentaire n’est récupérée. Sept vidéos ont des défauts de tables, dont une corruption effective le 1er mars ; les deux dates FAT de 2000 sont associées à un défaut commun avec SD-03.** Ces anomalies n’établissent ni retour aux paramètres d’usine, ni formatage daté, ni intervention malveillante. Le 15 octobre ne présente pas d’indice spécifique positif de réinitialisation.

Pour départager les causes, les éléments discriminants seraient l’affichage original, les journaux de caméra/compte/horloge, les réglages historiques et une expérience contrôlée sur un autre support reproduisant ensemble les dates FAT et les défauts MP4. Leur disponibilité n’est pas présumée.

## 10. Pièces techniques et termes de lecture

### 10.1. Références des constats

| Domaine | Pièces de contrôle |
|---|---|
| Acquisition, intégrité et reproduction | [Rapport d’acquisition](analyse-cartes_sd.md), [guide technique](recherche-SD-01/20261015/README.md), [guide des contrôles ciblés](recherche-SD-01/20261016-complement/README.md) |
| Inventaire et chronologie | [Vidéos](recherche-SD-01/20261015/inventaires/videos.csv), [par jour](recherche-SD-01/20261015/inventaires/par-jour.csv), [intervalles](recherche-SD-01/20261015/inventaires/intervalles.csv) |
| Temporaires et tables | [Comparaisons prioritaires](recherche-SD-01/20261015/inventaires/verification-prioritaire.json), [séries de tables](recherche-SD-01/20261015/inventaires/comparaison-stbl.json) |
| Dates FAT et dossier du 15 | [Slots de 1999/2000](recherche-SD-01/20261016-complement/inventaires/traces-fat-1999-2000.csv), [chronologie du 15](recherche-SD-01/20261016-complement/inventaires/chronologie-20241015.csv), [paquets vidéo](recherche-SD-01/20261016-complement/inventaires/paquets-video-20241015.json), [dates des dossiers](recherche-SD-01/20261016-complement/inventaires/repertoires-premier-dernier-clip.csv) |
| Résidus et espace libre | [Scan complet](recherche-SD-01/20261015/inventaires/scan-non-alloue-v2.json), [caractérisation](recherche-SD-01/20261015/inventaires/residus-caracterises-v2.json) |
| Défaut commun, images non indexées et fins comparées | [Analyse transversale](analyse-cartes_sd-transversale.md), [essais sur les médias résiduels](recherche-transversale/20261016/inventaires/nal-non-indexes.json), [fins comparées](recherche-transversale/20261016/inventaires/fins-comparees.json) |
| Contexte, comptes et poste Windows | [Retour de la cliente](../investigations/20261019-retour-cliente/compte-rendu.md), [recoupements](../investigations/20261017-recroisements/compte-rendu.md), [identification des caméras](../investigations/20261109-identification-cameras/compte-rendu.md) |

Les scripts, commandes, erreurs et manifestes conservent la traçabilité des mesures. Les médias et blocs privés sont des pièces dérivées exclues de Git ; le dépôt seul ne les contient pas nécessairement. Les empreintes historiques des rapports concernent leurs versions respectives et ne sont pas des signatures du présent texte.

### 10.2. Termes techniques

| Terme | Sens dans ce rapport |
|---|---|
| EWF / empreinte | Conteneur d’acquisition / valeur de comparaison du contenu. La stabilité d’une empreinte ne certifie pas l’histoire antérieure à l’acquisition. |
| FAT32 / cluster | Système de fichiers / unité d’allocation. Une entrée supprimée peut subsister alors que ses anciens clusters sont réutilisés. |
| FSInfo / boot | Informations de gestion de l’espace libre / structure de démarrage du volume. Leurs valeurs ne fournissent pas ici de date de formatage. |
| `.moov` / `.stbl` | Modèle de métadonnées et journal auxiliaire de production ; leur présence ne représente pas une vidéo supplémentaire. |
| `mdat` / tables MP4 | Données audio/vidéo / index décrivant tailles, positions et temps. Un index cohérent et des médias intacts sont deux propriétés distinctes. |
| PTS / DTS | Temps de présentation / de décodage des médias. Ce sont des temps internes, pas des heures civiles certifiées. |
| Slack / EOF | Octets alloués au-delà de la taille logique / fin logique d’un fichier. Ces octets nécessitent une validation avant toute attribution au fichier. |
