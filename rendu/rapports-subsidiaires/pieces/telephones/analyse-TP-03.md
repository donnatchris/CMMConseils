# Rapport d’analyse technique du téléphone TP-03

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev

**Équipement :** iPhone 13 mini — série `Y4Q9KGHG26`

**Mise à jour :** 17 novembre 2026 — réponse à Q3 sur le premier déverrouillage, iCloud et les doublons.

## 1. Objet et synthèse

J’ai examiné les indices d’activité conservés dans la sauvegarde de TP-03 pendant la rétention du **15 au 28 octobre 2024**, leur provenance, les communications et les rapprochements avec les autres supports. Il distingue les traitements système, les contenus datés, leur attribution au matériel et les éventuels gestes humains.

### 1.1. Résultats essentiels, en langage courant

**Premier constat — les documents PDF du 15 octobre.** Parmi les **20 contenus PDF distincts** représentés par les **27 fichiers** de l’inventaire transmis, **17** possèdent dans la sauvegarde TP-03 une métadonnée de dernière utilisation datée du **15 octobre 2024 entre 13 h 41 et 13 h 50**. Pour **16** de ces contenus, une autre métadonnée, relative au changement de statut du fichier, appartient à la même période. Les dates de dernière utilisation se situent à quelques secondes des dates de création consignées dans l’inventaire. Cette concordance est un **indice technique important en faveur de la historique de données conservée dans TP-03**. Elle ne prouve pas que les documents ont été créés, lus ou transférés depuis le téléphone physique à ces heures, ni qu’un enquêteur les a consultés.

**Deuxième constat — des traces de Mail et de Fichiers précèdent cette séquence.** Le 15 octobre, entre **13 h 25 et 13 h 51**, la sauvegarde conserve notamment des transactions des composants Mail et Fichiers. Elles attestent des enregistrements logiciels datés, mais ne désignent aucun des 17 PDF, ne prouvent aucune ouverture de document et n’identifient aucun utilisateur.

**Troisième constat — des traitements logiciels datés du 16 octobre.** Entre **05 h 31 min 33 s et 05 h 31 min 39 s**, heure de Paris, deux créations d’objets Santé, un échec interne CloudKit et huit transactions de gestion de conseils dans Messages sont enregistrés. Leur réunion est compatible avec des traitements automatiques. Elle ne démontre ni intervention humaine ni fonctionnement matériel du téléphone à une heure civile indépendamment vérifiée.

**Quatrième constat — le dossier PDF sur l’ordinateur.** Les **27 PDF** ont des dates de création Windows reprises dans l’inventaire et situées le **15 octobre**, mais leurs métadonnées de création de nom de fichier dans le dossier final d’**OP-01** sont regroupées le **28 octobre à 17 h 13**. Une date conservée lors d’une copie n’est pas nécessairement la date de transfert. Le mécanisme et les étapes intermédiaires restent inconnus.

**Conclusion d’ensemble.** Ces éléments justifient d’examiner la provenance des données et les opérations réalisées sur les appareils, **sans permettre à ce stade d’affirmer un déverrouillage après redémarrage, une extraction directe le 15 octobre, une consultation des PDF par un enquêteur ou une rupture de scellé**. Ils ne permettent pas non plus de certifier l’absence de manipulation.

### 1.2. Deux séquences à ne pas confondre

| Séquence | Ce qui est conservé | Ce que cela ne démontre pas |
|---|---|---|
| **15 octobre, 13 h 25–13 h 50** | Traces Mail et Fichiers ; 17 attributs de dernière utilisation de PDF rapprochés des dates de l’inventaire | Lecture, copie, impression ou transfert des PDF depuis le téléphone physique ; identité de l’opérateur |
| **16 octobre, vers 05 h 31** | Enregistrements Santé, tentative CloudKit en échec, gestion de conseils Messages | Action humaine, SMS lus ou envoyés, déverrouillage ou transfert de données |

### 1.3. Tableau récapitulatif des constatations

| Résultat | Conclusion permise |
|---|---|
| **15 octobre à 18:33–18:36**, préférences GNSS ; **16 à 01:40**, préférence `mediaremote` | États système datés après le repère de scellement, sans position, trajet ou lecture multimédia démontrés. |
| **16 octobre à 05:31**, Santé/PersonalAudio/TipKit | Séquence cohérente, compatible avec des traitements automatiques ; leur déclencheur reste inconnu. |
| Huit transactions Messages, quatorze changements | Gestion de conseils/règles, profil retrouvé dans **40 autres séquences** ; ni huit SMS ni affichage des conseils démontrés. |
| Communications natives arrêtées en juin 2024 | Aucun événement d’octobre sélectionné, mais couverture insuffisante pour exclure l’usage du téléphone. |
| **27 PDF Mini de L16B**, vingt contenus distincts, identiques dans les deux Mini | Contenu commun non discriminant entre TP-02 et TP-03 ou entre les scellés n° 3/n° 4. |
| CSV fourni : 27 chemins et SHA-512 concordants ; 17 attributs `lastused` dans TP-03 le 15 | Présence de ces contenus dans l’inventaire fourni et indice temporel en faveur de TP-03 ; contenu de l’archive finale non vérifié. |
| 15 octobre, 13:25–13:51 : 33 transactions Mail, cinq Fichiers et classes de protection | Activité logicielle conservée ; accès après première authentification compatible sous conditions, sans déverrouillage daté, partage, enregistrement ou impression PDF démontrés. |
| 27 créations NTFS FN le 28 octobre en environ 658 ms | Arrivée groupée au dossier final d’OP-01 étayée ; outil et étape intermédiaire inconnus. |
| Recherche des fichiers supprimés dans OP-01, dont 357 Go d’espace libre | Archive finale et fichier de rejets non récupérés ; références descriptives présentes, contenu du support E: à rechercher. |
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
| **15 octobre vers 13:24** | Remise des trois téléphones aux enquêteurs, selon la note de constatation fondée sur les vidéos fournies. L’horodatage vidéo n’est pas étalonné indépendamment. |
| **15 octobre à 13:25:19** | Apparition des logos Apple sur les trois appareils, consignée dans la note de visionnage ; séquence caractéristique d’un démarrage, sans preuve de déverrouillage ultérieur. |
| **15 octobre vers 13:30** | Repère initial de perte d’accès déclaré ; il ne constitue ni une heure certifiée de fermeture des scellés ni une correction des horodatages vidéo. |
| **15 octobre après 14:19** | Mise sous scellés consignée, sans fermeture individuelle précisément horodatée. |
| **28 octobre à 11:30** | Ouverture des téléphones et déverrouillage par la cliente. |
| **28 octobre à 11:45** | Insertion SIM dans le scellé n° 3, sans attribution TP-02/TP-03 certaine. |
| **28 octobre à 19:20** | Clôture ; restitution consignée sans heure individuelle, récupération approximative déclarée vers 19:20. |

La **fenêtre centrale de recherche**, définie initialement pour les traitements techniques, va du **15 à 13:30 au 28 à 19:20** ; elle comprend donc des opérations après ouverture. Le contrôle spécifique avant ouverture utilise **15 octobre 14:19 inclus → 28 octobre 11:30 exclu**, sans présumer une fermeture effective de tous les appareils à 14:19. La comparaison couvre le **1er octobre au 15 novembre inclus**.

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

Le complément du **14 novembre 2026** ajoute une collecte ciblée de **neuf objets natifs, 82 289 octets**, notamment pour examiner les marqueurs FirstUnlock et préférences applicatives. Les empreintes chiffrées avant/après et les empreintes claires sont conservées ; aucun secret n’est publié. Cette opération complémentaire est documentée séparément des périmètres de collecte précédents, dans le [rapport B à E](../inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md#sources-et-méthode).

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

Les huit transactions décrivent **quatorze changements** : trois insertions de conseils, trois insertions de règles, trois mises à jour de paramètres et cinq mises à jour de règles. Les paramètres liés sont **`ktWaitingForCloud`**, **`isEligibleForOnboarding`** et **`updateAppleID`**. Aucun changement ne porte sur une ligne de message ni sur un événement conservé signalant une action de l’utilisateur.

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

Les **26 exemplaires de TP-03** et **46 de TP-02**, soit **72 objets**, couvrent les vingt contenus distincts des **27 PDF de `C:\L16B\TELEPHONES\IPHONE13_MINI`**. Les SHA-512 calculés correspondent exactement aux 27 lignes du [CSV fourni](../inventaire-DNEF/documents-recus/Inventaire_saddedine.csv), dont le SHA-256 est `f2a4e9d05cca5c7b8082da42df76fca45e870f3e3acbbdf6ff03c07e68293c40`.

**La réserve ancienne tenant à l’absence d’inventaire est donc levée pour ces 27 entrées : leurs chemins et contenus figurent bien dans le CSV transmis.** Cela n’authentifie pas indépendamment le CD d’origine et ne remplace pas l’examen de l’archive finale. L’identité des contenus reste commune aux deux Mini ; les attributs temporels apportent, en revanche, un élément plus discriminant en faveur de TP-03.

#### 7.2.1. Création ancienne, emplacements et applications d’origine

**Aucun `Birth` des 72 objets ne tombe le 15 octobre 2024 entre 13:41 et 13:50.** Les exemplaires locaux de TP-03 portent essentiellement des créations de 2019 à 2023. La date « création » du CSV n’est donc pas la date de création `Birth` des copies iPhone sauvegardées, ni une preuve de génération du contenu ce jour-là.

Les vingt contenus ont tous une copie dans `AppDomainGroup-group.com.apple.FileProvider.LocalStorage`, sous `File Provider Storage/` : stockage local de Fichiers, interprété comme **« Sur mon iPhone »**. Dans TP-03, la plupart sont sous `Téléchargements/`, la facture RCT NOVEMBRE à la racine, le document Qonto/London sous `Téléchargements/London/Qonto/` et FA0046 à la racine et dans Téléchargements. Certains contenus ont aussi des copies WhatsApp ; Fattura-37 a une copie dans le conteneur WeChat. Aucun des 72 objets correspondants examinés n’est dans un domaine iCloud Drive ou un magasin de pièces jointes Mail. Cela n’exclut pas des exemplaires anciens, supprimés ou omis par la sauvegarde.

Sept contenus déclarent `Creator=Mail`, avec un producteur Quartz iOS et des dates internes anciennes. Les autres déclarent notamment Safari, Word, Excel, WPS, Chrome/Skia, wkhtmltopdf, Microsoft Print To PDF ou FPDF. **Ces champs décrivent une origine logicielle déclarée dans le PDF ; ils ne prouvent pas l’application utilisée pour son traitement ou son transfert le 15 octobre.** Pour RCT NOVEMBRE, l’attribut `com.whatsapp.original` renvoie au média WhatsApp identique retrouvé, sans dater ni orienter un export. Le [tableau Q1 des vingt contenus](../inventaire-DNEF/rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md#dates-de-création-et-origine-déclarée-des-pdf) donne chaque date et logiciel ; l’[annexe des 72 objets](../inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/annexe-objets.md) conserve les chemins et champs exacts.

#### 7.2.2. Les 17 rapprochements temporels propres à TP-03

Dans TP-03, **17 objets représentant 17 contenus** portent `com.apple.lastuseddate#PS` dans la séquence du **15 octobre, 13:41–13:50**. Pour **16**, `LastStatusChange` se situe aussi dans cette fenêtre. Aucun attribut de dernière utilisation des exemplaires TP-02 contrôlés n’y tombe. Les attributs actuels des trois autres contenus de TP-03 sont ultérieurs : cela n’exclut pas un traitement ancien.

Les 16 octets de `lastused` sont interprétés comme deux entiers signés little endian de 64 bits, secondes Unix puis nanosecondes. Les octets bruts sont conservés ; ce décodage cohérent ne transforme pas l’attribut en journal certifié de consultation humaine. La comparaison utilise toujours la première date CSV du contenu, sans choisir un doublon plus favorable.

**Exemple : `Rép  Dossier bourarach.pdf`.** Sa copie Fichiers TP-03 porte `Birth=17/12/2019 19:20:21`, `lastused=15/10/2024 13:42:55,987134933`, puis `LastStatusChange=13:42:56`. Le CSV indique une création à **13:42:57,930**, soit environ **1,943 seconde** d’écart. Les deux copies identiques TP-02 ont des attributs actuels datés du 28 octobre au soir. Ce PDF reproduisant des échanges avec Me Isabelle Guillou est donc **explicitement retrouvé dans l’inventaire fourni**, avec le contenu attendu ; sa lecture ou son utilisation par un agent n’est pas démontrée.

**Conclusion Q1 :** TP-03 est la piste la mieux étayée pour la lignée d’installation ayant conservé cette séquence documentaire. Ni la création des PDF le 15, ni un transfert direct depuis ce téléphone, ni un auteur ou le numéro de scellé ne sont établis. Une copie, restauration ou propagation des attributs reste possible.

### 7.3. Premier déverrouillage après redémarrage : investigation B

**Explication préalable.** Sur un iPhone protégé par un code, certains fichiers ne deviennent accessibles qu’après la première saisie du code suivant un redémarrage. Ils peuvent ensuite rester accessibles à des traitements logiciels lorsque l’écran est reverrouillé, jusqu’au redémarrage suivant. Cette propriété technique est importante ici, mais **la présence de dates dans une sauvegarde réalisée ultérieurement ne prouve pas, à elle seule, que les fichiers ont été lus ou modifiés localement sur l’appareil physique en octobre 2024**.

Les **26 exemplaires PDF TP-03**, les bases TipKit de **Mail et de Fichiers** et le modèle clavier sont de **classe C (`ProtectionClass=3`)** dans l’état sauvegardé. La classe C est une catégorie de protection iOS : **sur un appareil protégé par un code, le contenu de ces fichiers reste inaccessible jusqu’au premier déverrouillage après un redémarrage**. Après cette première authentification, il peut rester accessible aux traitements logiciels même si l’écran est de nouveau verrouillé, jusqu’à l’arrêt ou au redémarrage suivant. Un état **AFU** (*After First Unlock*, après le premier déverrouillage) ne signifie donc pas que l’écran est actuellement déverrouillé ; **BFU** (*Before First Unlock*) désigne l’état précédant cette première authentification. [Documentation Apple](https://developer.apple.com/documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication).

Les fichiers TCC, PeopleSuggester, les préférences coreduetd et FrontBoard contrôlés sont de **classe D (`ProtectionClass=4`)** ; leur seule présence ne démontre pas la levée de la protection de classe C.

**Si des lectures ou écritures nouvelles des contenus de classe C ont réellement eu lieu localement après le démarrage constaté dans la vidéo, avec cette protection déjà applicable, un état BFU strict serait incompatible avec ces opérations ordinaires.** Mail conserve une première transaction à **13:25:30,661993**, Fichiers à **13:29:50,324222**, et le modèle clavier une mise à jour à **13:35:42,098506**. Sous ces conditions seulement — notamment si les écritures ont réellement été effectuées localement à ces dates, après le redémarrage, et si les classes de protection étaient alors applicables — elles appuieraient un accès après première authentification, au plus tard à leur heure respective.

Mais la sauvegarde tardive ne certifie ni le premier déverrouillage, ni la continuité des classes depuis 2024, ni l’exécution locale historique de chaque écriture. Elle ne prouve pas davantage que la modification de `lastused` ou du statut des PDF nécessitait de lire leur contenu. Les historiques peuvent avoir été transportés ou restaurés. **La contradiction technique avec le récit de la cliente n’est donc pas démontrée, et aucun opérateur n’est identifié.**

Les recherches dans les deux manifestes ne fournissent pas de journal exploitable de démarrage/keybag, de `knowledgeC.db`, de Powerlog, de traces unifiées ou de Biome sous les motifs contrôlés. Les 92 diagnostics IPS, SpringBoard/backboardd et FrontBoard ne datent pas le redémarrage ou l’authentification litigieux. Les deux `.FirstUnlock` déchiffrés sont des marqueurs applicatifs Raccourcis datés des **24 mai 2024** et **17 septembre 2025**, pas des événements du 15 octobre. Les préférences Fichiers et Quick Look ne datent aucun accès aux PDF. Les sources Apple et la portée exacte des classes sont citées dans le [complément B](../inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md#b-le-téléphone-était-il-déverrouillé).

**Réponse à Q3 — premier déverrouillage et iCloud.** Dans l’état sauvegardé, le contenu des PDF de classe C est normalement inaccessible avant la première authentification après redémarrage. Une synchronisation iCloud ne suffit pas, à elle seule, à expliquer un nouvel accès local à ce contenu dans un état strictement antérieur au premier déverrouillage. Mais les dates de métadonnées ne démontrent ni un accès au contenu ni une création de PDF. L’état historique de protection, le lieu de production des traces et leur éventuel transport ne sont pas établis. **Les données ne permettent donc pas de déterminer si TP-03 a été déverrouillé ou a produit localement les fichiers aux heures litigieuses.** L’origine des noms suffixés est examinée en section 7.6.

### 7.4. Mail, Fichiers et traces indépendantes : investigation D

Toutes les heures ci-dessous concernent le **15 octobre 2024, heure de Paris**.

| Source | Constat précis | Portée et limite |
|---|---|---|
| TCC | Mail **13:25:26**, Fichiers **13:29:50**, Musique **13:40:52** ; service `kTCCServiceUbiquity`, `auth_value=2`, `auth_reason=4` | Entrées d’accès au service cloud ; aucun PDF, chemin ou destinataire identifié. Aucun clic d’autorisation démontré ; `boot_uuid=UNUSED`. |
| TipKit de Mail | **33 transactions, 8164–8196**, de **13:25:30,661993 à 13:29:09,106157** ; 35 mises à jour de règles et 13 de paramètres | Activité logicielle attribuée à Mail ; pas de message envoyé, PDF produit ou application au premier plan démontrés. Les deux conseils ont `ZLASTDISPLAYED=NULL`. Aucune transaction sélectionnée à 13:41–13:50. |
| TipKit de Fichiers | **Cinq transactions, 254–258**, de **13:29:50,324222 à 13:29:50,341425**, attribuées au processus `Files` / `com.apple.DocumentsApp` ; sept changements de règles | Activité logicielle attribuée à Fichiers ; aucun document, ouverture, enregistrement ou partage identifié. Les tables actuelles de donations et d’événements sont vides ; l’unique conseil a `ZLASTDISPLAYED=NULL`. |
| PeopleSuggester | `DeviceIdDate=13:41:02,145052`, métadonnées de fichier à 13:41:06 | Date d’identifiant ; ni ouverture du menu de partage, ni document ou destinataire. |
| coreduetd | Deux dates vers **13:50:40,668** | Maintenance/throttling et notification de tombstonage du flux `/app/activity` ; ni application au premier plan, ni suppression humaine de PDF démontrées. |
| Modèle clavier | **13:35:42,098506**, compteur cumulé `tium.totalWordsTypedInSecondaryLanguage` | Aucun texte ni état antérieur ; ne date pas une saisie de code et n’identifie pas un PDF. |

Les **8 interactions et 8 647 pièces jointes** de CoreDuet TP-03 ne rattachent pas nominalement les PDF aux événements contrôlés. Les états FrontBoard décodés de Mail et Fichiers ne donnent pas de date d’octobre exploitable ; certaines valeurs brutes sont communes aux deux Mini, sans unité temporelle ou session de démarrage validée.

**Contrôle ciblé du 16 novembre 2026, fenêtre 13:25–13:51.** Les cinq transactions Fichiers ci-dessus complètent la synthèse antérieure. Les lignes `ACHANGE` 403–409 concernent exclusivement `CoreRuleRecord` ; le texte actuel du conseil relatif au partage familial ne prouve ni son affichage ni un partage. La base TipKit Fichiers est elle aussi de classe C. Les requêtes sur SIFT, en lecture seule sans rejeu WAL, confirment les 33 transactions Mail et les 17 attributs de dernière utilisation des PDF ; les 20 fichiers suivis ont des SHA-256 avant/après identiques, et le complément Fichiers confirme également l’intégrité de sa base et du manifeste. La [note de vérification](../inventaire-DNEF/rapports/Note_reponse_TP02_TP03_15oct2024.md) conserve les requêtes, résultats et empreintes.

TP-02 ne conserve aucune ligne TCC correspondante ni transaction Mail dans la fenêtre **13:20–14:05** précédemment examinée ; le nouveau contrôle ne retrouve aucune transaction TipKit Mail ou Fichiers sur **13:25–13:51**, ni attribut de dernière utilisation des PDF contrôlés dans ce créneau. Cette différence précise les états sauvegardés ; elle ne prouve pas l’absence passée de toute activité TP-02. **Des traces propres à Mail et Fichiers existent avant la séquence des PDF, mais aucun événement indépendant ne les relie directement aux 17 contenus.** Aucun événement explicite du créneau ne démontre un premier déverrouillage après redémarrage, un déverrouillage d’écran, une ouverture du menu de partage, un enregistrement ou une impression PDF. Les métadonnées documentaires ne suffisent pas à établir ces gestes. Les horloges de la vidéo et des téléphones n’ont pas été étalonnées indépendamment ; leur proximité temporelle ne relie pas formellement les transactions au démarrage visible.

### 7.5. Arrivée sur OP-01 et mécanisme inconnu : investigation C

**Point de lecture essentiel.** Les dates de création inscrites dans l’inventaire sont celles d’un champ de métadonnées Windows (`$STANDARD_INFORMATION`), tandis que les dates de création du nom de fichier (`$FILE_NAME`) situent l’arrivée groupée des PDF dans **leur dossier final** le 28 octobre. Ces deux séries de dates ne décrivent pas nécessairement le même événement : une opération de copie peut préserver des dates antérieures. Il serait donc incorrect de présenter les dates du 15 octobre comme la preuve d’un transfert vers OP-01 ce jour-là.

Les parentés NTFS sont résolues. Les créations `$FILE_NAME` du **28 octobre 2024, heure de Paris**, donnent :

| Élément | Création FN |
|---|---|
| `C:\L16B` | **10:47:10,6339294** |
| `C:\L16B\TELEPHONES` | **17:00:37,5120727** |
| `C:\L16B\TELEPHONES\IPHONE13_MINI` | **17:12:06,6590911** |
| 27 PDF | **17:13:43,2355080 à 17:13:43,8934745** |

L’arrivée des 27 fichiers en **0,6579665 seconde** étaye une mise en place groupée au dossier final le 28, après ouverture. Les **27 dates « création » du CSV sont exactement égales aux créations `$STANDARD_INFORMATION` NTFS** du PC, datées du 15. Cela identifie le champ inventorié, sans déterminer son producteur initial. Une copie, extraction ou restauration peut conserver ou rétablir des dates ; aucune de ces opérations ni l’API effectivement utilisée n’est identifiée ici. Aucun flux nommé, notamment `Zone.Identifier`, ne fournit de provenance.

La recherche de copies de mêmes tailles a permis de lire et hacher **45 fichiers accessibles**. Au moins **six des vingt contenus** ont aussi des équivalents ailleurs sur OP-01 : RCT OCTOBRE, RCT NOVEMBRE et Avis ECH 0423 dans le cache Courrier Windows ; KEDY dans Downloads et L16B/LOCAL ; FA0037 et facture rct 0801 dans les deux exports SHINE. Les dates anciennes de ces exemplaires ne garantissent pas une présence physique continue, et leur existence ne prouve pas qu’ils ont servi de source au dossier Mini. Aucun des 18 candidats ZIP contemporains contrôlés ne reconstitue les 27 PDF ; 17 sont ouvrables, le dernier étant un fichier `$I` de métadonnées de corbeille.

Les **887 Prefetch**, UserAssist, SetupAPI, événements et traces d’outils ne rattachent aucun logiciel de transfert à ces PDF. iTunes est présent, mais les dates d’exécution retenues sont de 2022 ou 2026. Le pair record et SetupAPI confirment une relation ancienne avec TP-03, pas un branchement le 15 ou le 28. Les suppressions d’instances Apple de mars 2024 ne prouvent pas une suppression de données du téléphone. Aucun outil Apple Devices, iMazing, 3uTools ou forensic précis n’est identifié comme producteur de L16B.

UserAssist conserve l’exécution de **`D:\LdSD-1.0.4\bin\Win64\LdSD.bat` à 17:15:40,172**, après les créations FN des PDF. Le script/binaire et l’éditeur manquent ; cette dernière exécution ne définit ni sa fonction, ni toutes ses exécutions, ni son rôle dans le transfert. Les trois Kingston sont reconnus à **16:27:54, 17:00:07 et 17:14:51** ; les références à `E:\saddedine\` apparaissent ensuite. Les journaux `$UsnJrnl` et `$LogFile` exploitables couvrent 2026, pas les transactions de copie d’octobre 2024.

**Chaîne étayée :** contenus dans les deux sauvegardes et parfois ailleurs sur le PC → origine des dates du 15 inconnue → étape intermédiaire non identifiée → dossier Mini créé le 28 à 17:12:06 → arrivée groupée à 17:13:43 → références à l’archive/inventaire/rejets sur le support E:. Ni un transfert iPhone vers PC le 15, ni le canal ou l’outil intermédiaire ne sont démontrés.

### 7.6. Doublons, horloges et 72 objets : investigation E

Les sept exemplaires supplémentaires des 27 PDF correspondent à quatre groupes de même SHA-512 :

| Groupe | Exemplaires dans le CSV | Écarts successifs des créations SI |
|---|---|---|
| Qonto | 2 | **31,78 s** |
| facture rct 0801 | 3 | **8,98 s ; 9,40 s** |
| Avis ECH 0423 SAS RCT | 4 | **8,39 s ; 8,20 s ; 8,06 s** |
| KEDY FACTURE 202210 | 2 | **49,33 s** |

**`INV-184645.pdf` et `INV-184645 2.pdf` ont des contenus différents.** Les suffixes « 2/3/4 » ne caractérisent donc pas à eux seuls un doublon binaire, une application ou une opération iOS. Tous les noms suffixés ne sont pas retrouvés dans les sauvegardes tardives.

**Réponse à Q3 — doublons et conflits iCloud.** Les suffixes « 2 », « 3 » et « 4 » sont compatibles avec plusieurs mécanismes de copie ou de gestion de noms identiques. Ils ne départagent pas des enregistrements répétés d’un mécanisme de conflit iCloud. Aucun élément retrouvé n’identifie ici un conflit iCloud comme origine des exemplaires identiques, ni les conditions de sa survenue. La présence des contenus dans le stockage local Fichiers des deux Mini ne reconstitue pas leur circulation antérieure. **L’origine exacte des doublons reste indéterminée ; une contribution d’iCloud n’est ni confirmée ni exclue par les données disponibles.**

Les conversions `Europe/Paris` sont cohérentes : **UTC+2 le 15**, **UTC+1 le 28**. Les 17 écarts « première création CSV moins lastused TP-03 » vont de **−8,969649 à +10,51809805 secondes**, médiane **+2,14324401 secondes**. Leur dispersion ne prouve pas un décalage constant d’horloge. La correction Windows d’environ **−9,238 secondes le 28 à 11:19:30** ne calibre pas TP-03 le 15. Ni les centièmes du CSV ni les FILETIME à 100 ns ne certifient une exactitude physique équivalente.

La comparaison complète des **72 objets** comporte **63 paires de même contenu entre téléphones** : `Birth` identique dans **54/63**, `LastModified` dans **56/63**, aucun inode identique. TP-02 regroupe **36 changements de statut le 11 juin 2024**, date d’une restauration documentée ; TP-03 conserve **16 changements de statut le 15 octobre** et **17 lastused dans la séquence**, avec d’autres états ultérieurs. L’attribut lastused est présent sur **38 objets TP-02 et 22 TP-03**. TP-02 compte 45 objets de classe C et une copie d’avis de 2025 de classe B ; les 26 TP-03 sont de classe C.

**Aucun mécanisme uniforme expliquant les 72 objets n’est établi.** La conservation partielle de dates anciennes et les états ultérieurs différents imposent de garder l’hypothèse d’une propagation des métadonnées. Les écarts ne permettent pas de choisir entre enregistrements initiaux successifs et réutilisation de dates lors d’un transfert. L’étape finale groupée sur OP-01 est nettement étayée.

La séquence TipKit du 16 n’est pas retrouvée à l’identique dans les transactions Messages de TP-02 comparées ; son événement PersonalAudio est différent. Ce contrôle écarte une duplication exacte dans ce périmètre, sans rendre les historiques TP-03 intransportables.

### 7.7. Recherche de récupération de l’archive et des rejets dans OP-01

Le **16 novembre 2026**, une recherche complémentaire a vérifié si `Archive_saddedine.zip`, `Rejets_saddedine.txt` et `Inventaire_saddedine.csv` pouvaient subsister comme fichiers supprimés dans l’image du disque interne d’OP-01. **Aucun de ces trois fichiers n’a été récupéré par cette recherche. Le CSV disponible est la pièce transmise séparément, pas une récupération depuis OP-01.**

Les trois raccourcis conservés désignent **`E:\saddedine\`**, et mémorisent respectivement **3 525 227 798 octets pour le ZIP**, **0 octet pour le TXT** et **527 208 octets pour le CSV**. Une taille nulle est compatible avec un état vide du fichier de rejets à l’instant représenté, sans certifier son contenu définitif ni l’absence de rejets. Aucun fichier vide n’a été fabriqué puis présenté comme récupéré.

Le contrôle comprend la MFT courante entière, les entrées supprimées et de corbeille, **18 candidats** lus en début et fin, les fichiers mémoire/métadonnées et le balayage de **357 162 754 048 octets non alloués, répartis sur 73 355 intervalles**, sans erreur signalée. Les **982 répertoires centraux ZIP cohérents** ont été comparés aux noms des **1 558 fichiers L16B**. Le seul nom commun est `loading.gif`, dans un ZIP de composants Sage de 28,76 Mo : son contrôle CRC réussit, mais les GIF sont différents de celui de L16B et aucun PDF Mini n’y figure. Aucun candidat ne correspond à la taille connue de l’archive ou aux noms documentaires recherchés.

La MFT courante ne retrouve que les trois `.lnk`. Une vue dérivée VSS excluant les entrées d’un cliché endommagé permet aussi de lire la MFT d’un premier cliché de 2026 ; elle ne retrouve que les mêmes noms de raccourcis. Cette lecture complémentaire ne garantit pas une reconstruction exhaustive des clichés d’origine. Des mentions résiduelles des cibles subsistent, dont **deux Shell Items identiques de 128 octets** décrivant le nom et la taille du ZIP : **ce sont des métadonnées descriptives, sans son contenu compressé**.

L’image source a été traitée en lecture seule, sans rejeu de journal. La recherche complète des clusters libres ne garantit pas la reconstruction d’une archive fragmentée sans chaîne d’allocation, écrasée ou absente du disque ; elle n’inclut pas une décompression générale de la mémoire Windows, tout le slack ou tous les conteneurs alloués. **Le résultat négatif ne prouve pas que ces fichiers n’ont jamais existé sur C:.** Leur présence comme fichiers complets sur ce volume n’est pas établie. Le support E:, son image ou les copies conservées par l’administration restent les sources directes à rechercher. La récupération ne résout donc pas le mécanisme de transfert des PDF.

Le [rapport de récupération](../inventaire-DNEF/rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md) expose les méthodes, empreintes, candidats, vue VSS et limites détaillées.

## 8. Limites et conclusion technique

### 8.1. Questions restant ouvertes et pièces utiles

| Question à résoudre | Pièce ou vérification susceptible de départager les hypothèses |
|---|---|
| Quel scellé correspond matériellement à TP-03 ? | Correspondance vérifiable entre série, UDID, description de l’appareil et numéro de scellé |
| Le téléphone a-t-il été déverrouillé après le démarrage visible sur la vidéo ? | Traces contemporaines d’authentification, d’état de protection et d’alimentation, si elles existent |
| Les PDF ont-ils été effectivement extraits le 15 octobre ? | Journaux d’outil, rapports d’extraction, traces de session ou de transfert datées |
| Comment les PDF sont-ils arrivés dans le dossier final d’OP-01 ? | Archive d’origine, support intermédiaire, historique de constitution de L16B et version de l’outil employé |
| Quels fichiers ont été effectivement retenus ou rejetés ? | CD et inventaire d’origine authentifiés, `Archive_saddedine.zip`, `Rejets_saddedine.txt` et pièces de procédure associées |

### 8.2. Conclusion technique

La sauvegarde porte des dates de 2025, manque d’Info et de journal d’acquisition, et conserve un historique de restauration partiel. Les identités logiques et dates peuvent être transportées. Aucun journal continu de démarrage, authentification ou radio, aucune image physique ou référence historique d’heure indépendante ne résout cette provenance.

**Constat de visionnage :** la [note de constatation du 16 novembre 2026](../NOTE-DE-CONSTATION-téléphones.md) consigne, le **15 octobre 2024 à 13 h 25 min 19 s**, l’intervention sur les trois téléphones d’une femme identifiée par Mme Sadedine comme étant Mme Adam, avec apparition des logos Apple sur leurs écrans, caractéristique d’une séquence de démarrage d’iPhone. L’état à la fermeture des scellés et la continuité d’alimentation jusqu’au 28 octobre ne sont pas établis. Si une extinction à la fermeture était prouvée indépendamment, un fonctionnement local ultérieur supposerait une reprise à expliquer ou une autre origine des dates.

**Les préférences du 15 au soir et du 16, puis la séquence Santé/PersonalAudio/Messages à 05:31, constituent des indices positifs de traitements système datés pendant la conservation. L’examen détaillé identifie un échec CloudKit et une routine TipKit récurrente, sans marqueur validé d’action humaine.**

**Les 17 rapprochements documentaires du 15 octobre favorisent désormais la historique de données susceptible de suivre une copie ou une restauration de TP-03. Les 27 PDF figurent dans le CSV fourni, avec les empreintes attendues ; leur création ce jour-là n’est pas démontrée.** Cette conclusion complète l’identité de contenu commune aux deux Mini, sans résoudre l’appareil physiquement source ni le scellé correspondant.

L’utilisation physique de TP-03 aux heures civiles indiquées reste non certifiée. Ni premier déverrouillage après le démarrage constaté dans la vidéo, ni extraction directe, ni auteur ou rupture de scellé ne sont démontrés ; l’absence de manipulation ou le maintien éteint ne le sont pas davantage. Les traces de Mail/Fichiers ne désignent pas les PDF. Le regroupement sur OP-01 le 28 est étayé, mais son outil et les étapes intermédiaires restent inconnus.

Les pièces discriminantes seraient un rapprochement séries/scellés, les documents de conservation et d’alimentation, une acquisition plus proche de 2024, l’historique de restauration, des journaux contemporains à référence de temps indépendante, ainsi que l’archive finale, les supports intermédiaires et la version/journal de l’outil de transfert. Le CSV est désormais fourni ; le CD d’origine, le contenu du ZIP et le fichier de rejets restent à vérifier séparément. Leur disponibilité n’est pas présumée.

## 9. Pièces techniques et termes de lecture

| Domaine | Pièces de contrôle |
|---|---|
| Inventaire, déchiffrement et empreintes | [Synthèse](recherche-TP-03/summary.json), [collecte](recherche-TP-03/collection.json), [contrôles natifs](recherche-TP-03/final-checks/native-integrity.json) |
| SQLite et tri temporel | [Statistiques](recherche-TP-03/scan/timestamp-stats.json), [erreurs et limites](recherche-TP-03/scan/errors.json) |
| Séquence et provenance | [Santé](recherche-TP-03/priorite/findings/health.json), [préférences](recherche-TP-03/plists/dates.json), [corrélations](recherche-TP-03/correlations/results.json) |
| Examen approfondi du 16 | [Conseils, CloudKit, protection et contrôles élargis](../investigations/20261110-tp03-intervention-humaine/compte-rendu.md) |
| Caméras et PDF | [Métadonnées WebKit/caméras](recherche-TP-03/final-checks/camera-webkit.json), [identités PDF](recherche-TP-03/priorite/pdf-identities.json) |
| Comparaisons entre appareils | [Rapprochements transversaux](../investigations/20261110-telephones/compte-rendu.md), [contrôle avant ouverture](../investigations/20261110-revue-intervention-scelles/compte-rendu.md) |
| Inventaire DNEF et 17 rapprochements du 15 | [Réponse Q1](../inventaire-DNEF/rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md), [annexe des 72 objets](../inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/annexe-objets.md) |
| BFU, transfert, applications, doublons et horloges | [Investigations B à E](../inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md), [contrôle d’intégrité](../inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/verification-finale.json) |
| Contrôle du 15 octobre, 13:25–13:51, et complément Fichiers | [Note de vérification](../inventaire-DNEF/rapports/Note_reponse_TP02_TP03_15oct2024.md), [résultats SIFT](../inventaire-DNEF/documents-recus/verification-20241015-1325-1351/resultats-sift-v2.json), [complément Fichiers](../inventaire-DNEF/documents-recus/verification-20241015-1325-1351/complement-fichiers-sift.json) |
| Archive finale et fichier de rejets | [Recherche de récupération dans OP-01 du 16 novembre](../inventaire-DNEF/rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md), [bilan du balayage](../inventaire-DNEF/travaux-techniques/recuperation-archives-20261116/prive/balayage-v3/synthese.json) |
| Reproduction | [Notice et scripts](scripts/README-TP-01-TP-03.md) |

Les pièces conservent requêtes, localisateurs, champs bruts, erreurs et empreintes. Les contenus clairs restent sur SIFT à accès restreint ; les résultats privés sous `recherche-TP-03/` sont exclus de Git. Les synthèses n’exportent ni mots de passe, ni mesures médicales, ni conversations.

| Terme | Sens dans ce rapport |
|---|---|
| Sauvegarde logique / manifeste | Fichiers retenus par iOS / index de leurs chemins et métadonnées ; pas une image de tous les secteurs. |
| UDID / identité Santé / UUID de bibliothèque | Identifiants d’appareil déclaré, d’installation Santé et de historique de données ; leurs portées ne sont pas interchangeables. |
| Date de mesure / création d’objet | Intervalle représenté / enregistrement de son objet en base. Leur décalage ne date pas automatiquement un geste humain. |
| TipKit / CloudKit | Conseils applicatifs / mécanismes de données cloud. Une règle évaluée ou une tentative interne ne prouve ni affichage ni transfert réussi. |
| SQLite / WAL / `quick_check` | Base / journal de transactions / contrôle de cohérence. Un contrôle incomplet faute d’extension ne démontre pas une corruption. |
| Pair record | Fichier Apple conservant une relation de confiance ; ses métadonnées ne sont pas un journal de chaque branchement. |

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe Donnat — Donnat Dev
