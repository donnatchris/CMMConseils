# Rapport final d’investigation informatique — Mme Malika Sadedine

**Référence :** SADEDINE-2026  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Destinataire :** Me Delphine Ravon, avocate de Mme Malika Sadedine  
**Date du rapport :** 19 octobre 2026 ; réorganisation rédactionnelle le 12 novembre 2026  
**Nature :** investigation informatique indépendante réalisée à la demande de la cliente, sans désignation comme expert judiciaire.

## 1. Points suspects et questions prioritaires pour l’avocate

**Trois questions dominent : les téléphones ont-ils été utilisés pendant la fermeture des scellés ? Quelles données ont été effectivement emportées, notamment parmi les échanges avec des avocats ? Quel rôle les différents supports USB ont-ils joué ?** Les autres points ci-dessous concernent la conservation des appareils, les opérations après ouverture et une vidéo du jour de la perquisition.

L’appréciation juridique appartient à l’avocate et au juge. Les traitements automatiques sans signe distinctif de geste humain sont exposés plus loin et ne sont pas comptés ici comme des suspicions supplémentaires.

**Réserve concernant l’ordinateur OP-01.** Aucune trace d’extraction n’a été retrouvée sur l’ordinateur pour la période entre la saisie et l’ouverture des scellés. Cette absence ne permet pas de conclure définitivement à l’absence de copie des données. Une acquisition hors ligne, par exemple en reliant le support de stockage à un autre équipement au moyen d’un bloqueur en écriture, pourrait permettre d’en copier les données sans démarrer Windows ni modifier le support source, et donc sans y laisser les traces recherchées. Cette possibilité technique n’est ni démontrée ni exclue par les éléments disponibles.

### 1.1. TP-02 : indices d’une connexion Wi-Fi volontaire pendant la conservation

Constat. Les données de TP-02 conservent une séquence de configuration et de connexion au réseau ASUS_Z01RD le 17 octobre 2024 vers 17 h 25. La mention d’un ajout depuis les réglages Wi-Fi, l’indication de connexion par utilisateur, la génération d’une adresse MAC privée puis l’association au réseau en environ 4,7 secondes forment un ensemble cohérent en faveur d’une configuration volontaire à l’origine de cette connexion. Une simple synchronisation de mot de passe explique moins bien cette séquence complète.

L’historique contient également 53 appels du 15 au 26 octobre, dont 22 marqués sortants sur huit jours ; 19 sortants ont une durée positive. Ces appels peuvent être transportés par synchronisation ou restauration : ils ne permettent pas, à eux seuls, d’établir une utilisation de TP-02 pendant sa conservation.

Question. Une personne a-t-elle configuré et connecté TP-02 à ce réseau Wi-Fi avant l’ouverture de son scellé ?

Limite. La séquence Wi-Fi constitue un indice plus solide d’une intervention humaine que la seule présence des appels. Son attribution au téléphone physique TP-02 le 17 octobre reste toutefois à confirmer : une restauration complète pourrait avoir importé un état produit ailleurs. Aucune restauration expliquant cette séquence n’a été identifiée, sans que cette possibilité puisse être exclue. Aucun auteur ni déverrouillage de TP-02 n’est établi.

À vérifier. Journaux du réseau ASUS, historique des migrations ou restaurations et relevés opérateur avec identifiants matériels s’ils existent. Voir la section 4 et l’annexe B.2.

### 1.2. Téléphones rallumés avant leur mise sous scellés

Le prestataire indique, le 12 novembre 2026, que son visionnage des vidéos du salon du **15 octobre 2024 vers 13 h 25** montre **une agente de l’administration fiscale rallumant les téléphones précédemment éteints**. La mise sous scellés est consignée après 14 h 19.

**Question.** Les téléphones ont-ils été placés sous scellés encore allumés, et dans quelles conditions de conservation ?

**Limite.** Ce scénario est **compatible avec les éléments techniques**. Le diagnostic de TP-02 du 28 octobre ne prouve pas qu’il était éteint avant ouverture. En revanche, aucune continuité d’alimentation jusqu’au 28 n’est établie. La séquence de 13 h 25 n’a pas été revérifiée dans cette révision ; le contrôle antérieur portait sur des images échantillonnées d’un clip commençant à 13 h 28.

**À vérifier.** Extinction éventuelle avant fermeture, alimentation, isolement réseau et conditions de stockage. Un téléphone allumé peut travailler automatiquement ; cela ne suffit pas à prouver un geste humain sous scellé.

### 1.3. Différences d’emballage et de marquage

**Constat.** Le PV affirme l’intégrité des scellés à l’ouverture ; les observations annexées de la cliente décrivent des différences d’emballage et de marquage.

**Question.** La continuité des scellés entre le 15 et le 28 octobre peut-elle être documentée ?

**Limite.** Cette divergence ne démontre pas une ouverture clandestine. Les deux iPhone Mini ne sont pas encore rattachés avec certitude aux scellés n° 3 et n° 4.

**À vérifier.** Photographies, emballages, numéros, bordereaux de prise en charge et interventions consignées.

### 1.4. Données emportées et correspondances avec des avocats

**Constat.** L16B est le dossier de regroupement constitué par les agents de l’administration fiscale sur l’ordinateur de Mme Sadedine lors des opérations du 28 octobre 2024. Il rassemble des documents et données provenant notamment de l’ordinateur, de messageries, de services en ligne et de téléphones. Le PV décrit ensuite un filtrage et une copie finale sur un support de l’administration ; il précise que L16B est laissé sur l’ordinateur à titre informatif, avec l’accord de Mme Sadedine.

Des échanges avec des avocats sont effectivement présents dans ce dossier : notamment Negrevergne, Pascoët, Khallouki, Fakiroff / Roosevelt Avocats, Wahrheit et Guillou.

**Question.** Ces échanges ont-ils été exclus lors du filtrage précédant la copie emportée par l’administration ? Les documents finalement retenus entraient-ils dans le périmètre autorisé ? Ont-ils été utilisés fiscalement ?

**Limite.** Le dossier L16B laissé par les agents ne constitue pas une copie certifiée des fichiers finalement emportés. La présence de correspondances dans ce dossier ne prouve donc ni leur saisie définitive, ni leur lecture par les agents, ni leur utilisation fiscale. Le caractère protégé et le lien avocat-client doivent être examinés pour chaque échange.

**À vérifier.** Comparer le contenu de L16B avec l’inventaire final et les fichiers effectivement saisis, à l’aide de leurs empreintes de contrôle. Examiner également la liste des rejets, les critères de filtrage, l’ordonnance et les éventuels actes fiscaux citant ces documents. Voir la section 5 et l’annexe B.1.

### 1.5. Une clé de destination décrite, trois périphériques Kingston relevés

**Constat.** Le PV décrit une copie sur une clé USB vierge de l’administration, préalablement formatée. Les journaux de l’ordinateur enregistrent **trois identifiants distincts de périphériques Kingston DataTraveler le 28 octobre**, vers **16 h 27, 17 h 00 et 17 h 14**, après ouverture.

**Question.** Quel était le rôle de chacun et sur quel support les fichiers saisis ont-ils été copiés ?

**Limite.** Trois identifiants ne prouvent pas trois copies ou trois destinataires. Certains supports ont pu servir aux outils ou à des étapes intermédiaires. Le formatage seul n’explique pas trois identifiants matériels différents.

**À vérifier.** Identification des supports, journaux des outils, archive finale, inventaire et rejets. Le rattachement physique de la clé décrite au PV reste à effectuer.

### 1.6. Suppressions et opérations après ouverture

**Constat.** Dix mises à la corbeille sont documentées sur l’ordinateur le 28 octobre, sans description individualisée retrouvée au PV. TP-02 conserve trois SMS de validation/réinitialisation marqués lus et une séquence compatible avec une capture d’écran ; TP-01 conserve deux lignes WhatsApp sortantes.

**Question.** Qui a effectué ces opérations, dans quel but, et sur quelles données ou quels comptes ?

**Limite.** Les fichiers supprimés ont été récupérés ; aucune destruction malveillante n’est démontrée. L’origine physique des opérations téléphoniques et l’utilisation des codes SMS ne sont pas établies. Ces traces sont postérieures à l’ouverture.

**À vérifier.** Notes des opérateurs, outils employés et distinction entre données sources et copies de travail.

### 1.7. Vidéo anormale du jour de la perquisition

**Constat.** La dernière vidéo conservée du salon le **15 octobre**, commencée à **13 h 28**, présente une date informatique incohérente et un décalage de durée entre son et image. Les dernières images décodées se situent vers **13 h 32 min 26 s**, puis aucun fichier référencé n’est daté du 16 au 28.

**Question.** Qu’est-ce qui explique cette anomalie et la lacune qui suit ?

**Limite.** **Une manipulation volontaire ou une falsification n’est pas établie.** Le même défaut existe sur des vidéos antérieures, dès 2023, ce qui soutient un défaut récurrent de finalisation ou de récupération des fichiers. Son déclencheur reste inconnu : une interruption d’alimentation ou un redémarrage sont possibles, sans être démontrés. Une interruption pourrait elle-même être accidentelle ou résulter d’un geste humain. Le défaut du fichier n’explique pas à lui seul la lacune qui suit. Les caméras n’étaient pas sous scellés.

**À vérifier.** Autres copies, journaux et conditions de fonctionnement de la caméra, s’ils sont disponibles. Voir la section 6 et l’annexe B.4.

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

Le rapport distingue **les constats techniques**, issus des données examinées, **les mentions du procès-verbal (PV)** et **les observations rapportées** par la cliente ou le prestataire. Une hypothèse est une explication compatible avec ces éléments, qui reste à vérifier.

Une sauvegarde est une copie de données du téléphone, parfois réalisée longtemps après les faits. Elle peut contenir des informations venues d’un autre appareil ou d’un service en ligne. Une date présente dans cette copie ne prouve donc pas toujours une opération sur le téléphone physique à cet instant. De même, un nom de compte ou de réseau n’identifie pas une personne.

Cette version présente l’état des investigations réalisées jusqu’au 10 novembre 2026 et l’observation de visionnage communiquée le 12 novembre. La réorganisation est rédactionnelle : elle n’ajoute ni acquisition ni nouveau visionnage indépendant. Les précisions de méthode, les limites et les références sont réunies dans les annexes de la section 8.

## 3. Les dates essentielles

Les heures informatiques sont présentées en heure de Paris. Les heures affichées par les caméras n’ont pas été comparées à une référence commune : leur rapprochement avec les autres horaires reste prudent.

| Moment | Événement et provenance | Portée |
|---|---|---|
| **15 octobre, vers 10 h 43–10 h 53** | Fonctionnement puis veille prolongée d’OP-01 — traces Windows. | Aucune activité Windows intermédiaire corroborée jusqu’au 28. |
| **15 octobre, vers 13 h 25** | Rallumage des téléphones — observation de visionnage rapportée par le prestataire. | État lors de la fermeture non certifié. |
| **15 octobre, vers 13 h 30** | Perte d’accès aux téléphones — déclaration de la cliente. | Ce n’est pas l’heure de scellement. |
| **15 octobre, vers 13 h 32 min 26 s** | Dernières images conservées du salon — horloge caméra. | Ce n’est pas une heure certaine d’arrêt de la caméra. |
| **15 octobre, après 14 h 19** | Mise sous scellés — PV. | Heure de fermeture individuelle inconnue. |
| **15–26 octobre ; 17 octobre vers 17 h 25** | Historique d’appels et séquence Wi-Fi — données TP-02. | Origine physique à établir. |
| **28 octobre, 10 h 22 puis 10 h 41** | Arrivée de la cliente, puis ouverture du PC — PV. | Windows reprend à 10 h 41 min 56 s. |
| **28 octobre, 11 h 30** | Ouverture des scellés des téléphones — PV. | Les opérations suivantes sont après ouverture. |
| **28 octobre, journée** | Regroupements, suppressions et périphériques USB — traces d’OP-01 ; copies décrites au PV. | Contenu final emporté non vérifié. |
| **28 octobre, 19 h 20 ; 29 octobre, vers 17 h 59** | Clôture du PV et restitution déclarée ; reprise des fichiers du salon le lendemain. | Pas d’heure individuelle de remise ; heure caméra pour la reprise vidéo. |

La chronologie complète, incluant les traitements système et les événements après restitution, figure en annexe A.

## 4. Les appareils pendant la fermeture des scellés

**Une intervention humaine reste possible, surtout au regard des données de TP-02, mais elle n’est démontrée sur aucun appareil physique identifié pendant la fermeture de son scellé.** Un fonctionnement automatique, une intervention humaine et une ouverture matérielle d’emballage sont des faits différents.

### TP-02 : deux pistes à départager

Le réseau `ASUS_Z01RD` apparaît dans une séquence du 17 octobre qui associe ajout du réseau, indication de connexion par utilisateur, création d’une adresse réseau puis connexion. Cet ensemble est plus informatif qu’une date isolée. Il reste compatible avec une configuration par une personne, sans preuve de déverrouillage du téléphone. Les données peuvent aussi provenir d’un état complet importé lors d’une migration ou restauration ; cette explication n’est ni établie ni exclue.

Les 53 appels conservés comprennent 22 sortants, dont 19 à durée positive. Ils sont répartis sur plusieurs jours, à partir du 15 octobre en soirée. Un historique de communications peut toutefois circuler entre appareils : les données disponibles n’identifient pas le matériel ayant émis les appels. Une vérification auprès de l’opérateur ne serait discriminante que si elle permet aussi le rapprochement avec le téléphone physique.

Le nom ASUS ne prouve pas que le réseau était émis par l’ordinateur OP-01, ni que celui-ci se trouvait auprès de TP-02. Les adresses du point d’accès conservées concernent le 28 octobre et n’identifient pas avec certitude celui utilisé le 17.

### Ce que change le rallumage rapporté

Si les téléphones ont été rallumés avant leur scellement, ils ont pu continuer à exécuter des tâches internes. Le diagnostic du 28 octobre mesure un temps d’éveil depuis un démarrage ; il ne permet pas de calculer une heure certaine d’allumage, ni d’attester une extinction préalable.

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

Le CD est indisponible dans cette mission ; cela ne signifie pas que l’inventaire n’existe pas auprès de l’administration. Sans cet inventaire et les fichiers saisis, il est impossible de vérifier leur correspondance exacte avec L16B ou de certifier quels fichiers sont encore détenus.

### Les correspondances avec des avocats

Les échanges identifiés sont conservés dans des archives de messagerie et des PDF. Il ne s’agit pas seulement de noms repérés : certains documents reproduisent effectivement des correspondances. Ils concernent plusieurs dossiers et parties ; tous ne sont pas nécessairement des consultations confidentielles de Mme Sadedine.

Le PDF reproduisant des échanges avec Me Isabelle Guillou concerne un recours de 2017 relatif à un tiers. Ses dates soutiennent un regroupement local le 28 octobre. Les traces d’interaction du 29 sont postérieures à la restitution déclarée et ne prouvent pas une lecture par un agent pendant les opérations.

Les 27 PDF du dossier Mini ont des contenus identiques retrouvés dans **les deux sauvegardes TP-02 et TP-03**. Ce rapprochement ne départage pas le téléphone source, le sens du transfert ou l’inclusion dans la saisie finale. De même, des courriers d’avocat déjà adressés à l’administration, une proposition de services et une mention du conseil adverse doivent être distingués d’un échange confidentiel avocat-client.

Le contrôle doit porter sur les documents effectivement emportés, leur qualification et leur éventuelle utilisation fiscale. Le cadre juridique et les références déjà cités sont conservés en annexe B.1 ; le rapport technique ne conclut pas à la régularité ou à l’irrégularité globale de la saisie.

### Les supports USB et les suppressions

Les trois identifiants Kingston distinguent plusieurs périphériques dans les traces Windows. Des références à une archive, un inventaire et une liste de rejets apparaissent sur un volume Kingston vers 17 h 26–17 h 27. Leur contenu n’a pas été récupéré et ce volume n’est pas rattaché à l’un des trois identifiants. Les traces seules ne permettent donc pas de désigner le support final ou de compter les copies.

Les dix mises à la corbeille concernent notamment des raccourcis, un document de mots de passe, une archive de téléchargement, des fichiers d’états Ciel et un PDF de deux factures. Les contenus ont été récupérés ; les factures subsistent également sous forme de texte dans le PDF Sage. Une destruction de base comptable ou une utilisation des mots de passe n’est pas démontrée. Le motif des suppressions et leur effet sur les sources restent à expliquer.

### Les opérations sur les téléphones

Après l’ouverture à 11 h 30, TP-02 conserve trois SMS marqués lus entre **12 h 03 et 12 h 46** : un code de réinitialisation Microsoft et deux codes de validation Google. Les dates de lecture sont enregistrées, mais ne prouvent ni lecture humaine locale ni utilisation des codes. Une synchronisation ou restauration reste possible, sans explication établie pour ces lignes.

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

## 7. Bilan et vérifications encore nécessaires

**Les constats les plus utiles à l’examen du dossier sont les pistes TP-02, les opérations documentées du 28 octobre et la présence de correspondances d’avocats dans les données regroupées.** Les inconnues principales sont l’origine physique de certaines traces, le contenu définitivement emporté et le rôle des supports de destination.

Aucune rupture matérielle de scellé, intrusion non autorisée, falsification volontaire de vidéo ou suppression malveillante n’est établie. L’absence de preuve retrouvée ne garantit pas l’absence d’intervention. Les limites de conservation des historiques, des horloges et des sauvegardes expliquent cette prudence.

| Pièces ou explications à obtenir | Ce qu’elles permettraient de vérifier |
|---|---|
| Inventaire final, fichiers saisis et empreintes ; liste des rejets | Composition de la copie finale, exclusion éventuelle des correspondances, rapprochement avec L16B. |
| Ordonnance complète et éventuelles instructions du juge ; actes fiscaux utilisant les pièces | Périmètre autorisé et utilisation des documents litigieux, à examiner juridiquement. |
| Identification des supports et journaux des outils | Rôle des trois Kingston et destination de la copie. |
| Photographies et documents de conservation des scellés | Continuité des emballages, mouvements et interventions éventuelles. |
| Conditions d’extinction, d’alimentation et d’isolement réseau | Possibilité de fonctionnement automatique pendant la conservation. |
| Relevés opérateur avec identifiants matériels, journaux ASUS, historique de restauration | Origine des appels et de la configuration Wi-Fi de TP-02. |
| Notes d’opérations sur les fichiers, comptes et téléphones | Motif des suppressions et nature des opérations après ouverture. |
| Autres copies vidéo et journaux de caméra, s’ils existent | Cause possible des anomalies et des périodes sans fichiers. |

Ces documents ne sont pas présentés comme disponibles. La traçabilité de la mission et les copies de conservation de **2026** font l’objet d’une annexe distincte : leur achèvement n’est pas attesté par les pièces consultées. Cette question concerne la mission actuelle et ne constitue aucun indice d’une intervention en 2024.

## 8. Annexes et références

Les annexes permettent de retrouver les dates exactes, les détails vérifiables et les limites des contrôles. Elles développent les réponses du texte principal et ne présentent pas de nouvelles investigations.

**Accès direct :** [chronologie détaillée](#annexe-a) · [précisions techniques](#annexe-b) · [limites et provenance](#annexe-c) · [conservation en 2026](#annexe-d) · [glossaire](#annexe-e) · [sources](#annexe-f) · [inventaire du matériel](#annexe-g).

<a id="annexe-a"></a>

### Annexe A — Chronologie détaillée

Les heures informatiques sont en **heure de Paris** : UTC+2 avant le changement d’heure du 27 octobre 2024, puis UTC+1. Les heures caméra sont celles des fichiers ou images, sans synchronisation vérifiée avec les autres appareils. Les déclarations de la cliente sont distinguées des traces.

| Date et heure | Équipement | Fait constaté | Ce que cela permet d’établir |
|---|---|---|---|
| 15 octobre 2024, vers 10 h 43 à 10 h 53 | OP-01 | Reprise de Windows, session locale, puis veille prolongée avec batterie faible. | Fonctionnement du système ; auteur et position exacte par rapport au début de la perquisition inconnus. |
| 15 octobre, vers 13 h 25 — observation rapportée par le prestataire le 12 novembre 2026 | Téléphones / vidéo du salon | Le prestataire indique voir une agente de l’administration fiscale rallumer les téléphones précédemment éteints. | Observation de visionnage rapportée ; maintien sous tension lors de la fermeture et jusqu’au 28 non établi ; séquence non revérifiée dans cette révision. |
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
| 28 octobre, 11 h 30 puis 11 h 45 — PV | Téléphones | Ouverture des scellés 2 à 4 ; insertion de SIM dans le téléphone du scellé 3 pour un code Apple. | Actes consignés ; correspondance avec TP-02 ou TP-03 non établie. |
| 28 octobre, 13 h 25–13 h 57 | OP-01 | Interactions enregistrées avec des fichiers de messages sous `L16B/MESSAGERIES`. | Manipulations par le système ou les applications ; lecture humaine de chaque message non démontrée. |
| 28 octobre, 14 h 50–14 h 52 | OP-01 | Créations groupées dans `L16B/GDRIVE`, puis mise à la corbeille du document de mots de passe et de l’archive de téléchargement. | Regroupement local fortement étayé et suppressions datées ; contenus récupérés. |
| 28 octobre, vers 16 h 27, 17 h et 17 h 14 | OP-01 | Installation et démarrage associés à trois identifiants distincts de périphériques Kingston, selon les heures locales du journal Windows. | Présence de supports externes, sans preuve autonome de copie. |
| 28 octobre, 17 h 26–17 h 27 | OP-01 | Références à trois fichiers sur un volume Kingston. | Interactions avec ces chemins ; contenu de l’archive externe inconnu. |
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

##### Données regroupées, archives et suppressions du 28 octobre

Le dossier `L16B` contient des documents locaux, des données Google Drive et iCloud, des messageries, des données de téléphones et des documents comptables ou bancaires. La concentration des dates de création et les comparaisons de contenus soutiennent fortement un **regroupement local de données le 28 octobre**. La présence d’archives de conversations téléphoniques ne démontre pas leur extraction directe depuis un téléphone connecté à OP-01.

Les deux archives Outlook ont été lues lors des compléments. Une archive Google Takeout contient une messagerie et un manifeste indiquant un export le 28 octobre à 12 h 42 min 33 s, heure de Paris. **La présence de fichiers issus d’exports est établie ; leur production sur OP-01 ne l’est pas.** Ils peuvent avoir été créés ailleurs puis copiés sur cet ordinateur. Ni la machine ayant demandé l’export ni son demandeur ne sont identifiés.

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

Le CD étant indisponible et le support de destination n’ayant pas été examiné, ni la liste exhaustive des fichiers emportés ni leur conservation actuelle par l’administration ne sont vérifiées. Cela concerne notamment les 27 PDF du Mini et le document reproduisant des échanges avec Me Isabelle Guillou. Le contenu commun avec TP-02 et TP-03, établi par SHA-256, ne résout pas cette question et ne départage pas les deux Mini.

Le [contrôle des catégories du PV du 9 novembre](investigations/20261109-controle-l16b-photos/compte-rendu.md) confirme une concordance substantielle avec L16B : deux PST, trente EML, Takeout, PDF Sage et export SHINE ; ce dernier comporte 94 mouvements et 27 PDF de justificatifs, avec des bornes OFX concordantes. Cette concordance n’est pas une identité exhaustive avec le jeu saisi. Deux ZIP GDRIVE et `CADA.pdf.pdf` portent des créations NTFS FN de 2026 et ne sont pas automatiquement attribuables aux opérations de 2024.

##### Correspondances avec des avocats : présence locale et saisie définitive

**La présence de correspondances dans L16B est un constat de contenu, pas une simple possibilité. En revanche, leur copie sur le support emporté par l’administration n’est pas établie.** Le regroupement de L16B pendant les opérations du 28 octobre est fortement corroboré par le PV et la chronologie des fichiers. Il ne prouve pas que chacun des documents qui s’y trouvent a été retenu après le filtrage annoncé.

| Pièces effectivement retrouvées dans L16B | Nature du constat | Limite propre à ces pièces |
| --- | --- | --- |
| Cinq messages des 23 août, 6 et 12 septembre, 3 et 8 octobre 2024, dans les Éléments envoyés du PST `dmmconseils@hotmail.com` | En-têtes adressés au cabinet Negrevergne, au sujet du dossier DMM/BRED. | Les en-têtes ne prouvent pas la remise effective des messages au destinataire ni leur inclusion dans la copie finale. |
| `Re DMM CONSEILS Audience TC Bobigny du 04 septembre 2024 à 9h15.pdf`, pièce jointe au message du 3 octobre | PDF reproduisant un échange avec Christian Pascoët concernant l’audience et le dossier DMM/BRED. | La présence de la pièce dans le PST ne démontre pas sa lecture individuelle ou sa conservation après filtrage. |
| Messages des PST concernant Mustapha Khallouki, Nicolay Fakiroff / Roosevelt Avocats et Marc-Alexandre Wahrheit | Échanges, transferts ou chaînes de correspondance identifiés par leurs en-têtes, corps et signatures, concernant EXPERT 2 MOBILE ou ALMU. | Les rôles des parties, la nature juridique et le contexte de chaque échange doivent être examinés ; tous ne concernent pas nécessairement Mme Sadedine à titre personnel. |
| `L16B/TELEPHONES/IPHONE13_MINI/Rép  Dossier bourarach.pdf` | PDF reproduisant des échanges de juillet-août 2017 avec Me Isabelle Guillou sur un recours administratif concernant un tiers ; contenu identique par SHA-256 à un PDF de la sauvegarde TP-02. | La présence du PDF et de ces échanges est confirmée. Le lien avocat-client exact et la présence dans la copie finale restent à vérifier ; les traces Jump Lists du 29 octobre ne prouvent pas une lecture par un agent pendant les opérations. |

Les détails et références sont conservés dans le [tableau des messages](investigations/20261109-correspondances-elargies/tableau-messages.md), le [tableau des documents](investigations/20261109-correspondances-elargies/tableau-documents.md) et leurs annexes techniques. Une proposition de services d’avocats, une notification de recommandé, une mention du conseil de la partie adverse ou un courrier d’avocat déjà adressé à l’administration ne sont pas assimilés automatiquement à une consultation confidentielle entre la cliente et son avocat.

**Indices individualisés pour `Rép  Dossier bourarach.pdf`.** L’entrée MFT **381463, séquence 41**, porte une création FN au **28/10/2024 à 17:13:43,799497, heure de Paris**, dans `L16B/TELEPHONES/IPHONE13_MINI`. Son contenu, SHA-256 `2e82aa66ecbc307a98ce2a170799bed53af49c0de9dd9c0c2da00c87c530df3c`, est strictement identique à deux fichiers de la sauvegarde TP-02. Ce recoupement constitue un indice précis de copie ou de regroupement local pendant les opérations, sans identifier l’auteur ni prouver un transfert direct depuis TP-02. Deux références Jump Lists désignent ce PDF au chemin local, avec dernières interactions le **29 octobre vers 01:45:21 Paris** ; elles ne prouvent pas une copie sur clé USB. La [fiche de preuve dédiée](investigations/20261109-clarification-correspondances/fiche-bourarach.md) donne les dates distinctes, les identifiants des contreparties et les sources brutes vérifiables. **Aucune trace individuelle n’établit à ce stade l’emport de ce PDF dans la saisie finale.**

**Réponse à la question « l’administration a-t-elle pris des échanges avec un avocat ? » :** des échanges de cette nature sont présents dans les données regroupées localement ; leur présence parmi les fichiers définitivement emportés est une possibilité concrète à contrôler, et non un fait établi. Le rapport ne démontre ni leur lecture par les agents, ni leur utilisation fiscale, ni un échec du filtrage annoncé. La comparaison de l’inventaire final et de ses empreintes avec les PST, messages et PDF identifiés est nécessaire pour résoudre cette question. Si un PST entier était retrouvé strictement identique dans le jeu final, cela établirait que les messages qu’il contient ont été emportés, sans prouver pour autant leur lecture ou leur utilisation.

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

**Le présent rapport technique ne conclut ni à la régularité ni à l’irrégularité globale de la saisie.** Il identifie des documents et des limites probatoires à soumettre à l’avocate. Le contrôle nécessite de confronter l’ordonnance autorisant la visite, le PV, l’inventaire final et, si possible, les fichiers effectivement saisis. La demande prioritaire est une copie de l’inventaire final et l’accès au jeu saisi pour comparer les chemins, contenus et empreintes ; l’indisponibilité du CD dans cette mission ne signifie pas que cet inventaire n’existe plus auprès de l’administration.

##### Points de confrontation juridique à conserver

Le contrôle du filtrage doit notamment porter sur les échanges incorporés dans des PDF et ceux concernant des avocats absents de la liste manuscrite. Il faut demander les critères et opérations de filtrage, ainsi que la qualification des documents éventuellement retenus et leur utilisation dans une rectification ou une majoration.

L’ancienneté d’un document ou le fait qu’il concerne un tiers ne suffisent pas à le rendre insaisissable ; sa pertinence doit être appréciée concrètement au regard de l’ordonnance. Les conditions des recherches et extractions dans les messageries, téléphones et espaces cloud restent à confronter aux autorisations et instructions disponibles.

##### Accès à distance et attribution

Aucune prise en main à distance non autorisée n’est démontrée. Des invitations anciennes à une téléassistance Sage, datées de 2022, et un raccourci de téléassistance de 2023 ne prouvent pas une session effectivement établie. Une détection de document trompeur en mai 2024 est suivie d’une mise en quarantaine déclarée réussie, sans compromission réussie démontrée.

Le compte Windows observé est `fintm`. **Il n’identifie pas la personne ayant utilisé le poste.** Aucun effacement ou falsification des journaux destiné à masquer une activité n’a été établi.

##### Après la restitution, appairages et limites de datation

Le [tableau détaillé](investigations/20261019-retour-cliente/compte-rendu.md#4-dix-mises-à-la-corbeille--contre-lecture-directe) donne chaque chemin d’origine et chaque heure.

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

Le **28 octobre, après l’ouverture à 11 h 30**, les éléments les plus utiles sont trois SMS entrants comportant des horodatages `date_read` dans `sms.db` à **12 h 03 min 18 s, 12 h 10 min 06 s et 12 h 46 min 06 s** (heure de Paris), des associations Wi-Fi à 12 h 31 et 14 h 32, une séquence compatible avec une capture d’écran vers 13 h 36 et des traitements de Photos vers 17 h 31–17 h 32. Ces trois lignes portent également `is_read=1` : le constat repose donc sur des horodatages de lecture conservés dans la base, et pas seulement sur un état « lu » observé lors de l’analyse. Ces valeurs peuvent toutefois résulter d’un marquage, d’une synchronisation depuis un autre appareil ou d’une restauration ; elles ne démontrent pas une lecture humaine locale sur TP-02 à ces instants. Le [contrôle des corps des SMS](investigations/20261109-sms-lecture/compte-rendu.md) identifie un code de réinitialisation de mot de passe Microsoft et deux codes de validation Google, sans preuve d’utilisation de ces codes. Les horodatages ne permettent pas, à eux seuls, d’identifier l’appareil à l’origine du marquage comme lu ; aucune synchronisation ou restauration expliquant ces lignes n’est établie par ce contrôle. L’image de la capture manque ; aucun auteur ni extraction par un tiers n’est identifié.

Le diagnostic WidgetKit du **28 octobre à 12 h 26** conserve `uptime=2500` secondes, soit 41 min 40 s dans sa présentation. Apple nomme ce champ **« Time Awake Since Boot »**, temps d’éveil depuis le démarrage. La distinction documentée entre compteurs incluant ou excluant le sommeil système, la précision réduite et les limites de raccord au champ IPS empêchent d’en déduire une heure d’allumage par simple soustraction. **Cette valeur ne prouve ni un démarrage vers 11 h 45, ni que TP-02 était éteint avant l’ouverture des scellés.** Les sources Apple et les limites sont détaillées dans la [note documentaire sur l’uptime](investigations/20261109-documentation-uptime/note-technique.md).

À **17 h 39**, LSC Smart Connect conserve des ressources compatibles avec le chargement ou l’actualisation d’un panneau caméra. **Aucun visionnage de vidéo n’est démontré.** Les catalogues examinés ne contiennent aucune référence de média du 15 au 28 octobre et ne constituent pas un historique complet des accès. Xiaomi Home fournit surtout des configurations permettant des rapprochements avec des équipements réseau.

Le nom `ASUS_Z01RD` apparaît aussi dans des traces d’OP-01, probablement parmi des réseaux Wi-Fi disponibles. Ces traces ne sont pas datées et ne prouvent ni une connexion du PC à ce réseau, ni sa présence au même endroit que TP-02, ni l’émission de ce réseau par OP-01.

##### Identification des scellés, réseau ASUS et traces après restitution

**La correspondance TP-02/TP-03 avec les scellés n° 3/n° 4 reste indéterminée.** Les deux sont des iPhone 13 mini rouges ; la sauvegarde identifie TP-02 par sa série, mais le mail ne donne pas les séries des scellés. TP-01 est vert dans l’attestation et l’iPhone 13 du scellé n° 2 est décrit noir : rapprochement candidat, divergence non résolue. OP-01 correspond au modèle du scellé n° 1.

Deux BSSID ASUS_Z01RD sont conservés avec des associations du **28 octobre**, **22:B0:A5:94:1F:AF** et **32:0D:CA:FD:68:8C**. Ils ne certifient pas le point d’accès utilisé le **17**. Aucun propriétaire identifié ; synchronisation/restauration toujours non exclues. L’absence connue d’ASUS dans l’entourage est une déclaration, pas une identification de l’émetteur.

Des dates existent **après 19 h 20 le 28** : appel à **19:39:46**, champ `LinkDownTimestamp` ASUS à **19:40:02**, caches LSC vers **22:35 et 23:26**. Elles sont postérieures à la restitution déclarée, sans auteur établi et sans preuve de visionnage des caméras. Le tri ciblé du manifeste et la relecture de 25 plist de gestion/comptes ne révèlent pas de session d’extraction d’octobre 2024 ni d’historique complet des appareils associés depuis 2021.

Le rallumage rapporté vers 13 h 25 le 15 est exposé en section 1.2 et en annexe A, avec sa provenance. La date du branchement de l’appareil d’extraction demeure « le 15 / le 28 » et ne doit pas être confondue avec ce rallumage.

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

**Les 27 PDF Mini de L16B ont désormais des équivalents binaires exacts dans TP-02 ET TP-03** : ils représentent 20 contenus distincts. Ce résultat commun ne départage pas le premier et le second Mini du PV. Le rapprochement antérieur avec TP-02 reste une identité de contenu, mais **n’est pas discriminant entre les deux appareils**. Il n’établit ni sens de transfert, ni appareil exclusivement source, ni inclusion dans le jeu définitivement saisi.

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
- **Pièces absentes :** le CD d’inventaire est confirmé indisponible le 8 novembre. Le PV consulté décrit une copie vers une clé USB et l’authentification des fichiers, mais ne fournit pas leur inventaire détaillé ni leurs empreintes. Le journal de sauvegarde Mac manque pour préciser la provenance des données anciennes de TP-02 ; TP-01 est désormais couvert par le complément du 10 novembre ; TP-03 est couvert par le même complément, avec les limites d’acquisition et de provenance précisées au annexe B.2.

Le rapport Freebox relève aussi une divergence non résolue pour une première activité du **4 mars 2024** entre une ancienne retranscription et les données exportées. Les heures corrigées à partir des données brutes ont été privilégiées ; cette entrée n’est pas utilisée dans la chronologie des faits du 15 au 28 octobre.

#### Sauvegardes et historique documentaire

La mission portait sur l’utilisation du matériel pendant les périodes signalées, les éventuels accès par des tiers, les copies, transferts ou suppressions de données, les téléphones et le réseau, ainsi que les enregistrements de caméra et les anomalies de dates ou réinitialisations évoquées par Mme Sadedine.

Le périmètre effectivement analysé comprend l’ordinateur **OP-01** (portable ASUS), les sauvegardes des téléphones **TP-01** (iPhone 13), **TP-02** et **TP-03** (iPhone 13 mini), la **Freebox Révolution** et trois cartes de caméra : **SD-01 — chambre**, **SD-02 — terrasse**, **SD-03 — salon**.

**TP-01 a fait l’objet d’un complément le 10 novembre 2026**, à partir de sa sauvegarde du 9 novembre, identifiée par la série Q13QT4F164. Son indisponibilité lors des campagnes antérieures ne décrit plus le périmètre actuel. **TP-03 est également analysé le 10 novembre**, sur une sauvegarde chiffrée portant des dates de septembre 2025 et identifiée par la série Y4Q9KGHG26. Sa remise matérielle, postérieure à l’attestation du 6 octobre 2026, est confirmée par le prestataire.

Cette synthèse intègre les résultats antérieurs, le [complément du 19 octobre](investigations/20261019-retour-cliente/compte-rendu.md) et la [lecture du PV du 8 novembre](investigations/20261108-analyse-pv/compte-rendu.md). Le PV est désormais disponible et a été consulté ; ses énonciations sont distinguées des constats techniques et des observations de la cliente annexées. Le [complément technique du 8 novembre](investigations/20261108-complement-pv/compte-rendu.md) expose les nouveaux contrôles et les travaux encore suspendus ; la [reprise du 9 novembre](investigations/20261108-complement-pv/reprise-20261109.md) intègre les résultats SIFT récupérés. Le journal de création de la sauvegarde sur Mac demeure indisponible. La réorganisation du 12 novembre intègre les investigations réalisées jusqu’au 10 novembre et l’observation de visionnage communiquée par le prestataire le 12 novembre (section 1.2) ; elle ne constitue ni une nouvelle analyse des acquisitions ni un nouveau visionnage indépendant des vidéos. Les constats techniques, les énonciations du PV et les déclarations de la cliente sont distingués dans chaque conclusion.

<a id="annexe-d"></a>

### Annexe D — Conservation, traçabilité et remise en 2026

**Cette section concerne la conservation et la livraison des données en 2026. Elle ne sert pas à interpréter les événements de 2024.**

Mme Sadedine a demandé la conservation de l’ensemble des données extraites sur le cloud du prestataire pendant la durée prévue au devis et sur un disque dur neuf fourni par elle. La réalisation de ces deux copies doit être attestée avant la remise définitive.

Le **contrôle du 17 octobre 2026 constate un inventaire cloud incomplet** : des éléments d’OP-01 et de SD-03 ainsi que la sauvegarde TP-02 ne figurent pas intégralement dans le stockage contrôlé, pour environ **165,22 Go manquants par rapport aux acquisitions locales**. Ce constat ne couvre pas un éventuel autre stockage non inventorié. L’inventaire des extractions et résultats doit également être complété.

**Aucun document ultérieur consulté n’atteste la régularisation de cette situation ou la réalisation de la seconde copie sur disque.** La durée contractuelle de conservation n’est pas documentée par les pièces disponibles. Le présent rapport n’atteste donc pas l’achèvement de la conservation.

Avant la remise définitive, il reste à finaliser les copies, vérifier leur complétude et leur identité avec les données conservées, identifier le disque de destination et établir un bordereau de remise. L’attestation prévoit la restitution des matériels au plus tard le **6 novembre 2026**. Ces obligations pratiques ne constituent aucun indice d’une intervention sur les équipements en 2024.

#### Traçabilité de la remise et de l’acquisition

Deux divergences documentaires restent à signaler. L’attestation porte la date du **6 octobre 2026**, alors que des notes d’intervention indiquent une remise le **7 octobre à 16 h 15**. Les horaires notés pour l’acquisition d’OP-01 en 2026 ne sont pas entièrement raccordés aux horaires automatiques. Ces écarts concernent la documentation de la mission, sans établir une manipulation en 2024.

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
- Téléphones [TP-01](telephones/analyse-TP-01.md), [TP-02](telephones/analyse-TP-02.md), [TP-03](telephones/analyse-TP-03.md) ; [Freebox](freebox/analyse-freebox.md).
- Cartes [SD-01 — chambre](cartes_sd/analyse-cartes_sd-SD-01.md), [SD-02 — terrasse](cartes_sd/analyse-cartes_sd-SD-02.md), [SD-03 — salon](cartes_sd/analyse-cartes_sd-SD-03.md) et [comparaison transversale](cartes_sd/analyse-cartes_sd-transversale.md).

#### Conservation, opérations et correspondances

- [Compte rendu général et compléments du 17 octobre](investigations/20261017-recroisements/compte-rendu.md) et [retour de la cliente et contre-lectures du 19 octobre](investigations/20261019-retour-cliente/compte-rendu.md).
- [Complément technique du 8 novembre](investigations/20261108-complement-pv/compte-rendu.md) et [reprise SIFT du 9 novembre](investigations/20261108-complement-pv/reprise-20261109.md).
- [Contrôle de L16B et des catégories du PV](investigations/20261109-controle-l16b-photos/compte-rendu.md).
- [Recherche élargie des correspondances](investigations/20261109-correspondances-elargies/compte-rendu.md), [messages sélectionnés](investigations/20261109-correspondances-elargies/tableau-messages.md), [documents](investigations/20261109-correspondances-elargies/tableau-documents.md) et [fiche du PDF Bourarach](investigations/20261109-clarification-correspondances/fiche-bourarach.md).

#### Téléphones, hypothèses concurrentes et horloges

- [Relecture transversale du 10 novembre](investigations/20261110-telephones/compte-rendu.md), [approfondissement TP-03](investigations/20261110-tp03-intervention-humaine/compte-rendu.md) et [revue contradictoire des interventions avant ouverture](investigations/20261110-revue-intervention-scelles/compte-rendu.md).
- [Contrôle des SMS marqués lus](investigations/20261109-sms-lecture/compte-rendu.md) et [note documentaire sur l’uptime](investigations/20261109-documentation-uptime/note-technique.md).

<div style="break-before: page;"></div>

<a id="annexe-g"></a>

### Annexe G — Inventaire du matériel

Cet inventaire reprend les équipements et identifiants de l’annexe 1 de l’[attestation de remise de matériels](remise-documents/attestation-de-remise.md), datée du **6 octobre 2026**, et tient compte de la remise ultérieure de TP-03 confirmée par le prestataire.

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
