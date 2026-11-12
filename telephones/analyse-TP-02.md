# Analyse informatique du téléphone TP-02

**Relecture de cohérence : 12 novembre 2026.** Harmonisation avec le [rapport final réorganisé](../RAPPORT-FINAL-SADEDINE-2026.md), sans nouvelle acquisition ni nouvelle analyse des supports. Les campagnes et décomptes techniques conservent leurs dates et leurs périmètres. Le détail de cette révision et les empreintes actuelles figurent dans le [dossier de relecture](../investigations/20261112-coherence-rapports/compte-rendu.md).

## Revue du 10 novembre 2026 — intervention avant ouverture

**TP-02 reste la piste prioritaire d’une intervention humaine possible avant ouverture**, avec la chaîne Wi-Fi du 17 octobre à 17:25:47–52 et les appels datés du 15–26. Le nouveau contrôle SIFT confirme **53 appels, dont 22 marqués sortants sur huit jours et 19 sortants à durée positive**, ainsi que l’unique `JoinedByUserAt` de la fenêtre parmi les fichiers TP-02/03 contrôlés. Aucun SMS natif daté, lu ou livré n’est sélectionné avant le 28 à 11 h 30. La chaîne Wi-Fi est plus informative que son seul libellé ; un autre réseau fournit un contre-exemple de transport d’une date utilisateur ancienne (§ 7). L’origine physique des appels et de l’état Wi-Fi n’est pas établie. La capture d’écran du 28 à 13:36 et les SMS lus après midi sont postérieurs à l’ouverture, donc ne prouvent pas une manipulation sous scellé fermé. Voir la [comparaison des hypothèses et les nouveaux contrôles](../investigations/20261110-revue-intervention-scelles/compte-rendu.md). Les versions antérieures de ce rapport sont conservées pour cette mise à jour.

## Actualisation du 10 novembre 2026 — lecture courante

Le PV est disponible et a été consulté. Les repères à retenir sont la mise sous scellés après 14 h 19 le 15 octobre, l’ouverture du PC à 10 h 41 et celle des téléphones à 11 h 30 le 28 ; 10 h 22 est l’arrivée de la cliente et 19 h 20 la clôture, sans heure individuelle de restitution. Les mentions d’indisponibilité et bornes déclaratives des sections datées ci-dessous décrivent leurs campagnes historiques. Les analyses de [TP-01](analyse-TP-01.md) et [TP-03](analyse-TP-03.md) sont désormais réalisées. TP-03 livre une séquence Santé/PersonalAudio/TipKit Messages le **16 octobre vers 05 h 31**, distincte de la séquence TP-02 du 17. Les **27 PDF Mini de L16B existent identiques dans les deux Mini** : l’identité de contenu n’est pas discriminante. Le réseau ASUS reste absent des préférences contrôlées de TP-01/03 ; cela ne certifie ni sa provenance sur TP-02 ni l’absence de toute connexion perdue. Voir la [relecture transversale](../investigations/20261110-telephones/compte-rendu.md), qui distingue les nouveaux contrôles des reprises documentaires. Les empreintes historiques des rapports restent attachées à leurs versions datées.


## Actualisation du 19 octobre 2026 — retour de la cliente

Lors du complément du 19 octobre, le PV était indisponible. Le [mail complémentaire](../docs/mail-2.txt) rapportait l’ouverture des téléphones à **11 h 30**, l’insertion SIM à **11 h 45** sur le premier Mini et des téléphones éteints puis rallumés vers 13 h 30 le 15. La lecture du PV du 8 novembre confirme depuis les deux premiers horaires, sans départager TP-02/TP-03. Le rallumage fait l’objet d’une observation de visionnage rapportée par le prestataire le 12 novembre, détaillée ci-dessous. La date de branchement d’un appareil d’extraction demeure « le 15 / le 28 ».

**TP-02 ne peut pas être rattaché avec certitude au scellé n° 3 ou n° 4.** Sa série F5466LV9V7 est confirmée par la sauvegarde ; les deux Mini rouges ne sont pas départagés par le mail. TP-01 est vert dans l’attestation, noir dans le récit du scellé n° 2. Ne pas attribuer les scellés par simple ordre numérique.

La contre-lecture ASUS conserve deux BSSID, **22:B0:A5:94:1F:AF** et **32:0D:CA:FD:68:8C**, associés à des dates du **28 octobre**. Ils ne certifient pas le point d’accès physique du **17**. Synchronisation/restauration et incertitude d’horloge ne sont toujours pas exclues. **Après 19 h 20 le 28**, l’historique comporte un appel à **19:39:46**, l’entrée ASUS un `LinkDownTimestamp` à **19:40:02**, et les caches LSC des dates vers **22:35 et 23:26**. Ces états postérieurs à la restitution déclarée ne prouvent pas la poursuite d’une intervention administrative, ni un visionnage de caméra.

Le nouveau tri du manifeste ne trouve pas de nom de pair record, d’outil d’extraction ou des applications de télécommande ciblées ; cette recherche de noms n’est pas exhaustive des logiciels inconnus. La relecture de 25 plist de profils/comptes montre notamment deux `ProfileTruth` vides et `IsSupervised=false` dans l’état conservé, sans historique complet depuis 2021. Sur OP-01, un fichier d’appairage Apple ancien est retrouvé pour **un autre UDID que TP-02**, sans connexion d’octobre 2024 démontrée.

Les catalogues et états LSC ne restituent pas l’historique des partages/réappairages depuis mars 2023. La réinitialisation de la **chambre en février 2024** est désormais explicitement déclarée, sans être techniquement démontrée. Voir les [résultats, contre-lectures et limites](../investigations/20261019-retour-cliente/compte-rendu.md). Les sections antérieures gardent leur portée historique ; les nouvelles observations sont séparées de leurs contrôles d’origine.


**Complément du 17/10/2026 :** deux MAC conservées dans les préférences Wi-Fi correspondent à des entrées Freebox ; cela ne rattache pas à TP-02 les trois iPhone nocturnes d’octobre, dont les MAC ne figurent pas dans ces préférences. Une caméra Xiaomi `mxiang.camera.mwc11` est identifiée par correspondance exacte de MAC ; le rapprochement `mwc10` reste partiel, avec deux MAC différentes. Les catalogues LSC livrent 18 références de médias, aucune du 15 au 28/10/2024, sans historique exhaustif de visionnage. Voir le [compte rendu transversal](../investigations/20261017-recroisements/compte-rendu.md). Le PV, indisponible lors de ce complément d’octobre, a depuis été consulté ; le journal de sauvegarde Mac reste indisponible et les limites de provenance des traces anciennes demeurent.

**Affaire :** SADEDINE-2026

**Cliente :** Mme Malika Sadedine — DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev — christophe@donnat.dev

**Investigations décrites et mise à jour du 14/10/2026 :** conclusions reformulées pour une lecture sans connaissances techniques, intégration du rapprochement nominal avec OP-01 ; inventaire, déchiffrement sélectif, contrôles de cohérence, communications, Wi-Fi, applications de caméras, photothèque et provenance ; intégration des approfondissements d’octobre 2024, de l’investigation Wi-Fi du 17, des traces système et de l’étude contradictoire des horloges WidgetKit. La présente mise à jour est une synthèse documentaire des opérations déjà réalisées ; elle ne constitue pas une nouvelle acquisition.

**Acquisition examinée :** sauvegarde logique chiffrée réalisée sur Mac, puis copiée sur le support forensic ; les métadonnées de sauvegarde portent des dates de septembre et octobre 2026. Elles ne constituent pas à elles seules un journal d’acquisition.

**Périmètre principal :** période de rétention déclarée du 15 au 28 octobre 2024 ; comparaison du 1er octobre au 15 novembre 2024, avec des états antérieurs et postérieurs utilisés pour vérifier la provenance et les horloges. Ce document remplace les synthèses intermédiaires pour TP-02. Les résultats portent sur les données effectivement conservées dans la sauvegarde logique. Les questions relatives à la Freebox, au réseau dans son ensemble et aux cartes SD nécessitent leurs propres pièces.

## 1. Conclusions expliquées simplement

**En clair, nous avons retrouvé dans la sauvegarde de TP-02 des traces indiquant que plusieurs fonctions de l’iPhone ont été actives, ou ont enregistré une activité, à des dates situées pendant la période où Mme Sadedine déclare ne plus avoir eu son téléphone.**

Certaines traces ressemblent à des opérations produites sur un téléphone en fonctionnement. D’autres peuvent provenir de synchronisations automatiques, de calculs différés ou de données récupérées depuis une ancienne sauvegarde. Une synchronisation consiste à recopier ou mettre à jour des données entre appareils, par exemple l’historique des appels ou les photos.

**La présence des traces est vérifiée. Ce qui reste à déterminer est quand et sur quel appareil physique les opérations qu’elles représentent se sont réellement produites, puis si une personne les a déclenchées.** Voici concrètement ce que nous avons trouvé. Toutes les heures de cette présentation sont celles de Paris.

### 1.1. Le 17 octobre 2024 : la séquence la plus informative

Les traces du 17 méritent une attention particulière, car cette date se situe entre la perte d’accès aux téléphones déclarée le **15 octobre vers 13 h 30** et l’ouverture des téléphones consignée au PV le **28 octobre à 11 h 30**. Le PV situe la mise sous scellés après **14 h 19 le 15**, sans heure individuelle précise de fermeture. **10 h 22 est l’arrivée de la cliente le 28.**

| Heure enregistrée | Ce que nous avons trouvé | Explication concrète |
|---|---|---|
| **Vers 17 h 15** | Des écritures dans les données de Santé et une date de lancement d’un composant système | Santé enregistre notamment des estimations de dépense énergétique corporelle et reprend des informations plus anciennes. Cela peut se produire automatiquement ; il ne s’agit pas d’une mesure de batterie ni d’une preuve que quelqu’un marchait avec TP-02 à cette heure. |
| **Vers 17 h 16** | Des traitements dans les composants de Contacts, Messages et Photos | Messages conserve **huit modifications internes** de paramètres ou de règles : ce ne sont pas huit SMS envoyés ou lus. Photos conserve **deux opérations liées à sa synchronisation**. Aucun affichage de ces applications à l’écran n’est prouvé. |
| **Vers 17 h 18** | Des traitements associés à l’application Téléphone | **Quatorze modifications internes** sont enregistrées. Cela ne signifie pas que quatorze appels ont été passés. |
| **Vers 17 h 25** | Une succession de propriétés Wi-Fi datées concernant **ASUS_Z01RD** | En moins de cinq secondes, l’état conservé décrit la création d’une adresse Wi-Fi privée, l’ajout du réseau, la mise à jour d’une information liée au mot de passe et une première association avec ce réseau. C’est compatible avec un téléphone qui se connecte au Wi-Fi. |

Une **adresse Wi-Fi privée** est une adresse utilisée par l’iPhone pour se présenter au réseau en protégeant sa confidentialité. Ce n’est pas son numéro de série. Le nom `ASUS_Z01RD` désigne ici un réseau Wi-Fi ; il ne permet pas, à lui seul, de connaître son propriétaire ou l’appareil qui l’émettait.

**Le point remarquable est l’enchaînement : plusieurs composants enregistrent des traitements vers 17 h 15–17 h 18, puis une association Wi-Fi apparaît environ dix minutes plus tard.** La seule arrivée automatique d’un mot de passe Wi-Fi explique moins bien cet ensemble qu’une activité de plusieurs services sur le système qui a produit les traces. Cette activité peut toutefois être automatique, sans manipulation humaine.

Les données Photos contiennent aussi un identifiant propre à TP-02, conservé lors de plusieurs mises à jour avant et après octobre 2024. Cela renforce le lien historique entre ces données et cet iPhone, sans garantir que chaque ancienne trace a été produite sur ce téléphone à la date affichée. **La sauvegarde a été réalisée en 2026 : des fichiers peuvent conserver des dates anciennes après avoir été copiés ou restaurés.**

Nous avons également vérifié un rapport de panne d’un composant de widget, c’est-à-dire un petit élément d’affichage. Il porte une date de lancement le 17 et une date de panne le 28. Ses compteurs internes ne mesurent pas le temps comme le calendrier : un long sommeil du système peut expliquer une partie de l’écart, et une correction de date reste possible. **Nous n’avons prouvé ni une erreur d’horloge ni un sommeil prolongé. Ce rapport ne confirme donc pas, à lui seul, un allumage réel de TP-02 le 17.**

Détails et sources : § 6.3, 6.4, 6.6, 6.7 et 7.

### 1.2. Entre le 15 et le 26 octobre : 53 appels dans l’historique

La sauvegarde contient **53 enregistrements d’appels datés pendant la privation d’accès déclarée**, dont certains le 15 octobre après 13 h 30 et un le 17 octobre. Les dates vont du **15 octobre à 18 h 50** au **26 octobre à 17 h 14**. Le contrôle SIFT du 10 novembre confirme **22 lignes marquées sortantes sur huit jours, dont 19 à durée positive** ; ces décomptes ne désignent pas le téléphone physique à l’origine des appels.

L’historique des appels peut être synchronisé entre appareils Apple ou récupéré depuis une sauvegarde. Les informations conservées pour ces 53 appels ne permettent pas d’identifier le téléphone physique qui a porté la communication. **Nous ne pouvons donc pas affirmer qu’ils ont été passés ou reçus directement sur TP-02.** Leur présence ne prouve pas davantage que quelqu’un a utilisé l’application Téléphone sur cet appareil pendant sa rétention.

Détails et sources : § 6.1.

### 1.3. Le 27 octobre : des milliers de dates de modification de photos

La photothèque conserve **3 123 dates de modification regroupées vers 2 h 44–2 h 45**, avant le changement d’heure de cette nuit-là. Cela signifie que de nombreux éléments de la bibliothèque portent des dates très proches, pas que quelqu’un a ouvert ou retouché 3 123 photographies.

Un traitement groupé, une synchronisation, une mise à jour ou de la maintenance de la bibliothèque peuvent produire ce type de regroupement. **Le mécanisme exact n’a pas été établi.** Plus généralement, une date de modification peut concerner les informations qui accompagnent une photo, sans changement visible de l’image.

L’origine des photos appelle aussi à la prudence : **19 des 33 fichiers sélectionnés mentionnent un « iPhone 8 » dans leurs informations techniques**, alors que TP-02 est un iPhone 13 mini. Une photo présente dans cette sauvegarde n’a donc pas nécessairement été prise avec TP-02.

Détails et sources : § 9.1 à 9.3.

### 1.4. Le 28 octobre : plusieurs traces plus proches d’une utilisation

Les événements ci-dessous portent des heures **postérieures à l’ouverture des téléphones consignée au PV à 11 h 30 et antérieures à la récupération déclarée vers 19 h 20**. Le PV est clôturé à 19 h 20, sans heure individuelle de restitution. Ces opérations ne démontrent donc pas une intervention pendant la fermeture des scellés.

| Heure enregistrée | Ce qui a été retrouvé | Ce que nous pouvons en déduire |
|---|---|---|
| **12 h 03, 12 h 10 et 12 h 46** | Trois SMS reçus, avec des horodatages `date_read` dans `sms.db` quelques secondes après la réception, et `is_read=1` | Une consultation est possible. Un état transmis depuis un autre appareil ou restauré reste aussi possible ; aucune lecture locale certaine ni personne identifiée. |
| **12 h 31 et 14 h 32** | Des associations Wi-Fi au réseau `ASUS_Z01RD` | Des traces de connexion sont conservées. Une reconnexion peut être automatique ; elle ne prouve pas une manipulation. |
| **13 h 36** | Des opérations successives du gestionnaire d’interface de l’iPhone, appelé SpringBoard, puis du service de captures d’écran | **Compatible avec la réalisation d’une capture d’écran sur l’appareil qui a produit cet historique.** L’image correspondante n’a pas été récupérée. |
| **15 h 50** | Des marqueurs de retrait de données internes, associés à un service système | Compatible avec de l’entretien interne. Ce n’est pas une preuve de suppression volontaire de fichiers ou d’effacement de preuves. |
| **Vers 17 h 31** | Génération d’une miniature de vidéo, c’est-à-dire une petite image d’aperçu | Un traitement technique de la vidéo est établi ; son visionnage ne l’est pas. |
| **17 h 31 min 58 s à 17 h 32** | Deux opérations attribuées à l’application Photos, concernant un autre élément que cette vidéo | Compatible avec une activité de l’application, sans preuve de son affichage à l’écran ou de consultation d’une image précise. |
| **17 h 39** | Des ressources enregistrées par LSC Smart Connect, application disposant de fonctions caméra | Compatible avec le chargement ou l’actualisation d’un panneau caméra. **Aucune lecture de vidéo de caméra n’est démontrée.** |

**La séquence de 13 h 36 est particulièrement informative**, car les services nommés se succèdent sur le même élément de la photothèque, comme lors du traitement d’une capture d’écran. Elle est plus précise qu’une simple date de photo. Mais l’image manque, aucun auteur n’est identifié et un historique complet peut être conservé lors d’une restauration : elle ne suffit pas à prouver qui a manipulé TP-02.

Détails et sources : § 6.2, 8 et 9.4 à 9.7.

### 1.5. Le rapprochement avec l’ordinateur ASUS OP-01

Une investigation distincte sur OP-01 a retrouvé **cinq occurrences exactes de `ASUS_Z01RD` dans le fichier d’échange Windows**, un fichier où peuvent subsister des fragments de mémoire. La reconstruction des blocs montre des structures ressemblant fortement à des listes de réseaux Wi-Fi disponibles.

**Le même nom de réseau figure donc dans les données du téléphone et de l’ordinateur.** Cela fournit une piste de rapprochement, mais cinq occurrences ne signifient pas cinq connexions ou cinq détections distinctes. Les fragments du PC ne donnent pas de date et ne prouvent pas que l’ordinateur a rejoint ce réseau.

Nous ne pouvons pas affirmer que les deux appareils ont vu le réseau au même moment, qu’ils se trouvaient au même endroit le 17 octobre, ou que le PC émettait ce réseau. Un même nom peut aussi être utilisé par différents points d’accès. Sources : [recherche OP-01](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/compte-rendu.md), [interprétation des fragments](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/origine/interpretation.md) et [limites de datation](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/datation.md) ; rapprochement détaillé au § 10.

### 1.6. Ce qui est établi, soutenu par les indices ou non prouvé

| Niveau de conclusion | Ce qu’il faut comprendre |
|---|---|
| **Établi** | Les traces existent dans les données examinées et portent des dates pendant la privation d’accès déclarée : Wi-Fi, traitements internes, appels et photos. La sauvegarde est identifiée comme celle de TP-02 par son numéro de série. |
| **Soutenu par plusieurs indices, mais non certain** | L’ensemble est compatible avec des traitements sur un système iPhone historiquement lié à TP-02. Certains indices soutiennent un fonctionnement de cet iPhone pendant sa rétention. Il reste à exclure des données copiées ultérieurement et à vérifier l’exactitude de l’horloge de l’époque. |
| **Non prouvé** | Qu’une personne a déverrouillé TP-02, consulté ses données ou ses caméras, extrait des fichiers, ouvert des scellés ou falsifié des éléments. Aucun auteur, lieu ou caractère autorisé ou non autorisé d’un accès n’est déterminé. |

**Le point essentiel est donc le suivant : nous avons des traces d’activité, mais pas encore une preuve certaine de leur origine physique à la date indiquée ni de la personne qui en serait responsable.** Des traitements peuvent se produire sur un téléphone verrouillé, sans que quelqu’un regarde son écran.

### 1.7. Réponse d’ensemble à Mme Sadedine

> Nous avons retrouvé dans la sauvegarde de votre iPhone plusieurs traces informatiques datées de la période où vous n’aviez plus votre appareil. La plus remarquable concerne le 17 octobre 2024 : différents services ont enregistré une activité, puis une connexion à un réseau Wi-Fi nommé ASUS_Z01RD apparaît vers 17 h 25. D’autres opérations, dont une compatible avec une capture d’écran, sont datées du 28 octobre avant la récupération de vos appareils. Ces éléments justifient des vérifications, mais ne permettent pas encore d’affirmer que quelqu’un a utilisé votre téléphone sous scellés. Certaines traces peuvent être automatiques ou avoir été conservées dans des données copiées ; nous n’avons pas identifié de personne responsable.

### 1.8. Les autres demandes de la cliente et les vérifications à poursuivre

| Demande | Réponse à ce stade |
|---|---|
| **Accès au réseau et aux caméras depuis 2021/2022, avant et autour de la perquisition** | TP-02 ne fournit pas un historique complet du réseau ni une preuve d’accès distant aux caméras. La **Freebox et le réseau ont fait l’objet d’un [rapport distinct](../freebox/analyse-freebox.md)**. Aucun accès non autorisé n’y est démontré ; la couverture ne permet pas d’exclure tout accès ancien. |
| **Réinitialisations ou suppressions sur SD-01, SD-02 et SD-03** | Ce rapport sur le téléphone ne permet pas de confirmer les observations relatives au **31/12/1999**, à « février » ou au **15/10/2024**. Le nouveau mail précise désormais février 2024 et la caméra de la chambre. Les [analyses SD-01](../cartes_sd/analyse-cartes_sd-SD-01.md), [SD-02](../cartes_sd/analyse-cartes_sd-SD-02.md), [SD-03](../cartes_sd/analyse-cartes_sd-SD-03.md) et [transversale](../cartes_sd/analyse-cartes_sd-transversale.md) sont réalisées : anomalies et lacunes établies, sans réinitialisation ou effacement malveillant démontré. |
| **Origine et cadre des interventions éventuelles** | Il faut confronter les traces aux procès-verbaux, aux horaires et aux opérations effectivement consignées. Une date ou un nom de réseau ne suffit pas à identifier une personne ou à dire si son intervention était autorisée. |
| **Conservation sur le cloud et sur un disque neuf** | Les extractions locales sont conservées et contrôlées. Les deux copies demandées ne sont pas attestées par ces travaux ; la durée du devis, la réception du disque et la réalisation des copies restent à documenter (§ 12.3). |

Le PV est consulté. Les pièces encore les plus utiles sont les **documents de conservation et d’intervention complémentaires**, le **journal de création de la sauvegarde sur Mac**, d’**anciennes sauvegardes proches d’octobre 2024**, et, s’ils existent encore, les **journaux du réseau Wi-Fi à heure vérifiable**. Elles permettraient de mieux déterminer quand les traces ont été produites et sur quel appareil. Leur disponibilité n’est pas garantie. Les pistes et leur portée sont détaillées au § 12.2.

Les résultats techniques qui suivent permettent de vérifier cette présentation : sources, dates exactes, méthodes de lecture et limites. Au total, **3 945 fichiers distincts** ont été déchiffrés, pour environ **1,37 Go**, dont 55 fichiers de la campagne système complémentaire. Cela représente une sélection de la sauvegarde, pas la totalité de son contenu ni un relevé exhaustif de toute l’activité passée.

## 2. Sources, équipement et chronologie de procédure

### 2.1. Sources documentaires et techniques

Le [mail de la cliente](../docs/mail.txt) et l’[attestation du 06/10/2026](../remise-documents/attestation-de-remise.md) ont été relus selon le skill `cmm-attentes-cliente`. Le rapport suit la structure du [rapport ordinateur OP-01](../ordinateur/analyse-ordinateur.md), sans transposer ses conclusions au téléphone.

Les constatations proviennent du manifeste déchiffré, des fichiers de tête de sauvegarde et des contenus sélectivement déchiffrés. Les pièces sont conservées sous [recherche-TP-02](recherche-TP-02/), avec scripts sous [scripts](scripts/). Les sorties initiales et celles d’approfondissement restent distinctes. Le [dossier d’approfondissement d’octobre 2024](recherche-TP-02/approfondissement-activite-202410/methods-and-sources.md) conserve les cinq études thématiques, les résultats reproductibles et une chronologie corrélée de **663 lignes**. Les dates et valeurs brutes restent dans ces pièces ; les synthèses excluent secrets réseau, identifiants radio, mesures médicales et coordonnées des correspondants. Les [résultats finaux](recherche-TP-02/resultats-finaux-20261014/summary.json) décrivent la campagne complète ; les résultats à 1 141 fichiers correspondent uniquement à sa première passe.

Le dossier distinct [investigation-wifi-17oct2024](recherche-TP-02/investigation-wifi-17oct2024/methodes-et-reproduction.md) contient les études de continuité iOS, mécanismes Wi-Fi et recoupements Santé/Photos, la comparaison des **36 réseaux**, une chronologie ciblée du 17 et l’évaluation contradictoire H1–H5. Cette campagne réutilise les extractions ; elle n’augmente pas le nombre de fichiers déchiffrés. Les deux chronologies d’approfondissement ont des périmètres différents et ne s’additionnent pas en événements indépendants.

Deux campagnes ultérieures du même jour complètent ces résultats :

- [Investigation système d’octobre 2024](recherche-TP-02/investigation-systeme-oct2024/conclusion-technique.md) : audit des **202 928 entrées** du manifeste, relecture de **312 diagnostics IPS**, sept bases système déjà disponibles, 123 préférences et **55 nouveaux fichiers déchiffrés** ; recherches d’usage, alimentation, réseau, localisation et anciens états supprimés.
- [Investigation horloges WidgetKit](recherche-TP-02/investigation-horloges-widgetkit/conclusion-technique.md) : relecture directe du diagnostic, comparaison des 312 IPS, vérifications des compteurs et conversions, recherche de corrections civiles et [incidence sur le Wi-Fi](recherche-TP-02/investigation-horloges-widgetkit/impact-sur-wifi-17oct.md). Cette campagne réutilise les preuves existantes sans nouveau déchiffrement.

Leurs conclusions finales priment sur les formulations intermédiaires pour les questions qu’elles réexaminent, notamment la valeur chronologique de WidgetKit. Leurs chronologies ont des périmètres différents : les lignes communes ne sont pas des événements supplémentaires. Le détail des formats et contrôles est conservé dans les rapports thématiques ; les résultats négatifs sont toujours bornés aux fichiers et méthodes examinés.

Le PV, non examiné lors de la campagne initiale, a depuis été consulté dans le [complément du 8 novembre](../investigations/20261108-analyse-pv/compte-rendu.md). Les horaires de procédure ci-dessous tiennent compte de cette lecture ; la fermeture individuelle de chaque scellé reste non datée précisément. Le courrier du procureur évoqué par la cliente n’a pas été vérifié. Aucune conclusion juridique n’est déduite de cette déclaration.

### 2.2. Identification de TP-02

| Élément | Identification |
|---|---|
| Code officiel | **TP-02** |
| Équipement | Apple iPhone 13 mini rouge |
| Numéro de série dans l’attestation et `Info.plist` | **F5466LV9V7** |
| Modèle documentaire | **MLK83KH/A** |
| IMEI 1, transcription documentaire | `35292959671648 4` |
| IMEI 2, transcription documentaire | `35292959 723940 3` |
| Type produit dans `Info.plist` | **iPhone14,4** |
| Version produit dans `Info.plist` | **18.5** ; cette valeur de sauvegarde ne démontre pas la version d’octobre 2024. |
| Dossier de sauvegarde | `00008110-001C69A002BA801E` |
| Photographie documentaire | [TP-02-1.jpg](../remise-documents/photos/TP-02-1.jpg) |

Le rapprochement de série est positif, selon la [lecture des fichiers de tête](recherche-TP-02/identification-sauvegarde.json). TP-03 est un autre iPhone 13 mini rouge ; le modèle ou la couleur seuls ne permettent pas une identification individuelle. L’attestation indique TP-03 non remis le 06/10/2026, sans établir son état de réception ultérieur.

### 2.3. Dates documentaires et déclarées, fenêtres d’examen

Les horaires suivants distinguent les déclarations du mail et les repères du PV consulté. Les heures sont celles de Paris :

| Événement et provenance | Paris | UTC |
|---|---|---|
| Perquisition fiscale | **15/10/2024** | Heure de début non fournie |
| Perte d’accès aux téléphones | 15/10 vers **13:30** | Vers **11:30Z** |
| Mise sous scellés — PV, sans fermeture individuelle datée | 15/10 après **14:19** | Après **12:19Z** |
| Arrivée de la cliente — PV | 28/10 à **10:22** | **09:22Z** |
| Ouverture des téléphones — PV | 28/10 à **11:30** | **10:30Z** |
| Insertion SIM dans le scellé n° 3 — PV, sans attribution TP-02/03 | 28/10 à **11:45** | **10:45Z** |
| Clôture du PV ; restitution approximative déclarée | 28/10 à **19:20** | **18:20Z** |

- **Fenêtre principale :** environ `2024-10-15T11:30:00Z` à `2024-10-28T18:20:00Z`, bornes incluses pour les requêtes de cette campagne.
- **Comparaison :** 1er octobre au 15 novembre inclus à Paris, soit `[2024-09-30T22:00:00Z ; 2024-11-15T23:00:00Z[`.

La fenêtre principale reste celle de la recherche initiale et comprend aussi les opérations après ouverture ; ce n’est pas une fenêtre de scellé fermé. La perte d’accès à 13:30 n’est pas une heure de fermeture. Pour les téléphones, le repère d’ouverture est **11:30 le 28**. Le contrôle ciblé du 10 novembre utilise séparément **15 octobre 14:19 inclus → 28 octobre 11:30 exclu**, sans prétendre que les scellés étaient déjà fermés individuellement à 14:19.

Les conversions utilisent **`Europe/Paris`**, UTC+2 le 15 et UTC+1 le 28 après le changement d’heure du **27 octobre 2024**. Les heures répétées de cette nuit sont conservées avec leur décalage. L’horloge historique du téléphone n’a pas été comparée à une référence indépendante.

## 3. Sauvegarde, déchiffrement et cohérence des données

### 3.1. Support examiné et couverture matérielle

```text
Sauvegarde chiffrée :
/mnt/data/forensic/SADEDINE-2026/TP-02/00008110-001C69A002BA801E/

Manifeste déchiffré contrôlé :
/mnt/data/forensic/SADEDINE-2026/ANALYSES/TP-02/Manifest-decrypted.db
```

La structure comporte les fichiers `Info.plist`, `Status.plist`, `Manifest.plist`, `Manifest.db` et les objets stockés par fileID. Le manifeste contient **202 928 entrées**, dont **137 844 fichiers ordinaires selon le filtre `flags=1` de la bibliothèque**. Le [contrôle de présence](recherche-TP-02/presence-objets-source.json) retrouve les **137 844 objets**, sans objet référencé manquant. Leurs contenus chiffrés totalisent **102 552 017 488 octets**, environ **95,51 Gio**, hors fichiers de tête.

Cette couverture de présence n’est ni un déchiffrement intégral ni une garantie de conservation des journaux de 2024. La sauvegarde est logique : les secteurs non alloués, les fichiers exclus par iOS et les traces supprimées ne sont pas intégralement représentés.

### 3.2. Dates de sauvegarde et état déclaré

| Source | Valeur de date décodée | Autres champs pertinents |
|---|---|---|
| `Info.plist` | `Last Backup Date = 2026-10-12 20:59:21` | Produit `iPhone14,4`, version `18.5`, série conforme |
| `Status.plist` | `Date = 2026-09-18 18:45:43.504067` | `SnapshotState = finished`, `BackupState = new`, `IsFullBackup = False` |
| `Manifest.plist` | `Date = 2026-09-18 17:58:21.940905` | `IsEncrypted = True`, version `10.0` |

Les dates sont des valeurs de type date décodées depuis les plist ; elles sont distinctes de dates de système de fichiers. Les [valeurs et empreintes des fichiers de tête](recherche-TP-02/identification-sauvegarde.json) sont conservées. L’écart entre septembre et octobre doit être confronté au journal Mac et aux conditions de copie. Il n’a pas été résolu par une réécriture supposée de la chronologie. **`IsFullBackup=False` ne suffit pas à conclure que cette copie manque des objets référencés**, puisque leur contrôle de présence est positif.

Les dates d’acquisition, versions du logiciel Mac, options, interventions sur l’appareil et empreintes au moment de la copie restent à documenter. Les opérations de sauvegarde de 2026 peuvent créer des traces nouvelles ou contribuer à la rotation de journaux.

### 3.3. Manifeste déchiffré et contrôle indépendant

Le script préexistant [decrypt_manifest.py](scripts/decrypt_manifest.py) utilise `iphone_backup_decrypt`. Le manifeste de travail est lisible, sa taille est **264 048 640 octets**, et son `quick_check` est **ok**.

```text
SHA-256 Manifest-decrypted.db
cd34919ad3a2cb958e130b6ea7453e71f30fb02336d61f2e1dca0f2fb2b46eeb
```

Un **nouveau déchiffrement indépendant du manifeste chiffré** a produit la même empreinte que cette copie contrôlée ; les empreintes du manifeste chiffré avant et après sont identiques. Le bloc `manifest` de [coherence-initiale-20261014.json](recherche-TP-02/coherence-initiale-20261014.json) conserve ce contrôle. Le fichier temporaire a été placé hors de la sauvegarde originale et supprimé avec le répertoire temporaire.

### 3.4. Écarts de taille et empreintes internes

Le [contrôle complet de cohérence](recherche-TP-02/coherence-complete-20261014.json) compare les tailles, l’empreinte `Digest` lorsqu’elle existe et les en-têtes SQLite. **92 fichiers de la campagne principale présentent un écart entre la taille annoncée dans MBFile et celle du contenu déchiffré**, dont `Photos.sqlite` : **835 297 280 octets annoncés**, **770 113 536 octets extraits**.

Pour les contenus contrôlés, la différence taille chiffrée/taille déchiffrée reste de **1 à 16 octets**, cohérente avec le retrait du padding AES-CBC par la bibliothèque. Les en-têtes des bases SQLite contrôlées déclarent des tailles correspondant aux fichiers extraits. Le manifeste redéchiffré est identique : l’écart n’est pas causé par l’utilisation d’un autre manifeste dans ces deux lectures.

**Les 1 307 champs `Digest` de 20 octets disponibles dans cette campagne correspondent tous au SHA-1 du contenu chiffré source. Aucun ne correspond au SHA-1 du contenu déchiffré.** Le test initial limité au contenu déchiffré reposait sur une hypothèse rejetée ; sa correction est explicitement consignée dans la pièce initiale et le contrôle complet fait référence. Ces résultats ne sont pas une signature inviolable : ils établissent une cohérence avec les objets de cette copie.

Aucun fichier n’a été tronqué pour le ramener artificiellement à la taille du manifeste. Les écarts sont conservés. Leur cause au moment de la sauvegarde — état de bases actives, mise à jour de métadonnées, copie ou autre circonstance — n’est pas démontrée. Ils ne sont pas présentés comme une preuve de falsification.

### 3.5. Approfondissement des tailles et de la copie SQLite

L’audit du code local `iphone_backup_decrypt` 0.11.2 vérifie que `MBFile.Size` est lu directement comme entier. Le déchiffrement écrit l’objet complet, retire uniquement le padding AES-CBC, puis compare les tailles : **il ne tronque pas le contenu à Size**. Pour Photos, les 65 183 744 octets d’écart ne peuvent pas provenir du retrait d’un padding de 1 à 16 octets.

| Base ciblée | MBFile moins contenu déchiffré | Pages de 4 096 octets |
|---|---:|---:|
| Photos.sqlite | 65 183 744 | 15 914 |
| healthdb.sqlite | 61 440 | 15 |
| healthdb_secure.sqlite | 1 245 184 | 304 |
| sms.db | 524 288 | 128 |
| CallHistory.storedata | 159 744 | 39 |

Ces cinq bases ont des en-têtes cohérents avec les tailles extraites, zéro page libre déclarée et aucun compagnon WAL/SHM/journal référencé au manifeste. Parmi les **254 bases déjà confirmées**, toutes ont une freelist déclarée nulle et **185 partagent un même profil d’en-tête** : change_counter=version_valid_for=2, version SQLite inscrite 3043002. Cette régularité est compatible avec la production de copies reconstruites ou sérialisées ; elle ne prouve pas l’API utilisée. Les 92 écarts de la passe principale vont dans les deux sens : MBFile plus grand dans 73 cas, plus petit dans 19.

SQLite documente des copies transactionnelles de bases actives et la possibilité de produire une copie compacte de même contenu logique. Aucun VACUUM n’a été exécuté sur les sources ; son utilisation lors de l’acquisition n’est pas démontrée. Un WAL historique absent ne peut être rejoué. Les lignes `ATRANSACTION` de Photos sont un historique applicatif interne, distinct des frames WAL.

**Incidence :** les empreintes et lectures conservées restent vérifiables, mais l’exhaustivité des lignes, des données supprimées et des états historiques n’est pas garantie. La cause exacte des tailles reste ouverte ; aucune falsification n’est déduite. Voir [l’étude contradictoire de cohérence](recherche-TP-02/approfondissement-activite-202410/backup-consistency.md) et les [résultats de taille et d’en-tête](recherche-TP-02/approfondissement-activite-202410/backup-details.json).

## 4. Environnement, préservation et outils

L’analyse est exécutée sur l’hôte Ubuntu, sans VM SIFT. L’environnement est consigné dans [environnement-outils.json](recherche-TP-02/environnement-outils.json) : Python **3.14.4**, SQLite **3.46.1** et `iphone_backup_decrypt` **0.11.2** pour le déchiffrement. Les analyses standard ont également été exécutées avec `python3` de l’hôte. Les métadonnées de médias sont lues avec Pillow et, pour HEIC, l’API de métadonnées de libheif ; aucun contenu photographique n’a été affiché pour en interpréter la scène.

| Outil développé | Fonction |
|---|---|
| [tp02_forensic.py](scripts/tp02_forensic.py) | Inventaire, sélection, déchiffrement, signatures, schémas et candidats temporels SQLite |
| [tp02_targeted.py](scripts/tp02_targeted.py) | Dates de plist/JSON/logs, appels, SMS, OperatingDates et modèles Xiaomi |
| [tp02_followup.py](scripts/tp02_followup.py) | Photothèque, provenance Santé, recoupement Wi-Fi et contexte d’origine des appels |
| [tp02_media_metadata.py](scripts/tp02_media_metadata.py) | EXIF de médias sélectionnés, y compris HEIC, sans export GPS ni contenu visuel |
| [tp02_consistency.py](scripts/tp02_consistency.py) | Manifeste indépendant, tailles CBC, Digest et en-têtes SQLite |
| [tp02_verify.py](scripts/tp02_verify.py) | Revérification des empreintes sources et extraites |
| [tp02_wifi17_investigation.py](scripts/tp02_wifi17_investigation.py) | Continuité, restauration, comparaison Wi-Fi, journal PLJ, Santé et historiques de processus |
| [tp02_wifi17_crosschecks.py](scripts/tp02_wifi17_crosschecks.py) | Champs Wi-Fi évolutifs, CommCenter, identifiants persistants et EVTX WLAN OP-01 |
| [tp02_wifi17_verify.py](scripts/tp02_wifi17_verify.py) | Reproduction des résultats, conversions, liens et recherche ciblée dans les profils |

Le mot de passe fourni pour la sauvegarde a été transmis à `getpass` dans un terminal sans écho. Il n’est pas inscrit dans les scripts, sorties ou ce rapport. Les fichiers extraits peuvent naturellement contenir des données sensibles : permissions restrictives et exclusion de `recherche-TP-02/` de Git. Les jetons applicatifs, mots de passe réseau, contenus de messages et mesures médicales ne sont pas reproduits dans les synthèses.

Les chemins de sortie sont vérifiés, les destinations d’extraction doivent être nouvelles, les sélections sont vérifiées par domaine/chemin/fileID et les opérations journalisées. Les bases générales sont analysées sur **copies temporaires**, avec leurs compagnons présents. Les lectures ciblées utilisent `mode=ro&immutable=1` sans rejouer de WAL. Aucune écriture n’a été réalisée dans la sauvegarde originale.

Les campagnes système et horloges décrivent leurs propres scripts dans [méthodes système](recherche-TP-02/investigation-systeme-oct2024/methodes-et-reproduction.md) et [méthodes horloges](recherche-TP-02/investigation-horloges-widgetkit/methodes-et-reproduction.md). Leurs lectures SQLite analytiques utilisent des copies temporaires avec les compagnons disponibles et `query_only`, sans mode `immutable` sur ces copies. Le décodeur LZFSE et les parseurs SEGB/Protobuf concernent les formats identifiés dans les 55 nouveaux fichiers ; le décodage générique d’un Protobuf ne valide pas la signification de chacun de ses champs.

## 5. Inventaire, extraction et contrôles SQLite

### 5.1. Inventaire du manifeste

Les tables `Files` et `Properties` ainsi que les index sur domaine, chemin et flags sont confirmés. La colonne BLOB `file` est décodée comme archive plist MBFile, en exportant uniquement les champs utiles d’inventaire et de dates, sans clés de déchiffrement.

L’[inventaire détaillé](recherche-TP-02/inventaire-detaille/inventory.csv) contient **106 154 entrées** dans les trois domaines caméras, tous les domaines non applicatifs et les applications Apple natives. La [sélection des fichiers intéressants](recherche-TP-02/inventaire-detaille/interesting-files.csv) comporte **3 855 entrées de priorités 1 ou 2**. Les recherches incluent les fichiers sans extension ; les types déduits des noms restent présumés jusqu’à examen de signature. La [sélection de communications WhatsApp](recherche-TP-02/selection-whatsapp.csv), deux fichiers, constitue un complément distinct de ce périmètre initial.

| Domaine prioritaire | Entrées de manifeste |
|---|---:|
| `AppDomain-com.lscsmartconnection.smart` | **14 163** |
| `AppDomain-com.xiaomi.mihome` | **2 915** |
| `AppDomainGroup-group.com.xiaomi.mihome` | **425** |
| `CameraRollDomain` | **73 263** |
| `HomeDomain` | **3 568** |

Ces nombres incluent différents types d’entrées ; ils ne sont pas des nombres d’utilisations.

### 5.2. Extraction réalisée

| Passe | Fichiers extraits | Octets déchiffrés |
|---|---:|---:|
| Applications caméras, priorités 1 et 2 | 525 | 178 755 431 |
| Système et applications Apple prioritaires | 616 | 305 157 729 |
| Photos.sqlite et plist complémentaires | 2 714 | 786 346 406 |
| Médias sélectionnés par références Photos | 33 | 19 212 053 |
| Communications WhatsApp | 2 | 66 420 736 |
| Complément système : objets sélectionnés | 48 | 7 050 475 |
| Complément système : flux Spotlight/PegasusConfiguration | 7 | 4 457 168 |
| **Total des sept passes, fileID distincts** | **3 945** | **1 367 399 998** |

Les journaux sont conservés dans les répertoires d’[extraction caméras](recherche-TP-02/extraction-cameras-20261014/extraction.jsonl), [système](recherche-TP-02/extraction-systeme-20261014/extraction.jsonl), [compléments](recherche-TP-02/extraction-complements-20261014/extraction.jsonl), [médias](recherche-TP-02/extraction-medias-20261014/extraction.jsonl) et [WhatsApp](recherche-TP-02/extraction-whatsapp-20261014/extraction.jsonl). Les deux nouveaux journaux sont [extraction-nouveaux/extraction.jsonl](recherche-TP-02/investigation-systeme-oct2024/extraction-nouveaux/extraction.jsonl) et [extraction-pegasus/extraction.jsonl](recherche-TP-02/investigation-systeme-oct2024/extraction-pegasus/extraction.jsonl), tous deux à 100 % de statuts `ok`. Le nom Apple `PegasusConfiguration` ne constitue pas une identification du logiciel espion Pegasus. Le succès de déchiffrement ne garantit pas qu’un fichier soit SQLite ni que son format applicatif interne soit décodé.

Les **3 888 fichiers des quatre premières passes** et leurs objets chiffrés sources ont reçu une seconde vérification SHA-256, avec **3 888 correspondances**. Le [journal de vérification complète](recherche-TP-02/verification-complete-20261014.json) en conserve le détail. Le complément WhatsApp est contrôlé séparément, avec **deux correspondances supplémentaires** ; le total de ces premières passes est donc **3 890 objets sources sélectionnés et 3 890 contenus extraits**. Les **55 nouveaux objets**, soit **11 507 643 octets**, disposent de [contrôles propres avant/après et de concordance aux extractions](recherche-TP-02/investigation-systeme-oct2024/new-source-verification.json), portant le total à **3 945 fileID distincts**. Il n’y a pas d’empreinte intégrale recalculée de tous les 96 Gio dans cette campagne.

### 5.3. Bases réellement identifiées et erreurs

Les quatre premières passes identifient **252 signatures `SQLite format 3\0`**, avec leurs catalogues de schémas. L’[inventaire confirmé](recherche-TP-02/resultats-finaux-20261014/sqlite-confirmed.csv) et les [schémas](recherche-TP-02/resultats-finaux-20261014/sqlite-schemas.json) permettent de vérifier les tables et colonnes. Avec les **deux bases WhatsApp supplémentaires**, le total est **254 bases à signature confirmée**, dont **232 `quick_check` réussis**. Le détail des quatre premières passes comprend **une base LSC**, **44 bases Xiaomi principales**, **quatre dans son groupe partagé**, et **203 dans les autres domaines examinés**, dont Photos.

**Sur les quatre premières passes, 230 `quick_check` réussissent.** Les **22 contrôles non réalisables** concernent des structures nécessitant des collations absentes de cette installation SQLite, notamment des bases IndexedDB WebKit. Deux tables virtuelles AddressBook ne restituent pas leurs colonnes dans cet environnement. Les erreurs sont enregistrées par stade ; aucune collation arbitraire n’a été substituée et ces contrôles ne sont pas présentés comme réussis ni comme preuves de corruption.

La campagne système confirme en outre **trois nouvelles signatures SQLite** : les magasins PlaybackEventStreams de Music et Podcasts, ainsi que SiriPrivateLearningUniversalSuggestions, malgré leurs chemins sans extension `.db`. Leur ajout porte le total des fichiers distincts à signature SQLite à **257**. Le bilan de 232 `quick_check` réussis décrit les 254 bases des premières campagnes ; il n’est pas présenté comme un contrôle global des 257. Les 55 nouveaux objets incluent également **24 fichiers SEGB**, dont 20 v2 et quatre v1, analysés par signature, structure et CRC de payload (§ 9.7).

Les plafonds de scan des colonnes temporelles sont consignés ; les sorties de la passe finale n’indiquent pas de dépassement de la limite d’un million de lignes par table examinée. Les noms de colonnes restent un filtre de triage : un historique encapsulé dans un BLOB ou un format propriétaire peut lui échapper.

## 6. Activité générale, communications et provenance

### 6.1. Historique d’appels

`HomeDomain/Library/CallHistoryDB/CallHistory.storedata` contient **1 662 enregistrements ZCALLRECORD**, dont **53** avec `ZDATE` dans la fenêtre principale. Les conversions retiennent les secondes Apple/Cocoa depuis le 01/01/2001 UTC, comme le parseur de référence iLEAPP, avec valeurs originales et clés `Z_PK` conservées.

| Jour de Paris | Enregistrements dans la fenêtre principale |
|---|---:|
| 15/10, après 13:30 | 14 |
| 17/10 | 1 |
| 18/10 | 4 |
| 19/10 | 1 |
| 20/10 | 2 |
| 21/10 | 5 |
| 22/10 | 9 |
| 23/10 | 5 |
| 24/10 | 1 |
| 25/10 | 7 |
| 26/10 | 4 |

Les 53 lignes désignent `com.apple.Telephony`. `ZORIGINATED` vaut 1 pour 22 et 0 pour 31 ; les valeurs sont conservées sans assimiler un drapeau à un opérateur. Le contrôle du 10 novembre confirme que les **22 lignes marquées sortantes sont réparties sur huit jours, dont 19 à durée positive**, sans en établir l’origine matérielle. Le premier début conservé dans cette fenêtre est le **15/10 à 18:50:48,115369**, le dernier le **26/10 à 17:14:34,075273**, heure de Paris.

**Dans ces 53 lignes, les champs `ZLOCALPARTICIPANTUUID`, `ZOUTGOINGLOCALPARTICIPANTUUID` et `ZINITIATOR` sont absents.** D’autres lignes de la base possèdent des UUID, mais aucune liaison de ces 53 appels au numéro de série de TP-02 n’est établie. Le [contrôle d’origine](recherche-TP-02/approfondissement-final-20261014/calls-origin-assessment.json) conserve les distributions, sans coordonnées des correspondants.

Apple documente la synchronisation d’historiques Téléphone/FaceTime entre appareils. Cette possibilité n’établit pas que les 53 appels sont synchronisés ; elle interdit de les attribuer automatiquement à une utilisation physique de TP-02. Les appareils associés au compte, les restaurations et les relevés opérateur doivent être confrontés aux données.

L’examen complémentaire retrouve **53 `ZUNIQUE_ID` présents et distincts**, mais aucun `ZCONVERSATIONID` ni `ZPARTICIPANTGROUPUUID`. `ZANSWERED=1` concerne 15 lignes ; `ZREAD=1`, `ZCALLTYPE=1`, `ZCALL_CATEGORY=1` et `Z_OPT=1` sont communs aux 53. Ni ces codes ni la direction logique ne donnent l’appareil ayant porté la session radio. Aucune table de provenance matérielle ni date d’arrivée/importation par appel n’est disponible dans le schéma examiné. Les champs sont bien lisibles ailleurs : 657/821 lignes de 2024 et 840/841 de 2025 ont un participant local UUID non nul, sans que sa sémantique suffise à identifier un matériel.

**Aucun des 53 appels n’est donc attribuable de façon discriminante à TP-02 avec ces seules pièces.** Production locale, synchronisation et restauration peuvent produire les mêmes valeurs observables. Les identifiants d’appels permettraient une comparaison entre acquisitions ; un relevé opérateur avec IMEI/IMSI disponible serait plus discriminant qu’un relevé de ligne et d’horaires seul. Voir [l’analyse d’origine des appels](recherche-TP-02/approfondissement-activite-202410/calls-analysis.md) et les [distributions complètes non nominatives](recherche-TP-02/approfondissement-activite-202410/calls-details.json).

### 6.2. Messages natifs et dates de lecture

`HomeDomain/Library/SMS/sms.db` conserve **trois messages entrants de service SMS** avec une date dans la fenêtre principale, tous le **28/10** :

| rowid | Date du message, Paris | Champ `date_read`, Paris |
|---|---|---|
| 74688 | 12:03:14,750877 | 12:03:18,794336 |
| 74689 | 12:10:04,455465 | 12:10:06,276798 |
| 74690 | 12:46:03,902439 | 12:46:06,075801 |

Les timestamps entiers originaux sont conservés ; la conversion utilise les nanosecondes depuis l’époque Apple et tronque l’affichage à la microseconde. `is_from_me=0` est conservé comme indicateur de réception. Les codes et identifiants des correspondants ne sont pas reproduits dans ce rapport. Le complément du 9 novembre précise ci-dessous la nature des messages.

Les trois lignes portent aussi `is_read=1`, `is_finished=1`, `is_delivered=1`, `date_delivered=0`, `ck_sync_state=1`, `did_notify_recipient=0` et `version=10`. Ce dernier champ n’est pas une version d’iOS. Les délais réception→date_read sont **4,043459072 s, 1,821332992 s et 2,173361152 s**. Les valeurs `date_read` sont des horodatages de lecture conservés dans la base, distincts du seul indicateur `is_read=1` observé lors de l’analyse. Pour ces SMS entrants, elles ne constituent pas un accusé de lecture SMS adressé au correspondant.

Le contexte de clavier `UITextInputContextIdentifiers.plist` porte une date `SETTIME` à **12:03:18,492020**, soit **302,316 ms avant** le premier `date_read`. Sa valeur associée est une préférence de mode/langue, pas du texte saisi. **12 956 tests de SHA-1** sur les identifiants de conversations et de handles, selon les représentations UTF-8/UTF-16LE testées, n’ont établi aucune liaison entre cette clé et les messages. La dérivation Apple n’est pas validée par ces essais. Les messages **74689 et 74690 n’ont pas de jointure conservée dans `chat_message_join`** ; le premier est rattaché au chat 1063.

Le [contrôle ciblé du 9 novembre](../investigations/20261109-sms-lecture/compte-rendu.md) extrait les chaînes UTF-8 des trois `attributedBody` : **74688 contient un code de réinitialisation de mot de passe Microsoft ; 74689 et 74690 contiennent des codes de validation Google**. Les marques sont indiquées par le corps, sans authentification de l’émetteur. L’utilisation des codes et la réussite des opérations ne sont pas établies. Les dates distinctes suivent chacune la réception de quelques secondes ; elles ne prouvent pas trois lectures locales. `ck_sync_state=1` ne date aucune session de synchronisation. Aucune synchronisation ou restauration expliquant spécifiquement ces lignes n’est établie par ce contrôle. Les horodatages ne permettent pas, à eux seuls, d’identifier l’appareil à l’origine du marquage comme lu.

**Les dates des messages, les horodatages `date_read` et les indicateurs `is_read=1` sont vérifiés ; une lecture humaine locale sur TP-02 à ces instants ne l’est pas.** Une application déjà ouverte, une commande de marquage, un autre appareil ou un état synchronisé/restauré restent à départager. Aucune implémentation validée ne démontre ici qu’une simple notification reçue remplit automatiquement `date_read` ; inversement, `did_notify_recipient=0` n’exclut pas une notification historique. Ces traces suivent l’ouverture déclarée et ne prouvent ni saisie, ni déverrouillage, ni identité. Voir les [détails SMS/clavier](recherche-TP-02/approfondissement-activite-202410/sms-input-details.json) et [l’étude du 28 octobre](recherche-TP-02/approfondissement-activite-202410/october28-analysis.md).

### 6.3. Données Santé : types, créations et identité de source

Les **73 échantillons** sont sélectionnés par `start_date` dans la fenêtre principale. Les jointures `samples` → `objects` → `data_provenances`, puis `sources`, `source_devices` et `sync_identities`, distinguent l’intervalle représenté de la création de l’objet. Aucune quantité médicale n’est exportée.

| Code / type interprété | Total | 16/10 | 17/10 | 27/10 | 28/10 selon début avant restitution |
|---|---:|---:|---:|---:|---:|
| 7 — pas (`StepCount`) | 4 | 0 | 0 | 0 | 4 |
| 8 — distance marche/course (`DistanceWalkingRunning`) | 4 | 0 | 0 | 0 | 4 |
| 9 — énergie de repos (`BasalEnergyBurned`) | 60 | 7 | 18 | 12 | 23 |
| 10 — énergie active (`ActiveEnergyBurned`) | 5 | 0 | 1 | 0 | 4 |

Les correspondances de codes sont recoupées avec les lecteurs de bases de référence cités dans l’étude détaillée ; elles ne sont pas présentées comme des constantes Apple publiques universelles. Pas et distances peuvent être recueillis automatiquement. Les estimations énergétiques et les lots conservés sont également compatibles avec des traitements automatiques ; ils ne nécessitent pas une ouverture de Santé. **Le 17 ne possède aucun début d’échantillon de pas ou de distance dans cette sélection.** Sur les 60 intervalles de repos, 54 durent 3 600 secondes à la précision enregistrée.

Les créations d’objets apportent les constatations suivantes :

- **17/10 17:15:48,108443 +02 (15:15:48,108443Z)** : création commune de 24 intervalles horaires de repos, objets 19582–19605, dont sept commencent le 16. Leur répartition sur deux jours ne démontre pas 24 écritures aux heures représentées.
- **17/10 17:15:48,267241 et 17:15:48,269086 +02 (15:15:48,267241Z et 15:15:48,269086Z)** : créations des objets 19606 (distance) et 19607 (pas), dont l’intervalle est **15/10 13:12:49,207109–13:15:30,524874 Paris**. Ces écritures tardives ne prouvent aucun déplacement le 17. Le filtre nouveau sur `objects.creation_date` retrouve **27 objets créés le 17** : 24 repos, ce couple pas/distance et l’énergie active ci-dessous ; ce nombre est distinct des 73 sélectionnés par début d’intervalle.
- **17/10 17:25:37,672403 +02 (15:25:37,672403Z)** : création de l’objet d’énergie active 19608, **9,958457 s avant** la génération de MAC Wi-Fi. L’intervalle représenté se termine à 17:15:37,660830, environ dix minutes auparavant.
- **28/10 11:57:22,733460 +01 (10:57:22,733460Z)** : création conservée de l’objet 19609 dont l’intervalle commence le **17/10 à 17:15:27**. Ce décalage de plus de dix jours interdit d’assimiler systématiquement la date de début à une écriture contemporaine.
- **28/10 12:01:56,572760 +01 (11:01:56,572760Z)** : nouveau lot de 24 intervalles horaires couvrant les 27–28. Les quatre couples pas/distance du 28 débutent à **12:01:32, 15:11:20, 17:24:02 et 17:39:47**, avec créations différées. Un transport sans déverrouillage peut expliquer une collecte de mouvement.

Le filtre sur start_date inclut aussi une énergie active débutant le 28 à 19:18:05, terminant à 19:27:56 et créée à 19:28:15, après restitution déclarée. Les UTC et valeurs brutes de chaque début, fin et création sont conservés dans la chronologie ; la présence parmi les 73 ne signifie donc pas que toute la séquence précède 19:20.

Les 73 lignes partagent la provenance 9 : produits origine/local `iPhone14,4`, builds `21G93`, source 1 `local_device=1`, appareil 7, version **17.6.1**, Europe/Paris, `sync_provenance=0`, `sync_identity=2`, `derived_flags=0`. Le champ `source_devices.localIdentifier` est vide ; l’appareil source possède néanmoins un UUID de 16 octets.

**Un identifiant persistant supplémentaire a été retrouvé :** `sync_identities.ROWID=2` possède des `hardware_identifier` et `database_identifier` non nuls de 16 octets. Le hardware_identifier est **identique octet pour octet** à `HomeDomain/Library/Preferences/com.apple.healthd.plist/SyncIdentityHardwareIdentifier`. Les **59 951 échantillons conservés** partagent cette identité 2 et les produits origine/local iPhone14,4. Cela rattache les données à l’identité Santé déclarée de l’installation sauvegardée, au-delà du modèle seul. **Aucun lien au numéro de série de TP-02 en octobre 2024 ni caractère matériel infalsifiable de cet identifiant n’est démontré.** Une migration/restauration reste possible ; les UUID de source, d’objet et d’identité ne sont pas interchangeables.

Aucune métadonnée associée aux 73 objets n’a été retrouvée par metadata_values/metadata_keys ; aucun marqueur de saisie manuelle ne permet donc de trancher. **Santé corrobore des traitements compatibles avec une installation locale et proches du Wi-Fi, sans certifier la continuité physique de TP-02 ni une interaction humaine.** Voir [l’analyse Santé](recherche-TP-02/approfondissement-activite-202410/health-analysis.md), les [lignes et distributions sans mesures](recherche-TP-02/approfondissement-activite-202410/health-details.json) et le [rapprochement avec healthd](recherche-TP-02/approfondissement-activite-202410/health-identity-crosschecks.json).

La source Santé 17.6.1 est créée le **03/09/2024 à 06:51:32,530530 Paris (04:51:32,530530Z)**, environ 37 secondes avant la migration Photos vers le build 21G93. Cette convergence renforce une histoire logicielle commune. Les tables actuelles `sync_stores`, `cloud_sync_stores`, `cached_sync_requests` et `sync_anchors` sont vides : elles ne permettent pas de dater ni d’exclure une synchronisation passée. Deux préférences techniques healthd datées de 2018 montrent un héritage antérieur au modèle TP-02 ; la survie exacte de l’identité Santé lors d’une restauration inter-appareils n’est pas validée. Voir les [nouveaux recoupements Santé/Photos](recherche-TP-02/investigation-wifi-17oct2024/recoupements-sante-photos.md) et les [résultats Santé sans valeurs médicales](recherche-TP-02/investigation-wifi-17oct2024/health-continuity-details.json).

### 6.4. Autres états et diagnostics

Les compléments retrouvent notamment :

- une date `from_dated` d’historique de remappage de libellés dans `com.apple.commcenter.data.archive.plist`, le **17/10 à 17:15:33** ; son rôle exact n’est pas établi et elle ne prouve pas un changement de SIM ;
- une date `CKStartupTime` dans deux préférences Books le **28/10 à 11:39:27** ; un démarrage ou traitement automatique est possible ;
- un diagnostic `WidgetKitExtension-2024-10-28-122629.ips`, avec timestamp interne **12:26:29 +01:00** ; ce n’est pas une preuve d’ouverture d’une application par une personne ;
- `CPLSyncReminderLastPromptDate` dans `com.apple.mobileslideshow.plist`, le **28/10 à 17:31:38,131411**, distinct de la date d’une miniature vidéo six secondes plus tard (§ 9.4).

Les chemins, valeurs et localisateurs sont conservés dans la [chronologie complète](recherche-TP-02/chronologie-complete-20261014/chronology-evidence.csv). Les notifications, tâches de fond, synchronisations et changements d’état restent des explications alternatives.

#### 6.4.1. Traitements supplémentaires du 17 octobre autour de 17:16

| Heure Paris (+02) ; UTC = heure Paris moins deux heures | Constat vérifié | Limite d’interprétation |
|---|---|---|
| 17:16:01 | CommCenter : `label-remap-history.ts=1729178161`, action littérale `mdn match transfer` ; `from_dated` porte 17:15:33 et `to_dated` le 11/06 à 14:00:56 | Remappage de libellé ; ni démarrage, transfert de téléphone, insertion SIM ou appel démontré par le mot transfer |
| 17:16:01,915835 et 17:16:13,168689 | AddressBook : `ClientSequence` ROWID 104083/104084, dates de sauvegarde de séquence | Aucune ouverture de Contacts ou modification manuelle prouvée |
| 17:16:26,884375–17:16:26,916920 | **8 transactions TipKit**, PK 5490–5497, auteur/bundle Messages, processus MobileSMS | Changements de règles, paramètres et tips ; aucune lecture SMS ni application au premier plan établie |
| 17:18:07,047572–17:18:07,085727 | **14 transactions TipKit**, PK 7291–7304, auteur/bundle Téléphone, processus MobilePhone ; 16 changements CoreRuleRecord | Aucun appel, affichage de tip ou geste utilisateur établi |

Les stores TipKit sont sous `AppDomainGroup-group.com.apple.tipsnext/<bundle>/.tipkit/tips-store.db`. Aucune valeur actuelle de `ZLASTDISPLAYED` examinée ne tombe le 17. Les processus peuvent mettre à jour leurs règles en arrière-plan. L’absence de tables ANSCK dans leur schéma courant n’exclut pas tout mécanisme passé de synchronisation ; une copie du store transporte son historique.

Les dates `ts` et `from_dated` CommCenter doivent être distinguées : la première date une entrée de l’historique de remappage, la seconde est une valeur d’état référencée. Les champs et identifiants expurgés sont conservés dans les [résultats CommCenter](recherche-TP-02/investigation-wifi-17oct2024/commcenter-label-remap.json), [AddressBook](recherche-TP-02/investigation-wifi-17oct2024/addressbook-sequence-events.json) et [TipKit](recherche-TP-02/investigation-wifi-17oct2024/tipkit-process-events.json), avec fileID et empreintes dans le [contrôle des sources](recherche-TP-02/investigation-wifi-17oct2024/source-verification.json).

L’ensemble est compatible avec une reprise de services autour de 17:15–17:18, avant le Wi-Fi de 17:25 ; **aucun démarrage ou déverrouillage n’est démontré**. Ces magasins distincts rendent insuffisante l’explication par le seul import d’un mot de passe Wi-Fi. Ils ne constituent pas des preuves matérielles indépendantes contre une restauration globale ou une horloge erronée commune.

### 6.5. Complément WhatsApp

Deux bases du domaine partagé WhatsApp ont été déchiffrées : `ChatStorage.sqlite` et `ContactsV2.sqlite`. Elles sont réellement SQLite et leurs `quick_check` réussissent. Elles totalisent **66 420 736 octets déchiffrés** ; leurs tailles annoncées étaient différentes, ce qui porte à **94** le nombre total d’écarts de taille après ce complément. Les [schémas et états](recherche-TP-02/analyse-whatsapp-20261014/analysis-status.json), [candidats temporels](recherche-TP-02/analyse-whatsapp-20261014/temporal-candidates.csv) et [empreintes revérifiées](recherche-TP-02/verification-whatsapp-20261014.json) sont conservés.

`ZWAMESSAGE` contient **97 442 messages**, dont **aucun `ZMESSAGEDATE` dans la fenêtre principale**. Le dernier précédent est `Z_PK=105949`, avec `ZISFROMME=1`, au **15/10/2024 à 13:16:55,308172 Paris**. Le premier suivant est `Z_PK=105950`, avec `ZISFROMME=0`, au **29/10/2024 à 00:56:41 Paris**. Le [contrôle de fenêtre](recherche-TP-02/whatsapp-window-assessment.json) conserve les dates Cocoa brutes et leurs conversions. Aucun candidat temporel des colonnes examinées dans ces deux bases ne se place dans la fenêtre principale.

Ce résultat est compatible avec une interruption de messagerie sur l’instance conservée, autour de la privation d’accès déclarée. **Il ne prouve ni l’absence d’ouverture de WhatsApp ni l’absence de messages supprimés, de sessions liées ou d’une autre instance restaurée.** Il contraste avec les 30 actifs Photos attribués à un import WhatsApp et datés pendant cette fenêtre : ces données de photothèque ne doivent pas être assimilées aux messages de cette base ni à un usage démontré de cette instance sur TP-02.

### 6.6. Continuité d’installation, restauration et identifiants persistants

**Une restauration iCloud est effectivement documentée avant les faits.** `HomeDomain/Library/Preferences/com.apple.MobileBackup.plist`, fileID `2f0b2af6ff2371fcfaf405572b94d0e8551c5659`, conserve `RestoreInfo.RestoreDate=2024-06-11 12:00:31 UTC`, soit **14:00:31 Paris**, `WasCloudRestore=true`, builds source/destination `21F90`. `RestoreStateInfo` porte 14:00:50,334277 Paris, `isCloud=true`, `progress=1.0`, `state=4` ; `AirTrafficFinishedRestoring=true`. Ni `DeviceTransferInfo` ni sa variante orthographique recherchée ne sont présents. **Cette restauration de juin n’explique pas l’import d’événements encore futurs d’octobre. Aucune restauration postérieure au 17 explicative n’est identifiée**, sans que son absence soit démontrée par ces préférences d’instantané.

Le rapprochement nouveau le plus discriminant est l’égalité exacte entre **`ZMIGRATIONHISTORY.ZDEVICEUNIQUEID` et l’UDID TP-02 des en-têtes de sauvegarde**, dans les sept lignes conservées. Toutes portent D16AP et un `ZSTOREUUID` identique au `Z_METADATA.Z_UUID` actuel :

| PK | Date Europe/Paris | Build | Migration type / origine bruts |
|---|---|---|---|
| 1 | 11/06/2024 14:00:55,270360 | 21F90 | 3 / 2 |
| 2 | 03/09/2024 06:52:09,191969 | 21G93 | 2 / 8 |
| 3 | 06/12/2024 10:08:29,192623 | 22B91 | 2 / 8 |
| 4 | 21/02/2025 05:05:33,938345 | 22D72 | 2 / 8 |
| 8 | 16/03/2025 03:18:07,318947 | 22D82 | 0 / 8 |
| 10 | 28/04/2025 04:49:23,309826 | 22E252 | 2 / 8 |
| 11 | 25/05/2025 06:59:21,614924 | 22F76 | 2 / 8 |

**Le journal de migration a été nouvellement décodé.** `CameraRollDomain/Media/PhotoData/Journals/MigrationHistory-change.plj`, fileID `e3f8a26449a3b2e3356f42998493a49ed5a71303`, SHA-256 `647eb6bbe11d8a080a6059578272892281675a43fa374c0576641037f96ac8ea`, contient sept dictionnaires plist binaires validés correspondant aux sept lignes SQL, avec le même UDID et le même store. Les bornes d’octets, empreintes internes, UTC et dates Cocoa sont conservées dans [photos-continuity-and-journal.json](recherche-TP-02/investigation-wifi-17oct2024/photos-continuity-and-journal.json). Le format externe PLJ n’est pas intégralement interprété. Les deux représentations sont des miroirs d’un même historique, pas deux acquisitions indépendantes.

Les changements de build et de modèle de données sont compatibles avec des migrations de schéma de photothèque ; **ce ne sont pas sept restaurations iOS démontrées**. Le journal ne présente pas de migration vers un autre UDID ; cela défavorise une migration inter-appareils enregistrée par cette bibliothèque, sans exclure copie, restauration sur le même appareil ou lacune d’historique.

| Identifiant / préférence | Ce qui est rattaché | Ce qui reste indéterminé |
|---|---|---|
| UDID TP-02 | Matériel désigné dans les en-têtes, sept migrations Photos et journal ; occurrences dans plusieurs autres artefacts | Une chaîne historique copiée n’atteste pas physiquement son lieu d’écriture |
| Store UUID Photos | Lignée de la base ; égalité dans métadonnées, migrations, journal et mobileCPL | Une copie de base peut conserver cet UUID ; ce n’est pas un identifiant matériel sécurisé |
| Identités Santé hardware/database | Identité logique 2 et lien hardware avec healthd ; identifiants distincts | Pas de liaison documentée à l’UDID ni de non-transfert démontré après restauration |
| Info.GUID, Status.UUID, UUID FSEvent/volume et keybag | État de sauvegarde, de suivi ou de conteneur, selon l’artefact | Pas de preuve d’une installation ininterrompue depuis 2024 |
| Setup Assistant / purplebuddy | `RestoreChoice=true`, configuration achevée ; sous-état `SSDeviceType.hardwareModel=D79AP`, différent de D16AP | Héritage de configuration concret, sans date de transport établie ; ne pas l’assimiler à l’identité actuelle |

`SetupLastExit` vaut **06/12/2024 11:00:19,000489 Paris (10:00:19,000489Z)**. Une sortie de l’assistant n’est pas une restauration démontrée ; elle est distincte de la migration Photos à 10:08 Paris. La recherche littérale de huit identifiants dans 3 886 fichiers sélectionnés donne 13 correspondances, sans garantie de tous les encodages ; Photos.sqlite est interrogé séparément. Le trousseau extrait reste opaque au niveau des attributs internes utiles : aucun historique Wi-Fi de trousseau n’a été déchiffré dans cette campagne.

**La continuité d’une lignée Photos historiquement rattachée à TP-02, avant et après octobre 2024 et encore présente en 2026, est renforcée. La continuité ininterrompue de toute l’installation iOS n’est pas démontrée.** Les copies peuvent préserver les anciennes identités : une expérience publiée de migration sur d’autres versions conserve des lignes historiques Photos ; elle n’établit pas le comportement des deux plist Wi-Fi sous 17.6.1. Voir [l’étude de continuité et ses références](recherche-TP-02/investigation-wifi-17oct2024/continuite-ios.md), les [métadonnées de restauration/setup](recherche-TP-02/investigation-wifi-17oct2024/installation-restoration-details.json) et les [rapprochements d’identifiants](recherche-TP-02/investigation-wifi-17oct2024/cross-artifact-identifier-matches.json).

### 6.7. Diagnostic WidgetKit : lancement, verrouillage et horloges

La [lecture directe du diagnostic](recherche-TP-02/investigation-horloges-widgetkit/widgetkit-raw-analysis.md) précise les champs du fichier `WidgetKitExtension-2024-10-28-122629.ips`, fileID `daf74a189f4b8e8e71c8e3a2feb211d940ca875c`. Il contient deux objets JSON valides et décrit l’extension **Google News**, non une ouverture de l’application démontrée. Son SHA-256 déchiffré est `a6da7e464e750a2961b3c315458f39be5abaf8966cb865ac014ea6b6f3a89ed0`, conforme au journal d’extraction et inchangé aux contrôles de la campagne.

| Champ | Valeur conservée | Portée |
|---|---|---|
| `procLaunch` | **17/10/2024 17:15:46,8308 +02:00**, soit 15:15:46,830800Z | Date de lancement indiquée ; justesse civile non certifiée |
| `captureTime` | **28/10/2024 12:26:28,7192 +01:00**, soit 11:26:28,719200Z | Capture du crash indiquée, après ouverture déclarée |
| `uptime` | `2500` secondes, soit 41 min 40 s dans sa présentation | Libellé Apple « Time Awake Since Boot » ; précision réduite, pas une heure de démarrage |
| `procStartAbsTime` / `procExitAbsTime` | `18054155057` / `60303998486` | Compteurs bruts ; fraction matérielle de conversion absente du rapport |
| `wasUnlockedSinceBoot` / `isLocked` | `1` / `1` | Compatibles avec un déverrouillage antérieur dans la session et un appareil verrouillé à la capture ; aucun horaire de déverrouillage |
| Modèle / système | `iPhone14,4`, iOS **17.6.1**, build **21G93** | Cohérence avec la lignée logicielle étudiée ; modèle partagé par plusieurs appareils |

**Le diagnostic ne contient pas le numéro de série ni l’UDID permettant d’identifier individuellement TP-02.** Les 312 IPS se répartissent entre deux clés diagnostiques : 88 captures du 27 avril au 10 juin 2024, puis 224 du 11 juin 2024 au 13 août 2025. WidgetKit appartient au second ensemble, cohérent temporellement avec la restauration de juin. La recherche exacte de sa clé dans 3 573 fichiers extraits non IPS n’a pas obtenu de liaison à l’UDID ou à la série. Cette continuité diagnostique et la continuité Photos sont deux rapprochements distincts, sans jointure matérielle formellement établie (§ 6.6).

**L’écart entre les dates civiles est de 936 641,8884 secondes, soit environ 10,84 jours.** Sous le modèle de ticks proche de **24 MHz**, la différence des compteurs représente **1 760,410143 secondes de temps système éveillé**. Ce n’est pas du temps CPU propre à l’extension. Les 312 diagnostics sont compatibles avec ce modèle et une présentation d’uptime tronquée à deux chiffres significatifs ; pour WidgetKit, la sortie calculée à environ 2 512,667 secondes se place dans la tranche [2 500 ; 2 600[. La fréquence exacte et le raccord des champs privés IPS aux horloges Mach ne sont cependant pas mesurés dans la preuve.

La [documentation Apple des rapports de crash](https://developer.apple.com/documentation/xcode/interpreting-the-json-format-of-a-crash-report) définit `uptime` en secondes, sous le libellé **« Time Awake Since Boot »** (temps d’éveil depuis le démarrage). Apple précise séparément que [`mach_absolute_time` exclut le sommeil système, tandis que `mach_continuous_time` l’inclut](https://developer.apple.com/documentation/driverkit/c-runtime-support). Le sommeil système ne se confond pas avec le verrouillage ou l’extinction de l’écran. Le raccord du champ IPS au compteur Mach excluant le sommeil reste une inférence étayée par le code et le corpus : la documentation du champ ne nomme pas son API interne. De même, la troncature observée est un résultat empirique, pas un algorithme garanti par Apple. **Soustraire 2 500 secondes à 12 h 26 ne prouve donc pas un démarrage vers 11 h 45**, ni un téléphone éteint avant l’ouverture des scellés. Voir la [précision documentaire du 9 novembre](../investigations/20261109-documentation-uptime/note-technique.md).

Les [contrôles des horloges](recherche-TP-02/investigation-horloges-widgetkit/apple-clock-semantics.md) et la [confrontation des hypothèses](recherche-TP-02/investigation-horloges-widgetkit/hypotheses-contradictoires.md) imposent les distinctions suivantes :

- Un **sommeil système prolongé**, avec conservation du processus dans la même session, peut permettre au calendrier d’avancer sans progression équivalente du compteur. Sous ce scénario et le modèle 24 MHz, environ **934 881 secondes** de sommeil seraient nécessaires ; ni ce sommeil ni la conservation du processus pendant onze jours ne sont mesurés.
- Une **date civile incorrecte puis corrigée** peut aussi produire cet écart. Aucun événement de correction, aucune ancienne/nouvelle date ni historique timed/NTP contemporain n’a été retrouvé dans les recherches ciblées. La correction reste possible, sans être démontrée.
- La **suspension de l’extension seule**, sur un système continuellement éveillé, ne suffit pas à expliquer cet écart. Le changement d’heure du 27 a déjà été pris en compte par les décalages +02 et +01.
- La **copie du diagnostic** peut conserver ses dates et limiter l’attribution au matériel actuel ; elle n’explique pas, à elle seule, la divergence interne entre ses référentiels temporels.

WidgetKit est le cas le plus extrême du corpus, avec un ratio civil/compteur converti d’environ **532**, contre environ **15,52** pour le deuxième. C’est un motif de vérification, pas une preuve d’erreur d’horloge. Les préférences actuelles `TMAutomaticTimeOnlyEnabled=true`, fuseau automatique désactivé et `timezone=Paris, France` ne certifient pas les réglages de 2024. La [recherche de corrections](recherche-TP-02/investigation-horloges-widgetkit/clock-anomalies.md) couvre le manifeste par chemins ciblés et 3 379 fichiers Apple/système déjà déchiffrés de 32 Mio maximum ; elle n’est pas exhaustive de tous les formats et contenus.

**Conséquence : la date de lancement est correctement lue, mais WidgetKit ne fournit pas une preuve chronologique et matérielle indépendante de fonctionnement physique de TP-02 le 17.** Il ne permet ni de calculer un boot par `captureTime − uptime`, ni de dater un déverrouillage, ni de déplacer arbitrairement les dates Wi-Fi. L’[étude d’incidence sur ASUS_Z01RD](recherche-TP-02/investigation-horloges-widgetkit/impact-sur-wifi-17oct.md) confirme la séquence native sans l’étalonner extérieurement. Les hypothèses numérotées de cette étude concernent les horloges ; elles ne se confondent pas avec celles de l’étude Wi-Fi.

**Rallumage rapporté, intégré le 12 novembre :** le prestataire indique que son visionnage des vidéos du salon montre une agente de l’administration fiscale rallumant les téléphones le **15 octobre vers 13 h 25**, avant la mise sous scellés. Il s’agit d’une observation rapportée dans le [rapport final, § 1.2](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés), sans nouveau visionnage indépendant dans cette relecture. Cette séquence n’est pas celle du clip échantillonné à partir de 13 h 28. Un fonctionnement automatique ultérieur est compatible avec ce récit, mais l’état à la fermeture et la continuité d’alimentation jusqu’au 28 ne sont pas établis. Cela ne suffit pas à expliquer l’origine physique des appels ou de la configuration Wi-Fi.

### 6.8. Usage, alimentation et localisation : portée des recherches complémentaires

| Axe examiné | Résultat dans les artefacts ciblés | Limite |
|---|---|---|
| Usage / premier plan | InteractionC : aucune interaction conservée, dates des 9 446 pièces jointes NULL. FrontBoard : 1 465 valeurs plist décodées, aucune date plist centrale. Siri : tables de suggestions vides. AppSwitcher : état courant décompressé, schéma temporel non validé. | Aucun historique daté de premier plan, écran actif ou manipulation validé ; les valeurs scalaires et formats privés ne sont pas intégralement interprétés. |
| Déverrouillage / démarrage | Archives FirstUnlock datées de mai 2024 et septembre 2026 ; BootTime csidata, sous hypothèse Unix, en septembre 2026. Aucun magasin CurrentPowerLog historique identifié. | Aucun boot, charge ou déverrouillage pendant la rétention daté par ces artefacts ; leur absence n’établit pas l’inactivité. |
| Localisation / mouvement | Bases locationd et calibrage, ainsi que caches Maps/Weather : tables pertinentes vides ou dates hors fenêtre. | Aucun lieu, déplacement ou événement cellulaire matériellement attribué à TP-02 pendant la rétention ; aucune localisation déduite du SSID ou de l’IP. |
| Dictaphone / Contacts | Trois lignes cloud Dictaphone portent la même date **28/10 à 10:17:31** et la même durée ; pas de transaction centrale correspondante. Contacts conserve des traitements de doublons à **15:08:48**. | Ces valeurs déjà visibles dans les exports ne prouvent ni trois enregistrements locaux avant ouverture ni une consultation Contacts. Aucun audio écouté ou exporté. |

Les pièces détaillées sont les études [usage](recherche-TP-02/investigation-systeme-oct2024/artefacts-usage.md), [alimentation](recherche-TP-02/investigation-systeme-oct2024/artefacts-alimentation.md), [localisation](recherche-TP-02/investigation-systeme-oct2024/artefacts-localisation.md) et [transactions](recherche-TP-02/investigation-systeme-oct2024/artefacts-transactions.md). L’absence du chemin littéral `/Biome/` n’est pas une absence de flux de cette famille : des conteneurs BMStreamMetadata et SEGB ont été identifiés sous d’autres chemins (§ 9.7). Les candidats larges non retenus ne sont pas présentés comme analysés ou négatifs.

## 7. Réseau Wi-Fi : rapprochement du 17 et du 28 octobre

La base de comparaison contient **36 réseaux connus** dans `SystemPreferencesDomain/com.apple.wifi.known-networks.plist`. Le réseau **ASUS_Z01RD** présente plusieurs champs concordants :

| Champ et fichier | Date de Paris | Nature de l’observation |
|---|---|---|
| `MacGenerationTimeStamp`, plist des MAC privées | **17/10 17:25:47,630860** | Date de génération de MAC privée conservée |
| `JoinedByUserAt`, réseaux connus | **17/10 17:25:48,147446** | Champ étiqueté connexion par utilisateur |
| `AddedAt` et `addedAt`, deux plist | **17/10 17:25:48,153697** | Même date d’ajout dans deux structures |
| `WiFiNetworkPasswordModificationDate` | **17/10 17:25:48,196428** | Date d’un état associé au secret réseau ; aucune valeur du secret exportée |
| `FirstJoinWithNewMacTimestamp`, MAC privées | **17/10 17:25:52,303180** | Date de première association enregistrée ; lien au cycle de MAC courant à contrôler (§ 7.2) |
| `LastDiscoveredAt`, réseaux connus | **28/10 12:01:49,687669** | Date de découverte conservée |
| `BSSList/1/LastAssociatedAt` | **28/10 12:31:21,663303** | Date d’association d’un point d’accès conservée |
| `BSSList/0/LastAssociatedAt` | **28/10 14:32:37,808218** | Autre état d’association conservé |
| `JoinedBySystemAt` | **28/10 14:32:37,808282** | Champ étiqueté connexion système |
| `lastJoined`, MAC privées | **28/10 14:32:38,847545** | Date cohérente de rattachement conservée |

### 7.1. Propriétés et intégrité des pièces

Les deux fichiers originaux déchiffrés ont été retrouvés sous `extraction-systeme-20261014/files/SystemPreferencesDomain/`. Leurs SHA-256 sont revérifiés, ainsi que ceux des objets chiffrés correspondants ; les contenus avant/après lecture sont identiques :

| Pièce | fileID | SHA-256 déchiffré |
|---|---|---|
| `com.apple.wifi.known-networks.plist` | `0fa75546343ba224c9fe55adc73e8fdedc1029c3` | `d32e9c13df0276375a6301cbae85b6e452c6e67081f78e39b23db37015318f82` |
| `SystemConfiguration/com.apple.wifi-private-mac-networks.plist` | `e36b35ae4cc6038f9ce83b5e097f216144278b17` | `3d066811eea6285c3a70002743082d3b07d228df1b3d685588749b7db9c36454` |

Toutes les propriétés ASUS sont conservées dans les [arbres expurgés](recherche-TP-02/approfondissement-activite-202410/wifi-properties-redacted.json) : secrets masqués, identifiants radio et coordonnées remplacés par des alias d’égalité. `AddReason="WiFi Settings"`, WPA2 Personal, réseau non caché/non captif ; `PresentInKnownNetworks=true`, `privateMacSuccessfulAssocAtleastOnce=true`, `NoAssociationWithNewMac=false`. Les codes `PrivateMacAddReason=10`, `preSwUpdateNetwork=true` et la valeur networkUsage ne sont pas convertis en actions, octets ou durées sans sémantique validée.

### 7.2. Action locale ou état importé le 17 ?

La génération de MAC et le premier rattachement sont séparés de **4,672320 s**. La date addedAt est strictement identique dans les deux structures ; la raison WiFi Settings appuie une configuration dans cette catégorie. Les propriétés liées ne sont toutefois pas cinq preuves indépendantes.

**Le contrôle de transport de date est désormais plus précis :** un réseau marqué `Cloud Sync`, alias network-16, conserve `JoinedByUserAt` au **15/04/2024 12:20:55 Paris**, antérieur à `AddedAt` du **11/06/2024 13:46:15 Paris**. Il ne s’agit plus seulement d’une coexistence de champs : une date utilisateur historique est conservée dans un ajout ultérieur. Cela empêche d’assimiler cette clé seule à un geste local sur le matériel examiné. L’écrivain exact de chaque propriété Apple sous 17.6.1 reste non validé ; un parseur n’en démontre pas les conditions d’écriture.

| AddReason | Réseaux | MacGenerationTimeStamp présent | FirstJoin présent |
|---|---:|---:|---:|
| WiFi Settings | 25 | 25 | 24 |
| Cloud Sync | 3 | 0 | 0 |
| System App | 4 | 4 | 4 |
| WiFi Password Sharing | 3 | 3 | 3 |
| 3rd Party App | 1 | 1 | 1 |

Les 36 entrées ont un `AddedAt/addedAt` identique entre les deux structures. **Aucun des trois profils Cloud Sync n’offre le contre-exemple d’une chaîne privée complète comparable à ASUS.** Ce petit échantillon ne permet pas d’exclure tous les mécanismes de synchronisation. Un profil System App a une séquence génération→FirstJoin de **6,910436 s** ; une séquence courte n’est donc pas exclusive à une configuration manuelle.

**22 des 32 couples datés ont un FirstJoin antérieur à leur MacGenerationTimeStamp courant**, dont 15 écarts proches de quatorze jours. Les champs évoluent ; une rotation de MAC est compatible avec ces différences, sans expérimentation propre établissant leur cause. Il serait erroné de traiter chaque paire comme le premier usage certain de la MAC actuellement stockée ou comme une preuve d’horloge inversée. ASUS conserve une séquence cohérente de 4,672320 s. Les dates binaires natives ont été vérifiées directement : l’erreur de conversion Cocoa/Unix ou Paris n’explique pas les valeurs du 17. Une horloge source fausse reste distincte de cette vérification.

La [comparaison des 36 réseaux](recherche-TP-02/investigation-wifi-17oct2024/comparaison-reseaux.csv), les [contrôles des champs évolutifs](recherche-TP-02/investigation-wifi-17oct2024/network-field-history-controls.json) et les [doubles binaires natifs](recherche-TP-02/investigation-wifi-17oct2024/wifi-binary-date-validation.json) permettent de reproduire ces constatations sans exposer les identifiants radio.

**La chaîne est plus compatible avec une configuration puis association sur l’appareil source qu’avec la seule arrivée d’un mot de passe. Elle ne permet pas de départager avec certitude une action sur TP-02 et l’importation ultérieure d’un état complet produit ailleurs.** La synchronisation des mots de passe Wi-Fi et leur sauvegarde/restauration sont documentées ; leur rôle exact et le transport du fichier privé dans ce cas ne sont pas prouvés.

| Hypothèse | Éléments favorables | Limite discriminante |
|---|---|---|
| Configuration/connexion sur TP-02 le 17 | WiFi Settings, chaîne de 4,7 s, addedAt commun, créations Santé et traitements CPL proches | Pas de journal radio contemporain ni liaison historique de la MAC privée au numéro de série |
| Simple import de credentials | Synchronisation possible ; coexistence Cloud Sync/date user vérifiée ailleurs dans la pièce | N’explique pas seule toute la chaîne privée génération/association ; ASUS a une autre raison déclarée |
| Restauration/migration d’un état complet | Historiques transportables ; restauration iCloud du 11 juin vérifiée ; sous-état Setup hérité | Aucun transfert postérieur au 17 explicatif identifié ; la restauration de juin précède les faits ; comportement exact des champs privés à tester sur témoin |
| Traitement automatique/profil | Auto-association techniquement possible | Aucun profil ou événement spécifique démontré pour ASUS |

Les voies de transport doivent rester distinguées : Apple documente les mots de passe Wi-Fi synchronisables et les paramètres inclus dans une sauvegarde chiffrée, **pas le transfert garanti de chaque clé privée**. Migration directe, restauration locale et restauration iCloud n’ont pas une couverture identique. La présence des deux fichiers dans cette sauvegarde locale ne prouve pas leur restauration inchangée sur un autre appareil. Un auto-join tardif à horloge correcte produit une activité tardive ; pour expliquer des dates du 17 avec TP-02 éteint ce jour-là, il faut ajouter transport de valeurs anciennes ou horloge erronée. Aucun payload ASUS n’a été retrouvé par la recherche littérale dans les 13 fichiers de profils extraits ; cela n’exclut pas un profil effacé ou non sauvegardé.

L’[étude des mécanismes Wi-Fi](recherche-TP-02/investigation-wifi-17oct2024/mecanismes-wifi-apple.md) qualifie chaque voie de transport et les versions effectivement documentées. Elle propose des tests séparés sur témoins : connexion manuelle, seul trousseau, partage, profil, migration, restauration locale même/autre appareil et cloud. Un destinataire éteint au temps initial puis acquis avant/après association permettrait de vérifier le transport des dates privées anciennes. **Ces expériences n’ont pas été effectuées et aucune n’est autorisée sur TP-02 par cette méthode.**

### 7.3. Rapprochement du 28 et limites matérielles

Les deux BSSID du 28, canaux **36 et 6**, ont exactement la même signature IPv4 de routeur et le même serveur DHCP. Le BSSID de l’entrée privée et le BSSID global correspondent à celui du canal 6 **après normalisation en six octets** : un zéro de tête omis dans la notation privée aurait faussé une comparaison de chaînes. Les deux BSSID ont le bit d’administration locale ; leur préfixe n’identifie pas valablement un fabricant.

Ces observations rapprochent les entrées du 28 d’un même environnement réseau logique, compatible avec deux bandes d’un point d’accès ou un hotspot. Elles ne prouvent ni un boîtier unique ni le même point d’accès le 17 : aucun BSSID figé séparément à cette dernière date n’est conservé. `LinkDownTimestamp` vaut **28/10 19:40:02 +01 (18:40:02Z)**, après la restitution déclarée. `lastUpdated` privé le 06/12/2024 et `UpdatedAt` connu le 28/04/2025 montrent aussi que l’état n’est pas figé en octobre 2024.

Aucun autre réseau connu ne porte AddedAt/JoinedByUserAt/JoinedBySystemAt dans la fenêtre centrale. Le scan littéral SSID/BSSID des contenus extraits ≤32 Mio ne les retrouve que dans ces deux plist, sans journal indépendant d’association de 2024. Cette absence reste bornée par la taille, les encodages et les artefacts disponibles.

Deux transactions Photos **17/10 17:16:27–28 +02**, contextes CPL FetchNewEventsFromChangeHub et UploadingBatch, suivent le lot Santé de 17:15:48 et précèdent la chaîne Wi-Fi. Elles corroborent des traitements techniques, mais pas leur passage par ASUS_Z01RD, dont le premier rattachement conservé est ultérieur.

Le SSID ne désigne ni un propriétaire ni OP-01. La documentation ASUS rapproche Z01RD d’une famille de téléphones ; un manuel d’un autre modèle illustre un nom de hotspot dérivé du modèle. **Le nom par défaut exact ASUS_Z01RD n’est pas établi par ces documents** ; un SSID reste modifiable et copiable. La MAC privée est celle du client iPhone, distincte des BSSID de points d’accès. Les premiers contrôles du WLAN brut OP-01 n’établissaient aucun lien positif. Une étude distincte a ensuite retrouvé le même nom de réseau dans le fichier d’échange du PC, sans date ni connexion démontrée (§ 10). Voir les [analyses Wi-Fi initiales](recherche-TP-02/approfondissement-activite-202410/wifi-analysis.md) et les [mécanismes et sources ASUS qualifiés](recherche-TP-02/investigation-wifi-17oct2024/mecanismes-wifi-apple.md).

### 7.4. Recherche d’une troisième source et incidence des horloges

La [campagne système réseau](recherche-TP-02/investigation-systeme-oct2024/artefacts-reseau.md) n’a pas retrouvé de troisième source indépendante pour ASUS_Z01RD. DataUsage conserve des tables Wi-Fi/événements vides et des dates d’usage s’arrêtant au **11/06/2024**, sans couverture d’octobre. Un ancien `com.apple.wifi-networks.plist.backup` contient **69 réseaux datés de 2017 à 2020**, aucun ASUS et aucune date centrale. Cet état antérieur au modèle TP-02 illustre l’existence de données historiques héritées ; il ne date pas leur transport. La recherche des identifiants ASUS dans les 55 nouveaux contenus, selon les encodages testés, ne trouve aucune correspondance.

L’étude horloges relit directement les deux plist et confirme les instants du 17 et leur intervalle de **4,672320 s**. Elle ne trouve pas de correction civile historique validée, mais ne l’exclut pas. **La concordance des dates de plusieurs services n’est pas un étalon indépendant lorsqu’ils peuvent partager la même horloge.** WidgetKit ne réfute donc pas le Wi-Fi et ne le certifie pas : le faisceau soutient une activité sur l’installation source, avec les réserves d’horloge et de transport décrites au § 6.7.

## 8. Applications de gestion des caméras

### 8.1. LSC Smart Connect : bases et formats

Les sept entrées candidates portant des noms de bases se répartissent comme suit :

| Artefact | Résultat après déchiffrement |
|---|---|
| `Library/WebKit/WebsiteData/ResourceLoadStatistics/observations.db` | SQLite effectivement lisible |
| `Documents/ty_local_data_center/health_data_center.db` | Contenu de **0 octet** ; aucune table analysable |
| Cinq `Documents/lscsmartconnectionsmart_*_apm_v1.0.db` | Absence de signature SQLite, y compris à l’intérieur des fichiers lors du sondage |

Les fichiers APM font entre **196 608 et 1 048 576 octets**. Le [sondage de format](recherche-TP-02/lsc-apm-format-probes.json) retrouve une entropie proche de huit bits par octet et aucune occurrence littérale de `2024-10-28`. **L’entropie ne prouve pas un chiffrement supplémentaire.** Le format peut être chiffré, comprimé ou propriétaire ; aucune clé utilisable ni procédure validée de décodage n’a été établie.

L’un de leurs noms contient `1.1.9_20241028182914`. Cette chaîne n’a pas été transformée en événement du 28 octobre : il pourrait s’agir d’une information de version ou de construction sans fuseau connu. La recherche de noms de paramètres liés à l’APM/chiffrement et les sondages du panneau sont consignés dans [lsc-panel-and-format-probes.json](recherche-TP-02/lsc-panel-and-format-probes.json). Les valeurs de clés et de jetons n’y sont pas exportées. La fréquence de mots « camera », « light » ou « switch » ne suffit pas à identifier le panneau. L’examen fonctionnel complémentaire décrit en § 8.2 apporte des éléments plus spécifiques sur ses capacités, sans démontrer leur exécution.

### 8.2. Panneau LSC du 28 octobre

Le cache `Documents/panel/__access_time__.json` contient une valeur time pour **`0000000432_2.51.0`**, au **28/10/2024 à 17:39:17,525519 +01 (16:39:17,525519Z)**. Les métadonnées de **485 fichiers** sous ce panneau portent Birth/LastModified/LastStatusChange à 17:39:17, soit 1 455 champs concordants, conservés dans [metadata-complete-central.csv](recherche-TP-02/metadata-complete-central.csv).

**L’analyse fonctionnelle de `main.jsbundle` identifie des capacités de caméra IP/P2P et de prévisualisation** : chemins ipcCommonState, p2pIsConnected, reGetStream, showVideoLoad, ipcLocalViewTime et uiPhase:'preview', avec ui_source:'0000000432'. Un chemin de stockage de temps de vue prend un identifiant d’équipement et une constante « 600 » ; cette constante n’est pas une durée de visionnage observée. Les [extraits et positions du code](recherche-TP-02/approfondissement-activite-202410/panel-code-details.json) dépassent un simple comptage de mots, mais décrivent du code disponible, sans preuve de son exécution en octobre 2024. Aucun modèle ou exemplaire de caméra n’y est attribué.

`main.jsbundle.meta` est un contenu opaque de **21 octets**, non reconnu comme plist/JSON dans les essais. Son empreinte est conservée ; son rôle et sa sémantique ne sont pas établis. Les APM restent non décodés.

**Le cache est compatible avec une constitution ou mise à jour de ressources, un téléchargement, un préchargement ou un affichage du panneau.** Aucun événement runtime daté de flux connecté, première image reçue ou durée de session n’atteste une consultation de caméra. Cette séquence suit l’ouverture déclarée et précède la restitution. Voir [l’analyse du 28 octobre](recherche-TP-02/approfondissement-activite-202410/october28-analysis.md).

### 8.3. Xiaomi Home : équipements et historiques conservés

Les deux domaines Xiaomi fournissent **48 fichiers à signature SQLite** : 44 dans l’application principale et quatre dans l’espace partagé. Les bases et caches incluent notamment :

- `8216275811_mihome.sqlite`, avec **trois lignes ZDEVICE** ;
- `mihome_db.sqlite3`, avec tables `home`, `room`, `device`, `props`, `operationData` et `propValues` ;
- `yydb.sqlite3`, avec six tables d’alarmes ;
- bases OneTrack/OTPubSub, caches `manifest.sqlite` et bases de widgets.

Les [modèles conservés](recherche-TP-02/chronologie-complete-20261014/xiaomi-models.csv) comprennent **`mxiang.camera.mwc11`**, **`mxiang.camera.mwc10`** et **`yeelink.light.nl1`**. Les identifiants d’équipements, adresses et jetons restent dans les pièces protégées ; ils ne sont pas reproduits ici. Ces configurations ne constituent pas un historique de consultation.

Les **six tables d’alarmes de `yydb.sqlite3` sont vides**. Les tables d’événements et de cache de la base OneTrack examinée sont également vides, tout comme la table OTPubSub `events`. Les lignes ZDEVICE examinées portent `ZLASTONLINE=0.0`. Aucune de ces absences ou valeurs nulles ne démontre l’absence d’accès en 2024 : la rétention et le rôle de ces tables ne sont pas établis.

Les premiers candidats temporels SQLite retrouvés dans les applications caméras concernent essentiellement des dates de caches hors fenêtre principale. La configuration partagée `AppConfig/561CB9034971AB05FF2B2BBC88056031` porte dans le manifeste des dates au **28/10 à 17:40:50**, mais aucune opération de caméra n’est identifiée à partir de cette seule métadonnée.

### 8.4. WebKit OperatingDates

LSC et Xiaomi possèdent une table `OperatingDates`. **Le mois est codé de 0 à 11**, et non de 1 à 12 ; les dates sont des jours UTC sans heure. Cette particularité est confirmée par la structure observée et le code WebKit de référence. La date de début affichée dans les CSV est une borne de jour, pas une heure de lancement.

Après conversion correcte, Xiaomi conserve un jour **15 octobre** et un jour **28 octobre** ; LSC conserve le **28 octobre**, sans jour retenu entre le 15 et le 27 inclus. Les dates du 15 et du 28 ne permettent pas un placement avant/après 13:30, ouverture ou restitution. La version actuelle de WebKit montre aussi un ajout du jour à l’initialisation du magasin de statistiques : **OperatingDates n’est pas un historique de consultation de caméras ni un registre d’actions humaines**. Le comportement précis de la version utilisée en 2024 n’a pas été audité.

## 9. Photos, fichiers, modifications et suppressions

### 9.1. Photothèque effectivement déchiffrée

`CameraRollDomain/Media/PhotoData/Photos.sqlite` a une signature SQLite, un `quick_check=ok` et contient **19 516 lignes ZASSET**. Le [CSV des champs datés](recherche-TP-02/approfondissement-final-20261014/photos-date-fields.csv), les [actifs créés dans la fenêtre](recherche-TP-02/approfondissement-final-20261014/photos-assets-created-central.csv) et la [synthèse](recherche-TP-02/approfondissement-final-20261014/photos-summary.json) conservent les valeurs et jointures.

| Champ conservé dans la fenêtre principale | Lignes | Lecture à conserver |
|---|---:|---|
| `ZDATECREATED` | 87 | Date de création déclarée de l’actif, pas nécessairement prise de vue locale |
| `ZADDEDDATE` | 85 | Date d’ajout de bibliothèque, pas nécessairement date d’arrivée physique actuelle sur TP-02 |
| `ZMODIFICATIONDATE` | 5 958 | Modification d’état ou donnée de bibliothèque ; pas preuve de retouche humaine |
| `ZADJUSTMENTTIMESTAMP` | 6 | Date d’ajustement conservée ; origine et nature de l’ajustement à établir |
| `ZLASTVIEWEDDATE` des attributs associés | 5 154 | Champ de dernière vue, sans validation de son origine ni de toutes ses causes de mise à jour |
| `ZTRASHEDDATE` | 0 | Aucune date de ce champ conservée dans la fenêtre, pas absence démontrée de suppression |
| `ZANALYSISSTATEMODIFICATIONDATE` | 0 | Absence de valeur dans cette fenêtre pour ce champ examiné |

Ces lignes ne s’additionnent pas en opérations indépendantes. Une concentration de **2 480 dates de modification le 27/10 dans la minute 02:45 +02:00**, et de **643 dans 02:44 +02:00**, est conservée. Le décalage est indispensable pendant la nuit du changement d’heure. Ce regroupement doit être distingué de milliers de retouches manuelles : synchronisation ou traitement de bibliothèque sont des explications possibles, non démontrées.

### 9.2. Origine des actifs et médias sélectionnés

Pour les 87 actifs dont `ZDATECREATED` est dans la fenêtre : les attributs d’import désignent **SpringBoard pour 50**, **WhatsApp pour 30**, **TikTok pour trois**, et ne renseignent pas cette origine pour quatre. Les libellés proviennent de champs conservés ; ils ne prouvent pas que l’import a été réalisé sur TP-02 à cette date. En particulier, SpringBoard ne suffit pas, sans validation supplémentaire, à attribuer une capture d’écran locale à cet appareil.

**33 fichiers de médias ont été retrouvés et sélectionnés par correspondance de nom/UUID** dans la sauvegarde : 32 JPEG et un HEIC, soit **19 212 053 octets**. Ce rapprochement ne prétend pas identifier tous les originaux des 87 actifs ni toutes leurs variantes.

Le [contrôle EXIF final](recherche-TP-02/medias-metadata-final.json), après lecture HEIC avec libheif, identifie **19 modèles déclarés « iPhone 8 »** ; 14 médias ne renseignent pas de modèle. Les 33 lectures de métadonnées terminent sans erreur. Les dates `DateTimeOriginal` sont conservées brutes ; celles dépourvues de décalage ne reçoivent pas un fuseau arbitraire.

**Ce résultat est un contre-exemple concret à l’attribution automatique des dates Photos à TP-02.** Les métadonnées EXIF peuvent être modifiées et ne permettent pas d’identifier l’exemplaire d’iPhone 8 ou son utilisateur. Un tel équipement n’est pas identifié par un code dans l’attestation ; aucun code nouveau ne lui est attribué.

Apple documente la synchronisation automatique des photos et des modifications entre appareils via iCloud Photos. Cette possibilité est pertinente pour interpréter la bibliothèque ; les réglages historiques et les autres acquisitions restent nécessaires pour déterminer son rôle réel.

### 9.3. Portée des dates de modification et des suppressions

La sauvegarde unique ne permet pas de reconstituer un registre exhaustif des créations, modifications et suppressions depuis 2024. Une date de bibliothèque peut être héritée, copiée, synchronisée ou modifiée après les faits. Des objets supprimés définitivement ou exclus de la sauvegarde ne seront plus représentés ; des métadonnées actuelles peuvent remplacer des états plus anciens.

Les six dates d’ajustement, les champs de dernière vue et les modifications ont été exportés, sans conclure à six retouches ou 5 154 consultations humaines sur TP-02. Aucun carving physique ou extraction de secteurs supprimés n’est présenté comme réalisé.

Toutes les **5 958** lignes portant une modification centrale et les **85** ajouts possèdent un ZCLOUDASSETGUID dans leur état actuel : cela rend la piste cloud pertinente, sans prouver la cause de chaque modification. Le 28 avant restitution, les champs actuels donnent **zéro ZMODIFICATIONDATE, zéro ZLASTVIEWEDDATE et un ZADDEDDATE**, alors que 343 transactions de cette journée sont conservées (§ 9.5). Les seules valeurs actuelles ne forment donc pas un historique exhaustif ; les lignes ont pu évoluer ou disparaître. Voir les [regroupements et états cloud](recherche-TP-02/approfondissement-activite-202410/photos-details.json).

### 9.4. Miniature vidéo du 28 octobre

Le manifeste conserve trois dates au **28/10 à 17:31:44** pour :

```text
Media/PhotoData/Thumbnails/VideoKeyFrames/DCIM/101APPLE/IMG_1773.MP4/LocalVideoKeyFrame.jpg
```

Le catalogue Photos référence `IMG_1773.MP4` avec une date de création du **14 octobre 2024** et un import attribué à Instagram. La valeur actuelle de dernière vue de cet actif est **postérieure à la fenêtre de rétention**. **Le lien technique est désormais vérifié :** transaction `ATRANSACTION.Z_PK=117587` à **17:31:44,885448 +01 (16:31:44,885448Z)**, contexte `PLPrimaryResourceDataStoreLocalVideoKeyFrameRecipe _runNextJob`, avec changements sur **Asset 23729**, qui correspond à cette vidéo, et **InternalResource 85746**. La date du manifeste et le travail interne se recoupent donc au-delà d’une proximité horaire. Le rappel `CPLSyncReminderLastPromptDate` à 17:31:38,131411 le précède de 6,754037 s, sans causalité établie. **La génération de miniature est établie ; le visionnage de la vidéo ne l’est pas.**

### 9.5. Transactions Photos : traitements automatiques et indices d’interface

L’approfondissement exploite `ATRANSACTION`, `ATRANSACTIONSTRING` et `ACHANGE`. Les noms de processus/contextes se retrouvent par jointure des colonnes **ZAUTHORTS, ZBUNDLEIDTS, ZCONTEXTNAMETS, ZPROCESSIDTS** vers `ATRANSACTIONSTRING`, même lorsque les colonnes texte directes sont NULL. Les [345 transactions centrales et changements associés](recherche-TP-02/approfondissement-activite-202410/photos-transaction-correlations.json) comprennent deux transactions CPL le 17 et **343 le 28**. Une transaction est un ensemble de changements persistants, pas un geste.

Le 28, **277 contextes mediaanalysisd-service et 42 photoanalysisd**, soit 319/343, appuient une explication de traitement automatique. D’autres nomment explicitement nettoyage, récupération d’état cloud et génération de ressources. Deux séquences sont plus spécifiques d’une activité d’interface :

| Transaction / heure Paris (+01) | Fait vérifié | Portée |
|---|---|---|
| 117456 — **13:36:10,800948** (12:36:10,800948Z) | SpringBoard ; changements de type brut 0 sur Asset 23769 et ses attributs/ressources | Compatible avec une insertion dans la bibliothèque source |
| 117461 — **13:36:14,432556** (12:36:14,432556Z) | ScreenshotServicesService ; changements de type brut 1 sur le même actif | Indice spécifique d’une opération de capture d’écran, plus informatif qu’un libellé d’import isolé |
| 117588–117589 — **17:31:58,026875 et 17:32:00,403479** (16:31:58,026875Z et 16:32:00,403479Z) | PhotoKit changes attribués à com.apple.mobileslideshow (Photos), sur AdditionalAssetAttributes 23703 | Requêtes du client Photos ; elles visent un autre actif que la vidéo 23729 |

La correspondance des types bruts 0/1 avec insertion/mise à jour est cohérente avec Core Data. Le masque de propriétés n’est pas décodé : les requêtes Photos ne sont pas qualifiées de visionnage d’un média précis ni d’ouverture au premier plan.

**Asset 23769 est absent de ZASSET actuel**, mais son historique persiste : traitement cloud entrant le **29/10 à 10:05:52,532827 +01**, puis changement de type brut 2 sous `PLExpiredCleanupMaintenanceTask` le **29/11/2024 à 02:21:38,361269 +01**, transaction 124593. Valeurs brutes et UTC sont conservés dans le résultat détaillé. La purge de maintenance ne date pas un geste initial de mise à la corbeille et n’en établit pas le motif. Aucun contenu de capture n’a été récupéré ni interprété.

**Ces contextes soutiennent une activité d’interface compatible avec une intervention humaine sur l’appareil source de la bibliothèque.** Ils ne constituent pas un journal tactile et ne suffisent pas, à eux seuls, à identifier le matériel d’exécution en 2024 ; le rattachement historique de la lignée à l’UDID TP-02 est précisé aux § 6.6 et 9.6. Une restauration complète peut transporter l’historique ; il ne faut pas supposer qu’une simple synchronisation d’objets transporte toutes les tables de transactions. Aucun auteur n’est identifié. Voir [l’étude des corrélations du 28 octobre](recherche-TP-02/approfondissement-activite-202410/october28-analysis.md).

### 9.6. Valeur des transactions du 17 pour l’attribution matérielle

Les commits assetsd 117245 et 117246 du **17/10 à 17:16:27,568770 et 17:16:28,548546 Paris** décrivent des traitements CPL, pas l’ouverture de Photos ni un envoi réseau réussi. Leur ordre entre des transactions du 15 et du 28 est cohérent ; aucune régression temporelle n’a été observée dans l’ordre des PK des transactions 2024–2025, sans constituer une calibration indépendante de l’horloge.

Le contrôle nouveau de copie logique SQLite vers **`:memory:` uniquement**, depuis la source en lecture seule, conserve exactement ces deux lignes et dates. Un historique peut donc être transporté sans réexécution au temps enregistré sur la destination. **Ce test n’est pas une restauration iOS expérimentale.** À l’inverse, le fonctionnement public documenté d’import d’objets Core Data/CloudKit ne valide pas la réplication telle quelle des anciennes ATRANSACTION d’un autre appareil ; son extrapolation au CPL privé reste limitée. Simple synchronisation d’objets Photos et restauration du store ne sont pas interchangeables.

La fin de reconstruction Photos est datée du **11/06/2024 14:00:55,756208 Paris** ; `CloudInitialUploadDate` du **06/12/2024 10:09:39,006537**, alors que CPL est déjà présent auparavant. Ce champ ne démontre donc pas un premier usage historique d’iCloud. La reconstruction d’index des 28–29 avril 2025 ne constitue pas une restauration iOS. La lignée UDID et son journal (§ 6.6) renforcent le rattachement historique à TP-02, sans supprimer la transportabilité. Voir les [recoupements et limites Core Data](recherche-TP-02/investigation-wifi-17oct2024/recoupements-sante-photos.md) et le [contrôle de copie](recherche-TP-02/investigation-wifi-17oct2024/photos-continuity-and-journal.json).

### 9.7. Recherche ciblée d’anciens états et marqueurs de retrait interne

L’[étude de récupération](recherche-TP-02/investigation-systeme-oct2024/recuperation-suppressions.md) précise le devenir de l’actif **23769** de la séquence ScreenshotServices. Une ligne encore allouée d’historique, **ACHANGE 1493606**, entité Asset, transaction **124593**, conserve un UUID et un libellé d’expiration. `ZTOMBSTONE3=751880805.776` est convertible sous époque Cocoa au **29/10/2024 à 08:46:45,776 Paris** (07:46:45,776Z). **Le mapping de cette propriété n’étant pas validé, cette valeur n’est pas retenue comme une date démontrée de mise à la corbeille.** Elle est distincte de la purge de maintenance datée du 29 novembre (§ 9.5), et toutes deux sont hors de la rétention déclarée.

Sur une copie de Photos.sqlite, la recherche de l’UUID précis dans les zones inutilisées et freeblocks de **28 606 pages** des tables ZASSET, ZADDITIONALASSETATTRIBUTES et ACHANGE n’obtient aucune correspondance, sans erreur de structure. Les zones examinées représentent **2 390 389 octets non alloués** et **3 463 octets de payload freeblock**. La recherche dans les chemins du manifeste ne retrouve pas davantage cet UUID. **Aucune image et aucun ancien enregistrement supplémentaire de l’actif n’ont été récupérés.** Ce contrôle ciblé ne couvre ni tous les espaces SQLite ni les secteurs physiques de l’iPhone ; l’absence de WAL Photos au manifeste limite la récupération.

Les **24 flux SEGB** déchiffrés comportent **14 618 enveloppes** : **9 507 enregistrements écrits à CRC de payload valide** et **5 111 états supprimés à payload nul**. Parmi les observations dans la fenêtre principale, **47 métadonnées sont toutes datées du 28**, dont 20 états supprimés sans contenu et les **27 marqueurs de retrait interne (« tombstones »)** suivants :

| Source et date conservée | Constat | Ce qu’il ne démontre pas |
|---|---|---|
| Deux flux Spotlight/session ; **28/10 15:50:24,854333–15:50:24,869329 Paris** (14:50:24Z) | 27 enregistrements écrits, CRC de payload valide, libellé `parsecd` et références d’index | Ni suppression de données utilisateur, ni geste humain, ni dissimulation |
| Références vers les segments conservés | 27 adresses rejoignent des slots d’index, mais seulement cinq tailles présumées concordent avec le contenu actuel ; certaines dates actuelles sont plus tardives | L’occupant actuel d’un slot ne peut pas être identifié automatiquement comme l’événement historique retiré |

Un CRC contrôle le payload conservé ; il n’authentifie pas la date de l’index ni l’identité matérielle. Ces marqueurs sont compatibles avec des traitements d’entretien après l’ouverture déclarée, sans renforcer directement la preuve physique du 17. Aucun contenu original supprimé n’a été reconstitué. Les résultats et limites sont détaillés dans [artefacts-transactions.md](recherche-TP-02/investigation-systeme-oct2024/artefacts-transactions.md).

Le recensement des noms retrouve **137 844 objets ordinaires référencés, aucun manquant et aucun orphelin**. Il contrôle la présence des objets actuels, sans récupérer d’anciennes versions écrasées. Le manifeste comporte **78 compagnons WAL/SHM/journal**, mais aucun pour Photos ni les sept bases système ciblées. Les compagnons d’autres applications ne sont pas tous extraits. Le rapport précédent indiquait qu’aucun carving physique n’avait été réalisé ; cela reste exact. La présente recherche d’espaces internes SQLite est limitée et distincte d’une récupération physique générale.

## 10. Connexions à un ordinateur, extraction et rapprochements intersupports

Aucun artefact examiné n’établit un déverrouillage, une connexion USB, un appairage ordinateur ou une extraction en octobre 2024. Les recherches de noms dans le manifeste ont été contrôlées pour leurs faux positifs : répertoires `knowledgeconstructiond`, textes de ressources « pairing », `LockdownMode` et `LockdownParameters` ne constituent pas, par leur seul nom, une base knowledgeC ou une preuve d’appairage USB.

L’existence de la sauvegarde Mac démontre une acquisition logique disponible pour la mission ; elle ne date pas une connexion pendant la rétention. La sauvegarde iOS ne garantit pas un historique complet de connexions ou déverrouillages. L’absence de preuve dans ce périmètre n’exclut pas une lecture ou extraction sans artefact encore conservé.

Les résultats OP-01 peuvent fournir des comparaisons de fichiers, identifiants et horaires. Une recherche exacte de SSID/BSSID dans **193 exports textuels existants**, de taille ≤64 Mio chacun, n’a pas retrouvé les identifiants ASUS ciblés ; ce contrôle exclut un rapprochement dans ces seuls exports, sans reparsage des hives, EVTX binaires ou de l’image. Les [fichiers lus, empreintes et limites](recherche-TP-02/approfondissement-activite-202410/op01-network-comparison.json) sont conservés. Aucune équivalence matérielle entre le réseau ASUS_Z01RD et l’ordinateur OP-01, ni attribution de ses opérations à TP-02, n’est établie. TP-01 et TP-03 n’étaient pas disponibles dans les répertoires inspectés lors de cette campagne initiale. Leurs sauvegardes ont depuis été analysées le 10 novembre ; les [résultats intersupports](../investigations/20261110-telephones/compte-rendu.md) sont désormais intégrés. Les images SD-01/02/03 ont fait l’objet de rapports distincts, qui les associent respectivement à la chambre, à la terrasse et au salon sans identifier avec certitude les modèles de caméra : aucun historique de consultation caméra daté n’a été identifié dans TP-02 pour établir ce rapprochement.

**Complément issu de la campagne OP-01 : un rapprochement nominal est désormais positif.** Le [compte rendu de recherche ASUS_Z01RD](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/compte-rendu.md) documente cinq occurrences ASCII exactes du SSID dans `pagefile.sys`. L’[étude de leur origine](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/origine/interpretation.md) reconstruit des pages compressées dont les champs longueur/SSID et les paramètres associés soutiennent fortement l’interprétation comme listes de réseaux Wi-Fi disponibles. Certaines pages sont des copies du même contenu ; le nombre d’occurrences ne mesure pas des connexions ou détections distinctes.

Ce résultat complète les recherches négatives antérieures, qui portaient sur d’autres ensembles de données. Il établit que **le même nom figure dans les deux acquisitions**, sans identifier un même point d’accès physique. La [recherche de datation OP-01](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/datation.md) ne trouve ni date attribuable aux fragments, ni connexion ASUS dans les événements WLAN ou les profils examinés. La visibilité du réseau sur le PC est fortement soutenue ; sa connexion, le moment de la détection et une présence commune avec TP-02 le 17 ne sont pas démontrés. Les paramètres contrôlés n’établissent pas non plus qu’OP-01 émettait ce réseau. Aucun opérateur n’est attribué.

Les recherches d’accès cloud supplémentaires exigent des données ou journaux correspondants. L’autorisation de connexion distante à la Freebox dans le mail ne vaut pas une autorisation générale de connexion aux comptes caméras ou Apple ; aucune connexion à ces services n’a été réalisée dans cette campagne.

Le contrôle OP-01 a été étendu aux deux **EVTX WLAN bruts déjà extraits**, sans remontage de l’E01. Le fichier actif de 1 052 672 octets présente **1 325 enveloppes d’événements validées**, dans 16 chunks aux CRC cohérents, entre le 28/03/2024 et le 08/10/2026 UTC ; aucune ne porte la date du 17/10/2024. Aucune occurrence littérale du SSID, de la MAC cliente ou des deux BSSID n’est trouvée dans les encodages testés. Le fichier supprimé récupéré n’offre pas d’en-tête ni de chunks validés par ce contrôle. Les empreintes avant/après sont identiques. Il ne s’agit **pas d’un décodage sémantique BinXML** : dates extrêmes et recherches négatives ne prouvent pas une couverture continue ni l’absence de lien OP-01/ASUS. Les [contrôles WLAN bruts et leurs limites](recherche-TP-02/investigation-wifi-17oct2024/op01-raw-wlan-controls.json) complètent les 193 exports textuels, sans attribuer de hotspot à OP-01.

**Recoupement actualisé :** les **27 PDF Mini de L16B, soit 20 contenus distincts, existent à l’identique dans les sauvegardes TP-02 et TP-03**. Ce constat ne départage ni le téléphone source, ni les scellés n° 3/n° 4, ni le sens du transfert, ni l’inclusion dans la copie définitivement saisie. Le fichier d’appairage ancien d’OP-01 est rattaché à TP-03 par l’UDID ; il ne documente pas un branchement de TP-02 en octobre 2024. Voir la [relecture transversale du 10 novembre](../investigations/20261110-telephones/compte-rendu.md).

## 11. Chronologie, méthodes de conversion et niveaux de confiance

### 11.1. Chronologie de synthèse

Les horaires techniques ci-dessous sont exprimés à Paris. Ils sont des observations conservées, distinctes des horaires déclarés de procédure.

| Date ou intervalle | Source | Observation | Interprétation et confiance |
|---|---|---|---|
| 15/10 vers 13:30 | Mail | Perte d’accès déclarée | Déclaration à confronter au PV ; pas heure technique de scellement |
| 15/10 après 14:19 | PV | Mise sous scellés | Heure individuelle de fermeture inconnue |
| 15/10 18:50:48 à 26/10 17:14:34 | CallHistory | 53 dates de début d’appels | Confiance élevée dans la lecture des lignes ; origine locale et opérateur indéterminés |
| 15–28/10 | Photos | 87 dates de création, origines applicatives diverses | Confiance élevée dans les champs ; production sur TP-02 non établie, modèles EXIF iPhone 8 retrouvés |
| 15/10 13:16:55 et 29/10 00:56:41 | WhatsApp | Dernier message précédent et premier suivant ; aucun message dans la fenêtre principale | Couverture de l’instance conservée ; absence d’usage ou de suppression non démontrée |
| 16, 17, 27 et 28/10, selon début | Santé | 73 intervalles : 60 repos, 5 énergie active, 4 pas, 4 distance | Débuts distincts des créations, souvent groupées ; identité reliée à healthd, sans liaison de série historique |
| 17/10 17:15:33 ; entrée datée 17:16:01 | CommCenter | `from_dated`, puis `ts` de remappage `mdn match transfer` | Traitement de libellé ; ni boot ni transfert physique prouvé |
| 17/10 17:15:46,8308 | Diagnostic WidgetKit capturé le 28 | `procLaunch` conservé | Date lue, horloge réelle et matériel producteur non certifiés ; pas un boot ni un déverrouillage |
| 17/10 17:15:48 puis 17:25:37 | Santé | 27 créations : 24 repos, deux objets pas/distance représentant le 15, puis énergie active | Calculs différés et périodes représentées distinctes ; pas de mouvement le 17 démontré par le couple pas/distance |
| 17/10 17:16:01,915835 et 17:16:13,168689 | AddressBook | Deux sauvegardes de séquences ClientSequence | Traitement de client, sans consultation Contacts établie |
| 17/10 17:16:26,884375–,916920 | TipKit Messages | 8 transactions MobileSMS, PK 5490–5497 | Paramètres/règles/tips ; ni SMS lu ni premier plan établi |
| 17/10 17:16:27–28 | Photos, transactions 117245–117246 | Contextes CPL FetchNewEventsFromChangeHub / UploadingBatch | Traitements de bibliothèque, pas preuve d’usage d’ASUS avant le rattachement conservé |
| 17/10 17:18:07,047572–,085727 | TipKit Téléphone | 14 transactions MobilePhone, PK 7291–7304 | Règles traitées ; aucun appel ou geste utilisateur prouvé |
| 17/10 17:25:47–52 | Deux plist Wi-Fi | Chaîne MAC/ajout/premier rattachement, WiFi Settings | Origine locale TP-02 renforcée par la lignée UDID ; état complet restauré non exclu |
| 27/10 02:44–02:45 +02:00 | Photos | 3 123 dates de modification regroupées | Traitement groupé possible ; ne pas confondre les deux occurrences d’heure civile |
| 28/10 10:22 | PV | Arrivée de la cliente | Ce n’est pas l’ouverture des téléphones |
| 28/10 11:30 | PV | Ouverture des téléphones | Les traces suivantes sont après ouverture |
| 28/10 11:39:27 | Préférences Books | `CKStartupTime` dans deux fichiers | Traitement applicatif possible ; pas une heure de boot iPhone établie |
| 28/10 11:57:22 et 12:01:56 | Santé | Création différée d’un intervalle du 17 puis lot de 24 intervalles | Calcul/reprise/import à départager ; ne pas confondre intervalle et écriture |
| 28/10 12:01:49 | Wi-Fi | Dernière découverte conservée ASUS_Z01RD | État réseau, pas présence humaine démontrée |
| 28/10 12:03–12:46 | SMS | Trois SMS entrants avec horodatages `date_read` et `is_read=1` | Lecture humaine locale non établie ; marquage, synchronisation ou restauration possibles |
| 28/10 12:26:28,7192 ; suivi 12:26:29 | Diagnostic WidgetKit | Capture du crash, `uptime=2500`, `wasUnlockedSinceBoot=1`, `isLocked=1` | États au rapport, pas heure de boot ni de déverrouillage ; réserve d’horloge et de transport |
| 28/10 12:31 et 14:32 | Wi-Fi | Associations et connexion système conservées | Après ouverture déclarée ; propriétaire/opérateur inconnus |
| 28/10 13:36:10–14 | Photos, transactions 117456 et 117461 | Séquence SpringBoard puis ScreenshotServices sur Asset 23769 | Opération de capture compatible avec interaction sur appareil source ; attribution physique conditionnelle |
| 28/10 15:50:24,854333–,869329 | Flux SEGB Spotlight/session | 27 tombstones écrits à CRC de payload valide, libellé parsecd | Retrait/entretien interne compatible ; ni suppression humaine ni ancien contenu récupéré |
| 28/10 17:31:38–44 | Préférences, manifeste et transaction Photos 117587 | Rappel CPL puis travail de miniature lié à Asset 23729 | Génération de ressource vérifiée ; vidéo visionnée non démontrée |
| 28/10 17:31:58–17:32:00 | Photos, transactions 117588–117589 | Deux requêtes attribuées à Photos sur un autre actif | Client Photos identifié ; premier plan et visionnage non établis |
| 28/10 17:39:17 | LSC | Cache de panneau et ressources concordantes | Constitution/usage de panneau possible ; consultation caméra non démontrée |
| 28/10 17:40:50 | Xiaomi, manifeste | Dates d’un fichier AppConfig | Métadonnée seule, cause de modification indéterminée |
| 28/10 19:20 | PV et mail | Clôture et restitution approximative déclarée | Pas d’heure individuelle de remise au PV |
| 28/10 19:40:02 | Wi-Fi privé | LinkDownTimestamp | Après restitution déclarée ; ne pas classer dans la rétention |
| 29/10 08:46:45,776 +01:00 | Photos, ACHANGE 1493606 | Conversion candidate de ZTOMBSTONE3 | Hors fenêtre ; sémantique non validée, pas une date certaine de mise à la corbeille |
| 29/11 02:21:38 +01:00 | Photos, transaction 124593 | Purge de maintenance de l’actif de la séquence ScreenshotServices | Hors fenêtre, contexte de disparition actuelle ; motif et mise à la corbeille non établis |

Les observations du 17 et les dates de communications/photos antérieures au 28 ne doivent pas être masquées par une synthèse portant uniquement sur la journée d’ouverture. Inversement, une date du 28 après 11:30 ne démontre pas une activité avant l’ouverture des téléphones.

Pour le rapprochement procédural, distinguer la **perte d’accès déclarée le 15 vers 13:30**, la **mise sous scellés consignée après 14:19, sans heure individuelle de fermeture**, les **opérations après ouverture le 28 à partir de 11:30**, puis les dates **après la récupération déclarée vers 19:20**. Le PV ne fournit pas une heure individuelle de remise. Les traces du 28 à midi et dans l’après-midi sont postérieures à l’ouverture ; leur origine matérielle et l’auteur restent à établir.

Les nouvelles chronologies sont [timeline-new-evidence.csv](recherche-TP-02/investigation-systeme-oct2024/timeline-new-evidence.csv), **49 observations** (deux champs d’un même IPS et 47 métadonnées SEGB), et [sequence-direct-reread.csv](recherche-TP-02/investigation-horloges-widgetkit/sequence-direct-reread.csv), **1 064 propriétés exportées** depuis 58 requêtes et états sélectionnés. La seconde couvre aussi des écritures postérieures à la récupération pour comparaison ; toutes ses lignes ne relèvent pas de la rétention. Ces tableaux complètent les sources précédentes, sans additionner leurs lignes en gestes ou preuves indépendantes.

### 11.2. Valeurs brutes et formats

Les pièces conservent fichier logique, fileID et empreinte lorsqu’ils sont disponibles, table/clé/ligne, valeur, conversion UTC, heure Paris, interprétation et limites. La [chronologie centrale](recherche-TP-02/resultats-finaux-20261014/chronology-central.csv) contient les observations ciblées ; les nombreux champs Photos sont séparés dans leur CSV pour éviter de les présenter comme des actions indépendantes.

La [chronologie corrélée de l’approfondissement](recherche-TP-02/approfondissement-activite-202410/timeline-correlated.csv) rassemble **663 lignes**, avec phase procédurale déclarée, appartenance à la fenêtre et portée de l’empreinte. Pour les dates MBFile, l’empreinte est celle du manifeste et le fileID désigne l’objet référencé. Les débuts/fins/créations Santé et transactions Photos ne sont pas additionnés comme actions humaines.

La [chronologie ciblée du 17 octobre](recherche-TP-02/investigation-wifi-17oct2024/activite-17octobre.csv) contient **98 propriétés/commits**, dont **64 entre 16:45 et 18:00**, avec raw, UTC, Paris, localisateur, fileID, empreinte et limites d’attribution. Ce ne sont ni 98 actions ni des éléments tous indépendants. Les 289 candidats SQL antérieurs de la journée sont conservés séparément : des dates de mesure, d’actif ou synchronisables ne deviennent pas des manipulations locales par leur seul nom. Les [dates binaires Wi-Fi natives](recherche-TP-02/investigation-wifi-17oct2024/wifi-binary-date-validation.json) ajoutent offsets d’objet et hexadécimal des doubles Cocoa à la lecture décodée.

| Format | Méthode | Limite |
|---|---|---|
| Champs MBFile | Hypothèse secondes Unix ; valeur originale conservée | Métadonnées d’instantané, pas journal d’opérations |
| Appels, Photos, Santé | Secondes depuis le 01/01/2001 UTC ; ajout de 978 307 200 pour passage à Unix | Format vérifié par structure et cohérence ; signification/provenance du champ distinctes |
| SMS | Nanosecondes entières depuis la même époque Apple | Brut entier conservé ; affichage tronqué à la microseconde |
| Plist, type date | Date décodée UTC ; pour les deux plist Wi-Fi, contrôle des doubles Cocoa, offsets et octets natifs | Conversion vérifiée pour la séquence du 17 ; l’horloge source historique n’est pas calibrée |
| JSON/colonnes génériques | Essais Unix/Cocoa, secondes ou sous-unités, et ISO avec décalage | Hypothèses de triage ; un nombre compatible peut être un identifiant plutôt qu’une date |
| EXIF sans décalage | Valeur textuelle conservée sans conversion forcée | Fuseau à établir avant rapprochement temporel précis |
| OperatingDates | Année, mois zéro à onze, jour UTC ; intervalle d’un jour | Aucune heure de lancement ou de consultation |
| IPS WidgetKit | Chaînes civiles avec décalage explicite ; compteurs entiers bruts et modèles conditionnels distincts | Échelle proche de 24 MHz soutenue par corpus, fraction exacte non mesurée ; pas de boot calculé ni de calibration civile |

Le niveau de confiance est élevé pour la présence d’un champ lu et reproductible, mais ne se transmet pas automatiquement à son interprétation. Les catégories utilisées sont : **activité automatique possible**, **interaction probable à vérifier**, **événement indéterminé**. Aucune observation n’est présentée comme l’identification d’une personne.

## 12. Reproduction, vérifications et limites restantes

### 12.1. Reproduction des opérations

La [notice des outils](scripts/README-TP-02.md) détaille inventaire et extraction. Les CSV de sélection sont conservés : [caméras et système](recherche-TP-02/inventaire-detaille/inventory.csv), [compléments](recherche-TP-02/selection-complements.csv), [médias](recherche-TP-02/selection-medias-centraux.csv), [WhatsApp](recherche-TP-02/selection-whatsapp.csv). Utiliser des destinations nouvelles pour une reproduction.

```bash
python3 telephones/scripts/tp02_forensic.py inventory --out /tmp/TP02-inventaire-reproduction

# Extraction interactive ciblée : le mot de passe n’est pas un argument.
telephones/scripts/.venv-iphone/bin/python telephones/scripts/tp02_forensic.py extract \
  --inventory telephones/recherche-TP-02/selection-complements.csv \
  --max-priority 2 --out /tmp/TP02-complements-reproduction

python3 telephones/scripts/tp02_forensic.py analyze \
  --extracted /tmp/TP02-complements-reproduction \
  --out /tmp/TP02-analyse-reproduction --row-limit 1000000

python3 telephones/scripts/tp02_media_metadata.py \
  --extracted telephones/recherche-TP-02/extraction-medias-20261014 \
  --out /tmp/TP02-exif-reproduction.json

python3 telephones/scripts/tp02_consistency.py \
  --extracted telephones/recherche-TP-02/extraction-cameras-20261014 \
  --extracted telephones/recherche-TP-02/extraction-systeme-20261014 \
  --extracted telephones/recherche-TP-02/extraction-complements-20261014 \
  --extracted telephones/recherche-TP-02/extraction-medias-20261014 \
  --out /tmp/TP02-coherence-reproduction.json
```

Les tests synthétiques contrôlent chemins de sortie, formats de dates, lecture SQLite avec WAL, conservation des empreintes et absence de mot de passe dans le journal. Le déchiffrement et les analyses ont également été exécutés sur les pièces réelles. Les erreurs de SQLite sont séparées des erreurs d’extraction ; les étapes non décodées ne sont pas présentées comme réussies.

L’approfondissement est reproductible sans mot de passe ni nouveau déchiffrement, avec une destination nouvelle :

```bash
python3 telephones/scripts/tp02_activity_oct2024.py --out /tmp/TP02-activite-reproduction
python3 telephones/scripts/tp02_activity_correlations.py --out /tmp/TP02-activite-reproduction
python3 telephones/scripts/tp02_activity_verify.py \
  --out telephones/recherche-TP-02/approfondissement-activite-202410 \
  --reproduction /tmp/TP02-activite-reproduction
```

Les [contrôles de l’approfondissement](recherche-TP-02/approfondissement-activite-202410/verification-new-campaign.json) retrouvent **18 fichiers de données identiques**, dont les 663 lignes de chronologie, lors d’une seconde exécution ; les journaux d’opérations horodatés sont exclus de cette comparaison. Les **17 cibles** contrôlées ont des empreintes chiffrées/déchiffrées conformes aux journaux d’extraction, avec contrôle avant/après pour les 13 premières. Les couples UTC/Paris, valeurs brutes et absence des identifiants réseau/clé de rotation dans les nouvelles sorties ont été vérifiés. Cette reproduction utilise les mêmes sources et ne vaut pas acquisition indépendante. La [méthode détaillée et les références](recherche-TP-02/approfondissement-activite-202410/methods-and-sources.md) bornent les contrôles et formats non résolus.

L’investigation Wi-Fi du 17 est également reproductible sans nouveau déchiffrement, depuis la racine du projet vers un dossier neuf :

```bash
python3 telephones/scripts/tp02_wifi17_investigation.py --out /tmp/TP02-wifi17-reproduction
python3 telephones/scripts/tp02_wifi17_crosschecks.py --out /tmp/TP02-wifi17-reproduction
```

Une seconde exécution a reproduit **22 fichiers de résultats** : CSV identiques octet pour octet, JSON identiques après exclusion de la seule heure d’exécution dans les journaux. Les **31 sources principales** comprennent 28 fichiers extraits et trois en-têtes : concordance avec les empreintes d’extraction et chiffrées lorsqu’elles existent, sources inchangées avant/après. Les contrôles complémentaires OP-01 et profils ont leur propre traçabilité. Voir [verification-livrables.json](recherche-TP-02/investigation-wifi-17oct2024/verification-livrables.json), [source-verification.json](recherche-TP-02/investigation-wifi-17oct2024/source-verification.json) et [SHA256SUMS.txt](recherche-TP-02/investigation-wifi-17oct2024/SHA256SUMS.txt).

Le balayage borné des fichiers structurés existants sélectionne 3 326 fichiers, en parse 2 996 et conserve 330 erreurs de format ; les fichiers volumineux, formats opaques et traces absentes ne sont pas intégralement couverts. La recherche ciblée au manifeste ne retrouve pas les journaux `.obliterated`, `data_ark`, CurrentPowerLog ou netusage recherchés. Les préférences ne constituent pas un journal complet des restaurations ; **absence de trace n’est pas absence démontrée de restauration**. Les méthodes, faux positifs, limites de versions et protocole témoin non exécuté sont dans [methodes-et-reproduction.md](recherche-TP-02/investigation-wifi-17oct2024/methodes-et-reproduction.md).

Les [contrôles finaux de la campagne système](recherche-TP-02/investigation-systeme-oct2024/verification-livrables.json) indiquent **55 fichiers nouveaux examinés**, aucune extraction sélectionnée en attente, aucune modification constatée aux contrôles et des JSON valides. Les **319 sources principales** comprennent 312 IPS et sept bases ; les nouvelles extractions ont un contrôle distinct sur 55 clairs et chiffrés. La recherche de récupération Photos possède aussi ses propres contrôles. La [notice de reproduction système](recherche-TP-02/investigation-systeme-oct2024/methodes-et-reproduction.md) précise que certains scripts ont une destination fixée : adapter celle-ci dans une copie de travail avant toute reproduction, afin de préserver les résultats livrés.

L’étude horloges possède une [vérification arithmétique distincte](recherche-TP-02/investigation-horloges-widgetkit/independent-verification.json), une [reproduction en destination temporaire](recherche-TP-02/investigation-horloges-widgetkit/reproduction-check.json) retrouvant **22 sorties identiques**, ainsi qu’un [contrôle final des livrables](recherche-TP-02/investigation-horloges-widgetkit/deliverable-verification.json). Ces contrôles valident les calculs et lectures des mêmes preuves, sans créer une observation historique indépendante. Les commandes à destination neuve, dépendances et limites sont dans [méthodes horloges](recherche-TP-02/investigation-horloges-widgetkit/methodes-et-reproduction.md).

**La synthèse antérieure n’avait pas relancé les campagnes d’investigation. Le complément du 19 octobre comporte de nouvelles contre-lectures, documentées séparément.** Elle rapproche leurs rapports, journaux et contrôles conservés. Les mentions « rapport principal inchangé » dans leurs vérifications désignent l’état antérieur à cette synthèse ; elles ne sont pas revendiquées pour la version mise à jour. Les rapports techniques et pièces sources de ces campagnes sont conservés sans réécriture.

### 12.2. Limites empêchant une conclusion plus forte

- **Acquisition de 2026 :** journal Mac, options, historique de sauvegardes/restaurations et copie initiale non disponibles ; dates des fichiers de tête discordantes et tailles MBFile différentes des objets actuels.
- **Provenance :** appels centraux sans identifiants d’appareil discriminants, photos déclarant un iPhone 8 ; identité Santé reliée à healthd mais pas au numéro de série historique. Les transactions d’interface Photos peuvent être transportées par une restauration complète. La lignée Photos est désormais rattachée à l’UDID exact de TP-02 dans sept migrations, mais sa copie et la continuité ininterrompue de toute l’installation restent à départager par des acquisitions comparables.
- **Horloge et procédure :** absence de calibration historique ; PV désormais consulté ; perte d’accès et restitution approximatives, heure de fermeture des scellés inconnue. WidgetKit est compatible avec un modèle de temps système éveillé, sans mesure de sommeil ni correction civile observée ; il ne valide pas la date réelle du Wi-Fi.
- **Applications caméras :** format APM LSC non décodé, paramètres de rétention inconnus, données serveur non disponibles. L’acquisition logique ne contient pas nécessairement les binaires permettant de documenter ces formats.
- **Couverture :** absence d’image physique et de carving physique ; recherche interne SQLite ciblée sans récupération d’image, données supprimées/écrasées non garanties. Les signatures n’ont été recherchées que dans les contenus déchiffrés sélectionnés ; les candidats résiduels ne sont pas tous examinés.
- **SQLite :** 22 contrôles limités par des collations et deux tables virtuelles non entièrement décrites ; BLOB, journaux propriétaires et données temporelles à noms non reconnaissables non exhaustivement décodés.
- **Réseau :** recoupement Freebox réalisé sans attribution des trois iPhone nocturnes ; propriétaire ASUS_Z01RD inconnu ; configurations Wi-Fi d’instantané plutôt que journal continu.
- **Intersupports :** sauvegardes TP-01/03 désormais analysées ; PDF Mini communs aux deux Mini et identités iPhone nocturnes non attribuées. Aucun accès aux enregistrements SD depuis un téléphone scellé n’est établi ; les résultats d’un support ne se transposent pas automatiquement aux autres.

**Les critères d’arrêt atteints concernent les axes et fichiers ciblés, pas l’épuisement de la sauvegarde.** L’audit système recense 52 371 candidats de tri large, dont 9 938 fichiers ordinaires ; seuls les contenus retenus et disponibles ont été examinés. Des candidats restent `unexamined_residual` ou `deprioritized`. La disponibilité de l’historique 2021/2022 n’est pas établie par des préférences anciennes. Les exports Freebox déjà analysés ne restituent pas un audit complet des accès ; les éventuels autres journaux de réseau, caméra ou compte restent à rechercher selon leur disponibilité et leur rétention effective.

Les suites qui nécessitent des éléments externes sont précises : compléter le PV consulté par les documents de conservation/intervention et obtenir le journal d’acquisition Mac ; documenter les appareils Apple utilisés/restaurés et les réglages de synchronisation ; confronter les appels aux relevés opérateur ; confirmer l’usage habituel et l’équipement portant ASUS_Z01RD ; identifier le format et les clés APM de la version LSC concernée ; obtenir, dans le cadre autorisé, les historiques encore conservés des caméras et des comptes associés.

Les vérifications complémentaires sont hiérarchisées par leur capacité à départager les hypothèses. Les détenteurs possibles, voies d’obtention autorisées, limites de conservation et portée d’un résultat positif/négatif sont détaillés dans [preuves-manquantes.md](recherche-TP-02/investigation-wifi-17oct2024/preuves-manquantes.md) ; aucune disponibilité d’archives de 2024 n’est présumée :

1. **Priorité discriminante : retrouver une acquisition contemporaine d’octobre 2024 attribuée indépendamment au TP-02 physique**, contenant déjà les deux états Wi-Fi et les transactions voisines ; elle bornerait une introduction ultérieure. Comparer ensuite les sauvegardes 2024/2025 et autres appareils Apple, en complétant les comparaisons TP-01/TP-03 déjà réalisées à partir des sauvegardes disponibles.
2. Rechercher côté point d’accès un journal d’association à horloge indépendante, avec BSSID et MAC cliente **historiquement** rattachée à TP-02 ; une MAC actuelle seule ne suffit pas. Identifier l’équipement par des éléments indépendants du SSID et de la marque.
3. Obtenir le journal Mac, l’historique de restauration/migration et les documents complétant le PV, notamment les heures individuelles de fermeture et les conditions d’alimentation, de stockage et d’isolement réseau.
4. Tester sur témoins, idéalement iOS 17.6.1, chaque mécanisme Wi-Fi séparément, notamment un transfert différé avec destination éteinte au temps initial : les deux dates privées anciennes et WiFi Settings peuvent-ils être reproduits ? Ce protocole est préparé, non réalisé ; aucun essai sur TP-02. Le test date_read/contexte clavier reste une piste distincte.
5. Rechercher un historique d’horloge contemporain, ou une observation du même boot associant calendrier, compteur absolu et compteur continu avec provenance matérielle établie.
6. Confronter les appels aux données opérateur comportant si disponibles IMEI/IMSI et aux traces téléphonie/UI contemporaines, dans le cadre approprié.

### 12.3. Conservation et restitution

La cliente demande la conservation de **l’ensemble des données extraites sur le cloud du prestataire pendant la durée prévue au devis**, ainsi qu’une copie sur un **disque dur neuf qu’elle fournira**. Les résultats décrits sont conservés localement dans le projet avec accès restreint ; les sources et extractions disposent des contrôles d’empreintes décrits ci-dessus. **Ces opérations locales ne réalisent ni n’attestent les deux copies demandées.**

Avant de déclarer cette demande satisfaite, il reste à documenter la durée du devis, la réception effective du disque, les inventaires de copie cloud/disque et leur contrôle d’intégrité. Le mail et l’attestation ne donnent pas de durée de conservation cloud ; la durée prévue au devis reste non documentée dans les pièces consultées. Le PV est désormais disponible ; il ne remplace pas ces éléments contractuels. Le contrôle cloud du 17 octobre relevait environ **165,22 Go manquants** par rapport aux acquisitions locales, sans régularisation ultérieure attestée dans les documents consultés ; voir l’[annexe D du rapport final](../RAPPORT-FINAL-SADEDINE-2026.md#annexe-d). L’attestation prévoit la restitution de TP-02 au plus tard le **06/11/2026**, selon un mode à convenir.

La cliente demande également un règlement **30 % au démarrage / 70 % à l’achèvement**, en attente de confirmation du prestataire. Cette demande contractuelle est distincte des constats techniques ; son acceptation par les deux parties n’est pas établie par ce rapport.

## 13. Conclusion générale et références techniques

**Nous avons retrouvé des traces informatiques datées de la période où Mme Sadedine déclare ne plus avoir eu TP-02.** Elles concernent notamment des traitements internes, une connexion Wi-Fi enregistrée le **17 octobre vers 17 h 25**, des appels présents dans l’historique et des opérations sur la photothèque. Le **28 octobre**, après l’ouverture déclarée des scellés et avant la récupération déclarée, une séquence est compatible avec le traitement d’une capture d’écran ; d’autres traces concernent les SMS, le Wi-Fi, Photos et l’application LSC Smart Connect.

Ces éléments justifient des vérifications complémentaires. **Ils ne permettent pas encore d’affirmer qu’une personne a utilisé TP-02 sous scellés.** Plusieurs opérations peuvent être automatiques. Des historiques peuvent aussi être synchronisés ou récupérés depuis une sauvegarde, et l’heure affichée par le système n’a pas été vérifiée auprès d’une référence indépendante de l’époque. Le rapport de panne WidgetKit ne résout pas cette question : il ne prouve ni un allumage physique le 17 ni une erreur d’horloge.

**Aucun auteur n’est identifié. Aucune consultation de caméra, extraction par ordinateur en 2024 ou suppression volontaire de preuve n’est démontrée.** L’image correspondant à la possible capture d’écran n’a pas été récupérée. Les cinq occurrences du nom `ASUS_Z01RD` sur OP-01 constituent une piste de rapprochement avec le téléphone, sans date commune, connexion du PC ou point d’accès physique commun établis.

Pour aller plus loin, il faut surtout rapprocher ces constats des **procès-verbaux**, de l’**historique des sauvegardes et restaurations**, et des **journaux réseau encore disponibles**. Les demandes concernant la Freebox, les cartes SD et les copies cloud/disque doivent être suivies séparément. **La conclusion demeure : des traces d’activité existent ; leur attribution certaine à TP-02 à la date réelle, à une intervention humaine et à une personne reste à établir.**

### Références techniques et pièces détaillées

Les références suivantes soutiennent les formats et les explications alternatives ; les constats propres à TP-02 proviennent des pièces locales citées :

- [Apple — Date.timeIntervalSinceReferenceDate](https://developer.apple.com/documentation/foundation/date/timeintervalsincereferencedate-swift.property) : époque du 01/01/2001 UTC.
- [iLEAPP — CallHistory](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/callHistory.py) : référence de parsing, non exécution du logiciel complet dans cette campagne.
- [iLEAPP — Wi-Fi plist](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/appleWifiPlist.py) : structures et champs Wi-Fi de référence.
- [WebKit — OperatingDate](https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/Classifier/ResourceLoadStatisticsStore.h) et [magasin de statistiques](https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/Classifier/ResourceLoadStatisticsStore.cpp) : mois zéro à onze, jour UTC et enregistrement automatique ; version historique de l’appareil non auditée.
- [Apple — synchronisation Téléphone/FaceTime](https://support.apple.com/en-lamr/guide/icloud/mmc2662aa6e0/1.0/icloud/1.0) : possibilité de partage d’historiques entre appareils, sans preuve de son activation historique dans ce dossier.
- [Apple — iCloud Photos](https://support.apple.com/en-ie/108782) : synchronisation des photos et modifications, distincte de leur attribution à un appareil.
- [libheif — métadonnées EXIF](https://github.com/strukturag/libheif/blob/master/libheif/api/libheif/heif_metadata.h) : lecture des blocs de métadonnées, sans affichage des images.

Les huit livrables de l’investigation du 17 sont : [continuité iOS](recherche-TP-02/investigation-wifi-17oct2024/continuite-ios.md), [mécanismes Wi-Fi Apple](recherche-TP-02/investigation-wifi-17oct2024/mecanismes-wifi-apple.md), [comparaison des réseaux](recherche-TP-02/investigation-wifi-17oct2024/comparaison-reseaux.csv), [chronologie du 17](recherche-TP-02/investigation-wifi-17oct2024/activite-17octobre.csv), [recoupements Santé/Photos](recherche-TP-02/investigation-wifi-17oct2024/recoupements-sante-photos.md), [hypothèses contradictoires](recherche-TP-02/investigation-wifi-17oct2024/hypotheses-contradictoires.md), [preuves manquantes](recherche-TP-02/investigation-wifi-17oct2024/preuves-manquantes.md) et [conclusion technique](recherche-TP-02/investigation-wifi-17oct2024/conclusion-technique.md). Les [références consultées](recherche-TP-02/investigation-wifi-17oct2024/references-consultees.json) sont qualifiées dans les études : documentation générale, parseur, expérimentation sur autre version ou observation locale ne sont pas confondus. Les expériences sur témoins restent à réaliser.

Les références et pièces complémentaires de l’approfondissement sont rassemblées dans [methods-and-sources.md](recherche-TP-02/approfondissement-activite-202410/methods-and-sources.md). En particulier :

- [Apple — NSPersistentHistoryTransaction](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction) : transactions et contextes de changements, distincts des gestes.
- [iLEAPP — Santé](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/health.py) : recoupement des codes de types et structures.
- [Apple — synchronisation sécurisée du trousseau](https://support.apple.com/en-au/guide/security/sec0a319b35f/web) et [sauvegardes chiffrées](https://support.apple.com/en-ie/108353) : voies possibles d’import, sans preuve de leur rôle historique ici.
- [SQLite — WAL](https://www.sqlite.org/wal.html), [Backup API](https://www.sqlite.org/backup.html) et [VACUUM](https://www.sqlite.org/lang_vacuum.html) : distinction entre base active, instantané et copie reconstruite ; aucune de ces opérations n’a été exécutée sur les sources pour l’approfondissement.

Les rapports système et horloges sont également intégrés dans les sections correspondantes. Leurs points d’entrée sont :

- [Constats système priorisés](recherche-TP-02/investigation-systeme-oct2024/findings-priorises.md), [conclusion système A–H](recherche-TP-02/investigation-systeme-oct2024/conclusion-technique.md) et [méthodes système](recherche-TP-02/investigation-systeme-oct2024/methodes-et-reproduction.md).
- [Lecture brute WidgetKit](recherche-TP-02/investigation-horloges-widgetkit/widgetkit-raw-analysis.md), [référentiels Apple et sources conservées](recherche-TP-02/investigation-horloges-widgetkit/apple-clock-semantics.md), [recherche de corrections](recherche-TP-02/investigation-horloges-widgetkit/clock-anomalies.md), [hypothèses des horloges](recherche-TP-02/investigation-horloges-widgetkit/hypotheses-contradictoires.md), [incidence Wi-Fi](recherche-TP-02/investigation-horloges-widgetkit/impact-sur-wifi-17oct.md), [conclusion horloges A–H](recherche-TP-02/investigation-horloges-widgetkit/conclusion-technique.md) et [méthodes horloges](recherche-TP-02/investigation-horloges-widgetkit/methodes-et-reproduction.md).

Les sources externes déjà consultées lors des campagnes décrivent des formats ou mécanismes généraux, avec les limites de version indiquées dans ces études. La présente relecture n’ajoute pas de recherche externe ni d’expérience sur témoin.
