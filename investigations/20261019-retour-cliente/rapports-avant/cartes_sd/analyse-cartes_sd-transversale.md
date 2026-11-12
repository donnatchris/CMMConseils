# Investigation transversale des cartes SD-01, SD-02 et SD-03

**Complément du 17/10/2026 :** la recherche des manipulations Windows du 12/11/2024 a été étendue à OP-01 : ruches complètes accessibles, journaux System/PnP/stockage et SetupAPI. Aucun rattachement positif des cartes à ce poste n’a été obtenu ; ce résultat n’exclut pas une insertion ancienne dont les traces ont disparu. Les identifiants de volume ne sont pas des numéros matériels uniques. Le [compte rendu transversal](../investigations/20261017-recroisements/compte-rendu.md) et le [protocole de référence caméra](../investigations/20261017-recroisements/README.md) précisent les travaux et limites. Les essais sur caméra de référence ne sont pas exécutés. Les conclusions sur les défauts MP4 ci-dessous restent inchangées.

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils.  
**Prestataire :** Christophe Donnat — Donnat Dev.  
**Complément du 16 octobre 2026.** Investigation technique indépendante, non expertise judiciaire.  
**Périmètre :** chambre (SD-01), terrasse (SD-02), salon (SD-03). Réexamen ciblé des dérivés conservés, sans nouveau scan des images.

## Conclusions accessibles

**Les anomalies de SD-01 et SD-03 partagent un défaut précis de fabrication des index vidéo.** Dans les onze vidéos aux dates FAT de janvier 2000, le dernier compteur audio reprend le cumul des échantillons précédents au lieu des sept échantillons restants. Cette correspondance renforce fortement l'hypothèse d'un même mécanisme logiciel de finalisation ou de reprise. Elle ne prouve ni un même incident physique, ni un firmware strictement identique, ni une opération humaine commune.

**Un incident commun le 21 février reste plausible, sans être démontré.** Deux fichiers anormaux ont des fins nominales proches de deux secondes. Toutefois, les horloges ne sont pas étalonnées, un fichier perd des images référencées et l'autre conserve au moins trois images supplémentaires non indexées. La proximité est une piste sérieuse de comparaison, pas une heure de coupure commune établie.

**Le 15 octobre présente le défaut audio déjà rencontré avant la perquisition, ainsi qu'une particularité supplémentaire.** Sur SD-03, l'audio dure 277,760 secondes, contre 266,171 secondes pour la vidéo. Cet excédent de **11,589 secondes** est exceptionnel dans les trois populations comparées. L'audio supplémentaire se décode et contient un signal non nul. Une erreur H.264 se situe vers 125 secondes de lecture, bien avant les dernières images ; elle ne permet pas de dater un arrêt à la fin du fichier.

**Les défauts dépassent une simple erreur de date.** Des compteurs sont incohérents, certaines tables pointent hors des données vidéo et, dans deux fichiers, au moins quatre images supplémentaires au total sont décodables dans des zones non indexées. Une correction expérimentale des compteurs supprime l'avertissement `wrong sample count`, mais ne garantit pas l'intégrité des médias et ne restitue pas leurs temps manquants.

**Aucune réinitialisation, coupure d'alimentation, intervention intentionnelle ou connexion extérieure n'est démontrée par ces anomalies.** Une finalisation défaillante, une reprise après interruption avec date par défaut, un problème d'horloge ou un traitement ultérieur restent compatibles. Les fichiers auxiliaires de type Windows documentent séparément une histoire de traitement des supports, sans identifier un poste, un auteur ou un lien avec les anomalies.

**Les caméras n'ont jamais été placées sous scellés.** Leur fonctionnement après la perquisition ne constitue donc pas en soi une anomalie.

## 1. Sources, méthode et limites communes

Les [rapports SD-01](analyse-cartes_sd-SD-01.md), [SD-02](analyse-cartes_sd-SD-02.md) et [SD-03](analyse-cartes_sd-SD-03.md), leurs guides, résultats et scripts utiles ont été consultés. Sources de contexte : [mail original](../docs/mail.txt), [attestation de remise](../remise-documents/attestation-de-remise.md), [rapport d'acquisition](analyse-cartes_sd.md), [contexte corrigé](recherche-SD-01/20261016-complement/sources/contexte-et-observations.md), notes de mission et conventions existantes de qualification des conclusions. Le Markdown suit les rapports du projet ; aucun PDF supplémentaire n'est produit ici.

Le mail indique seulement « en février », sans année, sans carte, interface, fichier ni champ authentifiés. Février 2024 est le périmètre demandé pour cette investigation. Le second signalement est un « autre événement » au 15 octobre ; sa nature technique n'est pas connue. **13 h 30 correspond à la perte d'accès déclarée aux téléphones**, sans établir le début de perquisition ou un arrêt caméra. Aucun procès-verbal ni journal de synchronisation n'étalonne les horloges.

Le complément utilise les extractions, structures FAT et résultats FFprobe/FFmpeg déjà produits. Les empreintes de **37 copies MP4 complètes** sont contrôlées contre les inventaires avant leur analyse binaire : 21 SD-01, trois SD-02 et treize SD-03. Ces fichiers comprennent les dix-sept anomalies de tables connues et vingt témoins disponibles. Une absence de copie du voisin dans le jeu local n'entraîne pas de nouvelle extraction distante. Les chronologies complètes restent disponibles pour l'étude des voisins non reparsés.

Un nouveau parseur local, indépendant du parseur MP4 antérieur, vérifie 74 pistes : `stsc`, `stsz`, `stts`, positions de chunks, bornes de `mdat`, délimitation des unités H.264. Il ne vérifie pas toute la sémantique du flux compressé : des longueurs NAL cohérentes n'excluent pas une erreur H.264 interne. Les expériences modifient des **copies anonymes en RAM**, jamais les extraits conservés ni les images EWF. Aucun décodage exhaustif des trois cartes, aucune réparation de source, aucun scan disque, aucune connexion à SIFT, aux caméras ou aux comptes n'est effectué.

Les vingt slots FAT portant au moins une date de 2000 sont réexaminés, alias et marqueur vide compris. Douze sont directement contre-vérifiés sur les copies binaires nommées par cluster ; les huit autres SD-01 sont vérifiés dans un second temps grâce à leur index historique, nommé par identifiant de répertoire TSK. **Les vingt slots sont ainsi contrôlés sur leurs octets conservés**, sans compter les alias comme des événements supplémentaires. SD-02 ne fournit qu'un ancien slot de dossier, dont le premier caractère supprimé n'est pas reconstitué avec certitude.

**4 391 empreintes d'artefacts consommés** correspondent aux manifestes historiques, sans écart ni fichier consommé absent de ces manifestes dans le périmètre du contrôle. Ce résultat valide la stabilité des dérivés réutilisés ; il ne constitue pas une nouvelle vérification intégrale des EWF ni une authentification des opérations antérieures à 2026. Les limites de conservation, d'identification physique et de remise signalées dans les rapports individuels demeurent applicables.

Sources nouvelles, commandes, erreurs d'outillage et paramètres : [guide de reproduction](recherche-transversale/20261016/README.md). Aucune nouvelle image n'a été examinée visuellement, aucune écoute ou transcription audio n'a été effectuée. Les constats visuels de 2024 cités ici proviennent des examens antérieurs explicitement documentés.

## 2. Comparaison des populations et du système de production

| Population active | SD-01 | SD-02 | SD-03 |
| --- | ---: | ---: | ---: |
| MP4 | 674 | 3 301 | 2 431 |
| Dont finalisés analysables | 674 | 3 300 | 2 431 |
| MP4 aux dates FAT de 2000 | 2 | 0 | 9 |
| MP4 avec anomalies de tables connues | 7 | 0 finalisé | 10 |
| MP4 nommés du 15 octobre | 37 | 0 disponible | 65 |

Sur les **6 405 MP4 finalisés**, les onze vidéos aux dates FAT de 2000 ont le défaut audio cumulatif décrit au § 3. Six autres ont une erreur terminale différente, avec dates ordinaires ; les 6 388 restantes ne présentent pas les anomalies de tables retenues par les contrôles antérieurs. Il s'agit d'une association dans ce corpus, sans supposer l'indépendance statistique des fichiers ni estimer une probabilité de cause.

Les 37 copies reparsées ont exactement les mêmes descriptions de pistes `stsd` : audio `213b1835…678b9`, vidéo `53174a74…1051c`. Les trois cartes partagent aussi l'organisation `record`/`.record_tmp`, le modèle auxiliaire `.moov` de 1 006 octets et les dates internes MP4 conventionnelles de 1970. Cela étaye une famille commune de production et de stockage. **Ces ressemblances ne suffisent pas à identifier le modèle de caméra ou la version de son logiciel.**

La géométrie FAT32 commune, les sauvegardes FSInfo anciennes et l'octet de boot `0x41` ne datent pas un incident. L'identifiant de volume est identique sur SD-01/SD-02 et distinct sur SD-03 ; ce n'est pas un numéro matériel. La FAT courante ne fournit pas de journal des modifications historiques. Aucun de ces champs ne relie positivement un formatage aux dates recherchées.

**SD-02 constitue un témoin de fonctionnement, pas un témoin temporel de février ou du 15 octobre.** Son temporaire de novembre sans `moov` final montre un état de production inachevé ; ses suppressions et réutilisations massives étayent une gestion circulaire. Ses 3 300 fichiers finalisés sont cohérents selon les contrôles antérieurs. Les onze défauts couplés FAT/MP4 ne sont donc pas une propriété obligatoire de tous les fichiers de ce système. L'absence des anciennes vidéos SD-02 empêche d'y vérifier un incident commun.

## 3. Signature arithmétique commune et défauts associés

### 3.1. Le même compteur audio fautif dans les onze cas

`stsz` donne le nombre d'échantillons ; `stsc` les répartit entre chunks, dont les positions sont dans `stco`. La table `stsc` décrit un **nombre par chunk**, pas un cumul. Cette fonction est documentée par [Apple, Sample-to-chunk atom](https://developer.apple.com/documentation/quicktime-file-format/sample-to-chunk_atom).

| Carte, TSK | Nom abrégé | Audio total | Cumul avant dernier chunk | Valeur inscrite | Reste attendu |
| --- | --- | ---: | ---: | ---: | ---: |
| SD-01, 20903944 | 21/02, 23:39:14 | 1 183 | 1 176 | 1 176 | 7 |
| SD-01, 22835208 | 01/03, 04:05:05 | 98 | 91 | 91 | 7 |
| SD-03, 12727332 | 09/11/2023, 18:19:05 | 308 | 301 | 301 | 7 |
| SD-03, 261989424 | 21/02, 23:22:37 | 1 491 | 1 484 | 1 484 | 7 |
| SD-03, 261989436 | 21/02, 23:33:45 | 602 | 595 | 595 | 7 |
| SD-03, 261989444 | 21/02, 23:41:03 | 343 | 336 | 336 | 7 |
| SD-03, 266341920 | 29/02, 10:26:10 | 364 | 357 | 357 | 7 |
| SD-03, 266341968 | 29/02, 10:56:00 | 42 | 35 | 35 | 7 |
| SD-03, 266341984 | 29/02, 11:01:39 | 910 | 903 | 903 | 7 |
| SD-03, 266342024 | 29/02, 11:27:25 | 161 | 154 | 154 | 7 |
| SD-03, 714049800 | 15/10, 13:28:00 | 2 170 | 2 163 | 2 163 | 7 |

La correspondance exacte sur deux cartes et plusieurs mois rend fortement plausible un même défaut de calcul ou un même chemin de finalisation/reconstruction. Le remplacement expérimental du seul champ audio par sept laisse parfois `wrong sample count`, car **sept fichiers ont aussi un compteur vidéo incohérent**. Après correction expérimentale des deux compteurs concernés, cet avertissement disparaît dans les onze essais FFprobe. Cela démontre l'origine de cet avertissement dans les compteurs, sans certifier le contenu des médias ni prouver que `stsz` était historiquement la table correcte.

### 3.2. Sept excédents vidéo et six autres erreurs de petite fin de clip

Dans les sept fichiers concernés, le nombre vidéo annoncé pour le dernier chunk dépasse le reste calculé depuis `stsz` de **13 ou 26 échantillons** :

| Carte, TSK | Champ inscrit → reste calculé | Excédent |
| --- | --- | ---: |
| SD-01, 20903944 | 35 → 9 | 26 |
| SD-01, 22835208 | 17 → 4 | 13 |
| SD-03, 261989436 | 22 → 9 | 13 |
| SD-03, 261989444 | 15 → 2 | 13 |
| SD-03, 266341920 | 33 → 7 | 26 |
| SD-03, 266341968 | 24 → 11 | 13 |
| SD-03, 266342024 | 38 → 12 | 26 |

Des chunks vidéo de treize échantillons sont effectivement présents. L'excédent correspond donc à une ou deux unités de ce découpage récurrent. **La relation numérique est démontrée ; l'algorithme exact fautif ne l'est pas.** Le § 3.3 montre pourquoi une correction de compteur seule ne restitue pas nécessairement toute la vidéo : des tailles et des temps peuvent aussi manquer.

Les cinq autres anomalies SD-01 et celle de décembre SD-03 relèvent d'une seconde famille : le dernier chunk audio est compté comme sept échantillons alors qu'il n'en reste qu'un à trois. Ces fichiers ne portent pas les dates FAT de 2000 et leurs unités vidéo passent la vérification des longueurs NAL. Une erreur de clôture MP4 peut donc exister sans date aberrante. Le nom « défaut de finalisation » désigne ici un ensemble de constats, pas une preuve de coupure d'alimentation pour chaque fichier.

### 3.3. Tables hors données, médias non indexés et images supplémentaires

**Huit des onze fichiers** aux dates 2000 ont des chunks référencés hors du `mdat` : SD-01 du 1er mars et sept cas SD-03 de novembre/février. Des références peuvent atteindre le `moov` ou dépasser la fin du fichier ; ces octets ne sont pas des images simplement parce qu'une table les désigne. Les erreurs de délimitation NAL concordent avec les pertes d'images déjà observées.

Les trois autres fichiers — SD-01 du 21 février, SD-03 du 29 février à 10:26:10 et SD-03 du 15 octobre — gardent les tailles disponibles dans le `mdat`. Deux conservent toutefois des zones non indexées :

| Fichier | Zone non indexée du `mdat`, offset logique | Octets | Test borné sans horodatage ajouté |
| --- | ---: | ---: | --- |
| SD-01, 20903944 | 12 281 990 | 903 034 | Trois unités H.264 au début de cette zone : décodage de 2 170 à **2 173 images**, sans avertissement |
| SD-03, 266341920 | 5 308 698 | 15 489 | Une unité H.264 couvrant cette zone : décodage de 673 à **674 images**, sans avertissement |

Les essais convertissent en mémoire les unités AVC indexées et ce seul préfixe résiduel en flux H.264 élémentaire, avec les paramètres de décodage conservés. Ils n'inventent ni image ni horodatage MP4. **Quatre images supplémentaires sont ainsi décodables**, mais aucune nouvelle vidéo complète ou fin datée n'est livrée. Aucun examen visuel de ces quatre images n'est revendiqué.

Pour SD-01, seuls 14 348 octets du début de la zone sont ajoutés au test ; les **888 686 octets restants demeurent non attribués**. Leur mélange de données et de zéros ne permet pas d'en faire automatiquement une continuation. Les temps de présentation des images supplémentaires ne sont pas dans les tables examinées : on ne les extrapole pas à partir d'une cadence supposée. Cette limite affecte directement l'usage de la fin nominale du 21 février.

Ces observations précisent les défauts : **incohérence des compteurs, références à des médias absents, ou présence de médias sans index complet**. Elles sont compatibles avec une clôture/reprise utilisant des états de tables et de médias différents. Elles ne démontrent pas qu'une vidéo initialement saine a été modifiée ultérieurement.

Preuves : [tables et offsets](recherche-transversale/20261016/inventaires/tables-ciblees.json), [excédents et zones](recherche-transversale/20261016/inventaires/compteurs-video-et-zones-non-indexees.json), [tests de compteurs](recherche-transversale/20261016/inventaires/test-index-audio-video.json), [tests H.264 résiduels](recherche-transversale/20261016/inventaires/nal-non-indexes.json). Le fragment après EOF de 3,849 s déjà restauré sur SD-03 est un résultat antérieur distinct, conservé sans modification.

## 4. Février : mécanisme commun et événement commun sont deux questions

### 4.1. Rapprochement du 21 février à 23:41

| Mesure, en heures nominales de caméra | SD-01, 20903944 | SD-03, 261989444 |
| --- | --- | --- |
| Début du nom | 23:39:14 | 23:41:03 |
| Fin de piste vidéo selon tables | 23:41:45,924 | 23:41:47,101 |
| Dernière PTS d'image produite dans la lecture indexée | 23:41:45,851 | 23:41:44,023 |
| Fin audio selon tables | 23:41:45,424 | 23:41:46,904 |
| Écriture FAT brute | 01/01/2000 00:00:28 | 01/01/2000 00:00:26 |
| Particularité | Au moins trois images non indexées décodables | 587 images produites sur 630 annoncées |

La comparaison initiale, fin nominale SD-01 contre dernière PTS produite SD-03, donne bien **1,901 s**. Comparer les dernières PTS indexées produites des deux cartes donne **1,828 s** ; comparer les fins vidéo de tables donne **1,177 s**, dans l'autre ordre. Ces mesures ne sont pas interchangeables et aucune ne constitue seule une heure de coupure.

La proximité des fins, les deux dates 2000 et la même signature de compteur rendent **plausible un événement commun**, par exemple une interruption affectant les deux équipements. Mais les horloges ne sont pas étalonnées, la fin SD-03 est dégradée et celle de SD-01 n'indexe pas tous les médias présents. Un traitement différé de plusieurs enregistrements pourrait aussi produire les métadonnées communes. **Ni une simultanéité civile, ni une coupure commune, ni un redémarrage commun ne sont établis.**

SD-03 a déjà deux autres fichiers anormaux ce soir-là, à 23:22:37 et 23:33:45, séparés par des clips aux dates FAT ordinaires. Son clip de 23:37:04, voisin du dernier cas, porte une fin nominale 23:39:50,144 et une écriture cohérente. Le clip suivant est nommé 23:44:14, avec dates normales. SD-01 ne conserve ce soir-là que le fichier anormal considéré. Cette répartition ne permet pas de compter trois redémarrages sur SD-03, ni de synchroniser tous ses défauts avec SD-01.

### 4.2. Le 29 février et le 1er mars ne forment pas une panne continue démontrée

SD-03 présente quatre fichiers anormaux le 29 février, entrecoupés de vidéos cohérentes. SD-01 conserve douze vidéos du 29 février aux écritures FAT normales. En particulier, sa vidéo de **11:27:08 à 11:27:42,432** recouvre une partie du clip SD-03 de 11:27:25, endommagé. Les anomalies de finalisation ne sont donc pas systématiquement reproduites sur les deux cartes aux mêmes heures nominales.

L'anomalie SD-01 du **1er mars à 04:05:05** possède la signature audio commune, mais sa lecture indexée ne produit que **134 images sur 185**, dernière PTS **9,309 s**, contre 12,950 s de durée annoncée. Sa fin nominale annoncée n'est pas une fin lisible certaine. Le journal résiduel antérieurement associé conserve davantage de tailles que la table finale, ce qui corrobore le désaccord entre états de production.

**Conclusion pour février : même famille de mécanisme fortement étayée ; incident commun du 21 février possible ; un événement unique expliquant toutes les anomalies de février/mars non démontré.**

Preuves : [chronologie croisée](recherche-transversale/20261016/inventaires/chronologie-croisee.csv), [fins distinctes](recherche-transversale/20261016/inventaires/fins-comparees.json), nouveaux relevés d'images SD-01 et contrôles antérieurs d'images SD-03. Les noms et incrustations restent déclaratifs.

## 5. Le 15 octobre : défaut récurrent et particularités nouvelles

### 5.1. Ce qui reste commun aux cas antérieurs

Le dernier MP4 SD-03, **714049800**, `20241015_132800_10_0277.mp4`, présente le compteur audio cumulatif fautif et la date FAT de 2000. Son dossier reprend cette date, tandis que ses alias internes gardent le 15 octobre 08:02:36. Le motif de renseignement du dossier est déjà documenté sur les autres jours : **fichier et dossier ne sont pas deux événements indépendants de reset**.

Le champ audio fautif est à l'offset logique **32 865 034** : remplacer 2 163 par sept modifie seulement deux octets. L'avertissement de compteur disparaît. Le compteur vidéo terminal est ici arithmétiquement cohérent : six échantillons restants, six annoncés. Toutes les longueurs d'unités NAL examinées sont cohérentes avec les tailles vidéo. Cela distingue ce cas des fichiers avec références hors `mdat`.

### 5.2. Un audio réellement décodable plus long que la piste vidéo

| Population de métadonnées comparée | Plus grand excédent audio sur vidéo |
| --- | ---: |
| SD-01, 674 vidéos | 0,528 s |
| SD-02, 3 300 MP4 actifs analysables | 0,671 s |
| SD-03, hors dernier fichier du 15 octobre | 0,657 s |
| SD-03, dernier fichier du 15 octobre | **11,589 s** |

Sur ce dernier fichier : **2 170 échantillons AAC**, durée 277,760 s ; **3 802 images vidéo**, durée de piste 266,171 s, dernière PTS produite 266,103 s. Le test audio après correction du compteur produit **2 222 080 échantillons PCM mono à 8 kHz**, soit exactement 277,760 s, sans avertissement. Les fenêtres d'une seconde après la fin vidéo ont une énergie et des pics non nuls. Il ne s'agit donc pas seulement d'une durée fictive engendrée par la mauvaise valeur `stsc`, ni d'une extension composée exclusivement de silence numérique.

La fin du dernier chunk vidéo est l'offset **32 841 225** ; des chunks audio occupent ensuite les **23 296 octets** restants du `mdat`, jusqu'à **32 864 521**. Ces données sont dans la taille logique et référencées par les tailles audio. L'excédent de durée reste présent après correction du compteur, qui ne change ni les tailles ni `stts`.

**Interprétation :** les deux pistes se terminent différemment dans l'état enregistré. Arrêt de production vidéo avant l'audio, pertes d'index ou de données vidéo, calcul temporel défaillant, reprise ou assemblage ultérieur restent compatibles. Sans étalonnage des temps de pistes ni analyse sémantique, on ne démontre pas que ce son a été capté exactement 11,589 secondes après la dernière image civile. Aucun sens n'est attribué au signal sonore.

### 5.3. Une erreur vidéo vers le milieu, puis des images jusqu'à la fin

Le décodage ciblé avec un seul thread et `showinfo` retrouve l'erreur H.264 `left block unavailable for requested intra mode` et une dissimulation d'erreurs autour de l'image d'indice zéro **1 788**, PTS **125,176 s**. Les images et paquets antérieurement inventoriés situent cette image à l'offset logique **15 423 494**. Le temps nominal correspondant est **13:30:05,176**, sans étalonnage civil. La localisation autour de cette PTS repose sur le voisinage des messages de décodage et de `showinfo` ; aucune précision d'heure civile n'en est déduite.

Le décodeur produit ensuite des images jusqu'à la dernière PTS **266,103 s**, nominalement **13:32:26,103**. Le contrôle ne signale pas de nouvelle erreur vidéo terminale dans ce fichier. **Les 3 802 images produites ne sont donc pas toutes garanties intactes**, puisqu'une image est produite avec dissimulation d'erreurs. L'avertissement H.264 antérieurement observé n'est pas en lui-même la preuve d'une troncature de la dernière image ou d'une coupure à 13:32:26.

La fin audio nominale **13:32:37,760** ne doit pas être présentée comme une dernière image observée, ni comme une heure certaine d'arrêt de la caméra. L'heure 13 h 30 évoquée pour les téléphones ne permet pas d'attribuer l'erreur intermédiaire ou la fin du clip à une opération de perquisition.

### 5.4. Comparaison avec les autres cartes et la reprise disponible

Les deux clips SD-03 précédents, à 13:24:49 et 13:26:34, passent les contrôles prioritaires antérieurs. Aucun MP4 SD-03 référencé ne porte un nom du 16 au 28 octobre ; la reprise des noms est le **29 octobre à 17:59:18**. Cette longue lacune distingue le contexte du 15 de la reprise du 21 février vers 23:44:14. Elle ne distingue pas à elle seule arrêt, absence de déclenchement, perte de données ou suppression sans trace survivante.

SD-01 conserve **37 vidéos du 15 octobre**, sans anomalie spécifique de reset identifiée, dont des enregistrements postérieurs à la dernière image SD-03 et jusqu'à une fin nominale vers 22:46:17. Un arrêt prolongé simultané de toutes les caméras n'est donc pas étayé. Un événement bref commun, ou limité à une caméra, n'est pas exclu. SD-02 ne possède pas les séquences requises pour trancher.

**Conclusion : la signature de compteur du 15 octobre est ancienne et récurrente ; l'excédent audio est exceptionnel dans les populations comparées, et la lacune suivante est particulièrement longue. Ces différences ne démontrent pas une nouvelle cause ni une intention.**

Preuves : [audio et mesures de signal](recherche-transversale/20261016/inventaires/audio-714049800.json), [localisation de l'erreur vidéo](recherche-transversale/20261016/inventaires/video-erreur-714049800.json), [distribution SD-01/SD-03](recherche-transversale/20261016/inventaires/ecarts-audio-video.json), [population active SD-02](recherche-transversale/20261016/inventaires/ecarts-audio-video-SD02-actifs.json). Le relevé SD-02 initial du complément porte sur 3 310 métadonnées mêlant actifs et supprimés ; seule la population corrigée de 3 300 actifs sert au tableau ci-dessus.

## 6. Comment les dates FAT de 2000 pourraient-elles accompagner ces défauts ?

Les dates sont réellement inscrites dans les slots FAT ; ce n'est pas seulement l'affichage d'un champ nul. Les onze fichiers ont des créations/écritures proches de **00:00:26–00:00:28 au 1er janvier 2000**, malgré les noms et incrustations de 2023/2024. FAT ne contient pas de fuseau et ses champs ont des précisions différentes : création 10 ms, écriture deux secondes, accès un jour selon [Microsoft, File Times](https://learn.microsoft.com/en-us/windows/win32/sysinfo/file-times). Ces précisions ne prouvent pas l'exactitude des horloges.

**Scénario technique compatible, sans être observé en fonctionnement :** un enregistrement produit ses médias, son nom, ses incrustations et un journal auxiliaire ; une interruption laisse des états différents en mémoire et sur carte ; un traitement de clôture ou de reprise fabrique des tables à partir de ces états et inscrit les dates FAT alors que le chemin d'horodatage emploie une date par défaut. Un mauvais calcul de compteur et une date aberrante apparaissent ainsi dans le même fichier, tandis que les noms et images conservent 2024.

La présence des modèles/journaux et leurs correspondances avec les fichiers finalisés étayent l'architecture générale de production. **Ni l'exécution d'un mécanisme de reprise au démarrage, ni l'ordre exact écriture/date/synchronisation ne sont démontrés.** Une erreur de finalisation en fonctionnement sans redémarrage, une variable de date non initialisée, ou une récupération ultérieure pourraient produire des états comparables. Aucune architecture de double horloge matérielle n'est affirmée.

La concentration des heures autour de 26–28 secondes est compatible avec une phase répétable de traitement ou de démarrage. Elle ne constitue pas un chronomètre d'uptime validé. Plusieurs clips anormaux d'une même soirée peuvent avoir été traités plus tard dans une seule session ; le nombre de clips n'est pas un nombre de resets. L'écriture du dossier SD-01 du 21 février à 00:01:32 en 2000, différente de celle du fichier, interdit aussi de transformer toutes ces valeurs en une même seconde certaine de démarrage.

### Affichage du 31 décembre 1999 : préciser le sens de conversion

Une date naïve FAT **2000-01-01 00:00:26**, interprétée comme locale à Paris puis convertie en UTC, devient bien **1999-12-31 23:00:26Z**. Inversement, traiter ce minuit comme UTC puis l'afficher à Paris donne **2000-01-01 01:00:26+01:00**. Les deux sens sont reproduits dans [le calcul de conversion](recherche-transversale/20261016/inventaires/conversion-1999.json).

Cela précise les formulations des rapports SD-02/SD-03 : Paris peut produire la veille dans le premier sens de conversion ; il ne la produit pas dans le second. **La convention réellement employée dans l'affichage rapporté reste inconnue.** Aucune de ces conversions n'explique pourquoi la valeur de 2000 a été écrite, ni n'authentifie la provenance du signalement de la cliente. Aucune date FAT explicite de 1999 n'est identifiée dans les entrées déjà examinées.

## 7. Mécanismes distinguables et indices d'intervention extérieure

| Mécanisme envisagé | Éléments compatibles | Ce qui manque pour le démontrer |
| --- | --- | --- |
| Défaut de finalisation ou reconstruction | Même erreur audio dans onze fichiers, excédents vidéo répétés, index et médias en désaccord, journaux auxiliaires | Code/firmware ou expérience reproduisant exactement les défauts ; moment et logiciel ayant finalisé les fichiers |
| Interruption d'enregistrement | Données référencées absentes dans certains clips, temporaire SD-02, fins de pistes différentes | Journal d'état ou d'alimentation ; distinction entre données jamais écrites et données perdues ensuite |
| Redémarrage | Dates de référence très proches, reprise/finalisation possible | Journal de boot, compteur de démarrages, reproduction de la séquence ; aucun reset usine n'est déduit |
| Perte de synchronisation horaire | Date FAT 2000 avec nom et image 2024 | Journal NTP/horloge ; démonstration du champ concerné ; une simple dérive d'heure n'explique pas seule les compteurs MP4 |
| Modification ou récupération ultérieure | État acquis en 2026, métadonnées de traitement postérieures, possibilité de dates conservées/modifiées | Version antérieure authentifiée, traces d'un outil ou poste reliant une modification précise aux onze fichiers |
| Intervention intentionnelle ou accès distant | Aucun marqueur propre identifié dans les traces examinées | Journaux de session/configuration, compte, commande, outil ou acte attribuable ; une anomalie n'est pas une preuve d'intention |

Le classement le mieux étayé concerne **un chemin récurrent de finalisation/reconstruction défaillant**, avec origine et déclencheur inconnus. Les mécanismes peuvent se combiner : un redémarrage peut déclencher une reprise, mais une reprise n'implique pas nécessairement un redémarrage. Une date aberrante seule ne démontre ni formatage ni retour aux paramètres d'usine.

**Traces positives de traitement hors du seul contenu vidéo :** les trois cartes portent `System Volume Information`, `WPSettings.dat` et `IndexerVolumeGuid`. Les créations FAT des fichiers sont proches le **12 novembre 2024** : vers **23:35:28 sur SD-01**, **23:37:25 sur SD-03**, **23:51:46 sur SD-02**. Cette succession est compatible avec une manipulation des trois volumes dans un environnement Windows. Elle constitue une piste transversale de traitement ultérieur à examiner sur le poste concerné, **sans prouver un même poste, une même session, une personne ou une modification des vidéos**. Ces dates dépendent elles aussi d'horloges non étalonnées et peuvent avoir été conservées.

Les correspondances de fichiers actifs précédemment recensées entre cartes ne concernent que le marqueur `.rw` vide : elles ne démontrent pas une copie commune des vidéos. Les anciens renommages de répertoire, le nettoyage des temporaires et la réutilisation de clusters SD-02 ne sont pas datables comme des actes intentionnels ciblés sur février ou le 15 octobre. L'activité d'une application caméra sur un téléphone, citée dans les rapports antérieurs, ne devient pas une session établie sur une carte par seule proximité temporelle.

**Aucune trace positive ne relie une personne, une connexion distante ou une modification intentionnelle aux anomalies étudiées.** Cela n'exclut pas une opération ancienne sans trace survivante. La présence de fichiers compatibles Windows n'est pas effacée de l'analyse, mais son niveau de preuve reste distinct de celui d'une intervention sur les enregistrements.

## 8. Réponses aux six questions et investigations désormais utiles

| Question | Réponse défendable |
| --- | --- |
| Événement commun en février sur SD-01/SD-03 ? | Même signature de défaut établie ; événement commun proche de 23:41 le 21 février plausible, sans synchronisation ni cause commune démontrées. Toutes les anomalies de février ne se superposent pas. |
| Défaut SD-03 mieux caractérisé ? | Oui : cumul audio inscrit à la place du reste, excédents vidéo de 13/26 dans certains cas, références hors médias, données non indexées ; le 15 possède une erreur vidéo intermédiaire et un audio prolongé décodable. |
| Mécanisme simultané FAT 2000 / MP4 incohérent ? | Une finalisation/reprise avec date de référence explique conjointement les constats de façon compatible. Le processus réel, son déclencheur et sa date ne sont pas prouvés. |
| Peut-on choisir entre redémarrage, horloge, interruption, clôture et modification ultérieure ? | Le défaut de tables est démontré ; sa cause et son contexte restent indéterminés. Une simple erreur d'affichage horaire ne suffit pas à expliquer les défauts MP4. |
| Caractéristiques nouvelles le 15 octobre ? | Signature audio ancienne ; excédent audio de 11,589 s exceptionnel dans le corpus et longue lacune suivante. Aucun nouveau mécanisme causal ou intentionnel établi. |
| Intervention intentionnelle/extérieure positive ? | Traitement des volumes compatible Windows documenté séparément ; aucune connexion ni intervention intentionnelle sur les clips anormaux identifiée. |

Les recherches de meilleure valeur ne sont plus un nouveau carving exhaustif : retrouver l'affichage original et son contexte ; identifier modèles/firmwares ; rechercher les journaux de boot, d'heure, d'application et de compte ; tester sur une **autre carte** l'interruption et la reprise, en contrôlant ensemble les mots FAT et les compteurs MP4 ; identifier le poste ayant traité les volumes en novembre. Un procès-verbal préciserait les horaires de procédure, sans remplacer les traces de caméra.

Une expérience de firmware devra comparer les octets des tables, les tailles, les données non indexées, les durées de pistes et les heures FAT : obtenir seulement une date de 2000 ne reproduirait pas la signature complète. Aucun contact, accès à un compte, publication ou transfert n'est réalisé dans ce complément.

## 9. Livraison technique et traçabilité

Résultats : [recherche-transversale/20261016](recherche-transversale/20261016/). Quatre scripts locaux permettent la reproduction dans un répertoire neuf ; les sources historiques restent inchangées. Le [guide](recherche-transversale/20261016/README.md) décrit les populations, les commandes, les expériences en RAM, les incidents et le contrôle du manifeste. Les manifestes historiques sont conservés ; un manifeste propre au complément couvre les nouveaux résultats et ce rapport.

Les expériences ne produisent pas une nouvelle version originale des vidéos. Les médias privés antérieurs doivent accompagner une remise technique sécurisée : le dépôt Git seul est insuffisant. Les journaux publics nouveaux contiennent des données techniques, pas des images ni une transcription sonore. Les résultats donnent des états et des relations techniques ; ils ne datent ni n'attribuent avec certitude les opérations historiques qui les ont produits.
