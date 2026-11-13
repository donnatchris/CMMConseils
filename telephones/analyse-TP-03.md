# Rapport d’analyse technique du téléphone TP-03

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev

**Équipement :** iPhone 13 mini — série `Y4Q9KGHG26`

## 1. Objet et synthèse

Ce rapport présente les indices d’activité conservés dans la sauvegarde de TP-03 pendant la rétention du **15 au 28 octobre 2024**, leur provenance, les communications et les rapprochements avec les autres supports. Il distingue les traitements système, les contenus datés, leur attribution au matériel et les éventuels gestes humains.

**La séquence la plus informative est enregistrée le 16 octobre entre 05:31:33 et 05:31:39, heure de Paris : deux créations Santé, un échec interne CloudKit et huit transactions de conseils du composant Messages. Elle étaye des traitements logiciels sur l’installation source, sans établir un déverrouillage, un geste humain ou une activité du téléphone physique à une heure civile certifiée.**

| Résultat | Conclusion permise |
|---|---|
| **15 octobre à 18:33–18:36**, préférences GNSS ; **16 à 01:40**, préférence `mediaremote` | États système datés après le repère de scellement, sans position, trajet ou lecture multimédia démontrés. |
| **16 octobre à 05:31**, Santé/PersonalAudio/TipKit | Séquence cohérente, compatible avec des traitements automatiques ; leur déclencheur reste inconnu. |
| Huit transactions Messages, quatorze changements | Gestion de conseils/règles, profil retrouvé dans **40 autres séquences** ; ni huit SMS ni affichage des conseils démontrés. |
| Communications natives arrêtées en juin 2024 | Aucun événement d’octobre sélectionné, mais couverture insuffisante pour exclure l’usage du téléphone. |
| **27 PDF Mini de L16B**, vingt contenus distincts, identiques dans les deux Mini | Contenu commun non discriminant entre TP-02 et TP-03 ou entre les scellés n° 3/n° 4. |
| Pair record d’OP-01 portant l’UDID TP-03 | Relation de confiance ancienne conservée ; aucune connexion d’octobre 2024 datée. |

**Aucun auteur, accès distant non autorisé, outil d’extraction ou rupture de scellé n’est identifié. L’absence de manipulation n’est pas davantage démontrée et le maintien du téléphone à l’état éteint n’est pas certifié.**

## 2. Identification et repères de procédure

### 2.1. Identité de la sauvegarde

| Élément | Valeur |
|---|---|
| Code de mission / attestation | **TP-03**, iPhone 13 mini rouge |
| Série de l’attestation et de `Manifest.plist/Lockdown` | **Y4Q9KGHG26**, concordance exacte |
| Modèle commercial | `MLK83F/A` |
| Type produit | `iPhone14,4` |
| UDID | **`00008110-001249321444801E`** |
| Système déclaré dans les métadonnées | iOS **17.5.1**, sans certification de la version à chaque date historique |
| Fichier de tête absent | **`Info.plist`** ; l’identification repose sur les champs Lockdown du manifeste. |

L’[attestation](../remise-documents/attestation-de-remise.md) indique TP-03 non remis le 6 octobre 2026. La disponibilité de la sauvegarde ne date pas une remise ultérieure du matériel. Le champ « IMEI » transcrit sur 19 chiffres reste à vérifier.

Le PV distingue deux Mini rouges sans série ou UDID : **TP-03 ne peut pas être attribué avec certitude au scellé n° 3 ou n° 4**. L’appairage ancien et les PDF communs ne résolvent pas cette attribution.

### 2.2. Fenêtres et horloges

Les [mails](../docs/mail.txt), le [complément de la cliente](../docs/mail-2.txt) et la [lecture du PV](../investigations/20261108-analyse-pv/compte-rendu.md) donnent les repères suivants :

| Date et heure de Paris | Portée |
|---|---|
| **15 octobre vers 13:30** | Perte d’accès déclarée, pas une heure vérifiée de fermeture. |
| **15 octobre après 14:19** | Mise sous scellés consignée, sans fermeture individuelle précisément horodatée. |
| **28 octobre à 11:30** | Ouverture des téléphones et déverrouillage par la cliente. |
| **28 octobre à 11:45** | Insertion SIM dans le scellé n° 3, sans attribution TP-02/TP-03 certaine. |
| **28 octobre à 19:20** | Clôture ; restitution consignée sans heure individuelle, récupération approximative déclarée vers 19:20. |

La **fenêtre centrale de recherche** va du **15 à 13:30 au 28 à 19:20** ; elle comprend donc des opérations après ouverture. Le contrôle spécifique avant ouverture utilise **15 octobre 14:19 inclus → 28 octobre 11:30 exclu**, sans présumer une fermeture effective de tous les appareils à 14:19. La comparaison couvre le **1er octobre au 15 novembre inclus**.

Les conversions utilisent **Europe/Paris**, UTC+2 puis UTC+1 après le changement du 27 octobre. L’horloge source de 2024 n’est pas étalonnée indépendamment ; des magasins proches peuvent partager la même horloge et être transportés ensemble.

## 3. Sauvegarde, déchiffrement et fiabilité des données

### 3.1. Source et couverture

La source logique chiffrée est conservée sous `TP-03/00008110-001249321444801E/` dans le dossier forensic. Il ne s’agit pas d’une image physique ou d’une acquisition contemporaine de 2024.

| Métadonnée | Valeur conservée |
|---|---|
| `Manifest.plist.Date` | **17/09/2025 15:54:45.596360 UTC** |
| `Status.plist.Date` | **17/09/2025 16:50:54.990956 UTC** |
| État | `IsEncrypted=true`, `IsFullBackup=false`, `BackupState=new`, `SnapshotState=finished` |
| `Info.plist` | Absent |

Ces valeurs ne certifient pas la date matérielle de création de toute la copie. L’absence d’Info et du journal d’acquisition limite la provenance. L’état `finished` et la présence des objets sont contrôlés séparément ; `IsFullBackup=false` ne démontre pas à lui seul des objets manquants.

Le manifeste contient **177 695 entrées** : **117 865 fichiers `flags=1`**, 59 470 entrées `flags=2` et 360 `flags=4`. Les **117 865 objets attendus sont présents**. Le total déclaré est de **106 595 164 370 octets**, sans équivalence avec un déchiffrement ou contrôle cryptographique complet de la sauvegarde.

### 3.2. Déchiffrement et intégrité

Le déchiffrement utilise `iphone_backup_decrypt 0.11.2` sur SIFT, avec mot de passe saisi sans écho et non enregistré dans les rapports. Les sources sont ouvertes en lecture ; les écritures sont réservées aux dossiers de travail. Le partage source reste accessible en écriture par l’environnement et ne constitue pas un bloqueur matériel.

```text
SHA-256 du manifeste chiffré
 e99a859fe1ed8dcd682eb15b10ec9ab61ac0cbc9d36bd26e734f751ca194c768

SHA-256 du manifeste déchiffré
 334123a803c20b59c9610b459b8769a07d24cab7ea805e35c6f64caec65f365c
```

La collecte générale porte sur **4 632 objets, 1 820 972 351 octets**, sans échec. La sélection prioritaire porte sur **396 objets**, dont 26 PDF candidats ; **62 objets communs** ont des empreintes chiffrées et claires identiques entre les deux méthodes. Leur union représente **4 966 fileID distincts**. Deux artefacts d’usage supplémentaires totalisent **1 813 127 octets**, avec leurs propres contrôles.

Les fichiers de tête présents et objets collectés ont des empreintes source avant/après identiques. **32 contrôles ciblés** revérifient sources et clairs ; les cinq Digest SHA-1 disponibles correspondent aux objets chiffrés. Les écarts chiffré/clair de 1 à 16 octets sont distingués des **525 écarts entre taille MBFile et taille déchiffrée** de la collecte générale. Aucun objet n’est tronqué artificiellement pour rejoindre la taille annoncée ; ces écarts ne démontrent pas une falsification.

### 3.3. SQLite et portée des recherches

Le manifeste déchiffré donne `quick_check=ok`. Sur **1 548 contenus à signature SQLite**, **1 432 contrôles donnent `ok`** et **116 restent incomplets**, notamment faute de collations/tokenizers spécifiques. Ces limitations ne sont pas qualifiées de corruptions. **1 095 bases disposent d’un WAL collecté** ; les copies sont ouvertes avec leurs compagnons disponibles. Les trois sources principales de la séquence du 16 n’ont pas de WAL référencé dans le manifeste contrôlé.

La recherche élargie du 16 parcourt **10 985 tables ordinaires et 47 770 colonnes numériques ou sans affinité explicitement texte/BLOB**, sans filtre sur leurs noms. Les formats opaques, BLOB et tables virtuelles ne sont pas réputés entièrement décodés. Une collecte réussie n’équivaut pas à une interprétation exhaustive de chaque contenu.

## 4. Séquence système du 16 octobre à 05:31

### 4.1. Faits enregistrés

| Heure de Paris le 16 | Source et localisateur | Résultat |
|---|---|---|
| **05:31:33.935058** | Santé, objet **348331**, type 8 | Création d’un objet de distance représentant le **15 à 13:14:16.834842–13:14:49.933610**. |
| **05:31:33.945574** | Santé, objet **348332**, type 7 | Création d’un objet de pas sur le même intervalle du 15. |
| **05:31:35.372222–05:31:35.420874** | PersonalAudio, `ANSCKEVENT` **31013** | Échec de préparation CloudKit, type 0, erreur 134400, zéro objet traité. |
| **05:31:39.196280–05:31:39.252170** | TipKit Messages, transactions **1217–1224** | Huit transactions attribuées à `MobileSMS`, bundle `com.apple.MobileSMS`. |

Trois règles TipKit ont aussi des évaluations dans la dernière fraction de seconde ; elles sont liées aux transactions, pas trois témoins indépendants supplémentaires. L’ensemble se déroule en environ **5,3 secondes**.

Les objets Santé ont un retard d’environ **16 h 16 min 44 s** entre la fin des mesures du 15 et leur création le 16. **Ils ne décrivent aucun déplacement le 16.** La date de création d’un objet n’est pas un horaire de saisie de code, de consultation ou de démarrage.

### 4.2. Messages : gestion récurrente de conseils

Les huit transactions décrivent **quatorze changements** : trois insertions de conseils, trois insertions de règles, trois mises à jour de paramètres et cinq mises à jour de règles. Les paramètres liés sont **`ktWaitingForCloud`**, **`isEligibleForOnboarding`** et **`updateAppleID`**. Aucun changement ne porte sur une ligne de message ou une donation d’événement utilisateur.

Les trois conseils concernés ont **`ZLASTDISPLAYED=NULL`**. Un autre conseil du magasin possède une date d’affichage, mais aucun affichage des trois conseils du 16 n’est attesté. La seule donation conservée liée à l’envoi de message date du 31 mai 2024, pas du 16 octobre.

Le même profil, défini par huit transactions/quatorze changements regroupés par auteur avec écarts de deux secondes au plus, apparaît dans **41 groupes**, dont celui du 16. **Quarante autres occurrences**, notamment trois avant scellement le 15, montrent un mécanisme récurrent. Elles ne sont pas des témoins expérimentaux permettant de le classer exclusivement comme automatique ou humain.

**Ces lignes ne prouvent ni huit SMS lus/envoyés, ni affichage de Messages, ni clic, ni déverrouillage.** Une routine de conseils est étayée ; son déclencheur précis reste inconnu.

### 4.3. PersonalAudio : échec sans transfert attesté

L’événement dure **48,652 ms** et conserve `ZSUCCEEDED=0`, `NSCocoaErrorDomain/134400`, avec **zéro objet affecté ou terminé**. Le type 0 correspond à la préparation CloudKit. Sur 11 018 événements conservés, treize ont le même triplet type/échec/code, dont plusieurs avant scellement ou après octobre.

Cet état ne prouve **ni écoute, ni capture sonore, ni connexion Internet, ni import/export réussi**. Le texte explicatif de l’erreur n’est pas conservé dans la ligne : le code brut ne suffit pas à lui assigner une cause certaine. La table de transactions du magasin est vide dans la copie examinée.

### 4.4. Verrouillage, automatisme et hypothèses concurrentes

Les classes de protection du manifeste sont **2 pour Santé** et **3 pour PersonalAudio/TipKit**, dans l’état sauvegardé. Les mécanismes de protection permettent certains accès lorsque l’écran est verrouillé ; certaines écritures Santé peuvent aussi être différées jusqu’à un déverrouillage. **Aucun de ces mécanismes généraux ne transforme `creation_date` en preuve d’une nouvelle authentification le 16.**

| Scénario | Éléments compatibles | Élément discriminant absent |
|---|---|---|
| Traitements automatiques d’un appareil demeuré allumé | Enregistrement différé Santé, échec interne CloudKit, routine TipKit récurrente | État d’alimentation, veille/réveil et déclencheur contemporains. |
| Interaction humaine déclenchant les mêmes routines | Déverrouillage ou ouverture d’application possibles | Authentification, écran au premier plan ou geste daté. |
| Historique transporté plus tard | Transactions et identités conservables par copie/restauration | Transport postérieur explicatif positivement identifié. |
| Horloge source incorrecte | Absence d’étalonnage indépendant | Correction datée ou référence de temps contemporaine. |
| Extraction de données | Certains outils peuvent provoquer des traitements système | Outil, hôte, session ou transfert rattaché au 16. |

**L’intervention humaine n’est pas établie ; son absence n’est pas démontrée.** Les magasins distincts peuvent partager la même horloge et être copiés ensemble : leur cohérence ne constitue pas plusieurs références matérielles indépendantes.

## 5. Provenance logique et autres dates système

### 5.1. Lignée Santé et Photos

Les objets Santé du 16 sont liés à la provenance **166** : produits origine/local `iPhone14,4`, build `21F90`, version **17.5.1**, `Europe/Paris`, `sync_provenance=0`, `sync_identity=2`, appareil 49. L’identité Santé correspond exactement au `SyncIdentityHardwareIdentifier` de `healthd` dans la sauvegarde.

Cela rattache les objets à une identité logique de l’installation sauvegardée, **sans lien infalsifiable à la série matérielle en octobre**. Le `localIdentifier` est vide ; une source héritée conserve `iPhone9,3` et une autre identité. Le seul drapeau `local_device=1` n’est donc pas une preuve matérielle exclusive.

Photos conserve **18 migrations**, dont deux portent l’UDID TP-03 exact : **27/04/2024 à 05:03:56**, build `21E236`, et **03/06/2024 à 06:30:21**, build `21F90`, avec modèle `D16AP` et même lignée de bibliothèque. Cette continuité logique antérieure n’établit pas une présence physique ininterrompue jusqu’à la sauvegarde.

MobileBackup conserve une restauration du **29 octobre 2021** et Setup Assistant une sortie du **11 juin 2024**. Ces états ne démontrent pas un transport après octobre ; ils ne l’excluent pas. Une restauration antérieure ne peut pas, à elle seule, expliquer des traces encore futures.

### 5.2. Dates pendant la conservation et éléments non exécutifs

| Date et heure de Paris | Constat | Portée |
|---|---|---|
| **15/10 à 13:30–13:50** | Créations Santé, modèle clavier, autorisation TCC, PeopleSuggester et préférences CoreDuet | Avant le repère de scellement ; ni texte saisi ni suppression utilisateur établie. |
| **15/10 18:33:26.915492 et 18:36:27.578715** | `routined`, registration/désinscription GNSS | États système datés ; pas de coordonnées, trajet ou activation GPS par une personne. |
| **16/10 01:40:51.941617** | `mediaremote/MRDPQPDS.PED` | Date native, sens exact non validé ; pas une lecture musicale démontrée. |
| **16/10 13:13:33 et 21/10 05:34:00** | Préférences `NextFreshmint…` et `NextHeartbeat…` | Échéances programmées, pas exécutions constatées. |
| **18 et 26/10 à 22:00:14** | Configuration de clés Facebook | Métadonnées, sans activité locale validée. |
| **28/10, intervalles d’énergie entre 09:09 et 18:24** | Créations des six objets le **29** | Ni écriture ni allumage avant ouverture démontrés par leurs seuls débuts. |

Les treize lignes centrales Apple `PegasusConfiguration/AlpsWarehouse` ont des **payloads de zéro octet**. Elles ne prouvent pas un fonctionnement quotidien ; le nom de ce composant ne caractérise pas le logiciel espion Pegasus. Les dates de calendrier ou de contenu Santé ne sont pas assimilées à des utilisations locales.

### 5.3. Contre-épreuves d’usage, démarrage et réseau

La recherche élargie dans les 1 548 bases et **2 493 plists** ne fournit aucun nouveau témoin validé d’interaction du 16. Trois exceptions plist sont examinées séparément : un fichier vide, une date année 0000 et des sentinelles hors plage dans `sleepd`, sans fabrication de dates de remplacement.

Les préférences de biométrie, écran, planification et horloge ne datent pas un démarrage ou déverrouillage du 16. Les **157 alarmes** ne démontrent pas un déclenchement à 05:30 ; l’entrée à cette heure est désactivée dans l’état conservé et porte une date ancienne. Cet état n’exclut pas toute alarme historique.

Les sources d’interaction et DataUsage s’arrêtent en juin ; les tables Wi-Fi/événements et visites Safari contrôlées sont vides. Elles ne constituent donc pas des contre-épreuves fiables d’inactivité en octobre.

L’artefact ATX supplémentaire fournit **45 entrées délimitées : une base SQLite valide et 44 plists**. Ses derniers états, sa seule ligne de séquence de lancement et ses ancrages anciens ne donnent pas d’événement du 16. `RecentAppLayouts` se décompresse et son cadrage Protobuf est parcouru, mais ses champs privés n’offrent pas de chronologie de premier plan validée. Un état récent ne remplace pas un historique complet.

## 6. Communications, photos, réseaux et caméras

### 6.1. Communications et photothèque

L’historique natif contient **305 appels du 8 avril au 24 juin 2024**. `sms.db` contient **73 457 messages**, dernier `date` au **24 juin à 15:12:28.867429**. Aucun appel ou champ natif de message, lecture ou livraison sélectionné n’appartient à la fenêtre centrale ou au contrôle avant ouverture.

**Cette couverture arrêtée avant octobre ne permet pas d’exclure tout usage ou de trancher l’insertion SIM du 28.** Aucun code Apple d’octobre n’est identifié dans ces lignes, sans récupération exhaustive des messages supprimés.

Photos contient **21 814 actifs**. Les six champs contrôlés de création, ajout, modification, ajustement, corbeille et partage, ainsi que les transactions, ne fournissent pas de date centrale. Cela ne prouve pas l’absence historique de photos, captures ou suppressions exclues de la sauvegarde.

### 6.2. Wi-Fi et Freebox

Les préférences contiennent **onze réseaux connus**, **onze entrées privées** et une copie historique de **69 réseaux** ; `wifi-networks.plist` courant est vide. Aucun **`ASUS_Z01RD`**, aucune date centrale exploitable ou `JoinedByUserAt` central n’est sélectionné. Ces états ne sont pas un journal exhaustif d’associations.

La MAC privée **`C6:A2:88:AC:F8:CB`** correspond à une fiche Freebox de **septembre 2025**, pas d’octobre 2024. Les trois identités iPhone nocturnes des 16–17 octobre restent non attribuées. Rotation de MAC et perte d’états empêchent une exclusion matérielle certaine ; aucun identifiant client exploitable n’est disponible pour TP-01 dans les pièces contrôlées.

### 6.3. Caméras, diagnostics et outils

LSC Smart Connect et Xiaomi Home figurent au manifeste. Leurs états non multimédias ne reconstituent pas un historique exhaustif d’accès, visionnage ou partage. Les jours WebKit conservés s’arrêtent aux **10 et 11 juin 2024 UTC**, les 96 dates du cache LSC au **12 juin à 03:24 Paris**, sans valeur centrale.

Les **92 diagnostics `.ips`** sont nommés d’avril à juin, sans diagnostic d’octobre dans cet ensemble. Les chemins `knowledgeC.db`, CurrentPowerLog et netusage recherchés sont absents ; `interactionC.db` est présent mais de couverture ancienne. Aucun uptime d’octobre ne date un démarrage.

Les recherches d’outils et de pair records ne fournissent pas de session d’extraction ou de télécommande d’octobre identifiée. `LockdownMode` et `LockdownParameters` ne sont pas des appairages USB. Une recherche par noms ne couvre pas tous les outils renommés ou les traces omises par une sauvegarde logique. Aucun accès à un compte ou caméra en fonctionnement n’est impliqué par ces analyses.

## 7. Rapprochements avec OP-01 et TP-02

### 7.1. Relation de confiance ancienne avec OP-01

OP-01 conserve **`ProgramData/Apple/Lockdown/00008110-001249321444801E.plist`**, portant exactement l’UDID TP-03. Son SHA-256 est :

```text
a6eb37fd5aac553440132a381550e4ee9fe960b7b6820fe37576eb32d1bfa930
```

L’entrée MFT **113002** porte une création SI le **04/07/2022 à 13:19:51 Paris**, une création FN/modification le **14/12/2023 à 16:43:30 Paris** ; ces dates ne sont pas fusionnées en un premier appairage certain. Le `SystemBUID` concorde avec la configuration Apple du PC.

**Une relation de confiance conservée est étayée, sans connexion le 15 ou le 28 octobre 2024, extraction ou opérateur datés.** Ce fichier ne départage pas les numéros de scellés.

### 7.2. PDF communs aux deux Mini

Les **26 PDF candidats de TP-03** fournissent un équivalent SHA-256 exact aux **27 entrées PDF de `L16B/IPHONE13_MINI`**, représentant **vingt contenus distincts**. Le même résultat existe dans TP-02.

**Ces documents ne permettent de choisir ni le Mini physiquement extrait, ni le scellé correspondant, ni le sens ou la date du transfert.** Ils ne certifient pas leur présence dans le jeu définitivement saisi, distinct du dossier informatif L16B laissé sur le PC. Les dates NTFS SI du 15/FN du 28 ne deviennent pas des dates d’extraction certifiées de TP-03.

La séquence TipKit du 16 n’est pas retrouvée à l’identique dans les transactions Messages de TP-02 comparées ; son événement PersonalAudio est différent. Ce contrôle écarte une duplication exacte dans ce périmètre, sans rendre les historiques TP-03 intransportables.

## 8. Limites et conclusion technique

La sauvegarde porte des dates de 2025, manque d’Info et de journal d’acquisition, et conserve un historique de restauration partiel. Les identités logiques et dates peuvent être transportées. Aucun journal continu de démarrage, authentification ou radio, aucune image physique ou référence historique d’heure indépendante ne résout cette provenance.

**Observation de visionnage rapportée :** le prestataire indique voir une agente rallumer les téléphones le **15 octobre vers 13:25**, avant scellement ; la cliente situait ce geste vers 13:30 ou un peu avant. Le [rapport final](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés) distingue ce récit des seuls aperçus d’un clip débutant à 13:28. L’état à la fermeture et la continuité d’alimentation ne sont pas établis. Si une extinction à la fermeture était prouvée indépendamment, un fonctionnement local ultérieur supposerait une reprise à expliquer ou une autre origine des dates.

**Les préférences du 15 au soir et du 16, puis la séquence Santé/PersonalAudio/Messages à 05:31, constituent des indices positifs de traitements système datés pendant la conservation. L’examen détaillé identifie un échec CloudKit et une routine TipKit récurrente, sans marqueur validé d’action humaine.**

L’utilisation physique de TP-03 aux heures civiles indiquées reste non certifiée. Ni déverrouillage, ni extraction, ni auteur ou rupture de scellé ne sont démontrés ; l’absence de manipulation ou le maintien éteint ne le sont pas davantage. L’appairage ancien et les PDF communs sont des rapprochements de contenu et d’identité, pas des preuves de connexion en octobre.

Les pièces discriminantes seraient un rapprochement séries/scellés, les documents de conservation et d’alimentation, une acquisition plus proche de 2024, l’historique de restauration et des journaux contemporains à référence de temps indépendante. Leur disponibilité n’est pas présumée.

## 9. Pièces techniques et termes de lecture

| Domaine | Pièces de contrôle |
|---|---|
| Inventaire, déchiffrement et empreintes | [Synthèse](recherche-TP-03/summary.json), [collecte](recherche-TP-03/collection.json), [contrôles natifs](recherche-TP-03/final-checks/native-integrity.json) |
| SQLite et tri temporel | [Statistiques](recherche-TP-03/scan/timestamp-stats.json), [erreurs et limites](recherche-TP-03/scan/errors.json) |
| Séquence et provenance | [Santé](recherche-TP-03/priorite/findings/health.json), [préférences](recherche-TP-03/plists/dates.json), [corrélations](recherche-TP-03/correlations/results.json) |
| Examen approfondi du 16 | [Conseils, CloudKit, protection et contrôles élargis](../investigations/20261110-tp03-intervention-humaine/compte-rendu.md) |
| Caméras et PDF | [Métadonnées WebKit/caméras](recherche-TP-03/final-checks/camera-webkit.json), [identités PDF](recherche-TP-03/priorite/pdf-identities.json) |
| Comparaisons entre appareils | [Rapprochements transversaux](../investigations/20261110-telephones/compte-rendu.md), [contrôle avant ouverture](../investigations/20261110-revue-intervention-scelles/compte-rendu.md) |
| Reproduction | [Notice et scripts](scripts/README-TP-01-TP-03.md) |

Les pièces conservent requêtes, localisateurs, champs bruts, erreurs et empreintes. Les contenus clairs restent sur SIFT à accès restreint ; les résultats privés sous `recherche-TP-03/` sont exclus de Git. Les synthèses n’exportent ni mots de passe, ni mesures médicales, ni conversations.

| Terme | Sens dans ce rapport |
|---|---|
| Sauvegarde logique / manifeste | Fichiers retenus par iOS / index de leurs chemins et métadonnées ; pas une image de tous les secteurs. |
| UDID / identité Santé / UUID de bibliothèque | Identifiants d’appareil déclaré, d’installation Santé et de lignée de données ; leurs portées ne sont pas interchangeables. |
| Date de mesure / création d’objet | Intervalle représenté / enregistrement de son objet en base. Leur décalage ne date pas automatiquement un geste humain. |
| TipKit / CloudKit | Conseils applicatifs / mécanismes de données cloud. Une règle évaluée ou une tentative interne ne prouve ni affichage ni transfert réussi. |
| SQLite / WAL / `quick_check` | Base / journal de transactions / contrôle de cohérence. Un contrôle incomplet faute d’extension ne démontre pas une corruption. |
| Pair record | Fichier Apple conservant une relation de confiance ; ses métadonnées ne sont pas un journal de chaque branchement. |
