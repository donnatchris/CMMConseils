# Rapport final d’investigation informatique — Mme Malika Sadedine

**Référence :** SADEDINE-2026  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Destinataire :** Me Delphine Ravon, avocate de Mme Malika Sadedine  
**Date du rapport :** 19 octobre 2026 ; mise à jour le 9 novembre 2026  
**Nature :** investigation informatique indépendante réalisée à la demande de la cliente, sans désignation comme expert judiciaire.

## 1. Objet de la mission

La mission portait sur l’utilisation du matériel pendant les périodes signalées, les éventuels accès par des tiers, les copies, transferts ou suppressions de données, les téléphones et le réseau, ainsi que les enregistrements de caméra et les anomalies de dates ou réinitialisations évoquées par Mme Sadedine.

Le périmètre effectivement analysé comprend l’ordinateur **OP-01** (portable ASUS), une sauvegarde du téléphone **TP-02** (iPhone 13 mini), la **Freebox Révolution** et trois cartes de caméra : **SD-01 — chambre**, **SD-02 — terrasse**, **SD-03 — salon**.

**TP-01 et TP-03 n’ont pas fait l’objet de cette campagne d’analyse**, car ils étaient indisponibles. L’attestation initiale mentionne TP-01 comme remis et TP-03 comme non remis le 6 octobre 2026 ; elle ne décrit pas à elle seule leur disponibilité lors de la campagne complémentaire.

Cette synthèse intègre les résultats antérieurs, le [complément du 19 octobre](investigations/20261019-retour-cliente/compte-rendu.md) et la [lecture du PV du 8 novembre](investigations/20261108-analyse-pv/compte-rendu.md). Le PV est désormais disponible et a été consulté ; ses énonciations sont distinguées des constats techniques et des observations de la cliente annexées. Le [complément technique du 8 novembre](investigations/20261108-complement-pv/compte-rendu.md) expose les nouveaux contrôles et les travaux encore suspendus ; la [reprise du 9 novembre](investigations/20261108-complement-pv/reprise-20261109.md) intègre les résultats SIFT récupérés. Le journal de création de la sauvegarde sur Mac demeure indisponible.

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
| 28 octobre, 10 h 22 puis 10 h 41 — PV | Présence de la cliente, puis OP-01 | Arrivée de la cliente à 10 h 22 ; ouverture du scellé du PC à 10 h 41. | Repères documentaires distincts, concordance à la minute avec la reprise Windows. |
| 28 octobre, 11 h 30 puis 11 h 45 — PV | Téléphones | Ouverture des scellés 2 à 4 ; insertion de SIM dans le téléphone du scellé 3 pour un code Apple. | Actes consignés ; correspondance avec TP-02 ou TP-03 non établie. |
| 28 octobre, 10 h 41 min 56 s, puis 10 h 47–11 h 11 | OP-01 | Reprise de Windows ; créations de fichiers regroupées dans `L16B/LOCAL`. | Activité après l’ouverture déclarée ; regroupement local fortement étayé. |
| 28 octobre, 13 h 25–13 h 57 | OP-01 | Interactions enregistrées avec des fichiers de messages sous `L16B/MESSAGERIES`. | Manipulations par le système ou les applications ; lecture humaine de chaque message non démontrée. |
| 28 octobre, 14 h 50–14 h 52 | OP-01 | Créations groupées dans `L16B/GDRIVE`, puis mise à la corbeille du document de mots de passe et de l’archive de téléchargement. | Regroupement local fortement étayé et suppressions datées ; contenus récupérés. |
| 28 octobre, vers 16 h 27, 17 h et 17 h 14 | OP-01 | Installation et démarrage associés à trois identifiants distincts de périphériques Kingston, selon les heures locales du journal Windows. | Présence de supports externes, sans preuve autonome de copie. |
| 28 octobre, 17 h 26–17 h 27 | OP-01 | Références à trois fichiers sur un volume Kingston. | Interactions avec ces chemins ; contenu de l’archive externe inconnu. |
| 28 octobre, 19 h 20 — PV et déclaration | Matériels | Clôture du PV ; restitution consignée sans heure individuelle. | Le PV ne date pas séparément la remise de chaque appareil. |
| 29 octobre, 17 h 59 min 18 s, horloge caméra | SD-03, salon | Reprise des noms de fichiers vidéo disponibles. | Fin de la lacune documentaire, sans explication de sa cause. |
| 12 novembre 2024, vers 23 h 35–23 h 51, dates des cartes | Trois cartes SD | Création datée de fichiers auxiliaires caractéristiques de Windows. | Traitement des cartes compatible avec Windows ; poste, auteur et modification des vidéos non établis. |

## 4. Résultats concernant l’ordinateur

### Activité du 15 au 28 octobre

Les traces étayent l’activité du 15 et la reprise du 28, séparées par une veille prolongée. L’échéance programmée du 16 et les dates anciennes présentes dans certains fichiers ne suffisent pas à établir un fonctionnement de Windows pendant l’intervalle.

**Le 28 octobre, Windows reprend à 10 h 41 min 56 s**, ce qui concorde à la minute avec l’ouverture du scellé d’OP-01 consignée au PV à **10 h 41**. **10 h 22 correspond à l’arrivée de la cliente**, et non à l’ouverture du PC. Le PV décrit le regroupement L16B et des exports. Outlook affiche des demandes de confirmation de suppression définitive et d’enregistrement de propriétés de messages. **Les réponses et la réussite de ces suppressions ne sont pas établies**, contrairement aux mises à la corbeille documentées ci-dessous.

### Données regroupées, archives et suppressions du 28 octobre

Le dossier `L16B` contient des documents locaux, des données Google Drive et iCloud, des messageries, des données de téléphones et des documents comptables ou bancaires. La concentration des dates de création et les comparaisons de contenus soutiennent fortement un **regroupement local de données le 28 octobre**. La présence d’archives de conversations téléphoniques ne démontre pas leur extraction directe depuis un téléphone connecté à OP-01.

Les deux archives Outlook ont été lues lors des compléments. Une archive Google Takeout contient une messagerie et un manifeste indiquant un export le 28 octobre à 12 h 42 min 33 s, heure de Paris. **La présence de fichiers issus d’exports est établie ; leur production sur OP-01 ne l’est pas.** Ils peuvent avoir été créés ailleurs puis copiés sur cet ordinateur. Ni la machine ayant demandé l’export ni son demandeur ne sont identifiés.

**Dix mises à la corbeille sont enregistrées le 28 octobre**, entre 11 h 02 et 15 h 24 : deux raccourcis, un document de gestion de mots de passe, une archive de téléchargement, cinq fichiers du dossier d’états de Ciel et `L16B/test.pdf`. Les cinq fichiers Ciel ne doivent pas être présentés comme une base comptable détruite.

L’archive récupérée contient **94 fichiers**. Parmi eux, **93 sont identiques aux fichiers conservés dans `L16B/GDRIVE`**. Le document de gestion de mots de passe, absent de ce dossier actuel, subsiste à la fois dans l’archive récupérée et séparément dans la corbeille. Aucune consultation ou utilisation des identifiants n’est démontrée ; aucune valeur confidentielle n’est reproduite ici.

Le PDF récupéré `test.pdf` contient deux factures. Ses informations internes indiquent une impression PDF à **15 h 19 min 42 s**, suivie d’une mise à la corbeille à **15 h 24 min 17 s**, sans auteur identifié. **Le contrôle du 9 novembre retrouve le même texte de ces deux factures aux pages 254 et 255 de `L16B/SAGE/sage.pdf`**, après suppression des espaces du texte extrait. Leur contenu textuel subsiste donc dans L16B ; ce résultat ne démontre ni identité binaire des PDF ni motif de la suppression.

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

### Complément du 19 octobre : après la restitution, appairages et contexte

Le PV précise que `C:\L16B` a été laissé sur l’ordinateur avec l’accord de la cliente à titre informatif, sans remplacer les fichiers définitivement saisis. Les **dix mises à la corbeille** sont techniquement confirmées ; la lecture du PV ne retrouve pas leur description individualisée. Cela ne permet pas de qualifier leur motif ou leur régularité. Le [tableau détaillé](investigations/20261019-retour-cliente/compte-rendu.md#4-dix-mises-à-la-corbeille--contre-lecture-directe) donne chaque chemin d’origine et chaque heure.

La relecture de **359 journaux Windows, soit 275 577 enregistrements**, ne retrouve aucun événement après **19 h 20 le 28**, ni du 16 au 27. Les 285 rendus XML non valides ont été repris pour leurs dates. Le contrôle complet de la MFT retrouve toutefois **cinq fichiers iCloud avec des dates anciennes après 19 h 20**, mais une modification de leur entrée MFT en 2026 : **ces métadonnées ne prouvent pas une activité locale du PC le soir du 28**. Les interactions PST du 29 déjà décrites sont également postérieures à la restitution déclarée.

Un enregistrement d’appairage Apple existe sur OP-01 pour un UDID **différent de TP-02**, avec création SI en juillet 2022 et création FN/modification en décembre 2023. Il ne démontre ni un branchement en octobre 2024 ni l’emploi d’un outil d’extraction. Les deux dates ne sont pas fusionnées en une date certaine de premier appairage.

Les trois identifiants Kingston restent à rapprocher de la **clé unique décrite par la cliente** ; la concordance de marque n’identifie pas un support physique. Le nom Takeout donne **12:41:05 Paris**, le manifeste **12:42:33** : ces 88 secondes sont compatibles avec des étapes d’export, sans permettre de calibrer l’horloge Windows.

## 5. Résultats concernant les téléphones

La sauvegarde examinée est rattachée à **TP-02 par son numéro de série**. Elle contient des traces datées concernant les appels, les messages, les photographies, le Wi-Fi et les applications. **Ces dates ne prouvent pas que le téléphone physique a été manipulé aux heures indiquées** : certaines données peuvent avoir été synchronisées avec d’autres appareils ou restaurées ultérieurement.

Le **17 octobre**, des traitements internes vers 17 h 15–17 h 18 précèdent une association Wi-Fi à `ASUS_Z01RD` vers 17 h 25. Cet enchaînement est compatible avec un système iPhone actif, y compris automatiquement, sans démontrer un déverrouillage ni une consultation humaine.

La sauvegarde contient **53 enregistrements d’appels datés du 15 au 26 octobre 2024**, pendant la privation d’accès déclarée. Ces données ne permettent pas d’affirmer que ces appels ont été passés ou reçus sur ce téléphone physique pendant cette période, ni d’identifier une personne à l’origine des opérations.

Le **28 octobre**, les éléments les plus utiles sont des états « lu » de SMS, des associations Wi-Fi à 12 h 31 et 14 h 32, une séquence compatible avec une capture d’écran vers 13 h 36 et des traitements de Photos vers 17 h 31–17 h 32. Les états « lu » peuvent avoir été transmis depuis un autre appareil ou restaurés : ils ne démontrent pas une lecture locale des SMS. L’image de la capture manque ; aucun auteur ni extraction par un tiers n’est identifié.

À **17 h 39**, LSC Smart Connect conserve des ressources compatibles avec le chargement ou l’actualisation d’un panneau caméra. **Aucun visionnage de vidéo n’est démontré.** Les catalogues examinés ne contiennent aucune référence de média du 15 au 28 octobre et ne constituent pas un historique complet des accès. Xiaomi Home fournit surtout des configurations permettant des rapprochements avec des équipements réseau.

Le nom `ASUS_Z01RD` apparaît aussi dans des traces d’OP-01, probablement parmi des réseaux Wi-Fi disponibles. Ces traces ne sont pas datées et ne prouvent ni une connexion du PC à ce réseau, ni sa présence au même endroit que TP-02, ni l’émission de ce réseau par OP-01.

### Complément du 19 octobre : scellés, BSSID et traces du soir

**La correspondance TP-02/TP-03 avec les scellés n° 3/n° 4 reste indéterminée.** Les deux sont des iPhone 13 mini rouges ; la sauvegarde identifie TP-02 par sa série, mais le mail ne donne pas les séries des scellés. TP-01 est vert dans l’attestation et l’iPhone 13 du scellé n° 2 est décrit noir : rapprochement candidat, divergence non résolue. OP-01 correspond au modèle du scellé n° 1.

Deux BSSID ASUS_Z01RD sont conservés avec des associations du **28 octobre**, **22:B0:A5:94:1F:AF** et **32:0D:CA:FD:68:8C**. Ils ne certifient pas le point d’accès utilisé le **17**. Aucun propriétaire identifié ; synchronisation/restauration toujours non exclues. L’absence connue d’ASUS dans l’entourage est une déclaration, pas une identification de l’émetteur.

Des dates existent **après 19 h 20 le 28** : appel à **19:39:46**, champ `LinkDownTimestamp` ASUS à **19:40:02**, caches LSC vers **22:35 et 23:26**. Elles sont postérieures à la restitution déclarée, sans auteur établi et sans preuve de visionnage des caméras. Le tri ciblé du manifeste et la relecture de 25 plist de gestion/comptes ne révèlent pas de session d’extraction d’octobre 2024 ni d’historique complet des appareils associés depuis 2021.

La cliente rapporte un allumage des téléphones vers 13 h 30 le 15. Une image du salon à 13:30:21 ne suffit pas à prouver ce geste. La date du branchement de l’appareil d’extraction demeure « le 15 / le 28 ». Le point concernant TP-03 reste « à compléter ». Ces éléments sont conservés comme déclarations et questions ouvertes.

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

Une conversion horaire peut expliquer comment une date du début de janvier 2000 s’affiche au 31 décembre 1999, sans expliquer pourquoi cette date a été enregistrée. L’affichage observé par la cliente reste inconnu. Le nouveau mail précise désormais **février 2024 et la caméra de la chambre** ; l’interface et le fichier à l’origine de l’affichage restent non établis.

**Une réinitialisation en février ou le 15 octobre n’a pas été démontrée. Aucun formatage intentionnel ni effacement malveillant n’a été établi.** Les fichiers auxiliaires Windows datés du 12 novembre documentent séparément un traitement possible des cartes sur ordinateur ; ils ne démontrent pas une modification des vidéos. Le poste concerné n’a pas été identifié, y compris après les recherches complémentaires sur OP-01.

### Complément du 19 octobre : installation en 2023 et terrasse en continu

La cliente situe l’installation après mars 2023. Les noms vidéo conservés de la chambre commencent en décembre 2023, ceux du salon en novembre 2023 ; ils ne couvrent pas continûment cette période. La terrasse conserve principalement novembre 2024 et un clip daté du 21 octobre par ses images. Les données LSC ne restituent pas une chronologie complète des partages, réappairages ou changements de compte.

La terrasse est déclarée fonctionner **24 h/24**. Le nouveau calcul de l’union des intervalles des MP4 actifs à nom datable couvre **48,892 à 64,937 %** d’une journée sur les journées intérieures du **6 au 11 novembre**. Ce sont des lacunes du **corpus conservé**, pas une mesure certaine du temps d’arrêt de la caméra. Le calcul exclut les supprimés récupérés et le temporaire ; les durées restent nominales. Les mécanismes d’enregistrement, pertes, écrasements, interruptions ou suppressions restent à départager. La réutilisation circulaire des anciennes données est distincte d’une coupure du flux. **Aucun effacement ciblé le 15 ni intervention d’une personne sur la terrasse n’est démontré.**

## 8. Éléments inexpliqués et limites des conclusions

- **Auteur inconnu :** aucun compte, nom d’appareil ou horaire ne permet d’identifier la personne ayant effectué les opérations.
- **Historiques incomplets :** les traces conservées ne recensent pas tous les accès distants ni toutes les opérations anciennes. Des enregistrements ont pu être remplacés, particulièrement sur la terrasse.
- **Horloges non comparées à une référence commune :** une proximité entre heure caméra, heure informatique et heure déclarée ne prouve pas un événement simultané.
- **Signalements de réinitialisation non authentifiés :** l’interface, le message et les fichiers à l’origine des deux observations de la cliente restent inconnus.
- **Pièces absentes :** le CD d’inventaire est confirmé indisponible le 8 novembre. Le PV consulté décrit une copie vers une clé USB et l’authentification des fichiers, mais ne fournit pas leur inventaire détaillé ni leurs empreintes. Le journal de sauvegarde Mac manque pour préciser la provenance des données anciennes de TP-02 ; TP-01 et TP-03 n’ont pas été analysés.

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

1. Le PV précise désormais les horaires et décrit les copies. Il ne permet pas d’identifier les deux Mini par numéro de série ou IMEI. Les divergences relatives à l’apparence des scellés restent des positions documentaires contradictoires, sans résolution technique.
2. Le CD d’inventaire est indisponible. Les noms `Archive_saddedine.zip`, `Inventaire_saddedine.csv` et `Rejets_saddedine.txt`, ainsi que les identifiants Kingston, ne sont pas donnés par le PV. Le rapprochement exact avec les fichiers finalement saisis reste impossible en l’état.
3. Les images échantillonnées du salon ne démontrent ni allumage ni déverrouillage d’un téléphone. La transcription automatique n’a fourni aucun segment exploitable ; aucune conclusion sur l’absence de paroles n’en est tirée.
4. Les résultats SIFT ont été récupérés et contrôlés le 9 novembre. Cinq messages du dossier Envoyés du PST dmm portent le cabinet Negrevergne comme destinataire ; une pièce jointe reproduit un échange avec Pascoët, une proposition de services nomme Rachel Dress et une notification est au nom de Liwer. Les occurrences Meyer comprennent des mentions du représentant adverse et une homonymie sans lien établi. La lecture thématique des PDF Mini révèle également des échanges avec Me Isabelle Guillou dans `Rép  Dossier bourarach.pdf`, hors des noms recherchés initialement. Cela justifie un contrôle du filtrage annoncé, sans établir leur inclusion dans le jeu définitivement saisi. Le déchiffrement a finalement réussi : les **27 PDF de L16B/IPHONE13_MINI ont tous un équivalent binaire identique dans la sauvegarde TP-02**, après comparaison SHA-256. Ce contenu commun étaye le rapprochement avec TP-02, sans prouver une provenance physique exclusive, le sens ou la date du transfert. Voir la reprise du 9 novembre.

## 10. Conclusion générale

**Faits établis :** des traces d’activité d’OP-01 les 15 et 28 octobre, des opérations identifiées sur des fichiers le 28, des références à des supports externes, des traces datées dans la sauvegarde TP-02, des vidéos supprimées récupérées et des anomalies techniques récurrentes des enregistrements. La dernière vidéo conservée du salon et la lacune qui la suit sont précisément documentées, sans cause certaine.

**Faits non établis :** une intrusion non autorisée, l’identité de la personne responsable des opérations, une réinitialisation volontaire, un formatage intentionnel ou une suppression malveillante. Le PV consigne une copie sur une clé de l’administration et l’authentification des fichiers ; les traces techniques disponibles ne permettent pas d’en vérifier le contenu exact, les empreintes ou le rattachement à l’un des trois identifiants Kingston. Aucun accès distant non autorisé ni intention malveillante ne sont établis par ce rapprochement.

## Documents techniques de référence

- [Compte rendu général et compléments du 17 octobre 2026](investigations/20261017-recroisements/compte-rendu.md).
- [Ordinateur OP-01](ordinateur/analyse-ordinateur.md), [opérations du 28 octobre](ordinateur/recherche-OP-01/operations-28oct/compte-rendu.md) et [limites de datation du réseau ASUS_Z01RD](ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/datation.md).
- [Téléphone TP-02](telephones/analyse-TP-02.md) et [Freebox](freebox/analyse-freebox.md).
- [SD-01 — chambre](cartes_sd/analyse-cartes_sd-SD-01.md), [SD-02 — terrasse](cartes_sd/analyse-cartes_sd-SD-02.md), [SD-03 — salon](cartes_sd/analyse-cartes_sd-SD-03.md) et [comparaison des trois cartes](cartes_sd/analyse-cartes_sd-transversale.md).
- Sources de cadrage : [demandes de Mme Sadedine](docs/mail.txt) et [attestation de remise](remise-documents/attestation-de-remise.md).

- [Complément du 19 octobre 2026 — retour de la cliente, contre-lectures et réponses détaillées](investigations/20261019-retour-cliente/compte-rendu.md).

- [Lecture du PV du 8 novembre 2026](investigations/20261108-analyse-pv/compte-rendu.md) et [complément technique en cours](investigations/20261108-complement-pv/compte-rendu.md).

- [Reprise SIFT du 9 novembre — correspondances et conservation des deux factures](investigations/20261108-complement-pv/reprise-20261109.md).
