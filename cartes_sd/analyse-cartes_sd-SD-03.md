# Rapport d’analyse technique de la carte SD-03 — salon

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev

**Support :** image de la carte SD-03, arborescence `CAMERA SALON`

## 1. Objet et périmètre

Ce rapport présente les enregistrements conservés sur SD-03, les suppressions et récupérations possibles, les anomalies vidéo et temporelles, ainsi que les conclusions relatives aux événements signalés par la cliente. Une attention particulière porte sur la dernière vidéo disponible du **15 octobre 2024** et la lacune qui la suit.

Les [mails de mission](../docs/mail.txt) et [complémentaires](../docs/mail-2.txt) décrivent un affichage « 31/12/1999 », une réinitialisation rapportée de la **chambre en février 2024** et un autre événement le 15 octobre. Les anomalies du salon constituent des comparaisons techniques avec la chambre ; elles ne sont pas la provenance authentifiée du signalement de février. L’interface et le fichier à l’origine des observations restent inconnus.

**Les caméras et cartes n’étaient pas sous scellés.** Leurs enregistrements postérieurs à la perquisition ne démontrent pas une violation de scellés. L’analyse distingue les mesures sur l’image, les interprétations, les observations de visionnage rapportées et les hypothèses ; elle constitue une investigation privée, sans désignation comme expertise judiciaire.

## 2. Synthèse des conclusions

| Question | Résultat | Portée et limite |
|---|---|---|
| Quel corpus subsiste ? | **2 431 vidéos actives**, sur **175 jours représentés**, du **4 novembre 2023 au 31 octobre 2024** selon les noms. | Pas de continuité garantie depuis l’installation déclarée après mars 2023. |
| Des vidéos effacées sont-elles récupérées ? | Trois temporaires supprimés sont reliés à un final toujours présent. **Aucune vidéo supprimée distincte complète supplémentaire n’est récupérée.** | Leur suppression est fortement compatible avec un nettoyage après finalisation, sans date ou auteur établi. |
| Une récupération partielle est-elle obtenue ? | **3,849 s** à la fin d’un fichier actif endommagé du **29 février**, à partir de données au-delà de sa taille logique. | Conteneur reconstruit ; ce n’est ni une vidéo supprimée distincte ni la restauration complète de l’original. |
| Quelles anomalies sont établies ? | **Neuf vidéos datées en FAT de janvier 2000** ont la même erreur de compteur audio ; un dixième clip a une autre erreur de compte. | Le défaut récurrent est établi, sans identification du logiciel, du déclencheur ou de la date réelle d’écriture fautive. |
| Que montre le dernier clip du 15 octobre ? | Dates FAT de 2000, erreur H.264 intermédiaire, dernières images vers **13:32:26** et audio plus long de **11,589 s** que la piste vidéo. | L’audio supplémentaire est décodable et non nul ; les temps de pistes ne sont pas une horloge civile étalonnée. |
| Quel est le manque après ce clip ? | Aucun nom de vidéo du **16 au 28 octobre** ; nom suivant le **29 octobre à 17:59:18**. | Lacune du corpus, sans cause démontrée : elle ne prouve ni arrêt prolongé ni effacement. |
| Un reset ou acte malveillant est-il établi ? | **Aucune réinitialisation effective, aucun formatage daté, accès distant ou acte intentionnel n’est démontré.** | Les anomalies et la lacune ne désignent pas un auteur et n’excluent pas une intervention ancienne sans trace conservée. |

## 3. Identification, intégrité et méthode

### 3.1. Support et image

L’[attestation](../remise-documents/attestation-de-remise.md) décrit une carte de **32 Go**, marque transcrite « ScanDisk », sans série individuelle confirmée. Le numéro USB **`121220160204`** désigne le lecteur. Le rattachement SD-03 repose sur les références d’acquisition et la pièce EWF, dont la description « salon » concorde avec l’arborescence et les scènes des aperçus. Le modèle exact et le firmware de caméra ne sont pas identifiés.

L’image acquise en octobre 2026 comprend **douze segments `SD03.E01` à `SD03.E12`**, au format EWF/EnCase 6, représentant **31 914 983 424 octets** décompressés. Les dates de la vue FUSE utilisée pour lire cette image ne datent pas les vidéos.

### 3.2. Intégrité et préservation

`ewfverify` termine avec **SUCCESS**. Le MD5 stocké dans l’EWF et recalculé concorde ; le SHA-256 recalculé sur le flux complet est identique à celui du document d’acquisition :

```text
MD5     d0402e436587d9cb319f78575e81fec0
SHA-256 7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0
```

Le SHA-256 logique n’était pas enregistré dans les segments. Les **douze empreintes SHA-256 des conteneurs sont identiques avant et après les contrôles**. Guymager indique vérification d’image activée, vérification de source désactivée et aucun secteur défectueux. La concordance acquisition/image ne constitue pas une seconde lecture indépendante du support physique.

La vue EWF est lue en mode `0444`, sans montage FAT, réparation ou écriture sur l’image. Le partage source ne constitue pas un bloqueur matériel ; les commandes et empreintes étayent la préservation. Les essais de correction d’index modifient **seulement des copies anonymes en mémoire**, jamais les médias conservés ou les segments. L’intégrité de l’acquisition n’implique pas celle de chaque fichier qu’elle contient.

### 3.3. Couverture effective

Les contrôles utilisent SIFT, Sleuth Kit, une contre-lecture des slots et chaînes FAT32, FFprobe/FFmpeg et des scripts de tables MP4. Ils couvrent les empreintes des fichiers actifs, les métadonnées, tables et temps de paquets de tous les MP4, les entrées supprimées, l’espace libre complet, le slack et les allocations sans référence.

Le décodage intégral actif porte sur **387 fichiers ciblés**, dont **les 65 du 15 octobre**, les neuf anomalies de date et des témoins. L’examen visuel documenté porte sur **23 images** ; il ne constitue pas un visionnage humain intégral des 2 431 vidéos. Les durées déclarées et les images effectivement produites par les décodeurs sont distinguées. Aucune analyse sémantique de l’audio n’est établie par ces contrôles.

## 4. Structure FAT32 et inventaire

### 4.1. Organisation et cohérence du volume

| Paramètre | Valeur vérifiée |
|---|---|
| Partition FAT32 | Secteurs absolus **8 192–62 333 951**, jusqu’à la fin de l’image |
| Offset / secteur / cluster | **4 194 304 octets / 512 octets / 16 384 octets** |
| Début des clusters | **19 771 392 octets**, cluster 2 |
| Clusters de données | **1 946 729** |
| Libres / non libres | **471 351 / 1 475 378**, occupation environ **75,79 %** |
| Référencés / alloués sans référence active | **1 475 375 / 3** |
| FAT | Deux copies de **15 209 secteurs**, identiques |
| Identifiant de volume / OEM | **`0x6546a41d` / `mkdosfs`** |

Les deux FAT ont pour SHA-256 :

```text
19d943e6f80a9d9e63c707f486f833c7d1753f8d1a324bd0569cbdd0b6db374d
```

Le compteur FSInfo principal indique exactement **471 351 libres**, prochain suggéré **1 487 215**. La sauvegarde donne **1 946 728 libres**, prochain 2, compatible avec des valeurs initiales non actualisées. Le boot et sa sauvegarde ne diffèrent qu’à **`0x41`**, valeur 1 contre 0. Le champ BPB des secteurs cachés vaut zéro malgré la partition à 8 192. Ces valeurs ne datent pas une opération.

Les chaînes actives ne présentent ni superposition, ni chaîne trop courte, ni cluster marqué défectueux. Trois clusters alloués sans référence active et quatre fichiers à allocation excédentaire sont distingués de cette cohérence. Les défauts MP4 se trouvent dans les fichiers et ne sont pas annulés par une FAT cohérente.

**Aucun formatage daté n’est établi.** Les identifiants, compteurs, FAT identiques ou fichiers anciens ne suffisent pas à exclure un formatage rapide antérieur, une copie de structures ou des écrasements ultérieurs.

### 4.2. Inventaire logique

| Type d’entrée hors racine et alias | Nombre |
|---|---:|
| Fichiers actifs | **2 434** |
| Vidéos MP4 | **2 431**, sous `CAMERA SALON/record/` |
| Autres fichiers actifs | **3** : `.rw` vide, `WPSettings.dat` et `IndexerVolumeGuid` |
| Répertoires actifs | **179** |
| Fichiers supprimés | **3**, sous `.record_tmp` |
| Répertoire supprimé | **1**, `_CIM` |

L’inventaire FAT et TSK concorde sans écart. L’ancien `_CIM` pointe au même cluster initial que l’arborescence active `CAMERA SALON`, compatible avec un ancien nom du répertoire. Le premier caractère perdu et la date de l’opération ne sont pas établis ; l’entrée ne révèle pas un ensemble indépendant de vidéos supprimées.

## 5. Corpus vidéo et portée des dates

### 5.1. Couverture conservée

| Mois nominal | Jours représentés | MP4 |
|---|---:|---:|
| Novembre 2023 | 18 | 308 |
| Décembre 2023 | 17 | 220 |
| Janvier 2024 | 10 | 141 |
| Février 2024 | 8 | 125 |
| Mars 2024 | 13 | 140 |
| Avril 2024 | 20 | 131 |
| Mai 2024 | 13 | 84 |
| Juin 2024 | 12 | 460 |
| Juillet 2024 | 12 | 129 |
| Août 2024 | 18 | 448 |
| Septembre 2024 | 21 | 146 |
| Octobre 2024 | 13 | 99 |

Les **175 jours représentés** ne forment pas une continuité depuis mars 2023. La plus grande lacune interne quotidienne calculée est de **79 199,968 s**, le 13 août entre 00:53:31,032 et 22:53:31, sans cause établie.

Les noms des 2 431 vidéos ont une date syntaxiquement valide et leurs contenus actifs ont tous des SHA-256 distincts. Les descriptions de pistes sont communes : H.264 **1 920 × 1 080** et AAC **mono 8 kHz**. Les ressemblances de format ne certifient pas l’origine historique ou l’absence d’un traitement antérieur.

### 5.2. Horloges et métadonnées

Les noms, les incrustations et les dates FAT sont des indications des systèmes producteurs, sans étalonnage civil indépendant. FAT ne stocke pas de fuseau ; l’écriture a une granularité de deux secondes et l’accès principalement celle d’une journée. L’affichage UTC de TSK est une convention, pas une synchronisation démontrée.

Le suffixe du nom représente une durée approchée, **pas un numéro de séquence**. Des durées et fins de conteneur ne garantissent pas que chaque image existe ou se décode ; les fichiers défectueux exigent des mesures séparées.

Les **2 431 MP4** ont tous `creation_time=1970-01-01T00:00:00.000000Z` ; les cinq champs temporels bruts contrôlés par fichier valent **2 082 844 800** dans le repère MP4. Cette répétition est fortement compatible avec une valeur conventionnelle sans portée de date effective de captation, distincte des dates FAT de 2000.

## 6. Suppressions et récupérations

### 6.1. Temporaires associés à un final conservé

| Entrée supprimée TSK | Objet sous `.record_tmp` | Taille déclarée | Octets extraits |
|---|---|---:|---:|
| **1543** | `20241031_232538_10.mp4` | 2 123 808 | 16 384 |
| **1547** | Même base, `.mp4.moov` | 1 006 | 1 006 |
| **1551** | Même base, `.mp4.stbl` | 10 784 | 10 784 |

Le temporaire et le final actif **761370124**, `20241031_232538_10_0028.mp4`, partagent le premier cluster **1 487 054**. Le final mesure **2 617 249 octets**, dure **29,056 s** et se décode sans avertissement. Le préfixe de 16 384 octets récupéré est identique au sien.

Le `.stbl` concorde avec le début des cinq séries testées du final : **266 tailles vidéo, 182 tailles audio, 27 offsets vidéo, 26 offsets audio et 266 numéros de synchronisation vidéo**. Le `.moov` est un auxiliaire de production.

**Ces trois entrées sont fortement reliées à la création/finalisation de la vidéo qui subsiste.** Leur nettoyage est fortement étayé comme fonctionnement courant, sans preuve de disparition volontaire d’un autre enregistrement. Les dates des temporaires ne sont pas des dates de suppression et FAT ne désigne pas leur auteur.

### 6.2. Fragment récupéré après la fin logique d’un fichier actif

Le fichier actif **266342024**, `20240229_112725_10_0020.mp4`, déclare **1 169 358 octets**, mais sa chaîne alloue **143 clusters, soit 2 342 912 octets**. Des tables pointent au-delà de la fin logique et du `mdat`. La lecture ordinaire produit **222 images sur 295 annoncées**, dernière PTS **15,470 s**.

Des échantillons subsistent aux positions référencées après la fin logique. Un test borné retient une portion démarrant sur une image intra au temps initial **16,802 s**. Un **nouveau conteneur** réindexe ces médias sans inventer ni réencoder les images : **328 426 octets, durée 3,849 s**, décodage intégral sans avertissement. Les aperçus affichent **29/02/2024 de 11:27:41 à 11:27:45**.

Il s’agit d’une récupération partielle de données résiduelles d’un fichier actif endommagé, **pas d’une vidéo supprimée distincte ou d’une restauration complète**. La remise à zéro séparée des pistes peut introduire un léger décalage audio/vidéo. Les trois autres chaînes excédentaires examinées ont leurs clusters supplémentaires nuls et ne livrent pas de continuation.

### 6.3. Espace libre et autres résidus

Les **7 722 614 784 octets libres** sont intégralement lus. **11 577 clusters non nuls** sont conservés ; les autres sont nuls. L’empreinte de la concaténation du libre dans l’ordre croissant est :

```text
SHA-256 78870ea13eb832a60d674d17ea71b8c41f7139c0b53374324d1bff1bc41e1102
```

| Contenu caractérisé | Résultat |
|---|---:|
| Signatures `ftyp` / `mdat` | **0 / 0** |
| Modèles `moov` de 1 006 octets | **2 427**, identiques |
| Journaux auxiliaires / fragments | **4 959 / 4 191** |
| Clusters non classés selon la grammaire employée | **0** |
| Slots MP4 valides supplémentaires hors inventaire | **0** |

Les modèles et journaux ne constituent pas de nouvelles vidéos. Leur grammaire est inférée ; la classification ne certifie pas la compréhension de chaque octet. Les modèles ont le même SHA-256 que sur les autres cartes : `731c49c0eb32815913b66158889c78a53f83fcea0e661589ac633b8fa5c26e15`.

Les trois clusters alloués sans référence **552 486, 552 487 et 552 488** sont nuls. Le slack actif représente **20 239 422 octets**, dont **10 194 non nuls**. Les régions avant partition, réservées et terminales ne révèlent pas d’ancien système de fichiers selon les motifs recherchés.

**Aucune vidéo supprimée distincte supplémentaire n’est récupérée.** Aucun PhotoRec propre à SD-03 n’est exécuté ; la recherche spécialisée couvre le libre intégralement selon ses critères et les régions résiduelles identifiées. Les données effacées, écrasées ou inaccessibles au contrôleur restent une limite.

## 7. Anomalies MP4 et dates FAT de 2000

### 7.1. Neuf fichiers aux dates aberrantes

Les neuf fichiers suivants ont des créations/écritures FAT entre **00:00:26 et 00:00:28 le 01/01/2000**, malgré des incrustations examinées de 2023/2024. Les différences de représentation d’une seconde tiennent parfois au champ de précision de création. Aucune date FAT explicite de 1999 n’est identifiée.

| Vidéo nominale | TSK | Durée audio / vidéo | Images produites / annoncées |
|---|---:|---:|---:|
| `20231109_181905_10_0039.mp4` | 12727332 | 39,424 / 39,901 s | 547 / 570 |
| `20240221_232237_10_0190.mp4` | 261989424 | 190,848 / 190,842 s | 2 701 / 2 726 |
| `20240221_233345_10_0077.mp4` | 261989436 | 77,056 / 77,707 s | 1 051 / 1 110 |
| `20240221_234103_10_0044.mp4` | 261989444 | 43,904 / 44,101 s | 587 / 630 |
| `20240229_102610_10_0047.mp4` | 266341920 | 46,592 / 47,113 s | 673 / 673 |
| `20240229_105600_10_0006.mp4` | 266341968 | 5,376 / 6,299 s | 30 / 90 |
| `20240229_110139_10_0116.mp4` | 266341984 | 116,480 / 116,702 s | 1 621 / 1 667 |
| `20240229_112725_10_0020.mp4` | 266342024 | 20,608 / 20,651 s | 222 / 295 |
| `20241015_132800_10_0277.mp4` | 714049800 | 277,760 / 266,171 s | 3 802 / 3 802 |

Les durées sont des valeurs de pistes, pas une garantie d’images lisibles jusqu’à leur fin. Le fichier de six secondes du 29 février ne produit ainsi que trente images, dernière PTS **2,026 s**. Des erreurs peuvent exister malgré un code de retour FFmpeg nul.

### 7.2. Signature de compteur commune et limites des corrections

Dans les neuf cas, la dernière entrée audio **`stsc` reprend le nombre cumulé des échantillons précédents**, alors que la table attend le nombre par bloc. Le reste attendu est **sept échantillons**. Le dernier clip du 15 octobre compte par exemple **2 170 échantillons**, dont **2 163 avant le dernier bloc**, mais porte 2 163 dans le dernier champ au lieu de sept.

Les deux vidéos de SD-01 aux dates FAT de 2000 ont exactement ce défaut : la signature concerne **onze clips sur deux cartes, dès novembre 2023**. Sept des onze cas ont aussi des compteurs vidéo excédentaires de treize ou vingt-six échantillons. Les corrections expérimentales des seuls compteurs concernés sur des copies en mémoire suppriment `wrong sample count`, sans garantir les médias ni restituer les temps manquants.

**Un même chemin défectueux de finalisation ou de reconstruction est fortement étayé.** Une reprise après interruption avec date par défaut est compatible ; le firmware, son algorithme réel, son déclencheur et sa date d’exécution ne sont pas identifiés. Un retour aux réglages usine n’en découle pas.

Le fichier **266341920**, du 29 février à 10:26:10, conserve aussi une unité vidéo non indexée. Un test borné produit **une image supplémentaire**, de 673 à 674, sans lui inventer d’horodatage. Ce résultat est distinct du fragment daté de 3,849 s et ne constitue pas une nouvelle vidéo complète.

### 7.3. Autre anomalie et gestion des dates de dossier

Le clip **172620304**, `20231221_130102_10_0003.mp4`, a des dates FAT normales et une durée de **3,987 s**. Son index compte 35 échantillons audio contre 31 dans les tables de tailles/temps : le dernier bloc devrait en contenir trois. Cette dixième anomalie est un autre défaut terminal de compteur ; elle montre qu’une erreur MP4 peut exister sans date FAT de 2000.

Le bilan retient **dix fichiers actifs avec anomalies de tables**, aucune erreur de structure de boîtes et aucune progression de paquets signalée. Ces résultats ne signifient pas que tous les flux compressés sont intacts.

Sur les **175 dossiers quotidiens**, la création de l’entrée parent égale celle du dernier fichier dans **168 cas**, l’écriture dans **171 cas**, et l’alias `.` garde la création du premier fichier dans **167 cas**. Ce motif étaye une mise à jour liée à la gestion des enregistrements. Le dossier du 15 reprend la date de 2000 du dernier fichier tandis que `.` et `..` gardent **15/10/2024 à 08:02:36**. **Fichier et dossier ne sont pas deux preuves indépendantes de réinitialisation.**

## 8. Dernier clip du 15 octobre et lacune suivante

### 8.1. Séquence conservée et images constatées

Le jour comporte **65 clips**, du premier nom **08:02:03** au dernier **13:28:00**. Les deux fichiers précédant le dernier, à **13:24:49 et 13:26:34**, passent les contrôles prioritaires sans avertissement.

Le dernier fichier, **714049800**, présente la date FAT **01/01/2000 à 00:00:28**, le compteur audio erroné et une erreur H.264. Les aperçus examinés affichent **13:28:00, 13:30:21 et 13:32:26**. Ils montrent plusieurs personnes et des documents dans le salon ; le cadrage change et le dernier aperçu est flou. Ces images seules ne désignent ni rôle, ni identité, ni commande de caméra, ni retrait de carte.

### 8.2. Erreur vidéo intermédiaire

Le contrôle ciblé localise une erreur H.264 et une dissimulation d’erreurs autour de l’image d’indice zéro **1 788**, PTS **125,176 s**, soit nominalement **13:30:05,176**. Le temps provient du voisinage des messages de décodage et des informations d’images, sans précision civile garantie.

Le décodeur produit ensuite des images jusqu’à la PTS **266,103 s**, nominalement **13:32:26,103**, sans nouvelle erreur vidéo terminale signalée. **Les 3 802 images produites ne sont pas toutes garanties intactes**, puisqu’une image est produite avec dissimulation d’erreurs. L’erreur intermédiaire ne prouve pas une troncature à la fin du clip ou une coupure de caméra à 13:32:26.

### 8.3. Piste audio plus longue

| Mesure | Valeur |
|---|---:|
| Durée audio | **277,760 s**, 2 170 échantillons AAC |
| Durée de piste vidéo | **266,171 s**, 3 802 images produites |
| Dernière PTS d’image produite | **266,103 s** |
| Excédent audio sur vidéo | **11,589 s** |

Après correction expérimentale du compteur sur copie, l’audio produit **2 222 080 échantillons PCM mono à 8 kHz**, soit exactement 277,760 s, sans avertissement. Les fenêtres après la fin de piste vidéo ont un signal non nul. **L’excédent n’est donc ni une simple durée fictive du compteur erroné ni une extension exclusivement composée de silence numérique.**

Les données audio supplémentaires sont dans la taille logique, référencées dans les tables. Cet excédent est exceptionnel dans les populations comparées : les maxima des autres fichiers restent de **0,528 s pour SD-01**, **0,671 s pour les finalisés actifs SD-02** et **0,657 s pour les autres SD-03**.

Arrêt de production vidéo avant l’audio, pertes de données ou d’index, erreur temporelle ou reprise/assemblage ultérieur restent compatibles. Sans étalonnage des pistes, **il n’est pas établi que ce son ait été capté exactement 11,589 secondes civiles après la dernière image**. Aucun sens n’est attribué à son contenu.

La fin nominale du conteneur **13:32:37,760** ne doit donc pas être confondue avec la dernière image ou une heure certaine d’arrêt de la caméra.

### 8.4. Lacune et observation rapportée sur les téléphones

Aucun fichier référencé ne porte de nom du **16 au 28 octobre**. Le nom suivant est le **29 octobre à 17:59:18**. Cette absence est établie dans le corpus, sans identifier sa cause : arrêt, alimentation, réglages, absence de déclenchement ou perte/suppression sans trace survivante restent possibles.

**Observation de visionnage rapportée :** le prestataire indique que les vidéos du salon montrent, le **15 octobre vers 13:25**, une agente de l’administration fiscale rallumant les téléphones précédemment éteints. La cliente situait ce geste vers 13:30 ou un peu avant. Ce constat rapporté, repris dans le [rapport final](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés), est distinct des seuls aperçus contrôlés du clip commençant à 13:28. Il n’est pas présenté comme une nouvelle vérification indépendante de cette séquence.

L’image à **13:30:21** montre plusieurs personnes et des objets sur une table ; **elle seule ne démontre ni allumage, ni branchement, ni identité ou fonction**. Ni le geste rapporté, ni sa proximité avec l’erreur vidéo intermédiaire ne démontre la cause de l’anomalie ou de la lacune suivante. L’extinction ultérieure des téléphones et leur état à la fermeture ne sont pas déterminés par les aperçus.

Le PV consulté situe la mise sous scellés des appareils concernés après **14:19 le 15** et distingue le 28 l’arrivée à **10:22**, l’ouverture du PC à **10:41** et celle des téléphones à **11:30**. Ces repères ne calibrent pas l’horloge caméra et ne décrivent pas un placement des caméras sous scellés.

## 9. Événements signalés et recoupements

### 9.1. Février et affichage « 31/12/1999 »

Les sept vidéos du salon des 21/29 février portant la date FAT 2000 ont des anomalies confirmées. Le signalement de la cliente concerne toutefois **la chambre** ; ces fichiers ne sont pas sa source authentifiée. Les incrustations examinées restent datées de février 2024, sans bascule visible vers 1999/2000 dans les échantillons.

Interpréter une date FAT naïve `2000-01-01 00:00:26` comme locale à Paris puis la convertir en UTC donne **31/12/1999 à 23:00:26 UTC**. L’opération inverse reste au 1er janvier 2000. **Ce sens de conversion peut expliquer un affichage, pas l’origine de la valeur stockée ni le logiciel réellement utilisé.**

Les fins des clips anormaux SD-01 et SD-03 du **21 février vers 23:41** sont proches, mais les comparaisons homogènes diffèrent : **1,828 s entre dernières PTS indexées produites**, **1,177 s entre fins vidéo de tables, dans l’autre ordre**. L’écart de 1,901 s parfois cité mélange une fin de piste et une dernière image. Les pertes d’images SD-03 et les images non indexées SD-01 empêchent de dater une coupure commune.

La même signature de défaut est établie ; un incident commun reste plausible. Toutes les anomalies de février ne se superposent pas sur les deux cartes. **Ni événement unique, ni nombre de redémarrages, ni reset usine ne sont démontrés par le nombre de fichiers concernés.**

### 9.2. Événement du 15 octobre

La carte apporte une anomalie directement rattachable au jour signalé, sans établir qu’il s’agit de la métadonnée effectivement observée par la cliente. Le défaut audio est ancien et récurrent ; l’excédent audio exceptionnel et la longue lacune sont des particularités supplémentaires, sans nouvelle cause démontrée.

SD-01 conserve des enregistrements après la dernière image SD-03 le 15, jusqu’à une fin nominale vers **22:46:17**. Un arrêt prolongé simultané de toutes les caméras n’est donc pas étayé. Un incident bref commun ou limité au salon n’est pas exclu. SD-02 ne conserve pas les séquences requises pour départager ces scénarios.

**Une anomalie de finalisation et de métadonnées est établie ; une réinitialisation effective le 15 ne l’est pas.** Le moment réel d’écriture fautive, son auteur, son intention et un lien causal avec la perquisition ne sont pas déterminés.

### 9.3. Traitements Windows et états applicatifs

`WPSettings.dat` et `IndexerVolumeGuid` ont des créations FAT au **12/11/2024 à 23:37:25,19 et 23:37:25,34**. Ces auxiliaires sont compatibles avec un traitement Windows, sans preuve de lecture vidéo, poste ou opérateur identifié. Les recherches dans OP-01 ne rattachent pas positivement les cartes à ce poste ; la perte d’historique empêche de l’exclure sur ce seul résultat.

Les concordances de fichiers actifs avec SD-01 et SD-02 concernent seulement **`.rw` vide**, pas des vidéos. Les géométries, modèles `.moov` et codecs communs étayent une famille de production, sans identifier un firmware ou un incident physique commun.

Les données LSC conservées sur les téléphones ne fournissent pas d’historique complet des partages, comptes ou réappairages. Les caches non décodés et les ressources d’interface ne déterminent ni modèle exact ni firmware installé en 2024. Aucune trace de téléphone ne démontre une commande de caméra responsable des défauts ou de la lacune.

## 10. Limites et conclusion technique

L’image est acquise en 2026, avec une histoire de traitements postérieure aux scènes. Les horloges, la conservation depuis les faits, les réglages et le firmware ne sont pas vérifiés de bout en bout. FAT32 ne fournit pas de journal d’accès, de suppression, de démarrage ou de changement de compte. Les données écrasées et dépendances vidéo absentes ne sont pas recréées.

Les contrôles automatisés de tous les MP4 et le décodage ciblé permettent de caractériser les défauts, sans visionnage humain intégral. Les échantillons ne décrivent pas tous les instants. Un fichier décodable peut avoir subi un traitement antérieur techniquement propre ; aucune référence signée avant acquisition ou signature native caméra ne permet de l’exclure.

**SD-03 conserve 2 431 vidéos, dont 65 du 15 octobre, et des temporaires supprimés fortement associés à un final présent. Aucune vidéo supprimée distincte complète supplémentaire n’est récupérée ; un fragment résiduel de 3,849 s est restauré dans un fichier actif du 29 février.**

**Les neuf dates FAT de 2000 sont associées à une signature de compteur audio commune, déjà présente avant la perquisition. Le dernier clip du 15 ajoute une erreur vidéo intermédiaire, un excédent audio décodable de 11,589 s et une longue lacune du corpus après ses dernières images.** Ces constats renforcent le diagnostic de défauts de finalisation ou de reconstruction ; ils n’établissent ni reset usine, ni formatage daté, ni cause d’arrêt, accès distant ou intervention intentionnelle.

Les éléments discriminants seraient la source originale des affichages, des journaux historiques de caméra/compte/horloge, les réglages, les traces du poste Windows et une expérience contrôlée sur un autre support reproduisant conjointement les défauts FAT et MP4. Leur existence ou disponibilité n’est pas présumée.

## 11. Pièces techniques et termes de lecture

### 11.1. Références des constats

| Domaine | Pièces de contrôle |
|---|---|
| Acquisition et intégrité | [Rapport d’acquisition](analyse-cartes_sd.md), [ewfverify](recherche-SD-03/20261016/journaux/ewfverify-sha256.txt), [empreintes des segments](recherche-SD-03/20261016/journaux/segments-sha256-fin.txt) |
| Inventaire et volume | [Inventaire CSV](recherche-SD-03/20261016/inventaires/inventaire.csv), [contre-lecture FAT](recherche-SD-03/20261016/inventaires/lecture-fat.json), [allocation](recherche-SD-03/20261016/inventaires/allocation.json) |
| Chronologie | [Par jour](recherche-SD-03/20261016/inventaires/par-jour.csv), [chronologie](recherche-SD-03/20261016/inventaires/chronologie.csv), [intervalles globaux](recherche-SD-03/20261016/inventaires/intervalles-globaux.csv), [dates des dossiers](recherche-SD-03/20261016/inventaires/gestion-dates-dossiers.csv) |
| Temporaires et récupération partielle | [Comparaison des temporaires](recherche-SD-03/20261016/inventaires/comparaison-temporaires.json), [fragment après EOF](recherche-SD-03/20261016/inventaires/recuperation-apres-eof.json) |
| Zones libres et résidus | [Scan complet](recherche-SD-03/20261016/inventaires/espace-libre.json), [classification](recherche-SD-03/20261016/inventaires/residus-classes.json), [détails](recherche-SD-03/20261016/inventaires/residus-details.json) |
| MP4, erreurs et images produites | [Synthèse](recherche-SD-03/20261016/inventaires/synthese-medias.json), [anomalies](recherche-SD-03/20261016/inventaires/anomalies-medias.json), [finalisation](recherche-SD-03/20261016/inventaires/analyse-finalisation.json), [images](recherche-SD-03/20261016/inventaires/frames-cibles.json), [observations visuelles](recherche-SD-03/20261016/inventaires/observations-visuelles.json) |
| Particularités du 15 octobre | [Audio et signal](recherche-transversale/20261016/inventaires/audio-714049800.json), [erreur vidéo intermédiaire](recherche-transversale/20261016/inventaires/video-erreur-714049800.json), [analyse transversale](analyse-cartes_sd-transversale.md) |
| Février et affichage 1999 | [Fins comparées](recherche-transversale/20261016/inventaires/fins-comparees.json), [images non indexées](recherche-transversale/20261016/inventaires/nal-non-indexes.json), [sens de conversion](recherche-transversale/20261016/inventaires/conversion-1999.json) |
| Contexte et recoupements | [Retour de la cliente](../investigations/20261019-retour-cliente/compte-rendu.md), [poste Windows](../investigations/20261017-recroisements/compte-rendu.md), [identification des caméras](../investigations/20261109-identification-cameras/compte-rendu.md), [hypothèses d’intervention](../investigations/20261110-revue-intervention-scelles/compte-rendu.md) |
| Reproduction | [Guide technique](recherche-SD-03/20261016/REPRODUCTION.md), [commandes et retours](recherche-SD-03/20261016/journaux/commandes.jsonl) |

Les index, scripts et manifestes conservent tailles, empreintes, ordres de clusters et limites des essais. Les médias et blocs privés sont des pièces dérivées exclues de Git ; le dépôt seul ne restitue pas tout le dossier technique. Les tests sur copies ne sont pas des vidéos originales réparées.

### 11.2. Termes techniques

| Terme | Sens dans ce rapport |
|---|---|
| EWF / empreinte | Conteneur d’acquisition / valeur de comparaison de contenu. Une image stable peut contenir un fichier déjà défectueux. |
| FAT32 / cluster / FSInfo | Système de fichiers / unité d’allocation / informations de gestion du libre, sans journal complet des opérations historiques. |
| `moov` / `mdat` / `.stbl` | Métadonnées MP4 / données audio-vidéo / journal auxiliaire de production. Un modèle ou un index n’est pas un enregistrement supplémentaire. |
| `stsc` / `stsz` | Tables répartissant les échantillons par bloc / donnant leurs tailles et leur nombre. Leur comparaison permet de constater un compteur incohérent. |
| PTS / DTS | Temps internes de présentation / décodage. Ils ne certifient pas une heure civile de captation. |
| EOF / slack | Fin logique du fichier / octets restant dans son allocation. Un média retrouvé après EOF exige une validation spécifique. |
| Conteneur dérivé | Nouveau fichier indexant des médias existants récupérés. Il n’invente pas les données manquantes et demeure distinct de l’original. |
