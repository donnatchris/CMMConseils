# Rapport d’analyse technique du téléphone TP-02

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev — christophe@donnat.dev

**Équipement :** iPhone 13 mini — série `F5466LV9V7`

## 1. Objet et périmètre

Ce rapport présente les indices de fonctionnement, de communications, de connexions et de traitements de données conservés dans la sauvegarde de TP-02 pour la période du **15 au 28 octobre 2024**. Il examine leur provenance, les opérations après ouverture et les rapprochements avec OP-01, les autres téléphones, la Freebox et les caméras.

La présence d’une trace datée, son attribution au téléphone physique à cette date, son déclenchement par une personne et l’identité de cette personne sont des propositions distinctes. Une synchronisation peut transporter des objets et leurs dates ; une restauration peut également conserver un historique interne. Les mécanismes ne sont pas interchangeables et aucun n’est présumé avoir produit une ligne particulière sans preuve.

Les résultats portent sur une **sauvegarde logique chiffrée tardive**, pas sur une image physique de l’iPhone ou un historique exhaustif depuis 2021. Les [mails de mission](../docs/mail.txt) et [complémentaires](../docs/mail-2.txt), l’[attestation](../remise-documents/attestation-de-remise.md) et le PV définissent le contexte. L’analyse est une investigation privée, sans désignation comme expertise judiciaire.

## 2. Synthèse des conclusions

**TP-02 conserve un faisceau d’indices datés avant l’ouverture des téléphones : traitements de services le 17 octobre vers 17:15–17:18, puis configuration et association Wi-Fi à `ASUS_Z01RD` vers 17:25, ainsi que 53 appels du 15 au 26. Cette chaîne Wi-Fi est la piste la plus informative d’une intervention possible, mais son attribution matérielle à TP-02 et son déclenchement humain restent non établis.**

| Domaine | Résultat technique | Portée et limite |
|---|---|---|
| **17 octobre** | Santé, Contacts, Messages, Téléphone et Photos enregistrent des traitements ; les propriétés Wi-Fi décrivent ensuite une chaîne de **4,672320 s**. | Soutient une activité de plusieurs services sur l’installation source ; ni démarrage ni déverrouillage démontré. |
| **Appels** | **53 lignes**, dont **22 marquées sortantes sur huit jours et 19 à durée positive**. | L’origine matérielle n’est pas identifiée ; synchronisation ou restauration restent possibles. |
| **27 octobre** | **3 123 dates de modification Photos** groupées vers 02:44–02:45, UTC+2. | Traitement groupé de bibliothèque possible ; pas 3 123 retouches ou consultations humaines. |
| **28 octobre après 11:30** | Trois SMS de validation/réinitialisation avec dates de lecture, associations Wi-Fi, séquence compatible avec une capture d’écran et traitements Photos/LSC. | Après l’ouverture documentée ; ne prouve pas une manipulation sous scellé fermé. |
| **Provenance Photos** | Sept migrations et leur journal portent l’**UDID TP-02 exact**, avant et après octobre. | Renforce le rattachement historique de la lignée, sans rendre ses historiques intransportables. |
| **WidgetKit** | Diagnostic portant un lancement le 17 et une capture le 28, avec compteurs temporels différents du calendrier. | Ne date ni un allumage ni un déverrouillage ; ne prouve ni erreur d’horloge ni sommeil prolongé. |
| **Caméras et extraction** | Présence de ressources de panneau caméra et de configurations ; aucun flux consulté ou outil d’extraction d’octobre identifié. | Un cache ou une capacité du logiciel ne prouve pas l’utilisation de la fonction. |
| **Autres supports** | Nom ASUS présent aussi dans le fichier d’échange d’OP-01 ; PDF Mini communs à TP-02 et TP-03. | Ni point d’accès commun daté, ni téléphone source exclusif, ni copie finale saisie certifiés. |

**Aucune rupture de scellé, identité d’auteur, consultation de caméra, extraction clandestine ou suppression volontaire de preuve n’est démontrée. L’absence de toute manipulation ou le maintien du téléphone éteint ne sont pas davantage certifiés.**

## 3. Identification, procédure et horloges

### 3.1. Identification du téléphone

| Élément | Valeur |
|---|---|
| Code / équipement | **TP-02**, iPhone 13 mini rouge |
| Série de l’attestation et de `Info.plist` | **F5466LV9V7**, concordance exacte |
| Modèle commercial | **MLK83KH/A** |
| IMEI documentaires transcrits | `35292959671648 4` et `35292959 723940 3` |
| Type produit | **`iPhone14,4`** |
| UDID / dossier de sauvegarde | **`00008110-001C69A002BA801E`** |
| Système déclaré par `Info.plist` | **18.5**, sans certification de la version d’octobre 2024 |

Le PV distingue deux Mini rouges sans série ou UDID : **TP-02 ne peut pas être attribué avec certitude au scellé n° 3 ou n° 4**. La couleur, l’ordre des codes internes, les PDF communs et l’insertion SIM ne suffisent pas à les départager.

### 3.2. Repères documentaires et fenêtres de recherche

| Date et heure de Paris | Provenance et précision |
|---|---|
| **15 octobre 2024** | Perquisition ; heure de début non fournie. |
| **15 octobre vers 13:30** | Perte d’accès déclarée aux téléphones, pas heure vérifiée de fermeture. |
| **15 octobre après 14:19** | Mise sous scellés au PV, sans fermeture individuelle précisément datée. |
| **28 octobre à 10:22** | Arrivée de la cliente ; ce n’est pas l’ouverture des téléphones. |
| **28 octobre à 11:30** | Ouverture des trois téléphones et déverrouillage par la cliente. |
| **28 octobre à 11:45** | Insertion SIM dans le scellé n° 3, sans équivalence TP-02/TP-03 certaine. |
| **28 octobre à 19:20** | Clôture ; restitution sans heure individuelle, récupération approximative déclarée vers 19:20. |

La **fenêtre principale de calcul** est **15/10/2024 13:30 → 28/10/2024 19:20 Paris**, soit environ `2024-10-15T11:30:00Z` à `2024-10-28T18:20:00Z`, bornes incluses. Elle comprend les opérations après ouverture et ne doit pas être décrite comme une fenêtre de scellé fermé.

Le contrôle spécifique avant ouverture utilise **15 octobre 14:19 inclus → 28 octobre 11:30 exclu**, sans supposer tous les scellés déjà fermés à 14:19. La comparaison élargie couvre le **1er octobre au 15 novembre inclus**, soit `[2024-09-30T22:00:00Z ; 2024-11-15T23:00:00Z[`.

Les conversions utilisent **Europe/Paris**, UTC+2 puis UTC+1 après le changement du 27 octobre. Les heures répétées sont distinguées par leur décalage. **La correction de conversion ne garantit pas la justesse de l’horloge source**, qui n’est pas étalonnée contre une référence indépendante de 2024.

## 4. Sauvegarde, déchiffrement et cohérence

### 4.1. Source et couverture

La sauvegarde Mac chiffrée contient `Info.plist`, `Status.plist`, `Manifest.plist`, `Manifest.db` et les objets par fileID. Le manifeste comporte **202 928 entrées**, dont **137 844 fichiers ordinaires selon le filtre `flags=1`**. Tous les objets référencés sont présents, sans objet manquant ou orphelin dans ce recensement. Les contenus chiffrés totalisent **102 552 017 488 octets**, hors fichiers de tête.

| Métadonnée | Date décodée | État pertinent |
|---|---|---|
| `Info.plist.Last Backup Date` | **12/10/2026 20:59:21** | Série concordante, version 18.5 |
| `Status.plist.Date` | **18/09/2026 18:45:43.504067** | `finished`, `BackupState=new`, `IsFullBackup=false` |
| `Manifest.plist.Date` | **18/09/2026 17:58:21.940905** | `IsEncrypted=true` |

L’écart septembre/octobre n’est pas résolu par un journal Mac, qui manque au dossier. Les dates des plist ne sont pas des dates de système de fichiers ni une certification indépendante de toutes les étapes de copie. `IsFullBackup=false` ne démontre pas des objets référencés absents puisque leur présence est contrôlée.

La sauvegarde logique ne garantit pas la conservation des fichiers exclus par iOS, des états anciens, des secteurs non alloués ou des données définitivement supprimées.

### 4.2. Déchiffrement et intégrité des extractions

Le manifeste déchiffré, de **264 048 640 octets**, donne `quick_check=ok`. Un déchiffrement indépendant du même manifeste source produit la même empreinte :

```text
SHA-256 Manifest-decrypted.db
cd34919ad3a2cb958e130b6ea7453e71f30fb02336d61f2e1dca0f2fb2b46eeb
```

**3 945 fileID distincts** sont déchiffrés, pour **1 367 399 998 octets** :

| Ensemble sélectionné | Fichiers | Octets déchiffrés |
|---|---:|---:|
| Applications caméras | 525 | 178 755 431 |
| Système et applications Apple prioritaires | 616 | 305 157 729 |
| Photos et préférences complémentaires | 2 714 | 786 346 406 |
| Médias sélectionnés | 33 | 19 212 053 |
| WhatsApp | 2 | 66 420 736 |
| Artefacts système et flux complémentaires | 55 | 11 507 643 |

Les empreintes des **3 890 premiers objets** et des **55 compléments** sont contrôlées avec leurs sources chiffrées et extractions. Il ne s’agit pas d’une relecture cryptographique intégrale des quelque 95,51 Gio de contenus chiffrés.

Les analyses principales utilisent des copies sur l’hôte ; les contrôles communs aux téléphones incluent des lectures sur SIFT. Les sources ne sont pas des destinations d’écriture. Les sélections sont vérifiées par domaine, chemin et fileID ; les copies et résultats restent distincts. Le mot de passe est saisi sans écho, non enregistré dans les scripts ou synthèses. Les données privées restent à accès restreint et sont exclues de Git.

### 4.3. Écarts de tailles et empreintes internes

Les lots principaux présentent **92 écarts MBFile/clair**, auxquels s’ajoutent les **deux bases WhatsApp**, soit **94 écarts dans ces ensembles contrôlés**. Parmi les 92, MBFile est plus grand dans 73 cas et plus petit dans 19. Aucun fichier n’est tronqué pour rejoindre artificiellement la taille déclarée.

| Base ciblée | Taille MBFile moins taille extraite | Équivalent en pages de 4 096 octets |
|---|---:|---:|
| Photos | **65 183 744 octets** | 15 914 |
| Santé générale | 61 440 octets | 15 |
| Santé sécurisée | 1 245 184 octets | 304 |
| SMS | 524 288 octets | 128 |
| Appels | 159 744 octets | 39 |

Photos annonce **835 297 280 octets**, contre **770 113 536 extraits**. Les en-têtes SQLite correspondent aux tailles extraites. L’audit de `iphone_backup_decrypt 0.11.2` confirme une écriture du contenu complet, avec retrait du seul padding AES-CBC de **1 à 16 octets** : ce mécanisme n’explique pas l’écart de plusieurs mégaoctets.

Les **1 307 Digest de 20 octets disponibles** correspondent au SHA-1 des **objets chiffrés**, pas des contenus clairs. Cette cohérence se rapporte à la copie examinée et n’est pas une signature historique inviolable.

Les 254 premières bases confirmées ont une freelist déclarée nulle ; 185 partagent un profil d’en-tête identique. Ces régularités sont compatibles avec des copies reconstruites ou sérialisées, sans démontrer l’API ou le procédé utilisé. La cause exacte des écarts reste inconnue. **Aucune falsification n’est déduite et l’exhaustivité des anciennes lignes ou données supprimées n’est pas garantie.**

### 4.4. SQLite et formats non interprétés

Les premières sélections et WhatsApp comportent **254 bases à signature SQLite**, dont **232 `quick_check=ok`** et **22 contrôles incomplets** faute de collations spécifiques ; deux tables virtuelles AddressBook ne sont pas entièrement décrites. Trois signatures supplémentaires portent le total à **257**, sans extrapoler les 232 contrôles au total des 257.

Le manifeste référence **78 compagnons WAL/SHM/journal**, mais aucun pour Photos et les sept bases système ciblées. Les compagnons disponibles sont traités sur copies selon la méthode documentée ; un WAL historique absent ne peut pas être rejoué. Les transactions applicatives `ATRANSACTION` sont distinctes d’un WAL.

Les formats SEGB, Protobuf, LZFSE et ressources propriétaires ont leurs propres contrôles. Un déchiffrement réussi ne démontre pas le décodage du format interne ; des champs opaques et des candidats non sélectionnés restent hors de la couverture.

## 5. Traitements du 17 octobre et provenance de l’installation

### 5.1. Séquence de services avant l’association Wi-Fi

| Heure de Paris le 17, UTC+2 | Constat | Portée |
|---|---|---|
| **17:15:33**, puis **17:16:01** | CommCenter, état `from_dated` puis entrée `mdn match transfer` | Remappage de libellé ; ni transfert physique, SIM, appel ou démarrage démontré. |
| **17:15:46.8308** | `procLaunch` du diagnostic WidgetKit capturé le 28 | Date déclarée de lancement, avec réserves d’horloge et de provenance détaillées en section 9. |
| **17:15:48.108443** | Création groupée de 24 intervalles Santé d’énergie de repos | Calculs horaires différés, pas 24 gestes ou 24 moments d’utilisation. |
| **17:15:48.267241 et .269086** | Créations d’objets de distance et pas | Mesures représentant le **15 à 13:12:49–13:15:30**, pas un déplacement le 17. |
| **17:16:01.915835 et 17:16:13.168689** | Deux sauvegardes de séquences AddressBook | Traitements client, sans consultation Contacts établie. |
| **17:16:26.884375–.916920** | Huit transactions TipKit Messages | Règles, paramètres et conseils ; ni SMS lu ni premier plan démontré. |
| **17:16:27.568770 et 17:16:28.548546** | Deux transactions Photos/CPL | Traitements de synchronisation, sans transfert réussi ou ouverture de Photos démontré. |
| **17:18:07.047572–.085727** | Quatorze transactions TipKit Téléphone | Seize changements de règles, pas quatorze appels. |
| **17:25:37.672403** | Création d’un objet d’énergie active | Environ dix secondes avant la génération de MAC ; mesure terminée vers 17:15:37. |
| **17:25:47–52** | Propriétés Wi-Fi `ASUS_Z01RD` | Chaîne de configuration/association conservée, détaillée en section 6. |

**Plusieurs services enregistrent des traitements avant la chaîne Wi-Fi.** La seule arrivée d’un mot de passe ne rend pas compte de tout cet ensemble. Une reprise automatique de services, une intervention ou le transport d’un état complet restent à départager. Les traitements CPL précèdent le rattachement ASUS : leur passage par ce réseau n’est pas démontré.

Aucune date TipKit `ZLASTDISPLAYED` contrôlée ne tombe le 17. Les transactions ne prouvent pas que Messages ou Téléphone aient été affichés. Des magasins distincts peuvent être copiés ensemble ou partager une horloge erronée ; ils ne constituent pas des étalons indépendants.

### 5.2. Santé : mesures, créations et identité

La sélection par **début d’intervalle** compte **73 échantillons** : **60 d’énergie de repos, cinq d’énergie active, quatre de pas et quatre de distance**. Ils sont répartis sur les 16, 17, 27 et 28 ; aucun début de pas ou distance ne tombe le 17 dans cette sélection. L’énergie Santé concerne le corps, pas la batterie du téléphone.

Le filtre distinct par **création d’objet** retrouve **27 créations le 17** : 24 repos, le couple pas/distance du 15 et l’énergie active. Un intervalle débutant le 17 à 17:15:27 n’est créé que le **28 à 11:57:22**. Un autre lot de 24 intervalles des 27–28 est créé le **28 à 12:01:56**. Les dates des mesures ne sont donc pas systématiquement des écritures contemporaines.

Les quatre couples pas/distance du 28 commencent à **12:01:32, 15:11:20, 17:24:02 et 17:39:47**, avec créations différées. Un transport de l’appareil sans déverrouillage est compatible. Un intervalle d’énergie commence aussi à 19:18:05 mais finit et est créé après 19:20 : sa sélection ne place pas toute l’opération avant restitution.

Les 73 lignes partagent une provenance `iPhone14,4`, build `21G93`, source **17.6.1**, `local_device=1`, `sync_identity=2`, Europe/Paris. L’identité Santé correspond exactement à `healthd/SyncIdentityHardwareIdentifier` ; les **59 951 échantillons conservés** partagent cette identité. Le `localIdentifier` matériel est vide. **L’identité logique est rattachée à l’installation sauvegardée, sans liaison infalsifiable à la série de TP-02 en octobre.**

La source 17.6.1 est créée le **3 septembre à 06:51:32 Paris**, environ 37 secondes avant la migration Photos correspondante. Des préférences Santé héritées de 2018 et des tables actuelles de synchronisation vides limitent l’interprétation : aucune synchronisation passée n’est datée ou exclue par leur seul état.

### 5.3. Restauration et continuité Photos

Une **restauration iCloud le 11 juin 2024 à 14:00:31 Paris** est conservée dans MobileBackup, avec `WasCloudRestore=true`, progression terminée et builds `21F90`. Elle précède octobre et ne peut pas, à elle seule, expliquer le transport d’événements encore futurs. Aucune restauration postérieure au 17 expliquant positivement la séquence n’est identifiée ; les préférences d’instantané ne suffisent pas à l’exclure.

Les **sept migrations Photos** et les sept dictionnaires de leur journal PLJ portent l’**UDID TP-02 exact**, modèle `D16AP`, avec le même UUID de bibliothèque actuel. Elles vont du **11 juin 2024 au 25 mai 2025** ; celles du **3 septembre** et du **6 décembre 2024** encadrent octobre. Les représentations SQL et PLJ sont des miroirs d’un même historique, pas deux acquisitions indépendantes.

Les changements de build sont compatibles avec des migrations de schéma : **ils ne prouvent pas sept restaurations iOS**. Aucun autre UDID n’est enregistré dans cette lignée. Cela défavorise une migration inter-appareils inscrite par cette bibliothèque, sans exclure copie ou restauration du même appareil.

Un sous-état Setup Assistant garde `hardwareModel=D79AP`, différent du modèle courant, et une sortie au **6 décembre à 11:00:19**. Cet héritage est réel mais ne date pas son transport ; la sortie n’est pas une restauration démontrée. Les identifiants de sauvegarde, bibliothèque et Santé n’ont pas la même portée.

**La continuité d’une lignée Photos historiquement liée à TP-02 est étayée ; celle de toute l’installation physique, ininterrompue depuis octobre, ne l’est pas.** Une copie logique de Photos vers une base en mémoire conserve les transactions du 17 sans réexécution. Ce contrôle valide leur transportabilité, pas une restauration iOS expérimentale ni une réplication systématique de tout l’historique par simple synchronisation d’objets.

## 6. Wi-Fi ASUS_Z01RD : chaîne conservée et limites d’attribution

### 6.1. Propriétés et chronologie des deux fichiers

Deux préférences déchiffrées contiennent les propriétés correspondantes :

| Fichier | SHA-256 du contenu déchiffré |
|---|---|
| `com.apple.wifi.known-networks.plist` | `d32e9c13df0276375a6301cbae85b6e452c6e67081f78e39b23db37015318f82` |
| `SystemConfiguration/com.apple.wifi-private-mac-networks.plist` | `3d066811eea6285c3a70002743082d3b07d228df1b3d685588749b7db9c36454` |

Les empreintes claires et chiffrées concordent avec les extractions ; les lectures ne modifient pas les contenus.

| Champ | Date et heure de Paris | Nature |
|---|---|---|
| `MacGenerationTimeStamp` | **17/10 17:25:47.630860** | Génération de MAC privée conservée |
| `JoinedByUserAt` | **17/10 17:25:48.147446** | Propriété étiquetée connexion utilisateur |
| `AddedAt` / `addedAt` | **17/10 17:25:48.153697**, identique dans les deux fichiers | Ajout conservé |
| `WiFiNetworkPasswordModificationDate` | **17/10 17:25:48.196428** | État associé au secret réseau, sans valeur de mot de passe reproduite |
| `FirstJoinWithNewMacTimestamp` | **17/10 17:25:52.303180** | Première association enregistrée dans cet état |
| `LastDiscoveredAt` | **28/10 12:01:49.687669** | Découverte conservée |
| `LastAssociatedAt`, premier BSS | **28/10 12:31:21.663303** | Association conservée |
| `LastAssociatedAt`, autre BSS | **28/10 14:32:37.808218** | Autre association conservée |
| `JoinedBySystemAt` | **28/10 14:32:37.808282** | Rattachement système |
| `lastJoined` | **28/10 14:32:38.847545** | État cohérent de rattachement |

L’entrée porte **`AddReason="WiFi Settings"`**, WPA2 Personal, réseau non caché/non captif, présence dans les réseaux connus et au moins une association privée déclarée réussie. Les codes privés non documentés ne sont pas convertis en gestes, volumes ou durées.

Les doubles temporels natifs et leurs octets sont contrôlés : **une confusion d’époque Apple/Unix ou de fuseau n’explique pas les dates du 17**. Une horloge source fausse reste une question distincte.

### 6.2. Action locale, synchronisation et état restauré

La génération de MAC et le premier rattachement sont séparés de **4,672320 s**. La raison WiFi Settings, l’ordre des propriétés et l’ajout identique dans les deux structures appuient une configuration puis association sur l’installation source. Ces propriétés liées ne sont toutefois pas autant de témoins indépendants.

La comparaison des **36 réseaux** fournit des contre-épreuves :

| Raison d’ajout | Réseaux | Date de génération MAC présente | Date de première association présente |
|---|---:|---:|---:|
| WiFi Settings | 25 | 25 | 24 |
| Cloud Sync | 3 | 0 | 0 |
| System App | 4 | 4 | 4 |
| WiFi Password Sharing | 3 | 3 | 3 |
| 3rd Party App | 1 | 1 | 1 |

Un réseau `Cloud Sync` conserve un **`JoinedByUserAt` du 15 avril**, antérieur à son **ajout du 11 juin**. **Une date utilisateur peut donc être conservée dans un état ajouté plus tard** ; sa seule présence ne démontre pas un geste local sur le matériel examiné.

Aucun des trois profils Cloud Sync ne fournit cependant une chaîne privée complète comparable à ASUS. Le simple import de mot de passe n’explique donc pas seul tous les champs observés. À l’inverse, un profil `System App` présente une chaîne courte de **6,910436 s** : la brièveté n’est pas exclusive à une connexion manuelle.

Sur 32 couples datés, **22 ont une première association antérieure à leur génération de MAC courante**, dont quinze écarts proches de quatorze jours. Les champs sont évolutifs ; une rotation est compatible et il serait erroné d’identifier systématiquement chaque date au premier usage de la MAC actuellement stockée.

| Hypothèse | Éléments compatibles | Limite |
|---|---|---|
| Configuration/association sur TP-02 le 17 | WiFi Settings, chaîne de 4,7 s, traitements voisins, lignée liée à l’UDID | Aucun journal radio contemporain ou liaison historique MAC/série. |
| Simple import d’un mot de passe | Synchronisation possible ; transport d’une date utilisateur observé ailleurs | Insuffisant à expliquer seul toute la chaîne privée. |
| Import/restauration d’un état complet | Historiques transportables et héritage de restauration | Aucun transfert postérieur explicatif identifié ; comportement exact des champs privés non reproduit. |
| Traitement automatique ou profil | Auto-association possible | Aucun profil ASUS ou déclencheur spécifique démontré. |

**La chaîne est plus informative que le libellé `JoinedByUserAt` seul, sans permettre de trancher avec certitude entre action sur TP-02 et import d’un état complet produit ailleurs.** Les mécanismes documentés de trousseau ou sauvegarde ne garantissent pas le transport de chaque propriété privée. Les tests sur appareils témoins restent non réalisés.

### 6.3. Points d’accès du 28 et états ultérieurs

Les deux BSSID **`22:B0:A5:94:1F:AF`** et **`32:0D:CA:FD:68:8C`**, canaux **36 et 6**, partagent une signature IPv4 de routeur et un serveur DHCP. Le BSSID privé rejoint celui du canal 6 après normalisation des six octets. Les deux adresses sont administrées localement ; leur préfixe ne permet pas d’identifier valablement un fabricant.

Ces propriétés sont compatibles avec un même environnement logique, deux bandes ou un hotspot, **sans prouver un boîtier unique ni le point d’accès physique du 17**. Aucun BSSID figé séparément à cette dernière date n’est conservé. Les mises à jour ultérieures des préférences montrent qu’elles ne sont pas un instantané immuable d’octobre.

Le `LinkDownTimestamp` est le **28 à 19:40:02**, après la clôture/récupération déclarée. Un appel à **19:39:46** et des dates de caches LSC vers **22:35 et 23:26** sont également postérieurs. Ces états ne prouvent ni poursuite d’une intervention administrative ni consultation de caméra.

Aucune troisième source d’association indépendante n’est retrouvée : DataUsage n’a pas de couverture d’octobre et la copie Wi-Fi historique de 69 réseaux conserve des dates de 2017–2020, sans ASUS. Le SSID reste modifiable et copiable : **il ne désigne ni un propriétaire, ni un lieu, ni OP-01**.

## 7. Communications

### 7.1. Historique d’appels

`CallHistory.storedata` contient **1 662 lignes**, dont **53** dans la fenêtre principale, du **15 octobre à 18:50:48.115369 au 26 octobre à 17:14:34.075273 Paris**. Le même ensemble est retrouvé par le contrôle avant ouverture.

| Jour | Appels conservés dans la fenêtre | Dont marqués sortants |
|---|---:|---:|
| 15/10 | 14 | 8 |
| 17/10 | 1 | 0 |
| 18/10 | 4 | 0 |
| 19/10 | 1 | 1 |
| 20/10 | 2 | 0 |
| 21/10 | 5 | 2 |
| 22/10 | 9 | 1 |
| 23/10 | 5 | 3 |
| 24/10 | 1 | 1 |
| 25/10 | 7 | 4 |
| 26/10 | 4 | 2 |
| **Total** | **53** | **22** |

Les 22 sortants se répartissent sur huit jours ; **19 ont une durée positive**. Les quinze lignes `ZANSWERED=1` sont toutes entrantes. Une valeur zéro pour les sortants ne signifie donc pas automatiquement un échec et aucun taux de communications abouties n’en est déduit.

Les 53 lignes désignent `com.apple.Telephony` et possèdent un `ZUNIQUE_ID` distinct, mais **aucun participant local UUID, initiateur ou identifiant de provenance matérielle discriminant**. D’autres lignes ont des UUID, sans jointure établissant ici la série de l’appareil ayant porté l’appel. Le schéma ne donne pas de date d’arrivée/importation par appel.

Les historiques Téléphone/FaceTime peuvent être synchronisés ou restaurés. Cette possibilité n’établit pas que ces appels l’ont été ; elle empêche leur attribution automatique à TP-02. **Les valeurs ne départagent pas production locale, synchronisation ou restauration.** Une comparaison d’acquisitions et des relevés opérateur avec IMEI/IMSI seraient plus discriminants qu’un relevé de ligne seul.

### 7.2. Trois SMS du 28 avec horodatages de lecture

| ROWID | Date du message, Paris | `date_read`, Paris | Nature indiquée par le corps |
|---|---|---|---|
| **74688** | **12:03:14.750877** | **12:03:18.794336** | Code de réinitialisation de mot de passe Microsoft |
| **74689** | **12:10:04.455465** | **12:10:06.276798** | Code de validation Google |
| **74690** | **12:46:03.902439** | **12:46:06.075801** | Code de validation Google |

Les corps `attributedBody` sont contrôlés sans reproduire les codes. Les marques sont celles du texte, sans authentification de l’émetteur. **Ni demandeur, ni utilisation des codes, ni réussite d’une connexion ou réinitialisation ne sont établis.** Aucun de ces trois corps n’est un code Apple.

Les dates de lecture sont distinctes et suivent la réception d’environ **4,043 s, 1,821 s et 2,173 s**. Les lignes portent `is_read=1`, `is_finished=1`, `is_delivered=1`, `date_delivered=0` et `ck_sync_state=1`. Le dernier champ ne date pas une synchronisation. Les dates `date_read` sont différentes du seul état actuel `is_read` ; pour ces SMS entrants, elles ne sont pas des accusés de lecture SMS adressés au correspondant.

Une préférence clavier à **12:03:18.492020**, environ 302 ms avant le premier `date_read`, ne contient pas le texte saisi. Les essais de liaison n’établissent pas sa relation avec les messages. Aucun mécanisme validé ne montre ici qu’une simple notification remplit automatiquement `date_read`, ni que l’absence de notification dans un champ actuel exclut une notification historique.

**Les dates de lecture sont vérifiées ; trois lectures humaines locales sur TP-02 ne le sont pas.** Marquage dans une application, autre appareil et état synchronisé/restauré restent à départager ; aucune session de transport explicative n’est positivement identifiée. Tous les horaires sont après l’ouverture à 11:30. Le contrôle avant ouverture ne sélectionne aucun SMS natif par date de message, lecture ou livraison.

### 7.3. WhatsApp

Les deux bases WhatsApp contrôlées sont SQLite et donnent `quick_check=ok`. **97 442 messages** sont conservés, sans `ZMESSAGEDATE` dans la fenêtre principale. Le dernier précédent est sortant le **15 à 13:16:55.308172** ; le premier suivant est entrant le **29 à 00:56:41**. Aucun candidat central n’est retenu dans les colonnes examinées de ces deux bases.

Ce résultat est compatible avec une interruption de cette instance de messagerie, sans preuve d’absence d’ouverture, de messages supprimés, de session liée ou d’autre état restauré. Les trente actifs Photos attribués à WhatsApp pendant la fenêtre ne sont pas assimilés aux messages de cette base ou à un usage local démontré.

## 8. Photothèque, transactions et suppressions

### 8.1. Dates conservées et origines des médias

Photos contient **19 516 actifs** et satisfait `quick_check=ok`.

| Champ dans la fenêtre principale | Lignes | Portée |
|---|---:|---|
| Création `ZDATECREATED` | **87** | Date déclarée de l’actif, pas nécessairement prise de vue locale. |
| Ajout `ZADDEDDATE` | **85** | Ajout de bibliothèque, pas nécessairement arrivée physique actuelle. |
| Modification `ZMODIFICATIONDATE` | **5 958** | Modification de donnée ou d’état, pas nécessairement retouche. |
| Ajustement `ZADJUSTMENTTIMESTAMP` | **6** | Nature et origine à établir. |
| Dernière vue `ZLASTVIEWEDDATE` | **5 154** | Origine et causes de mise à jour non validées comme consultations humaines. |
| Corbeille `ZTRASHEDDATE` | **0** | Pas de date conservée, sans preuve d’absence de suppression. |

Ces champs ne s’additionnent pas en gestes indépendants. **3 123 modifications** sont groupées le **27 à 02:44–02:45 +02:00**, avant le changement d’heure. Traitement de bibliothèque, maintenance ou synchronisation sont possibles, sans cause établie. Les 5 958 modifications et les 85 ajouts ont actuellement un identifiant cloud, sans preuve de la cause de chaque changement.

Les 87 créations ont des origines d’import déclarées **SpringBoard pour 50, WhatsApp pour 30, TikTok pour trois**, non renseignées pour quatre. Trente-trois médias sont retrouvés par nom/UUID, **32 JPEG et un HEIC** ; **19 déclarent un iPhone 8 dans leurs EXIF** et quatorze n’ont pas de modèle. Ce contre-exemple interdit d’attribuer automatiquement les photos à la caméra de TP-02. Les EXIF restent modifiables et ne désignent pas un exemplaire ou un utilisateur.

### 8.2. Traitements techniques et séquence compatible avec une capture

L’historique Photos conserve **345 transactions centrales : deux le 17 et 343 le 28**. Sur celles du 28, **277 contextes `mediaanalysisd-service` et 42 `photoanalysisd`**, soit 319, soutiennent des traitements automatiques. Une transaction est un ensemble de changements persistants, pas un geste.

| Heure du 28, Paris | Localisateur et constat | Portée |
|---|---|---|
| **13:36:10.800948** | Transaction **117456**, SpringBoard, insertions compatibles sur **Asset 23769** | Création d’un élément dans la bibliothèque source. |
| **13:36:14.432556** | Transaction **117461**, ScreenshotServicesService, mise à jour du même actif | **Séquence compatible avec le traitement d’une capture d’écran**, plus informative qu’une origine d’import isolée. |
| **17:31:44.885448** | Transaction **117587**, recette de miniature, **Asset 23729 / InternalResource 85746** | Génération de ressource pour `IMG_1773.MP4`, pas visionnage démontré. |
| **17:31:58.026875 et 17:32:00.403479** | Transactions **117588–117589**, requêtes attribuées à Photos sur un autre actif | Client Photos identifié, sans premier plan ou consultation d’une image précise établis. |

Le fichier miniature et la transaction interne sont liés techniquement. La vidéo est déclarée créée le 14 octobre et importée depuis Instagram ; son état actuel de dernière vue est postérieur à la fenêtre. Le rappel CPL de 17:31:38 précède la miniature sans causalité démontrée.

**La séquence SpringBoard/ScreenshotServices soutient une activité d’interface compatible avec une intervention sur l’appareil source de l’historique.** Elle se situe après ouverture, ne fournit ni journal tactile ni auteur, et ne certifie pas le matériel d’exécution de 2024. Une restauration complète peut transporter ces transactions ; une simple synchronisation d’objets ne doit pas être supposée transporter toutes les tables historiques.

### 8.3. Disparition de l’actif et recherches de récupération

L’actif **23769** est absent de `ZASSET` actuel, mais son historique conserve un traitement cloud le **29 octobre à 10:05:52** et une purge de maintenance le **29 novembre à 02:21:38**, transaction **124593**. Cette purge ne date pas un geste initial de mise à la corbeille ni son motif.

Une propriété `ZTOMBSTONE3` convertible au **29 octobre à 08:46:45.776** reste de sémantique non validée ; **elle n’est pas retenue comme date certaine de suppression**. Ces valeurs sont hors de la rétention déclarée.

La recherche ciblée de l’UUID dans les zones inutilisées/freeblocks de **28 606 pages** de trois tables Photos et dans les chemins du manifeste ne récupère ni image ni ancien enregistrement supplémentaire. Le contrôle couvre **2 390 389 octets non alloués et 3 463 octets de payload freeblock**, sans couvrir toute la base ou les secteurs physiques. **L’image de la possible capture d’écran n’est pas récupérée.**

### 8.4. Marqueurs de retrait interne SEGB

Les **24 flux SEGB** examinés contiennent **14 618 enveloppes** : **9 507 enregistrements écrits à CRC valide** et **5 111 états supprimés à payload nul**. Les **47 métadonnées centrales** sont toutes du 28 ; elles comprennent vingt états sans contenu et **27 marqueurs de retrait interne** datés de **15:50:24.854333–.869329**, libellés `parsecd`.

Ces marqueurs concernent des références d’index, compatibles avec de l’entretien interne après ouverture. Le contenu actuel d’un slot ne peut pas être assimilé automatiquement à son ancien occupant. **Ni suppression de fichiers utilisateur, ni geste humain, ni dissimulation ne sont démontrés ; aucun contenu original supprimé n’est reconstitué.** Le CRC valide le payload conservé, pas sa date historique ou son matériel producteur.

## 9. WidgetKit : états de verrouillage et référentiels temporels

Le diagnostic `WidgetKitExtension-2024-10-28-122629.ips` décrit l’extension **Google News**, pas une ouverture de l’application démontrée. Son contenu déchiffré, inchangé aux contrôles, a pour SHA-256 :

```text
a6da7e464e750a2961b3c315458f39be5abaf8966cb865ac014ea6b6f3a89ed0
```

| Champ | Valeur conservée |
|---|---|
| `procLaunch` | **17/10/2024 17:15:46.8308 +02:00** |
| `captureTime` | **28/10/2024 12:26:28.7192 +01:00** |
| `uptime` | **2 500 secondes**, présenté comme temps d’éveil depuis le démarrage |
| `procStartAbsTime` / `procExitAbsTime` | **18 054 155 057 / 60 303 998 486** |
| `wasUnlockedSinceBoot` / `isLocked` | **1 / 1** |
| Modèle / système | `iPhone14,4`, **17.6.1**, build `21G93` |

Les indicateurs sont compatibles avec un appareil verrouillé à la capture et un déverrouillage antérieur dans la session, **sans horaire de déverrouillage**. Le diagnostic ne contient ni série ni UDID individuel. Sa clé appartient à un ensemble de diagnostics cohérent avec la restauration de juin, sans jointure formelle à la série ou à la lignée Photos.

L’écart des dates civiles est de **936 641,8884 s**, environ 10,84 jours. Sous un modèle de ticks proche de **24 MHz**, la différence des compteurs représente **1 760,410143 s de temps système éveillé**, pas du temps CPU propre à l’extension. Les **312 diagnostics** étudiés sont compatibles avec ce modèle et une présentation d’uptime tronquée ; la fraction matérielle exacte n’est pas disponible dans la preuve.

Apple distingue les compteurs incluant ou excluant le sommeil système. Le raccord du champ IPS à un compteur excluant le sommeil est une **inférence étayée**, pas une API interne explicitement nommée dans sa définition publique. Sommeil système, écran éteint et verrouillage sont des états différents.

| Explication possible | Portée |
|---|---|
| Sommeil système prolongé, processus conservé | Peut dissocier calendrier et compteur ; environ 934 881 s seraient nécessaires sous le modèle retenu, sans sommeil mesuré. |
| Date civile erronée puis corrigée | Compatible, mais aucun saut d’horloge contemporain validé n’est retrouvé. |
| Suspension de la seule extension | Ne suffit pas à expliquer l’écart sur un système continuellement éveillé. |
| Copie du diagnostic | Peut conserver ses dates et limiter l’attribution matérielle, sans expliquer seule la divergence interne des compteurs. |

Le changement d’heure est déjà pris en compte. Les préférences actuelles d’horloge ne certifient pas celles de 2024. **Aucun sommeil prolongé ni correction civile n’est prouvé. Soustraire 2 500 s à 12:26 ne démontre pas un démarrage vers 11:45 ou un téléphone éteint avant ouverture.**

WidgetKit ne confirme ni ne réfute la date civile de la chaîne Wi-Fi. Il ne permet pas de la déplacer arbitrairement et ne constitue pas une preuve matérielle indépendante de fonctionnement de TP-02 le 17.

## 10. Applications caméra et états réseau

### 10.1. LSC Smart Connect : formats et panneau du 28

Le domaine LSC contient une base WebKit réellement SQLite, un fichier `health_data_center.db` vide et **cinq APM sans signature SQLite**, de 196 608 à 1 048 576 octets. Leur forte entropie ne démontre pas à elle seule un chiffrement supplémentaire ; ils restent de format non décodé. Les versions ou dates apparentes de leurs noms ne sont pas converties en événements d’utilisation ou firmware installé.

Le cache de panneau **`0000000432_2.51.0`** porte une date au **28 octobre à 17:39:17.525519 Paris**. Les métadonnées de **485 ressources**, soit 1 455 champs associés, concordent autour de cet instant. Ces champs décrivent un même ensemble de cache, pas autant d’observations indépendantes.

Le code disponible contient des capacités de caméra IP/P2P, connexion de flux et prévisualisation. **La présence du code ne prouve pas son exécution.** Constitution ou mise à jour de ressources, téléchargement, préchargement et affichage de panneau sont compatibles ; aucun événement runtime de première image, flux connecté ou durée de session ne démontre une consultation de caméra. La constante « 600 » d’un chemin de code n’est pas une durée observée.

Les catalogues LSC livrent **18 références de médias**, réparties sur deux identifiants d’équipement et des dates discontinues de **2023 à 2025**, aucune de février 2024 ou du 15 au 28 octobre. Ces références ne sont pas un historique exhaustif d’enregistrements ou de visionnages.

Les caches `home/detailv1` et `home/list313` restent non décodés. Les ressources de panneaux décodables contiennent des traductions ; leurs versions ne déterminent pas le modèle exact ou le firmware des caméras. **Aucun historique complet de partages, comptes invités, réappairages ou changements de compte depuis mars 2023 n’est reconstitué.**

### 10.2. Xiaomi Home et rapprochements Freebox

Les deux domaines Xiaomi comprennent **48 bases à signature SQLite**. Les configurations mentionnent **`mxiang.camera.mwc11`**, **`mxiang.camera.mwc10`** et **`yeelink.light.nl1`**. Elles n’établissent pas un historique d’accès.

Les six tables d’alarmes contrôlées, plusieurs tables de cache/événements et les valeurs `ZLASTONLINE=0` ne prouvent pas l’absence d’accès : leur rétention et leur rôle exact ne fournissent pas un journal complet de 2024. Une date de configuration partagée le **28 à 17:40:50** ne caractérise pas une commande de caméra.

Le modèle **mwc11** a une correspondance MAC exacte avec une entrée Freebox ; le rapprochement **mwc10** est partiel, avec des MAC différentes malgré une IP et un nom cohérents. Ces résultats ne rattachent pas une caméra physique à une carte SD déterminée et ne démontrent pas une consultation distante.

Deux MAC clientes des préférences TP-02 correspondent à la Freebox. Les trois identités iPhone nocturnes des **16–17 octobre** n’ont pas de correspondance parmi les états disponibles ; rotation des MAC et historique incomplet empêchent de les exclure matériellement de TP-02 sur ce seul constat.

### 10.3. Dates WebKit et signalements sur les cartes

Les tables `OperatingDates` utilisent des **mois de zéro à onze** et des jours UTC sans heure. Après conversion, Xiaomi conserve les jours **15 et 28 octobre**, LSC le **28**, sans jour du 15 au 27 dans ce magasin. L’initialisation du magasin peut produire une date ; **ces lignes ne sont pas des registres de consultation humaine ou de vidéo caméra** et ne se placent pas précisément avant/après les heures de procédure.

La cliente rapporte une réinitialisation de la **chambre en février 2024** et un fonctionnement continu de la terrasse. Les cartes SD établissent séparément des anomalies et lacunes, sans reset usine ou effacement malveillant démontré. Aucun identifiant, commande ou flux ne rattache une action d’un téléphone pendant la fermeture des scellés à ces défauts. Les caméras n’étaient pas scellées.

## 11. Connexions à un ordinateur et contrôles intersupports

### 11.1. Appairage, extraction, profils et autres traces d’usage

Aucun artefact contrôlé n’identifie une connexion USB, un appairage ordinateur ou une session d’extraction d’octobre 2024 pour TP-02. La présence de la sauvegarde Mac n’en date pas une pendant la rétention. Les noms `LockdownMode`, `LockdownParameters`, ressources « pairing » ou `knowledgeconstructiond` ne constituent pas à eux seuls une preuve d’appairage ou une base d’activité recherchée.

Les recherches de noms d’outils d’extraction ou télécommande ne donnent pas de session identifiée. Deux `ProfileTruth` sont vides et `IsSupervised=false` dans l’état conservé, sans historique complet des profils ou comptes depuis 2021. Ces résultats ne couvrent pas tous les logiciels inconnus, renommés, supprimés ou exclus de la sauvegarde.

Les contrôles d’usage, alimentation et localisation ne fournissent ni écran au premier plan, ni démarrage, charge ou déverrouillage daté pendant la rétention, ni lieu ou session radio matériellement attribué. InteractionC est vide, les états FrontBoard/Siri/AppSwitcher sont partiels ou sans chronologie validée. Les FirstUnlock et BootTime exploitables sont hors fenêtre. Les magasins de localisation pertinents sont vides ou de dates différentes ; aucune localisation n’est déduite du SSID ou d’une IP.

Trois lignes cloud Dictaphone au **28 à 10:17:31** ne prouvent pas trois enregistrements locaux avant ouverture. Des traitements de doublons Contacts à **15:08:48** ne prouvent pas une consultation. Ces exemples illustrent la distinction entre donnée de contenu, traitement interne et geste humain.

### 11.2. ASUS_Z01RD sur OP-01

Le fichier d’échange Windows d’OP-01 contient **cinq occurrences ASCII exactes de `ASUS_Z01RD`**. Les pages reconstruites et leurs champs soutiennent fortement une origine dans des **listes de réseaux Wi-Fi disponibles**. Certaines sont des copies du même contenu : cinq occurrences ne désignent pas cinq détections ou connexions.

**Le même nom existe dans les deux acquisitions**, mais aucun fragment du PC n’est daté. Les événements/profils WLAN contrôlés ne démontrent ni connexion d’OP-01 à ASUS, ni émission du réseau par ce PC, ni présence commune avec TP-02 le 17.

Les recherches négatives dans les exports et les **1 325 enveloppes d’événements WLAN validées** du fichier actif portent sur des sources différentes du fichier d’échange. Elles ne fournissent pas une couverture continue de tous les usages. Le contrôle binaire n’est pas un décodage sémantique exhaustif de BinXML.

Le SSID ne désigne donc ni un point d’accès unique, ni un propriétaire ou opérateur. La correspondance nominale est une piste de rapprochement, pas une attribution physique.

### 11.3. Autres téléphones, PDF et relation de confiance

Les **27 PDF Mini de L16B représentent vingt contenus distincts**, tous identiques par SHA-256 dans **TP-02 et TP-03**. Ils ne départagent ni le Mini source ni les scellés, ni le sens ou la date du transfert. Leur présence locale ne certifie pas leur inclusion dans le jeu définitivement saisi, distinct du dossier informatif L16B.

Le fichier d’appairage Apple ancien d’OP-01 désigne l’UDID exact de **TP-03**, pas TP-02, avec métadonnées de 2022/2023. Il ne date aucun branchement des Mini en octobre 2024.

TP-01 n’a pas de faisceau local comparable dans les sources examinées. TP-03 conserve une séquence distincte le **16 à 05:31**, compatible avec des traitements internes récurrents. **Ces résultats ne sont pas transférés à TP-02 et ne constituent pas des preuves d’un même événement physique.**

## 12. Limites, hypothèses et conclusion technique

### 12.1. Ce que les données ne permettent pas de certifier

La sauvegarde de 2026 manque de journal Mac, options d’acquisition, historique complet de restauration et contrôle indépendant de la copie initiale. Les dates de tête et tailles MBFile comportent des discordances conservées. La présence des objets et leur cohérence avec les dérivés ne garantissent ni exhaustivité historique ni authenticité des événements de 2024.

Les appels n’ont pas d’ancrage matériel discriminant ; des médias déclarent un iPhone 8 ; les identités Santé et Photos peuvent être conservées lors de copies. La lignée Photos rattachée à l’UDID renforce la provenance sans démontrer une installation physique ininterrompue. L’absence de migration ou synchronisation explicative identifiée ne les exclut pas.

Les dates partagent potentiellement la même horloge source. WidgetKit ne la calibre pas. Les heures individuelles de fermeture et de restitution restent inconnues. Une trace du 28 après 11:30 ne démontre pas une manipulation antérieure à l’ouverture.

Les recherches restent sélectives : **3 945 fichiers déchiffrés sur 137 844 ordinaires** ; BLOB, formats propriétaires, tables nécessitant des extensions et candidats résiduels ne sont pas tous interprétés. Aucun carving physique ou récupération générale des secteurs supprimés n’est réalisé. La recherche interne SQLite est ciblée et ne récupère pas l’image de la possible capture.

### 12.2. État d’alimentation et observation rapportée

Le prestataire rapporte que les vidéos du salon montrent une agente rallumant les téléphones le **15 octobre vers 13:25**, avant scellement ; la cliente situait ce geste vers 13:30 ou un peu avant. Le [rapport final](../RAPPORT-FINAL-SADEDINE-2026.md#12-téléphones-rallumés-avant-leur-mise-sous-scellés) distingue ce récit des seuls aperçus d’un clip commençant à 13:28. Aucun nouveau visionnage indépendant n’est revendiqué dans ce rapport.

Le récit rend compatible un fonctionnement automatique ultérieur, sans prouver l’état à la fermeture ou une continuité d’alimentation jusqu’au 28. Si une extinction à la fermeture était établie, une production locale ultérieure supposerait une reprise à expliquer ou une autre origine des traces. Ni le diagnostic WidgetKit ni le PV de déverrouillage ne prouvent un démarrage au moment de l’ouverture.

### 12.3. Éléments discriminants encore nécessaires

| Question | Pièce ou contrôle utile |
|---|---|
| Les états du 17 existaient-ils déjà sur TP-02 à cette époque ? | Acquisition contemporaine attribuée au matériel ; comparaison d’anciennes sauvegardes et autres appareils du compte. |
| Quel appareil s’est associé au réseau ASUS ? | Journal indépendant du point d’accès, BSSID et MAC cliente historiquement rattachée à TP-02 ; identité du point d’accès indépendante du SSID. |
| Les historiques ont-ils été restaurés ? | Journal Mac, historique de migrations/restaurations et documents de conservation/alimentation. |
| Quelle est l’origine physique des appels ? | Relevés opérateur avec IMEI/IMSI si disponibles, identifiants d’appels comparés entre acquisitions et traces radio contemporaines. |
| Que signifient exactement les champs privés Wi-Fi et les dates de lecture ? | Expériences distinctes sur témoins de version pertinente : connexion manuelle, synchronisation, partage, migration et restauration ; aucune expérimentation sur les pièces. |
| Les horloges étaient-elles exactes ? | Historique de correction ou observation contemporaine des compteurs et du calendrier, liée au matériel et à une référence indépendante. |

La disponibilité de ces éléments n’est pas présumée. Les historiques de comptes et caméras doivent provenir de sources autorisées et réellement conservées ; les états locaux ne les remplacent pas.

### 12.4. Conclusion

**Les traces du 17 soutiennent des traitements de plusieurs services puis une configuration/association Wi-Fi sur l’installation source. Le faisceau Wi-Fi est plus précis qu’un simple nom de réseau ou une date utilisateur isolée. Il justifie de vérifier une intervention possible avant ouverture, sans certifier son origine physique sur TP-02 ni un geste humain.** Les 53 appels renforcent la question de l’origine des communications, sans l’établir.

Après ouverture le 28, les SMS avec dates de lecture, la séquence compatible avec une capture d’écran, les associations Wi-Fi et les travaux Photos/LSC sont établis dans les données. **La possible capture n’est pas récupérée ; les codes SMS ne sont pas démontrés utilisés et aucune consultation de caméra n’est attestée.** Les marqueurs de retrait interne ne prouvent pas un effacement volontaire de preuves.

Aucun auteur, déverrouillage daté sous scellé, extraction d’octobre ou rupture matérielle de scellé n’est identifié. Les pistes de transport d’historique, de fonctionnement automatique et d’horloge restent ouvertes, sans en choisir une comme fait certain. La sauvegarde ne permet ni d’affirmer une utilisation humaine sous scellé ni de certifier une inactivité complète.

## 13. Pièces techniques et termes de lecture

### 13.1. Sources de contrôle

| Domaine | Pièces de référence |
|---|---|
| Identification et présence | [En-têtes](recherche-TP-02/identification-sauvegarde.json), [objets source](recherche-TP-02/presence-objets-source.json) |
| Déchiffrement et cohérence | [Contrôle complet](recherche-TP-02/coherence-complete-20261014.json), [tailles et en-têtes](recherche-TP-02/approfondissement-activite-202410/backup-details.json), [étude de cohérence](recherche-TP-02/approfondissement-activite-202410/backup-consistency.md) |
| Extraction et couverture | [Synthèse des sélections](recherche-TP-02/resultats-finaux-20261014/summary.json), [vérification principale](recherche-TP-02/verification-complete-20261014.json), [contrôles système complémentaires](recherche-TP-02/investigation-systeme-oct2024/new-source-verification.json) |
| Communications | [Origine des appels](recherche-TP-02/approfondissement-activite-202410/calls-analysis.md), [valeurs et distributions](recherche-TP-02/approfondissement-activite-202410/calls-details.json), [nature et lecture des SMS](../investigations/20261109-sms-lecture/compte-rendu.md), [fenêtre WhatsApp](recherche-TP-02/whatsapp-window-assessment.json) |
| Santé et lignée | [Santé](recherche-TP-02/approfondissement-activite-202410/health-analysis.md), [identité healthd](recherche-TP-02/approfondissement-activite-202410/health-identity-crosschecks.json), [continuité iOS](recherche-TP-02/investigation-wifi-17oct2024/continuite-ios.md), [Photos et journal PLJ](recherche-TP-02/investigation-wifi-17oct2024/photos-continuity-and-journal.json) |
| Wi-Fi du 17 | [Comparaison des réseaux](recherche-TP-02/investigation-wifi-17oct2024/comparaison-reseaux.csv), [dates binaires](recherche-TP-02/investigation-wifi-17oct2024/wifi-binary-date-validation.json), [champs évolutifs](recherche-TP-02/investigation-wifi-17oct2024/network-field-history-controls.json), [mécanismes et limites](recherche-TP-02/investigation-wifi-17oct2024/mecanismes-wifi-apple.md) |
| Photos, interface et suppressions | [Champs Photos](recherche-TP-02/approfondissement-final-20261014/photos-date-fields.csv), [transactions](recherche-TP-02/approfondissement-activite-202410/photos-transaction-correlations.json), [étude du 28](recherche-TP-02/approfondissement-activite-202410/october28-analysis.md), [récupération ciblée](recherche-TP-02/investigation-systeme-oct2024/recuperation-suppressions.md) |
| WidgetKit et horloges | [Lecture brute](recherche-TP-02/investigation-horloges-widgetkit/widgetkit-raw-analysis.md), [référentiels temporels](recherche-TP-02/investigation-horloges-widgetkit/apple-clock-semantics.md), [hypothèses](recherche-TP-02/investigation-horloges-widgetkit/hypotheses-contradictoires.md), [précision sur uptime](../investigations/20261109-documentation-uptime/note-technique.md) |
| Caméras et autres supports | [Code de panneau](recherche-TP-02/approfondissement-activite-202410/panel-code-details.json), [recoupements Freebox/caméras](../investigations/20261017-recroisements/compte-rendu.md), [historiques LSC](../investigations/20261019-retour-cliente/compte-rendu.md), [identification des modèles](../investigations/20261109-identification-cameras/compte-rendu.md) |
| ASUS sur OP-01 | [Recherche](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/compte-rendu.md), [origine des fragments](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/origine/interpretation.md), [limites de datation](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/datation.md) |
| Procédure et comparaison des téléphones | [Lecture du PV](../investigations/20261108-analyse-pv/compte-rendu.md), [rapprochements](../investigations/20261110-telephones/compte-rendu.md), [contrôles avant ouverture](../investigations/20261110-revue-intervention-scelles/compte-rendu.md) |
| Méthode et reproduction | [Notice principale](scripts/README-TP-02.md), [approfondissement](recherche-TP-02/approfondissement-activite-202410/methods-and-sources.md), [Wi-Fi](recherche-TP-02/investigation-wifi-17oct2024/methodes-et-reproduction.md), [système](recherche-TP-02/investigation-systeme-oct2024/methodes-et-reproduction.md), [horloges](recherche-TP-02/investigation-horloges-widgetkit/methodes-et-reproduction.md) |

Les chronologies conservent valeurs brutes, UTC/Paris, localisateurs, fileID, empreintes et limites. Leurs périmètres se recoupent : les lignes des différents exports ne s’additionnent pas en événements indépendants. Scripts, commandes, erreurs et manifestes sont conservés ; les destinations de reproduction doivent être distinctes des sources et résultats existants. Les médias et données sensibles sont exclus de Git ; le dépôt seul ne contient pas tous les clairs nécessaires au contrôle.

### 13.2. Termes techniques

| Terme | Sens dans ce rapport |
|---|---|
| Sauvegarde logique / MBFile | Fichiers retenus par iOS / métadonnées de leurs objets dans le manifeste ; pas une image de tous les secteurs. |
| UDID / UUID de bibliothèque | Identifiant déclaré de l’appareil / identifiant de lignée de données. Une copie peut conserver un historique sans le réexécuter. |
| SSID / BSSID / MAC privée | Nom du réseau / adresse du point d’accès / adresse cliente utilisée par l’iPhone. Ils ne sont pas interchangeables ni des identités de personne. |
| SQLite / WAL / `quick_check` | Base de données / journal de transactions / contrôle de cohérence. Un journal absent limite les états anciens récupérables. |
| ATRANSACTION / Core Data / CPL | Historique applicatif de changements / mécanisme de persistance / services de photothèque cloud. Une transaction n’est pas un geste. |
| TipKit / SEGB / tombstone | Conseils applicatifs / conteneur de flux système / marqueur de retrait interne. Leur présence ne prouve pas une suppression volontaire de document. |
| IPS / uptime | Diagnostic Apple / temps d’éveil présenté depuis le démarrage ; pas une heure de démarrage calculable sans autres éléments. |
| Synchronisation / restauration | Échange ou mise à jour d’objets / remise en place d’un état sauvegardé. Leur couverture et leurs effets sur les historiques diffèrent. |

### 13.3. Références de formats

Les références de formats et mécanismes utilisées dans les pièces techniques comprennent [l’époque Apple](https://developer.apple.com/documentation/foundation/date/timeintervalsincereferencedate-swift.property), [les transactions Core Data](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction), [le format des diagnostics Apple](https://developer.apple.com/documentation/xcode/interpreting-the-json-format-of-a-crash-report), [les compteurs Mach](https://developer.apple.com/documentation/driverkit/c-runtime-support), [les journaux SQLite](https://www.sqlite.org/wal.html) et [l’API de copie SQLite](https://www.sqlite.org/backup.html). Ces mécanismes généraux expliquent des possibilités ; ils ne sont pas des journaux d’opérations propres à TP-02.
