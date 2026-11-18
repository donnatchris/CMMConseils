# Rapport final d’investigation informatique — Mme Malika Sadedine

**Référence :** SADEDINE-2026  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Destinataire :** Me Delphine Ravon, avocate de Mme Malika Sadedine  
**Rapport initial :** 19 octobre 2026<br>
**Analyses prises en compte :** septembre–17 novembre 2026 ; dates propres à chaque contrôle dans les rapports de référence<br>
**Révision documentaire :** 18 novembre 2026, sans nouvelle acquisition ni nouvelle expertise des supports<br>
**Nature :** investigation informatique indépendante réalisée à la demande de la cliente, sans désignation comme expert judiciaire.

## 1. Points utilisables pour préparer la contestation

J’ai examiné les images, sauvegardes et résultats techniques disponibles, puis comparé les contenus à l’inventaire fourni. Les sept points suivants indiquent ce qui est établi, l’explication que je retiens, sa limite et la pièce utile pour avancer. L’appréciation du périmètre autorisé et des conséquences procédurales relève de l’avocate.

### 1.1. Correspondances avec des avocats

**Constat et intérêt.** J’ai retrouvé **21 messages** identifiant un avocat ou son cabinet dans les en-têtes du PST DMM : neuf Fakiroff/Roosevelt, sept Wahrheit, cinq Negrevergne. Le fichier qui les contient correspond à l’**empreinte numérique permettant de comparer les contenus** inscrite dans l’inventaire fourni. Le PDF Guillou/Bourarach y concorde aussi individuellement. Ce résultat permet de confronter des éléments précis au filtrage annoncé au PV.

**Explication retenue et limite.** Je retiens leur présence dans les contenus décrits par cet inventaire. Les citations Pascoët/Rubio et les notifications Dress/Liwer restent distinctes des échanges directs. Les deux messages Khallouki et trois transferts du PST 93300 proviennent d’un fichier divergent : leur présence dans la version inventoriée n’est pas certifiée. Ni la lecture par les agents ni la qualification de chaque correspondance ne s’en déduisent.

**Pour avancer.** Obtenir l’archive finale, les rejets et le support d’inventaire. Le [rapport correspondances, tableaux 1 et 2](ordinateur/recherche-OP-01/correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md) et la [fiche Bourarach](investigations/20261109-clarification-correspondances/fiche-bourarach.md) donnent les références individuelles.

### 1.2. Inventaire et intégrité des fichiers

**Constat et intérêt.** J’ai retrouvé les **1 555 chemins** attendus et calculé l’empreinte SHA-512 de chaque fichier : **1 552 contenus concordent, trois divergent**, sans erreur de lecture signalée. Les différences concernent le raccourci USB2, `FACT 2018 SUITE.pdf` et le PST 93300. Le contrôle distingue ainsi un nom présent d’un contenu identique.

**Explication retenue et limite.** Les concordances établissent l’identité des octets comparés au CSV. Pour les écarts, version différente, modification entre deux contrôles ou erreur dans l’inventaire restent à départager : les données ne permettent pas de classer leurs causes. Le dossier local L16B ne devient pas une copie certifiée de l’archive finale.

**Pour avancer.** Comparer les trois versions inventoriées, le CSV sur son support d’origine et l’archive finale. La [synthèse, section 3](ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/rapport-comparaison-L16B-inventaire.md#3-fichiers-inventoriés-présents-au-chemin-attendu-mais-de-contenu-divergent) et son annexe exhaustive conservent chemins, empreintes et résultats.

### 1.3. Documents ALMU et accès Sage

**Constat et intérêt.** Après ouverture du PC le 28 octobre, les traces étayent un accès de Sage à ses services distants puis la génération d’un PDF de **458 pages, toutes émises par ALMU**. Les 85 dénominations destinataires et 86 codes clients ne sont pas autant de sociétés émettrices. Ces documents justifient d’examiner leur rapport au périmètre autorisé.

**Explication retenue et limite.** Je retiens une sortie effective de factures ALMU, corroborée par le journal d’impression et le contenu. La réponse réussie du serveur ne prouve pas la frappe d’un mot de passe ; la génération PDF ne prouve pas une impression papier ou le transfert externe de ce fichier précis. L’appréciation du périmètre appartient à l’avocate.

**Pour avancer.** Rapprocher ordonnance, archive finale et journaux de collecte. Les [compléments Sage](ordinateur/rapport-complementaire-OP-01-Sage50-reseaux-28oct2024.md), [Samsung/ALMU](ordinateur/rapport-complementaire-OP-01-Samsung-ALMU-28oct2024.md) et l’[inventaire des pages](inventaire-DNEF/rapports/rapport-repartition-sage-458-pages.md) documentent les contrôles.

### 1.4. TP-02 : séquence Wi-Fi pendant la conservation

**Constat et intérêt.** La sauvegarde de TP-02 conserve le 17 octobre, vers 17 h 25, une préparation de connexion, un ajout du réseau ASUS par les réglages, puis une association en moins de cinq secondes. C’est l’indice technique le plus discriminant d’une activité possible pendant la conservation.

**Explication retenue et limite.** Je privilégie une configuration suivie d’une connexion locale : la chaîne est plus complète que les profils de simple synchronisation de mot de passe comparés. Un import ultérieur de l’historique reste possible ; aucune restauration postérieure au 17 expliquant cette chaîne n’a été identifiée. Il manque une preuve indépendante de l’activité physique et du premier déverrouillage. Aucun opérateur n’est identifié par le nom du réseau.

**Pour avancer.** Rechercher sauvegarde contemporaine, historique de restauration et journal du point d’accès. Le [rapport TP-02, section 6](telephones/analyse-TP-02.md#6-wi-fi-asus_z01rd-chaîne-conservée-et-limites-dattribution) compare les scénarios et fournit les pièces.

### 1.5. Parcours des PDF associés à TP-03

**Constat et intérêt.** Les **27 fichiers PDF inventoriés représentent vingt contenus**, retrouvés dans les deux Mini. Pour dix-sept contenus, TP-03 conserve une date de dernière utilisation le 15 octobre entre 13 h 41 et 13 h 50, proche de celle du CSV ; seize ont aussi un changement de statut rapproché. L’arrivée des 27 fichiers au dossier final du PC est, elle, datée du 28 octobre.

**Explication retenue et limite.** Ces rapprochements répétés favorisent l’historique de données conservé dans TP-03. Un historique peut suivre une copie, une sauvegarde ou une restauration vers un autre appareil. Les attributs ne prouvent ni ouverture des documents, ni création ou extraction le 15, ni transfert direct depuis le téléphone physique.

**Pour avancer.** Obtenir les journaux et paramètres de collecte, une sauvegarde contemporaine et l’archive finale. [Q1](inventaire-DNEF/rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md) distingue les dates ; [B–E](inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md) examine déverrouillage, arrivée des PDF et doublons.

### 1.6. Conservation et déroulement des opérations

**Constat et intérêt.** La note de visionnage consigne l’apparition de logos Apple avant scellement. Les PV décrivent un iPhone noir, tandis que TP-01 est indiqué vert à la remise ; les deux Mini rouges ne sont pas départagés par leurs séries. Le 28 après ouverture, Windows conserve trois identifiants Kingston et dix mises à la corbeille.

**Explication retenue et limite.** Les logos sont caractéristiques d’un démarrage, sans démontrer une extinction ultérieure ni un maintien allumé pendant toute la conservation. Les conditions de garde et identités attribuées par la cliente restent des déclarations à confronter aux pièces. Trois identifiants USB ne prouvent pas trois copies ; les deux factures supprimées subsistent textuellement dans Sage. Je retiens des questions documentaires et des opérations à expliquer, sans irrégularité acquise.

**Pour avancer.** Obtenir photographies et mouvements des scellés, séries/IMEI, état d’alimentation et isolement réseau, identification des supports et notes d’opérations. Les [notes de constatation](NOTE-DE-CONSTATION-téléphones.md), [TP-01](NOTE-DE-CONSTATATION-TP-01.md) et [OP-01, sections 7–8](ordinateur/analyse-ordinateur.md) donnent les éléments.

### 1.7. Vidéo du salon

**Constat et intérêt.** Le dernier clip du 15 octobre présente une erreur vidéo intermédiaire, une piste audio plus longue de **11,589 secondes** et des dates incohérentes. Aucun fichier n’est nommé du 16 au 28 ; le suivant est daté du 29 octobre. Il existe donc une anomalie réelle et une lacune à expliquer.

**Explication retenue et limite.** Je privilégie un défaut de finalisation ou de reconstruction pour la signature de compteur : elle se répète dans onze clips sur deux cartes dès 2023. Une falsification n’est pas démontrée. Ce défaut n’explique pas toute la lacune ; arrêt, réglages, alimentation ou perte de fichiers ne sont pas départagés. La dernière image n’est pas une heure certaine d’arrêt de la caméra.

**Pour avancer.** Rechercher anciennes copies, réglages et journaux caméra, puis reproduire le défaut sur témoin si possible. Le [rapport SD-03, sections 7–9](cartes_sd/analyse-cartes_sd-SD-03.md) et l’[analyse transversale](cartes_sd/analyse-cartes_sd-transversale.md) distinguent les mesures, les scénarios et leurs limites.

## 2. Comprendre la mission et les appareils

### Ce qui a été recherché

Mme Sadedine a demandé de rechercher des utilisations, accès, copies, transferts ou suppressions sur ses équipements, notamment autour de la perquisition fiscale du **15 octobre 2024** et de la conservation des matériels jusqu’au **28 octobre**. Les recherches concernent aussi le réseau, les caméras et les réinitialisations signalées. Les historiques anciens demandés depuis 2021/2022 ne sont que partiellement disponibles.

| Repère | Équipement analysé |
|---|---|
| **OP-01** | Ordinateur portable ASUS |
| **TP-01** | iPhone 13 vert, étudié à partir de sa sauvegarde |
| **TP-02** | iPhone 13 mini rouge, série F5466LV9V7 |
| **TP-03** | Autre iPhone 13 mini rouge, série Y4Q9KGHG26 |
| **SD-01 / SD-02 / SD-03** | Cartes des caméras de la chambre / terrasse / salon |
| **Freebox** | Équipement fournissant les traces du réseau domestique |

Ces repères identifient les supports de la mission ; ils ne valent pas numéros de scellés. La correspondance des deux Mini avec les scellés n° 3/n° 4 reste indéterminée. Une divergence de couleur subsiste entre TP-01, vert dans l’attestation, et l’iPhone du scellé n° 2, décrit noir.

### Comment lire les résultats

Le rapport distingue **les constats techniques**, issus des données examinées, **les constats de visionnage du prestataire**, **les mentions du procès-verbal (PV)** et **les déclarations de la cliente**. Une hypothèse est une explication compatible avec ces éléments, qui reste à vérifier.

Une sauvegarde est une copie de données du téléphone, parfois réalisée longtemps après les faits. Elle peut contenir des informations venues d’un autre appareil ou d’un service en ligne. Une date présente dans cette copie ne prouve donc pas toujours une opération sur le téléphone physique à cet instant. De même, un nom de compte ou de réseau n’identifie pas une personne.

Les résultats techniques conservent leurs dates propres : acquisitions et sauvegardes entre 2025 et 2026 selon les supports, analyses jusqu’au 17 novembre 2026. La révision du 18 novembre organise leur présentation, sans nouvelle acquisition ni expérience sur les supports. Les annexes fournissent les localisateurs et les limites des contrôles.

## 3. Les dates essentielles

Les heures informatiques sont présentées en heure de Paris. Les heures affichées par les caméras n’ont pas été comparées à une référence commune : leur rapprochement avec les autres horaires reste prudent.

| Phase | Repères de Paris et provenance | Sens |
|---|---|---|
| **15 octobre 2024 — opérations et placement sous scellés** | OP-01 reprend vers 10:43 puis hiberne vers 10:53 (Windows). Logos Apple à 13:25:19 selon l’horloge vidéo ; perte d’accès aux téléphones vers 13:30 selon la cliente. Mise sous scellés après 14:19 (PV). | Les heures vidéo ne sont pas étalonnées ; aucune heure individuelle de fermeture n’est fournie. Les métadonnées PDF 13:41–13:50 ne prouvent pas une extraction. |
| **Conservation avant ouverture** | OP-01 : aucune reprise Windows intermédiaire corroborée. TP-03 : traitements internes du 16 vers 05:31. TP-02 : traitements et Wi-Fi du 17 vers 17:15–17:25, plus historique d’appels du 15 au 26. | Distinguer fonctionnement local, traitement automatique et historique copié ; aucun auteur certain. |
| **28 octobre 2024 — après ouverture** | Arrivée 10:22, ouverture PC 10:41 et téléphones 11:30 (PV). Samsung reconnu 11:18 ; Sage lancé 15:10, PDF ALMU 458 pages 15:28 ; PDF Mini regroupés 17:13 ; références Kingston 17:26–17:27. Clôture 19:20 ; récupération vers 19:20 déclarée. | Les opérations après ouverture ne prouvent pas une manipulation sous scellé fermé. Les références externes ne donnent pas le contenu de l’archive. |

La chronologie complète, incluant les traitements système et les événements après restitution, figure en annexe A.

## 4. Les appareils pendant la fermeture des scellés

**Une intervention humaine reste possible, surtout au regard des données de TP-02, mais elle n’est démontrée sur aucun appareil physique identifié pendant la fermeture de son scellé.** Un fonctionnement automatique, une intervention humaine et une ouverture matérielle d’emballage sont des faits différents.

### TP-02 : deux pistes à départager

Le réseau `ASUS_Z01RD` apparaît dans une séquence du 17 octobre qui associe ajout du réseau, indication de connexion par utilisateur, création d’une adresse réseau puis connexion. Cet ensemble est plus informatif qu’une date isolée. Il reste compatible avec une configuration par une personne, sans preuve de déverrouillage du téléphone. Les données peuvent aussi provenir d’un état complet importé lors d’une migration ou restauration ; cette explication n’est ni établie ni exclue.

Les 53 appels conservés comprennent 22 sortants, dont 19 à durée positive. Ils sont répartis sur plusieurs jours, à partir du 15 octobre en soirée. Un historique de communications peut toutefois circuler entre appareils : les données disponibles n’identifient pas le matériel ayant émis les appels. Une vérification auprès de l’opérateur ne serait discriminante que si elle permet aussi le rapprochement avec le téléphone physique.

Le nom ASUS ne prouve pas que le réseau était émis par l’ordinateur OP-01, ni que celui-ci se trouvait auprès de TP-02. Les adresses du point d’accès conservées concernent le 28 octobre et n’identifient pas avec certitude celui utilisé le 17.

### Ce que change le démarrage constaté dans la vidéo

Le démarrage constaté avant leur scellement est compatible avec la poursuite de tâches internes si les téléphones sont restés allumés. Le diagnostic du 28 octobre mesure un temps d’éveil depuis un démarrage ; il ne permet pas de calculer une heure certaine d’allumage, ni d’attester une extinction préalable.

Cette possibilité rend compréhensibles des traitements automatiques pendant la conservation. Elle ne suffit pas à expliquer l’origine des appels et de la configuration Wi-Fi, ni à démontrer une manipulation après fermeture. Aucune pièce citée ne certifie l’état d’alimentation lors de chaque scellement ou son maintien jusqu’à la restitution.

### Les autres traces ne caractérisent pas un geste humain

Sur **TP-03**, des traitements système du 16 octobre concernent notamment des données Santé et des conseils internes de l’application Messages. Les contrôles détaillés ne retrouvent ni SMS lu ou envoyé, ni déverrouillage, ni déplacement le 16. Le même profil de traitement existe à d’autres dates. Une explication automatique est compatible ; elle n’est pas une preuve générale d’absence d’intervention.

Sur **TP-01**, les messages et métadonnées datés pendant la conservation ne prouvent pas un usage local. Certains messages sont compatibles avec une récupération différée le 28 ; les dates de services en ligne peuvent provenir d’ailleurs. Les historiques incomplets empêchent de certifier une inactivité.

Sur **OP-01**, aucune activité Windows n’est corroborée entre la veille du 15 et la reprise du 28. L’heure de réveil du 16 précédemment relevée est une échéance programmée, pas un réveil constaté. Ce résultat n’exclut pas une manipulation qui n’aurait laissé aucune trace disponible.

## 5. Après ouverture : opérations et données copiées

**Le PV décrit une extraction et une copie par l’administration. L’incertitude porte sur les fichiers finalement retenus, leur support et certaines opérations effectuées pendant la séance.** Les traces montrent une activité après ouverture ; elles ne doivent pas être utilisées comme preuve d’intervention pendant la fermeture.

### Du regroupement sur le PC à la copie finale

Le dossier **L16B** rassemble des documents locaux, des données Google Drive et iCloud, des messageries, des documents comptables et bancaires ainsi que des données de téléphones. Les créations de fichiers concentrées le 28 octobre et les comparaisons de contenu corroborent fortement un regroupement pendant les opérations.

Le PV décrit ensuite une sélection, l’exclusion de données personnelles et de correspondances d’avocats, puis une copie sur une clé de l’administration, une authentification des fichiers et deux CD d’inventaire. Il précise que L16B est laissé sur le PC à titre informatif. **Ce dossier de travail ne constitue donc pas une image certifiée de la copie emportée.**

Le CD reste indisponible, mais un **CSV d’inventaire a été fourni et ses 1 555 lignes ont désormais toutes été contrôlées** contre L16B dans l’image. **Aucun chemin ne manque ; 1 552 SHA-512 concordent et 3 divergent** : le raccourci USB2, `FACT 2018 SUITE.pdf` et le PST 93300. Les 27 PDF Mini, le PST DMM et Takeout font partie des concordances. Le point 1.1 précise la portée pour les correspondances d’avocats ; le **point 1.2** décrit le contrôle complet et renvoie au [rapport Markdown des 1 555 comparaisons](ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/rapport-comparaison-SHA512-exhaustive-1555-fichiers.md). L’authentification du support d’origine et le contrôle matériel de l’archive finale et de sa conservation restent distincts ; L16B ne devient pas pour autant une copie certifiée du jeu final.

### Le Samsung et l’accès Internet d’OP-01 le 28 octobre

À **11 h 18 min 34 s**, Windows reconnaît un Samsung de série **`R58RB2ETQER`**, enregistré sous le nom **« XCover 5 de David »**. Les identifiants USB sont **VID `04E8`**, PID **`6860`**, puis **`6863`** en mode de partage réseau. Windows configure un pilote **« Remote NDIS based Internet Sharing Device »**, permettant de fournir une interface réseau par USB.

Le profil **« Réseau 2 »** dispose d’Internet dès **11 h 18 min 56 s**, se déconnecte vers **11 h 35**, puis **« Réseau 3 »** dispose d’Internet à partir de **11 h 47 min 32 s**. Une brève interruption est suivie d’une reconnexion à **16 h 27 min 53 s**. Le retrait du Samsung à **17 h 14 min 11,399 s** précède d’environ **0,19 seconde** la déconnexion de « Réseau 3 ». Cette séquence **étaye fortement un partage Internet par le Samsung**. La catégorie « Ethernet » de Windows inclut ce type d’interface USB ; elle ne prouve pas un câble réseau branché dans les locaux.

Aucun usage antérieur du numéro exact n’a été retrouvé dans les journaux conservés. Cela n’établit pas sa première connexion absolue : d’anciennes traces peuvent manquer et les instances du périphérique ont été supprimées lors d’un nettoyage Windows en décembre 2024. Le libellé « XCover 5 de David » ne certifie pas son propriétaire. La correspondance persistante directe de chaque interface opérationnelle avec la série USB, le réseau amont et l’IP publique ne sont pas établis. **Aucune connexion Wi-Fi à `ASUS_Z01RD` n’est démontrée sur OP-01 le 28.**

### Sage 50 : authentification et sorties de documents ALMU

**Sage 50 est lancé vers 15 h 10** et contacte ses serveurs. Son journal natif enregistre un échange avec le service de souscription, puis une requête **`id.sage.com/oauth/token` à 15 h 11 min 48 s**, résultat **200 à 15 h 11 min 49 s**, suivie d’un accès au service de données hébergées avec résultat 200. **Un échange de jeton abouti et un accès au service sont fortement étayés**, sans preuve de saisie manuelle d’un mot de passe, d’une nouvelle activation de licence ou de l’identité de l’utilisateur. Cette séquence se déroule pendant la connexion « Réseau 3 ».

**Seul le dossier SAS ALMU, SIRET 81816735500010, est confirmé comme utilisé le 28.** Les trois alias ALMU modifiés ce jour-là désignent le même dossier. La présence de cinq autres stockages société ou d’un modèle d’impression nommé DMM CONSEILS ne suffit pas à prouver leur ouverture. Les contrôles supplémentaires du composant web de Sage retrouvent des bases de mots de passe vides et un historique de Gestion Commerciale limité à 2026 : ils ne permettent pas de déterminer si une saisie ou un accès mémorisé a servi à l’authentification de 2024. La liste exhaustive des ouvertures et le mode de connexion restent non établis.

Des sorties PDF sont ensuite attestées par le journal d’impression et par leurs contenus : **FA0338 à 15 h 18 min 42 s**, puis **FA0338 et FA0339 dans `C:\L16B\test.pdf` à 15 h 19 min 42 s**, enfin **458 pages ALMU à 15 h 28 min 33 s**, retrouvées dans **`C:\L16B\SAGE\sage.pdf`**. Un premier travail d’une page à 15 h 16 et un travail de 205 pages à 15 h 23 sont également consignés, mais leurs contenus exacts n’ont pas été retrouvés séparément. Les états se recouvrent : leurs nombres de pages ne doivent pas être additionnés comme des documents distincts.

Les **pages 1 à 458 portent toutes le SIRET ALMU 81816735500010**. Les autres sociétés mentionnées comme clientes ne sont pas d’autres sociétés émettrices identifiées dans le PDF, et leur présence ne démontre pas l’ouverture de leurs dossiers Sage. La copie récupérée et les résultats détaillés sont accessibles depuis le [rapport ordinateur, section 7.3](ordinateur/analyse-ordinateur.md#73-google-takeout-drive-sage-et-shine).

**Il s’agit de sorties effectives au format PDF, au-delà des seules modifications de fichiers de configuration ou d’impression.** Elles ne démontrent ni impression papier, ni copie intégrale de la base Sage, ni transfert de ce PDF précis sur la clé de l’administration. À **17 h 04 min 50 s**, Sage reçoit encore un résultat 200 ; après la déconnexion de 17 h 14, ses tentatives de fin de session échouent en résolution du serveur à **17 h 28 min 57 s**, au moment où Windows consigne aussi une défaillance du logiciel. Les références précises et les contrôles des fichiers figurent en annexe B.1.

### Les correspondances avec des avocats

**Le contrôle SHA-512 du 16 novembre établit la présence de 21 messages dans le PST DMM correspondant à l’empreinte de l’inventaire** : Fakiroff / Roosevelt Avocats (9), Wahrheit (7), Negrevergne (5). Les citations Pascoët / Rubio et les notifications Dress / Liwer proviennent également de conteneurs concordants. Les 2 messages Khallouki et 3 transferts proviennent du PST 93300 divergent et ne sont pas certifiés dans la version inventoriée. Le [rapport détaillé](ordinateur/recherche-OP-01/correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md) donne les deux tableaux et les empreintes.

Les échanges identifiés sont conservés dans des archives de messagerie et des PDF. Il ne s’agit pas seulement de noms repérés : certains documents reproduisent effectivement des correspondances. Ils concernent plusieurs dossiers et parties ; tous ne sont pas nécessairement des consultations confidentielles de Mme Sadedine.

Le PDF reproduisant des échanges avec Me Isabelle Guillou concerne un recours de 2017 relatif à un tiers. Ses dates soutiennent un regroupement local le 28 octobre. Les traces d’interaction du 29 sont postérieures à la restitution déclarée et ne prouvent pas une lecture par un agent pendant les opérations.

Les 27 PDF du dossier Mini ont des contenus identiques retrouvés dans **les deux sauvegardes TP-02 et TP-03** et figurent désormais dans le **CSV d’inventaire fourni**, avec les mêmes SHA-512. Les 17 rapprochements temporels favorisent l’historique conservé dans TP-03, sans identifier un transfert direct ou un opérateur. **Le PDF Bourarach est donc identifié individuellement dans cet inventaire** ; l’archive finale et son utilisation restent à contrôler. Les courriers déjà adressés à l’administration, propositions de services ou mentions du conseil adverse doivent toujours être distingués d’un échange confidentiel avocat-client.

Le contrôle doit porter sur les documents effectivement emportés, leur qualification et leur éventuelle utilisation fiscale. Le cadre juridique et les références déjà cités sont conservés en annexe B.1 ; le rapport technique ne conclut pas à la régularité ou à l’irrégularité globale de la saisie.

### Les supports USB et les suppressions

Les trois identifiants Kingston distinguent plusieurs périphériques dans les traces Windows. Des références à une archive, un inventaire et une liste de rejets apparaissent sur un volume Kingston vers 17 h 26–17 h 27. **Le CSV a été transmis séparément ; il n’est pas présenté comme une récupération depuis OP-01.** Le contenu du ZIP et du TXT n’a pas été récupéré et ce volume n’est pas rattaché à l’un des trois identifiants. Les traces seules ne permettent donc pas de désigner le support final ou de compter les copies.

Les dix mises à la corbeille concernent notamment des raccourcis, un document de mots de passe, une archive de téléchargement, des fichiers d’états Ciel et un PDF de deux factures. Les contenus ont été récupérés ; les factures subsistent également sous forme de texte dans le PDF Sage. Une destruction de base comptable ou une utilisation des mots de passe n’est pas démontrée. Le motif des suppressions et leur effet sur les sources restent à expliquer.

### Les opérations sur les téléphones

Après l’ouverture à 11 h 30, TP-02 conserve trois SMS marqués lus entre **12 h 03 et 12 h 46** : un code de réinitialisation Microsoft et deux codes de validation Google. **Mme Sadedine confirme avoir effectué elle-même cette réinitialisation et ces validations, car elle n’arrivait pas à se connecter pour l’administration** ([courriel, point 3](docs/mail-3.txt)). Les horodatages restent des constats de base de données ; l’explication de ces démarches repose sur sa déclaration. **À sa demande, ce point ne nécessite pas d’approfondissement et n’est plus retenu comme une opération inexpliquée.**

Une séquence est compatible avec une capture d’écran vers **13 h 36**, mais l’image manque. Les données de l’application de caméra vers 17 h 39 ne prouvent aucun visionnage. TP-01 conserve deux lignes WhatsApp sortantes vers **17 h 44**, sans auteur identifié. Ces éléments appellent des explications sur les opérations réalisées ; ils ne suffisent pas à attribuer une action à une personne.

## 6. Les caméras et le réseau

### Vidéos anormales et périodes sans enregistrement

**Des anomalies et des lacunes sont établies, mais aucune falsification volontaire de vidéo n’est démontrée.** Les caméras n’ont jamais été placées sous scellés. Leur activité après la perquisition ne constitue donc pas, en elle-même, une anomalie de conservation.

Pour le **salon**, 65 vidéos du 15 octobre sont conservées. La dernière commence à 13 h 28 ; les images contrôlées portent cette date, alors que les informations du fichier indiquent janvier 2000. Le son est plus long que l’image d’environ 11,6 secondes. Cela ne prouve pas qu’il a été enregistré exactement aussi longtemps après la dernière image en temps réel. Aucun fichier référencé n’est daté du 16 au 28 ; les enregistrements reprennent le 29. Arrêt, absence de déclenchement et perte de fichiers ne peuvent pas être départagés.

Pour la **chambre**, 37 vidéos du 15 octobre sont conservées, dont certaines vont jusqu’à environ 22 h 46 selon la caméra. Aucun indice spécifique de réinitialisation ce jour-là n’a été identifié. Deux vidéos de février et mars présentent toutefois des dates incohérentes et l’une est partiellement endommagée.

Un défaut structurel identique est retrouvé dans onze vidéos de la chambre et du salon, dès novembre 2023. Cette répétition soutient un problème de production ou de finalisation, sans en établir le mécanisme exact. Une conversion horaire peut expliquer l’affichage du 31 décembre 1999 à partir d’une date de janvier 2000 ; elle n’explique pas pourquoi la date initiale a été enregistrée. Le signalement de réinitialisation de la chambre en février 2024 reste non authentifié.

**Les scénarios techniques doivent être distingués de leur déclencheur.** Un défaut logiciel lors de la clôture du fichier ou de sa récupération après interruption est l’explication la mieux étayée pour l’erreur structurelle répétée. Une coupure d’alimentation, un redémarrage avec horodatage par défaut, un problème de production ou d’écriture des données, ou un traitement ultérieur restent compatibles, sans être établis. Un défaut logiciel pourrait être déclenché par un débranchement humain : son caractère récurrent ne prouve donc pas l’absence d’intervention. Aucun élément identifié n’attribue toutefois une telle action à une personne. **Le défaut du dernier fichier et l’absence de fichiers référencés du 16 au 28 octobre sont deux constats dont le lien causal n’est pas démontré.** Les scénarios et leurs limites sont détaillés en annexe B.4.

### Vidéos récupérées et couverture réelle

Pour la **terrasse**, onze vidéos supprimées ont été récupérées entièrement et la fin d’une douzième partiellement. Elles sont datées du **5 novembre 2024**, après la période de conservation des téléphones. La carte presque pleine présente des traces compatibles avec le remplacement automatique d’anciens enregistrements ; chaque suppression n’est pas expliquée individuellement.

Aucune vidéo du 15 octobre n’a été récupérée sur cette carte. Malgré le fonctionnement continu déclaré, les fichiers conservés ne couvrent pas des journées complètes. Cela mesure la couverture du corpus disponible, pas le temps certain d’arrêt de la caméra. Aucun effacement ciblé le 15, formatage intentionnel ou réinitialisation volontaire n’est établi.

### Appareils réseau et accès éventuels

La Freebox confirme l’identité réseau d’OP-01, mais un autre ordinateur et trois identités « iPhone » relevés les 16–17 octobre restent sans attribution certaine. Aucun lien n’est établi avec une utilisation des appareils scellés. Une présence sur le réseau ne démontre ni lecture de fichiers ni consultation des caméras.

Deux tentatives d’accès au partage de fichiers d’OP-01 en mars 2024 ont échoué. Les traces anciennes de téléassistance et de mise en quarantaine d’un document ne démontrent pas une prise en main non autorisée ou une compromission réussie. Les historiques restent incomplets : aucune absence générale d’accès depuis 2021/2022 ne peut être certifiée.

## 7. Pièces complémentaires à demander

Les comparaisons au CSV sont accomplies ; les demandes ci-dessous visent à expliquer les écarts, contrôler le jeu final et rattacher les traces aux appareils. La priorité exprime leur pouvoir de clarification, sans présumer leur disponibilité ni leur détenteur exact.

| Pièce | Détenteur présumé | Question à résoudre | Priorité |
|---|---|---|---|
| `Archive_saddedine.zip` et `Rejets_saddedine.txt`, avec empreintes et conservation | Administration / support de destination décrit au PV | Quels contenus ont été retenus ou exclus ? Les correspondances inventoriées sont-elles dans l’archive ? | 1 |
| Inventaire CSV sur son support d’origine et CD annoncés au PV | Administration ; copies éventuellement conservées par la cliente | Authentifier l’inventaire fourni, son algorithme et sa relation au jeu final. | 1 |
| Versions inventoriées du PST 93300, du PDF FACT 2018 SUITE et du raccourci USB2 | Administration / archive finale | Expliquer les trois différences de contenu. | 1 |
| Nom, version, paramètres et journaux du logiciel de collecte | Opérateurs des opérations techniques / administration | Expliquer les dates du 15, le regroupement du 28, les doublons et les étapes intermédiaires. | 1 |
| Séries/IMEI des téléphones, photographies et correspondance avec les scellés ; identité matérielle des Kingston | Dossier de procédure / détenteurs des supports | Rattacher TP-01/02/03 et le volume de destination aux appareils matériels. | 1 |
| Ordonnance complète, instructions applicables et actes utilisant les pièces | Dossier de procédure, via l’avocate | Examiner le périmètre ALMU, la qualification des correspondances et leurs conséquences juridiques. | 1 |
| PV et photographies de garde, mouvements, état d’alimentation et isolement réseau | Administration / détenteurs des scellés | Distinguer opérations constatées, automatisme possible et conditions déclarées. | 2 |
| Sauvegarde contemporaine TP-02/TP-03 et historique de migrations après le 17 octobre | Cliente, anciens ordinateurs ou sauvegardes conservées | Distinguer activité locale et historique transporté ultérieurement. | 2 |
| Relevés opérateur avec identité du matériel et journaux du point d’accès ASUS | Opérateur / détenteur du point d’accès, si conservés | Attribuer les appels et l’association Wi-Fi à un appareil à horloge vérifiable. | 2 |
| Identification Samsung série `R58RB2ETQER` et notes d’opérations Sage/suppressions | Opérateurs / détenteur du téléphone | Préciser le partage Internet, l’accès Sage et le motif des suppressions après ouverture. | 2 |
| Copies vidéo antérieures, réglages et journaux caméra/compte/horloge | Cliente / fournisseur ou équipements, si conservés | Expliquer le défaut et la lacune du salon, puis envisager une expérience sur témoin. | 3 |

La confirmation de mise à disposition S3 de 2026 et les contrôles de téléchargement sont documentés séparément en annexe D ; ils ne constituent pas des indices sur les opérations de 2024.

## 8. Annexes et références

Les annexes permettent de retrouver les dates exactes, les détails vérifiables et les limites des contrôles. Elles développent les réponses du texte principal et ne présentent pas de nouvelles investigations.

**Accès direct :** [chronologie détaillée](#annexe-a) · [précisions techniques](#annexe-b) · [limites et provenance](#annexe-c) · [conservation en 2026](#annexe-d) · [glossaire](#annexe-e) · [sources](#annexe-f) · [inventaire du matériel](#annexe-g).

<a id="annexe-a"></a>

### Annexe A — Chronologie détaillée

Les heures informatiques sont en **heure de Paris** : UTC+2 avant le changement d’heure du 27 octobre 2024, puis UTC+1. Les heures caméra sont celles des fichiers ou images, sans synchronisation vérifiée avec les autres appareils. Les déclarations de la cliente sont distinguées des traces.

Le 28 octobre, Windows rapporte une synchronisation avec `time.windows.com` et une correction d’environ **−9,238 secondes à 11 h 19 min 30 s**. Les heures antérieures sont reproduites telles qu’enregistrées ; elles ne sont pas corrigées silencieusement.

| Date et heure | Équipement | Fait constaté | Ce que cela permet d’établir |
|---|---|---|---|
| 15 octobre 2024, vers 10 h 43 à 10 h 53 | OP-01 | Reprise de Windows, session locale, puis veille prolongée avec batterie faible. | Fonctionnement du système ; auteur et position exacte par rapport au début de la perquisition inconnus. |
| 15 octobre, 13 h 25 min 19 s — horodatage vidéo, [note du 16 novembre 2026](NOTE-DE-CONSTATION-téléphones.md) | Téléphones / vidéo du salon | Une femme identifiée par Mme Sadedine comme étant Mme Adam intervient sur les trois téléphones ; les logos Apple apparaissent sur leurs écrans. | Constat de visionnage du prestataire, caractéristique d’un démarrage ; état antérieur, déverrouillage ultérieur et maintien sous tension jusqu’au 28 non établis. |
| 15 octobre, de 13 h 28 à environ 13 h 32 min 26 s, horloge caméra | SD-03, salon | Dernière vidéo conservée sur SD-03 pour cette journée, présentant des anomalies. | Présence d’images jusqu’à l’heure affichée ; aucune heure certaine d’arrêt de la caméra. |
| 15 octobre, vers 13 h 30 — déclaration | Téléphones | Mme Sadedine indique ne plus avoir accès à ses téléphones. | Repère déclaré, sans constituer l’heure vérifiée du début de la perquisition. |
| 15 octobre, après 14 h 19 — PV | OP-01 et téléphones | Mise sous scellés consignée, sans heure de fermeture individuelle. | Début documentaire de la conservation ; 13 h 30 reste un repère distinct de perte d’accès déclarée. |
| 15–26 octobre | Données TP-02 | 53 appels, dont 22 marqués sortants et 19 sortants à durée positive. | Historique de communications ; origine physique non établie, synchronisation/restauration non départagées. |
| 15 octobre, 18:33:26–18:36:27 | Données TP-03 | Deux champs `routined` liés à la registration/désinscription GNSS. | Dates système après le scellement consigné ; ni coordonnées, ni trajet, ni auteur établis. |
| 16 octobre, 01:40:51 puis 05:31:33–05:31:39 | Données TP-03 | Préférence mediaremote, puis créations Santé, événement PersonalAudio et huit transactions TipKit Messages. | Indices d’activité de services sur l’installation source ; pas de déplacement le 16, de SMS envoyé/lu ni de déverrouillage démontrés. |
| 16 octobre, 5 h 51 min 7 s | OP-01 | Heure de réveil programmé inscrite dans un événement du 15. | Une échéance prévue, **pas un réveil effectivement constaté**. |
| 16 octobre, 21 h 27 min 48 s | Freebox | Première activité conservée pour `DESKTOP-ICPNCMD`. | Présence réseau d’un ordinateur non identifié ; aucune action sur des fichiers démontrée. |
| 17 octobre, vers 17 h 15–17 h 18, puis 17 h 25 | Données de TP-02 | Traitements internes, puis propriétés d’association au réseau `ASUS_Z01RD`. | Séquence compatible avec un système iPhone en fonctionnement ; origine physique et manipulation humaine non certaines. |
| 27 octobre, vers 2 h 44–2 h 45, avant le changement d’heure | Données de TP-02 | Regroupement de 3 123 dates de modification dans la photothèque. | Traitement groupé possible ; aucune preuve de consultation ou retouche de chacune des photos. |
| 28 octobre, 10 h 22 puis 10 h 41 — PV | Présence de la cliente, puis OP-01 | Arrivée de la cliente à 10 h 22 ; ouverture du scellé du PC à 10 h 41. | Repères documentaires distincts, concordance à la minute avec la reprise Windows. |
| 28 octobre, 10 h 41 min 56 s, puis 10 h 47–11 h 11 | OP-01 | Reprise de Windows ; créations de fichiers regroupées dans `L16B/LOCAL`. | Activité après l’ouverture déclarée ; regroupement local fortement étayé. |
| 28 octobre, 10 h 41 min 56–59 s | OP-01 | Déconnexion du profil Wi-Fi `Freebox-537E9F` au réveil. | Pas de nouvelle connexion à cette box établie ce matin-là. |
| 28 octobre, 11 h 18 min 34–54 s | OP-01 / Samsung | Reconnaissance USB de `R58RB2ETQER`, nom « XCover 5 de David », puis configuration du pilote RNDIS de partage réseau. | Première reconnaissance conservée ; aucun usage antérieur retrouvé, sans certitude sur la première connexion absolue. |
| 28 octobre, 11 h 18 min 55–56 s | OP-01 | Création du profil « Réseau 2 » et capacité Internet signalée à 11:18:56.722328. | Accès Internet évalué par Windows ; interface de type Ethernet compatible avec un partage USB. |
| 28 octobre, 11 h 30 puis 11 h 45 — PV | Téléphones | Ouverture des scellés 2 à 4 ; insertion de SIM dans le téléphone du scellé 3 pour un code Apple. | Actes consignés ; correspondance avec TP-02 ou TP-03 non établie. |
| 28 octobre, 11 h 35 min 44–46 s puis 11 h 47 min 31–32 s | OP-01 / Samsung | Déconnexion de « Réseau 2 », reconfiguration de pilotes, puis « Réseau 3 » avec Internet. | Rapprochement fort avec le Samsung USB, sans preuve de deux accès physiques distincts. |
| 28 octobre, 13 h 25–13 h 57 | OP-01 | Interactions enregistrées avec des fichiers de messages sous `L16B/MESSAGERIES`. | Manipulations par le système ou les applications ; lecture humaine de chaque message non démontrée. |
| 28 octobre, 14 h 50–14 h 52 | OP-01 | Créations groupées dans `L16B/GDRIVE`, puis mise à la corbeille du document de mots de passe et de l’archive de téléchargement. | Regroupement local fortement étayé et suppressions datées ; contenus récupérés. |
| 28 octobre, 15 h 10 min 12–31 s | OP-01 / Sage | Lancement WGC, contacts avec les serveurs Sage et service de souscription, résultat 200. | Utilisation connectée du logiciel, pendant « Réseau 3 ». |
| 28 octobre, 15 h 11 min 48–51 s | OP-01 / Sage | Requête OAuth, résultat 200 à 15:11:49, puis requête au service de données hébergées avec résultat 200. | Échange de jeton abouti fortement étayé ; ni saisie manuelle d’identifiants ni opérateur établis. |
| 28 octobre, 15 h 16 min 31 s puis 15 h 18 min 42 s | OP-01 | Deux travaux PDF d’une page vers le `test.pdf` du Bureau OneDrive ; l’état conservé contient ALMU FA0338. | Génération PDF établie ; contenu initial de 15:16 non retrouvé séparément. |
| 28 octobre, 15 h 19 min 42 s | OP-01 | Génération de `C:\L16B\test.pdf`, deux pages ALMU FA0338 et FA0339. | Travail d’impression et contenu récupéré concordants. |
| 28 octobre, 15 h 23 min 32 s puis 15 h 24 min 17 s | OP-01 | Travail PDF de 205 pages vers `C:\L16B\Sage.pdf`, puis mise à la corbeille du `test.pdf` de deux pages. | Contenu des 205 pages non retrouvé séparément ; suppression du PDF de deux pages précisément datée. |
| 28 octobre, 15 h 28 min 33 s | OP-01 | Génération de 458 pages ALMU, retrouvées dans `C:\L16B\SAGE\sage.pdf`. | Sortie PDF effective corroborée ; pas de preuve autonome d’impression papier ou de transfert externe. |
| 28 octobre, 16 h 27 min 50–53 s | OP-01 | Brève déconnexion puis rétablissement de « Réseau 3 » et de sa capacité Internet. | Continuité du même profil avec interruption ; pas une garantie d’accès permanent à tous les services. |
| 28 octobre, vers 16 h 27, 17 h et 17 h 14 | OP-01 | Installation et démarrage associés à trois identifiants distincts de périphériques Kingston, selon les heures locales du journal Windows. | Présence de supports externes, sans preuve autonome de copie. |
| 28 octobre, 17 h 04 min 49–50 s | OP-01 / Sage | Lecture d’un flux de contenu Sage avec résultat 200. | Communication applicative encore réussie avant le retrait du Samsung. |
| 28 octobre, 17 h 14 min 11 s | OP-01 / Samsung | Retrait USB à 17:14:11.399631, déconnexion de « Réseau 3 » à 17:14:11.588420, perte de capacité Internet à 17:14:11.744032. | Concordance de moins d’une seconde renforçant fortement l’hypothèse du partage USB Samsung. |
| 28 octobre, 17 h 26–17 h 27 | OP-01 | Références à trois fichiers sur un volume Kingston. | Interactions avec ces chemins ; contenu de l’archive externe inconnu. |
| 28 octobre, 17 h 28 min 56 s–17 h 29 | OP-01 / Sage | Échec de résolution du serveur lors des tentatives de fin de session ; exception non gérée et défaillance de WGC enregistrées par Windows. | Échec de réseau/DNS et défaillance applicative ; pas une preuve de mot de passe refusé. |
| 28 octobre, 19 h 20 — PV et déclaration | Matériels | Clôture du PV ; restitution consignée sans heure individuelle. | Le PV ne date pas séparément la remise de chaque appareil. |
| 29 octobre, 17 h 59 min 18 s, horloge caméra | SD-03, salon | Reprise des noms de fichiers vidéo disponibles. | Fin de la lacune documentaire, sans explication de sa cause. |
| 12 novembre 2024, vers 23 h 35–23 h 51, dates des cartes | Trois cartes SD | Création datée de fichiers auxiliaires caractéristiques de Windows. | Traitement des cartes compatible avec Windows ; poste, auteur et modification des vidéos non établis. |

<a id="annexe-b"></a>

### Annexe B — Précisions techniques et pièces individualisées

Les noms de champs, identifiants et décomptes ci-dessous servent au contrôle des constats. Les conclusions accessibles sont exposées aux sections 4 à 6.

<a id="annexe-b1"></a>

#### B.1. Ordinateur, copies et correspondances

##### Activité du 15 au 28 octobre

Les traces étayent l’activité du 15 et la reprise du 28, séparées par une veille prolongée. L’échéance programmée du 16 et les dates anciennes présentes dans certains fichiers ne suffisent pas à établir un fonctionnement de Windows pendant l’intervalle.

**Le 28 octobre, Windows reprend à 10 h 41 min 56 s**, ce qui concorde à la minute avec l’ouverture du scellé d’OP-01 consignée au PV à **10 h 41**. **10 h 22 correspond à l’arrivée de la cliente**, et non à l’ouverture du PC. Le PV décrit le regroupement L16B et des exports. Outlook affiche des demandes de confirmation de suppression définitive et d’enregistrement de propriétés de messages. **Les réponses et la réussite de ces suppressions ne sont pas établies**, contrairement aux mises à la corbeille documentées ci-dessous.

##### Samsung : identification, antériorité et accès Internet

Le numéro exact **`R58RB2ETQER`** est lié au nom **« XCover 5 de David »** par la clé SOFTWARE `Microsoft\Windows Portable Devices\Devices\USB#VID_04E8&PID_6860#R58RB2ETQER`, valeur `FriendlyName`. Sa dernière écriture est le **28 octobre à 10:18:36.174023 UTC**, soit 11:18:36 à Paris ; cette date n’est pas assimilée à une date certaine de création de la clé. Les instances matérielles sont `USB\VID_04E8&PID_6860\R58RB2ETQER` et `USB\VID_04E8&PID_6863\R58RB2ETQER`. Le pilote RNDIS utilise le service **`usbrndis6`**.

La première occurrence du numéro exact est **Kernel-PnP/Configuration, événement 430, RecordID 893**, à **11:18:34.352547 Paris**, corroborée par la section SetupAPI débutant à **11:18:34.392**. Les **18 événements alloués portant explicitement cette série** se répartissent entre le 28 octobre (16 événements) et les suppressions d’instances du 3 décembre (deux événements). Aucun usage antérieur du numéro exact n’est retrouvé dans les 359 EVTX ni les dix journaux SetupAPI examinés. Les sections du 3 décembre portent la commande **`cleanmgr.exe /autocleanstoragesense /d C:`** ; elles documentent un nettoyage Windows sans intention de dissimulation établie. Aucune propriété de première installation rattachable à cette série ne reste accessible dans les clés examinées. **La première connexion absolue reste donc indéterminée.**

NetworkProfile et NCSI documentent « Réseau 2 » sur l’interface **`{01D72DD1-9584-43CE-B52E-BC555D29936A}`**, puis « Réseau 3 » sur **`{479CF457-AF75-4CDC-8C88-124C0693B5F6}`**. La configuration RNDIS et le retrait du Samsung immédiatement suivi de la perte réseau constituent un faisceau fort pour le partage USB. La correspondance persistante directe de ces deux GUID opérationnels avec la série n’est plus conservée ; les interfaces explicitement nommées RNDIS par NDIS ont des GUID distincts, détaillés dans le [complément réseau](ordinateur/rapport-complementaire-OP-01-Sage50-reseaux-28oct2024.md). Le nom de l’appareil, la catégorie Ethernet et la proximité temporelle ne désignent ni propriétaire, ni réseau amont, ni opérateur humain.

##### Sage : traces d’authentification et PDF ALMU effectivement produits

Le journal **`C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Logs\Standard.SgLog`** conserve 199 lignes du 28. Les lignes **1832–1833** décrivent le service de souscription à 15:10:30–31 ; les lignes **1834–1836**, la requête OAuth à 15:11:48 et son résultat 200 à 15:11:49 ; les lignes **1837–1839**, l’accès au service CDM avec résultat 200. Le type d’octroi et le corps des réponses ne sont pas conservés : **une saisie manuelle d’identifiants, l’identité du compte utilisé et une nouvelle activation de licence ne peuvent être affirmées**. Le stockage local ALMU est identifié dans **`C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\ALMU\CDMDATA`**, distinct de la référence logique au service de données hébergées.

Le journal **PrintService/Operational** conserve cinq fins de travaux **307**, toutes vers **Microsoft Print to PDF** :

| Heure de Paris | RecordID | Résultat et contrôle du contenu |
|---|---|---|
| **15:16:31** | **2419** | Une page vers `C:\Users\fintm\OneDrive\Bureau\test.pdf` ; contenu initial non retrouvé comme état distinct. |
| **15:18:42** | **2424** | Une page au même chemin : **ALMU FA0338**, PDF de **405 202 octets**, entrée MFT **181043**. |
| **15:19:42** | **2429** | Deux pages vers `C:\L16B\test.pdf` : **FA0338 et FA0339**, PDF de **499 320 octets**, entrée MFT **166334**, retrouvé dans la corbeille. |
| **15:23:32** | **2445** | **205 pages** vers `C:\L16B\Sage.pdf` ; contenu exact non retrouvé séparément. |
| **15:28:33** | **2450** | **458 pages ALMU**, PDF de **42 818 862 octets**, entrée MFT **30590**, actuellement dans `C:\L16B\SAGE\sage.pdf`. |

Le PDF final porte le titre **`Facture - FA0543`**, le producteur **`Microsoft: Print To PDF`** et une création/modification interne à **15:28:33 Paris**. Sa modification NTFS à **15:28:33.485057** précède immédiatement la fin de travail à **15:28:33.649956**. Son SHA-256 est **`0718f1b0819210c2def92a8097bafb1a7c0586673cf37848afbbf55c943728a6`**. Les **458 textes de page portent ALMU**. Le PDF d’une page correspond textuellement à sa page **254** ; les deux pages du PDF de la corbeille correspondent aux pages **254 et 255**, après retrait des espaces et sauts de ligne. Les états se recouvrent et ne sont pas additionnés. Une tentative intermédiaire `Facture - FA0543` se termine à 15:21:33 par l’événement **824 / RecordID 2435**, erreur `0x80070057` : elle n’est pas comptée comme une impression réussie.

Le contrôle du SIRET dans les **458 textes de page** retrouve uniquement **`81816735500010`**, celui de SAS ALMU. Les alias et sorties ne confirment l’utilisation que de ce dossier ; les autres stockages présents et le modèle global DMM CONSEILS ne certifient pas d’autres ouvertures. Les préférences `CamBFile`, non intégralement décodées, ne constituent pas un journal exhaustif.

Le contrôle complémentaire **EBWebView** retrouve pour Gestion Commerciale **27 visites de juillet à octobre 2026**, **zéro entrée dans chacune des deux bases de mots de passe**, et **11 métadonnées de cookies Sage/Ciel de 2026**. Pour Ciel Paye, il retrouve **12 visites d’avril au 29 octobre 2024**, sans visite du 28, et une base de mots de passe vide ; ce second logiciel ne prouve pas le mode d’authentification du premier. **Aucun de ces états ne départage une saisie manuelle, un identifiant mémorisé ou un renouvellement de jeton le 28 octobre 2024.** Les **39 vérifications d’empreintes** concordent avant/après lecture et les **sept fichiers de résultats rapatriés** concordent avec SIFT. Les [résultats et limites du contrôle](ordinateur/recherche-OP-01/sage-dossiers-auth-20261113-swqgba2s/compte-rendu.md) sont détaillés dans le rapport ordinateur, section 7.3.

Ces recoupements **établissent une production locale de PDF ALMU le 28**, sans identifier l’auteur ni certifier la copie complète de la base ou l’inclusion du PDF dans les fichiers finalement emportés. Le champ auteur PDF `malika sadedine` n’identifie pas la personne au clavier. Les compléments du 13 novembre ont contrôlé respectivement **19 et 22 copies de pièces par SHA-256**, et **65 et 54 événements par un second lecteur EVTX** ; leurs périmètres se recoupent. Les [événements d’impression](ordinateur/recherche-OP-01/samsung-almu-20261113/resultats/print-events-day.json), [contenus et empreintes PDF](ordinateur/recherche-OP-01/samsung-almu-20261113/resultats/pdf-content.json) et [contrôles indépendants](ordinateur/recherche-OP-01/samsung-almu-20261113/resultats/verification-evenements-independante.json) permettent de vérifier les constats.

##### Données regroupées, archives et suppressions du 28 octobre

Le dossier `L16B` contient des documents locaux, des données Google Drive et iCloud, des messageries, des données de téléphones et des documents comptables ou bancaires. La concentration des dates de création et les comparaisons de contenus soutiennent fortement un **regroupement local de données le 28 octobre**. La présence d’archives de conversations téléphoniques ne démontre pas leur extraction directe depuis un téléphone connecté à OP-01.

Les deux archives Outlook ont été lues lors des compléments. Une archive Google Takeout contient une messagerie et un manifeste indiquant un export le 28 octobre à 12 h 42 min 33 s, heure de Paris. **La présence de cet export Google est établie ; sa production sur OP-01 ne l’est pas.** Il peut avoir été créé ailleurs puis copié sur cet ordinateur. Ni la machine ayant demandé cet export ni son demandeur ne sont identifiés. Cette limite ne s’applique pas indistinctement aux PDF ALMU, dont la génération locale est corroborée par les travaux d’impression et les fichiers décrits ci-dessus.

**Dix mises à la corbeille sont enregistrées le 28 octobre**, entre 11 h 02 et 15 h 24 : deux raccourcis, un document de gestion de mots de passe, une archive de téléchargement, cinq fichiers du dossier d’états de Ciel et `L16B/test.pdf`. Les cinq fichiers Ciel ne doivent pas être présentés comme une base comptable détruite.

L’archive récupérée contient **94 fichiers**. Parmi eux, **93 sont identiques aux fichiers conservés dans `L16B/GDRIVE`**. Le document de gestion de mots de passe, absent de ce dossier actuel, subsiste à la fois dans l’archive récupérée et séparément dans la corbeille. Aucune consultation ou utilisation des identifiants n’est démontrée ; aucune valeur confidentielle n’est reproduite ici.

Le PDF récupéré `test.pdf` contient deux factures. Ses informations internes indiquent une impression PDF à **15 h 19 min 42 s**, suivie d’une mise à la corbeille à **15 h 24 min 17 s**, sans auteur identifié. **Le contrôle du 9 novembre retrouve le même texte de ces deux factures aux pages 254 et 255 de `L16B/SAGE/sage.pdf`**, après suppression des espaces du texte extrait. Leur contenu textuel subsiste donc dans L16B ; ce résultat ne démontre ni identité binaire des PDF ni motif de la suppression.

Les archives `GDRIVE.zip` et `GDRIVE (2).zip` présentent des erreurs, mais **les contenus des 93 fichiers contrôlés sont retrouvés intacts dans `L16B/GDRIVE`**. L’intégrité des contenus ne signifie donc pas celle des archives. Ces dernières portent des dates de création locale de juillet 2026 ; l’origine et la date de leurs défauts restent inconnues.

##### Supports externes et limites des transferts

Les journaux Windows enregistrent le 28 octobre **trois identifiants distincts de périphériques USB Kingston DataTraveler**. Il s’agit bien d’identifiants différents, et non du seul comptage de trois événements de connexion. Le rapprochement avec les supports physiques reste à effectuer. Entre **17 h 26 min 19 s et 17 h 27 min 29 s**, les historiques d’interaction référencent un volume nommé Kingston et trois fichiers sous `E:\saddedine\` :

- `Archive_saddedine.zip` ;
- `Inventaire_saddedine.csv` ;
- `Rejets_saddedine.txt`.

**Ces trois noms sont à rechercher dans les pièces de procédure et sur les supports de destination.** L’archive externe elle-même n’a pas été récupérée. Son contenu, son intégrité et son rattachement à l’un des trois identifiants de périphériques ne sont pas établis. Aucun lien de contenu ne permet d’affirmer qu’elle contient `L16B` ou les archives Outlook.

Des traces concernent aussi un dispositif Western Digital et le lancement de son programme de déverrouillage. Elles ne démontrent pas un déverrouillage réussi. **Les traces informatiques seules ne permettent pas de rattacher le jeu copié à un support externe déterminé.** Le PV décrit toutefois une copie sur une clé de l’administration ; cette destination est donc documentée, même si le support physique et le contenu exact n’ont pas été contrôlés. Aucun autre destinataire de transfert sortant n’est identifié par les analyses.

##### Ce que le PV décrit comme extrait et emporté

Aux **pages 7 à 11 du fichier PDF**, le [PV de saisie](docs/PV%20DE%20SAISIE.pdf) décrit des copies de fichiers locaux, Google Drive et iCloud, de messageries, de données SAGE et SHINE, ainsi que de conversations WhatsApp de l’iPhone 13 et de fichiers du premier Mini. Il décrit ensuite une sélection, l’exclusion de données personnelles et de correspondances d’avocats, puis la copie des fichiers retenus sur une clé USB de l’administration, leur authentification numérique et la gravure des inventaires sur deux CD finalisés.

**Le PV consigne donc bien une extraction et une copie de fichiers par l’administration.** L’incertitude concerne la composition exacte du jeu retenu, et non l’existence de la copie déclarée. La page 13 précise que L16B est laissé sur le PC à titre informatif avec l’accord de la cliente et ne remplace pas les fichiers saisis. La présence d’un document dans L16B ne suffit pas à prouver son inclusion dans la copie emportée.

**Complément du 16 novembre :** le CSV désormais fourni contient les 27 chemins PDF du Mini et les SHA-512 des vingt contenus, dont le document reproduisant des échanges avec Me Isabelle Guillou. Cette présence dans l’inventaire est établie ; elle ne repose plus seulement sur L16B. Le CD d’origine et le support de destination n’ont pas été examinés : l’authentification indépendante de l’inventaire, sa correspondance exhaustive avec l’archive emportée et la conservation actuelle par l’administration restent à vérifier. Les attributs de 17 contenus favorisent la lignée TP-03 sans déterminer un appareil physiquement source ou le numéro de scellé.

Le [contrôle des catégories du PV du 9 novembre](investigations/20261109-controle-l16b-photos/compte-rendu.md) confirme une concordance substantielle avec L16B : deux PST, trente EML, Takeout, PDF Sage et export SHINE ; ce dernier comporte 94 mouvements et 27 PDF de justificatifs, avec des bornes OFX concordantes. Cette concordance n’est pas une identité exhaustive avec le jeu saisi. Deux ZIP GDRIVE et `CADA.pdf.pdf` portent des créations NTFS FN de 2026 et ne sont pas automatiquement attribuables aux opérations de 2024.

##### Correspondances avec des avocats : présence locale et saisie définitive

**La présence de correspondances dans L16B est un constat de contenu. La comparaison SHA-512 établit désormais que le PST DMM et Takeout correspondent exactement aux empreintes de l’inventaire fourni ; le PDF Bourarach est également identifié individuellement dans ce CSV. Le PST 93300 diverge.** Le contrôle matériel de l’archive et du support emportés reste distinct de cette identification dans l’inventaire. Le regroupement de L16B pendant les opérations du 28 octobre est fortement corroboré par le PV et la chronologie des fichiers. Il ne prouve pas que chacun des documents qui s’y trouvent a été retenu après le filtrage annoncé.

| Pièces effectivement retrouvées | Concordance à l’inventaire fourni | Portée et limite |
|---|---|---|
| **21 messages du PST DMM** : Fakiroff / Roosevelt Avocats (9), Wahrheit (7), Negrevergne (5) | **SHA-512 du PST identique au CSV**, ligne 1498. | Présence établie dans le conteneur correspondant à l’inventaire ; lecture par les agents et utilisation fiscale non démontrées. |
| Échanges Pascoët / Rubio cités, notifications Dress / DocuSign et Liwer / AR24 | PST DMM ou ZIP Takeout **concordants** avec le CSV, lignes 1498 et 1529. | Distinguer citations et notifications des messages directs ; un avis de non-remise ne prouve pas la réception. |
| **2 messages Khallouki et 3 transferts/reproductions du PST 93300** | **SHA-512 divergent** de celui du CSV, ligne 1497. | Présents dans l’image, mais présence et identité non certifiées dans la version inventoriée. |
| `L16B/TELEPHONES/IPHONE13_MINI/Rép  Dossier bourarach.pdf` | Chemin et **SHA-512 concordants** dans le CSV ; contenu identique dans TP-02 et TP-03. | Présence dans l’inventaire établie ; qualification avocat-client, archive finale et utilisation à examiner. |

Les détails et références sont conservés dans le [tableau des messages](investigations/20261109-correspondances-elargies/tableau-messages.md), le [tableau des documents](investigations/20261109-correspondances-elargies/tableau-documents.md) et leurs annexes techniques. Une proposition de services d’avocats, une notification de recommandé, une mention du conseil de la partie adverse ou un courrier d’avocat déjà adressé à l’administration ne sont pas assimilés automatiquement à une consultation confidentielle entre la cliente et son avocat.

**Indices individualisés pour `Rép  Dossier bourarach.pdf`.** L’entrée MFT **381463, séquence 41**, porte une création FN au **28/10/2024 à 17:13:43,799497, heure de Paris**, dans `L16B/TELEPHONES/IPHONE13_MINI`. Son contenu, SHA-256 `2e82aa66ecbc307a98ce2a170799bed53af49c0de9dd9c0c2da00c87c530df3c`, est strictement identique à deux copies TP-02 et à une copie TP-03. Cette dernière conserve `lastused=15/10/2024 13:42:55,987134933`, suivi d’un changement de statut à 13:42:56 ; la création CSV est à **13:42:57,930**. Le chemin et le SHA-512 du PDF figurent dans l’inventaire transmis. Les références Jump Lists du **29 vers 01:45:21 Paris** restent postérieures et ne prouvent pas une lecture par les agents. La [fiche historique](investigations/20261109-clarification-correspondances/fiche-bourarach.md) est complétée par la [réponse Q1](inventaire-DNEF/rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md). **L’ancienne réserve d’absence de toute trace individuelle d’inventaire est levée pour ce PDF ; le contenu de l’archive finale reste à contrôler.**

**Réponse à la question « l’administration a-t-elle pris des échanges avec un avocat ? » : la présence de correspondances dans des fichiers correspondant aux empreintes de l’inventaire fourni est établie.** Le PST DMM concordant contient les 21 messages précités et les traces Pascoët / Rubio / Dress ; Takeout concordant contient la notification Liwer. Le PDF Bourarach / Guillou est identifié individuellement dans le CSV. Cette preuve documentaire ne repose plus seulement sur L16B. **Les correspondances Khallouki du PST 93300 divergent ne peuvent pas être certifiées dans la version inventoriée.** Le contrôle du support authentifié et de l’archive finale, la lecture par les agents, l’utilisation fiscale et la qualification du filtrage restent distincts ; la portée juridique relève de l’avocate. Les [deux tableaux classés selon la concordance SHA-512](ordinateur/recherche-OP-01/correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md) individualisent toutes les traces.

##### Correspondances : couverture de la recherche élargie et limites

La recherche a été étendue aux en-têtes et corps de **6 206 occurrences de messages**, aux pièces jointes, aux documents indépendants de L16B, aux images et aux anciens formats bureautiques. Les **1 487 fichiers sources suivis ont les mêmes SHA-256 avant et après collecte**. Cette campagne porte sur un corpus délimité, pas sur l’intégralité du disque.

Des échanges supplémentaires ont été identifiés avec **Mustapha Khallouki**, **Nicolay Fakiroff / Roosevelt Avocats** et **Marc-Alexandre Wahrheit**. Un ancien Word joint à un message contient un état de frais et honoraires de Wahrheit pour ALMU, daté du 15 novembre 2022. Les courriers de Jonathan Rubio retrouvés sont adressés à l’administration fiscale : ils doivent être distingués des échanges confidentiels avocat-client. Les destinataires appelés « Maître » sans qualité établie restent à vérifier.

Le [tableau des messages](investigations/20261109-correspondances-elargies/tableau-messages.md) présente **41 occurrences sélectionnées**, qui peuvent répéter des conversations. Le [tableau des documents](investigations/20261109-correspondances-elargies/tableau-documents.md) distingue correspondances, honoraires, pièces fiscales, mentions générales et faux positifs. Les sources, empreintes complètes et rapprochements avec les traces de fichiers sont conservés dans les annexes techniques privées de la campagne. **Aucune de ces lignes ne démontre une inclusion dans le jeu définitivement saisi.**

Une **proposition de rectification du 29 juillet 2022**, concernant DMM et les exercices 2019–2020, a été retrouvée dans `L16B/LOCAL/DMM/RECTIFICATION JUILLET 2022.pdf` (56 pages). Son identification repose sur la première page contrôlée visuellement ; ses motifs ne font pas l’objet d’une nouvelle analyse fiscale complète. Elle est antérieure à la saisie de 2024 et ne remplace ni l’ordonnance de visite ni une éventuelle rectification ultérieure utilisant les données saisies.

Pour le PDF Guillou du Mini, les références Jump Lists examinées datent du **29 octobre 2024 vers 1 h 45, heure de Paris**, après la restitution. Elles ne prouvent donc pas une lecture par un agent pendant les opérations. Les dates NTFS peuvent être conservées lors d’une copie et n’identifient pas à elles seules l’auteur ou la date d’une extraction du téléphone. Le contrôle des trois textes WhatsApp n’a identifié aucun échange d’avocat par les motifs utilisés ; cela ne constitue pas une preuve générale d’absence.

**Limite de clôture :** à la demande du prestataire, l’OCR exhaustif a été arrêté après **4 238 résultats journalisés sur 5 365 contenus**, laissant **1 127 contenus sans résultat terminé dans cette passe**. Les résultats acquis et la liste de reprise sont conservés. La passe native sur les PDF et les vérifications ciblées complètent ce décompte ; aucune exhaustivité n’est revendiquée. Le [compte rendu détaillé](investigations/20261109-correspondances-elargies/compte-rendu.md) documente méthodes, résultats, limites et suites.

**Pour ces correspondances, les deux priorités sont le filtrage et le périmètre.** Les nouveaux résultats précisent les pièces à contrôler, sans établir une illégalité. Leur confrontation avec l’inventaire, les fichiers définitivement saisis et l’ordonnance reste indispensable.

##### Cadre légal général et limites de l’appréciation

L’[article L. 16 B du livre des procédures fiscales, version applicable en 2024](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048834116), prévoit, sous autorisation judiciaire, la recherche et la saisie de documents, y compris informatiques, se rapportant aux agissements visés. Ce pouvoir est encadré par l’ordonnance et les garanties de procédure, notamment le respect du secret professionnel et des droits de la défense. **La copie de fichiers n’est donc pas, par elle-même, une irrégularité ; l’existence de ce pouvoir ne valide pas chaque document saisi.**

Les échanges avocat-client appellent un examen juridique de leur contenu et de leur contexte. Distinctement de la saisie, leur utilisation pour établir une imposition ou une majoration est encadrée : voir la [décision du Conseil d’État du 28 février 2025, n° 486336](https://www.conseil-etat.fr/fr/arianeweb/CE/analyse/2025-02-28/486336), relative à l’absence d’accord du client à la levée du secret professionnel.

**Le présent rapport technique ne conclut ni à la régularité ni à l’irrégularité globale de la saisie.** Il identifie des documents et des limites probatoires à soumettre à l’avocate. Le contrôle nécessite de confronter l’ordonnance autorisant la visite, le PV, l’inventaire fourni et les fichiers effectivement saisis. La demande prioritaire est l’authentification du CSV désormais fourni et l’accès au jeu saisi pour compléter la comparaison des chemins, contenus et empreintes ; l’indisponibilité du CD d’origine ne signifie pas que cet inventaire n’existe plus auprès de l’administration.

##### Points de confrontation juridique à conserver

Le contrôle du filtrage doit notamment porter sur les échanges incorporés dans des PDF et ceux concernant des avocats absents de la liste manuscrite. Il faut demander les critères et opérations de filtrage, ainsi que la qualification des documents éventuellement retenus et leur utilisation dans une rectification ou une majoration.

L’ancienneté d’un document ou le fait qu’il concerne un tiers ne suffisent pas à le rendre insaisissable ; sa pertinence doit être appréciée concrètement au regard de l’ordonnance. Les conditions des recherches et extractions dans les messageries, téléphones et espaces cloud restent à confronter aux autorisations et instructions disponibles.

##### Accès à distance et attribution

Aucune prise en main à distance non autorisée n’est démontrée. Des invitations anciennes à une téléassistance Sage, datées de 2022, et un raccourci de téléassistance de 2023 ne prouvent pas une session effectivement établie. Une détection de document trompeur en mai 2024 est suivie d’une mise en quarantaine déclarée réussie, sans compromission réussie démontrée.

Le compte Windows observé est `fintm`. **Il n’identifie pas la personne ayant utilisé le poste.** Aucun effacement ou falsification des journaux destiné à masquer une activité n’a été établi.

##### Après la restitution, appairages et limites de datation

Le [tableau détaillé](investigations/20261019-retour-cliente/compte-rendu.md#4-dix-mises-à-la-corbeille-contre-lecture-directe) donne chaque chemin d’origine et chaque heure.

La relecture de **359 journaux Windows, soit 275 577 enregistrements**, ne retrouve aucun événement après **19 h 20 le 28**, ni du 16 au 27. Les 285 rendus XML non valides ont été repris pour leurs dates. Le contrôle complet de la MFT retrouve toutefois **cinq fichiers iCloud avec des dates anciennes après 19 h 20**, mais une modification de leur entrée MFT en 2026 : **ces métadonnées ne prouvent pas une activité locale du PC le soir du 28**. Les interactions PST du 29 déjà décrites sont également postérieures à la restitution déclarée.

Un enregistrement d’appairage Apple existe sur OP-01 pour un UDID **différent de TP-02 et désormais identifié comme celui de TP-03**, avec création SI en juillet 2022 et création FN/modification en décembre 2023. Il ne démontre ni un branchement en octobre 2024 ni l’emploi d’un outil d’extraction. Les deux dates ne sont pas fusionnées en une date certaine de premier appairage.

Les trois identifiants Kingston restent à rapprocher de la **clé de destination décrite au PV** ; la concordance de marque n’identifie pas un support physique. Le nom Takeout donne **12:41:05 Paris**, le manifeste **12:42:33** : ces 88 secondes sont compatibles avec des étapes d’export, sans permettre de calibrer l’horloge Windows.

<a id="annexe-b2"></a>

#### B.2. Téléphones et recoupements

##### Séquence Wi-Fi et bornes des appels

Le **17 octobre, 17:25:47–52**, la séquence conservée associe ajout du réseau `ASUS_Z01RD`, motif `WiFi Settings`, date `JoinedByUserAt`, génération d’une MAC puis association en **4,7 secondes**. Aucun déverrouillage ni appareil physique à l’origine n’est établi. Un autre réseau fournit un contre-exemple : une date « utilisateur » ancienne est conservée lors d’un ajout ultérieur. La migration/restauration d’un état complet reste donc à départager.

Le contrôle des **53 appels** situe leurs bornes au **15 octobre à 18:50–26 octobre à 17:14**. Parmi eux, **22 sont marqués sortants sur huit jours**, dont **19 à durée positive**. Ces enregistrements ne localisent pas leur origine sur un téléphone physique. Voir la [revue contradictoire](investigations/20261110-revue-intervention-scelles/compte-rendu.md).

##### TP-02 — traces avant et après ouverture

La sauvegarde examinée est rattachée à **TP-02 par son numéro de série**. Elle contient des traces datées concernant les appels, les messages, les photographies, le Wi-Fi et les applications. **Ces dates ne prouvent pas que le téléphone physique a été manipulé aux heures indiquées** : certaines données peuvent avoir été synchronisées avec d’autres appareils ou restaurées ultérieurement.

Le **17 octobre**, des traitements internes vers 17 h 15–17 h 18 précèdent une association Wi-Fi à `ASUS_Z01RD` vers 17 h 25. Cet enchaînement est compatible avec un système iPhone actif, y compris automatiquement, sans démontrer un déverrouillage ni une consultation humaine.

La sauvegarde contient **53 enregistrements d’appels datés du 15 au 26 octobre 2024**, dont **22 marqués sortants sur huit jours et 19 sortants à durée positive**, confirmés par le contrôle SIFT du 10 novembre. Ces dates se situent avant l’ouverture consignée des téléphones. Ces données ne permettent pas d’affirmer que ces appels ont été passés ou reçus sur ce téléphone physique pendant cette période, ni d’identifier une personne à l’origine des opérations.

Le **27 octobre vers 02:44–02:45 (UTC+2)**, 3 123 dates de modification sont regroupées dans la photothèque. Ce regroupement est compatible avec un traitement de bibliothèque ; il n’établit ni consultation ni retouche humaine des photos.

Le **28 octobre, après l’ouverture à 11 h 30**, TP-02 conserve trois SMS entrants comportant des horodatages `date_read` dans `sms.db` à **12 h 03 min 18 s, 12 h 10 min 06 s et 12 h 46 min 06 s** (heure de Paris), des associations Wi-Fi à 12 h 31 et 14 h 32, une séquence compatible avec une capture d’écran vers 13 h 36 et des traitements de Photos vers 17 h 31–17 h 32. Les trois lignes SMS portent également `is_read=1` ; le [contrôle des corps](investigations/20261109-sms-lecture/compte-rendu.md) identifie un code de réinitialisation de mot de passe Microsoft et deux codes de validation Google. Les dates de lecture ne démontrent pas, à elles seules, une lecture humaine locale ou l’utilisation des codes. **Mme Sadedine confirme toutefois avoir effectué elle-même la réinitialisation Microsoft et les validations Google, car elle n’arrivait pas à se connecter pour l’administration** ([courriel, point 3](docs/mail-3.txt)). Cette déclaration explique ces démarches ; **à sa demande, les trois SMS ne font plus partie des points à approfondir**. L’image de la capture manque ; aucun auteur de cette capture ni extraction par un tiers n’est identifié.

Le diagnostic WidgetKit du **28 octobre à 12 h 26** conserve `uptime=2500` secondes, soit 41 min 40 s dans sa présentation. Apple nomme ce champ **« Time Awake Since Boot »**, temps d’éveil depuis le démarrage. La distinction documentée entre compteurs incluant ou excluant le sommeil système, la précision réduite et les limites de raccord au champ IPS empêchent d’en déduire une heure d’allumage par simple soustraction. **Cette valeur ne prouve ni un démarrage vers 11 h 45, ni que TP-02 était éteint avant l’ouverture des scellés.** Les sources Apple et les limites sont détaillées dans la [note documentaire sur l’uptime](investigations/20261109-documentation-uptime/note-technique.md).

À **17 h 39**, LSC Smart Connect conserve des ressources compatibles avec le chargement ou l’actualisation d’un panneau caméra. **Aucun visionnage de vidéo n’est démontré.** Les catalogues examinés ne contiennent aucune référence de média du 15 au 28 octobre et ne constituent pas un historique complet des accès. Xiaomi Home fournit surtout des configurations permettant des rapprochements avec des équipements réseau.

Le nom `ASUS_Z01RD` apparaît aussi dans des traces d’OP-01, probablement parmi des réseaux Wi-Fi disponibles. Ces traces ne sont pas datées et ne prouvent ni une connexion du PC à ce réseau, ni sa présence au même endroit que TP-02, ni l’émission de ce réseau par OP-01.

##### Identification des scellés, réseau ASUS et traces après restitution

**La correspondance TP-02/TP-03 avec les scellés n° 3/n° 4 reste indéterminée.** Les deux sont des iPhone 13 mini rouges ; la sauvegarde identifie TP-02 par sa série, mais le mail ne donne pas les séries des scellés. TP-01 est vert dans l’attestation et l’iPhone 13 du scellé n° 2 est décrit noir : rapprochement candidat, divergence non résolue. OP-01 correspond au modèle du scellé n° 1.

Deux BSSID ASUS_Z01RD sont conservés avec des associations du **28 octobre**, **22:B0:A5:94:1F:AF** et **32:0D:CA:FD:68:8C**. Ils ne certifient pas le point d’accès utilisé le **17**. Aucun propriétaire identifié ; synchronisation/restauration toujours non exclues. L’absence connue d’ASUS dans l’entourage est une déclaration, pas une identification de l’émetteur.

Des dates existent **après 19 h 20 le 28** : appel à **19:39:46**, champ `LinkDownTimestamp` ASUS à **19:40:02**, caches LSC vers **22:35 et 23:26**. Elles sont postérieures à la restitution déclarée, sans auteur établi et sans preuve de visionnage des caméras. Le tri ciblé du manifeste et la relecture de 25 plist de gestion/comptes ne révèlent pas de session d’extraction d’octobre 2024 ni d’historique complet des appareils associés depuis 2021.

Le démarrage constaté dans la vidéo le 15 à 13 h 25 min 19 s est exposé en section 1.6 et en annexe A, avec référence à la [note de constatation du 16 novembre](NOTE-DE-CONSTATION-téléphones.md). La date du branchement de l’appareil d’extraction demeure « le 15 / le 28 » et ne doit pas être confondue avec ce rallumage.

##### TP-01 — réception différée possible et métadonnées non localisantes

La sauvegarde du 9 novembre 2026 est rattachée à **TP-01 par la série Q13QT4F164**. Sur SIFT, l’inventaire vérifie la présence des 48 895 objets ordinaires référencés et la collecte avec empreintes de 2 420 objets, complétée par le Wi-Fi de secours et des ressources applicatives. Le [rapport dédié](telephones/analyse-TP-01.md) détaille les contrôles et leurs limites.

**Pendant l’intervalle de conservation**, deux messages WhatsApp entrants sont datés du **15 octobre à 16:51:24 et 17:41:48**, mais leur `ZSENTDATE` se situe le **28 vers 16:13:08**, dans un groupe de quatorze messages datés du 15. Une récupération différée est compatible avec ces valeurs ; une réception locale le 15 n’est pas démontrée. La table `deleted` de la messagerie vocale comporte des dates du 15, du 17 et du 19 : ce sont des dates associées aux messages, pas des dates de suppression. Les `trashed_date` de ces lignes valent zéro.

Des métadonnées iCloud Drive portent des dates du **23 octobre, 09:39–09:47**. Leur présence dans les bases client et serveur ne fait pas deux preuves indépendantes d’activité sur TP-01 ; l’appareil à l’origine de ces dates n’est pas établi. Des traductions/configurations et quatorze fichiers de ressources ou de cache AliExpress portent également des dates pendant l’intervalle. Ces pistes sont conservées, sans départager écriture locale, conservation de dates distantes ou import/restauration.

**Après l’ouverture à 11 h 30 le 28**, des transactions de Calendrier, Messages, Mail, Notes, Rappels, Téléphone, Safari, Fichiers et Photos sont datées entre **14:26 et 17:51**. Elles décrivent des traitements internes, sans prouver autant de consultations humaines. Deux lignes WhatsApp sortantes apparaissent à **17:44:24 et 17:44:54**, sans auteur établi. Un champ `uartDetachTimes` porte une date compatible avec **16:59:23** ; il n’identifie ni accessoire, ni ordinateur, ni extraction.

Le fichier Wi-Fi courant est vide ; sa copie de secours conserve **37 réseaux**, aucun `ASUS_Z01RD`, sans date centrale parmi les 423 valeurs plist décodées. Aucun horodatage central n’est retrouvé dans les quatre champs de messages natifs et les six champs de la photothèque explicitement contrôlés. Les journaux Santé, Knowledge et diagnostics utiles à l’étude de TP-02 ne sont pas disponibles sous les noms recherchés dans TP-01. Ces absences limitent la conclusion : **activité locale sous scellé non établie ; inactivité non certifiée**. La divergence entre TP-01 vert et le scellé n° 2 décrit noir subsiste.

##### TP-03 — traitements système et recherche d’un marqueur humain

**La sauvegarde TP-03, série Y4Q9KGHG26, contient des indices datés avant l’ouverture des téléphones.** Le **15 octobre à 18:33:26 et 18:36:27**, deux préférences `routined` conservent des dates de registration/désinscription GNSS. Elles ne fournissent aucune position ni identité d’opérateur. Une autre date native figure dans `mediaremote` le **16 à 01:40:51**, sans sémantique exacte validée.

**Le 16 à 05:31:33–05:31:39**, une séquence associe trois magasins : créations des objets Santé **348331 et 348332**, événement interne PersonalAudio **31013**, puis huit transactions TipKit **1217–1224** attribuées à `MobileSMS`. Les objets Santé représentent un intervalle du **15 à 13:14**, et ne prouvent aucun déplacement le 16. Les transactions ne sont pas huit SMS. Cette convergence est compatible avec une reprise de services, y compris automatique, sur l’installation source ; une restauration d’historique et une horloge incorrecte restent à départager. L’identité Santé concorde avec la préférence healthd de TP-03, sans devenir un identifiant matériel infalsifiable.

**Approfondissement de la piste humaine, le 10 novembre.** Les huit transactions correspondent à 14 changements de conseils/règles/paramètres TipKit, sans modification de message identifiée. Leurs règles visent l’attente du cloud, l’éligibilité à l’accueil et la mise à jour Apple ID ; les trois conseils n’ont pas de date d’affichage. Le même profil est retrouvé dans **40 autres séquences** : il n’identifie pas un geste humain. PersonalAudio enregistre un **échec de préparation CloudKit**, erreur 134400, zéro objet traité. Les deux créations Santé concernent des mesures du 15 ; elles ne datent pas un déplacement ou une authentification du 16.

La recherche dans toutes les colonnes numériques prises en charge de **1 548 bases**, la reprise des préférences et le déchiffrement de deux artefacts supplémentaires d’usage des applications n’apportent aucun témoin indépendant d’interaction du 16. Les sources d’interaction/réseau s’arrêtant en juin et les historiques d’applications étant partiels, leur silence ne permet pas d’exclure une intervention. **Traitement automatique compatible ; intervention humaine non établie, absence d’intervention non démontrée.** Le [complément détaillé](investigations/20261110-tp03-intervention-humaine/compte-rendu.md) expose les contre-arguments, la couverture et les limites.

Le déchiffrement porte sur **4 632 objets généraux** et une sélection indépendante de **396 objets**, avec recouvrements contrôlés ; aucun échec de déchiffrement et aucun objet ordinaire référencé manquant. La sauvegarde porte des dates de **septembre 2025** et manque d’`Info.plist` : son identification repose sur `Manifest.plist/Lockdown`, et le journal d’acquisition manque. Les SMS et appels natifs conservés s’arrêtent en **juin 2024** ; leur absence en octobre ne prouve pas une inactivité. Six intervalles Santé du 28 ont des créations le 29 et ne datent pas des écritures avant ouverture. Le [rapport dédié](telephones/analyse-TP-03.md) détaille la couverture et les limites.

##### Recoupements entre téléphones et ordinateur

**Les 27 PDF Mini de L16B ont des équivalents binaires exacts dans TP-02 ET TP-03**, soit vingt contenus. Leurs chemins et SHA-512 figurent aussi dans le CSV désormais fourni. L’identité de contenu commune ne départage pas les appareils ; les **17 lastused TP-03 du 15 octobre**, dont 16 changements de statut concordants, favorisent en revanche l’historique de données conservé dans TP-03. Aucun `Birth` des 72 objets ne tombe dans cette séquence. Le regroupement des 27 fichiers sur OP-01 à **17:13:43 le 28**, en environ **658 ms**, est étayé ; l’origine des dates SI du 15 et le logiciel restent inconnus. La protection de classe C rendrait certaines nouvelles opérations locales incompatibles avec BFU après redémarrage, mais les conditions historiques nécessaires ne sont pas toutes établies. **Premier déverrouillage, transfert direct, auteur et scellé n° 3/n° 4 non démontrés.** Voir le [point 1.5](#15-parcours-des-pdf-associés-à-tp-03) et les sections 7.2 à 7.6 du [rapport TP-03](telephones/analyse-TP-03.md).

L’UDID TP-03 correspond exactement au nom du **fichier d’appairage Apple ancien d’OP-01** précédemment non attribué à un téléphone de mission. Cela relie cette relation de confiance conservée à TP-03, sans dater de connexion en octobre 2024. Les dates SI de juillet 2022 et FN/modification de décembre 2023 restent distinctes.

Enfin, les préférences Wi-Fi de TP-03 ne contiennent pas `ASUS_Z01RD`. Une MAC privée correspond à une fiche Freebox de **septembre 2025**, mais les trois identités iPhone nocturnes du **16–17 octobre 2024** restent sans correspondance dans les identifiants clients contrôlés des trois sauvegardes. Rotation et états perdus empêchent une exclusion matérielle absolue. Voir la [relecture transversale et les nouveaux contrôles](investigations/20261110-telephones/compte-rendu.md).

<a id="annexe-b3"></a>

#### B.3. Réseau et accès

Le rapprochement des identifiants réseau confirme que **`LAPTOP-RMCOB2VU` correspond à OP-01**.

En revanche, **`DESKTOP-ICPNCMD` reste non identifié**. Sa première activité conservée est datée du 16 octobre 2024 à 21 h 27 min 48 s. Aucun élément ne permet de l’attribuer à une personne ou à l’administration.

Trois identités « iPhone » se succèdent dans les traces des 16 et 17 octobre. Aucune ne correspond aux identifiants clients contrôlés des trois sauvegardes TP-01/02/03. Les changements d’adresse et les lacunes des historiques empêchent toutefois une exclusion matérielle absolue.

Une entrée auparavant inconnue correspond exactement à une configuration de caméra Xiaomi de modèle `mxiang.camera.mwc11` dans TP-02. Le rapprochement d’une seconde caméra Xiaomi reste partiel, car ses identifiants ne concordent pas exactement. Ces modèles ne sont pas reliés avec certitude aux trois cartes SD ; aucun accès aux images n’est reconstitué.

Deux **tentatives échouées d’accès au partage de fichiers d’OP-01**, le 26 mars 2024 à 15 h 20 min 36 s et 15 h 21 min 12 s, proviennent d’une adresse locale associée dans l’inventaire Freebox à `LAPTOP-205Q5H9C`. Ce rapprochement est plausible, sans attribution certaine à cet appareil au moment exact des tentatives. Aucun accès réussi n’en découle.

**Aucun accès distant non autorisé n’a été démontré.** La Freebox fournit des traces de présence réseau, mais pas un historique complet des fichiers lus, des volumes transférés ou des sessions d’administration depuis 2021/2022. L’accès distant activé en septembre 2026 à la demande du prestataire relève de la mission autorisée ; il ne décrit pas la situation d’octobre 2024.

<a id="annexe-b4"></a>

#### B.4. Caméras et cartes SD

**Les caméras n’ont jamais été placées sous scellés.** Leurs enregistrements après la perquisition ne constituent donc pas, par eux-mêmes, une anomalie.

##### SD-01 — Chambre

La carte conserve **674 vidéos**, dont **37 du 15 octobre 2024**. Certaines prolongent les enregistrements de cette journée jusqu’à environ 22 h 46 selon la caméra. Aucun indice spécifique de réinitialisation le 15 octobre n’a été identifié.

Aucune vidéo supprimée supplémentaire n’a été récupérée. Trois fichiers temporaires supprimés sont très fortement reliés à la fabrication d’une vidéo encore présente ; ils ne représentent pas trois enregistrements distincts disparus.

Des anomalies de lecture existent. Deux vidéos nommées du **21 février et du 1er mars 2024** portent des dates de fichiers de janvier 2000 alors que les images contrôlées affichent 2024. La vidéo du 1er mars est partiellement endommagée.

##### SD-02 — Terrasse

**Onze vidéos supprimées ont été récupérées entièrement**, représentant environ 44 minutes et 36 secondes. **La fin d’une douzième vidéo a été récupérée**, pour environ 2 minutes et 6 secondes. Ces vidéos, situées au **5 novembre 2024** selon la caméra, passent les contrôles de lecture.

Un **enregistrement temporaire du 12 novembre a été restauré partiellement**, sur environ 69 secondes. Il était encore présent mais non terminé : **il ne s’agit pas d’une vidéo supprimée**.

La carte presque pleine comporte de nombreuses traces de suppression et de réutilisation des anciens emplacements. L’ensemble est fortement compatible avec un **remplacement automatique des anciennes vidéos lorsque le stockage est plein**, sans établir le mécanisme de chaque suppression.

Aucune vidéo du 15 octobre ou de février/mars n’a été récupérée. Un ancien dossier porte une date de janvier 2000 ; un autre fichier possède un nom de date impossible alors que ses images indiquent le 21 octobre 2024. Ces anomalies ne démontrent ni réinitialisation ni effacement intentionnel.

##### SD-03 — Salon

Le fichier du 15 octobre concerné est `20241015_132800_10_0277.mp4` (copie extraite précédemment référencée sous le préfixe `714049800_`).

La carte conserve **65 vidéos du 15 octobre 2024**, parmi 2 431 vidéos disponibles. La dernière vidéo conservée sur SD-03 pour cette journée commence à **13 h 28 selon l’horloge de la caméra**. Ses informations de fichier indiquent janvier 2000, tandis que les images contrôlées affichent le 15 octobre 2024.

Ce fichier présente une anomalie de production : la piste sonore dure **277,760 secondes**, contre **266,171 secondes** pour la piste vidéo, soit **11,589 secondes de plus**. Cet excédent est exceptionnel dans les populations comparées des trois cartes. Le son correspondant existe, peut être décodé et contient un signal non nul ; son contenu n’a pas été interprété dans les contrôles cités.

La **dernière image techniquement décodée se situe vers 13 h 32 min 26 s**, selon le début et les temps de lecture du fichier. Un aperçu effectivement examiné près de cette fin affiche également 13 h 32 min 26 s. Une autre erreur affecte la lecture d’image vers **13 h 30 min 05 s**, selon le même calcul ; des images subsistent ensuite.

**Ces anomalies ne permettent pas de déterminer si la caméra a été arrêtée, redémarrée ou manipulée à ce moment.** Le supplément sonore n’a pas été interprété comme preuve d’une action ou d’un arrêt précis. L’écart des durées ne démontre pas une captation du son exactement 11,589 secondes après la dernière image en heure réelle.

**Aucune vidéo référencée ne porte une date du 16 au 28 octobre. Les fichiers disponibles reprennent le 29 octobre à 17 h 59 min 18 s**, selon la caméra. Cette lacune mérite l’attention, mais sa cause reste indéterminée : arrêt, absence de déclenchement ou perte d’enregistrements ne peuvent pas être départagés.

Aucune vidéo supprimée distincte et complète n’a été récupérée. Un fragment d’environ quatre secondes a toutefois été restauré à la fin d’une vidéo déjà présente mais endommagée du 29 février ; ce résultat est distinct des suppressions.

**Explications techniques possibles et niveau d’appui.** La même erreur de compteur audio est retrouvée dans onze vidéos de SD-01 et SD-03, dès novembre 2023. Dans le fichier du 15 octobre, le dernier compteur contient 2 163 éléments alors que sept restent attendus. Cette répétition étaye fortement un mécanisme récurrent de finalisation ou de reconstruction défaillante, sans identifier son déclencheur ni démontrer une cause unique pour toutes les anomalies.

| Scénario | Ce qu’il pourrait expliquer | Limite des éléments disponibles |
|---|---|---|
| **Défaut logiciel de finalisation ou de récupération** | Erreur répétée lors de la clôture du MP4 ou de la reconstruction de ses tables de lecture. | Mécanisme le mieux étayé pour le défaut structurel ; logiciel exact, séquence et déclencheur non établis. |
| **Interruption d’alimentation ou redémarrage** | Enregistrement interrompu, puis récupération du fichier avec une date par défaut si le mécanisme d’horodatage n’est pas correctement initialisé. | Scénario compatible, non observé en fonctionnement ; aucune coupure ni heure de redémarrage démontrée. Aucun retour aux réglages d’usine n’en est déduit. |
| **Problème de production vidéo, d’écriture ou de gestion des temps** | Arrêt de production des images avant l’audio, données ou index vidéo manquants, ou durées de pistes mal calculées. | Les deux pistes se terminent différemment dans le fichier acquis ; la cause de cette différence n’est pas identifiée. |
| **Récupération ou modification ultérieure** | Un traitement après l’enregistrement pourrait produire un état comparable des données, index et dates. | Aucune version antérieure authentifiée ni trace d’outil ou d’auteur n’établit une modification précise de cette vidéo. |

**Un mécanisme technique ne détermine pas l’origine de l’événement.** Une interruption pourrait être accidentelle ou provoquée par une personne, par exemple par un débranchement. Le défaut récurrent ne permet pas d’exclure ce second cas ; aucune trace positive ne démontre toutefois une intervention humaine à son origine. La dernière image décodée ne constitue pas une heure certaine d’arrêt de la caméra.

**La lacune suivante reste à expliquer séparément.** Arrêt de la caméra ou de l’enregistrement, absence de déclenchement, problème de stockage, perte ou suppression de fichiers sans trace survivante restent possibles. Aucun lien causal entre cette lacune et le défaut du dernier clip n’est établi. Les vidéos de SD-01 conservées plus tard le 15 octobre ne soutiennent pas un arrêt prolongé simultané de toutes les caméras. Voir les [contrôles et comparaisons détaillés](cartes_sd/analyse-cartes_sd-transversale.md).

##### Conclusions communes

**Onze vidéos provenant des caméras de la chambre et du salon présentent exactement le même défaut dans leur structure informatique, accompagné de dates incohérentes de janvier 2000.** Ce défaut, observé dès novembre 2023, semble lié à la manière dont les caméras terminent ou récupèrent leurs enregistrements.

Ces concordances étayent fortement le caractère récurrent du défaut, sans en identifier la cause exacte.

Une conversion horaire peut expliquer comment une date du début de janvier 2000 s’affiche au 31 décembre 1999, sans expliquer pourquoi cette date a été enregistrée. L’affichage observé par la cliente reste inconnu. Le nouveau mail précise désormais **février 2024 et la caméra de la chambre** ; l’interface et le fichier à l’origine de l’affichage restent non établis.

**Une réinitialisation en février ou le 15 octobre n’a pas été démontrée. Aucun formatage intentionnel ni effacement malveillant n’a été établi.** Les fichiers auxiliaires Windows datés du 12 novembre documentent séparément un traitement possible des cartes sur ordinateur ; ils ne démontrent pas une modification des vidéos. Le poste concerné n’a pas été identifié, y compris après les recherches complémentaires sur OP-01.

##### Couverture des enregistrements et fonctionnement continu déclaré

La cliente situe l’installation après mars 2023. Les noms vidéo conservés de la chambre commencent en décembre 2023, ceux du salon en novembre 2023 ; ils ne couvrent pas continûment cette période. La terrasse conserve principalement novembre 2024 et un clip daté du 21 octobre par ses images. Les données LSC ne restituent pas une chronologie complète des partages, réappairages ou changements de compte.

La terrasse est déclarée fonctionner **24 h/24**. Le nouveau calcul de l’union des intervalles des MP4 actifs à nom datable couvre **48,892 à 64,937 %** d’une journée sur les journées intérieures du **6 au 11 novembre**. Ce sont des lacunes du **corpus conservé**, pas une mesure certaine du temps d’arrêt de la caméra. Le calcul exclut les supprimés récupérés et le temporaire ; les durées restent nominales. Les mécanismes d’enregistrement, pertes, écrasements, interruptions ou suppressions restent à départager. La réutilisation circulaire des anciennes données est distincte d’une coupure du flux. **Aucun effacement ciblé le 15 ni intervention d’une personne sur la terrasse n’est démontré.**

<a id="annexe-c"></a>

### Annexe C — Provenance, couverture et limites

- **Auteur inconnu :** aucun compte, nom d’appareil ou horaire ne permet d’identifier la personne ayant effectué les opérations.
- **Historiques incomplets :** les traces conservées ne recensent pas tous les accès distants ni toutes les opérations anciennes. Des enregistrements ont pu être remplacés, particulièrement sur la terrasse.
- **Horloges non comparées à une référence commune :** une proximité entre heure caméra, heure informatique et heure déclarée ne prouve pas un événement simultané.
- **Signalements de réinitialisation non authentifiés :** l’interface, le message et les fichiers à l’origine des deux observations de la cliente restent inconnus.
- **Inventaire et pièces absentes :** le CD d’origine reste indisponible, mais les **1 555 lignes du CSV fourni ont été comparées à l’image : 1 552 SHA-512 identiques et 3 divergents, sans chemin absent** ; les 27 PDF Mini font partie des concordances. Voir le point 1.2. Le ZIP final, le fichier de rejets et le support de destination restent à obtenir ou authentifier ; le CSV seul ne certifie pas la conservation actuelle des fichiers. Le journal de sauvegarde Mac manque pour la provenance de TP-02 ; les rapports TP-01 et TP-03 exposent les limites propres à leurs sauvegardes, complétées pour TP-03 les 14 et 16 novembre.

Le rapport Freebox relève aussi une divergence non résolue pour une première activité du **4 mars 2024** entre une ancienne retranscription et les données exportées. Les heures corrigées à partir des données brutes ont été privilégiées ; cette entrée n’est pas utilisée dans la chronologie des faits du 15 au 28 octobre.

#### Sauvegardes et historique documentaire

La mission portait sur l’utilisation du matériel pendant les périodes signalées, les éventuels accès par des tiers, les copies, transferts ou suppressions de données, les téléphones et le réseau, ainsi que les enregistrements de caméra et les anomalies de dates ou réinitialisations évoquées par Mme Sadedine.

Le périmètre effectivement analysé comprend l’ordinateur **OP-01** (portable ASUS), les sauvegardes des téléphones **TP-01** (iPhone 13), **TP-02** et **TP-03** (iPhone 13 mini), la **Freebox Révolution** et trois cartes de caméra : **SD-01 — chambre**, **SD-02 — terrasse**, **SD-03 — salon**.

**TP-01 a fait l’objet d’un complément le 10 novembre 2026**, à partir de sa sauvegarde du 9 novembre, identifiée par la série Q13QT4F164. Son indisponibilité lors des campagnes antérieures ne décrit plus le périmètre actuel. **TP-03 est également analysé le 10 novembre**, sur une sauvegarde chiffrée portant des dates de septembre 2025 et identifiée par la série Y4Q9KGHG26. Sa remise matérielle, postérieure à la remise initiale du 7 octobre 2026, rectifiée par le document du 17 novembre, est confirmée par le prestataire.

Les sources techniques gardent leurs dates et contrôles propres. La [lecture du PV](investigations/20261108-analyse-pv/compte-rendu.md) et le [complément consolidé des 8–9 novembre](investigations/20261108-complement-pv/compte-rendu.md) distinguent les mentions procédurales et les observations techniques. La note vidéo documente le constat de visionnage ; le courrier de la cliente explique les SMS. Le journal Mac manque encore pour la provenance de TP-02. Les contrôles de contenu du 16 novembre et la confirmation S3 du 17 sont distincts de la révision rédactionnelle du 18.

<a id="annexe-d"></a>

### Annexe D — Conservation, traçabilité et remise en 2026

**Cette section concerne la conservation et la livraison des données en 2026. Elle ne sert pas à interpréter les événements de 2024.**

L’ensemble des données extraites et du dossier de travail est conservé sur **OVHcloud S3**. **Le prestataire confirme le 17 novembre 2026 que le stockage S3 est complet.** Cette actualisation remplace l’état de conservation mentionné dans la version précédente du rapport.

**Mme Sadedine dispose d’un accès lui permettant de télécharger les données depuis le stockage S3 au moyen d’une clé d’accès.** Les identifiants de connexion sont communiqués séparément du rapport et du bordereau. L’espace de destination est le bucket `sadedine-2026`, sous le préfixe `SADEDINE-2026/`. La [notice de téléchargement](remise-documents/notice-telechargement-s3.md) décrit les modalités d’accès et de récupération.

Le [bordereau de mise à disposition des données](remise-documents/bordereau-mise-a-disposition-donnees-20261117.md) décrit le contenu accessible et les empreintes de contrôle de référence. **Aucun disque dur n’a été remis à la cliente à la date de cette actualisation.** La copie et la remise sur un disque dur neuf fourni par elle feront l’objet d’un bordereau distinct lors de cette remise. La conservation sur S3 se poursuit selon la durée prévue au devis.

#### Rectification de la date de remise des matériels

**La date de remise effective à retenir est le 7 octobre 2026**, conformément aux notes d’intervention, qui indiquent **16 h 15**. La mention du 6 octobre 2026 portée sur l’attestation d’origine est rectifiée par le [rectificatif du 17 novembre 2026](remise-documents/rectificatif-attestation-remise-20261117.md), à conserver avec celle-ci. L’attestation d’origine et ses signatures ne sont pas réécrites. TP-03, indiqué comme non remis lors de cette remise initiale, reste hors du périmètre de cette correction de date.

Les horaires notés pour l’acquisition d’OP-01 en 2026 ne sont pas entièrement raccordés aux horaires automatiques. Cet écart concerne la documentation de l’acquisition et ne permet pas de conclure à une manipulation en 2024.

<a id="annexe-e"></a>

### Annexe E — Glossaire

| Terme | Sens dans ce rapport |
|---|---|
| **PV** | Procès-verbal décrivant les opérations de procédure. |
| **L16B** | Nom du dossier de regroupement laissé sur l’ordinateur ; son contenu n’est pas assimilé à la copie finale saisie. |
| **Sauvegarde logique** | Copie des données accessibles par le mécanisme de sauvegarde, qui ne décrit pas à elle seule toutes les opérations physiques du téléphone. |
| **Synchronisation / restauration** | Mise en commun de données entre appareils ou réimportation d’un état sauvegardé ; des dates anciennes peuvent ainsi être conservées. |
| **Métadonnée / horodatage** | Information descriptive ou date associée à une donnée ; sa signification dépend du logiciel qui l’a produite. |
| **Journal** | Enregistrement d’événements par un système ; sa couverture peut être incomplète. |
| **Empreinte SHA-256** | Valeur calculée sur un fichier pour comparer son contenu exact avec un autre ; elle ne prouve pas à elle seule sa provenance ou la date d’une copie. |
| **PST / EML / MBOX** | Formats d’archives ou de fichiers de messagerie. |
| **MAC / BSSID** | Identifiants réseau utilisés pour des interfaces ou points d’accès ; leur présence ne désigne pas une personne. |
| **UDID / IMEI / numéro de série** | Identifiants d’appareil utilisés pour rapprocher les données et le matériel, selon leur disponibilité. |
| **MFT, NTFS SI/FN / FAT** | Structures et métadonnées des systèmes de fichiers ; certaines dates peuvent être conservées lors de copies. |
| **Uptime** | Ici, durée présentée comme temps d’éveil depuis le démarrage ; elle ne suffit pas à dater l’allumage physique. |
| **SIFT** | Environnement d’analyse utilisé pour les contrôles techniques cités. |
| **OCR** | Reconnaissance automatique du texte dans des images ou documents numérisés ; une recherche incomplète ne prouve pas l’absence de contenu. |

<a id="annexe-f"></a>

### Annexe F — Sources et rapports de référence

#### Pièces de cadrage et de procédure

- [Demandes initiales de Mme Sadedine](docs/mail.txt), [précisions complémentaires](docs/mail-2.txt) et [attestation de remise](remise-documents/attestation-de-remise.md).
- [PV de saisie](docs/PV%20DE%20SAISIE.pdf) et [lecture du PV du 8 novembre](investigations/20261108-analyse-pv/compte-rendu.md).

#### Rapports par équipement

- [Ordinateur OP-01](ordinateur/analyse-ordinateur.md), [opérations du 28 octobre](ordinateur/recherche-OP-01/operations-28oct/compte-rendu.md) et [limites de datation du réseau ASUS_Z01RD](ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/datation.md).
- Compléments OP-01 du **13 novembre 2026** : [Sage 50 et connexions réseau](ordinateur/rapport-complementaire-OP-01-Sage50-reseaux-28oct2024.md), [antériorité du Samsung et sorties ALMU](ordinateur/rapport-complementaire-OP-01-Samsung-ALMU-28oct2024.md), [registre identifiant le Samsung](ordinateur/recherche-OP-01/samsung-almu-20261113/resultats/samsung-registry.json), [chronologie réseau](ordinateur/recherche-OP-01/sage-reseaux-20261113/resultats/chronologie-reseau-28oct.json) et [journal natif Sage](ordinateur/recherche-OP-01/sage-reseaux-20261113/resultats/sage-log-day.json).
- Contrôle complémentaire Sage du **13 novembre 2026** : [dossiers société, SIRET et mode d’authentification](ordinateur/recherche-OP-01/sage-dossiers-auth-20261113-swqgba2s/compte-rendu.md), [métadonnées web](ordinateur/recherche-OP-01/sage-dossiers-auth-20261113-swqgba2s/webview-auth-metadata.json), [méthode](ordinateur/recherche-OP-01/sage-dossiers-auth-20261113-swqgba2s/method.json) et [contrôles d’intégrité](ordinateur/recherche-OP-01/sage-dossiers-auth-20261113-swqgba2s/final-checks.json).
- Téléphones [TP-01](telephones/analyse-TP-01.md), [TP-02](telephones/analyse-TP-02.md), [TP-03](telephones/analyse-TP-03.md) ; [Freebox](freebox/analyse-freebox.md).
- Cartes [SD-01 — chambre](cartes_sd/analyse-cartes_sd-SD-01.md), [SD-02 — terrasse](cartes_sd/analyse-cartes_sd-SD-02.md), [SD-03 — salon](cartes_sd/analyse-cartes_sd-SD-03.md) et [comparaison transversale](cartes_sd/analyse-cartes_sd-transversale.md).

#### Conservation, opérations et correspondances

- [Compte rendu général et compléments du 17 octobre](investigations/20261017-recroisements/compte-rendu.md) et [retour de la cliente et contre-lectures du 19 octobre](investigations/20261019-retour-cliente/compte-rendu.md).
- [Complément technique du 8 novembre](investigations/20261108-complement-pv/compte-rendu.md) et [reprise SIFT du 9 novembre](investigations/20261108-complement-pv/compte-rendu.md).
- [Contrôle de L16B et des catégories du PV](investigations/20261109-controle-l16b-photos/compte-rendu.md).
- [Recherche élargie des correspondances](investigations/20261109-correspondances-elargies/compte-rendu.md), [messages sélectionnés](investigations/20261109-correspondances-elargies/tableau-messages.md), [documents](investigations/20261109-correspondances-elargies/tableau-documents.md) et [fiche du PDF Bourarach](investigations/20261109-clarification-correspondances/fiche-bourarach.md).

- [Rapport du 16 novembre : correspondances classées selon la concordance SHA-512](ordinateur/recherche-OP-01/correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md), [comparaison aux SHA-512 du CSV et empreintes complètes](ordinateur/recherche-OP-01/extraction-messageries-20261116/comparaison-inventaire-SHA512-20261116.md), [résultats structurés](ordinateur/recherche-OP-01/extraction-messageries-20261116/comparaison-inventaire-SHA512-20261116.json) et [validation des 5 875 en-têtes PST](ordinateur/recherche-OP-01/correspondances-avocats-20261116/validation-nouveaux-decodages.json). Les fichiers concordants et le PST 93300 divergent y sont séparés.

- Contrôle exhaustif du **16 novembre 2026** : [rapport Markdown des 1 555 fichiers et des 3 110 SHA-512 intégraux](ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/rapport-comparaison-SHA512-exhaustive-1555-fichiers.md), [synthèse des concordances et divergences, écarts de chemins](ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/rapport-comparaison-L16B-inventaire.md), [tableau CSV](ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/comparaison-SHA512-tous-les-fichiers.csv) et [résultats structurés avec montage en lecture seule](ordinateur/recherche-OP-01/comparaison-L16B-inventaire-20261116/resultats-comparaison-L16B-inventaire.json).

#### Téléphones, hypothèses concurrentes et horloges

- [Relecture transversale du 10 novembre](investigations/20261110-telephones/compte-rendu.md), [approfondissement TP-03](investigations/20261110-tp03-intervention-humaine/compte-rendu.md) et [revue contradictoire des interventions avant ouverture](investigations/20261110-revue-intervention-scelles/compte-rendu.md).
- [Contrôle des SMS marqués lus](investigations/20261109-sms-lecture/compte-rendu.md) et [note documentaire sur l’uptime](investigations/20261109-documentation-uptime/note-technique.md).
- [Inventaire CSV transmis](inventaire-DNEF/documents-recus/Inventaire_saddedine.csv), [réponse Q1 et 17 rapprochements TP-03](inventaire-DNEF/rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md), [investigations B à E](inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md) et [recherche de récupération du ZIP et du fichier de rejets](inventaire-DNEF/rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md).

<div style="break-before: page;"></div>

<a id="annexe-g"></a>

### Annexe G — Inventaire du matériel

Cet inventaire reprend les équipements et identifiants de l’annexe 1 de l’[attestation de remise de matériels](remise-documents/attestation-de-remise.md), portant la date du **6 octobre 2026**, rectifiée au **7 octobre 2026** par le [rectificatif du 17 novembre](remise-documents/rectificatif-attestation-remise-20261117.md), et tient compte de la remise ultérieure de TP-03 confirmée par le prestataire.

| Repère et matériel | Caractéristiques et identifiants transcrits | Remise du matériel |
|---|---|---|
| **OP-01** — Ordinateur portable ASUS | Modèle : **UX333F NOTEBOOK PC** ; série : `KAN0CV116290436` ; système : Windows 11 version 23H2 x64. | Remis au prestataire. |
| **TP-01** — Apple iPhone 13 vert | Série : `Q13QT4F164` ; modèle : `MNGK3ZD/A` ; IMEI : `35 876346 861150 5`. | Remis au prestataire. |
| **TP-02** — Apple iPhone 13 mini rouge | Série : `F5466LV9V7` ; modèle : `MLK83KH/A` ; IMEI 1 : `35292959671648 4` ; IMEI 2 : `35292959 723940 3`. | Remis au prestataire. |
| **TP-03** — Apple iPhone 13 mini rouge | Série : `Y4Q9KGHG26` ; modèle : `MLK83F/A` ; champ « IMEI » : `8933130002078820373`. | Remis ultérieurement au prestataire, selon sa confirmation. |
| **SD-01** — Carte SD | Marque transcrite : **ScanDisk** ; capacité : **32 Go** ; numéro de série non renseigné. | Inscrite à l’inventaire des matériels remis. |
| **SD-02** — Carte SD | Marque transcrite : **ScanDisk** ; capacité : **32 Go** ; numéro de série non renseigné. | Inscrite à l’inventaire des matériels remis. |
| **SD-03** — Carte SD | Marque transcrite : **ScanDisk** ; capacité : **32 Go** ; numéro de série non renseigné. | Inscrite à l’inventaire des matériels remis. |

La Freebox et les caméras ne sont pas répertoriées comme matériels remis dans cette attestation ; aucun identifiant officiel de remise ne leur est donc attribué dans cet inventaire.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe DOnnat — Donnat Dev
