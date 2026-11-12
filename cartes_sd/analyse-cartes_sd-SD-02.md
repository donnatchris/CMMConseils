# Analyse informatique de la carte SD-02

**Relecture de cohérence : 12 novembre 2026.** Harmonisation avec le [rapport final réorganisé](../RAPPORT-FINAL-SADEDINE-2026.md), sans nouvelle acquisition ni nouvelle analyse des supports. Les campagnes et décomptes techniques conservent leurs dates et leurs périmètres. Le détail de cette révision et les empreintes actuelles figurent dans le [dossier de relecture](../investigations/20261112-coherence-rapports/compte-rendu.md).

## Actualisation du 10 novembre 2026 — lecture courante

Le PV est disponible et a été consulté. Les repères à retenir sont la mise sous scellés après 14 h 19 le 15 octobre, l’ouverture du PC à 10 h 41 et celle des téléphones à 11 h 30 le 28 ; 10 h 22 est l’arrivée de la cliente et 19 h 20 la clôture, sans heure individuelle de restitution. Les mentions d’indisponibilité et bornes déclaratives des sections datées ci-dessous décrivent leurs campagnes historiques. Les caméras et cartes n’étaient pas sous scellés. Les nouvelles traces système TP-03 ne prouvent ni un accès aux caméras ni une modification des vidéos. Cette relecture ne réexécute pas les scans/récupérations SD ; elle maintient les anomalies, lacunes et limites déjà établies. Voir la [relecture transversale](../investigations/20261110-telephones/compte-rendu.md), qui distingue les nouveaux contrôles des reprises documentaires. Les empreintes historiques des rapports restent attachées à leurs versions datées.


## Actualisation du 19 octobre 2026 — terrasse déclarée en continu

Dans [mail-2.txt](../docs/mail-2.txt), la cliente indique que la terrasse enregistre **24 h/24 et 7 j/7** et qu’un arrêt ou effacement ne correspond pas à son usage habituel. Cette déclaration est désormais prise en compte : **les lacunes du corpus ne doivent pas être assimilées à un arrêt normal démontré**. La gestion circulaire du stockage reste fortement compatible avec la réutilisation des clusters, sans expliquer à elle seule chaque lacune.

Le nouveau calcul de l’union des intervalles des vidéos actives à nom datable donne **48,892 à 64,937 %** d’une journée de 24 h pour les journées intérieures du **6 au 11 novembre**. Il mesure la couverture nominale des fichiers conservés, pas le temps certain d’alimentation de la caméra ; les supprimés récupérés, le temporaire et le nom impossible sont exclus de ce calcul. Les noms des vidéos actives finalisées à date exploitable vont du **5 au 12 novembre 2024** ; les entrées supprimées portent aussi des noms du 4 novembre ; le clip `20242010` reste séparément daté du **21 octobre par ses images**. Aucun enregistrement récupéré du 15 ne permet d’examiner l’intervention déclarée sur la terrasse.

La présence rapportée d’une inspectrice sur la terrasse ne relie aucune manipulation aux suppressions. Le signalement de février **2024** concerne désormais explicitement la **chambre**, sans pouvoir être transposé à SD-02. Le PV n’était pas disponible lors de cette campagne d’octobre ; il a depuis été consulté le 8 novembre. Méthode, tableaux journaliers et limites : [complément du 19 octobre](../investigations/20261019-retour-cliente/compte-rendu.md).


**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils.  
**Prestataire :** Christophe Donnat — Donnat Dev.  
**Campagne :** 16 octobre 2026. Investigation technique indépendante, non expertise judiciaire.  
**Support étudié :** image EWF identifiée SD-02 ; arborescence `CAMERA TERRASSE`.

## Questions auxquelles l'analyse tente de répondre

1. Peut-on retrouver et récupérer des vidéos effacées ? Que reste-t-il lorsque les données ont été remplacées ?
2. Les enregistrements ou le système de fichiers présentent-ils des modifications anormales ? Peut-on établir une intervention intentionnelle ou malveillante ?
3. SD-02 permet-elle d'expliquer l'affichage « 31/12/1999 » évoqué pour février et l'événement signalé le **15 octobre 2024** ? Une réinitialisation est-elle démontrée ?

Les caméras **n'ont jamais été placées sous scellés**. Leurs enregistrements après la perquisition ne sont donc pas suspects pour cette seule raison. L'origine exacte des observations de la cliente reste inconnue ; elle pourrait concerner des métadonnées, mais cette provenance n'est pas établie.

## Conclusions simples à présenter à l'avocate

- **Des vidéos supprimées ont été retrouvées : onze fichiers complets et la fin d'un douzième.** Les onze premiers représentent **2 676,096 secondes**, soit **44 min 36,096 s** ; la portion du douzième dure **126,464 s**. Tous passent le décodage intégral sans avertissement. Leurs noms et les aperçus contrôlés les situent au **5 novembre 2024**, selon les horloges déclarées par la caméra. Les méthodes de reconstruction et leurs limites sont documentées (§ 6).
- **La carte porte de nombreuses traces de suppression et de réutilisation.** Elle est occupée à environ **99,11 %**. Sur 326 entrées de fichiers supprimés, 315 pointent désormais à l'intérieur de vidéos actives ou d'autres fichiers actifs. L'ensemble est **fortement compatible avec un enregistrement en boucle remplaçant les données anciennes**. Cela ne prouve ni une suppression manuelle ni une intention malveillante.
- **Aucune vidéo du 15 octobre, ni de février/mars 2024, n'a été récupérée sur SD-02.** Un ancien nom de dossier compatible avec le 15 octobre subsiste, mais son emplacement a été réutilisé. On ne peut donc pas examiner les séquences de la perquisition à partir de cette carte.
- **Une date FAT de janvier 2000 est confirmée**, dans une entrée supprimée de dossier au nom partiellement conservé `_0241013`. Aucune date FAT explicite de 1999 n'a été trouvée dans les entrées examinées. Cette anomalie **ne permet pas de dater ni de démontrer une réinitialisation**, en février ou le 15 octobre.
- **Une anomalie de nom est établie : `20242010`.** Dans ce fichier, les images contrôlées affichent le **21 octobre 2024 à 06:00:29**, en accord avec les dates FAT. Le nom est incohérent ; une modification malveillante du contenu n'est pas démontrée.
- **Un enregistrement temporaire du 12 novembre était resté non finalisé.** Un conteneur dérivé permet de lire **68,992 s**, sans avertissement de décodage. La cause de l'arrêt reste inconnue. Une tentative d'utiliser les octets alloués au-delà de la taille logique provoque des erreurs et **n'est pas retenue comme récupération validée**.

**Conclusion défendable :** SD-02 établit des suppressions anciennes, une réutilisation importante des emplacements et plusieurs anomalies techniques. Elle ne permet d'établir **ni une réinitialisation aux dates signalées, ni une intervention malveillante, ni son auteur**. Cette absence de preuve ne garantit pas qu'aucune intervention n'ait existé.

## Hypothèses pouvant expliquer les anomalies

| Constat | Explications compatibles | Qualification |
| --- | --- | --- |
| Suppressions anciennes, carte presque pleine, données anciennes remplacées | Gestion circulaire automatique du stockage ; d'autres suppressions restent possibles | Fonctionnement normal **fortement étayé**, mécanisme exact non observé en fonctionnement |
| Création FAT en 2000 et autre date d'écriture en 2024 | Horloge non initialisée ou corrigée, défaut logiciel, métadonnées réécrites, copie/modification ultérieure | **Cause indéterminée** ; aucun scénario ne permet ici de dater une réinitialisation |
| Nom `20242010`, image et FAT concordantes au 21/10/2024 | Erreur de génération du nom, défaut logiciel, renommage ultérieur | Anomalie de nom **confirmée**, cause et intention inconnues |
| Dates internes MP4 à 1970 dans les vidéos analysables | Valeur conventionnelle ou par défaut du logiciel | Interprétation **fortement étayée** par sa répétition ; aucune date d'événement n'en est déduite |
| Dernier MP4 temporaire sans métadonnées finales | Arrêt ou interruption d'écriture, retrait/alimentation, défaut de finalisation | Interruption technique **plausible**, cause non démontrée |
| Fichiers `System Volume Information` datés du 12/11/2024 | Traitement du volume par un environnement compatible Windows | Trace de métadonnées **confirmée** ; ne prouve pas une lecture des vidéos ni l'identité d'un utilisateur |

## 1. Périmètre, sources et qualification des conclusions

Sources de contexte : [mail original](../docs/mail.txt), notamment son § 4 ; [attestation de remise](../remise-documents/attestation-de-remise.md) ; [rapport d'acquisition](analyse-cartes_sd.md) ; [corrections de contexte de la mission](recherche-SD-01/20261016-complement/sources/contexte-et-observations.md). Le premier mail ne précisait pas l’année ni la caméra ; [le nouveau mail](../docs/mail-2.txt) indique désormais **février 2024 et la chambre**, distincte de SD-02/terrasse. Le fichier et l’interface de l’observation restent non établis.

L'heure de début de la perquisition n'est pas documentée dans ces pièces. **13 h 30 concerne la perte d'accès aux téléphones.** Aucun rapprochement automatique avec une coupure caméra à cette heure n'est justifié.

Niveaux utilisés : **observation confirmée** (lecture et artefact identifiés), **interprétation fortement étayée** (plusieurs concordances indépendantes), **hypothèse possible**, **absence de preuve**, **limitation**. Une date, une suppression et une intention sont des questions distinctes. La présence d'un fichier lisible ne garantit pas son authenticité historique en l'absence de référence antérieure signée.

## 2. Identification, intégrité et préservation

L'image source comporte **quinze segments**, `SD02.E01` à `SD02.E15`, dans :

```text
/media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/
```

EWF : dossier `SADEDINE-2026`, pièce `SD-02`, examinateur Christophe Donnat ; description « Carte SD contenant les enregistrements vidéos des caméras (terrasse) ». Acquisition Guymager du **12 octobre 2026**, de 13:07:17 à 13:40:06 selon le document d'acquisition. Ce document indique vérification de l'image activée, vérification de la source désactivée et aucun secteur défectueux signalé. Il ne constitue pas une preuve de l'état antérieur aux acquisitions.

L'attestation décrit une carte de 32 Go, marque transcrite « ScanDisk », sans numéro de série. Le numéro USB `121220160204` est celui du **lecteur**, pas un numéro matériel confirmé de SD-02. La photo `SD-02-1.jpg` référencée par l'attestation n'est pas disponible au chemin indiqué dans ce projet ; aucun contrôle visuel de cette photo n'est revendiqué. Le rattachement « terrasse » est concordant entre la description EWF, le nom du dossier et les aperçus d'une scène extérieure ; il ne constitue pas une identification physique de modèle de caméra.

| Vérification | Résultat | Preuve |
| --- | --- | --- |
| Vue EWF | `/mnt/ewf-sd02/ewf1`, **31 914 983 424 octets**, mode 0444 | [état initial](recherche-SD-02/20261016/journaux/etat-initial.txt), [provenance](recherche-SD-02/20261016/journaux/provenance.txt) |
| Vérification libewf | `ewfverify: SUCCESS` | [sortie complète](recherche-SD-02/20261016/journaux/ewfverify-sha256.txt) |
| MD5 enregistré et recalculé | `d15c25a454693c2140a00c9da951e63d` | Même sortie |
| SHA-256 des données décompressées | `ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d` ; concorde avec l'acquisition | Même sortie, rapport d'acquisition |
| Quinze SHA-256 de segments | **Identiques avant et en fin de campagne** | [empreintes initiales](recherche-SD-02/20261016/journaux/segments-sha256.txt), [empreintes finales](recherche-SD-02/20261016/journaux/segments-sha256-fin.txt) |

Le SHA-256 des données décompressées n'était pas stocké dans les segments EWF : il est calculé par cette vérification et comparé au rapport d'acquisition. Le contrôle EWF valide également les contrôles internes du conteneur et le MD5 enregistré.

**Préservation :** accès aux sources en lecture seule, aucun montage FAT, aucune réparation ni écriture sur FORENSIC. Le partage source lui-même n'est pas présenté comme un bloqueur matériel d'écriture. La préservation pendant cette campagne est étayée par les commandes et les empreintes avant/après. Toutes les sorties persistantes sont dans le projet. Les vidéos traitées dans SIFT sont lues dans des fichiers anonymes en mémoire (`memfd`), fermés après usage. Les fichiers sensibles et blocs bruts sont exclus de Git par `.gitignore`, conservés sur disque dans le projet.

## 3. Méthode et environnement

VM SIFT, Linux 6.8.0-110, Python **3.12.3**, Sleuth Kit **4.11.1**, libewf-tools **20140816**, FFmpeg/FFprobe **6.1.1**, PhotoRec disponible dans TestDisk **7.1**. Versions et disponibilité : [outils](recherche-SD-02/20261016/journaux/outils.txt). Connexion via `ssh -F /home/chris/.ssh/config -o BatchMode=yes sift`, configuration explicite de l'hôte `sift` demandé.

Ordre : intégrité ; partition et FAT ; inventaires indépendants ; chronologie et examen des médias ; récupérations ; espace libre, slack et allocations sans référence ; anomalies temporelles et structures ; recoupements ; vérification finale. Aucun résultat SD-01 n'est assimilé à un constat SD-02.

La jointure initiale a isolé **108 entrées orphelines TSK** absentes de la récursion des seuls répertoires référencés. Leur cluster commence par des fragments LFN, et non par une entrée `.` valide. Une lecture ciblée de leurs slots a confirmé ces 108 entrées, sans les présenter comme un dossier actif. L'inventaire final comporte **zéro écart FAT/TSK**. Essais et rejets sont conservés, pas masqués. Références : [FAT indépendante](recherche-SD-02/20261016/inventaires/lecture-fat-v2.json), [slots orphelins](recherche-SD-02/20261016/inventaires/orphelins-slots.json), [état de jointure](recherche-SD-02/20261016/inventaires/etat-inventaire.json).

**Portée vidéo effectivement exécutée :** empreinte et lecture de tous les fichiers actifs ; FFprobe, inspection des boîtes/tables MP4 et temps des paquets sur toutes les vidéos actives analysables. Décodage intégral ciblé de **20 fichiers actifs distincts**, (17 dans le lot principal, un complément pour le 12 novembre, deux pour le chevauchement maximal), comprenant les témoins premier/dernier par jour et les cas anormaux détectés ; contrôle prioritaire supplémentaire du fichier au nom impossible et du temporaire. Les onze vidéos récupérées, le fragment et les deux essais du temporaire ont aussi reçu un décodage intégral. **Le contenu de toutes les vidéos n'a pas été visionné ni intégralement décodé.** Les seize PNG décrits au § 8 ont été effectivement examinés visuellement par l'assistant ; aucun visionnage humain intégral n'est revendiqué.

Le stockage initial disponible était d'environ 16 Gio : conservation sélective, plafonds explicites, pas de duplication de l'image de 31,9 Go. Les scripts de réception refusent liens, chemins hors projet, écrasements et dépassements de taille. Les incidents et choix sont détaillés dans [incidents et limites](recherche-SD-02/20261016/journaux/incidents-et-limites.md).

## 4. Partition, FAT et inventaire

| Paramètre | Valeur vérifiée |
| --- | --- |
| Partition FAT32 0x0c | Secteurs absolus **8 192–62 333 951**, jusqu'à la fin de l'image |
| Début en octets | **4 194 304**, secteurs de 512 octets |
| Secteurs réservés / FAT | 6 / deux FAT de **15 209 secteurs** chacune |
| Taille de cluster | **16 384 octets**, soit 32 secteurs |
| Premier octet des clusters | **19 771 392**, cluster 2 |
| Clusters de données | **1 946 729** |
| Clusters libres / non libres | **17 288 / 1 929 441** |
| Référencés par structures actives / sans référence active | **1 929 373 / 68** |
| Queue de partition hors clusters complets | 8 secteurs, soit 4 096 octets |

Preuves : [mmls](recherche-SD-02/20261016/journaux/mmls.txt), [fsstat](recherche-SD-02/20261016/journaux/fsstat.txt), [géométrie et FAT](recherche-SD-02/20261016/inventaires/lecture-fat-v2.json), [audit d’allocation](recherche-SD-02/20261016/inventaires/allocation.json). Les commandes Sleuth Kit sur le système de fichiers utilisent toutes **`-o 8192`**. Les numéros de clusters sont relatifs au volume ; les offsets JSON sont explicitement absolus en octets.

| Inventaire logique, hors pseudo-entrées virtuelles | Nombre |
| --- | ---: |
| Fichiers alloués | **3 306** |
| Dont MP4 | **3 301**, comprenant un temporaire non finalisé |
| MP4 dans `record/` | **3 300** : 3 299 noms valides de novembre et un nom de date impossible |
| Autres fichiers actifs | 5 : `.rw`, deux auxiliaires temporaires, deux fichiers `System Volume Information` |
| Répertoires alloués, hors racine et alias `.`/`..` | **13** |
| Entrées de fichiers supprimés | **326**, dont 108 sous `$OrphanFiles` virtuel |
| Entrées de répertoires supprimés | **115** |

Ces nombres concernent des **entrées** : ils ne signifient pas que 326 vidéos supprimées sont encore récupérables. Les anciens dossiers comportent des noms partiellement perdus, compatibles avec des jours d'avril à novembre 2024. Les pointeurs de nombreux anciens dossiers aboutissent désormais dans les données d'autres fichiers : ils ne sont pas interprétés comme des arborescences actuelles corrompues. Aucun fichier vidéo de février/mars n'est identifié dans l'inventaire.

Inventaires exploitables : [CSV exhaustif](recherche-SD-02/20261016/inventaires/inventaire.csv), [fls brut](recherche-SD-02/20261016/inventaires/fls.txt), [chronologie FAT brute](recherche-SD-02/20261016/inventaires/timeline.body), [mactime UTC](recherche-SD-02/20261016/inventaires/timeline-mactime.csv). Les entrées de date nulle affichées par mactime ne sont pas de véritables événements. Le mode UTC est une **convention de présentation** ; FAT ne fournit pas de fuseau horaire permettant d'authentifier l'heure civile.

## 5. Chronologie des vidéos actives

Heures déduites des noms, fin estimée = début nominal + durée mesurée FFprobe. Une superposition dans l'image constitue une autre indication **de la caméra**, pas une horloge civile indépendante.

| Jour nominal | Vidéos finalisées | Premier nom | Dernier nom | Plus grande lacune interne estimée, s |
| --- | ---: | --- | --- | ---: |
| 2024-11-05 | 155 | 07:06:23 | 23:57:00 | 30707.696 |
| 2024-11-06 | 346 | 00:00:00 | 23:57:30 | 21429.952 |
| 2024-11-07 | 489 | 00:00:00 | 23:57:41 | 5624.352 |
| 2024-11-08 | 372 | 00:00:02 | 23:56:11 | 2931.056 |
| 2024-11-09 | 511 | 00:00:02 | 23:58:32 | 24906.696 |
| 2024-11-10 | 499 | 00:00:02 | 23:55:07 | 14269.184 |
| 2024-11-11 | 451 | 00:00:01 | 23:59:19 | 8440.507 |
| 2024-11-12 | 476 | 00:00:01 | 19:48:21 | 1771.464 |

Le temporaire non finalisé est séparé de ce tableau. Le fichier `20242010` est exclu du calcul calendaire car son mois serait 20. La somme des durées ne mesure pas une surveillance continue. La plus grande lacune interne nominale va du **5 novembre 09:15:31,304 au 17:47:19**, soit **30 707,696 s**. Faute de réglages et journaux de déclenchement, sa cause n'est pas déterminée.

Les calculs trouvent aussi **360 petits chevauchements internes**, entre **0,008 et 3,888 s**. Le cas maximal concerne `20241105_214356_10_0101.mp4` (657582352) et `20241105_214534_10_0266.mp4` (657582356). Les deux passent un décodage intégral sans avertissement. Les quatre images supplémentaires effectivement examinées montrent respectivement 21:43:55 puis 21:45:35 à 100 s dans le premier, et 21:45:34 puis 21:45:38 à 4 s dans le second. Les incrustations couvrent donc aussi des heures qui se chevauchent ; ce n'est pas seulement un effet d'addition des durées audio. Un pré-enregistrement, des frontières de segments ou un comportement d'horloge sont compatibles, sans cause unique démontrée. Cela ne démontre pas une falsification. Références : [contrôles du chevauchement](recherche-SD-02/20261016/inventaires/ecarts-index.json) et `inventaires/ecarts/`. Le premier clip finalisé du 12 novembre a reçu un contrôle complémentaire distinct, car le premier tri quotidien retenait le temporaire comme témoin initial : [complément](recherche-SD-02/20261016/inventaires/supplement-index.json). Les intervalles calculés sont dans [intervalles](recherche-SD-02/20261016/inventaires/intervalles.csv) et les fins/durées/FAT dans [chronologie détaillée](recherche-SD-02/20261016/inventaires/chronologie.csv).

Le suffixe final est **compatible avec une durée approximative**, et non avec une numérotation séquentielle des événements : les différences durée réelle moins suffixe vont de **0.089 à 1.568 s**. Le champ `_10` n'est pas interprété faute de documentation constructeur. Les clips longs voisins de 300 s et les multiples clips plus courts montrent un découpage ; ils ne suffisent pas à déterminer les réglages exacts de déclenchement. Une lacune ne prouve pas une suppression.

Les fichiers actifs se caractérisent par les profils codec consignés dans la synthèse (H.264 1920 × 1080 et AAC pour les vidéos analysables). Les contrôles de lecture et de structure, ainsi que les éventuelles anomalies de paquets et de tables, sont détaillés au § 8 et dans [synthèse médias](recherche-SD-02/20261016/inventaires/synthese-medias.json). La comparaison des dates des dossiers et de leurs alias `.` est séparée : [répertoires et horloges](recherche-SD-02/20261016/inventaires/repertoires-horloges.csv). Une date de dossier peut refléter une mise à jour ou une finalisation, et ne date pas à elle seule une remise à zéro.

## 6. Fichiers supprimés et récupérations

### 6.1 Ce que démontrent les entrées supprimées

Les 326 entrées de fichiers supprimés ont des dates FAT de création distribuées entre le **4 novembre (234)** et le **5 novembre (92)**. Pour les orphelins, le chemin `$OrphanFiles` est une présentation virtuelle de TSK ; leurs noms courts partiellement perdus ne sont pas réinventés.

**315 premiers clusters sont maintenant à l'intérieur de chaînes actives**, et non simplement à leur début. Une extraction `icat -r` de ces entrées peut donc renvoyer des octets d'un fichier ultérieur : elle n'est pas une récupération certaine de l'ancien contenu. La portion terminale du fichier 575101252 constitue l'exception partielle décrite ci-dessous, pas une récupération de son début.

Preuves : [réutilisations, CSV](recherche-SD-02/20261016/inventaires/supprimes-reutilisation.csv), [synthèse de réutilisation](recherche-SD-02/20261016/inventaires/reutilisation-synthese.json), inventaire et FAT. **Confiance élevée** sur la réutilisation actuelle ; la FAT ne conserve pas l'auteur ni l'heure de suppression. Les anciens horodatages ne sont pas des journaux d'effacement.

### 6.2 Onze vidéos récupérées complètes

| Fichier supprimé | Durée mesurée, s | Identifiant TSK |
| --- | ---: | ---: |
| 20241105_061941_10_0300.mp4 | 300.544000 | 575101256 |
| 20241105_062453_10_0300.mp4 | 300.544000 | 575101260 |
| 20241105_063005_10_0163.mp4 | 163.968000 | 575101264 |
| 20241105_063247_10_0300.mp4 | 300.544000 | 575101268 |
| 20241105_063759_10_0033.mp4 | 33.536000 | 575101272 |
| 20241105_063835_10_0300.mp4 | 300.544000 | 575101276 |
| 20241105_064347_10_0074.mp4 | 74.368000 | 575101280 |
| 20241105_064508_10_0300.mp4 | 300.416000 | 575101284 |
| 20241105_065032_10_0300.mp4 | 300.544000 | 575101288 |
| 20241105_065547_10_0300.mp4 | 300.544000 | 575101292 |
| 20241105_070105_10_0300.mp4 | 300.544000 | 575101296 |

Leurs premiers clusters sont libres. Leurs chaînes historiques ont été effacées. La reconstruction utilise les clusters libres de contenu, en ordre physique croissant, en excluant les emplacements actuellement alloués et les auxiliaires reconnus, avec borne au début de fichier suivant. Chaque cluster et chaque exclusion sont listés, et aucun octet de contenu n'est inventé.

**Résultat :** taille déclarée atteinte, boîtes MP4 complètes, cohérence des tables, décodage intégral sans avertissement pour les onze. Dix reconstructions sont **strictement identiques sur toute leur longueur** à `icat -r`. Pour **575101296**, `icat -r` incorpore un fragment de journal à l'offset logique **14 073 856** ; son exclusion rétablit les tables et le décodage. La concordance avec les structures et le décodage étaye fortement l'ordre retenu ; elle ne restitue pas une chaîne FAT historique indépendante ni une signature d'authenticité antérieure.

Référence complète, tailles, SHA-256, cartes de clusters, contrôles `icat` et FFmpeg : [récupérations](recherche-SD-02/20261016/inventaires/recuperations.json). Copies et témoins `icat` : `prive/recuperations/`, exclus de Git. **Confiance élevée sur la récupération technique**, avec l'hypothèse d'ordre physique explicitement conservée.

### 6.3 Fin d'une douzième vidéo

Entrée **575101252**, `20241105_061426_10_0300.mp4`, taille initialement déclarée **26 289 617 octets**. Son premier cluster est réutilisé, mais **688 clusters libres** conservent une portion terminale, dont le `moov` original. Le début manquant est évalué à **15 024 128 octets** sous l'hypothèse d'ordre physique ; le `moov` terminal tombe exactement à la position attendue d'après la taille déclarée.

La reconstruction conserve seulement les échantillons entièrement présents, commence sur une image clé et crée un **nouveau conteneur** avec des tables adaptées. La séquence récupérée commence à **173,968 s** dans la vidéo initiale supposée et dure **126,464 s**. Elle passe le décodage intégral sans avertissement. Les deux aperçus affichent **06:17:20** et **06:18:20** le 5 novembre, en cohérence avec cette portion.

Ce résultat est un **fragment vidéo lisible**, pas le fichier d'origine complet. Les octets manquants ne sont pas remplacés par une vidéo inventée. Les pistes sont ramenées séparément à zéro ; un léger décalage audio/vidéo peut résulter de cette opération. Preuve et hypothèses : [fragment final](recherche-SD-02/20261016/inventaires/recuperation-fragment-final.json), script [sd02_partial_remote.py](scripts/sd02_partial_remote.py). Le `moov` original est conservé séparément.

### 6.4 Enregistrement temporaire du 12 novembre

Trois fichiers **alloués**, identifiants **1543, 1547, 1551** :

```text
CAMERA TERRASSE/.record_tmp/20241112_234855_10.mp4        6 135 808 octets
CAMERA TERRASSE/.record_tmp/20241112_234855_10.mp4.moov       1 006 octets
CAMERA TERRASSE/.record_tmp/20241112_234855_10.mp4.stbl      24 824 octets
```

Le MP4 a `ftyp`/`mdat` mais pas de `moov` final. Son journal contient des tailles, offsets et informations temporelles ; le modèle `.moov` fournit les descriptions de pistes. La grammaire est inférée et contrôlée par les cumuls et la cohérence des tables, sans documentation du micrologiciel.

Une reconstruction limitée aux chunks complets **dans la taille logique** restaure **690 images vidéo** et **539 échantillons audio**, durée globale **68,992 s**, décodage sans avertissement. Seul le conteneur et ses tables sont reconstruits ; les médias proviennent des octets existants. La chaîne allouée contient **380 clusters**, alors que 375 suffisent à la taille déclarée. L'essai sur toute cette chaîne donne un fichier de durée apparente **70,788 s** mais produit des erreurs H.264/AAC : ces octets excédentaires ne sont **pas validés comme la suite de l'enregistrement**. Le journal plus long ne prouve pas que tous les médias correspondants aient été écrits durablement.

**Interprétation :** finalisation interrompue ou défaillante, fortement compatible avec les trois fichiers encore actifs. Une coupure, un retrait ou un défaut logiciel sont possibles ; leur cause, auteur et intention ne sont pas établis. Ce n'est pas une vidéo supprimée ni une preuve d'un événement du 15 octobre. Artefacts : [contrôles prioritaires](recherche-SD-02/20261016/inventaires/priorite-index.json), [reconstructions et échecs](recherche-SD-02/20261016/inventaires/reconstructions-temporaires.json), [chaîne complète et provenance](recherche-SD-02/20261016/inventaires/complements-index.json).

## 7. Zones libres, slack et allocations résiduelles

Les **283 246 592 octets libres** ont tous été lus et empreintés, sans échantillonnage. Les **17 288 clusters libres sont tous non nuls**. SHA-256 du flux libre concaténé en ordre croissant : `2a01201b12dad7c859de37f8d4ba18e26a1ed48ec2c56e3426fe0d10bc8c793e`.

| Recherche/classification | Résultat |
| --- | ---: |
| Signatures `ftyp` / `mdat` | **11 / 11** |
| Signatures `moov` | **629** : modèles et métadonnées finales |
| Modèles `moov` complets de 1 006 octets en début de cluster | **617**, tous identiques entre eux |
| Journaux auxiliaires / fragments de journaux | **1 025 / 616** |
| Autres clusters libres, avant récupération | **15 030** |
| Clusters de contenu utilisés pour les onze fichiers | **14 292** |
| Clusters utilisés pour le reliquat terminal du douzième | **688** |
| Slots de fichiers MP4 supplémentaires répondant aux critères et absents de l'inventaire | **0** |

Les 50 autres clusters de classe « autre » ne sont pas annoncés comme des vidéos supplémentaires. Les modèles et journaux sont des **structures auxiliaires**, pas autant de vidéos. Le modèle de 1 006 octets a le même SHA-256 que le modèle observé sur SD-01 : `731c49c0eb32815913b66158889c78a53f83fcea0e661589ac633b8fa5c26e15`.

Les **68 clusters alloués sans référence active** forment trois chaînes de 66, 1 et 1 clusters, racines 309402, 309403 et 309404. Les blocs sont non nuls, sans signature `ftyp`/`moov`/`mdat` dans les recherches consignées. Leur provenance et leur date restent indéterminées ; aucun fichier vidéo complet n'en est tiré. C'est une **anomalie d'allocation confirmée**, pas une preuve de dissimulation volontaire.

Le slack des fichiers actifs représente **27 156 879 octets** lus, dont **26 001 641 non nuls**. Les octets hors taille logique ne sont pas assimilés au contenu du fichier actuel ; l'échec du prolongement du temporaire en fournit un exemple concret. L'audit fournit empreintes et candidats de signatures, pas une récupération automatique de chaque occurrence. Les 4 Mio avant la partition, les secteurs réservés et les huit secteurs de fin ont aussi été inspectés ; seuls les secteurs de démarrage actuels/sauvegardés portent les signatures FAT repérées dans ces régions.

Preuves : [scan libre](recherche-SD-02/20261016/inventaires/espace-libre.json), [classification](recherche-SD-02/20261016/inventaires/residus-classes.json), [synthèse et chaînes perdues](recherche-SD-02/20261016/inventaires/residus-synthese.json), [allocation et slack](recherche-SD-02/20261016/inventaires/allocation.json). Une occurrence ASCII `2000` dans une charge vidéo compressée est conservée comme faux candidat non datable, pas comme une métadonnée. Les signatures de type H.264 isolées sont heuristiques, sans garantie de flux récupérable.

**Limite :** aucun PhotoRec SD-02 n'a été exécuté : la recherche spécialisée exhaustive des clusters libres a permis des récupérations validées et évite une extraction aveugle de 32 Go. Le résultat antérieur de PhotoRec sur SD-01 ne vaut pas pour SD-02. L'absence d'autres fichiers reconstruits ne prouve pas l'absence d'autres effacements, notamment après réécriture.

## 8. Anomalies temporelles et vérification des médias

### 8.1 Date FAT de janvier 2000

Une entrée supprimée de dossier, **TSK 1072**, nom `_0241013`, offset absolu **19 805 600**, conserve :

- Création par contre-lecture : **2000-01-01 00:00:27**, en interprétant le champ des centièmes.
- Écriture : **2024-10-27 22:46:28** ; accès : **2024-10-27**, sans heure d'accès probante.
- `istat` affiche création **00:00:26** : les champs bruts comportent une seconde supplémentaire dans le champ des centièmes ; cette différence de représentation n'est pas un second événement.
- Premier cluster **1296303**, actuellement **75e cluster** de `20241110_072906_10_0079.mp4`. Le contenu ancien du dossier n'est plus récupérable à cet emplacement.

La date aberrante est **établie**, l'événement qui l'a produite ne l'est pas. Le nom partiellement perdu est compatible avec le 13 octobre ; il ne relie pas cette entrée à février et ne date pas un reset. Preuves : inventaire brut/CSV, [istat 1072](recherche-SD-02/20261016/journaux/istat/1072.txt), réutilisation et FAT.

FAT encode les secondes d'écriture par pas de deux secondes ; la création possède aussi un champ de précision supplémentaire. Le dernier accès est principalement une **date de jour**, pas un journal de lecture. Aucun fuseau n'est stocké dans ces champs. Une conversion d'une date proche de minuit vers un fuseau à l'ouest d'UTC pourrait afficher le jour précédent ; **ce mécanisme n'est pas reproduit ni établi pour l'affichage de la cliente** et le fuseau Europe/Paris ne suffit pas à produire la veille à partir de ce minuit. Il faut distinguer une explication possible de l'affichage de la cause ayant écrit la valeur 2000.

### 8.2 Métadonnées internes MP4 et contrôles automatisés

Les dates MP4 internes et leurs valeurs brutes sont recensées dans [synthèse médias](recherche-SD-02/20261016/inventaires/synthese-medias.json). Les fichiers analysables répètent la valeur `1970-01-01T00:00:00.000000Z` ; la valeur brute courante `2082844800` correspond à 1970 dans l'échelle de temps MP4. Cette répétition dans des enregistrements de plusieurs jours lui retire sa valeur de date d'enregistrement effective.

Résultats actifs : **3301 MP4**, **3300 dans `record/`**, échecs FFprobe : **CAMERA TERRASSE/.record_tmp/20241112_234855_10.mp4**. Nombre de fichiers actifs avec erreurs de structure : **0** ; anomalies de tables : **0** ; anomalies de progression de paquets retenues : **0**. Le détail par fichier et les avertissements bruts font foi : [anomalies](recherche-SD-02/20261016/inventaires/anomalies-medias.json), dossier `inventaires/medias/`, `journaux/decodage/`.

Les descriptions de pistes `stsd` sont strictement identiques pour chacun des 3 300 fichiers finalisés (une empreinte audio commune et une empreinte vidéo commune). Aucune progression non croissante de PTS/DTS vidéo n'est retenue par le contrôle automatisé. Les dates FAT d'écriture se situent entre **−2,072 et +1,960 s** des fins estimées sur les fichiers dont le nom est calendairement valide, ce qui est cohérent avec leur précision et le processus de finalisation. Cela n'étalonne pas l'heure civile.

Les avertissements de dépréciation de `-enc_time_base -1` sont des messages d'outil, pas des corruptions. FFmpeg peut aussi retourner zéro malgré des erreurs : l'essai non validé du temporaire est explicitement séparé. Une structure MP4 cohérente et un décodage réussi ne prouvent pas qu'un montage vidéo techniquement propre n'ait jamais été réalisé. Aucun mécanisme de signature native de caméra n'a été authentifié.

### 8.3 Nom impossible et observations visuelles effectivement effectuées

Fichier **273341448**, `CAMERA TERRASSE/record/20242010/20242010_060029_10_0032.mp4`, taille **2 572 714 octets**, durée **32,768 s** : création et écriture FAT **21/10/2024 06:01:02**, dossier parent également daté ainsi. Les deux images contrôlées affichent **21/10/2024 06:00:29** et **06:00:44**. Le décodage intégral du fichier prioritaire réussit ; les avertissements signalés sont ceux de dépréciation.

**Observation confirmée :** le nom est calendairement impossible, tandis que FAT et incrustation convergent vers le 21 octobre. **Interprétation :** anomalie de nom, sans explication unique démontrée. Un bug et un renommage ultérieur sont compatibles ; aucun auteur, intention ou outil de modification n'est identifié. Le caractère non calendaire du dossier pourrait aussi le faire échapper à un nettoyage fondé sur des dates valides, ce qui expliquerait la survie isolée de ce fichier d'octobre au milieu des vidéos de novembre. Cette hypothèse de fonctionnement n'est pas confirmée par le code ou un essai du micrologiciel.

Seize images effectivement examinées par l'assistant : deux du fichier au nom impossible ; deux du temporaire reconstruit à 0 et 60 s ; deux de la première et deux de la dernière vidéo récupérée à 0 et 150 s ; un témoin actif du 5 novembre et un du 12 novembre ; deux du fragment final ; quatre des deux clips au chevauchement maximal. Elles montrent une scène extérieure de terrasse et des horodatages incrustés. Une personne ou une partie de corps est visible à proximité de la caméra dans les témoins du 12 novembre, notamment à **23:49:54** dans le temporaire ; ces images ne prouvent ni un retrait de carte, ni l'identité de la personne, ni une intention. Aucune analyse audio ou identification personnelle n'est revendiquée.

Provenance et empreintes : [index des dix premiers aperçus](recherche-SD-02/20261016/inventaires/apercus-index.json), [deux aperçus du fragment](recherche-SD-02/20261016/inventaires/recuperation-fragment-final.json). Les PNG sont conservés sous `prive/apercus/`.

### 8.4 Accès ultérieurs et indices hors logiciel caméra

`System Volume Information/WPSettings.dat` (12 octets) et `IndexerVolumeGuid` (76 octets) ont des créations FAT au **12/11/2024 23:51:46,33 et 23:51:46,49**. Leur présence est compatible avec un traitement du volume par Windows. Leur proximité nominale avec le dernier temporaire est une piste pour un arrêt/retrait puis un traitement sur ordinateur, **pas une séquence causale démontrée** : horloges non étalonnées et absence de journaux de l'ordinateur concerné.

Plusieurs dates de dernier accès vont jusqu'en 2025/2026. Elles sont déjà dans l'image acquise et ne sont pas des écritures de cette analyse. Une date FAT d'accès ne prouve pas un visionnage ni son auteur. Le marqueur `.rw` est vide ; sa fonction exacte n'est pas établie. Les empreintes finales identiques étayent l'absence de modification des segments pendant les opérations présentes.

## 9. Réponse séparée aux deux événements signalés

### 9.1 Événement apparent de février / affichage du 31 décembre 1999

**Trace d’origine :** le premier mail ne donnait ni année ni caméra ; le [mail complémentaire](../docs/mail-2.txt) précise **février 2024, caméra de la chambre**, donc SD-01. La capture, l’application, le fichier et l’heure restent inconnus. SD-02 constitue une comparaison technique, sans lui transposer le signalement. La supposition « peut-être les métadonnées » n'authentifie pas cette origine.

**Ce qu'elle démontre :** une observation rapportée justifiant l'investigation. Sur SD-02, une date FAT de 2000 subsiste dans un ancien slot compatible avec un dossier d'octobre ; aucune vidéo de février/mars ni entrée FAT de 1999 n'a été identifiée dans le périmètre contrôlé. Le résultat SD-01 concernant février/mars ne doit pas être transplanté à SD-02.

**Explications compatibles :** affichage/conversion d'une date de référence pour la présentation « 31/12/1999 » ; pour la valeur stockée, horloge non initialisée/corrigée, dysfonctionnement, ou métadonnées modifiées ultérieurement. La présence répétée de 1970 dans les MP4 relève d'un autre champ et ne date pas un reset.

**Une réinitialisation est-elle établie ?** **Non.** Ni l'événement technique, ni sa date réelle, ni un lien avec février 2024 ne sont démontrés sur SD-02. La source exacte de l'affichage et les journaux de caméra/application manquent.

### 9.2 Événement du 15 octobre 2024

**Trace d'origine :** même mail, parlant d'« un autre événement » ce jour-là ; ce libellé n'est pas une preuve de reset. Pas d'heure de début de perquisition vérifiée, pas de source technique originale de l'observation.

**Ce que SD-02 démontre :** l'entrée supprimée **1074**, `_0241015`, porte création **15/10/2024 23:57:59**, écriture **28/10/2024 00:28:18**. Son premier cluster **1328191** est maintenant le **53e cluster** de `20241110_073415_10_0055.mp4`. L'entrée voisine `_0241014` (1073) porte création **15/10/2024 00:00:00**, écriture **27/10/2024 22:49:00**, et pointe également dans une vidéo ultérieure. **Ces dates ne sont pas des heures d'effacement.** Les vidéos de ces dossiers ne sont pas retrouvées.

**Explications compatibles :** ancienne organisation quotidienne et remplacement circulaire des contenus ; dates de dossiers liées à finalisation/mise à jour ; autres modifications possibles, sans moyen de choisir une cause précise à partir des slots seuls. Aucun flux vidéo du 15 octobre n'est disponible pour tester une coupure, un changement de codec, une séquence ou une reprise autour de la perquisition.

**Une réinitialisation est-elle établie ?** **Non.** La carte ne permet ni de confirmer ni d'exclure une opération le 15 octobre. L'absence actuelle de ces vidéos, sur une carte massivement réutilisée et contenant des vidéos postérieures, ne démontre pas un effacement ciblé ce jour-là. L'anomalie `20242010` se rattache techniquement au **21 octobre**, pas au 15.

Preuves : inventaire CSV, [réutilisation des dossiers ciblés](recherche-SD-02/20261016/inventaires/reutilisation-synthese.json), `journaux/istat/1073.txt` et `1074.txt`.

## 10. Formatage, réinitialisation et cohérence FAT32

Les deux FAT ont le même SHA-256 :

```text
f55dd2becbbd17fe60c010570db3a36db049a1d66734b99e445c99a4fd4b60d2
```

Le compteur FSInfo principal (**17 288 libres**, prochain suggéré **1245116**) concorde exactement avec la lecture complète de la FAT. La sauvegarde contient **1 946 728 libres**, prochain **2**, valeurs compatibles avec un état initial non actualisé. Boot principal/sauvegarde : une seule différence à **0x41**, principal 1, sauvegarde 0 ; cet octet n'est pas une date.

OEM `mkdosfs`, étiquette FAT32, identifiant de volume **0x386d4397**, champ BPB secteurs cachés **0** malgré le début de partition à 8192. Ces caractéristiques sont documentées telles quelles ; l'identifiant identique à celui de SD-01 n'est ni un identifiant matériel unique ni une date fiable de formatage. Le champ caché ne suffit pas à établir une altération malveillante.

**Pas de chaîne active trop courte ni de recouvrement entre propriétaires actifs** dans l'audit. Les 68 allocations sans référence et l'excédent du temporaire sont explicitement conservés comme anomalies. Pas de signature supplémentaire d'ancien boot NTFS/exFAT/FAT dans l'espace libre selon les motifs contrôlés ; les secteurs de boot actuels ne permettent pas de dater leur création.

**Conclusion limitée :** structure actuelle globalement cohérente, avec anomalies d'allocation précisées. **Aucun formatage daté n'est démontré.** Une FAT cohérente, un FSInfo exact et des résidus anciens ne permettent pas d'exclure tout formatage rapide antérieur, copie de structures, écrasement ou opération sans trace survivante. Un reset d'horloge, une remise à zéro des réglages caméra et un formatage de la carte sont des opérations différentes.

## 11. Recoupements, classement et limites

| Niveau | Conclusion et justification |
| --- | --- |
| Observation confirmée — confiance élevée | Intégrité EWF ; inventaire indépendant ; 326 fichiers et 115 dossiers supprimés ; 315 premiers clusters réutilisés ; récupérations vérifiées ; nom impossible ; date FAT 2000 ; allocations sans référence |
| Fonctionnement normal fortement étayé | Remplacement circulaire : saturation, enregistrements postérieurs, suppressions groupées anciennes et réutilisation intérieure aux fichiers actuels |
| Dysfonctionnement plausible | Horloge/métadonnées de référence, anomalie de nom, finalisation interrompue ; causes individuelles indéterminées |
| État anormal confirmé ; modification historique non établie | Incohérence de nom et anomalies structurelles/allocation décrites ; **aucune transformation historique attribuable d’un fichier initialement sain, ni modification malveillante du contenu, n’est démontrée** |
| Intervention intentionnelle ou malveillante démontrée | **Aucune établie** par cette investigation |
| Impossible à trancher | Existence/date des resets rapportés, sort exact de toutes les vidéos anciennes, auteur et motivation des opérations |

Recoupement SD-01/SD-02 : organisation `record`/`.record_tmp`, marqueurs et modèle `moov` communs, même géométrie et identifiant de volume ; ce sont des concordances de format de stockage, **pas une preuve d'une opération commune ni d'un matériel identique**. Comparaison par SHA-256 des fichiers actifs : **1 concordance(s)** consignées dans la synthèse, la seule concordance concerne **`.rw`, fichier vide** ; aucune vidéo active identique à une vidéo active SD-01 n'est identifiée par cette comparaison. Seuls les fichiers comparés sont couverts. Leurs caméras et périodes disponibles sont distinctes. SD-01 conserve des fichiers de février/mars et octobre ; SD-02 est presque pleine de vidéos de novembre et nécessite des récupérations d'anciens contenus.

Limites déterminantes : pas d'accès aux réglages/micrologiciel de la caméra, aux journaux de son application ou au compte cloud ; pas de journal d'accès ou d'effacement FAT ; pas d'horloge civile étalonnée ; source exacte des observations de la cliente inconnue ; contenus écrasés non restaurables par simple récupération logique ; décodage actif ciblé et examen visuel de seize images seulement ; aucune garantie cryptographique d'origine des vidéos avant acquisition. Les fragments compressés sans début identifiable ne sont pas assimilés à des vidéos autonomes.

Pistes utiles si des éléments deviennent disponibles : source exacte de l'affichage 1999 et du signalement du 15 octobre, exports d'application/cloud, modèle et version de micrologiciel, essais de fonctionnement sur une **autre carte**, journaux du poste ayant traité le volume, procès-verbaux pour les horaires. Aucun de ces éléments manquants n'est remplacé par une supposition.

## 12. Annexes techniques et reproductibilité

### Artefacts principaux

| Référence | Objet |
| --- | --- |
| A01 | `journaux/ewfverify-sha256.txt`, `segments-sha256*.txt`, `ewfinfo.txt`, `provenance.txt` : source et intégrité |
| A02 | `inventaires/lecture-fat*.json`, `orphelins-slots.json`, `inventaire.csv`, `fls.txt` : entrées et géométrie |
| A03 | `chronologie.csv`, `par-jour.csv`, `intervalles.csv`, `timeline*` : dates nominales, FAT et durées |
| A04 | `inventaires/medias/`, `synthese-medias.json`, `anomalies-medias.json`, journaux de décodage : contrôles vidéo |
| A05 | `recuperations.json`, `recuperation-fragment-final.json`, `prive/recuperations/` : contenus supprimés récupérés et preuves |
| A06 | `reconstructions-temporaires.json`, `complements-index.json`, `prive/reconstructions/` : temporaire, y compris essai invalide |
| A07 | `espace-libre.json`, `residus-classes.json`, `residus-synthese.json`, `allocation.json`, structures brutes : résidus et FAT |
| A08 | `apercus-index.json`, `prive/apercus/` et observations du § 8 : contrôles visuels limités |

Les empreintes individuelles des vidéos sont dans les index JSON et le manifeste global. Les octets extraits sont des preuves **dérivées**, pas de nouvelles acquisitions physiques. Les médias privés ne doivent pas être ajoutés à Git ; leur présence sur disque dans le projet est intentionnelle.

### Commandes et scripts

Journal des commandes SSH, paramètres, scripts, heures UTC et codes de retour : [commandes JSONL](recherche-SD-02/20261016/journaux/commandes.jsonl). Guide d'exécution : [reproductibilité](recherche-SD-02/20261016/REPRODUCTION.md). Scripts : [collecteur](scripts/sd02_collect.py), [lecture FAT](scripts/sd02_rawfat_remote.py), [plan/jointure](scripts/sd02_plan.py), [médias](scripts/sd02_media_remote.py), [scanner](scripts/sd02_scan_remote.py), [récupérations](scripts/sd02_recover_remote.py), [fragment terminal](scripts/sd02_partial_remote.py), [temporaire](scripts/sd02_finalize_temp_remote.py), [synthèse](scripts/sd02_analyze.py).

Exemples représentatifs **en lecture seule**, sorties redirigées sur le poste du projet :

```bash
ssh -F /home/chris/.ssh/config sift \
  'sudo -n ewfverify -q -d sha256 /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-02/SD02.E01'
ssh -F /home/chris/.ssh/config sift 'sudo -n mmls /mnt/ewf-sd02/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fsstat -o 8192 /mnt/ewf-sd02/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fls -o 8192 -r -p /mnt/ewf-sd02/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n istat -z UTC -o 8192 /mnt/ewf-sd02/ewf1 1072'
ssh -F /home/chris/.ssh/config sift 'sudo -n icat -r -o 8192 /mnt/ewf-sd02/ewf1 575101256'
```

Un `icat -r` reste heuristique lorsque la chaîne a disparu. Les commandes de récupération ne doivent pas être redirigées vers FORENSIC. Les scripts de réception enregistrent toutes leurs sorties sous le répertoire de campagne du projet. Les dépendances réutilisées sont les **fonctions pures** du parseur MP4 SD-01, dont l'empreinte est tracée ; aucun ancien script SD-01 avec effets de bord n'est exécuté.

Formule d'offset de cluster : `19 771 392 + (cluster − 2) × 16 384`. Formule de contre-vérification des identifiants FAT TSK : `3 + (offset_absolu_du_slot − 19 771 392) / 32`. Une reconstruction énumère ses clusters, son ordre, sa taille et son SHA-256 ; la portion terminale et le temporaire signalent explicitement la fabrication d'un conteneur dérivé.
