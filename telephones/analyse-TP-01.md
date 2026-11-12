# Analyse informatique du téléphone TP-01

**Relecture de cohérence : 12 novembre 2026.** Harmonisation avec le [rapport final réorganisé](../RAPPORT-FINAL-SADEDINE-2026.md), sans nouvelle acquisition ni nouvelle analyse des supports. Les campagnes et décomptes techniques conservent leurs dates et leurs périmètres. Le détail de cette révision et les empreintes actuelles figurent dans le [dossier de relecture](../investigations/20261112-coherence-rapports/compte-rendu.md).

## Revue du 10 novembre 2026 — intervention avant ouverture

Le contrôle complémentaire sur SIFT, limité au 15 octobre 14:19 → 28 octobre 11:30, ne retrouve aucune ligne SMS par date de message, lecture ou livraison. La base d’appels et le fichier `known-networks` sont absents des chemins contrôlés : ce ne sont pas des résultats « zéro appel » ou « zéro connexion ». Les résultats WhatsApp, cloud et Wi-Fi de secours ci-dessous restent applicables. Aucune interaction locale avant ouverture n’est établie. Voir la [comparaison des hypothèses et les nouveaux contrôles](../investigations/20261110-revue-intervention-scelles/compte-rendu.md). Les versions antérieures de ce rapport sont conservées pour cette mise à jour.

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Analyse :** 10 novembre 2026 — sauvegarde logique, sans nouvelle acquisition du téléphone.

## 1. Conclusions expliquées simplement

**L’analyse retrouve des données portant des dates comprises dans la conservation déclarée, mais ne permet pas d’établir une utilisation du téléphone physique TP-01 entre sa mise sous scellé et l’ouverture du 28 octobre 2024 à 11 h 30. Elle ne permet pas non plus de certifier qu’il est resté éteint.**

La distinction est essentielle : la date d’un message, d’un fichier cloud ou d’une ressource téléchargée peut être conservée alors que cette donnée arrive sur le téléphone beaucoup plus tard. À l’inverse, l’absence d’un journal dans une sauvegarde ne prouve pas l’absence d’activité.

Les principaux résultats sont les suivants :

- Deux messages WhatsApp entrants portent des dates du **15 octobre à 16:51:24 et 17:41:48**. Leur autre champ temporel, `ZSENTDATE`, se situe le **28 octobre vers 16:13:08**, avec un groupe d’autres messages plus anciens. L’ensemble est compatible avec une récupération différée ; il ne prouve pas que TP-01 a reçu ou affiché ces messages le 15.
- Des messages vocaux portent des dates du **15, du 17 et du 19 octobre**. Ils sont conservés dans une table appelée `deleted`, mais ces dates ne sont pas des dates de suppression. Aucun geste de consultation ou de suppression sous scellé n’en est déduit.
- Des dates du **23 octobre** figurent dans les métadonnées iCloud Drive, à la fois dans les magasins client et serveur. Elles ne localisent pas l’action sur TP-01. Des ressources de traduction/configuration et des fichiers de cache d’applications portent également des dates pendant l’intervalle ; leur provenance locale n’est pas établie.
- **Après l’ouverture du 28**, plusieurs magasins système enregistrent des traitements à partir de **14 h 26** ; WhatsApp présente deux lignes sortantes vers **17 h 44**. Ces indices sont plus compatibles avec une reprise d’activité après ouverture, sans identification de l’opérateur ni preuve autonome de l’appareil physique à l’origine de chaque donnée.
- Aucune date de message natif ou de lecture, ni date de création, ajout, modification, retouche, mise à la corbeille ou partage des photos, n’a été trouvée dans les champs contrôlés pour la fenêtre du **15 octobre à 13 h 30 au 28 à 19 h 20**.
- Le fichier Wi-Fi courant est vide ; sa copie de secours contient **37 réseaux**, aucun nommé `ASUS_Z01RD`, et aucune des **423 dates plist** décodées ne tombe dans cette fenêtre. Cela ne prouve pas l’absence de toute connexion ancienne.

**Aucune rupture de scellé, extraction clandestine, intrusion ni identité d’auteur n’est démontrée.** Les résultats propres à TP-02 ne doivent pas être transférés à TP-01.

**Observation de visionnage rapportée le 12 novembre :** le prestataire indique voir une agente de l’administration fiscale rallumer les téléphones le **15 octobre vers 13 h 25**, avant le scellement. Le [rapport final, § 1.2](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés) distingue ce récit du contrôle antérieur d’images d’un clip débutant à 13 h 28. Aucun nouveau visionnage indépendant n’est effectué ici ; le récit ne précise pas l’état final à la fermeture et ne démontre aucune continuité d’alimentation jusqu’au 28. Un fonctionnement automatique reste compatible, sans établir l’origine physique des traces de la sauvegarde.

## 2. Identification, sources et fenêtres d’examen

### 2.1. Identification

| Élément | Constat |
|---|---|
| Code de l’attestation | TP-01 — iPhone 13 vert, modèle commercial `MNGK3ZD/A` |
| Série de l’attestation et de `Info.plist` | **Q13QT4F164**, concordance exacte |
| Type matériel dans la sauvegarde | `iPhone14,5` |
| UDID de la sauvegarde | `00008110-000A70993407801E` |
| Version déclarée par `Info.plist` lors de la sauvegarde | `26.6.2`, build `23G90` ; ce n’est pas la version établie pour octobre 2024 |

Le PV décrit un **iPhone 13 noir** pour le scellé n° 2, tandis que l’attestation décrit TP-01 comme vert. Le modèle fait de TP-01 un candidat, mais cette divergence et l’absence de série/IMEI dans les passages du PV contrôlés empêchent d’affirmer une correspondance matérielle certaine. Les codes TP et les numéros de scellés restent distincts.

### 2.2. Pièces et bornes

Sources : [rapport de méthode TP-02](analyse-TP-02.md), [mail initial](../docs/mail.txt), [complément de la cliente](../docs/mail-2.txt), [attestation de remise](../remise-documents/attestation-de-remise.md), [lecture du PV et références de pages](../investigations/20261108-analyse-pv/compte-rendu.md), sauvegarde TP-01 et résultats SIFT ci-dessous.

| Période | Portée |
|---|---|
| 15 octobre 2024 vers 13 h 30 | Perte d’accès aux téléphones déclarée par la cliente ; pas une heure de scellement vérifiée |
| 15 octobre, après le repère de 14 h 19 du PV, p. 25 du PDF | Mise sous scellés consignée, sans seconde de fermeture individuelle |
| 28 octobre à 11 h 30, PV p. 9 | Ouverture des trois téléphones et déverrouillage par la cliente |
| 28 octobre à 19 h 20, PV p. 13 | Clôture ; restitution consignée sans heure individuelle ; 19 h 20 est aussi l’heure approximative déclarée de récupération |
| Fenêtre large de recherche | 1er octobre au 15 novembre 2024 inclus |

La recherche utilise une fenêtre centrale large du **15 à 13 h 30 au 28 à 19 h 20**. L’interprétation distingue le scellement, l’ouverture à 11 h 30 et les opérations postérieures. Une date du 28 après 11 h 30 ne constitue pas, par elle-même, une activité sous scellé fermé.

Toutes les conversions sont faites en **Europe/Paris** : UTC+2 avant le changement du 27 octobre, UTC+1 ensuite. Aucun étalonnage de l’horloge de 2024 n’est disponible.

## 3. Sauvegarde examinée et préservation

Chemin source sur l’hôte :

```text
/mnt/data/forensic/SADEDINE-2026/TP-01/00008110-000A70993407801E/
```

Sur SIFT, le même partage est accessible sous `/media/shared/forensic/SADEDINE-2026/TP-01/…`. Le partage est monté en lecture-écriture par l’environnement ; **les scripts n’écrivent pas dans la source**. Les analyses utilisent des copies dans `/home/sansforensics/analysis/tp01-20261110/`, avec permissions restrictives. Il ne s’agit pas d’une image physique ni d’une acquisition contemporaine de 2024.

| Métadonnée | Valeur enregistrée, UTC |
|---|---|
| `Manifest.plist.Date` | 09/11/2026 11:31:28.171107 |
| `Status.plist.Date` | 09/11/2026 11:48:09.677857 |
| `Info.plist.Last Backup Date` | 09/11/2026 11:48:23 |
| État | `IsEncrypted=false`, `IsFullBackup=false`, `BackupState=new`, `SnapshotState=finished` |

Ces dates et états sont ceux des fichiers de sauvegarde ; ils ne remplacent pas un journal indépendant d’acquisition. `IsFullBackup=false` est conservé comme valeur, sans déduire à lui seul que des objets seraient absents.

Le manifeste contient **78 457 entrées** : **48 895 fichiers `flags=1`**, 29 487 entrées `flags=2` et 75 `flags=4`. Les **48 895 objets attendus sont présents** ; les tailles déclarées totalisent **12 648 356 415 octets**. La présence n’est pas une authentification cryptographique exhaustive de tous leurs contenus.

La collecte initiale couvre **2 420 objets**, soit **620 310 196 octets**, incluant bases SQLite, compagnons et préférences sélectionnées. Un complément conserve le Wi-Fi de secours et onze ressources `.ahe`. Les empreintes SHA-256 de chaque objet collecté sont comparées avant/après lecture à celles de sa copie. Les quatre fichiers de tête ont également des empreintes identiques avant, après et sur copie.

Empreinte SHA-256 du manifeste source :

```text
ab12f937dc0a6d1c1ca15312a8c3a9faf1322e8d44fa5e68b4dd18e8676ca0a8
```

Le manifeste satisfait `quick_check=ok`. **877 fichiers portent une signature SQLite** dans la collecte : **826 contrôles `quick_check` donnent `ok`**, 51 restent incomplets en raison de collations/tokenizers spécifiques indisponibles. Ce sont des limites d’outillage, pas 51 corruptions démontrées. La seconde passe lit leurs tables ordinaires lorsque possible, sans inventer une collation de remplacement. Les tables virtuelles ne sont pas interprétées dans ce tri.

Les compagnons SQLite sont recueillis avec les bases. Les copies sont ouvertes en `mode=ro`, sans `immutable=1` pour les bases d’activité, afin de permettre la prise en compte des WAL présents. Aucune fusion n’est faite dans la source. **355 des bases à signature SQLite disposent d’un WAL collecté.**

## 4. Communications et traces datées pendant la conservation

### 4.1. SMS et iMessage

`HomeDomain/Library/SMS/sms.db` contient **2 561 messages**. Pour les champs `date`, `date_read`, `date_delivered` et `date_played`, aucune valeur ne tombe dans la fenêtre centrale après conversion des nanosecondes depuis le 01/01/2001.

Le dernier message conservé avant la fenêtre porte la date du **12 octobre à 13:42:09.661421** (`ROWID=642`) ; le premier après porte celle du **17 novembre à 16:56:32.189545** (`ROWID=613`). L’ordre des ROWID n’est donc pas utilisé comme une chronologie d’arrivée. La base ne permet pas de reconstituer exhaustivement les communications de cet intervalle ni d’exclure des suppressions ou une importation d’historique.

### 4.2. WhatsApp

Les magasins WhatsApp ordinaire et Business contiennent respectivement **15 473** et **10 lignes** dans `ZWAMESSAGE`. Business ne livre aucune date centrale dans les champs examinés. Les valeurs brutes et indicateurs du magasin ordinaire sont exportés sans corps de conversation.

| `Z_PK` | `ZMESSAGEDATE`, heure de Paris | `ZSENTDATE`, heure de Paris | Indicateur et portée |
|---|---|---|---|
| 10051 | 15/10 16:51:24 | 28/10 16:13:08.424826 | `ZISFROMME=0`, type 0 ; ne démontre pas une réception locale le 15 |
| 10050 | 15/10 17:41:48 | 28/10 16:13:08.426692 | `ZISFROMME=0`, type 0 ; même réserve |
| 10052 | 28/10 16:13:09.009604 | Non renseigné | Type 10 ; ne pas compter automatiquement comme une conversation humaine |
| 10053 | 28/10 17:44:24.344572 | 28/10 17:44:24.401593 | `ZISFROMME=1`, type 0, statut 6 ; ligne sortante après ouverture |
| 10054 | 28/10 17:44:54.357658 | 28/10 17:44:54.391634 | `ZISFROMME=1`, type 0, statut 6 ; ligne sortante après ouverture |
| 10055 | 28/10 17:57:57 | 28/10 23:24:42.795958 | Entrante ; second champ postérieur à la clôture et à la restitution déclarée |

**Quatorze lignes datées du 15 dans `ZMESSAGEDATE` ont un `ZSENTDATE` groupé le 28 entre 16:13:07.674380 et 16:13:08.426692.** Cette différence soutient une récupération ou un traitement différé ; le nom `ZSENTDATE` ne suffit pas à prouver une heure de réception locale ou de lecture. Les deux dates du 15 après le scellement ne démontrent donc pas une activité matérielle à ces heures. Aucune date de message conservée du 16 au 27 n’est trouvée dans ces deux champs. L’index de recherche reprend des dates des messages et n’est pas une seconde source indépendante.

Les lignes sortantes du 28 sont des indices d’activité du compte après ouverture ; ni l’auteur ni l’appareil source exclusif ne sont établis. Le contrôle des bases d’appels WhatsApp ne trouve pas de date dans la fenêtre centrale. **L’historique natif `CallHistory.storedata` n’est pas présent dans le manifeste.**

### 4.3. Messagerie vocale

Dans `HomeDomain/Library/Voicemail/voicemail.db`, sept lignes de `deleted` portent une `date` centrale : **15/10 13:32:24 et 16:18:54 ; 17/10 12:08:42 et 15:37:40 ; 19/10 15:58:55 ; 28/10 18:06:28 et 19:08:38**. Les `trashed_date` de ces lignes valent **0**.

Il s’agit de dates associées aux messages vocaux, pas d’une datation de leur suppression. Une messagerie opérateur peut conserver un message lorsque le téléphone n’est pas joignable. Ces lignes ne démontrent ni un appel décroché sur TP-01, ni une écoute ou une suppression pendant le scellement. L’état `deleted` est celui conservé dans la sauvegarde de 2026, sans reconstitution de la transition vers cet état.

## 5. Wi-Fi, cloud et ressources applicatives : provenance à distinguer

### 5.1. Wi-Fi

`SystemPreferencesDomain/SystemConfiguration/com.apple.wifi-networks.plist` est un dictionnaire vide. Le contrôle de sa **copie `.plist.backup`**, collectée séparément pour ne pas omettre ce suffixe, retrouve **37 réseaux** et **423 valeurs de date plist**. Aucune ne tombe dans la fenêtre centrale ; `ASUS_Z01RD` n’y figure pas.

Ce fichier conserve un état partiel de réseaux connus, pas un journal exhaustif de toutes les associations. Il ne justifie ni d’affirmer une absence de Wi-Fi en octobre, ni de répliquer la connexion du 17 trouvée dans TP-02.

### 5.2. iCloud Drive, 23 octobre

Les bases `CloudDocs/session/db/client.db` et `server.db` contiennent chacune **deux `item_birthtime`** au **23 octobre à 09:39:06 et 09:47:07**, un `version_mtime` à **09:47:07**, et **dix `item_lastusedtime`** entre **09:39:31 et 09:41:38**. Ce sont des champs de métadonnées d’objets cloud ; la présence dans les deux bases n’en fait pas deux observations indépendantes d’un geste local.

La table `devices` conserve trois noms d’iPhone. Les dix lignes portant un `item_lastusedtime` du 23 sont associées, dans le champ de version contrôlé, à `version_device=1`, nommé **« iPhone de MALIKA »** ; le nom déclaré de TP-01 lors de la sauvegarde est **« iPhoneun. Nscz s »**, également présent comme autre entrée de cette table. Ces noms peuvent changer et ne remplacent pas des UDID. `version_device` ne prouve pas quel appareil a produit `item_lastusedtime`. **Aucune attribution matérielle au téléphone scellé n’est établie.**

### 5.3. Dates de ressources applicatives

Le tri repère notamment **1 050 valeurs `last_timestamp`** centrales dans `multi_language` de l’application `com.ctrip.EBooking`, et une valeur `timestamp` au **22 octobre à 05:31:33** dans une configuration CargoSDK (`grade3_switch`). Les schémas décrivent des traductions et des paramètres, pas un historique d’utilisation. Des dates de version de ressources distantes peuvent être recopiées ultérieurement ; aucune session d’application à ces dates n’est prouvée.

Le manifeste conserve aussi **28 valeurs Birth/LastModified pour 14 fichiers AliExpress** entre le 15 et le 24 : onze modules `.ahe`, deux PNG et un JSON. Les dates Birth et LastModified sont identiques pour chacun. Les onze `.ahe` ont été copiés et contrôlés ; ce ne sont pas des ZIP reconnus et leur format interne n’a pas été décodé. **La possibilité d’écritures locales anciennes reste ouverte**, mais ces dates isolées ne départagent pas création locale, conservation de dates de ressources, restauration ou import. Elles ne sont pas écartées comme nécessairement automatiques.

## 6. Activité du 28 octobre après ouverture

Les tables de transactions système et les préférences montrent une séquence enregistrée après **11 h 30** :

| Heure de Paris | Source et constat | Limite |
|---|---|---|
| 14:26:41 puis 16:47:01 | Quatre transactions TipKit du composant Calendrier | Traitements internes ; pas quatre consultations |
| 14:31:35 | Préférence `homed`, `hh1LastSharedUserAddRemoveTimestamp` | Champ lié à un état de partage ; ne démontre pas un ajout de tiers ni un accès aux caméras |
| 14:31:36–16:21:54 | 28 transactions TipKit de Messages | Aucun SMS central conservé dans `sms.db` ; ce ne sont pas 28 SMS |
| 14:31:42–14:31:57 | Transactions Notes, Mail et Rappels | Traitements possibles en arrière-plan |
| 14:32:21 puis 14:39:07 | Transactions Téléphone puis Safari | Ne prouvent ni appel ni site effectivement consulté |
| 16:13:07–16:13:09 | Regroupement de dates WhatsApp | Compatible avec un traitement différé des messages |
| 16:17:17 | Quatre transactions TipKit de Fichiers | Pas une preuve d’export de quatre fichiers |
| 16:18:23 | Trois ressources WeChat avec `consumeTime` daté | Sens fonctionnel exact non validé ; pas trois messages |
| 16:59:23.299 | `accessoryd.plugin.plist`, valeur `uartDetachTimes/1` interprétable en millisecondes Unix | Compatible avec une information de détachement d’accessoire ; aucun identifiant d’ordinateur, outil ou extraction établi |
| 17:44:24 et 17:44:54 | Deux lignes WhatsApp sortantes | Activité du compte après ouverture, sans auteur établi |
| 17:51:40 | Sept transactions TipKit de Photos | Pas sept photographies prises ou consultées |

Treize lignes de `TCC.db` conservent également une modification d’état d’autorisation du 28 entre **14:26:13 et 17:51:40**. Elles concernent notamment des services iCloud et différentes applications ; ce ne sont ni des ouvertures d’applications certifiées, ni un journal de déverrouillages.

La concordance de plusieurs magasins est compatible avec une reprise de services le 28, sans exclure une restauration globale ou une origine commune des dates. Aucun compteur de démarrage ni journal continu ne permet de dater un allumage. Le PV fournit le contexte d’examen et de copies ; les données ne permettent pas d’identifier un outil d’extraction ou son opérateur.

## 7. Photos, profils et limites de couverture

La photothèque contient **6 455 lignes `ZASSET`**. Aucune valeur centrale n’est présente dans les six champs contrôlés : `ZDATECREATED`, `ZADDEDDATE`, `ZMODIFICATIONDATE`, `ZADJUSTMENTTIMESTAMP`, `ZTRASHEDDATE`, `ZLASTSHAREDDATE`. Toutes les valeurs `ZTRASHEDDATE` sont nulles dans cet état. Cela ne prouve pas l’absence de photos supprimées avant la sauvegarde. Aucune capture du 28 analogue à celle discutée pour TP-02 n’est mise en évidence.

Le manifeste ne contient ni `healthdb`, ni `knowledgeC.db`, ni `interactionC.db`, ni diagnostic `.ips`, ni domaine LSC Smart Connect ou Xiaomi Home correspondant aux recherches de noms. Leurs historiques ne peuvent donc pas servir ici de contrôle équivalent à celui de TP-02. L’absence d’un artefact dans une sauvegarde logique n’est pas une preuve qu’il n’a jamais existé sur l’appareil.

Le `ProfileTruth` utilisateur est vide. Celui du système contient une entrée `com.apple.Free_fr.…`, avec des catégories de restrictions ; sa seule présence ne démontre pas une gestion MDM hostile. L’examen ne fournit pas un historique des profils ou appareils associés depuis 2021. Le seul chemin `Library/LockdownMode` ne constitue pas un fichier d’appairage Apple avec un ordinateur. Aucune session datée d’un outil d’extraction n’est identifiée par les recherches de noms et les artefacts décodés ; un outil laissant peu de traces ou un journal omis par la sauvegarde reste possible.

## 8. Méthode, résultats conservés et reproduction

Les scripts adaptent la démarche TP-02 : inventaire complet du manifeste, copies sélectives avec empreintes, signature réelle des bases, contrôle des schémas, tri temporel, puis validation ciblée des champs. L’environnement SIFT utilise **Python 3.12.3 et SQLite 3.45.1**. Aucun déchiffrement n’est nécessaire pour TP-01. Les scripts refusent un dossier de résultats déjà existant.

Le tri numérique explore secondes Unix/Apple, millisecondes et microsecondes Unix, nanosecondes Unix/Apple, pour les colonnes dont les noms évoquent une date ou un temps. Les résultats de ce tri sont des **candidats**, pas des événements validés. Il n’est exhaustif ni des chaînes de dates, ni des BLOB, ni des formats propriétaires ou données supprimées. Les conclusions ci-dessus reposent sur les champs et schémas explicitement cités. Les dates plist natives sont traitées comme UTC ; les dates de manifeste comme secondes Unix, avec réserve de provenance.

Exemple de reproduction sur SIFT, depuis un chemin de projet accessible, avec un **nouveau** dossier de destination :

```bash
python3 telephones/scripts/tp01_inventory.py SOURCE NOUVELLE_DESTINATION
python3 telephones/scripts/tp01_scan.py NOUVELLE_DESTINATION NOUVELLE_DESTINATION/scan
python3 telephones/scripts/tp01_targeted.py NOUVELLE_DESTINATION
python3 telephones/scripts/tp01_supplement.py NOUVELLE_DESTINATION SOURCE
```

Résultats privés locaux : [inventaire et empreintes](recherche-TP-01/summary.json), [objets collectés](recherche-TP-01/collection.json), [tri SQLite corrigé](recherche-TP-01/scan-v2/timestamp-stats.json), [erreurs et limites SQLite](recherche-TP-01/scan-v2/errors.json), [communications et contrôles ciblés](recherche-TP-01/targeted/whatsapp.json), [contrôles complémentaires](recherche-TP-01/supplement-v2/results.json), [dates Wi-Fi](recherche-TP-01/supplement-v2/wifi-dates.json). Les copies de contenu demeurent sur SIFT ; les JSON et archives de résultats sont rapatriés dans `recherche-TP-01/`, exclu de Git et à accès restreint. Le complément a été reproduit avec les bornes exactes dans `supplement-v2` : ses résultats structurés sont identiques à la première passe, conservée séparément. Aucun mot de passe ni contenu de conversation n’est reproduit dans ce rapport.

## 9. Réponse à la question de la conservation sous scellé

**Présence de données datées pendant la conservation : oui. Fonctionnement local de TP-01 avant l’ouverture : non établi. Manipulation humaine ou rupture de scellé : non établie.**

Les pistes à conserver sont les métadonnées AliExpress, les objets cloud du 23 et les messages datés pendant la conservation. Leur portée reste limitée par la sauvegarde de 2026 et par la possibilité de réception différée, synchronisation ou restauration. Les traces système et sortantes du 28 se situent après l’ouverture documentée. Leur présence ne permet pas de reporter cette activité aux journées précédentes.

Pour aller au-delà, les pièces discriminantes seraient une acquisition plus proche de 2024, des journaux d’acquisition/restauration, des identifiants persistants des appareils cloud, des relevés opérateur et les documents de conservation/intervention. Aucun de ces compléments n’est présumé disponible. **On ne peut pas conclure que TP-01 était actif sous scellé, ni certifier son inactivité, à partir de cette seule sauvegarde.**
