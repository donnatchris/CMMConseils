# Analyse informatique du téléphone TP-03

**Relecture de cohérence : 12 novembre 2026.** Harmonisation avec le [rapport final réorganisé](../RAPPORT-FINAL-SADEDINE-2026.md), sans nouvelle acquisition ni nouvelle analyse des supports. Les campagnes et décomptes techniques conservent leurs dates et leurs périmètres. Le détail de cette révision et les empreintes actuelles figurent dans le [dossier de relecture](../investigations/20261112-coherence-rapports/compte-rendu.md).

## Revue du 10 novembre 2026 — intervention avant ouverture

La revue contradictoire maintient la séquence du 16 à 05:31 comme indice de traitements système, sans marqueur humain discriminant. Le contrôle complémentaire SIFT des bases natives SMS et appels ne sélectionne aucune ligne dans la fenêtre du 15 octobre 14:19 au 28 octobre 11:30 ; leur ancienneté interdit d’en faire une garantie d’inactivité. Aucun `JoinedByUserAt` natif n’est sélectionné dans le fichier de réseaux connus. La piste humaine la plus informative de la comparaison demeure TP-02, sans transfert de ses résultats à TP-03. Voir la [comparaison des hypothèses et les nouveaux contrôles](../investigations/20261110-revue-intervention-scelles/compte-rendu.md). Les versions antérieures de ce rapport sont conservées pour cette mise à jour.

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Analyse :** 10 novembre 2026 — sauvegarde logique chiffrée, sans nouvelle acquisition du téléphone.

## 1. Conclusions expliquées simplement

**Oui, TP-03 conserve des indices de traitements système datés pendant la période de conservation sous scellé. Le plus informatif est un enchaînement de plusieurs magasins le 16 octobre 2024, entre 05:31:33 et 05:31:39, heure de Paris.** Ce résultat mérite une confrontation aux conditions de conservation des appareils. Il ne constitue pas une preuve certaine d’utilisation du téléphone physique à ces heures, de manipulation humaine ou de rupture du scellé.

Le constat ne repose pas seulement sur la date d’un message ancien : deux créations d’objets Santé sont suivies d’une tentative interne CloudKit et de huit transactions du composant Messages. **L’approfondissement identifie un échec CloudKit sans objet traité et un mécanisme TipKit dont le profil se répète dans 40 autres séquences. Aucun affichage des trois conseils concernés ni déverrouillage n’est attesté.** Cela est compatible avec des traitements automatiques, sans exclure qu’une intervention ait pu les déclencher. Une copie/restauration peut transporter un historique, et l’horloge de 2024 n’est pas étalonnée. Voir l’[étude approfondie de l’intervention humaine](../investigations/20261110-tp03-intervention-humaine/compte-rendu.md).

| Résultat principal | Portée |
|---|---|
| **15 octobre, 18:33:26–18:36:27** | Deux dates plist natives dans des champs `routined` de registration/désinscription GNSS ; indices système après le scellement consigné, sans position géographique ni déplacement établis |
| **16 octobre, 01:40:51** | Date native dans une préférence `mediaremote` ; sémantique exacte du champ non validée |
| **16 octobre, 05:31:33–05:31:39** | Santé, magasin PersonalAudio et TipKit Messages : séquence cohérente, sans preuve de déverrouillage, d’envoi ou de lecture de SMS |
| **27 PDF Mini de L16B identiques dans TP-03** | Tous ont un équivalent SHA-256 exact, comme dans TP-02 ; ce contenu commun ne départage donc pas les deux Mini |
| **Appairage ancien avec OP-01** | Le nom du pair record conservé sur le PC contient exactement l’UDID TP-03 ; aucune connexion d’octobre 2024 n’en est datée |
| Wi-Fi et communications | Pas de réseau `ASUS_Z01RD` dans les fichiers Wi-Fi contrôlés ; les SMS et appels natifs conservés s’arrêtent en juin 2024, ce qui limite fortement leur usage comme contre-épreuve pour octobre |

**Aucun auteur, outil d’extraction, accès distant non autorisé ou geste humain sous scellé n’est identifié.** L’absence de messages d’octobre ne neutralise pas les traces système du 16 et ne prouve pas que l’appareil était éteint.

**Observation de visionnage rapportée le 12 novembre :** le prestataire indique voir une agente de l’administration fiscale rallumer les téléphones le **15 octobre vers 13 h 25**, avant le scellement. Le [rapport final, § 1.2](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés) distingue ce récit du contrôle antérieur d’images d’un clip débutant à 13 h 28. Aucun nouveau visionnage indépendant n’est effectué ici ; le récit ne précise pas l’état final à la fermeture et ne démontre aucune continuité d’alimentation jusqu’au 28. Un fonctionnement automatique reste compatible, sans établir l’origine physique des traces de la sauvegarde.

## 2. Identification, sources et chronologie de procédure

### 2.1. Identification de la sauvegarde

| Élément | Valeur |
|---|---|
| Code de mission | TP-03 — iPhone 13 mini rouge |
| Série de l’attestation et de `Manifest.plist/Lockdown` | **Y4Q9KGHG26**, concordance exacte |
| Modèle commercial de l’attestation | `MLK83F/A` |
| Type produit de la sauvegarde | `iPhone14,4` |
| UDID de la sauvegarde | **00008110-001249321444801E** |
| Système déclaré dans les métadonnées de sauvegarde | iOS **17.5.1** ; ne suffit pas seul à établir la version à chaque date de 2024 |
| Fichier de tête absent | **Info.plist** : identification par les champs Lockdown du manifeste, pas par un Info reconstitué |

L’attestation indique TP-03 **non remis le 6 octobre 2026**. La sauvegarde est disponible lors de la présente analyse ; cela ne documente pas à soi seul une date ultérieure de remise du matériel. Le champ « IMEI » de 19 chiffres de l’attestation reste une transcription à vérifier.

Le PV distingue deux Mini rouges sans donner leurs séries/UDID. **TP-03 ne peut pas être identifié avec certitude comme scellé n° 3 ou n° 4.** Le fichier d’appairage ancien et les PDF communs ne lèvent pas cette limite.

### 2.2. Sources et fenêtres

Sources : [méthode TP-02](analyse-TP-02.md), [demandes initiales](../docs/mail.txt), [complément de la cliente](../docs/mail-2.txt), [attestation](../remise-documents/attestation-de-remise.md), [lecture du PV](../investigations/20261108-analyse-pv/compte-rendu.md), sauvegarde TP-03 et dérivés SIFT. Les pages **7, 9, 11, 13, 19 et 25 du PDF du PV** ont été revérifiées visuellement le 10 novembre. Le PDF conserve son SHA-256 historique `18928481d246c8dff907dcebb37dc3133289b291d0007c2c5900613b8c780db3`.

- **15 octobre vers 13 h 30 :** perte d’accès déclarée ; pas une heure vérifiée de scellement.
- **15 octobre après le repère de 14 h 19, PV p. 25 :** mise sous scellés consignée ; heure individuelle de fermeture non donnée.
- **28 octobre à 11 h 30, PV p. 9 :** ouverture des téléphones et déverrouillage par la cliente. L’insertion SIM à 11 h 45 concerne le scellé n° 3, sans équivalence TP-03 démontrée.
- **28 octobre à 19 h 20, PV p. 13 :** clôture ; restitution consignée sans horaire individuel. La cliente situe également sa récupération vers 19 h 20.

La fenêtre centrale de recherche est **15/10/2024 13:30–28/10/2024 19:20 Paris**. Les interprétations distinguent l’avant-scellement, la conservation avant ouverture et les opérations après ouverture. Comparaison : **1er octobre–15 novembre inclus**. Conversions en `Europe/Paris`, UTC+2 puis UTC+1 à partir du changement du 27 ; aucune calibration historique du téléphone n’est revendiquée.

## 3. Support examiné, déchiffrement et contrôles

Source sur l’hôte :

```text
/mnt/data/forensic/SADEDINE-2026/TP-03/00008110-001249321444801E/
```

Sur SIFT, le même partage est sous `/media/shared/forensic/SADEDINE-2026/TP-03/…`. Le partage est accessible en écriture par l’environnement ; **les scripts ouvrent les sources en lecture et écrivent exclusivement dans les dossiers de travail**. Aucun changement du téléphone ni nouvelle sauvegarde n’est effectué.

| Métadonnée | Valeur conservée |
|---|---|
| `Manifest.plist.Date` | **17/09/2025 15:54:45.596360 UTC** |
| `Status.plist.Date` | **17/09/2025 16:50:54.990956 UTC** |
| État | `IsEncrypted=true`, `IsFullBackup=false`, `BackupState=new`, `SnapshotState=finished` |
| `Info.plist` | Absent dans la source inspectée |

Ce sont les dates déclarées par ces fichiers, **pas une certification de la date de création matérielle de toute la copie**. L’absence d’Info et du journal d’acquisition réduit la documentation de provenance. L’état `finished` et la présence des objets sont contrôlés séparément, sans assimiler `IsFullBackup=false` à des objets nécessairement manquants.

Le déchiffrement utilise `iphone_backup_decrypt` **0.11.2**, avec `pycryptodome` **4.4.0**, dans un dossier de dépendances séparé sur SIFT ; Python **3.12.3**, SQLite **3.45.1**. L’essai de création d’un environnement venv a échoué faute d’`ensurepip` ; les dépendances ont ensuite été installées dans un répertoire de travail, sans modifier les preuves. Le mot de passe fourni a été saisi via `getpass`, sans écho, et n’est pas écrit dans les scripts ou les rapports.

Le manifeste contient **177 695 entrées** : **117 865 fichiers `flags=1`**, 59 470 entrées `flags=2` et 360 `flags=4`. Les **117 865 objets attendus sont présents** ; les tailles du manifeste totalisent **106 595 164 370 octets**. Ce total est déclaratif et n’est pas une mesure des octets déchiffrés ni une vérification cryptographique de toute la sauvegarde.

La collecte générale déchiffre **4 632 objets**, **1 820 972 351 octets**, sans échec. Une passe prioritaire indépendante déchiffre **396 objets**, dont les bases natives, des états caméra et **26 PDF candidats**. Les **62 objets communs aux deux passes ont des SHA-256 chiffrés et déchiffrés identiques**. L’union représente donc **4 966 fileID distincts** ; les deux passes ne sont pas additionnées sans déduplication. **32 contrôles ciblés** revérifient sources et clairs ; les cinq Digest SHA-1 disponibles correspondent aux objets chiffrés. Les écarts chiffrement/clair sont de 1 à 16 octets. Pour Santé et Photos, les tailles SQLite d’en-tête correspondent aux tailles extraites, malgré les écarts MBFile.

Empreintes SHA-256 du manifeste :

```text
Source chiffrée : e99a859fe1ed8dcd682eb15b10ec9ab61ac0cbc9d36bd26e734f751ca194c768
Copie déchiffrée : 334123a803c20b59c9610b459b8769a07d24cab7ea805e35c6f64caec65f365c
```

Les trois fichiers de tête présents et les objets collectés ont des empreintes source avant/après identiques. Le manifeste déchiffré donne `quick_check=ok`. **525 objets généraux présentent une différence entre taille MBFile et taille déchiffrée** ; aucun n’est tronqué artificiellement pour rejoindre la taille annoncée. Cette anomalie de cohérence est conservée et n’est pas assimilée à une falsification.

**1 548 contenus ont une signature SQLite**, dont **1 432 `quick_check=ok`** ; les **116 contrôles incomplets** correspondent à des collations/tokenizers absents (`IDBKEY`, `REVID`, etc.), sans preuve de corruption déduite. Les tables ordinaires lisibles restent examinées ; les tables virtuelles ne sont pas prétendues intégralement décodées. **1 095 bases disposent d’un WAL collecté**. Les copies sont ouvertes en lecture seule avec leurs compagnons ; les sources chiffrées ne sont pas modifiées.

## 4. Séquence du 16 octobre : les indices les plus informatifs

### 4.1. Les faits datés

| Heure Paris le 16/10, UTC+2 | Artefact et localisateur | Constat |
|---|---|---|
| **05:31:33.935058** | `Health/healthdb_secure.sqlite`, objet **348331**, type 8 | Création d’un objet de distance ; intervalle représenté le **15 à 13:14:16.834842–13:14:49.933610** |
| **05:31:33.945574** | Même base, objet **348332**, type 7 | Création d’un objet de pas sur le même intervalle du 15 |
| **05:31:35.372222–05:31:35.420874** | `Accessibility/com.apple.personalaudio.sqlite`, `ANSCKEVENT.Z_PK=31013` | Échec de préparation CloudKit, type 0, `ZSUCCEEDED=0`, erreur 134400, zéro objet traité ; aucune écoute ou capture sonore démontrée |
| **05:31:39.196280–05:31:39.252170** | TipKit Messages, `ATRANSACTION.Z_PK=1217–1224` | **Huit transactions** attribuées à `MobileSMS`, bundle `com.apple.MobileSMS` |

Trois règles TipKit (`Z_PK=132–134`) portent aussi des `ZLASTEVALUATED` dans cette dernière fraction de seconde. Les règles et transactions sont liées, **pas onze observations indépendantes**.

**La séquence associe plusieurs magasins en environ 5,3 secondes.** Elle étaye des traitements de services sur l’installation source, avec la même réserve de transport et d’horloge que pour TP-02. Les huit transactions ne sont ni huit SMS, ni huit lectures, ni huit déverrouillages. Une reprise ou tâche automatique est compatible avec les données ; aucun démarrage ni geste humain n’est directement enregistré.

Les deux objets Santé ne décrivent **aucun déplacement du 16** : ils reprennent des mesures du 15 avant le repère de mise sous scellés. C’est leur **date de création d’objet**, distincte de celle des mesures, qui constitue ici la piste du 16.

### 4.2. Provenance Santé et continuité logique

Les objets sont joints à `data_provenances.ROWID=166` : produits origine/local `iPhone14,4`, build `21F90`, source **17.5.1**, `Europe/Paris`, `sync_provenance=0`, `sync_identity=2`, appareil 49. L’identifiant matériel logique de cette identité Santé correspond exactement à `com.apple.healthd.plist/SyncIdentityHardwareIdentifier` dans la sauvegarde.

Ce rapprochement rattache les objets à l’identité Santé de l’installation sauvegardée. **Il ne lie pas de façon infalsifiable cette identité à la série matérielle en octobre 2024.** Le `localIdentifier` de l’appareil Santé est vide. La ligne de source 1 garde un ancien produit `iPhone9,3` et une autre identité, tandis que les provenances des objets et l’appareil 49 indiquent `iPhone14,4` : cet héritage interdit d’assimiler le seul drapeau `local_device=1` à une preuve matérielle exclusive.

Photos conserve **18 migrations**, dont deux nomment exactement l’UDID TP-03 : **27/04/2024 à 05:03:56** (build `21E236`) et **03/06/2024 à 06:30:21** (`21F90`), avec modèle matériel `D16AP` et le même UUID de bibliothèque que les migrations héritées. Cela renforce la continuité d’une lignée logique avant octobre. Il n’existe pas ici une chaîne de migrations encadrant octobre et établissant une continuité matérielle ininterrompue jusqu’à la sauvegarde.

La préférence MobileBackup conserve une restauration au **29 octobre 2021**, et Setup Assistant une sortie au **11 juin 2024**. Ces états hérités ne documentent pas un transport explicatif après les événements d’octobre ; ils ne l’excluent pas non plus. Une restauration de 2021 ne peut pas, à elle seule, expliquer l’arrivée de traces encore futures de 2024.

### 4.3. Ce qu’il reste impossible de départager

| Hypothèse | Éléments et limites |
|---|---|
| TP-03 a fonctionné automatiquement le 16 vers 05:31 | Séquence cohérente Santé/PersonalAudio/Messages, avec identité logique liée à healthd ; absence de journal de démarrage ou d’association radio matériellement attribué |
| Une personne a manipulé TP-03 | Possible, mais aucun écran, déverrouillage, SMS envoyé/lu ou geste n’est établi par cette séquence |
| Des historiques ont été transportés plus tard | Les copies peuvent conserver des transactions et dates ; aucun transport postérieur explicatif n’est positivement identifié par ces pièces |
| Une horloge source était incorrecte | Possibilité non exclue ; aucune correction civile contemporaine ni référence indépendante ne permet de la quantifier |

La répétition de dates cohérentes dans plusieurs magasins n’est pas un étalonnage indépendant s’ils partagent la même horloge ou ont été copiés ensemble.


### 4.4. Approfondissement : la séquence permet-elle d’identifier une intervention humaine ?

**Non : les recherches supplémentaires ne valident pas cette attribution et ne permettent pas non plus de l’exclure.** Les résultats détaillés figurent dans le [complément consacré à cette question](../investigations/20261110-tp03-intervention-humaine/compte-rendu.md).

- Les huit transactions 1217–1224 décrivent **14 changements de conseils/règles/paramètres**, liés à `ktWaitingForCloud`, `isEligibleForOnboarding` et `updateAppleID`. Aucun changement de message ou donation d’événement utilisateur n’y figure. Les trois conseils liés ont `ZLASTDISPLAYED=NULL` ; une autre ligne du magasin possède un affichage renseigné, mais aucun affichage du 16 n’est attesté.
- Le même profil de huit transactions/quatorze changements apparaît dans **41 groupes au total, dont celui-ci**, selon un regroupement par écarts de deux secondes au plus pour le même auteur. Les **40 autres occurrences**, notamment trois avant scellement le 15, montrent un mécanisme récurrent. Elles ne sont pas des témoins expérimentaux d’utilisation humaine ou automatique.
- L’événement PersonalAudio dure **48,652 ms**, échoue et traite zéro objet. Il ne prouve ni transfert ni Internet ; le code brut n’est pas traduit en cause certaine. Les créations Santé reprennent des mesures du 15 avec un retard d’environ 16 h 17 : leur présence ne vaut pas journal d’authentification.
- La recherche sans filtre de noms de colonnes parcourt **1 548 bases, 10 985 tables et 47 770 colonnes numériques ou non explicitement textuelles/BLOB** pour le 16. Elle ne fournit aucun nouvel indice au-delà des sources connues. Les treize payloads quotidiens Apple sont **vides**.
- Deux artefacts supplémentaires d’usage sont déchiffrés. ATX livre **45 entrées entièrement délimitées : une base SQLite valide et 44 plists**. Ni les dates examinées de ces modèles ni l’état récent SpringBoard décompressé n’apportent de témoin d’interaction du 16. Leur rétention est partielle : derniers états, une seule ligne de séquence de lancement, anciens ancrages.
- **2 493 plists** sont parsés ; les trois exceptions sont reprises séparément, dont `sleepd` bloqué par une date sentinelle hors plage. Aucun déverrouillage, démarrage ou alarme déclenchée à 05:30 le 16 n’est identifié. Les magasins réseau et interaction contrôlés s’arrêtent en juin, ce qui empêche une contre-épreuve fiable pour octobre.

La cliente situe le rallumage vers 13:30 ou un peu avant ; le prestataire rapporte le 12 novembre un visionnage le situant vers **13:25**, sans contrôle indépendant supplémentaire dans cette révision. L’état final à la fermeture reste non établi. Si une extinction à la fermeture était prouvée indépendamment, le scénario d’un appareil demeuré allumé devrait être écarté ; une production locale de la séquence supposerait alors une reprise à expliquer.

Les classes de protection du manifeste et les mécanismes documentés de HealthKit autorisent certains traitements verrouillés ou différés. Une vidange de données à l’occasion d’un déverrouillage reste également possible. **Aucun de ces mécanismes généraux ne transforme `creation_date` en preuve d’un nouveau déverrouillage le 16.** Aucun démarrage daté, écran au premier plan, geste ou opérateur ne tranche. Le complément distingue les possibilités documentées des observations propres à cette sauvegarde.

## 5. Autres dates pendant la conservation et faux positifs à éviter

### 5.1. Préférences système du 15 au 16

| Date et heure Paris | Source et clé | Portée |
|---|---|---|
| 15/10 13:30:32 et 13:34:13 | Créations Santé d’énergie, objets 348329–348330 | Avant le scellement consigné après 14:19 ; pas une activité sous scellé fermé démontrée |
| 15/10 13:35:42 | `user_model_database.sqlite/last_update_date` | Métadonnée du modèle clavier ; aucun texte saisi attribué |
| 15/10 13:40:52 | TCC, autorisation iCloud de `com.apple.Music` | Changement d’état d’autorisation, sans ouverture humaine certifiée |
| 15/10 13:41:02 | PeopleSuggester, `DeviceIdDate` | Date d’un état technique, pas identité d’une personne ni preuve de consultation |
| 15/10 13:50:40 | Deux préférences CoreDuet | Dates d’entretien/retrait interne ; ne démontrent pas une suppression de données utilisateur |
| **15/10 18:33:26.915492** | `com.apple.routined.plist/RTDefaultsIntermittentGNSSLastRegistrationDate` | Date native après le scellement consigné |
| **15/10 18:36:27.578715** | Même fichier, `RTDefaultsIntermittentGNSSLastUnregistrationDate` | Deuxième date native, environ trois minutes plus tard |
| **16/10 01:40:51.941617** | `com.apple.mediaremote.plist/MRDPQPDS.PED` | Date native ; sémantique exacte du champ non validée |

Les deux champs `routined` sont des indices d’un état lié à la gestion du GNSS, **pas des coordonnées, un trajet, une preuve de sortie des locaux ou une heure de GPS activé par une personne**. Leur signification fonctionnelle précise n’est pas validée par un journal runtime indépendant. Le champ `mediaremote` n’est pas traduit en lecture musicale ou télécommande démontrée.

### 5.2. Échéances et dates de contenu

Les préférences globales contiennent `INNextFreshmintRefreshDateKey` au **16 octobre à 13:13:33** et `INNextHeartbeatDate` au **21 à 05:34:00**, sous conversion Cocoa. Le libellé **Next** désigne des échéances : **ce ne sont pas des exécutions constatées**, comme le réveil programmé d’OP-01 ne prouve pas un réveil réel.

Le magasin Apple `PegasusConfiguration/AlpsWarehouse` comporte treize dates centrales, notamment des repères quotidiens à minuit UTC. Le contrôle approfondi établit que leurs treize payloads centraux ont une longueur de zéro octet ; ils ne prouvent pas un fonctionnement quotidien. Le nom de ce composant Apple ne constitue pas une identification du logiciel espion Pegasus.

Deux dates de configuration de clés Facebook sont conservées les **18 et 26 octobre à 22:00:14** ; une date de contenu Santé vise le **24**, et le calendrier contient des occurrences du **27**. Ce sont des pistes de métadonnées ou de contenu ; sans provenance runtime validée, elles ne sont pas comptées comme autant d’utilisations locales.

Six intervalles d’énergie Santé commencent le **28 octobre entre 09:09 et 18:24**, mais leurs créations d’objet sont enregistrées **le 29**. Ils ne prouvent donc pas des écritures ou un allumage de TP-03 avant l’ouverture du 28 à 11 h 30.

## 6. Communications, photos, Wi-Fi et caméras

### 6.1. Communications et photothèque

L’historique natif conserve **305 appels**, du **8 avril au 24 juin 2024**, dernier début à **12:06:00** le 24 juin. `sms.db` contient **73 457 messages**, dont le dernier `date` est au **24 juin 2024 à 15:12:28.867429**. Aucun appel ni date de message/lecture/livraison dans les champs contrôlés ne tombe dans la fenêtre centrale.

Cette couverture s’arrête avant octobre : **elle ne permet pas de confirmer ou d’infirmer l’insertion SIM du 28, ni d’exclure tout usage du téléphone**. Aucun code Apple d’octobre n’est identifié dans ces lignes conservées. Le présent contrôle ne prétend pas récupérer tous les messages supprimés.

Photos contient **21 814 actifs**. Aucune date centrale n’est trouvée dans `ZDATECREATED`, `ZADDEDDATE`, `ZMODIFICATIONDATE`, `ZADJUSTMENTTIMESTAMP`, `ZTRASHEDDATE` ou `ZLASTSHAREDDATE`, ni dans `ATRANSACTION.ZTIMESTAMP`. Cela ne prouve pas l’absence de photos ou de captures supprimées, ou d’historiques exclus de la sauvegarde.

### 6.2. Réseau

Les préférences Wi-Fi contiennent **11 réseaux connus**, **11 entrées privées** et une copie historique de **69 réseaux** ; le fichier historique courant `wifi-networks.plist` est vide. Aucun `ASUS_Z01RD` ni date centrale ne ressort des préférences Wi-Fi décodées. L’instantané n’est pas un journal complet d’associations.

Une adresse privée de TP-03, **C6:A2:88:AC:F8:CB**, correspond exactement à une fiche Freebox au nom UUID. Les dates de cette fiche concernent **septembre 2025**, pas octobre 2024. Les trois adresses iPhone nocturnes du **16–17 octobre 2024** restent sans correspondance dans les identifiants clients exploitables des sauvegardes examinées ; aucun identifiant Wi-Fi client exploitable n’a été retrouvé pour TP-01. Une rotation de MAC ou la perte des anciens états empêche d’en faire une exclusion matérielle certaine. Voir le [recoupement transversal](../investigations/20261110-telephones/compte-rendu.md).

### 6.3. Applications caméra et diagnostics

LSC Smart Connect et Xiaomi Home sont présents dans le manifeste. Des configurations, bases, préférences et ressources non multimédias ont été déchiffrées ; cela ne reconstitue pas un historique exhaustif de visionnage, de partage ou d’accès distant. Les formats opaques ne sont pas interprétés comme des bases SQLite sur leur seule extension. Les magasins WebKit OperatingDates conservent respectivement **263 jours LSC et 18 jours Xiaomi**, s’arrêtant aux **10 et 11 juin 2024 UTC** après conversion des mois codés de zéro à onze ; aucun jour d’octobre 2024. Les **96 valeurs time** du cache LSC `__access_time__.json` s’arrêtent au **12 juin 2024 à 03:24 Paris**, sans valeur centrale. Ces états ne sont pas des historiques exhaustifs de visionnage. Aucun accès à un compte ni à une caméra en fonctionnement n’a été effectué.

La sauvegarde conserve **92 diagnostics `.ips` nommés d’avril à juin 2024** ; aucun nom de diagnostic d’octobre n’a été trouvé dans cet ensemble. Le contrôle de leurs métadonnées est conservé dans les vérifications finales. Aucun uptime d’octobre n’est utilisé pour inventer une heure de démarrage. `knowledgeC.db`, CurrentPowerLog et netusage ne sont pas trouvés sous les noms recherchés ; `interactionC.db` est présent et compris dans le tri SQLite.

Les recherches de noms de pair records et de plusieurs outils d’extraction/télécommande ne fournissent pas de session identifiée d’octobre. `LockdownMode/metadata.plist` et `ConfigurationProfiles/LockdownParameters.plist` ne sont pas des fichiers d’appairage avec un ordinateur. Une recherche de noms ne détecte pas tous les outils inconnus, renommés ou les traces omises par une sauvegarde logique.

## 7. Rapprochements avec OP-01 et TP-02

### 7.1. Fichier d’appairage ancien

Le fichier **`ProgramData/Apple/Lockdown/00008110-001249321444801E.plist`** d’OP-01, documenté lors de la campagne du 19 octobre, désigne exactement l’UDID désormais identifié pour TP-03. Le SHA-256 de la chaîne UDID est `ccb3428f115ef6f7c6c5a9aa09385cf511792867fb4355ebe72c42e19d2bacef`, identique à celui du contrôle antérieur. Le fichier avait pour SHA-256 `a6eb37fd5aac553440132a381550e4ee9fe960b7b6820fe37576eb32d1bfa930`.

La MFT **113002** conserve une création SI au **04/07/2022 à 13:19:51 Paris**, une création FN et modification au **14/12/2023 à 16:43:30 Paris** ; les dates ne sont pas fusionnées en un premier appairage certain. Le `SystemBUID` concordait avec la configuration Apple du PC. **L’identification du téléphone est nouvelle ; les dates et octets du pair record restent ceux de l’analyse antérieure**, sans prétendre à une nouvelle acquisition d’OP-01.

Cela étaye une relation de confiance conservée avec TP-03. **Aucune connexion le 15 ou le 28 octobre 2024, extraction ou identité d’opérateur n’est datée par ce fichier.**

### 7.2. Les PDF Mini ne départagent plus aucun des deux appareils

Les **26 PDF candidats déchiffrés de TP-03** fournissent un équivalent SHA-256 exact à **chacune des 27 entrées PDF de L16B/IPHONE13_MINI**, lesquelles représentent **20 contenus binaires distincts**. Le même résultat de contenu commun était déjà acquis pour TP-02.

**La correspondance binaire est donc commune aux deux sauvegardes : elle ne permet pas de choisir le Mini physiquement extrait le 28**, ni le sens du transfert, sa date initiale ou l’appareil sur lequel un document a été consulté. Elle ne prouve pas non plus que les documents figurent dans le jeu définitivement saisi, distinct de L16B laissé sur le PC.

La comparaison et les chemins restent en annexe privée. Les dates NTFS SI du 15/FN du 28 déjà décrites ne deviennent pas des dates d’extraction certifiées de TP-03. Les documents peuvent exister sur plusieurs supports par copie, partage ou synchronisation ; le mécanisme exact reste à déterminer.

## 8. Reproduction, pièces et limites

Dossiers SIFT : `/home/sansforensics/analysis/tp03-20261110/` et `/home/sansforensics/analysis/tp03-priority-20261110/`. Leurs copies de contenu sont à accès restreint. Les résultats sont rapatriés dans [recherche-TP-03](recherche-TP-03/), exclu de Git. Les JSON conservent champs bruts, requêtes, localisateurs et empreintes ; les synthèses n’exportent ni mots de passe, ni valeurs médicales, ni corps des conversations.

Scripts : [collecte chiffrée](scripts/tp03_collect.py), [sélection prioritaire et PDF](scripts/tp03_priority.py), [tri SQLite](scripts/tp01_scan.py), [requêtes natives](scripts/tp03_findings.py), [préférences](scripts/telephones_plists.py), [corrélations](scripts/tp03_correlations.py), [contrôles finaux](scripts/tp03_final_checks.py), [rapprochements entre appareils](scripts/telephones_crosschecks.py). La passe prioritaire utilise les fonctions de déchiffrement de la version 0.11.2 après vérification exacte par fileID ; son résultat est confronté à la passe générale utilisant l’API d’extraction par chemin.

Pièces principales : [inventaire/traçabilité](recherche-TP-03/summary.json), [collecte](recherche-TP-03/collection.json), [tri temporel](recherche-TP-03/scan/timestamp-stats.json), [erreurs SQLite](recherche-TP-03/scan/errors.json), [Santé](recherche-TP-03/priorite/findings/health.json), [préférences datées](recherche-TP-03/plists/dates.json), [transactions du 16](recherche-TP-03/correlations/results.json), [PDF communs](recherche-TP-03/priorite/pdf-identities.json). Les [contrôles finaux](recherche-TP-03/final-checks/native-integrity.json) et [métadonnées caméra](recherche-TP-03/final-checks/camera-webkit.json) complètent ces pièces ; la [notice](scripts/README-TP-01-TP-03.md) détaille l’ordre et les destinations neuves.

Le tri numérique teste les époques Unix/Apple et plusieurs unités, puis valide les schémas et champs retenus. Il reste limité aux colonnes et formats pris en charge ; les BLOB, charges propriétaires, bases avec extensions manquantes et secteurs supprimés ne sont pas intégralement interprétés. Trois plist échouent au parseur standard ; l’approfondissement les reprend explicitement : une vide, une XML avec année 0000 et `sleepd` avec une date sentinelle hors plage. Les autres dates récupérées ne donnent pas d’événement du 16. La collecte d’un fichier n’équivaut pas à son interprétation complète.

**Limites déterminantes :** sauvegarde tardive portant des dates de 2025, Info absent, journal d’acquisition manquant, historique de restauration incomplet, horloge de 2024 non étalonnée, métadonnées et transactions transportables, absence d’image physique et de journal continu des démarrages/déverrouillages/liaisons radio. Aucun historique serveur ou relevé opérateur n’est réputé disponible. Aucune conclusion juridique n’est tirée.

## 9. Réponse à la question des scellés

**Des indices positifs existent : préférences système du 15 au soir et du 16, puis séquence Santé/PersonalAudio/Messages du 16 à 05 h 31.** Ils sont plus informatifs qu’une simple date de contenu reçue à distance et justifient des vérifications sur la conservation des téléphones.

**L’utilisation physique de TP-03 aux dates civiles indiquées reste non certifiée ; l’intervention humaine et la rupture de scellé ne sont pas démontrées. L’approfondissement confirme des traitements internes récurrents et un échec CloudKit, sans marqueur validé d’action humaine. L’absence de manipulation ne peut pas davantage être démontrée.** Aucun artefact de cette campagne ne permet d’affirmer « le téléphone a été déverrouillé par telle personne ». Le résultat ne permet pas davantage de certifier que TP-03 est resté éteint.

Les pièces les plus discriminantes seraient une acquisition antérieure attribuée au matériel, un journal contemporain de démarrage/radio à horloge indépendante, l’historique de restauration, les documents de conservation et un rapprochement des séries avec les scellés. L’appairage ancien et les PDF communs sont des rapprochements utiles ; ils ne remplacent pas ces pièces.
