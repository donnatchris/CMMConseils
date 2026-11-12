# Analyse informatique de la carte SD-03

**Relecture de cohérence : 12 novembre 2026.** Harmonisation avec le [rapport final réorganisé](../RAPPORT-FINAL-SADEDINE-2026.md), sans nouvelle acquisition ni nouvelle analyse des supports. Les campagnes et décomptes techniques conservent leurs dates et leurs périmètres. Le détail de cette révision et les empreintes actuelles figurent dans le [dossier de relecture](../investigations/20261112-coherence-rapports/compte-rendu.md).

## Actualisation du 10 novembre 2026 — lecture courante

Le PV est disponible et a été consulté. Les repères à retenir sont la mise sous scellés après 14 h 19 le 15 octobre, l’ouverture du PC à 10 h 41 et celle des téléphones à 11 h 30 le 28 ; 10 h 22 est l’arrivée de la cliente et 19 h 20 la clôture, sans heure individuelle de restitution. Les mentions d’indisponibilité et bornes déclaratives des sections datées ci-dessous décrivent leurs campagnes historiques. Les caméras et cartes n’étaient pas sous scellés. Les nouvelles traces système TP-03 ne prouvent ni un accès aux caméras ni une modification des vidéos. Cette relecture ne réexécute pas les scans/récupérations SD ; elle maintient les anomalies, lacunes et limites déjà établies. Voir la [relecture transversale](../investigations/20261110-telephones/compte-rendu.md), qui distingue les nouveaux contrôles des reprises documentaires. Les empreintes historiques des rapports restent attachées à leurs versions datées.


## Actualisation du 19 octobre 2026 — salon, période ancienne et téléphones

Le [nouveau mail](../docs/mail-2.txt) demande l’examen depuis l’installation déclarée après mars 2023. La relecture des noms conservés sur SD-03 couvre **175 jours entre le 04/11/2023 et le 31/10/2024**, sans continuité garantie ; 125 lignes portent février 2024 et 65 le 15 octobre. La signature de finalisation avec date 2000 existe dès novembre 2023. Le signalement de réinitialisation en **février 2024** concerne explicitement la **chambre** ; les cas du salon sont des comparaisons techniques, pas la provenance démontrée de ce signalement.

La cliente rapporte l’allumage des téléphones vers 13 h 30 le 15 pendant son absence. La contre-lecture de l’image conservée affichant **13:30:21** montre plusieurs personnes et des objets sur une table, **sans démontrer un allumage, un branchement ni l’identité ou le rôle des personnes**. Aucun visionnage intégral ou analyse audio sémantique supplémentaire n’est revendiqué. L’erreur vidéo intermédiaire vers 13:30:05 et la fin des images vers 13:32:26 ne sont pas attribuées à ce geste déclaré.

Les enregistrements manquants du 16 au 28 ne démontrent pas leur cause. Le PV n’était pas disponible lors de cette campagne d’octobre ; il a depuis été consulté le 8 novembre. Voir la [réponse détaillée et les limites](../investigations/20261019-retour-cliente/compte-rendu.md).


**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils.  
**Prestataire :** Christophe Donnat — Donnat Dev.  
**Campagne :** 16 octobre 2026. Investigation technique indépendante, non expertise judiciaire.  
**Image :** SD-03 ; description EWF « salon », arborescence `CAMERA SALON`.

**Observation distincte rapportée le 12 novembre :** le prestataire indique que son visionnage des vidéos du salon montre une agente de l’administration fiscale rallumant les téléphones le **15 octobre vers 13 h 25**. Cette observation, reprise au [§ 1.2 du rapport final](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés), ne résulte pas des seuls aperçus du clip commençant à **13 h 28** contrôlés lors de la campagne antérieure. Aucun nouveau visionnage indépendant n’est réalisé ici ; ni une heure précise d’extinction ultérieure ni l’état des téléphones à la fermeture ne sont établis. Cette observation ne démontre pas la cause de l’anomalie vidéo ni de la lacune suivante.

## Questions auxquelles l'analyse tente de répondre

1. Peut-on récupérer des vidéos effacées ou des portions devenues inaccessibles ? Que distingue-t-on entre fichiers actifs, temporaires supprimés et fragments ?
2. Les enregistrements ou le système de fichiers ont-ils subi des modifications anormales ? Peut-on établir une intervention intentionnelle ou malveillante ?
3. Que démontrent les traces associées à février 2024, à l'affichage « 31/12/1999 » et au **15 octobre 2024** ? Peut-on confirmer une réinitialisation ?

**Les caméras n'ont jamais été placées sous scellés.** Leurs enregistrements après la perquisition ne constituent pas une anomalie pour cette seule raison. L'origine exacte des observations de la cliente demeure inconnue ; l'hypothèse d'une consultation des métadonnées n'est pas une provenance authentifiée.

## Conclusions simples à présenter à l'avocate

- **SD-03 contient 2 431 vidéos actives, dont 65 du 15 octobre 2024.** Les noms vont du 4 novembre 2023 au 31 octobre 2024. Les heures sont celles déclarées par la caméra, sans étalonnage civil indépendant.
- **Une anomalie réelle concerne la dernière vidéo du 15 octobre et son dossier : leur date FAT est le 1er janvier 2000.** Les images examinées portent pourtant une incrustation du **15 octobre 2024**. Ce décalage peut expliquer une interrogation fondée sur les métadonnées ; il ne prouve pas qu'une remise à zéro de la caméra ait été effectuée ce jour-là.
- **Le même type d'anomalie touche sept vidéos de février et une de novembre 2023.** Les neuf fichiers ont une erreur arithmétique commune dans leur dernière entrée de table audio. Un dixième fichier, daté normalement de décembre 2023, présente un autre défaut de compteur. Cela étaye fortement des défauts récurrents de finalisation ou de reconstruction des fichiers. Un redémarrage avec horloge non synchronisée reste une explication possible ; il n'est pas directement démontré.
- **Les dernières images contrôlées du 15 octobre affichent 13:32:26.** Aucun MP4 référencé ne se situe du 16 au 28 octobre ; les noms suivants sont du 29 octobre à 17:59:18. Cette lacune est constatée, mais sa cause n'est pas établie. Elle ne prouve ni une suppression ni une caméra restée hors service pendant toute la période.
- **Aucune vidéo supprimée distincte et complète n'a été récupérée.** Les trois fichiers supprimés retrouvés sont des temporaires associés à une vidéo finalisée encore présente. La concordance des octets et des tables étaye fortement un nettoyage après finalisation.
- **Un fragment supplémentaire de 3,849 secondes a été restauré**, à la fin d'un fichier actif endommagé du 29 février. Il provient de données au-delà de la taille logique du fichier et passe le décodage sans avertissement. Il est séparé des vidéos supprimées et son conteneur est explicitement reconstruit.

**Ce qui n'est pas démontré :** une réinitialisation aux dates signalées, un formatage daté, une modification intentionnelle ou malveillante, un accès distant, ou l'identité de l'auteur d'une opération. Les traces ne permettent pas davantage de garantir l'absence de toute intervention antérieure.

## Hypothèses pouvant expliquer les anomalies

| Observation | Explications compatibles | Qualification |
| --- | --- | --- |
| Dates FAT de 2000, images datées de 2023/2024 et tables MP4 défectueuses | Finalisation/récupération défaillante ; date de référence ; horloge non initialisée ou corrigée ; traitement ultérieur | **Défaut de tables confirmé**, mécanisme commun fortement étayé ; cause de la date et moment réel d'écriture indéterminés |
| Dernière vidéo du 15 octobre affectée puis lacune | Arrêt/reprise, alimentation, réglages ou absence de déclenchements, données effacées sans traces survivantes | Hypothèses possibles ; aucune cause unique établie |
| Temporaires supprimés avec contenu final toujours présent | Finalisation puis nettoyage des auxiliaires | Fonctionnement normal **fortement étayé** par plusieurs concordances |
| Octets vidéo au-delà de la taille logique d'un fichier abîmé | Taille finale et tables mal mises à jour, interruption d'écriture ou récupération incomplète | Anomalie d'allocation/finalisation confirmée, intention inconnue |
| Changement de cadrage dans les images | Mouvement motorisé, suivi, commande ou déplacement ; réglages inconnus | Observation visuelle ; aucun accès distant ni auteur identifiable |
| `System Volume Information` daté du 12 novembre 2024 | Traitement du volume dans un environnement compatible Windows | Métadonnées confirmées ; ne prouve pas un visionnage ni son auteur |

La cause qui a écrit une mauvaise date et la façon dont une interface aurait affiché « 31/12/1999 » sont deux questions distinctes (§ 9).

## 1. Périmètre, contexte et sources

Sources de référence : [mail original](../docs/mail.txt), notamment son § 4 ; [attestation de remise](../remise-documents/attestation-de-remise.md) ; [rapport d'acquisition](analyse-cartes_sd.md) ; [contexte corrigé de la mission](recherche-SD-01/20261016-complement/sources/contexte-et-observations.md). Le premier mail disait « en février » sans année. Le nouveau mail précise **février 2024 et la chambre**, sans interface ou fichier authentifié ; les anomalies SD-03 restent des éléments de comparaison.

L'heure du début de perquisition n'est pas documentée dans ces sources. **13 h 30 correspond à la perte d'accès aux téléphones**, pas à une heure de début vérifiée ni à une synchronisation avec la caméra. La campagne initiale n’utilisait pas le PV ; sa lecture du 8 novembre précise depuis les horaires de procédure, sans étalonner l’horloge caméra.

L'attestation décrit trois cartes de 32 Go, marque transcrite « ScanDisk », sans série physique confirmée. L'identification SD-03 repose sur les références d'acquisition et les champs EWF. Le numéro USB `121220160204` désigne le **lecteur**, pas une série propre à la carte. Aucune identification physique supplémentaire de SD-03 ou du modèle/micrologiciel de caméra n'est établie par les éléments examinés.

Niveaux : **observation confirmée**, **interprétation fortement étayée**, **hypothèse possible**, **absence de preuve**, **limitation**. Aucune date, corruption ou suppression technique n'est assimilée à une intention. Aucun rôle ni identité n'est attribué aux personnes visibles.

## 2. Image, provenance, intégrité et préservation

Source en lecture uniquement :

```text
/media/shared/forensic/SADEDINE-2026/ANALYSES/SD-03/SD03.E01 à SD03.E12
```

Douze segments EWF EnCase 6, deflate. Description EWF : « Carte SD contenant les enregistrement vidéo des caméras (salon) », dossier `SADEDINE-2026`, pièce `SD-03`, examinateur Christophe Donnat. Vue `/mnt/ewf-sd03/ewf1`, **31 914 983 424 octets**, mode **0444**, créée pour la lecture ; les dates du fichier FUSE reflètent cette vue, pas les dates des enregistrements.

| Contrôle | Résultat | Preuve |
| --- | --- | --- |
| Vérification du conteneur et des données | `ewfverify: SUCCESS` | [ewfverify](recherche-SD-03/20261016/journaux/ewfverify-sha256.txt) |
| MD5 enregistré et recalculé | `d0402e436587d9cb319f78575e81fec0` | Même sortie |
| SHA-256 du flux décompressé | `7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0` | Même sortie ; concorde avec l'acquisition |
| Douze empreintes SHA-256 de segments | Identiques au début et au contrôle final | [début](recherche-SD-03/20261016/journaux/segments-sha256.txt), [fin](recherche-SD-03/20261016/journaux/segments-sha256-fin.txt) |

Le SHA-256 logique n'était pas enregistré dans les segments EWF ; il a été recalculé et comparé au document d'acquisition. Guymager indique acquisition du **12/10/2026 à 14:03:19**, fin à **14:35:50**, vérification d'image activée, vérification de source désactivée et aucun secteur défectueux signalé. L'affirmation documentaire de deux empreintes source/image identiques ne constitue pas une seconde lecture indépendante de la carte physique. La rubrique SD-03 comporte aussi un libellé « SD-01 » dans sa phrase de branchement ; cette discordance rédactionnelle est signalée, sans modifier le document source.

L'image a été lue sans montage FAT, sans réparation ni écriture sur FORENSIC. Le partage source n'est pas présenté comme un bloqueur matériel. Les empreintes établissent la conservation du contenu des segments pendant cette campagne ; la chaîne de conservation antérieure n'est pas intégralement auditée ici.

Toutes les sorties persistantes sont dans le projet. Les médias traités dans SIFT sont placés dans des descripteurs anonymes en mémoire (`memfd`), fermés après usage. Les essais de correction touchent **ces seules copies RAM**. Aucun secteur ni fichier de l'image originale n'a été corrigé. La cohérence de l'image acquise n'implique pas celle de chacun des MP4 qu'elle contient.

Preuves initiales : [identification et montage](recherche-SD-03/20261016/journaux/etat-initial.txt), [SD03.info et provenance](recherche-SD-03/20261016/journaux/provenance.txt), [ewfinfo](recherche-SD-03/20261016/journaux/ewfinfo.txt).

## 3. Méthode, environnement et portée effective

SIFT via `ssh -F /home/chris/.ssh/config -o BatchMode=yes sift`, configuration utilisateur explicite de l'hôte demandé. Linux 6.8.0-110 ; Python **3.12.3** ; Sleuth Kit **4.11.1** ; libewf-tools **20140816** ; FFmpeg/FFprobe **6.1.1** ; PhotoRec/TestDisk **7.1** disponible. Tesseract et le filtre OCR FFmpeg sont absents ; aucune installation n'a été réalisée. Les incrustations citées ont été lues visuellement par l'assistant. Versions : [outils](recherche-SD-03/20261016/journaux/outils.txt), [disponibilité OCR](recherche-SD-03/20261016/journaux/disponibilite-ocr.txt).

Ordre : intégrité ; partition/BPB/FAT ; inventaire TSK et contre-lecture de slots ; chronologie ; analyse et récupération des fichiers ; scan des zones libres, slack et allocations sans référence ; horloges et finalisation ; comparaisons ; contrôle final. Aucune conclusion SD-01/SD-02 n'est transposée à SD-03. Les résultats antérieurement vérifiés de ces cartes servent uniquement aux recoupements expressément indiqués.

**Exécution :** lecture et SHA-256 de tous les fichiers actifs, FFprobe et examen des tables sur tous les MP4, contrôle des temps de paquets ; décodage intégral ciblé de **387 fichiers actifs**, dont **les 65 vidéos du 15 octobre**, les neuf anomalies de date et des témoins premier/dernier par jour. Des contrôles prioritaires indépendants et le décodage image par image des neuf cas de date ont complété le lot. Les durées de conteneur, audio, vidéo et images effectivement produites sont séparées.

L'assistant a effectivement examiné **23 PNG** ; ce n'est pas un visionnage humain intégral des 2 431 vidéos. Les autres aperçus générés ne sont pas cités comme s'ils avaient tous été examinés. Aucune analyse audio sémantique ni identification personnelle n'est revendiquée. [observations visuelles et empreintes](recherche-SD-03/20261016/inventaires/observations-visuelles.json).

Stockage : environ 15 Gio disponibles initialement ; conservation sélective plafonnée à 2 Gio pour le lot principal, puis petits compléments ciblés. Pas de copie brute supplémentaire de 31,9 Go ni d'extraction aveugle de tout l'espace libre. Les récepteurs refusent chemins hors projet, liens, écrasements et dépassements de taille. Les médias/blocs sensibles sont exclus de Git par des règles ajoutées à `.gitignore`, sans retirer les règles précédentes.

Un transfert de résidus a été interrompu (code 143, cause indéterminée). **5 311 blocs reçus ont été vérifiés**, un fichier de zéro octet conservé comme incomplet, puis seulement les **6 266 blocs restants** ont été transférés. La classification partielle a été isolée comme non valide et remplacée par une nouvelle classification complète. Un premier test de table a aussi échoué sur une incompatibilité `bytearray`/`bytes`, corrigée avant toute conclusion. Ces incidents d'outillage n'affectent pas l'image ; les versions et sorties d'erreur sont conservées dans les [incidents](recherche-SD-03/20261016/incidents-et-limites.md).

## 4. Partition et système de fichiers

| Paramètre | Valeur vérifiée |
| --- | --- |
| Partition FAT32 0x0c | Secteurs absolus **8192 à 62333951**, jusqu'au bout de l'image |
| Secteur / offset de partition | 512 octets / **4 194 304 octets** |
| Cluster | **16 384 octets**, 32 secteurs |
| Réservés / FAT | 6 secteurs / deux FAT de **15 209 secteurs** chacune |
| Premier octet de la zone de clusters | **19 771 392**, cluster 2 |
| Clusters de données | **1 946 729** |
| Libres / non libres | **471 351 / 1 475 378** ; occupation environ **75.79 %** |
| Référencés / alloués sans référence active | **1 475 375 / 3** |
| Queue hors clusters complets | Huit secteurs, **4 096 octets** |

Tous les appels Sleuth Kit visant le système de fichiers utilisent **`-o 8192`**. Les offsets bruts sont absolus en octets ; les secteurs de boot/FAT indiqués relativement au volume sont explicitement distingués. Preuves : [mmls](recherche-SD-03/20261016/journaux/mmls.txt), [fsstat](recherche-SD-03/20261016/journaux/fsstat.txt), [contre-lecture FAT](recherche-SD-03/20261016/inventaires/lecture-fat.json).

Les deux FAT ont le SHA-256 :

```text
19d943e6f80a9d9e63c707f486f833c7d1753f8d1a324bd0569cbdd0b6db374d
```

Le FSInfo principal est valide : **471 351 clusters libres**, prochain suggéré **1 487 215**, exactement cohérent avec la lecture de FAT. La sauvegarde comporte **1 946 728 libres**, prochain **2**, compatible avec des valeurs initiales non actualisées. Le boot et sa sauvegarde ne diffèrent qu'à **0x41**, valeur 1 contre 0 ; ce champ n'est pas une date.

OEM `mkdosfs`, FAT32, identifiant de volume **0x6546a41d**, champ des secteurs cachés **0** malgré le début de partition à 8192. Les valeurs sont constatées sans attribuer une date de formatage, un outil réellement exécuté ou une série matérielle. L'identifiant diffère de celui de SD-01/SD-02 ; la géométrie commune ne prouve pas une même opération.

## 5. Inventaire et chronologie

| Type d'entrée, hors racine et alias | Nombre |
| --- | ---: |
| Fichiers actifs | **2 434** |
| Dont vidéos MP4 sous `CAMERA SALON/record/` | **2 431** |
| Autres actifs | **3** : `.rw` vide, `WPSettings.dat` (12 octets), `IndexerVolumeGuid` (76 octets) |
| Répertoires actifs | **179** |
| Fichiers supprimés | **3**, sous `.record_tmp` |
| Répertoire supprimé | **1**, `_CIM`, premier caractère perdu |

Inventaire TSK et contre-lecture FAT concordent **sans écart**. Aucun slot orphelin supplémentaire n'a été nécessaire. La présence d'un ancien pointeur ne signifie pas que son contenu antérieur soit encore disponible. Le dossier supprimé `_CIM` pointe actuellement sur le même cluster initial que l'arborescence active `CAMERA SALON` ; le caractère initial perdu ne peut être restitué avec certitude.

Fichiers CSV/JSON : [inventaire](recherche-SD-03/20261016/inventaires/inventaire.csv), [fls brut](recherche-SD-03/20261016/inventaires/fls.txt), [jointure](recherche-SD-03/20261016/inventaires/etat-inventaire.json), [chronologie détaillée](recherche-SD-03/20261016/inventaires/chronologie.csv), [par jour](recherche-SD-03/20261016/inventaires/par-jour.csv), [bodyfile](recherche-SD-03/20261016/inventaires/timeline.body), [mactime](recherche-SD-03/20261016/inventaires/timeline-mactime.csv).

Les noms couvrent **175 jours représentés**, du **4 novembre 2023 au 31 octobre 2024**. Répartition :

| Mois nominal | Jours représentés | MP4 |
| --- | ---: | ---: |
| 2023-11 | 18 | 308 |
| 2023-12 | 17 | 220 |
| 2024-01 | 10 | 141 |
| 2024-02 | 8 | 125 |
| 2024-03 | 13 | 140 |
| 2024-04 | 20 | 131 |
| 2024-05 | 13 | 84 |
| 2024-06 | 12 | 460 |
| 2024-07 | 12 | 129 |
| 2024-08 | 18 | 448 |
| 2024-09 | 21 | 146 |
| 2024-10 | 13 | 99 |

Les **2 431 noms** de vidéos ont une date syntaxiquement valide et aucune paire de fichiers actifs n'est identique par SHA-256 sur SD-03. Tous les MP4 déclarent une vidéo **H.264 1920 × 1080** et un audio **AAC mono 8 kHz** ; leurs deux descriptions de pistes ont les mêmes empreintes dans le lot. Ces concordances techniques n'authentifient pas l'absence d'un traitement antérieur.

Le suffixe est compatible avec une **durée approximative**, pas une numérotation de séquence : différence durée du conteneur moins suffixe de **0.016 à 1.608 s**. Le champ `_10` n'est pas interprété faute de documentation. De nombreux fichiers avoisinent 300 s ; les réglages de déclenchement et de découpage ne sont pas disponibles. Une absence de clip n'est pas automatiquement une suppression.

Les heures de noms/FAT/incrustations restent déclaratives. UTC est une **convention d'affichage TSK**, pas une synchronisation démontrée ; FAT ne stocke pas de fuseau. L'écriture a une granularité de deux secondes, la création un champ supplémentaire de précision, l'accès essentiellement une date de jour. Les dates nulles rendues par mactime ne sont pas des événements réels.

Les écarts calculés, y compris les petits chevauchements et grandes lacunes, sont conservés dans [intervalles quotidiens](recherche-SD-03/20261016/inventaires/intervalles.csv) et [intervalles entre tous les fichiers successifs](recherche-SD-03/20261016/inventaires/intervalles-globaux.csv). Les fins estimées reposent sur les métadonnées et doivent être réévaluées pour les fichiers défectueux. La plus grande lacune interne quotidienne calculée est **79199.968 s**, de `2024-08-13 00:53:31.032000` à `2024-08-13 22:53:31` ; sa cause n'est pas déterminée par cette carte seule.

## 6. Entrées supprimées et récupération

Trois entrées supprimées :

| TSK | Fichier sous `.record_tmp/` | Taille déclarée | Extraction `icat -r` |
| --- | --- | ---: | ---: |
| 1543 | `20241031_232538_10.mp4` | **2 123 808** | **16 384** octets |
| 1547 | `20241031_232538_10.mp4.moov` | **1 006** | **1 006** octets |
| 1551 | `20241031_232538_10.mp4.stbl` | **10 784** | **10 784** octets |

La chaîne historique du temporaire n'est pas récupérée. Son premier cluster (**1487054**) est aussi celui du fichier actif **761370124**, `20241031_232538_10_0028.mp4`, **2 617 249 octets**, durée du conteneur **29,056 s**, décodage sans avertissement. Les **16 384 octets** extraits sont identiques au début du fichier final. Ils correspondent à un même emplacement actuel : cette identité ne garantit pas que ces octets soient inchangés depuis la suppression.

Le journal `.stbl`, analysé sur ses **10 784 octets logiques**, concorde avec le fichier final sur les cinq séries examinées : tailles vidéo/audio, offsets vidéo/audio, numéros de synchronisation vidéo. Les préfixes ont respectivement **266 / 182 / 27 / 26 / 266 valeurs**. Le modèle `.moov` est un modèle auxiliaire, pas une autre vidéo.

**Interprétation fortement étayée :** les trois entrées sont associées au processus de création/finalisation de la vidéo encore présente. Il n'y a pas d'élément positif établissant l'effacement volontaire d'un enregistrement distinct. La FAT ne conserve pas la date d'effacement ni l'auteur ; les horodatages des temporaires ne datent pas automatiquement leur suppression.

Preuve : [comparaisons, tailles et SHA-256](recherche-SD-03/20261016/inventaires/comparaison-temporaires.json), [réutilisations](recherche-SD-03/20261016/inventaires/supprimes-reutilisation.csv), `journaux/istat/1543.txt`, `1547.txt`, `1551.txt`. Les extraits sont sous `prive/priorite/` et `prive/extraits/`. **Aucune vidéo supprimée complète supplémentaire** n'est annoncée à partir de ces fichiers.

### Fragment d'un fichier actif restauré au-delà de EOF

Le fichier actif **266342024**, `20240229_112725_10_0020.mp4`, déclare **1 169 358 octets**, mais sa chaîne FAT compte **143 clusters**, soit **2 342 912 octets**. Les tables référencent notamment des données au-delà de la taille logique et de la fin du `mdat` actuel. La lecture ordinaire ne produit que **222 images**, dernière PTS **15,470 s**, contre **295 images** annoncées.

Des échantillons vidéo subsistent après EOF, aux positions indiquées par les tables. Un essai borné a retenu une portion démarrant sur une image intra analysée, au temps relatif original **16,802 s** ; les échantillons et leurs positions sont listés. Un **nouveau conteneur** réindexe cette portion, sans inventer ni réencoder les images. Résultat : **3,849 s**, taille **328 426 octets**, décodage intégral sans avertissement. Les aperçus effectivement examinés affichent **29/02/2024 11:27:41 à 11:27:45**, cohérents avec cette fin d'enregistrement.

Ce résultat est une **récupération partielle de données résiduelles d'un fichier actif endommagé**, pas la découverte d'une vidéo effacée distincte ni la restauration complète du fichier. Les pistes sont remises séparément à zéro ; un léger décalage audio/vidéo peut en résulter. Les autres octets excédentaires ne sont pas tous assimilés à une suite vidéo validée.

Artefact : `prive/reconstructions/266342024-fragment-apres-EOF.mp4`. Provenance, chaîne, positions de chaque échantillon, hypothèses, empreintes et contrôles : [récupération après EOF](recherche-SD-03/20261016/inventaires/recuperation-apres-eof.json). Les trois autres chaînes excédentaires examinées n'ont pas fourni de continuation vidéo : leurs clusters excédentaires sont nuls.

## 7. Recherche dans les zones libres et résiduelles

**7 722 614 784 octets libres ont été lus intégralement**, sans échantillonnage. **11 577 clusters non nuls** ont été conservés ; les autres sont nuls. SHA-256 du flux libre concaténé en ordre croissant :

```text
78870ea13eb832a60d674d17ea71b8c41f7139c0b53374324d1bff1bc41e1102
```

| Constat dans l'espace libre | Résultat |
| --- | ---: |
| Signatures `ftyp` / `mdat` | **0 / 0** |
| Modèles `moov` de 1 006 octets | **2 427**, même SHA-256 |
| Journaux auxiliaires / fragments | **4 959 / 4 191** |
| Clusters non classés après reprise complète | **0** selon les critères de grammaire employés |
| Slots MP4 répondant aux critères et absents de l'inventaire | **0** |

Les modèles ont le SHA-256 `731c49c0eb32815913b66158889c78a53f83fcea0e661589ac633b8fa5c26e15`, identique au modèle observé sur les autres cartes. Les journaux sont identifiés par une grammaire inférée ; une structure auxiliaire ou une signature isolée n'est pas une vidéo. Les limites d'interprétation des préfixes/suffixes de fragments sont quantifiées dans [détails des résidus](recherche-SD-03/20261016/inventaires/residus-details.json).

**Trois clusters alloués sans référence active**, **552486, 552487 et 552488**, sont entièrement nuls, chacun une chaîne terminée. Ils ne livrent aucune vidéo. Le slack des fichiers actifs représente **20 239 422 octets**, dont **10 194 non nuls**. Ses empreintes et signatures candidates sont conservées ; les octets au-delà d'une taille logique ne sont pas automatiquement attribués au contenu courant. Le fragment du § 6 a nécessité des contrôles spécifiques.

Les régions avant la partition (4 Mio), les secteurs réservés et les huit secteurs finaux ont été conservés et inspectés. Les seules signatures FAT reconnues dans ces régions sont les boot actuel et de sauvegarde. La recherche de signatures d'anciens systèmes de fichiers dans le libre n'en identifie pas selon les motifs consignés ; cela n'exclut pas tout formatage antérieur ni des traces écrasées.

Preuves : [scan complet](recherche-SD-03/20261016/inventaires/espace-libre.json), [classification](recherche-SD-03/20261016/inventaires/residus-classes.json), [synthèse](recherche-SD-03/20261016/inventaires/residus-synthese.json), [allocation et slack](recherche-SD-03/20261016/inventaires/allocation.json), [exports complémentaires](recherche-SD-03/20261016/inventaires/complements-index.json).

Aucun PhotoRec SD-03 n'a été exécuté : la recherche spécialisée du libre est exhaustive sur les motifs documentés et a été complétée par les zones allouées résiduelles. Les résultats PhotoRec de SD-01 ne valent pas pour cette carte. **Une absence de nouvelle récupération ne prouve pas qu'aucun effacement n'ait eu lieu.**

## 8. Dates de 2000 et anomalies MP4

### 8.1 Neuf fichiers et un dossier concernés

Les neuf fichiers portent des créations/écritures FAT entre **00:00:26 et 00:00:28 le 01/01/2000**, selon la contre-lecture des champs bruts, avec quelques différences d'une seconde liées au champ de précision de création. Aucune date FAT explicite de 1999 n'est identifiée dans les entrées examinées.

| Nom de vidéo | TSK | Durée audio / vidéo, s | Images produites / déclarées |
| --- | ---: | ---: | ---: |
| 20231109_181905_10_0039.mp4 | 12727332 | 39.424 / 39.901 | 547 / 570 |
| 20240221_232237_10_0190.mp4 | 261989424 | 190.848 / 190.842 | 2701 / 2726 |
| 20240221_233345_10_0077.mp4 | 261989436 | 77.056 / 77.707 | 1051 / 1110 |
| 20240221_234103_10_0044.mp4 | 261989444 | 43.904 / 44.101 | 587 / 630 |
| 20240229_102610_10_0047.mp4 | 266341920 | 46.592 / 47.113 | 673 / 673 |
| 20240229_105600_10_0006.mp4 | 266341968 | 5.376 / 6.299 | 30 / 90 |
| 20240229_110139_10_0116.mp4 | 266341984 | 116.48 / 116.702 | 1621 / 1667 |
| 20240229_112725_10_0020.mp4 | 266342024 | 20.608 / 20.651 | 222 / 295 |
| 20241015_132800_10_0277.mp4 | 714049800 | 277.76 / 266.171 | 3802 / 3802 |

Les durées annoncées ne garantissent pas que toutes les images correspondantes existent ou soient correctement décodables. Par exemple, le fichier de six secondes du 29 février ne produit que **30 images**, dernière PTS **2,026 s**, contre 90 annoncées. Les compteurs et fins effectivement observables sont dans [contrôle des images](recherche-SD-03/20261016/inventaires/frames-cibles.json), ses sorties FFprobe et journaux.

Les premiers/derniers aperçus de chacun de ces fichiers gardent les dates 2023/2024 de leurs noms. Ce constat concerne les images examinées, pas chaque image intermédiaire ni le moment où les métadonnées FAT ont été écrites. Le temps exact d'une opération produisant ces dates de 2000 reste indéterminable à partir de cette date incohérente.

### 8.2 Motif commun de table audio et expérience de contrôle

Dans les **neuf cas**, la dernière entrée audio `stsc` reprend le **nombre cumulé des échantillons précédents**, au lieu du nombre restant attendu d'après `stsz`. Les trois témoins normaux examinés ne présentent pas cette erreur. Une dixième anomalie d'index, sans date FAT de 2000, est distinguée ci-dessous : le motif arithmétique des neuf cas n'est pas assimilé à toutes les erreurs MP4. Exemple du 15 octobre : **2 170 échantillons**, **2 163 dans les chunks précédents**, donc **7 restants** ; le dernier champ vaut pourtant **2 163**. Ce n'est pas une simple interprétation de date : les nombres et offsets sont contrôlables.

Sur une **copie RAM** du fichier 714049800, ce seul compteur est remplacé par 7. L'avertissement FFprobe `wrong sample count` disparaît, tandis qu'une erreur vidéo H.264 subsiste. Aucun échantillon vidéo/audio ni horodatage n'est modifié par ce test sur l'index de la copie RAM ; les octets d'index modifiés, SHA-256 avant/après et commandes sont consignés. Aucune réparation de l'image n'est effectuée et ce test ne devient pas une vidéo originale restaurée.

**Observation confirmée :** erreur arithmétique commune, associée aux neuf dates FAT aberrantes. **Interprétation fortement étayée :** même défaut ou même chemin de finalisation/reconstruction de fichiers. **Hypothèse possible :** traitement après interruption ou redémarrage avant synchronisation de l'horloge. Le logiciel précis, le déclencheur, la date réelle et le caractère humain ou automatique ne sont pas établis. Une remise à zéro des réglages usine n'est pas démontrée.

Preuve : [analyse de finalisation et test](recherche-SD-03/20261016/inventaires/analyse-finalisation.json), `journaux/test-index-714049800.txt`, script [sd03_finalization_pattern_remote.py](scripts/sd03_finalization_pattern_remote.py).

### 8.3 Dates des dossiers, dates MP4 internes et autres contrôles

Sur **175 dossiers quotidiens**, la création dans l'entrée parent égale exactement celle du dernier fichier nommé dans **168 cas**, et l'écriture égale celle du dernier fichier dans **171 cas**. L'alias `.` garde exactement la création du premier fichier dans **167 cas**. Les écarts restants sont conservés, sans forcer les égalités.

Ce motif étaye une gestion des dates du dossier liée à la clôture/mise à jour des fichiers. Pour le **15 octobre**, l'entrée parent 1201 porte la même date 2000 que la dernière vidéo, tandis que `.` et `..` conservent **15/10/2024 08:02:36**. Les deux entrées datées de 2000 ne constituent donc pas à elles seules deux preuves de reset distinctes, ni une date de création civile fiable du dossier. [dates des dossiers](recherche-SD-03/20261016/inventaires/gestion-dates-dossiers.csv), [recoupements](recherche-SD-03/20261016/inventaires/evenements-focus.json).

Les **2 431 MP4** portent tous `creation_time=1970-01-01T00:00:00.000000Z`. Les cinq champs temporels bruts contrôlés par fichier valent tous **2 082 844 800**, correspondant ici à 1970 dans le repère MP4. Les valeurs brutes et les profils codec sont dans la [synthèse médias](recherche-SD-03/20261016/inventaires/synthese-medias.json). La répétition de la date **1970** dans des clips de plusieurs mois est fortement compatible avec une valeur par défaut du logiciel, sans valeur de date d'enregistrement effective. Ce champ est distinct des dates FAT de 2000.

Un autre fichier, **172620304**, `20231221_130102_10_0003.mp4`, porte des dates FAT cohérentes du **21/12/2023 13:01:06** et une durée de **3,987 s**. Son unique règle audio `stsc` annonce sept échantillons pour chacun des cinq chunks, soit 35, contre **31** dans `stsz`/`stts` ; le dernier chunk ne devrait en contenir que trois. FFprobe/FFmpeg signalent `wrong sample count`, sans autre avertissement de décodage dans ce contrôle ; les 58 paquets vidéo sont temporellement croissants et leurs références restent dans le fichier. Ce défaut de compteur terminal est distinct du cumul erroné observé dans les neuf fichiers de 2000. Il montre qu'une anomalie MP4 peut aussi survenir sans anomalie FAT, sans établir un reset ou une intervention. Preuves : [cas de décembre](recherche-SD-03/20261016/inventaires/anomalie-decembre.json), `inventaires/medias/172620304.json`, `journaux/decodage/172620304.txt`.

Bilan automatisé : **10 fichiers actifs avec anomalies de tables**, **0 avec erreurs de structure de boîtes**, **0 avec progression de paquets signalée**. FFmpeg retourne parfois zéro malgré des erreurs : les journaux font foi, pas le seul code de retour. Le décodage normal de fichiers témoins ne garantit pas l'absence d'un montage vidéo techniquement propre antérieur. Aucun dispositif de signature native des vidéos n'a été authentifié. [anomalies par fichier](recherche-SD-03/20261016/inventaires/anomalies-medias.json).

## 9. Réponses aux deux événements signalés

### 9.1 Février 2024 et affichage « 31 décembre 1999 »

**Trace d'origine :** déclaration de la cliente dans le mail, sans carte, fichier ni interface authentifiés. Le nouveau mail précise désormais février 2024 et la chambre ; le premier mail ne donnait pas ces précisions. Les sept vidéos du salon des 21/29 février portant des dates FAT de 2000 servent de **comparaison technique** avec les anomalies de la chambre. Elles ne sont pas la provenance établie de l’observation de la cliente concernant cette autre caméra.

**Ce qui est démontré :** sept fichiers nommés de février 2024 ont des dates FAT aberrantes, la même erreur audio et parfois des images manquantes ou données hors taille logique. Les images effectivement examinées affichent des dates de février 2024 ; aucune bascule vers 1999/2000 n'est observée dans ces échantillons. Le fragment de fin du 29 février est récupéré et daté dans l'image par la caméra.

**Explications compatibles :** pour le stockage, une date par défaut lors d'une finalisation/récupération défaillante, une horloge non synchronisée après interruption/redémarrage, ou un traitement ultérieur des métadonnées. Pour l'affichage « 31/12/1999 », une conversion de la date de référence vers un fuseau à l'ouest d'UTC pourrait produire la veille ; cette conversion n'est pas reproduite sur l'interface de la cliente, et Europe/Paris ne suffit pas à expliquer ce recul. La cause technique de la valeur stockée et son affichage doivent rester séparés.

**Une réinitialisation est-elle établie ?** **Non.** Les anomalies sont confirmées ; un redémarrage et un problème d'horloge sont compatibles. Le nombre, la nature et les dates civiles d'éventuelles réinitialisations ne peuvent pas être déduits du nombre de fichiers affectés. Aucun journal de boot, réglage usine, NTP ou application ne tranche.

Un rapprochement avec SD-01 mérite d'être conservé : son fichier `20240221_233914_10_0151.mp4`, également daté de 2000, a une fin nominale **23:41:45,924** ; SD-03 produit des images jusqu'à une PTS donnant nominalement **23:41:44,023**, soit **1,901 s d'écart**. C'est une piste d'événement technique commun, **sans preuve de coupure commune ni de synchronisation civile**. Le rapprochement utilise les résultats SD-01 antérieurement vérifiés, sans nouvelle analyse lourde de son image.

Le [complément transversal, § 4.1](analyse-cartes_sd-transversale.md#41-rapprochement-du-21-février-à-2341) précise que cet écart compare deux mesures différentes : fin nominale de piste et dernière image produite. Les comparaisons homogènes donnent **1,828 s** entre dernières PTS indexées produites et **1,177 s** entre fins vidéo de tables, dans l’autre ordre pour ce dernier calcul. Des images supplémentaires non indexées subsistent sur SD-01 ; aucune de ces valeurs ne date une coupure commune. La signature de compteur audio concerne onze vidéos sur les deux cartes, dès novembre 2023.

### 9.2 Événement du 15 octobre 2024

**Trace d'origine :** le mail évoque « un autre événement » au 15 octobre, sans préciser sa source ni démontrer un reset. Les métadonnées de SD-03 offrent cette fois une anomalie directement rattachable au jour signalé, sans établir qu'elles sont celles effectivement consultées par la cliente.

**Ce qui est démontré :** 65 vidéos actives, premier nom **08:02:03**, dernier **13:28:00**. Les deux fichiers précédant le dernier, `13:24:49` et `13:26:34`, passent le contrôle prioritaire sans avertissement. Le dernier, TSK **714049800**, présente la date FAT **01/01/2000 00:00:28**, une durée audio **277,760 s**, une durée vidéo **266,171 s**, **3 802 images produites**, dernière PTS **266,103 s**, avec erreur de décodage vidéo signalée.

Les aperçus examinés affichent **13:28:00**, **13:30:21** et, proche de la dernière PTS, **13:32:26**. Ils montrent plusieurs personnes et des documents dans le salon ; le cadrage change, puis le dernier aperçu est flou. Ni les rôles des personnes ni une commande de reset, un retrait de carte ou une coupure ne peuvent être attribués à partir de ces seuls aperçus. Les dates restent celles de la caméra.

La fin nominale **13:32:37,760**, calculée à partir de la durée du conteneur, **n'est pas la dernière image constatée** : elle inclut l'audio plus long. Il n'existe aucun nom de fichier du 16 au 28 octobre ; le nom suivant est **29/10/2024 17:59:18**. La caméra n'étant pas sous scellés, cette chronologie ne décrit pas une violation de scellés.

**Explications compatibles :** même mécanisme défectueux que les autres clips de 2000 ; finalisation après arrêt ou reprise avec horloge non synchronisée ; arrêt d'alimentation/fonctionnement, réglages ou absence de déclenchements pour la lacune ; effacements sans traces survivantes restent techniquement possibles. Le motif de tables est commun à des dates antérieures à la perquisition ; il n'identifie pas à lui seul la cause de l'événement du 15 octobre.

**Une réinitialisation est-elle établie ?** **Non.** Une anomalie de finalisation et de métadonnées est établie, une réinitialisation ou un redémarrage reste possible. La carte ne permet pas de dater précisément l'écriture fautive ni d'en désigner l'auteur ou l'intention. Aucun lien causal avec la perquisition n'est démontré par la seule proximité des dates/heures déclarées.

Preuves des deux événements : [focus](recherche-SD-03/20261016/inventaires/evenements-focus.json), [tables et test](recherche-SD-03/20261016/inventaires/analyse-finalisation.json), [images produites](recherche-SD-03/20261016/inventaires/frames-cibles.json), [observations visuelles](recherche-SD-03/20261016/inventaires/observations-visuelles.json), `journaux/istat/1201.txt` et `714049800.txt`.

## 10. Formatage, accès ultérieurs et recoupements

La structure FAT actuelle est cohérente sur ses chaînes actives : pas de recouvrement, pas de chaîne trop courte, pas de cluster marqué défectueux dans la lecture FAT. Trois allocations sans référence et quatre excédents sont documentés séparément. Les défauts d'index MP4 existent **dans les fichiers**, indépendamment de cette cohérence des liens FAT.

**Aucun formatage daté n'est établi.** Un compteur cohérent, des FAT identiques ou des fichiers anciens n'excluent pas un formatage rapide antérieur, une copie de structures ou un écrasement ultérieur. Aucune date fiable de formatage n'est déduite du boot, de l'identifiant de volume ou d'une date 2000. La remise à zéro de l'horloge, un redémarrage, un reset des réglages et le formatage sont des opérations distinctes.

Deux fichiers actifs `System Volume Information` ont des créations FAT au **12/11/2024 23:37:25,19** et **23:37:25,34**. Ils sont compatibles avec un traitement du volume sous Windows, sans identifier le poste, une personne ou une vidéo lue. Des dates d'accès de 2026 sont déjà dans l'image acquise : elles ne sont pas générées par cette campagne. Un accès FAT n'est pas un journal d'activité. Le marqueur `.rw` est vide ; sa fonction exacte n'est pas confirmée.

Comparaison avec SD-01 et SD-02 : organisation et modèle `.moov` communs, géométrie identique, identifiant de volume SD-03 distinct. Les concordances de SHA-256 des fichiers actifs sont dans la synthèse : **1 avec SD-01**, **1 avec SD-02**. Elles concernent uniquement le marqueur **`.rw` vide**, pas des vidéos communes, comme le précise le [rapport transversal](analyse-cartes_sd-transversale.md). Les profils et valeurs par défaut communs ne prouvent pas une opération ou un auteur commun.

SD-01 possède des enregistrements après l'heure de fin nominale de SD-03 le 15 octobre, dont un fichier se terminant nominalement vers **22:46:17**. Cette comparaison ne démontre donc pas un arrêt simultané de toutes les caméras ce jour-là. Elle ne permet pas de déterminer l'alimentation ou les réglages de chacune.

## 11. Qualification des résultats et limites

| Qualification | Conclusion défendable |
| --- | --- |
| Confirmé — confiance élevée | Inventaire, dates FAT aberrantes, erreur de table audio des neuf cas, limites de décodage, lacune des noms, temporaires supprimés associés à un final présent, fragment de 3,849 s restauré, intégrité de l'image |
| Fonctionnement normal fortement étayé | Nettoyage des trois temporaires après finalisation ; pas d'effacement distinct établi par ces entrées |
| Dysfonctionnement fortement étayé | Défaut récurrent de tables/finalisation ou reconstruction ; rôle précis du micrologiciel non confirmé |
| Hypothèses possibles | Redémarrage avec date par défaut, problème d'alimentation/écriture, finalisation différée, traitement ultérieur ; causes individuelles indéterminées |
| Anomalies démontrées ; modification ultérieure non établie | Incohérences de métadonnées, de tables et de taille logique ; elles ne démontrent pas à elles seules une modification après enregistrement |
| Intervention intentionnelle ou malveillante démontrée | **Aucune établie** par cette analyse |
| Limitation | Nature/date réelle des resets rapportés, origine de l'affichage 1999, cause de la lacune, logiciels/personnes intervenus, contenu écrasé sans trace |

L'absence de preuve ne certifie pas l'absence d'intervention. Des vidéos décodables peuvent avoir été traitées antérieurement sans laisser de preuve identifiable ; aucun état de référence signé avant acquisition ni signature native caméra n'est disponible. Les horloges ne sont pas étalonnées entre elles ou avec les horaires de procédure. Aucun journal d'accès caméra/cloud/réseau, de boot, d'effacement, de réglage ou du poste Windows n'est fourni par la carte.

Les analyses automatisées couvrent les métadonnées de tous les fichiers, mais le décodage intégral est ciblé et le contrôle visuel limité à 23 images. Une image échantillonnée ne suffit pas à décrire toute une séquence. Les données perdues ou réécrites et certaines dépendances H.264 manquantes ne sont pas recréées. Le fragment après EOF est une restauration partielle documentée, sans garantie d'authenticité historique au-delà de sa provenance et de sa cohérence technique.

Pistes utiles si disponibles : source originale de l'affichage 1999/événement du 15 octobre, modèle/micrologiciel et réglages, journaux d'application/cloud/NTP, essais sur **une autre carte**, journaux du poste ayant traité les volumes en novembre, procès-verbaux pour les horaires. Ces éléments pourraient tester les hypothèses ; ils ne sont pas supposés exister.

## 12. Annexes et reproductibilité

Les résultats sont conservés sous `cartes_sd/recherche-SD-03/20261016/`. Le [guide de reproduction](recherche-SD-03/20261016/REPRODUCTION.md) détaille l'ordre, les plafonds, les paramètres et les incidents. Les [commandes SSH](recherche-SD-03/20261016/journaux/commandes.jsonl) enregistrent heures UTC, scripts/paramètres, retours et sorties. Les erreurs locales sont également consignées.

| Référence | Artefacts |
| --- | --- |
| A01 — image/intégrité | `journaux/ewfverify-sha256.txt`, `segments-sha256*.txt`, `ewfinfo.txt`, `provenance.txt` |
| A02 — inventaire/structures | `inventaire.csv`, `fls.txt`, `lecture-fat.json`, `structures-index.json`, structures brutes |
| A03 — chronologie | `chronologie.csv`, `par-jour.csv`, `intervalles.csv`, `timeline*`, `gestion-dates-dossiers.csv` |
| A04 — vidéos | `inventaires/medias/`, `priorite/`, `synthese-medias.json`, `anomalies-medias.json`, journaux de décodage |
| A05 — supprimés | `comparaison-temporaires.json`, `supprimes-reutilisation.csv`, extraits `prive/` |
| A06 — résidus | `espace-libre.json`, `residus-classes.json`, `residus-details.json`, `residus-synthese.json`, `allocation.json`, `complements-index.json` |
| A07 — événements et tests | `evenements-focus.json`, `analyse-finalisation.json`, `frames-cibles.json`, journaux associés |
| A08 — récupération et visuel | `recuperation-apres-eof.json`, `observations-visuelles.json`, index d'aperçus et PNG |

Les tailles, SHA-256 et emplacements des extraits sont dans les index ; le manifeste global récapitule les empreintes. Médias et blocs sont des preuves dérivées conservées dans le projet, **exclues de Git** : un clone Git seul ne restitue pas tous les artefacts privés. Aucune ancienne version du rapport n'est créée ; les essais techniques non validés sont conservés et étiquetés comme tels.

Exemples représentatifs en lecture seule, dont les sorties doivent être redirigées **localement dans le projet** :

```bash
ssh -F /home/chris/.ssh/config sift 'sudo -n ewfverify -q -d sha256 /media/shared/forensic/SADEDINE-2026/ANALYSES/SD-03/SD03.E01'
ssh -F /home/chris/.ssh/config sift 'sudo -n mmls /mnt/ewf-sd03/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fsstat -o 8192 /mnt/ewf-sd03/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n fls -o 8192 -r -p /mnt/ewf-sd03/ewf1'
ssh -F /home/chris/.ssh/config sift 'sudo -n istat -z UTC -o 8192 /mnt/ewf-sd03/ewf1 714049800'
ssh -F /home/chris/.ssh/config sift 'sudo -n icat -r -o 8192 /mnt/ewf-sd03/ewf1 1543'
```

Formules : offset absolu de cluster = `19 771 392 + (cluster − 2) × 16 384` ; identifiant TSK de slot = `3 + (offset_absolu_slot − 19 771 392) / 32`. La récupération après EOF énumère ses échantillons et sa chaîne ; le test d'index énumère ses modifications RAM. Les fonctions pures MP4 réutilisées sont empreintées dans les journaux, sans exécuter les programmes SD-01/SD-02 avec effets de bord.
