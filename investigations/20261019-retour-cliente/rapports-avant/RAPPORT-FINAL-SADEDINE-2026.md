# Rapport final d’investigation informatique — Mme Malika Sadedine

**Référence :** SADEDINE-2026  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Destinataire :** Me Delphine Ravon, avocate de Mme Malika Sadedine  
**Date du rapport :** 18 octobre 2026  
**Nature :** investigation informatique indépendante réalisée à la demande de la cliente, sans désignation comme expert judiciaire.

## 1. Objet de la mission

La mission portait sur l’utilisation du matériel pendant les périodes signalées, les éventuels accès par des tiers, les copies, transferts ou suppressions de données, les téléphones et le réseau, ainsi que les enregistrements de caméra et les anomalies de dates ou réinitialisations évoquées par Mme Sadedine.

Le périmètre effectivement analysé comprend l’ordinateur **OP-01** (portable ASUS), une sauvegarde du téléphone **TP-02** (iPhone 13 mini), la **Freebox Révolution** et trois cartes de caméra : **SD-01 — chambre**, **SD-02 — terrasse**, **SD-03 — salon**.

**TP-01 et TP-03 n’ont pas fait l’objet de cette campagne d’analyse**, car ils étaient indisponibles. L’attestation initiale mentionne TP-01 comme remis et TP-03 comme non remis le 6 octobre 2026 ; elle ne décrit pas à elle seule leur disponibilité lors de la campagne complémentaire.

Cette synthèse reprend les résultats déjà documentés, en donnant priorité au compte rendu général du **17 octobre 2026** et aux conclusions actualisées. Les procès-verbaux de procédure et le journal de création de la sauvegarde du téléphone sur Mac étaient indisponibles et n’ont pas été consultés.

## 2. Résumé des conclusions

**Windows présente des traces d’activité sur OP-01 le 15 octobre 2024 vers 10 h 43, puis le 28 octobre à partir de 10 h 41.** Les traces sont cohérentes avec une mise en veille prolongée le 15 vers 10 h 53 et une reprise le 28. Aucune activité Windows corroborée n’a été retrouvée entre les deux ; des manipulations non enregistrées restent possibles.

**Le 28 octobre 2024, plusieurs opérations sur les données de l’ordinateur sont documentées.** Un regroupement local de fichiers dans le dossier `L16B` est fortement étayé ; des fichiers issus d’exports sont présents. **Dix mises à la corbeille sont enregistrées**, dont celle d’un document de gestion de mots de passe et d’une archive contenant 94 fichiers. Le document et l’archive ont été récupérés.

Les traces Windows mentionnent également trois identifiants distincts de périphériques USB Kingston. Des références à des fichiers sur un volume Kingston sont relevées vers **17 h 26–17 h 27**. **Ces traces n’établissent pas quels fichiers auraient été copiés vers ces supports**, ni même qu’une telle copie a abouti.

**La sauvegarde de TP-02 conserve des traces datées pendant la privation d’accès déclarée**, notamment des traitements internes et une association Wi-Fi le 17 octobre, puis plusieurs opérations le 28. Leur présence ne suffit pas à attribuer chaque opération au téléphone physique à la date affichée, ni à une personne : des données anciennes peuvent avoir été synchronisées ou restaurées.

**Les recherches sur l’ordinateur, le téléphone et la Freebox ne démontrent aucun accès distant non autorisé.** Certains appareils réseau sont identifiés, d’autres restent inconnus. Leur présence sur le réseau ne démontre pas une intrusion.

**Sur la terrasse, onze vidéos supprimées ont été récupérées entièrement et une douzième partiellement**, toutes situées au 5 novembre 2024 selon les indications de la caméra. Un enregistrement temporaire du 12 novembre, non supprimé, a aussi été restauré partiellement.

**Au salon, la dernière vidéo conservée sur SD-03 pour le 15 octobre commence à 13 h 28 selon la caméra et présente des anomalies.** La dernière image techniquement décodée se situe vers 13 h 32 min 26 s selon la caméra ; la durée sonore dépasse celle de l’image de **11,589 secondes**. Aucun fichier vidéo référencé ne couvre les 16 à 28 octobre ; les fichiers disponibles reprennent le 29. La cause de cette lacune reste inconnue.

**Onze vidéos provenant des caméras de la chambre et du salon présentent exactement le même défaut dans leur structure informatique, accompagné de dates incohérentes de janvier 2000.** Observé dès novembre 2023, ce défaut semble lié à la manière dont les caméras terminent ou récupèrent leurs enregistrements ; sa cause exacte reste inconnue. Aucune intervention malveillante, réinitialisation volontaire ou identité d’auteur n’a été établie. L’absence de preuve retrouvée ne signifie pas qu’aucun événement n’a eu lieu.

## 3. Chronologie des faits constatés

Les heures informatiques sont en **heure de Paris** : UTC+2 avant le changement d’heure du 27 octobre 2024, puis UTC+1. Les heures caméra sont celles des fichiers ou images, sans synchronisation vérifiée avec les autres appareils. Les déclarations de la cliente sont distinguées des traces.

| Date et heure | Équipement | Fait constaté | Ce que cela permet d’établir |
|---|---|---|---|
| 15 octobre 2024, vers 10 h 43 à 10 h 53 | OP-01 | Reprise de Windows, session locale, puis veille prolongée avec batterie faible. | Fonctionnement du système ; auteur et position exacte par rapport au début de la perquisition inconnus. |
| 15 octobre, de 13 h 28 à environ 13 h 32 min 26 s, horloge caméra | SD-03, salon | Dernière vidéo conservée sur SD-03 pour cette journée, présentant des anomalies. | Présence d’images jusqu’à l’heure affichée ; aucune heure certaine d’arrêt de la caméra. |
| 15 octobre, vers 13 h 30 — déclaration | Téléphones | Mme Sadedine indique ne plus avoir accès à ses téléphones. | Repère déclaré, sans constituer l’heure vérifiée du début de la perquisition. |
| 16 octobre, 5 h 51 min 7 s | OP-01 | Heure de réveil programmé inscrite dans un événement du 15. | Une échéance prévue, **pas un réveil effectivement constaté**. |
| 16 octobre, 21 h 27 min 48 s | Freebox | Première activité conservée pour `DESKTOP-ICPNCMD`. | Présence réseau d’un ordinateur non identifié ; aucune action sur des fichiers démontrée. |
| 17 octobre, vers 17 h 15–17 h 18, puis 17 h 25 | Données de TP-02 | Traitements internes, puis propriétés d’association au réseau `ASUS_Z01RD`. | Séquence compatible avec un système iPhone en fonctionnement ; origine physique et manipulation humaine non certaines. |
| 27 octobre, vers 2 h 44–2 h 45, avant le changement d’heure | Données de TP-02 | Regroupement de 3 123 dates de modification dans la photothèque. | Traitement groupé possible ; aucune preuve de consultation ou retouche de chacune des photos. |
| 28 octobre, vers 10 h 22 — déclaration | Matériels concernés par les scellés | Début d’ouverture indiqué par la cliente. | Repère à confronter au procès-verbal indisponible. |
| 28 octobre, 10 h 41 min 56 s, puis 10 h 47–11 h 11 | OP-01 | Reprise de Windows ; créations de fichiers regroupées dans `L16B/LOCAL`. | Activité après l’ouverture déclarée ; regroupement local fortement étayé. |
| 28 octobre, 13 h 25–13 h 57 | OP-01 | Interactions enregistrées avec des fichiers de messages sous `L16B/MESSAGERIES`. | Manipulations par le système ou les applications ; lecture humaine de chaque message non démontrée. |
| 28 octobre, 14 h 50–14 h 52 | OP-01 | Créations groupées dans `L16B/GDRIVE`, puis mise à la corbeille du document de mots de passe et de l’archive de téléchargement. | Regroupement local fortement étayé et suppressions datées ; contenus récupérés. |
| 28 octobre, vers 16 h 27, 17 h et 17 h 14 | OP-01 | Installation et démarrage associés à trois identifiants distincts de périphériques Kingston, selon les heures locales du journal Windows. | Présence de supports externes, sans preuve autonome de copie. |
| 28 octobre, 17 h 26–17 h 27 | OP-01 | Références à trois fichiers sur un volume Kingston. | Interactions avec ces chemins ; contenu de l’archive externe inconnu. |
| 28 octobre, vers 19 h 20 — déclaration | Matériels restitués | Récupération indiquée par Mme Sadedine. | Repère déclaré de fin de privation d’accès. |
| 29 octobre, 17 h 59 min 18 s, horloge caméra | SD-03, salon | Reprise des noms de fichiers vidéo disponibles. | Fin de la lacune documentaire, sans explication de sa cause. |
| 12 novembre 2024, vers 23 h 35–23 h 51, dates des cartes | Trois cartes SD | Création datée de fichiers auxiliaires caractéristiques de Windows. | Traitement des cartes compatible avec Windows ; poste, auteur et modification des vidéos non établis. |

## 4. Résultats concernant l’ordinateur

### Activité du 15 au 28 octobre

Les traces étayent l’activité du 15 et la reprise du 28, séparées par une veille prolongée. L’échéance programmée du 16 et les dates anciennes présentes dans certains fichiers ne suffisent pas à établir un fonctionnement de Windows pendant l’intervalle.

**Le 28 octobre, Windows reprend à 10 h 41 min 56 s**, environ vingt minutes après l’ouverture déclarée vers 10 h 22. Des traces de session et d’applications sont enregistrées avant la restitution déclarée ; leur rapprochement avec les actes de procédure reste à effectuer. Outlook affiche des demandes de confirmation de suppression définitive et d’enregistrement de propriétés de messages. **Les réponses et la réussite de ces suppressions ne sont pas établies**, contrairement aux mises à la corbeille documentées ci-dessous.

### Données regroupées, archives et suppressions du 28 octobre

Le dossier `L16B` contient des documents locaux, des données Google Drive et iCloud, des messageries, des données de téléphones et des documents comptables ou bancaires. La concentration des dates de création et les comparaisons de contenus soutiennent fortement un **regroupement local de données le 28 octobre**. La présence d’archives de conversations téléphoniques ne démontre pas leur extraction directe depuis un téléphone connecté à OP-01.

Les deux archives Outlook ont été lues lors des compléments. Une archive Google Takeout contient une messagerie et un manifeste indiquant un export le 28 octobre à 12 h 42 min 33 s, heure de Paris. **La présence de fichiers issus d’exports est établie ; leur production sur OP-01 ne l’est pas.** Ils peuvent avoir été créés ailleurs puis copiés sur cet ordinateur. Ni la machine ayant demandé l’export ni son demandeur ne sont identifiés.

**Dix mises à la corbeille sont enregistrées le 28 octobre**, entre 11 h 02 et 15 h 24 : deux raccourcis, un document de gestion de mots de passe, une archive de téléchargement, cinq fichiers du dossier d’états de Ciel et `L16B/test.pdf`. Les cinq fichiers Ciel ne doivent pas être présentés comme une base comptable détruite.

L’archive récupérée contient **94 fichiers**. Parmi eux, **93 sont identiques aux fichiers conservés dans `L16B/GDRIVE`**. Le document de gestion de mots de passe, absent de ce dossier actuel, subsiste à la fois dans l’archive récupérée et séparément dans la corbeille. Aucune consultation ou utilisation des identifiants n’est démontrée ; aucune valeur confidentielle n’est reproduite ici.

Le PDF récupéré `test.pdf` contient deux factures. Ses informations internes indiquent une impression PDF à **15 h 19 min 42 s**, suivie d’une mise à la corbeille à **15 h 24 min 17 s**, sans auteur identifié.

Les archives `GDRIVE.zip` et `GDRIVE (2).zip` présentent des erreurs, mais **les contenus des 93 fichiers contrôlés sont retrouvés intacts dans `L16B/GDRIVE`**. L’intégrité des contenus ne signifie donc pas celle des archives. Ces dernières portent des dates de création locale de juillet 2026 ; l’origine et la date de leurs défauts restent inconnues.

### Supports externes et limites des transferts

Les journaux Windows enregistrent le 28 octobre **trois identifiants distincts de périphériques USB Kingston DataTraveler**. Il s’agit bien d’identifiants différents, et non du seul comptage de trois événements de connexion. Le rapprochement avec les supports physiques reste à effectuer. Entre **17 h 26 min 19 s et 17 h 27 min 29 s**, les historiques d’interaction référencent un volume nommé Kingston et trois fichiers sous `E:\saddedine\` :

- `Archive_saddedine.zip` ;
- `Inventaire_saddedine.csv` ;
- `Rejets_saddedine.txt`.

**Ces trois noms sont à rechercher dans les pièces de procédure et sur les supports de destination.** L’archive externe elle-même n’a pas été récupérée. Son contenu, son intégrité et son rattachement à l’un des trois identifiants de périphériques ne sont pas établis. Aucun lien de contenu ne permet d’affirmer qu’elle contient `L16B` ou les archives Outlook.

Des traces concernent aussi un dispositif Western Digital et le lancement de son programme de déverrouillage. Elles ne démontrent pas un déverrouillage réussi. **Le regroupement sur le PC, la présence de fichiers issus d’exports et les références au volume Kingston sont trois constats distincts : ils ne démontrent pas une copie de ces données vers un support externe déterminé.** Aucun destinataire d’un transfert sortant n’a été identifié.

### Accès à distance et attribution

Aucune prise en main à distance non autorisée n’est démontrée. Des invitations anciennes à une téléassistance Sage, datées de 2022, et un raccourci de téléassistance de 2023 ne prouvent pas une session effectivement établie. Une détection de document trompeur en mai 2024 est suivie d’une mise en quarantaine déclarée réussie, sans compromission réussie démontrée.

Le compte Windows observé est `fintm`. **Il n’identifie pas la personne ayant utilisé le poste.** Aucun effacement ou falsification des journaux destiné à masquer une activité n’a été établi.

## 5. Résultats concernant les téléphones

La sauvegarde examinée est rattachée à **TP-02 par son numéro de série**. Elle contient des traces datées concernant les appels, les messages, les photographies, le Wi-Fi et les applications. **Ces dates ne prouvent pas que le téléphone physique a été manipulé aux heures indiquées** : certaines données peuvent avoir été synchronisées avec d’autres appareils ou restaurées ultérieurement.

Le **17 octobre**, des traitements internes vers 17 h 15–17 h 18 précèdent une association Wi-Fi à `ASUS_Z01RD` vers 17 h 25. Cet enchaînement est compatible avec un système iPhone actif, y compris automatiquement, sans démontrer un déverrouillage ni une consultation humaine.

La sauvegarde contient **53 enregistrements d’appels datés du 15 au 26 octobre 2024**, pendant la privation d’accès déclarée. Ces données ne permettent pas d’affirmer que ces appels ont été passés ou reçus sur ce téléphone physique pendant cette période, ni d’identifier une personne à l’origine des opérations.

Le **28 octobre**, les éléments les plus utiles sont des états « lu » de SMS, des associations Wi-Fi à 12 h 31 et 14 h 32, une séquence compatible avec une capture d’écran vers 13 h 36 et des traitements de Photos vers 17 h 31–17 h 32. Les états « lu » peuvent avoir été transmis depuis un autre appareil ou restaurés : ils ne démontrent pas une lecture locale des SMS. L’image de la capture manque ; aucun auteur ni extraction par un tiers n’est identifié.

À **17 h 39**, LSC Smart Connect conserve des ressources compatibles avec le chargement ou l’actualisation d’un panneau caméra. **Aucun visionnage de vidéo n’est démontré.** Les catalogues examinés ne contiennent aucune référence de média du 15 au 28 octobre et ne constituent pas un historique complet des accès. Xiaomi Home fournit surtout des configurations permettant des rapprochements avec des équipements réseau.

Le nom `ASUS_Z01RD` apparaît aussi dans des traces d’OP-01, probablement parmi des réseaux Wi-Fi disponibles. Ces traces ne sont pas datées et ne prouvent ni une connexion du PC à ce réseau, ni sa présence au même endroit que TP-02, ni l’émission de ce réseau par OP-01.

## 6. Résultats concernant la Freebox et les connexions

Le rapprochement des identifiants réseau confirme que **`LAPTOP-RMCOB2VU` correspond à OP-01**.

En revanche, **`DESKTOP-ICPNCMD` reste non identifié**. Sa première activité conservée est datée du 16 octobre 2024 à 21 h 27 min 48 s. Aucun élément ne permet de l’attribuer à une personne ou à l’administration.

Trois identités « iPhone » se succèdent dans les traces des 16 et 17 octobre. Elles ne sont pas rattachées aux adresses Wi-Fi conservées dans TP-02. Les changements d’adresse et les lacunes des historiques empêchent toutefois d’exclure ce téléphone.

Une entrée auparavant inconnue correspond exactement à une configuration de caméra Xiaomi de modèle `mxiang.camera.mwc11` dans TP-02. Le rapprochement d’une seconde caméra Xiaomi reste partiel, car ses identifiants ne concordent pas exactement. Ces modèles ne sont pas reliés avec certitude aux trois cartes SD ; aucun accès aux images n’est reconstitué.

Deux **tentatives échouées d’accès au partage de fichiers d’OP-01**, le 26 mars 2024 à 15 h 20 min 36 s et 15 h 21 min 12 s, proviennent d’une adresse locale associée dans l’inventaire Freebox à `LAPTOP-205Q5H9C`. Ce rapprochement est plausible, sans attribution certaine à cet appareil au moment exact des tentatives. Aucun accès réussi n’en découle.

**Aucun accès distant non autorisé n’a été démontré.** La Freebox fournit des traces de présence réseau, mais pas un historique complet des fichiers lus, des volumes transférés ou des sessions d’administration depuis 2021/2022. L’accès distant activé en septembre 2026 à la demande du prestataire relève de la mission autorisée ; il ne décrit pas la situation d’octobre 2024.

## 7. Résultats concernant les caméras

**Les caméras n’ont jamais été placées sous scellés.** Leurs enregistrements après la perquisition ne constituent donc pas, par eux-mêmes, une anomalie.

### SD-01 — Chambre

La carte conserve **674 vidéos**, dont **37 du 15 octobre 2024**. Certaines prolongent les enregistrements de cette journée jusqu’à environ 22 h 46 selon la caméra. Aucun indice spécifique de réinitialisation le 15 octobre n’a été identifié.

Aucune vidéo supprimée supplémentaire n’a été récupérée. Trois fichiers temporaires supprimés sont très fortement reliés à la fabrication d’une vidéo encore présente ; ils ne représentent pas trois enregistrements distincts disparus.

Des anomalies de lecture existent. Deux vidéos nommées du **21 février et du 1er mars 2024** portent des dates de fichiers de janvier 2000 alors que les images contrôlées affichent 2024. La vidéo du 1er mars est partiellement endommagée.

### SD-02 — Terrasse

**Onze vidéos supprimées ont été récupérées entièrement**, représentant environ 44 minutes et 36 secondes. **La fin d’une douzième vidéo a été récupérée**, pour environ 2 minutes et 6 secondes. Ces vidéos, situées au **5 novembre 2024** selon la caméra, passent les contrôles de lecture.

Un **enregistrement temporaire du 12 novembre a été restauré partiellement**, sur environ 69 secondes. Il était encore présent mais non terminé : **il ne s’agit pas d’une vidéo supprimée**.

La carte presque pleine comporte de nombreuses traces de suppression et de réutilisation des anciens emplacements. L’ensemble est fortement compatible avec un **remplacement automatique des anciennes vidéos lorsque le stockage est plein**, sans établir le mécanisme de chaque suppression.

Aucune vidéo du 15 octobre ou de février/mars n’a été récupérée. Un ancien dossier porte une date de janvier 2000 ; un autre fichier possède un nom de date impossible alors que ses images indiquent le 21 octobre 2024. Ces anomalies ne démontrent ni réinitialisation ni effacement intentionnel.

### SD-03 — Salon

La carte conserve **65 vidéos du 15 octobre 2024**, parmi 2 431 vidéos disponibles. La dernière vidéo conservée sur SD-03 pour cette journée commence à **13 h 28 selon l’horloge de la caméra**. Ses informations de fichier indiquent janvier 2000, tandis que les images contrôlées affichent le 15 octobre 2024.

Ce fichier présente une anomalie de production : la piste sonore dure **11,589 secondes de plus que la piste vidéo**. Le son correspondant existe et peut être décodé.

La **dernière image techniquement décodée se situe vers 13 h 32 min 26 s**, selon le début et les temps de lecture du fichier. Un aperçu effectivement examiné près de cette fin affiche également 13 h 32 min 26 s. Une autre erreur affecte la lecture d’image vers **13 h 30 min 05 s**, selon le même calcul ; des images subsistent ensuite.

**Ces anomalies ne permettent pas de déterminer si la caméra a été arrêtée, redémarrée ou manipulée à ce moment.** Le supplément sonore n’a pas été interprété comme preuve d’une action ou d’un arrêt précis. L’écart des durées ne démontre pas une captation du son exactement 11,589 secondes après la dernière image en heure réelle.

**Aucune vidéo référencée ne porte une date du 16 au 28 octobre. Les fichiers disponibles reprennent le 29 octobre à 17 h 59 min 18 s**, selon la caméra. Cette lacune mérite l’attention, mais sa cause reste indéterminée : arrêt, absence de déclenchement ou perte d’enregistrements ne peuvent pas être départagés.

Aucune vidéo supprimée distincte et complète n’a été récupérée. Un fragment d’environ quatre secondes a toutefois été restauré à la fin d’une vidéo déjà présente mais endommagée du 29 février ; ce résultat est distinct des suppressions.

### Conclusions communes

**Onze vidéos provenant des caméras de la chambre et du salon présentent exactement le même défaut dans leur structure informatique, accompagné de dates incohérentes de janvier 2000.** Ce défaut, observé dès novembre 2023, semble lié à la manière dont les caméras terminent ou récupèrent leurs enregistrements.

Ces concordances étayent fortement le caractère récurrent du défaut, sans en identifier la cause exacte.

Une conversion horaire peut expliquer comment une date du début de janvier 2000 s’affiche au 31 décembre 1999, sans expliquer pourquoi cette date a été enregistrée. L’affichage observé par la cliente reste inconnu. Son mail évoque « février » sans année ; les analyses ont retenu février 2024 pour comparaison.

**Une réinitialisation en février ou le 15 octobre n’a pas été démontrée. Aucun formatage intentionnel ni effacement malveillant n’a été établi.** Les fichiers auxiliaires Windows datés du 12 novembre documentent séparément un traitement possible des cartes sur ordinateur ; ils ne démontrent pas une modification des vidéos. Le poste concerné n’a pas été identifié, y compris après les recherches complémentaires sur OP-01.

## 8. Éléments inexpliqués et limites des conclusions

- **Auteur inconnu :** aucun compte, nom d’appareil ou horaire ne permet d’identifier la personne ayant effectué les opérations.
- **Historiques incomplets :** les traces conservées ne recensent pas tous les accès distants ni toutes les opérations anciennes. Des enregistrements ont pu être remplacés, particulièrement sur la terrasse.
- **Horloges non comparées à une référence commune :** une proximité entre heure caméra, heure informatique et heure déclarée ne prouve pas un événement simultané.
- **Signalements de réinitialisation non authentifiés :** l’interface, le message et les fichiers à l’origine des deux observations de la cliente restent inconnus.
- **Pièces absentes :** les procès-verbaux ne permettent pas, à ce stade, de confronter les traces aux heures et opérations de procédure. Le journal de sauvegarde Mac manque pour préciser la provenance des données anciennes de TP-02 ; TP-01 et TP-03 n’ont pas été analysés.

Le rapport Freebox relève aussi une divergence non résolue pour une première activité du **4 mars 2024** entre une ancienne retranscription et les données exportées. Les heures corrigées à partir des données brutes ont été privilégiées ; cette entrée n’est pas utilisée dans la chronologie des faits du 15 au 28 octobre.

## 9. Conservation des données, traçabilité et situation de remise

**Cette section concerne la conservation et la livraison des données en 2026. Elle ne sert pas à interpréter les événements de 2024.**

Mme Sadedine a demandé la conservation de l’ensemble des données extraites sur le cloud du prestataire pendant la durée prévue au devis et sur un disque dur neuf fourni par elle. La réalisation de ces deux copies doit être attestée avant la remise définitive.

Le **contrôle du 17 octobre 2026 constate un inventaire cloud incomplet** : des éléments d’OP-01 et de SD-03 ainsi que la sauvegarde TP-02 ne figurent pas intégralement dans le stockage contrôlé, pour environ **165,22 Go manquants par rapport aux acquisitions locales**. Ce constat ne couvre pas un éventuel autre stockage non inventorié. L’inventaire des extractions et résultats doit également être complété.

**Aucun document ultérieur consulté n’atteste la régularisation de cette situation ou la réalisation de la seconde copie sur disque.** La durée contractuelle de conservation n’est pas documentée par les pièces disponibles. Le présent rapport n’atteste donc pas l’achèvement de la conservation.

Avant la remise définitive, il reste à finaliser les copies, vérifier leur complétude et leur identité avec les données conservées, identifier le disque de destination et établir un bordereau de remise. L’attestation prévoit la restitution des matériels au plus tard le **6 novembre 2026**. Ces obligations pratiques ne constituent aucun indice d’une intervention sur les équipements en 2024.

### Traçabilité de la remise et de l’acquisition

Deux divergences documentaires restent à signaler. L’attestation porte la date du **6 octobre 2026**, alors que des notes d’intervention indiquent une remise le **7 octobre à 16 h 15**. Les horaires notés pour l’acquisition d’OP-01 en 2026 ne sont pas entièrement raccordés aux horaires automatiques. Ces écarts concernent la documentation de la mission, sans établir une manipulation en 2024.

## Éléments à confronter aux pièces de procédure

1. Comparer les opérations constatées sur OP-01 le **28 octobre**, dès **10 h 41 min 56 s**, avec le procès-verbal : ouverture déclarée vers 10 h 22, personnes présentes, consultations, copies, **dix mises à la corbeille** et supports utilisés.
2. Vérifier si les supports Kingston et les noms **`Archive_saddedine.zip`, `Inventaire_saddedine.csv` et `Rejets_saddedine.txt`** figurent dans les inventaires ou pièces de procédure ; rapprocher ces mentions des références enregistrées vers **17 h 26–17 h 27**.
3. Comparer la chronologie de la dernière vidéo conservée du salon pour le **15 octobre** avec les horaires et opérations consignés, en tenant compte de l’absence de synchronisation vérifiée entre les horloges.

## 10. Conclusion générale

**Faits établis :** des traces d’activité d’OP-01 les 15 et 28 octobre, des opérations identifiées sur des fichiers le 28, des références à des supports externes, des traces datées dans la sauvegarde TP-02, des vidéos supprimées récupérées et des anomalies techniques récurrentes des enregistrements. La dernière vidéo conservée du salon et la lacune qui la suit sont précisément documentées, sans cause certaine.

**Faits non établis :** une intrusion non autorisée, l’identité de la personne responsable des opérations, une réinitialisation volontaire, un formatage intentionnel ou une suppression malveillante. Ni une copie des données vers un support externe déterminé ni un transfert vers un destinataire identifié ne sont démontrés. Les pièces de procédure pourront confirmer, expliquer ou contredire les rapprochements envisagés, sans que les traces seules permettent d’attribuer une intention malveillante.

## Documents techniques de référence

- [Compte rendu général et compléments du 17 octobre 2026](investigations/20261017-recroisements/compte-rendu.md).
- [Ordinateur OP-01](ordinateur/analyse-ordinateur.md), [opérations du 28 octobre](ordinateur/recherche-OP-01/operations-28oct/compte-rendu.md) et [limites de datation du réseau ASUS_Z01RD](ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/datation.md).
- [Téléphone TP-02](telephones/analyse-TP-02.md) et [Freebox](freebox/analyse-freebox.md).
- [SD-01 — chambre](cartes_sd/analyse-cartes_sd-SD-01.md), [SD-02 — terrasse](cartes_sd/analyse-cartes_sd-SD-02.md), [SD-03 — salon](cartes_sd/analyse-cartes_sd-SD-03.md) et [comparaison des trois cartes](cartes_sd/analyse-cartes_sd-transversale.md).
- Sources de cadrage : [demandes de Mme Sadedine](docs/mail.txt) et [attestation de remise](remise-documents/attestation-de-remise.md).
