# Rapport d’analyse technique du téléphone TP-01

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev

**Équipement :** iPhone 13 — série `Q13QT4F164`

## 1. Objet et synthèse

Ce rapport présente les données de TP-01 relatives à la conservation des téléphones du **15 au 28 octobre 2024**, les indices d’activité, les communications, les métadonnées cloud et les limites de leur attribution au matériel. Il repose sur une sauvegarde logique tardive, sans image physique ni journal continu d’utilisation.

**Des données portent des dates comprises dans la période de conservation, mais aucune interaction locale sur le téléphone physique TP-01 avant l’ouverture du 28 à 11:30 n’est établie. Son maintien à l’état éteint n’est pas davantage certifié.**

| Domaine | Résultat | Conclusion permise |
|---|---|---|
| WhatsApp avant ouverture | Deux messages entrants datés du **15 à 16:51 et 17:41**, avec un autre horodatage groupé le **28 vers 16:13** | Récupération ou traitement différé compatible ; réception ou lecture locale le 15 non démontrée. |
| Messagerie vocale | Dates de messages les **15, 17 et 19 octobre** dans une table `deleted` | Ces dates ne sont pas des dates de suppression ou d’écoute. |
| Cloud et ressources | Métadonnées iCloud du **23 octobre**, dates de ressources et caches pendant la conservation | Leur provenance ne permet pas de localiser les opérations sur TP-01. |
| SMS, photos et Wi-Fi | Aucun événement central dans les champs SMS/photos et les dates Wi-Fi contrôlés | Résultat borné aux données conservées ; l’absence de journal n’est pas une preuve d’inactivité. |
| Après ouverture le 28 | Traitements système dès **14:26**, regroupement WhatsApp à **16:13**, deux lignes sortantes vers **17:44** | Indices d’activité du compte et des services après ouverture, sans auteur ou origine physique exclusive établis. |
| Extraction ou intrusion | Aucun outil, appairage ordinateur ou accès non autorisé identifié en octobre | Aucune rupture de scellé ou extraction clandestine démontrée ; des traces absentes ou omises restent possibles. |

## 2. Identification et repères de procédure

### 2.1. Identité de la sauvegarde

| Élément | Valeur |
|---|---|
| Code de mission | **TP-01** |
| Attestation | iPhone 13 **vert**, modèle `MNGK3ZD/A` |
| Série de l’attestation et de `Info.plist` | **Q13QT4F164**, concordance exacte |
| Type produit | `iPhone14,5` |
| UDID | **`00008110-000A70993407801E`** |
| Système déclaré lors de la sauvegarde | `26.6.2`, build `23G90` ; ne certifie pas la version installée en octobre 2024. |

Le PV décrit un **iPhone 13 noir** pour le scellé n° 2, tandis que l’[attestation](../remise-documents/attestation-de-remise.md) décrit TP-01 comme vert. Le modèle en fait un candidat, mais la divergence de couleur et l’absence de série/IMEI dans les passages contrôlés empêchent une correspondance matérielle certaine. Les codes de mission et numéros de scellés restent distincts.

### 2.2. Fenêtres et conventions horaires

Les [mails](../docs/mail.txt), le [complément de la cliente](../docs/mail-2.txt) et la [lecture du PV](../investigations/20261108-analyse-pv/compte-rendu.md) distinguent :

| Repère | Portée |
|---|---|
| **15 octobre vers 13:30** | Perte d’accès déclarée aux téléphones ; pas une heure vérifiée de fermeture. |
| **15 octobre après 14:19** | Mise sous scellés consignée, sans heure individuelle de fermeture. |
| **28 octobre à 11:30** | Ouverture des téléphones et déverrouillage par la cliente. |
| **28 octobre à 19:20** | Clôture ; restitution sans heure individuelle, récupération approximative déclarée vers 19:20. |

La **fenêtre centrale de recherche** va du **15 à 13:30 au 28 à 19:20** ; elle comprend les opérations après ouverture. Le contrôle spécifique avant ouverture utilise **15 octobre 14:19 inclus → 28 octobre 11:30 exclu**, sans affirmer que chaque scellé était déjà fermé à 14:19. La comparaison couvre le **1er octobre au 15 novembre inclus**.

Les conversions utilisent **Europe/Paris**, UTC+2 avant le changement d’heure du 27 octobre, UTC+1 ensuite. Aucune référence indépendante n’étalonne l’horloge de 2024. Une date après le 28 à 11:30 ne démontre pas une activité sous scellé fermé.

## 3. Sauvegarde, intégrité et méthode

### 3.1. Support et couverture

La source est la sauvegarde logique non chiffrée identifiée par l’UDID TP-01, conservée sous `TP-01/00008110-000A70993407801E/` dans le dossier forensic.

| Métadonnée | Valeur enregistrée, UTC |
|---|---|
| `Manifest.plist.Date` | **09/11/2026 11:31:28.171107** |
| `Status.plist.Date` | **09/11/2026 11:48:09.677857** |
| `Info.plist.Last Backup Date` | **09/11/2026 11:48:23** |
| État | `IsEncrypted=false`, `IsFullBackup=false`, `BackupState=new`, `SnapshotState=finished` |

Ces états et dates ne remplacent pas un journal indépendant d’acquisition. Le manifeste contient **78 457 entrées** : **48 895 fichiers `flags=1`**, 29 487 entrées `flags=2` et 75 `flags=4`. Les **48 895 objets attendus sont présents**, avec des tailles déclarées totalisant **12 648 356 415 octets**. La présence des objets ne constitue pas une authentification exhaustive de tous leurs contenus ; `IsFullBackup=false` ne prouve pas à lui seul un objet manquant.

### 3.2. Contrôles et préservation

Empreinte SHA-256 du manifeste source :

```text
ab12f937dc0a6d1c1ca15312a8c3a9faf1322e8d44fa5e68b4dd18e8676ca0a8
```

La collecte principale porte sur **2 420 objets, soit 620 310 196 octets**, avec un complément Wi-Fi de secours et onze ressources `.ahe`. Les objets collectés et fichiers de tête ont des empreintes source avant/après identiques à celles de leurs copies. Les sources sont ouvertes en lecture et les écritures réservées aux dossiers de travail SIFT. Le partage reste accessible en écriture par l’environnement ; il ne constitue pas un bloqueur matériel.

Le manifeste satisfait `quick_check=ok`. Sur **877 contenus à signature SQLite**, **826 contrôles donnent `ok`** et **51 restent incomplets**, notamment faute de collations ou tokenizers spécifiques. Ces limites ne sont pas des corruptions démontrées. **355 bases** ont un WAL collecté ; les copies sont ouvertes en lecture seule avec leurs compagnons, sans ignorer les WAL par un mode `immutable` inadapté aux bases d’activité.

Le tri temporel recherche différentes unités et époques, puis valide les champs retenus selon leur schéma. Un nombre compatible avec une date reste un candidat tant que sa signification n’est pas établie. Les BLOB, formats propriétaires, tables virtuelles et données supprimées ne sont pas intégralement interprétés.

## 4. Communications

### 4.1. SMS et iMessage

`sms.db` contient **2 561 messages**. Aucun champ `date`, `date_read`, `date_delivered` ou `date_played` ne tombe dans la fenêtre centrale après conversion des nanosecondes depuis l’époque Apple. Le contrôle spécifique avant ouverture ne retrouve pas davantage de ligne par date de message, lecture ou livraison.

Le dernier message précédent est daté du **12 octobre à 13:42:09.661421**, `ROWID=642`, et le premier suivant du **17 novembre à 16:56:32.189545**, `ROWID=613`. Les ROWID ne forment donc pas une chronologie fiable d’arrivée. La base ne permet pas d’exclure des messages supprimés ou un historique importé.

### 4.2. WhatsApp

Les magasins ordinaire et Business contiennent respectivement **15 473 et 10 lignes `ZWAMESSAGE`**. Business ne livre pas de date centrale dans les champs examinés.

| `Z_PK` | Date de message, Paris | Champ `ZSENTDATE`, Paris | Portée |
|---|---|---|---|
| **10051** | 15/10 16:51:24 | 28/10 16:13:08.424826 | Entrante, type 0 ; pas de réception locale le 15 démontrée. |
| **10050** | 15/10 17:41:48 | 28/10 16:13:08.426692 | Même réserve. |
| **10052** | 28/10 16:13:09.009604 | Non renseigné | Type 10 ; pas une conversation humaine automatiquement identifiable. |
| **10053** | 28/10 17:44:24.344572 | 28/10 17:44:24.401593 | `ZISFROMME=1`, type 0, statut 6 ; sortante après ouverture. |
| **10054** | 28/10 17:44:54.357658 | 28/10 17:44:54.391634 | Même qualification. |
| **10055** | 28/10 17:57:57 | 28/10 23:24:42.795958 | Entrante ; second champ postérieur à la clôture. |

**Quatorze lignes datées du 15 dans `ZMESSAGEDATE` ont un `ZSENTDATE` groupé le 28 entre 16:13:07.674380 et 16:13:08.426692.** Cet ensemble est compatible avec une récupération ou un traitement différé. Le nom du champ ne prouve ni réception locale ni lecture ; l’index de recherche qui reprend ces dates n’est pas une deuxième source indépendante. Aucune date du 16 au 27 n’est retrouvée dans ces deux champs.

Les deux lignes sortantes du 28 sont des indices d’activité du compte après ouverture, sans opérateur ou appareil source exclusif établi. Les bases d’appels WhatsApp ne fournissent pas de date centrale. **L’historique d’appels natifs `CallHistory.storedata` est absent du manifeste** : il ne s’agit pas d’un résultat « zéro appel ».

### 4.3. Messagerie vocale

Sept lignes de la table `deleted` de `voicemail.db` portent des dates centrales : **15/10 à 13:32:24 et 16:18:54 ; 17/10 à 12:08:42 et 15:37:40 ; 19/10 à 15:58:55 ; 28/10 à 18:06:28 et 19:08:38**. Toutes ont `trashed_date=0`.

Il s’agit de dates associées aux messages, **pas de dates d’effacement**. Une messagerie opérateur peut conserver un message alors que le téléphone n’est pas joignable. Ni appel décroché, ni écoute, ni suppression sous scellé ne sont démontrés. L’état `deleted` observé dans la sauvegarde de 2026 ne date pas la transition vers cet état.

## 5. Réseau, cloud et ressources applicatives

### 5.1. Wi-Fi

Le fichier `com.apple.wifi-networks.plist` est un dictionnaire vide ; sa copie de secours contient **37 réseaux et 423 dates plist**, sans valeur centrale ni nom **`ASUS_Z01RD`**. Le fichier distinct `known-networks` n’est pas présent au chemin contrôlé.

Ces préférences décrivent des états partiels, pas toutes les connexions historiques. Leur contenu ne prouve ni absence de Wi-Fi en octobre ni association au réseau ASUS trouvé dans TP-02. Aucun identifiant client Wi-Fi exploitable ne permet ici une attribution matérielle aux appareils nocturnes recensés par la Freebox.

### 5.2. iCloud Drive et provenance des dates du 23 octobre

Les magasins `CloudDocs/session/db/client.db` et `server.db` contiennent chacun **deux `item_birthtime` au 23 octobre à 09:39:06 et 09:47:07**, un `version_mtime` à 09:47:07 et **dix `item_lastusedtime` entre 09:39:31 et 09:41:38**. La répétition client/serveur ne forme pas deux témoins indépendants d’un geste local.

Les dix lignes sont associées, dans le champ de version contrôlé, à `version_device=1`, nommé **« iPhone de MALIKA »**. Le nom de TP-01 à la sauvegarde, **« iPhoneun. Nscz s »**, figure comme une autre entrée. Un nom peut changer et ne remplace pas un UDID ; `version_device` ne prouve pas l’appareil ayant produit `item_lastusedtime`. **Aucune action du 23 n’est matériellement attribuée au téléphone scellé.**

### 5.3. Ressources et caches

Le tri retrouve **1 050 `last_timestamp` centraux** dans des traductions `multi_language` de `com.ctrip.EBooking` et une date de configuration CargoSDK le **22 à 05:31:33**. Ce sont des ressources et paramètres, pas des journaux de session ; leurs dates peuvent être conservées lors d’une arrivée ultérieure.

Le manifeste conserve également **28 dates Birth/LastModified sur 14 fichiers AliExpress** entre le 15 et le 24 : onze modules `.ahe`, deux PNG et un JSON. Les dates sont identiques par paire. Les `.ahe` sont copiés et empreintés, mais leur format interne n’est pas décodé. Une écriture locale ancienne reste possible ; création locale, import, restauration et date de ressource ne sont pas départagés. Ces objets ne sont donc pas qualifiés d’automatiques par principe.

## 6. Traitements du 28 octobre après ouverture

| Heure de Paris | Constat conservé | Interprétation limitée |
|---|---|---|
| **14:26:41 et 16:47:01** | Quatre transactions TipKit Calendrier | Traitements internes, pas quatre consultations. |
| **14:31:35** | `homed/hh1LastSharedUserAddRemoveTimestamp` | État lié au partage, sans ajout de tiers ou accès caméra démontré. |
| **14:31:36–16:21:54** | 28 transactions TipKit Messages | Ce ne sont pas 28 SMS ; aucun SMS central conservé. |
| **14:31:42–14:31:57** | Transactions Notes, Mail, Rappels | Traitements de fond possibles. |
| **14:32:21 et 14:39:07** | Transactions Téléphone et Safari | Ni appel ni site consulté établi. |
| **16:13:07–16:13:09** | Groupe d’horodatages WhatsApp | Traitement différé compatible. |
| **16:17:17** | Quatre transactions TipKit Fichiers | Pas une preuve d’export de quatre fichiers. |
| **16:18:23** | Trois ressources WeChat datées | Sens fonctionnel non validé ; pas trois messages. |
| **16:59:23.299** | `accessoryd.plugin.plist/uartDetachTimes/1` | Information compatible avec un détachement d’accessoire, sans ordinateur ou extraction identifié. |
| **17:44:24 et 17:44:54** | Deux lignes WhatsApp sortantes | Activité du compte après ouverture. |
| **17:51:40** | Sept transactions TipKit Photos | Pas sept photographies prises ou consultées. |

Treize lignes TCC conservent aussi des modifications d’autorisations entre **14:26:13 et 17:51:40**. Elles ne sont ni un journal d’ouvertures d’applications ni un historique de déverrouillages.

Plusieurs magasins décrivent ainsi une reprise de traitements le 28. Une origine commune, une restauration ou des tâches automatiques restent possibles. Aucun compteur continu ne date un allumage ; le contexte d’examen au PV ne suffit pas à identifier un outil d’extraction ou son opérateur.

## 7. Photos, profils et couverture absente

La photothèque comporte **6 455 actifs**. Aucune date centrale n’apparaît dans les six champs de création, ajout, modification, ajustement, mise à la corbeille et dernier partage contrôlés. Les `ZTRASHEDDATE` sont tous nuls dans cet état, sans preuve d’absence de suppression antérieure. Aucune séquence analogue à la capture du 28 discutée pour TP-02 n’est mise en évidence.

Le manifeste ne contient pas les objets `healthdb`, `knowledgeC.db`, `interactionC.db`, diagnostics `.ips` ou domaines LSC/Xiaomi recherchés. Leur absence dans cette sauvegarde logique ne prouve pas qu’ils n’ont jamais existé sur le téléphone et empêche une contre-épreuve équivalente à celle de TP-02.

Le `ProfileTruth` utilisateur est vide ; celui du système contient notamment une entrée `com.apple.Free_fr.…`, sans preuve d’une gestion MDM hostile. Aucun historique exhaustif des profils ou appareils associés depuis 2021 n’est reconstitué. Un chemin `Library/LockdownMode` ne constitue pas un appairage Apple avec un ordinateur. Les recherches d’outils et artefacts décodés ne fournissent pas de session d’extraction d’octobre identifiée.

## 8. Limites et conclusion technique

La sauvegarde est postérieure de deux ans aux faits. Les états et historiques peuvent être copiés, restaurés ou synchronisés. Une date de message, d’objet cloud ou de ressource peut précéder son arrivée sur l’appareil sauvegardé. À l’inverse, un journal absent ou une table sans date centrale ne certifie pas l’inactivité.

**Observation de visionnage rapportée :** le prestataire indique que les vidéos du salon montrent une agente rallumant les téléphones le **15 octobre vers 13:25**, avant le scellement. Le [rapport final](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés) distingue ce récit des seuls aperçus d’un clip débutant à 13:28. L’état final à la fermeture et la continuité d’alimentation jusqu’au 28 ne sont pas établis ; aucun nouveau visionnage indépendant n’est revendiqué par ce rapport.

**TP-01 conserve des données datées pendant la conservation, mais aucun faisceau établissant son fonctionnement local ou une interaction humaine avant ouverture. Les traitements et lignes sortantes du 28 sont postérieurs à l’ouverture documentée.** Ils ne peuvent pas être reportés aux journées précédentes. Ni rupture de scellé, ni extraction clandestine, ni identité d’auteur ne sont démontrées ; l’inactivité ou le maintien éteint ne sont pas certifiés.

Les éléments discriminants seraient une acquisition plus proche de 2024, l’historique des sauvegardes/restaurations, les identifiants matériels des appareils cloud, les relevés opérateur et les documents de conservation. Leur disponibilité n’est pas présumée. Les conclusions de TP-02 et TP-03 restent propres à leurs données.

## 9. Pièces techniques et termes de lecture

| Domaine | Pièces de contrôle |
|---|---|
| Inventaire, copies et empreintes | [Synthèse](recherche-TP-01/summary.json), [collecte](recherche-TP-01/collection.json) |
| SQLite et tri temporel | [Statistiques](recherche-TP-01/scan-v2/timestamp-stats.json), [erreurs et limites](recherche-TP-01/scan-v2/errors.json) |
| Communications | [Contrôle WhatsApp](recherche-TP-01/targeted/whatsapp.json), [contrôles complémentaires](recherche-TP-01/supplement-v2/results.json) |
| Wi-Fi | [Dates des préférences](recherche-TP-01/supplement-v2/wifi-dates.json) |
| Comparaison avant ouverture | [Contrôles communs aux téléphones](../investigations/20261110-revue-intervention-scelles/compte-rendu.md) |
| Provenance et autres appareils | [Rapprochements transversaux](../investigations/20261110-telephones/compte-rendu.md) |
| Reproduction | [Notice et scripts](scripts/README-TP-01-TP-03.md) |

Les pièces conservent requêtes, valeurs brutes, localisateurs et empreintes. Les contenus de travail restent sur SIFT à accès restreint ; les résultats sous `recherche-TP-01/` sont exclus de Git. Les contrôles ne reproduisent ni mot de passe ni corps des conversations.

| Terme | Sens dans ce rapport |
|---|---|
| Sauvegarde logique / manifeste | Ensemble de fichiers sélectionnés par iOS / index de leurs chemins et métadonnées. Ce n’est pas une copie de tous les secteurs du téléphone. |
| UDID / identité matérielle | Identifiant déclaré d’appareil / attribution au matériel à une date donnée. Une sauvegarde identifiée peut contenir des historiques transportés. |
| SQLite / WAL | Base de données / journal de transactions pouvant compléter son état. Une collecte doit tenir compte des compagnons disponibles. |
| TipKit / TCC | Gestion de conseils applicatifs / autorisations d’accès. Une transaction n’est pas automatiquement une consultation ou un déverrouillage. |
| Époque Apple | Origine temporelle au 1er janvier 2001 UTC, avec unités à vérifier selon le champ. Une conversion correcte ne garantit pas la justesse de l’horloge source. |
