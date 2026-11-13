# Rapport d’analyse technique transversale des cartes SD-01, SD-02 et SD-03

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev

**Supports :** SD-01 — chambre ; SD-02 — terrasse ; SD-03 — salon

## 1. Objet et périmètre

Ce rapport compare les enregistrements, structures de fichiers et métadonnées des trois cartes afin de caractériser les défauts communs, les récupérations possibles et les événements signalés en **février 2024** et le **15 octobre 2024**. Il distingue un mécanisme commun de production de fichiers, un éventuel incident physique commun et une intervention humaine : ces propositions ne nécessitent pas les mêmes preuves.

La cliente déclare une installation des caméras après mars 2023, une réinitialisation de la **chambre en février 2024** et un fonctionnement **continu de la terrasse**. L’affichage « 31/12/1999 » et l’autre événement du 15 octobre ne sont pas rattachés à une interface ou un fichier d’origine authentifiés. Les [mails](../docs/mail.txt) et [complémentaires](../docs/mail-2.txt) documentent ces déclarations, sans constituer des journaux de réinitialisation.

**Les caméras et cartes n’étaient pas sous scellés.** Leurs enregistrements après la perquisition ne constituent donc pas une anomalie pour cette seule raison. Les traces des téléphones et les horaires du PV apportent du contexte, sans étalonner les horloges des caméras ou démontrer une commande sur une carte. L’analyse est une investigation privée, sans désignation comme expertise judiciaire.

## 2. Synthèse des conclusions

| Question | Résultat technique | Portée et limite |
|---|---|---|
| Les cartes partagent-elles un système de production ? | Organisation `record/.record_tmp`, modèle auxiliaire commun et descriptions de pistes identiques dans les copies comparées. | Une famille commune de production est étayée, sans modèle exact ou firmware identifié. |
| Les anomalies de dates sont-elles accompagnées d’un défaut précis ? | **Onze vidéos SD-01/SD-03 datées en FAT de janvier 2000** portent le même compteur audio fautif. | Un chemin récurrent de finalisation/reconstruction défaillant est fortement étayé ; son déclencheur reste inconnu. |
| Les défauts se limitent-ils aux dates ? | Non : compteurs incohérents, références hors données et médias non indexés. **Quatre images supplémentaires** sont décodables dans deux fichiers. | Elles n’ont pas de nouveaux temps de présentation validés et ne constituent pas des vidéos complètes récupérées. |
| Un incident commun en février est-il établi ? | Les fins nominales de deux clips du **21 février vers 23:41** sont proches. | Incident commun plausible, sans synchronisation civile, coupure ou redémarrage commun démontrés. |
| Que distingue le 15 octobre ? | Sur SD-03 : défaut audio récurrent, erreur H.264 intermédiaire, **excédent audio de 11,589 s** et lacune du corpus jusqu’au 29. | Ces particularités sont confirmées, sans cause, heure certaine d’arrêt ou intention établies. |
| SD-02 confirme-t-elle une continuité d’enregistrement ? | Corpus actuel discontinu malgré le fonctionnement continu déclaré ; stockage circulaire fortement étayé. | Les lacunes ne sont pas une mesure du temps d’extinction et ne prouvent pas une suppression ciblée. |
| Une intervention extérieure est-elle démontrée ? | Auxiliaires compatibles Windows sur les trois cartes, sans poste ni auteur identifié. | Aucun reset usine, formatage daté, accès distant ou acte malveillant n’est établi. |

**La conclusion la mieux étayée concerne un défaut récurrent de fabrication ou de reconstruction des index, associé aux dates FAT de 2000. Elle ne démontre ni un incident unique commun aux caméras, ni une réinitialisation effective, ni une manipulation intentionnelle.**

## 3. Sources, méthode et portée des contrôles

### 3.1. Corpus et préservation

Les constats reposent sur les [rapports SD-01](analyse-cartes_sd-SD-01.md), [SD-02](analyse-cartes_sd-SD-02.md) et [SD-03](analyse-cartes_sd-SD-03.md), leurs inventaires, structures FAT, extractions MP4 et résultats FFprobe/FFmpeg. Le [rapport d’acquisition](analyse-cartes_sd.md) et l’[attestation](../remise-documents/attestation-de-remise.md) documentent les supports. Les limites d’identification physique et de conservation des rapports individuels restent applicables.

La comparaison binaire ciblée porte sur **37 copies complètes** : **21 SD-01, trois SD-02 et treize SD-03**, comprenant **les dix-sept anomalies de tables connues et vingt témoins**. Un parseur distinct vérifie **74 pistes** : comptes d’échantillons, temps, positions des blocs, limites des données et délimitation des unités H.264.

Les **vingt slots FAT portant au moins une date de 2000** sont contrôlés sur leurs octets conservés, y compris les alias de répertoires et le marqueur vide. Ils ne représentent pas vingt événements indépendants. Les **4 391 empreintes d’artefacts consommés** concordent avec les manifestes dans le périmètre du contrôle consigné, sans authentifier les opérations antérieures à l’acquisition de 2026.

Les essais de correction d’index ou de lecture des médias résiduels utilisent des **copies en mémoire**, sans modifier les extraits conservés ou les images EWF. Une copie expérimentale n’est pas une nouvelle vidéo originale réparée. Les observations visuelles proviennent des échantillons documentés dans les rapports individuels ; aucun visionnage humain intégral des trois corpus ou interprétation sémantique de l’audio n’est établi.

### 3.2. Limites de temps et d’interprétation

Les dates FAT ne stockent pas de fuseau ; l’écriture a une granularité de deux secondes, la création un champ supplémentaire de précision et le dernier accès une précision de journée. Noms et incrustations restent des indications de l’horloge du producteur, sans référence civile indépendante.

La durée d’un conteneur, la fin d’une piste vidéo, la dernière image produite et la fin audio sont des mesures distinctes. Une structure de boîte cohérente ou une longueur d’unité H.264 valide ne garantit pas le décodage de toutes les images. Un code retour FFmpeg nul peut coexister avec des erreurs consignées dans son journal.

L’image de 2026 ne constitue pas un instantané de 2024. Une copie peut conserver dates et défauts ; des données écrasées ou non exposées par le contrôleur peuvent ne plus être récupérables. Les relations numériques sont contrôlables, mais ne datent pas automatiquement l’opération qui les a produites.

## 4. Comparaison des supports et des résultats de récupération

### 4.1. Populations conservées

| Population active | SD-01 — chambre | SD-02 — terrasse | SD-03 — salon |
|---|---:|---:|---:|
| MP4 actifs | **674** | **3 301**, dont un temporaire | **2 431** |
| MP4 finalisés analysables | **674** | **3 300** | **2 431** |
| MP4 aux dates FAT de 2000 | **2** | **0** | **9** |
| MP4 avec anomalies de tables retenues | **7** | **0 parmi les finalisés** | **10** |
| MP4 nommés du 15 octobre | **37** | **0 disponible** | **65** |
| Couverture nominale principale | **02/12/2023–28/10/2024**, 81 jours représentés | **05–12/11/2024**, plus un clip au nom impossible daté du 21 octobre par ses images | **04/11/2023–31/10/2024**, 175 jours représentés |

Les **6 405 MP4 finalisés** comprennent **onze cas couplant date FAT 2000 et compteur audio cumulatif erroné**, **six autres erreurs terminales avec dates ordinaires**, et **6 388 fichiers sans les anomalies de tables retenues**. Il s’agit d’une association dans ce corpus, sans calcul de probabilité de cause ou hypothèse d’indépendance statistique.

Les dates disponibles ne couvrent pas continûment la période depuis mars 2023. SD-02 conserve en outre des vestiges nommés du 4 novembre, sans restitution de tous leurs contenus. Son cas `20242010` reste séparé du calendrier des noms valides.

### 4.2. Système de production commun

Les 37 copies comparées ont les mêmes descriptions `stsd` audio et vidéo. Les trois cartes partagent l’organisation de dossiers, le modèle auxiliaire **`.moov` de 1 006 octets** et les dates internes MP4 conventionnelles de **1970**, distinctes des dates FAT de 2000.

La géométrie FAT32, les sauvegardes FSInfo anciennes et l’octet d’état du boot ne datent pas un incident. L’identifiant de volume est commun à SD-01/SD-02 et différent sur SD-03 ; ce n’est pas une série matérielle. **Les ressemblances étayent une famille de production et de stockage, sans démontrer un matériel, firmware ou événement physique unique.**

Le temporaire non finalisé de SD-02 illustre un état de production inachevé, mais n’est pas un témoin de février ou du 15 octobre. L’absence de défaut de tables retenu parmi ses 3 300 finalisés montre que les onze anomalies couplées ne sont pas obligatoires pour chaque fichier de cette famille.

### 4.3. Suppressions et récupérations : résultats distincts

| Support | Résultat de récupération | Interprétation |
|---|---|---|
| **SD-01** | Trois temporaires reliés à une vidéo finale toujours présente ; aucune vidéo effacée distincte supplémentaire. | Nettoyage de finalisation fortement étayé, pas trois enregistrements perdus. |
| **SD-02** | **Onze vidéos complètes**, soit **44 min 36,096 s**, et **126,464 s** de la fin d’une douzième, nominalement du **5 novembre**. | Contenus survivants validés avec hypothèses d’ordre de clusters documentées ; le fragment n’est pas le fichier original complet. |
| **SD-02, temporaire actif** | **68,992 s** lisibles dans un conteneur dérivé limité aux données complètes de la taille logique. | Fichier non finalisé du 12 novembre, pas une vidéo supprimée ; le prolongement en erreur n’est pas validé. |
| **SD-03** | Trois temporaires associés à un final présent ; **3,849 s** restaurées après la fin logique d’un fichier actif du 29 février. | Récupération partielle d’un actif endommagé, pas une vidéo supprimée distincte. |

Les **quatre images non indexées** détaillées ci-dessous sont un autre résultat : sans temps de présentation reconstitués, elles ne sont ajoutées ni à une nouvelle durée de vidéo validée ni aux récupérations complètes. Une absence de récupération ne prouve pas l’absence historique d’effacement.

## 5. Signature arithmétique commune et défauts associés

### 5.1. Le même compteur audio fautif dans onze vidéos

`stsz` décrit les tailles et le nombre d’échantillons ; `stsc` les répartit par bloc, appelé *chunk*, dont la position est donnée par `stco`. **La valeur attendue est un nombre d’échantillons par bloc, pas un cumul.** Dans les onze cas, la dernière entrée reprend le cumul précédent alors que sept échantillons restent à répartir.

| Carte et TSK | Date et début nominaux | Audio total | Cumul avant dernier bloc | Valeur inscrite | Reste attendu |
|---|---|---:|---:|---:|---:|
| SD-01, **20903944** | 21/02/2024, 23:39:14 | 1 183 | 1 176 | 1 176 | **7** |
| SD-01, **22835208** | 01/03/2024, 04:05:05 | 98 | 91 | 91 | **7** |
| SD-03, **12727332** | 09/11/2023, 18:19:05 | 308 | 301 | 301 | **7** |
| SD-03, **261989424** | 21/02/2024, 23:22:37 | 1 491 | 1 484 | 1 484 | **7** |
| SD-03, **261989436** | 21/02/2024, 23:33:45 | 602 | 595 | 595 | **7** |
| SD-03, **261989444** | 21/02/2024, 23:41:03 | 343 | 336 | 336 | **7** |
| SD-03, **266341920** | 29/02/2024, 10:26:10 | 364 | 357 | 357 | **7** |
| SD-03, **266341968** | 29/02/2024, 10:56:00 | 42 | 35 | 35 | **7** |
| SD-03, **266341984** | 29/02/2024, 11:01:39 | 910 | 903 | 903 | **7** |
| SD-03, **266342024** | 29/02/2024, 11:27:25 | 161 | 154 | 154 | **7** |
| SD-03, **714049800** | 15/10/2024, 13:28:00 | 2 170 | 2 163 | 2 163 | **7** |

La correspondance exacte sur deux cartes et plusieurs mois soutient fortement un même défaut de calcul ou chemin de finalisation/reconstruction. La correction du seul compteur audio peut laisser l’avertissement `wrong sample count` lorsque le compteur vidéo est également erroné. Après correction expérimentale des compteurs concernés, l’avertissement disparaît dans les **onze essais FFprobe**.

**Ce résultat démontre l’origine de l’avertissement dans les comptes d’index, sans certifier les médias, restaurer des temps manquants ou prouver que la table de référence était historiquement correcte.** Les défauts existent dès novembre 2023 ; ils ne sont pas propres au séjour rapporté en février ou à la perquisition.

### 5.2. Sept excédents de compteur vidéo

| Carte et TSK | Valeur vidéo inscrite → reste calculé | Excédent |
|---|---|---:|
| SD-01, **20903944** | 35 → 9 | **26** |
| SD-01, **22835208** | 17 → 4 | **13** |
| SD-03, **261989436** | 22 → 9 | **13** |
| SD-03, **261989444** | 15 → 2 | **13** |
| SD-03, **266341920** | 33 → 7 | **26** |
| SD-03, **266341968** | 24 → 11 | **13** |
| SD-03, **266342024** | 38 → 12 | **26** |

Des blocs de treize échantillons sont présents. L’excédent correspond à une ou deux unités de ce découpage : **la relation numérique est établie, l’algorithme fautif exact ne l’est pas**.

Les cinq autres anomalies SD-01 et celle de décembre SD-03 relèvent d’une seconde famille : sept échantillons audio sont annoncés dans le dernier bloc alors qu’il n’en reste qu’un à trois. Leurs dates FAT sont ordinaires. Une erreur de clôture peut donc exister sans anomalie de date ; elle ne prouve pas une coupure d’alimentation pour chaque fichier.

### 5.3. Médias absents et médias présents sans index complet

**Huit des onze fichiers de 2000** ont des blocs référencés hors du `mdat` : SD-01 du 1er mars et sept cas SD-03 de novembre/février. Des références atteignent des métadonnées ou dépassent le fichier ; ces octets ne sont pas des images simplement parce qu’un index les désigne.

Les trois autres — SD-01 du 21 février, SD-03 du 29 février à 10:26:10 et SD-03 du 15 octobre — conservent les tailles référencées dans le `mdat`. Deux possèdent aussi des zones non indexées :

| Fichier | Offset logique de la zone | Taille de zone | Résultat du test borné |
|---|---:|---:|---|
| SD-01, **20903944** | **12 281 990** | **903 034 octets** | Trois unités H.264 supplémentaires au début : **2 170 → 2 173 images**, sans avertissement. |
| SD-03, **266341920** | **5 308 698** | **15 489 octets** | Une unité supplémentaire : **673 → 674 images**, sans avertissement. |

Les essais exploitent des octets existants sans inventer d’image ou d’horodatage. Pour SD-01, **14 348 octets** sont utilisés ; les **888 686 restants** ne sont pas attribués à une continuation valide. Aucun temps de présentation de ces quatre images n’est reconstitué et aucun examen visuel de leur contenu n’est revendiqué.

**Compteurs incohérents, données référencées absentes et données présentes sans index complet sont trois constats distincts.** Ils sont compatibles avec une clôture ou reprise utilisant des états de tables et de médias différents, sans démontrer qu’un fichier initialement sain a été modifié après sa production.

## 6. Dates FAT de 2000 et affichage de 1999

### 6.1. Valeurs réellement stockées

Les onze vidéos portent des créations/écritures FAT proches de **00:00:26–00:00:28 le 1er janvier 2000**, malgré leurs noms et les incrustations examinées de 2023/2024. Les valeurs sont inscrites dans les octets FAT : il ne s’agit pas seulement de l’affichage d’un champ nul. Aucune date FAT explicite de 1999 n’est identifiée dans les entrées examinées.

Les alias `.` et `..`, les dates des dossiers et un dernier accès du marqueur `.rw` ne sont pas comptés comme des réinitialisations indépendantes. Les dossiers reprennent fréquemment les dates liées aux premiers ou derniers clips. Une date de dossier dite de création ne garantit donc pas une première initialisation du support.

La concentration autour de 26–28 secondes est compatible avec un chemin de traitement répétable, **sans être un chronomètre de démarrage validé**. Plusieurs clips peuvent être finalisés dans une même reprise ultérieure ; leur nombre n’est pas un nombre de redémarrages ou resets.

### 6.2. Mécanisme compatible et cause non établie

Un scénario compatible est le suivant : médias, noms, incrustations et journaux auxiliaires sont produits ; une interruption ou un défaut laisse des états différents en mémoire et sur carte ; une clôture ou reprise construit les tables à partir de ces états et inscrit une date de référence. Cela pourrait associer un compteur erroné et une date FAT 2000 à des images conservant 2024.

Les modèles et journaux étayent l’architecture générale de production. **Ni une reprise au démarrage, ni l’ordre exact écriture/date/synchronisation, ni une coupure n’est observé directement.** Une erreur sans redémarrage, une variable non initialisée ou un traitement ultérieur restent compatibles. Aucune architecture de double horloge matérielle n’est affirmée.

### 6.3. Sens de la conversion « 31/12/1999 »

| Interprétation d’une date FAT naïve | Résultat |
|---|---|
| `2000-01-01 00:00:26` traitée comme locale à Paris, puis convertie en UTC | **`1999-12-31 23:00:26Z`** |
| Même valeur traitée comme UTC, puis affichée à Paris | **`2000-01-01 01:00:26+01:00`** |

**Le sens de conversion peut expliquer un affichage de la veille, mais la convention réellement employée par l’interface de la cliente reste inconnue.** Ce calcul n’explique pas pourquoi la valeur de 2000 a été inscrite et n’authentifie pas la provenance de son signalement.

## 7. Comparaison de février et mars 2024

### 7.1. Fins proches le 21 février vers 23:41

| Mesure nominale | SD-01, **20903944** | SD-03, **261989444** |
|---|---|---|
| Début du nom | **23:39:14** | **23:41:03** |
| Fin de piste vidéo selon les tables | **23:41:45,924** | **23:41:47,101** |
| Dernière PTS d’image produite en lecture indexée | **23:41:45,851** | **23:41:44,023** |
| Fin audio selon les tables | **23:41:45,424** | **23:41:46,904** |
| Écriture FAT | **01/01/2000 00:00:28** | **01/01/2000 00:00:26** |
| Limite | Au moins trois images non indexées décodables | **587 images produites sur 630 annoncées** |

Les comparaisons homogènes donnent **1,828 s entre dernières PTS indexées produites** et **1,177 s entre fins vidéo de tables, dans l’autre ordre**. L’écart de **1,901 s** mélange une fin de piste SD-01 et une dernière image SD-03 ; il ne doit pas devenir une mesure de simultanéité.

La proximité des fins et la même signature rendent **plausible un incident commun**, sans le démontrer. Les horloges ne sont pas étalonnées, une fin perd des images et l’autre n’indexe pas tous ses médias. Un traitement différé pourrait aussi produire des métadonnées semblables. **Ni simultanéité civile, ni coupure commune, ni redémarrage commun ne sont établis.**

Les deux autres anomalies SD-03 de cette soirée, à **23:22:37 et 23:33:45**, sont séparées par des clips aux dates ordinaires. Un voisin normal finit nominalement à **23:39:50,144** et le suivant est nommé **23:44:14**. Cette alternance ne permet pas de compter trois redémarrages. SD-01 ne conserve ce soir-là que le fichier anormal comparé.

### 7.2. Le 29 février et le 1er mars

SD-03 comporte quatre cas anormaux le 29 février, entrecoupés de fichiers cohérents. SD-01 conserve douze clips du même jour aux écritures FAT normales ; celui de **11:27:08 à 11:27:42,432** recouvre une partie du clip SD-03 de 11:27:25 endommagé. Les anomalies ne se reproduisent donc pas systématiquement aux mêmes heures nominales sur les deux cartes.

Le clip SD-01 du **1er mars à 04:05:05** a la signature audio commune mais ne produit en lecture indexée que **134 images sur 185**, dernière PTS **9,309 s**, contre **12,950 s** de durée annoncée. Son journal résiduel conserve davantage de tailles que la table finale. La fin nominale n’est pas une fin lisible certaine.

**Même famille de mécanisme fortement étayée ; événement commun du 21 février possible ; événement unique ou panne continue expliquant toutes les anomalies de février/mars non démontrés.**

## 8. Dernière vidéo du salon le 15 octobre 2024

### 8.1. Défaut récurrent et particularité audio

Le dernier MP4 SD-03, **714049800**, `20241015_132800_10_0277.mp4`, porte la date FAT 2000 et le compteur audio cumulatif fautif. Son dossier reprend cette date, tandis que ses alias gardent **15/10/2024 08:02:36**. Fichier et dossier ne sont pas deux événements indépendants de reset.

Le champ audio à l’offset **32 865 034** vaut **2 163 au lieu de sept**. Sa correction sur copie supprime l’avertissement de compte. Le compteur vidéo terminal est cohérent — six échantillons attendus et annoncés — et les longueurs NAL contrôlées concordent avec les tailles.

| Population comparée | Plus grand excédent audio sur vidéo |
|---|---:|
| SD-01, 674 vidéos | **0,528 s** |
| SD-02, 3 300 finalisés actifs | **0,671 s** |
| SD-03, hors dernier clip du 15 | **0,657 s** |
| SD-03, dernier clip du 15 | **11,589 s** |

Ce fichier comporte **2 170 échantillons AAC**, durée audio **277,760 s**, contre **266,171 s de piste vidéo**, avec **3 802 images produites**. Après correction du compteur sur copie, l’audio produit **2 222 080 échantillons PCM mono à 8 kHz**, exactement 277,760 s, sans avertissement. Les fenêtres après la fin de piste vidéo portent un signal non nul.

Les données audio occupent notamment les **23 296 octets** de `mdat` entre la fin du dernier bloc vidéo à **32 841 225** et la fin des données à **32 864 521**. Elles sont dans la taille logique et référencées. **L’excédent n’est donc ni une durée fictive due au seul compteur erroné ni une extension exclusivement composée de silence numérique.**

Les pistes se terminent différemment dans l’état enregistré. Arrêt de production vidéo, perte d’index ou de données, calcul temporel défaillant et reprise/assemblage ultérieur restent compatibles. Sans étalonnage des pistes, **il n’est pas démontré que ce son ait été capté exactement 11,589 secondes civiles après la dernière image**. Aucun sens n’est attribué à son contenu.

### 8.2. Erreur intermédiaire et dernières images

Le contrôle ciblé situe l’erreur H.264 `left block unavailable for requested intra mode` et une dissimulation d’erreurs autour de l’image d’indice zéro **1 788**, PTS **125,176 s**, offset **15 423 494**. Le temps nominal correspondant est **13:30:05,176**, sans précision civile indépendante.

Des images sont ensuite produites jusqu’à la dernière PTS **266,103 s**, nominalement **13:32:26,103**, sans nouvelle erreur vidéo terminale signalée. Les **3 802 images produites ne sont pas toutes garanties intactes**, puisqu’une image est produite avec dissimulation d’erreurs. Cette erreur intermédiaire ne date donc pas une troncature terminale ou une coupure à 13:32:26.

La fin audio nominale **13:32:37,760** est distincte de la dernière image et d’une heure certaine d’arrêt. L’heure rapportée pour l’allumage des téléphones ne permet pas d’attribuer le défaut vidéo ou la fin du clip à une manipulation. Les deux clips précédents, nommés **13:24:49 et 13:26:34**, passent les contrôles prioritaires sans avertissement.

### 8.3. Lacune et comparaison intercartes

Aucun MP4 SD-03 référencé ne porte un nom du **16 au 28 octobre** ; le nom suivant est le **29 octobre à 17:59:18**. La lacune ne départage pas arrêt, alimentation, réglages, absence de déclenchement ou données perdues/supprimées sans trace survivante.

SD-01 conserve **37 vidéos du 15**, sans anomalie spécifique de reset identifiée, dont des clips après les dernières images du salon et jusqu’à une fin nominale vers **22:46:17**. Un arrêt prolongé simultané de toutes les caméras n’est donc pas étayé ; un événement bref commun ou limité à une caméra n’est pas exclu. SD-02 ne dispose pas des séquences nécessaires pour trancher.

**Le défaut de compteur est ancien et récurrent ; l’excédent audio et la longue lacune sont des particularités du cas. Ces différences ne démontrent ni cause nouvelle, ni réinitialisation, ni intention.**

## 9. Terrasse : stockage circulaire et corpus discontinu

SD-02 est occupée à environ **99,11 %** ; **315 des 326 entrées de fichiers supprimés** pointent désormais à l’intérieur de chaînes actives. La saturation, les enregistrements plus récents et la réutilisation étayent fortement une gestion circulaire remplaçant les contenus anciens. Ce mécanisme ne date pas les suppressions ni leur auteur.

La cliente déclare pourtant une captation continue. L’union des intervalles nominaux des **vidéos actives à nom datable**, sans double comptage des recouvrements, donne :

| Journée intérieure du corpus, novembre 2024 | Part nominale de 24 heures couverte |
|---|---:|
| 6 novembre | **62,466 %** |
| 7 novembre | **62,655 %** |
| 8 novembre | **64,937 %** |
| 9 novembre | **48,892 %** |
| 10 novembre | **50,992 %** |
| 11 novembre | **52,340 %** |

Les supprimés récupérés, le temporaire non finalisé et le nom impossible sont exclus de ce calcul. **Les lacunes du corpus ne sont pas assimilées à un arrêt habituel démontré ni au temps certain d’extinction de la caméra.** Réglage historique, interruption, écrasement/suppression, défaut de production ou datation restent à départager.

Le remplacement circulaire peut expliquer la disparition d’anciens fichiers, y compris sur un système enregistrant en continu ; il ne démontre pas la cause de chaque lacune du flux conservé. Aucune vidéo du 15 octobre n’est récupérée sur SD-02, donc aucun effacement ciblé ou geste sur la terrasse ce jour-là n’est établi à partir des enregistrements disponibles.

## 10. Traitements ultérieurs, modèles et accès extérieurs

### 10.1. Auxiliaires compatibles avec Windows

Les trois cartes portent `System Volume Information`, `WPSettings.dat` et `IndexerVolumeGuid`. Les créations FAT des deux fichiers auxiliaires sont proches le **12 novembre 2024**, selon les valeurs brutes non étalonnées :

| Support | Heure FAT approximative |
|---|---|
| **SD-01** | **23:35:28** |
| **SD-03** | **23:37:25** |
| **SD-02** | **23:51:46** |

Cette succession est compatible avec un traitement des trois volumes dans un environnement Windows. **Elle ne prouve pas un même poste, une même session, un opérateur ou une modification des vidéos.** Ces dates peuvent aussi avoir été conservées lors d’un traitement ultérieur.

Les recherches dans les ruches complètes et journaux System/PnP/stockage/SetupAPI d’OP-01 n’obtiennent pas de rattachement positif des cartes à ce poste. L’absence de correspondance n’exclut pas une insertion ancienne dont les traces ont disparu. Les identifiants de volume ne sont pas des séries matérielles uniques.

Les fichiers actifs communs par SHA-256 entre cartes ne concernent que **`.rw` vide**, pas des vidéos identiques. Anciens noms de répertoires, temporaires retirés et clusters réutilisés ne datent pas des actes intentionnels ciblés sur février ou le 15 octobre.

### 10.2. Modèles, firmwares et historiques caméra

Les caches LSC `home/detailv1` et `home/list313` ne sont pas décodés par les sondages documentés. Les **54 ressources voisines** décodables en base64 puis JSON contiennent des traductions, pas une preuve de version installée. Les **104 fichiers sources** consommés par ce contrôle conservent les empreintes d’extraction ; ce résultat valide les dérivés, pas le firmware historique.

**Aucun modèle exact ni firmware des trois caméras associées aux cartes n’est identifié par ces pièces.** Les versions de l’application, panneaux et mini-applications ne sont pas assimilées à celles du micrologiciel. L’échec des sondages non exhaustifs ne prouve pas l’absence de ces informations dans les caches opaques.

Les catalogues et états LSC ne reconstituent pas un historique complet des comptes, partages, réappairages ou visionnages depuis mars 2023. Les configurations Xiaomi identifiées ailleurs ne sont pas reliées matériellement à une des trois cartes par ces seuls rapprochements.

### 10.3. Téléphones, réseau et procédure

La séquence Wi-Fi de TP-02, les traitements système de TP-03 et les présences Freebox restent propres à leurs artefacts et limites de provenance. **Aucun lien technique ne démontre une commande de caméra depuis un téléphone pendant la fermeture des scellés ou une responsabilité dans les lacunes SD.** Une proximité horaire ne remplace pas une session, un identifiant d’équipement ou une commande.

Le PV consulté distingue la mise sous scellés des appareils concernés après **14:19 le 15 octobre**, l’arrivée de la cliente le **28 à 10:22**, l’ouverture du PC à **10:41**, celle des téléphones à **11:30** et la clôture à **19:20**, sans heure individuelle de restitution. Ces repères ne datent pas une réinitialisation caméra et ne permettent pas de forcer la concordance d’horloges non étalonnées.

## 11. Hypothèses, limites et conclusion technique

### 11.1. Mécanismes distingués

| Mécanisme envisagé | Éléments compatibles | Ce qui manque pour le démontrer |
|---|---|---|
| **Finalisation ou reconstruction défaillante** | Signature audio commune, excédents vidéo, index/médias en désaccord, journaux auxiliaires | Firmware ou expérience reproduisant les défauts exacts ; moment et logiciel responsables. |
| **Interruption d’enregistrement** | Médias référencés absents, temporaire inachevé, fins de pistes différentes | Journal d’état/alimentation ; distinction entre données jamais écrites et perdues ensuite. |
| **Redémarrage** | Dates de référence proches, possibilité de reprise de fichiers | Journal de boot ou compteur validé ; le nombre de clips ne compte pas les démarrages. |
| **Défaut d’horloge ou de synchronisation** | Dates FAT 2000 avec noms/images 2024 | Journal d’horloge/NTP ; une erreur d’affichage seule n’explique pas les compteurs MP4. |
| **Copie, récupération ou modification ultérieure** | Acquisition tardive et métadonnées de traitements postérieurs | Version antérieure authentifiée ou trace d’outil/poste reliant une transformation précise aux fichiers. |
| **Intervention intentionnelle ou distante** | Aucun marqueur propre identifié dans les données examinées | Session, compte, commande, outil ou acte attribuable ; une anomalie ne démontre pas une intention. |

Les mécanismes peuvent se combiner : un redémarrage peut déclencher une reprise, sans que toute reprise implique un redémarrage. Une remise à l’heure, un redémarrage, un retour aux paramètres d’usine et un formatage sont des opérations différentes. **Aucune n’est établie par la seule date FAT 2000.**

### 11.2. Limites et éléments discriminants

La conservation est tardive et incomplète pour l’histoire recherchée. Les horloges caméra ne sont pas étalonnées ; FAT32 ne fournit pas de journal complet des modifications, accès ou suppressions. Les contenus peuvent être copiés avec leurs dates et défauts ; les états supprimés, écrasés ou non adressables ne sont pas tous récupérables.

La comparaison ciblée des 37 copies ne constitue pas un décodage exhaustif et indépendant de chaque vidéo des trois cartes. Les résultats de population reposent aussi sur les contrôles individuels. Les essais bornés valident des relations de tables et certains médias résiduels, sans certifier une absence de montage antérieur techniquement propre ou une origine humaine/automatique.

Les éléments les plus discriminants seraient :

- l’affichage original de 1999 et son contexte, pour déterminer le champ et la convention de conversion réellement utilisés ;
- les modèles, firmwares et réglages historiques, ainsi que les journaux de démarrage, synchronisation horaire, compte et application ;
- les traces du poste ayant traité les cartes en novembre ;
- une expérience sur **un autre support**, reproduisant ensemble les valeurs FAT, les compteurs, les tailles, les données non indexées et les fins de pistes. Obtenir seulement une date de 2000 ne reproduirait pas la signature complète.

Ces expériences ne sont pas réalisées et la disponibilité des archives n’est pas présumée. Une répétition de recherche ne recrée pas des traces déjà écrasées.

### 11.3. Conclusion

**Les cartes chambre et salon partagent un défaut arithmétique précis dans onze vidéos aux dates FAT de 2000, dès novembre 2023. Les incohérences de compteurs, les références hors données et les médias non indexés étayent fortement un chemin récurrent de finalisation ou reconstruction défaillant.** Le logiciel, son déclencheur et la date réelle du traitement restent inconnus.

La proximité des fins du **21 février** rend un incident commun plausible, sans démontrer une coupure ou un redémarrage simultanés. Les autres cas de février/mars ne forment pas une panne continue commune établie.

Le dernier clip du **15 octobre sur SD-03** associe la signature ancienne à une erreur vidéo intermédiaire, un excédent audio décodable de **11,589 s** et une longue lacune du corpus. Les dernières images produites, la fin audio et l’heure d’arrêt de la caméra restent des notions distinctes. SD-01 conserve des enregistrements ultérieurs ce jour-là ; SD-02 ne permet pas de vérifier les événements de la perquisition en vidéo.

**Aucun retour aux paramètres d’usine, formatage daté, accès extérieur ou acte malveillant n’est démontré.** Les auxiliaires Windows documentent séparément un traitement possible des volumes, sans poste ni auteur identifié. Les lacunes et l’absence de récupération complète ne prouvent pas l’absence historique d’intervention.

## 12. Pièces techniques et termes de lecture

### 12.1. Sources de contrôle

| Domaine | Pièces de référence |
|---|---|
| Supports et résultats individuels | [SD-01](analyse-cartes_sd-SD-01.md), [SD-02](analyse-cartes_sd-SD-02.md), [SD-03](analyse-cartes_sd-SD-03.md), [acquisition](analyse-cartes_sd.md) |
| Méthode, scripts et traçabilité | [Guide de reproduction](recherche-transversale/20261016/README.md), [dossier des résultats](recherche-transversale/20261016/) |
| Compteurs et références de médias | [Tables ciblées](recherche-transversale/20261016/inventaires/tables-ciblees.json), [excédents et zones non indexées](recherche-transversale/20261016/inventaires/compteurs-video-et-zones-non-indexees.json), [tests d’index](recherche-transversale/20261016/inventaires/test-index-audio-video.json) |
| Images résiduelles | [Tests H.264 non indexés](recherche-transversale/20261016/inventaires/nal-non-indexes.json) |
| Février et mars | [Chronologie croisée](recherche-transversale/20261016/inventaires/chronologie-croisee.csv), [fins comparées](recherche-transversale/20261016/inventaires/fins-comparees.json) |
| Dernier clip du 15 | [Audio et signal](recherche-transversale/20261016/inventaires/audio-714049800.json), [erreur vidéo](recherche-transversale/20261016/inventaires/video-erreur-714049800.json), [distributions SD-01/SD-03](recherche-transversale/20261016/inventaires/ecarts-audio-video.json), [population active SD-02](recherche-transversale/20261016/inventaires/ecarts-audio-video-SD02-actifs.json) |
| Conversion 1999/2000 | [Calcul des deux sens de conversion](recherche-transversale/20261016/inventaires/conversion-1999.json) |
| Couverture, continuité et comptes caméra | [Analyse du retour de la cliente](../investigations/20261019-retour-cliente/compte-rendu.md), [couverture nominale SD-02](../investigations/20261019-retour-cliente/resultats/local-v2/sd-daily-nominal-coverage.json) |
| Traitements Windows et modèles | [Recoupements avec OP-01](../investigations/20261017-recroisements/compte-rendu.md), [modèles et firmwares](../investigations/20261109-identification-cameras/compte-rendu.md) |
| Téléphones et procédure | [Lecture du PV](../investigations/20261108-analyse-pv/compte-rendu.md), [comparaison des téléphones](../investigations/20261110-telephones/compte-rendu.md), [hypothèses d’intervention](../investigations/20261110-revue-intervention-scelles/compte-rendu.md) |

Les pièces conservent valeurs brutes, offsets, localisateurs, paramètres et empreintes. Les essais sur copies sont distincts des originaux. Les médias et blocs privés doivent accompagner une remise technique sécurisée : le dépôt Git seul ne contient pas tous les contenus nécessaires aux contrôles. Les manifestes historiques restent attachés à leurs jeux de résultats et versions de rapport.

### 12.2. Termes techniques

| Terme | Sens dans ce rapport |
|---|---|
| **FAT / slot / alias** | Système de fichiers / entrée de répertoire / références internes `.` et `..`. Plusieurs dates recopiées ne sont pas autant d’événements. |
| **`moov` / `mdat` / `.stbl`** | Métadonnées du MP4 / données audio-vidéo / journal auxiliaire de production. Un modèle ou un index n’est pas une vidéo supplémentaire. |
| **`stsz` / `stsc` / `stco` / `stts`** | Tables de tailles et comptes / répartition par bloc / positions des blocs / temps des échantillons. Leur comparaison révèle des incohérences d’index. |
| **NAL / AVC / H.264** | Unités et format du flux vidéo compressé. Une longueur valide ne garantit pas l’intégrité du contenu de l’image. |
| **PTS / fin de piste** | Temps de présentation / fin calculée de la piste. La dernière image produite peut différer de la durée déclarée. |
| **EOF / conteneur dérivé** | Fin logique d’un fichier / nouvelle structure indexant des médias existants récupérés, distincte de l’original. |
| **FSInfo / identifiant de volume** | Métadonnées de gestion de l’espace FAT / valeur de volume, sans date fiable de formatage ni série physique unique. |

### 12.3. Références de formats

Les interprétations de format s’appuient notamment sur [Apple — Sample-to-chunk atom](https://developer.apple.com/documentation/quicktime-file-format/sample-to-chunk_atom) et [Microsoft — File Times](https://learn.microsoft.com/en-us/windows/win32/sysinfo/file-times). Elles définissent la fonction des champs et leur précision, sans expliquer à elles seules la cause historique des défauts observés.
