# Rapport d’analyse technique de l’ordinateur OP-01

**Affaire :** SADEDINE-2026

**Cliente :** Mme Malika Sadedine — DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev — christophe@donnat.dev

**Équipement :** ASUS UX333F NOTEBOOK PC — numéro de série `KAN0CV116290436`

## 1. Objet et périmètre

Ce rapport présente les constats techniques et les conclusions relatifs au fonctionnement d’OP-01 pendant sa rétention du **15 au 28 octobre 2024**, aux opérations sur ses fichiers, aux copies de données et aux indices éventuels de compromission antérieurs à la perquisition. La recherche remonte à 2021/2022 lorsque des traces sont encore conservées.

Il repose sur l’image du SSD, les artefacts Windows, les contenus présents ou récupérables et leur confrontation au procès-verbal de saisie. Les demandes de la cliente sont documentées dans les [mails de mission](../docs/mail.txt) et [complémentaires](../docs/mail-2.txt) ; l’identification du matériel figure dans l’[attestation de remise](../remise-documents/attestation-de-remise.md).

Les résultats distinguent ce qu’un artefact enregistre, l’interprétation permise par les recoupements et les questions qui restent ouvertes. Une date de fichier ne démontre pas à elle seule un allumage ; une session Windows ne désigne pas une personne ; un export présent localement ne démontre pas son transfert vers un tiers.

## 2. Synthèse des conclusions

**Les traces conservées sont cohérentes avec une hibernation d’OP-01 du 15 octobre vers 10 h 53 au 28 octobre vers 10 h 41, heure de Paris. Aucune reprise Windows intermédiaire corroborée n’est établie. L’utilisation du PC le 28 après l’ouverture consignée au procès-verbal est, en revanche, étayée par plusieurs familles d’artefacts.**

| Question | Conclusion technique | Portée et limite |
|---|---|---|
| OP-01 a-t-il fonctionné le 15 octobre ? | Reprise Windows vers **10:43**, puis passage en hibernation vers **10:53**, batterie à 2 %. | Ces événements précèdent la mise sous scellés consignée après 14:19. L’heure de début de la perquisition et l’opérateur ne sont pas établis. |
| A-t-il repris Windows avant l’ouverture du 28 ? | Aucune activité intermédiaire corroborée ; la reprise suivante conservée est à **10:41:56 le 28**. | L’absence de trace ne permet pas d’exclure une manipulation hors ligne, un démarrage externe ou une activité dont les traces ont disparu. |
| Le 16 octobre à 05:51 correspond-il à un réveil ? | Il s’agit d’une **échéance de réveil programmée**, inscrite dans un événement du 15. | Aucun réveil effectif à cette échéance n’est corroboré ; le demandeur et la date de programmation restent inconnus. |
| Les journaux révèlent-ils une dissimulation ? | Aucun indice probant d’effacement ou de falsification volontaire n’est établi. Les CRC et les séquences conservées sont cohérents. | Des anomalies d’en-tête existent ; les journaux ne constituent pas une preuve inviolable de leur histoire. |
| Des données ont-elles été regroupées et exportées ? | `L16B` contient **1 558 fichiers, soit 4,64 Go**, dont des messageries, documents locaux et exports cloud/bancaires. **1 555 créations FN** sont datées du 28 octobre. | Le PV décrit une copie par l’administration. Le dossier informatif laissé sur le PC ne certifie pas la composition du jeu définitivement saisi. |
| Des fichiers ont-ils été supprimés ? | **Dix mises à la corbeille le 28 octobre**, après l’ouverture du PC, sont explicitement datées. Des contenus déterminants restent récupérables. | Une mise à la corbeille n’est pas un effacement sécurisé ; elle n’établit ni le motif ni l’auteur. |
| Une compromission antérieure est-elle démontrée ? | Une détection de PDF de phishing et des indices de téléassistance sont présents. **Aucune compromission réussie ni exfiltration clandestine antérieure à la perquisition n’est établie.** | Les historiques sont incomplets et l’acquisition est postérieure de près de deux ans aux faits. |

L’analyse ne détermine ni l’intégrité matérielle des scellés, ni le caractère juridiquement autorisé d’une intervention, ni l’identité physique de l’opérateur.

## 3. Support analysé, méthode et fiabilité des sources

### 3.1. Identification de l’ordinateur et du support

| Élément | Identification |
|---|---|
| Ordinateur | **OP-01**, ASUS UX333F NOTEBOOK PC |
| Numéro de série du portable | **KAN0CV116290436** |
| Nom Windows | **LAPTOP-RMCOB2VU** |
| Compte local observé | **fintm**, SID `S-1-5-21-1394434332-468722268-2897565647-1001` |
| Processeur relevé | Intel Core i7-8565U CPU @ 1.80 GHz |
| SSD acquis | NVMe **INTEL SSDPEKNW512G8**, série **BTNH93120FL8512A** |
| Capacité du SSD | **512 110 190 592 octets**, soit 1 000 215 216 secteurs de 512 octets |
| Système indiqué à la remise | Windows 11 version 23H2 x64 ; cette identification ne certifie pas la version installée en octobre 2024. |
| Interface réseau identifiée | MAC **50:E0:85:63:41:5B**, concordante entre les événements WLAN d’OP-01 et l’entrée Freebox `LAPTOP-RMCOB2VU`. |

La présence de Sage 50, Ciel Paye Evolution, Adobe, Word, Excel, Outlook, OpenOffice, Teams, Oodrive Sign, PaperCut et Norton ne suffit pas à démontrer leur utilisation à une date donnée. L’identité du SSD est distincte de celle du portable ; l’identité réseau ne désigne pas son utilisateur.

### 3.2. Image disque et vérification d’acquisition

L’image du SSD a été acquise le **12 octobre 2026** avec **Guymager 0.8.13-1**, au format EWF/EnCase 6, en **74 segments `OP01.E01` à `OP01.E74`**, accompagnés de `OP01.info`. L’acquisition est déclarée terminée avec succès, sans mauvais secteur, et sa vérification d’image porte la mention **« Image verification OK »**.

Empreintes du flux disque, identiques entre acquisition et vérification de l’image :

```text
MD5     10c9f3df1ecd999567a05beaa4056ace
SHA-256 0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484
```

Ces empreintes concernent le flux disque reconstitué, pas chaque segment individuellement. La seconde vérification de la source était désactivée (`Source verification: off`) ; aucune nouvelle vérification intégrale par `ewfverify` ne complète ce contrôle. La vérification à l’acquisition ne certifie donc pas à elle seule l’absence de modification ultérieure des segments.

L’état SMART annonce une santé `PASSED`, aucun avertissement critique ni erreur de média/intégrité, 924 cycles d’alimentation, 2 202 heures sous tension et 13 arrêts non sûrs. Ces compteurs cumulés ne datent pas une utilisation particulière en 2024. Le [journal d’acquisition et l’environnement technique](recherche-OP-01/environnement-acquisition.txt) en conservent le détail.

### 3.3. Accès aux données et préservation

La partition Windows chiffrée BitLocker commence au secteur **567 296**, soit à l’offset **290 455 552 octets**. La chaîne de lecture dans SIFT est la suivante :

```text
Segments EWF → vue disque ewfmount → loop en lecture seule
             → déchiffrement Dislocker -r → volume NTFS ro,norecover
```

Les contrôles de montage montrent le loop avec `RO=1`, Dislocker avec `-r` et NTFS en lecture seule. Les sorties et copies de travail sont distinctes des données analysées. Les façades FUSE apparaissant en `rw` ne doivent pas être confondues avec les protections appliquées aux couches de lecture. **Le partage hébergeant les segments EWF est toutefois monté en écriture : il ne constitue pas un blocage d’écriture des fichiers d’acquisition.**

Les logiciels issus de l’image, les liens de connexion et les actions de documents n’ont pas été exécutés pour examiner leurs contenus. Les bases SQLite sont interrogées sur des copies ou en lecture seule, avec prise en compte des fichiers compagnons disponibles. Les empreintes des sources et des extractions permettent de contrôler les pièces utilisées ; elles ne remplacent pas la vérification intégrale de l’image.

Les principaux outils sont libewf, libevtx/pyevtx, pyfsntfs, pyregf, pyscca, pylnk, SQLite, Sleuth Kit, JLECmd, readpst, dfir_ntfs, les outils Poppler et PDFiD. Leurs versions, scripts et sorties sont conservés dans les dossiers techniques référencés en section 12.

### 3.4. Couverture et limites de conservation

| Source | Étendue utile | Limite principale |
|---|---|---|
| Journaux Windows EVTX | **359 fichiers, 275 577 enregistrements alloués** ; événements d’octobre 2024 conservés dans plusieurs journaux. | Les journaux sont partiels et leur période min/max ne garantit pas une couverture continue. |
| Security | **34 472 événements**, de septembre à octobre **2026**. | Les authentifications et audits de 2024 ne sont plus vérifiables dans ce journal. |
| MFT | **1 046 016 emplacements**, dont **1 045 790 entrées FILE exploitables**. | Les dates de fichiers ne sont pas des dates certaines d’utilisation ou de suppression. |
| USN | **325 252 enregistrements V2**, du 2 au 12 octobre **2026**. | Aucune couverture directe d’octobre 2024. |
| Prefetch, UserAssist et raccourcis récents | **887 Prefetch**, **313 valeurs UserAssist**, **268 LNK**. | Conservation limitée des dernières exécutions et métadonnées de cibles. |
| Jump Lists | **107 fichiers**, 4 351 entrées automatiques et 187 personnalisées. | Une entrée mémorisée n’équivaut pas à une consultation humaine ni à une copie réussie. |
| Navigation | Firefox : traces depuis 2019, mais seulement **5 visites en 2023 et 23 en 2024** ; Edge sans historique d’octobre 2024. | L’absence de visite est peu discriminante dans un historique aussi clairsemé. |
| Defender, PowerShell, sessions et WinRM | Traces disponibles principalement depuis septembre–décembre 2023 selon le journal. | Ne représentent pas toutes les menaces, commandes ou méthodes d’accès. |
| SetupAPI | Rotations couvrant notamment septembre 2023 à décembre 2024. | Décrit des installations de périphériques, pas tous les branchements ou transferts. |
| SRUM | Réseau : **682 lignes de septembre–octobre 2026** ; énergie : **127 lignes historiques de 2021 à 2024**. | Les statistiques d’énergie ne sont pas des compteurs de transfert réseau. |
| VSS | Deux créations référencées en octobre 2026 ; contenu non accessible. | Aucun état de volume d’octobre 2024 récupéré. |

## 4. Fonctionnement du PC pendant la rétention

### 4.1. Repères documentaires et conventions horaires

Le [procès-verbal de saisie](../docs/PV%20DE%20SAISIE.pdf) fournit les repères suivants. Ils sont distingués des déclarations de la cliente et des horodatages du PC.

| Repère | Date et heure de Paris | Précision |
|---|---|---|
| Perquisition | **15/10/2024** | L’heure exacte de début n’est pas établie dans les éléments exploités. |
| Mise sous scellés | **15/10 après 14:19** | L’heure de fermeture individuelle du PC n’est pas précisée. |
| Arrivée de la cliente | **28/10 à 10:22** | Ce repère ne correspond pas à l’ouverture du PC. |
| Ouverture du scellé du PC | **28/10 à 10:41** | Repère à comparer à la reprise Windows de 10:41:56. |
| Ouverture des téléphones | **28/10 à 11:30** | Borne distincte de celle d’OP-01. |
| Clôture des opérations | **28/10 à 19:20** | Restitution consignée sans heure individuelle ; récupération vers 19:20 déclarée par la cliente. |

La cliente déclare ne plus avoir eu accès au PC dès le début de la perquisition. L’heure approximative de 13:30 concerne sa perte d’accès aux téléphones ; elle n’est pas une borne de saisie de l’ordinateur.

Les heures locales utilisent **Europe/Paris** : UTC+2 le 15 octobre et UTC+1 le 28, après le changement d’heure du 27. Les dates UTC originales sont conservées. L’horloge du PC n’a pas été calibrée contre une source externe.

Les décomptes de l’**intervalle technique central** portent exactement sur **`[2024-10-15T08:53:09Z ; 2024-10-28T09:22:00Z[`**, soit du 15 à 10:53:09 au 28 à 10:22 à Paris. Ce périmètre de calcul ne correspond pas exactement à la durée des scellés : son début suit l’hibernation et sa fin précède de dix-neuf minutes l’ouverture documentée. Les décomptes associés, notamment les 3 461 entrées MFT, ne sont pas étendus implicitement jusqu’à 10:41. La reprise conservée à 10:41:56 est examinée séparément.

La fenêtre élargie couvre les dates civiles françaises du **14 au 29 octobre inclus**, soit **`[2024-10-13T22:00:00Z ; 2024-10-29T23:00:00Z[`**.

### 4.2. Reprise et hibernation du 15 octobre

| Heure de Paris | Source | Constat |
|---|---|---|
| **10:43:00–02** | System, Kernel-General/1, RecordID **37368** ; Power-Troubleshooter/1, **37385** | Reprise avec `WakeTime=2024-10-15T08:43:00.851496500Z`. Le `SleepTime` rapporté est le 10/10 à 22:34:30 Paris. |
| **10:43:01–03** | LocalSessionManager/Operational, événements **21, 22, 36**, RecordIDs **1805–1807** | Session 2 sous `LAPTOP-RMCOB2VU\fintm`, adresse `LOCAL`, puis état `DesktopLocked`. |
| **10:43:28 et 10:52:42** | System, Kernel-Power **506/507**, RecordIDs **37393/37437** | Capot signalé fermé puis ouvert ; alimentation secteur absente. |
| **10:53:05–08** | System, Kernel-Power **524, 42, 107**, RecordIDs **37443, 37445, 37447** | Batterie à **2 %**, absence de secteur et transition vers **S4/hibernation**, états cible/effectif à 5. |

Les Prefetch de `SHELLEXPERIENCEHOST.EXE` à 10:43:14 et de `WERFAULT.EXE` à 10:53:08 corroborent cette séquence. Elle établit un fonctionnement Windows, mais ne prouve pas à elle seule une saisie de mot de passe ou une consultation humaine : la session apparaît lors d’une reprise et le bureau est ensuite signalé verrouillé.

### 4.3. Absence d’activité intermédiaire corroborée

Les 359 journaux ne conservent **aucun événement daté du 16 au 27 octobre 2024**. Aucun événement alloué, fragment EVTX datable, lancement Prefetch/UserAssist ou horodatage LNK examiné ne corrobore une activité dans l’intervalle technique central.

Dans System, les RecordIDs **37447** et **37448**, associés respectivement à la fin de la séquence du 15 et à la reprise du 28, sont consécutifs. Power-Troubleshooter rapporte le 28 un `SleepTime` correspondant au 15 à 10:53:05 Paris. Le rattrapage d’horloge relie également ces deux séquences.

**Ces recoupements soutiennent un scénario d’hibernation sans reprise Windows intermédiaire conservée. Ils n’établissent pas une absence absolue de manipulation.** Une lecture du SSD hors ligne, un autre système de démarrage, une activité non journalisée ou des traces écrasées peuvent échapper aux sources disponibles.

### 4.4. Reprise et interactions du 28 octobre

| Heure de Paris | Source | Résultat et interprétation |
|---|---|---|
| **10:41:56–58** | System, Kernel-General/1 **37448**, Kernel-Power/105 **37452**, Power-Troubleshooter/1 **37466** | Reprise sur secteur, état cible/effectif 5 ; concordance à la minute avec l’ouverture du PC à 10:41 au PV. |
| **10:50:44, 10:53:35, 11:01:54** | OAlerts, Office 16 Alerts/300, **247, 249, 251** | Activité Word, Excel et Outlook. Les exécutions Word/Excel sont aussi corroborées par Prefetch. |
| **13:08:11–13:12:54** | OAlerts/300, **257–264** | Huit demandes Outlook de confirmation de suppression définitive. |
| **13:26:30–13:39:05** | OAlerts/300, **265–281** | Dix-sept demandes d’enregistrement de propriétés modifiées de messages, dont certains portent le sujet `RELEVES CE DMM CONSEILS`. |
| **15:38:14** | OAlerts/300, **284** | Nouvelle demande Outlook de confirmation de suppression définitive. |
| **17:15:40** | UserAssist | Lancement référencé de `D:\LdSD-1.0.4\bin\Win64\LdSD.bat`. Sa fonction et son éditeur ne sont pas identifiés de manière fiable. |
| **17:26:19** | UserAssist et Prefetch | Lancement de Notepad, concordant entre les deux sources à environ 82 ms. |
| **17:31:37** | UserAssist | Lancement référencé de `D:\WD Drive Unlock.exe`, sans preuve autonome de déverrouillage ou de copie. |
| **17:37:47** | LocalSessionManager/Operational, **23/24**, RecordIDs **1808/1812** | Fin puis déconnexion de la session locale 2 sous `fintm`. |

Les alertes Outlook sont des indices forts d’interaction. Elles ne prouvent pas la réponse donnée aux boîtes de dialogue, la réussite des suppressions ou le contenu effectivement modifié. Les commandes PowerShell conservées à 11:02–11:03 et 11:23 concernent des diagnostics et le retrait du package `C27EB4BA.DropboxOEM` ; elles peuvent provenir d’opérations automatiques.

Le fournisseur nommé `TerminalServices` n’implique pas à lui seul un accès RDP. Les notifications Winlogon numériques 4/5 n’étant pas validées contre le schéma local, elles sont utilisées seulement comme recoupements. Security ne permet pas de confirmer un type d’authentification de 2024.

Le 28 à 11:19:30, une correction d’environ **−9,238 secondes** est déduite des champs `OldTime/NewTime`. Le champ `TimeDeltaInMs` incohérent n’est pas utilisé. Aucun événement EVTX n’est retrouvé après 19:20 ce jour-là ; les dates de fichiers postérieures ne suffisent pas à démontrer une utilisation locale après la clôture.

### 4.5. Échéance de réveil du 16 octobre

L’événement **System / Microsoft-Windows-Kernel-Power / 107 / version 1 / RecordID 37447**, enregistré le 15 à **08:53:08.371843800 UTC**, contient :

```xml
<Data Name="TargetState">5</Data>
<Data Name="EffectiveState">5</Data>
<Data Name="WakeFromState">5</Data>
<Data Name="ProgrammedWakeTimeAc">2024-10-16T03:51:07.133163100Z</Data>
<Data Name="ProgrammedWakeTimeDc">1601-01-01T00:00:00.000000000Z</Data>
<Data Name="WakeRequesterTypeAc">2</Data>
<Data Name="WakeRequesterTypeDc">0</Data>
```

`ProgrammedWakeTimeAc` décrit une **échéance sur secteur**, le **16 à 05:51:07 Paris**. Il diffère du champ `WakeTime` de Power-Troubleshooter, qui rapporte une reprise effective. La valeur DC à l’époque FILETIME 1601 est compatible avec l’absence d’échéance sur batterie.

L’échéance exacte n’a qu’une occurrence dans les 359 journaux. L’examen de **264 définitions de tâches**, de **2 265 clés ciblées**, dont **260 TaskCache/Tasks**, et des ruches SYSTEM/SOFTWARE ne fournit ni demandeur identifié ni date d’armement. Le journal détaillé TaskScheduler/Operational est absent et les audits Security de création/modification de tâche de 2024 ne sont plus conservés.

Huit tâches acquises portent `WakeToRun=true`, notamment NGEN, InstallService et UpdateOrchestrator. Cet état tardif, leurs dates XML ou leurs échéances ne reconstituent pas leur état exact en 2024. Des événements antérieurs présentent déjà `WakeRequesterTypeAc=2`. Le précédent événement 107 du 10 octobre concerne un état différent et ne borne pas avec certitude la création du minuteur entre le 10 et le 15.

**L’échéance est attestée dès le 15 à 10:53:08 ; un réveil le 16 n’est pas démontré.** Maintenance et Windows Update sont des explications possibles, sans attribution établie à une tâche. Le sens détaillé du type de demandeur 2 et la raison interne de cet événement 107 ne sont pas déterminés.

## 5. Journaux Windows : cohérence, anomalies et traces d’effacement

### 5.1. Couverture des événements et qualité du décodage

La lecture des **275 577 enregistrements alloués** comprend **274 638 exports XML interprétés** et **939 exports rejetés par le parseur XML**. Ces rejets ont tous un horodatage extractible et sont pris en compte dans le contrôle temporel ; 285 appartiennent à la fenêtre élargie et aucun à l’intervalle central. Un export XML mal formé ne démontre pas à lui seul une altération du fichier EVTX.

| Date civile de Paris | XML interprétés | Rejets XML datés | Total contrôlé |
|---|---:|---:|---:|
| 14/10/2024 | 0 | 0 | 0 |
| 15/10/2024 | 412 | 0 | 412 |
| 16 au 27/10/2024 | 0 | 0 | 0 |
| 28/10/2024 | 5 964 | 108 | 6 072 |
| 29/10/2024 | 3 417 | 177 | 3 594 |

Les **9 793 événements XML interprétés de la fenêtre élargie** proviennent de 91 journaux. Ils sont distingués des rejets datés et du total de tous les enregistrements. Chaque RecordID n’a de sens qu’avec le journal et le fournisseur auxquels il appartient.

### 5.2. Structure binaire et continuité

Les contrôles portent sur les signatures, tailles, bornes, identifiants et CRC32. Les **359 CRC d’en-tête de fichier** et ceux des **2 951 blocs signés** sont valides. Les **275 577 enregistrements binaires** concordent avec les décomptes libevtx. Aucune anomalie de taille finale, rupture interne de séquence, duplication ou lacune d’identifiant n’est relevée entre le minimum et le maximum conservés dans chaque fichier.

| Journal | Enregistrements | Identifiants conservés |
|---|---:|---|
| System | 36 445 | 5 446–41 890 |
| Security | 34 472 | 1 567 448–1 601 919 |
| Application | 21 577 | 1–21 577 |
| Winlogon/Operational | 2 506 | 8 411–10 916 |
| LocalSessionManager/Operational | 1 748 | 244–1 991 |
| TaskScheduler/Maintenance | 805 | 1–805 |

**Des anomalies d’en-tête existent : 41 fichiers sont signalés « corrupted » par libevtx et 59 portent le flag `dirty`.** Trente-neuf fichiers présentent un premier numéro de bloc supérieur au dernier. Application et Ntfs/Operational contiennent davantage de blocs physiques que déclaré. Certains compteurs du prochain enregistrement sont en retrait des identifiants réellement présents.

Ces anomalies sont compatibles avec des en-têtes non actualisés ou une clôture incomplète. Leur cause historique n’est pas établie. **Le signalement « corrupted » ne prouve pas une falsification volontaire ; des CRC valides et des séquences continues ne garantissent pas non plus l’authenticité historique**, car ils peuvent être reconstruits.

### 5.3. Recherche d’effacement et fragments résiduels

Aucun événement explicite d’effacement **Eventlog 104 ou Security 1102** n’est retrouvé dans les enregistrements alloués, les fragments interprétables ou les blocs décodés depuis d’anciennes entrées MFT. Les événements d’arrêt du service de journalisation ou de modification d’horloge conservés dans la sélection sont de 2026 ; ils ne documentent pas une dissimulation en octobre 2024.

La configuration acquise indique une taille maximale de **20 Mio** et `Retention=0` pour Security et System, ainsi qu’un TaskScheduler/Operational désactivé. La rotation et la désactivation sont des explications normales possibles des lacunes. Ces paramètres tardifs ne prouvent pas une configuration identique en 2024.

L’espace libre des blocs EVTX contient **7 587 candidats**, dont **4 120 interprétables** et **3 467 illisibles**. Aucun horodatage externe candidat ni événement récupéré interprétable n’appartient à l’intervalle central. Les fragments ne représentent pas autant d’effacements : **6 040** partagent le triplet journal/RecordID/FILETIME d’un enregistrement alloué, et l’ensemble ne compte que **7 160 triplets distincts**.

Parmi **103 anciennes entrées MFT non allouées nommant des EVTX**, les lectures retrouvent 37 blocs et permettent de décoder **4 537 enregistrements**. **35 blocs sont identiques par SHA-256 à des blocs actuels** ; les deux autres ont un CRC de données invalide. Les divergences entre anciens noms et fournisseurs décodés attestent la réutilisation d’emplacements, sans restituer les anciens System/Security de 2024. Aucun événement de l’intervalle central ni 104/1102 n’y est retrouvé. Les conteneurs synthétiques employés pour lire ces blocs sont des auxiliaires de décodage, pas des EVTX originaux.

**Conclusion : aucun indice probant de suppression ou de falsification destinée à masquer une activité pendant la rétention n’est établi. Les lacunes de conservation et les limites d’authentification des journaux empêchent de l’exclure absolument.**

## 6. Métadonnées NTFS et dates de fichiers pendant la rétention

### 6.1. Lecture de la MFT et sens des dates

La **MFT**, table des fichiers NTFS, mesure **1 071 120 384 octets**. Son empreinte est :

```text
SHA-256 4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b
```

Les **1 045 790 entrées FILE exploitables** comprennent **665 406 entrées allouées** et **380 384 non allouées**, sans échec de fixup ou de bornage relevé. Ces nombres incluent dossiers et extensions ; ils ne sont pas des décomptes de documents récupérables.

Les attributs **STANDARD_INFORMATION (SI)** et **FILE_NAME (FN)** conservent des jeux de dates distincts. Une copie ou une décompression peut préserver certaines dates antérieures ; un changement de métadonnées peut en modifier d’autres. Leur confrontation est donc nécessaire avant d’associer une date à une opération locale.

### 6.2. Les 3 461 entrées datées dans l’intervalle central

| Ensemble | Entrées allouées | Constat |
|---|---:|---|
| `Users/fintm/iCloudPhotos/Photos/…` | **3 434** | Au moins une date dans l’intervalle central, mais toutes ont un changement MFT SI en **2026** et des divergences SI/FN. |
| `L16B/TELEPHONES/IPHONE13_MINI/…` | **27** | Création SI le **15/10/2024**, création FN le **28/10/2024** ; changement MFT SI le 28 pour deux entrées et le 29 pour vingt-cinq. |

Aucune des **3 461 entrées** n’a sa date SI de changement MFT dans l’intervalle central. Les 472 entrées nommant des EVTX n’ont aucune date SI/FN dans cet intervalle.

Un exemple est `Avis ECH 0423 SAS RCT 2.pdf` : sa création SI est le **15/10 à 11:47:17.660 UTC**, mais ses quatre dates FN sont le **28/10 à 16:13:43.235508 UTC**. Cette combinaison est compatible avec une copie après ouverture conservant une date plus ancienne ; elle ne démontre pas un PC actif le 15 à 13:47 Paris.

Les fichiers iCloud portent aussi des dates historiques avec changements ultérieurs. Le recoupement USN, par référence MFT et numéro de séquence, retrouve **3 252 des 3 434 fichiers** dans **54 678 événements** de changement de métadonnées (`BASIC_INFO_CHANGE`), tous le 2 octobre 2026. Ces événements ne portent pas `DATA_OVERWRITE`, `DATA_EXTEND` ou `DATA_TRUNCATION`. Ils attestent un traitement de métadonnées, sans identifier les champs modifiés, leur origine initiale ou le logiciel demandeur.

Cinq fichiers iCloud portent des dates SI/FN du 28 après 19:20, avec changement MFT SI en octobre 2026. **Ils ne prouvent pas une utilisation locale du PC après la clôture du 28.** Le mécanisme exact de provenance ou de restauration des métadonnées n’est pas entièrement déterminé.

### 6.3. Journaux NTFS et clichés de volume

Le journal **USN** conservé ne couvre que le 2–12 octobre 2026. Il ne peut donc pas confirmer une copie ou un effacement de 2024.

Le **`$LogFile`**, de **67 108 864 octets**, est décodé avec **dfir_ntfs 1.1.20** et livre **388 732 enregistrements de journal NTFS**. Les **31 063 structures USN** interprétées portent exclusivement des dates du 8 et du 12 octobre 2026. Sept correspondances ciblées concernent des raccourcis Recent vers L16B, GDRIVE et les fichiers d’inventaire/archive ; les données redo/undo indiquent des mises à jour de dates d’accès en octobre 2026. Les dates anciennes embarquées dans certains enregistrements ne datent pas la transaction qui les contient.

**Ce décodage n’apporte aucune transaction datée d’octobre 2024 permettant de reconstruire les exports.** Ce résultat ne prouve pas l’absence d’opérations anciennes : le journal conserve des données plus récentes et ne fournit pas un historique complet. Les empreintes du journal et de la MFT concordent avant et après lecture ; les [résultats du décodage](../investigations/20261017-recroisements/compte-rendu.md#décodage-complet-du-journal-ntfs) en donnent le détail.

Les clichés **VSS** ne sont pas accessibles : `vshadowinfo` retourne une erreur d’identifiant d’en-tête. Le catalogue référence deux créations du **2 octobre 2026**, aucun état de volume d’octobre 2024. Aucun cliché n’est monté, réparé ou restauré ; la cause de l’échec n’est pas attribuée à une falsification.

## 7. Regroupement, exports et copies de données

### 7.1. Composition et datation du dossier L16B

Le dossier `C:\L16B` contient **1 558 fichiers totalisant 4 643 450 972 octets**, soit 4,64 Go décimaux. Le total additionne des archives et des contenus également présents sous forme développée : il ne mesure ni un volume de données uniques ni un volume transmis.

| Ensemble | Contenu observé | Créations FN du 28 octobre, heure de Paris |
|---|---|---|
| `LOCAL` | **1 389 fichiers**, notamment documents locaux | **10:47:55–11:11:10** |
| `GDRIVE`, dossier développé | **93 fichiers** | **14:50:40–14:50:46** |
| `MESSAGERIES` | **34 fichiers**, dont deux PST, trente EML, une archive Takeout et un PDF à création FN de 2026 | Messageries regroupées le 28 ; le PDF supplémentaire doit en être distingué. |
| `TELEPHONES` | **30 fichiers**, dont 27 PDF dans `IPHONE13_MINI` et trois ZIP WhatsApp dans `IPHONE13` | **17:01:10–17:13:43** |
| `iCloud Drive` | **8 fichiers** | **14:30:23–14:37:51** |
| `SAGE/sage.pdf` | PDF de **42 818 862 octets** | **15:27:24** |
| Export SHINE | ZIP de **1 769 414 octets** | **15:57:55** |
| Deux ZIP GDRIVE | Archives distinctes du dossier développé | Créations FN en **2026**, détaillées ci-dessous. |

**1 555 créations FN sont datées du 28 octobre 2024**, entre 10:47:55 et 17:13:43 Paris. Les trois autres concernent :

| Fichier | Création FN, heure de Paris |
|---|---|
| `L16B/GDRIVE.zip` | **27/07/2026 à 19:01:33** |
| `L16B/GDRIVE (2).zip` | **27/07/2026 à 19:07:00** |
| `L16B/MESSAGERIES/misssmalika@hotmail.com/CADA.pdf.pdf` | **02/10/2026 à 19:23:38** |

Ces trois fichiers ne peuvent pas être attribués automatiquement à une création par l’administration en 2024. Les dates sont compatibles avec des ajouts ou recréations ultérieurs ; elles n’identifient pas l’auteur et ne démontrent pas une substitution.

Les SI plus anciens, dont **93 créations au 31/12/1979**, doivent être distingués des FN du 28. Des dates minimales ZIP au 01/01/1980, avec effets de fuseau, et des métadonnées préservées lors de décompressions peuvent expliquer ce type d’écart. Les FN ne sont toutefois pas des signatures inviolables.

Sur **40 documents** sélectionnés parmi 1 232 PDF/Office de moins de 4 Mio de `LOCAL`, **16 contreparties** sont retrouvées dans le profil `fintm`, toutes identiques par SHA-256. L’échantillon confirme des contenus communs au profil et à L16B, sans établir le sens de copie ni l’origine de tous les fichiers. L’absence de contrepartie aux chemins candidats pour les vingt-quatre autres ne prouve pas leur suppression.

**Le regroupement local de données pendant les opérations du 28 est fortement étayé par les créations concentrées, les formats et les correspondances de contenu.**

### 7.2. Messageries Outlook et fichiers EML

Les deux PST sont de véritables conteneurs de messagerie décodés avec `readpst` :

| Conteneur | Taille | Messages reparsés |
|---|---:|---:|
| `dmmconseils@hotmail.com.pst` | **2 143 626 240 octets** | **3 836** |
| `dmmconseils93300@hotmail.com.pst` | **1 156 260 864 octets** | **2 039** |
| **Total** | | **5 875** |

Le comptage concerne les messages reparsés, sans certifier tous les objets Outlook, les éléments supprimés ou l’exhaustivité des boîtes serveur. Les trente EML sont analysables comme messages : quatorze sous `fint.ms@hotmail.com` et seize sous `misssmalika@hotmail.com`. Les chemins et en-têtes ne certifient pas une extraction complète ou exclusive depuis ces comptes.

Le PST `93300` contient un diagnostic Outlook dont l’en-tête est daté du 28 à **14:12:02 UTC**. Son corps décrit une synchronisation **15:04:42–15:12:02**, **937 éléments ajoutés**, puis l’erreur **8004010E**, « Ressources système insuffisantes ». Ces heures sont cohérentes avec Paris, mais le diagnostic ne localise pas sa machine d’origine et ne certifie pas une synchronisation complète. Les 937 éléments ne sont pas le nombre total de messages du PST.

Les recherches textuelles ciblées dans les 5 875 messages ne mettent pas en évidence une transmission sortante de L16B ou des fichiers `Archive_saddedine`, `Inventaire_saddedine`, `Rejets_saddedine`. Elles ne couvrent pas tous les contenus binaires des pièces jointes ni d’autres canaux de transmission.

Les Jump Lists référencent les PST avec des dernières interactions le **29 octobre vers 18:37 Paris**. Ces dates sont postérieures à la restitution déclarée ; elles ne sont pas des consultations du 28. De même, la date d’un message reçu avant l’ouverture du PC est une date de messagerie, pas une preuve d’utilisation locale du PC à cette heure.

### 7.3. Google Takeout, Drive, Sage et SHINE

L’archive **`takeout-20241028T114105Z-001.zip`**, de **41 828 775 octets**, contient un **MBOX de 66 015 300 octets** et un manifeste HTML de 197 837 octets. Les deux membres se décompressent sans erreur. Le manifeste mentionne `rct93300@gmail.com` et affiche une date d’export correspondant au **28/10 à 12:42:33 Paris**. Le nom de l’archive correspond à **12:41:05 Paris** et sa création FN à **12:46:29**.

Ces repères corroborent un export le 28, sans authentifier cryptographiquement le producteur ni désigner la machine ou l’auteur de la demande. L’écart de 88 secondes entre nom et manifeste ne calibre pas l’horloge Windows. Les dates DOS minimales des membres ne datent pas l’export.

Les **93 fichiers du dossier `GDRIVE`** sont tous identiques par SHA-256 à des membres d’une archive de téléchargement récupérée dans la corbeille, qui contient **94 fichiers**. Le fichier supplémentaire est un document de gestion de mots de passe, détaillé en section 8. Les flux `Zone.Identifier` relevés renvoient à cette archive et renforcent le rapprochement téléchargement/décompression vers le dossier.

Les deux ZIP GDRIVE à création FN de 2026 mesurent chacun **61 847 396 octets** et possèdent des catalogues identiques de **97 membres, dont 93 fichiers**, mais des empreintes globales différentes. Le contrôle des contenus établit :

| Archive | Résultat de décompression | Portée |
|---|---|---|
| `GDRIVE.zip` | **90 fichiers lisibles sur 93** ; trois PDF bancaires en erreur | Deux erreurs d’en-tête local et une erreur de décompression. |
| `GDRIVE (2).zip` | **92 fichiers lisibles sur 93** ; erreur sur `GDRIVE/ALMU 2023 ZIP.zip` | Défaut portant sur un autre membre. |

Les **89 fichiers lisibles dans les deux archives** ont des SHA-256 identiques. Leurs membres lisibles complémentaires couvrent les **93 contenus du dossier développé**, avec identité SHA-256. Les contenus sont donc disponibles dans le corpus malgré les défauts des conteneurs. La date, la cause et l’intention éventuelle de ces défauts ne sont pas établies ; ils ne démontrent pas une altération par les agents en 2024.

Le PDF **`SAGE/sage.pdf`** contient des factures et conserve le texte des deux factures retrouvées dans le `test.pdf` supprimé, aux **pages 254 et 255**. Cette concordance textuelle ne valide pas l’ensemble du PDF contre la base Sage et ne constitue pas une identité binaire entre les deux PDF.

L’archive **`RCT_01-2023_15-10-2024_EXPORT.zip`** se décompresse sans erreur et comporte **30 membres : CSV, OFX, QIF et 27 justificatifs PDF**. Le CSV comprend **94 lignes** et l’OFX **94 transactions**, avec une période déclarée du **01/01/2023 au 15/10/2024**. La période comptable ne date pas l’export, dont les traces locales sont du 28. Le nom RCT et le titulaire doivent être rapprochés de pièces bancaires ; le PV ne les authentifie pas à lui seul.

### 7.4. Supports Kingston et références à une archive externe

Trois identifiants **Kingston DataTraveler 3.0** distincts apparaissent dans les anciennes rotations SetupAPI :

| Identifiant matériel enregistré | Début de section du 28 octobre, heure locale consignée |
|---|---|
| `E0D55EA493C4F3A178B11467&0` | **16:27:54.063** |
| `E0D55EA49333E49089B402AD&0` | **17:00:07.167** |
| `0026188879D7F250D72E0E88&0` | **17:14:51.903** |

Les sections décrivent une installation et un démarrage réussis de périphériques. Le texte ne porte pas de fuseau ; les heures locales sont cohérentes avec la séquence du 28. **Ces traces établissent une présence de supports, pas une copie déterminée.** Leur disparition du registre USBSTOR actuel est expliquée par un nettoyage Storage Sense consigné le 3 décembre 2024, sans preuve d’intention de dissimulation.

Le recoupement MountedDevices/MountPoints2 relie trois volumes aux identifiants Kingston et un quatrième au **CD virtuel Western Digital de déverrouillage**, avec `D:\WD Drive Unlock.exe`. Il n’identifie pas la partition de données externe. Une lettre de lecteur ne désigne pas durablement un support.

Les Jump Lists et des LNK concordants référencent un volume **KINGSTON `140B8328`** et :

- `E:\saddedine\Rejets_saddedine.txt`, vers **17:26:19** ;
- `E:\saddedine\Inventaire_saddedine.csv`, vers **17:26:33** ;
- `E:\saddedine\Archive_saddedine.zip`, vers **17:27:29**.

Le numéro `140B8328` identifie un système de fichiers ; il n’est pas un numéro de série matériel USB et n’est pas rattaché à l’un des trois Kingston. Les tailles mémorisées des cibles sont de **3 525 227 798 octets** pour l’archive et **527 208 octets** pour l’inventaire. Les fichiers externes eux-mêmes n’ayant pas été récupérés, ces références ne certifient ni leur contenu, ni leur intégrité, ni la copie de L16B dans l’archive.

Une clé PHILIPS porte par ailleurs des propriétés datées du **30 octobre à 00:38:33 Paris**, après la restitution déclarée. Ces propriétés ne constituent pas un historique complet de ses branchements.

### 7.5. Rapprochement avec le PV et limites de la copie finale

**Le PV décrit une extraction, un filtrage, une copie sur une clé de l’administration et une authentification des fichiers, avec inventaires sur CD.** Les catégories de L16B, les deux PST, les trente EML, Takeout, Sage et SHINE concordent substantiellement avec les opérations annoncées. Les créations FN concentrées après 10:41 et les références à l’archive/inventaire/rejets corroborent matériellement ce récit.

Le PV précise cependant que **L16B est laissé sur le PC à titre informatif et ne remplace pas les fichiers définitivement saisis**. Le CD d’inventaire, les empreintes finales et les contenus emportés ne sont pas disponibles pour comparaison. Il n’est donc pas possible de certifier que chaque fichier actuel de L16B a été saisi, que tous les fichiers saisis s’y trouvent ou qu’aucun contenu différent n’a été emporté.

La présence de **trois identifiants Kingston**, face à la clé unique décrite, reste à expliquer par les pièces de procédure et les supports. Elle ne démontre ni trois copies ni trois destinataires. L’attribution des opérations décrites à l’administration repose sur le recoupement du PV et des artefacts ; elle ne constitue pas une identification technique individuelle de chaque opérateur.

### 7.6. Documents de téléphones et correspondances avec des avocats

Les **27 PDF de `IPHONE13_MINI` représentent 20 contenus distincts**, tous retrouvés à l’identique dans les sauvegardes **TP-02 et TP-03**. Ils ne permettent pas de désigner un téléphone source exclusif, de départager les scellés n° 3/n° 4 ou de prouver une extraction directe sur OP-01. Les trois archives WhatsApp portent des dates internes anciennes qui ne datent pas leur importation sur le PC.

Le fichier d’appairage Apple ancien présent sur OP-01 est rattaché à **TP-03 par l’UDID exact**. Ses dates SI de juillet 2022 et FN/modification de décembre 2023 ne datent aucun branchement ou transfert d’octobre 2024.

Des **correspondances avec des avocats sont présentes dans L16B**, notamment Negrevergne, Pascoët, Khallouki, Fakiroff/Roosevelt Avocats, Wahrheit et Guillou. Les [messages](../investigations/20261109-correspondances-elargies/tableau-messages.md), [documents](../investigations/20261109-correspondances-elargies/tableau-documents.md) et la [fiche du PDF Bourarach](../investigations/20261109-clarification-correspondances/fiche-bourarach.md) individualisent les pièces.

Leur **emport définitif, leur lecture par les agents et leur utilisation fiscale ne sont pas établis**. Leur qualification exige un examen individuel ; une mention d’avocat ne suffit pas. La recherche n’est pas exhaustive : l’OCR dispose de 4 238 résultats sur 5 365 contenus, avec 1 127 sans résultat terminé dans la passe considérée.

## 8. Suppressions et contenus récupérables

### 8.1. Portée de la récupération

Une **mise à la corbeille** retire le fichier de son chemin d’origine, mais son contenu `$R` peut rester alloué. La métadonnée `$I` associée conserve l’ancien chemin, la taille et une date explicite de suppression. À l’inverse, une **entrée MFT non allouée** peut conserver un nom et des dates alors que ses clusters sont réutilisés. Les SI/FN ne sont pas des dates explicites d’effacement.

L’inventaire porte sur toute la MFT. La sélection de récupération retient **4 299 candidats**, dont **4 122 non alloués** et **177 objets de corbeille alloués**, selon les chemins, formats et noms pertinents. Elle ne couvre pas tous les anciens contenus du SSD.

| Résultat | Nombre ou volume | Limite d’interprétation |
|---|---:|---|
| Lectures logiques complètes | **4 253** | Ne certifient pas l’identité historique des octets récupérés. |
| Lecture limitée à un préfixe | **1**, ancien `WhatsApp.dll` | Limite de 64 Mio ; pas de validation complète du binaire. |
| Échecs | **45** | 34 décompressions NTFS, 10 absences de flux DATA et une erreur d’entrée. |
| Octets lus | **675 734 678** | Peuvent inclure des données réutilisées ou recouvrantes. |
| Contenus non vides et non entièrement nuls conservés | **3 261** | Empreintes vérifiées sans divergence entre SIFT et les copies locales. |
| Lectures de taille nulle / non vides entièrement nulles | **978 / 15** | Une taille nulle ne signifie pas un écrasement par des zéros. |
| Candidats non alloués dont tous les clusters ordinaires évalués sont actuellement alloués | **1 753** | Réutilisation possible ; l’ancien nom n’authentifie pas le contenu lu. |

Les chemins à parent manquant ou réutilisé sont signalés comme incertains. Un recoupement `fls` est partiel ; il ne remplace pas le scan MFT complet. Les tentatives sur anciens journaux OneDrive compressés n’ont pas reconstitué d’historique de transferts de 2024.

### 8.2. Dix mises à la corbeille le 28 octobre

La corbeille du profil `fintm` conserve **89 métadonnées `$I` de version 2**, datées de 2020 à 2026. Parmi les 88 objets `$R` associés retrouvés, 48 ont un contenu non nul conservé. **Dix mises à la corbeille sont datées du 28 octobre**, toutes après l’ouverture du PC à 10:41 et avant la clôture à 19:20.

| Heure de Paris | Ancien chemin ou objet | Contenu et portée |
|---|---|---|
| **11:02:53.315 et .322** | Deux raccourcis sous `C:\L16B\LOCAL`, nommés `Téléchargements - Raccourci (2).lnk` et sa copie | Deux LNK identiques de 758 octets, ciblant `C:\Users\fintm\Downloads`. |
| **14:51:12.749** | `…\Downloads\drive-download-20241028T134819Z-001\GESTION DES MOTS DE PASSES 2.docx` | DOCX de **10 562 octets**, récupéré et structure ZIP contrôlée. |
| **14:52:25.983** | `…\Downloads\drive-download-20241028T134819Z-001.zip` | ZIP de **61 904 642 octets**, récupéré avec validation CRC de tous les membres. |
| **15:12:28.791–15:12:29.137** | Cinq fichiers Ciel sous `Compléments utilisateur\Etats` : `BANMAT`, `My Little`, `Prestations de service~YARA`, `RCT`, `RCT Shine` | Contenus récupérés de **36 552 à 59 661 octets**, compatibles avec des états propriétaires dont le format n’est pas intégralement interprété. |
| **15:24:17.961** | `C:\L16B\test.pdf` | PDF de **499 320 octets**, deux pages lisibles. |

Les métadonnées et contenus de ces dix opérations concordent avec les contre-lectures directes de l’image. Les [chemins complets, heures et références MFT](../investigations/20261019-retour-cliente/compte-rendu.md#4-dix-mises-à-la-corbeille--contre-lecture-directe) permettent leur contrôle individuel.

Ces constats établissent des retraits vers la corbeille, sans démontrer un effacement sécurisé, un motif ou l’identité de l’auteur. Les cinq fichiers d’états Ciel ne doivent pas être décrits comme une base comptable détruite. Le SID identifie un profil Windows, pas la personne présente devant le PC.

### 8.3. Archive de téléchargement et document de gestion de mots de passe

Le ZIP récupéré contient **96 membres, dont 94 fichiers**, totalisant **68 224 820 octets décompressés**. Son nom est caractéristique d’un téléchargement Drive, sans constituer à lui seul une authentification du service ou du compte.

La comparaison cryptographique établit deux correspondances :

- les **93 fichiers actuels de `L16B/GDRIVE`** sont identiques par SHA-256 à 93 membres de cette archive ;
- le **94e fichier**, `GESTION DES MOTS DE PASSES 2.docx`, est identique au DOCX récupéré séparément dans la corbeille et absent du dossier `L16B/GDRIVE` actuel.

Le DOCX contient **quatre tableaux, 34 lignes et 86 cellules non vides**, avec des rubriques d’identifiants et de mots de passe, dont des valeurs en clair dans le XML. Aucune valeur de connexion n’est reproduite dans ce rapport. Sa présence ne prouve ni la validité actuelle des identifiants ni leur consultation ou leur utilisation.

```text
ZIP récupéré — MFT 76808 — SHA-256
03a593ea508aefdb1bf8b0280dce839a1b7f8098a7560a3f8c345a61d7a5bc44

DOCX récupéré — MFT 77995 — SHA-256
38fcaf9ab9a8aac80038dd0bd75a45e884339208def6d083d6134473becf2b0a
```

**Un ensemble de 94 fichiers comprenant ce document a donc été présent localement dans un chemin de téléchargement.** Le document développé et l’archive ont été mis à la corbeille à une minute d’intervalle, tandis que L16B conserve les 93 autres contenus. Ce rapprochement renforce le constat de regroupement local le 28. Il n’établit ni la machine ayant demandé l’archive, ni l’opérateur, ni une transmission ultérieure, ni le motif de l’absence du 94e document dans L16B.

### 8.4. PDF de factures créé puis supprimé

Le `test.pdf` récupéré contient deux factures Sage/ALMU, **FA0338 et FA0339**, dont les dates commerciales de mars 2022 ne datent pas la génération du PDF. Les métadonnées internes indiquent **Microsoft: Print To PDF**, le titre `Facture - FA0339` et une création/modification le **28 octobre à 15:19:42 Paris**. La mise à la corbeille survient environ 4 min 36 s plus tard.

Son SHA-256 est `f2cb8dbbbb28fe11eaddc59d31045152218516a1585109bd529a075e48dd8201`. Le texte des deux factures subsiste aux pages **254 et 255 de `L16B/SAGE/sage.pdf`**, après normalisation des espaces. **Une destruction malveillante de ces factures n’est pas établie.** La concordance n’identifie ni le processus à l’origine de l’impression ni l’auteur, et ne certifie pas les transactions commerciales.

### 8.5. Autres contenus et portée pour la période sous scellés

Les contrôles statiques sur les 3 261 contenus conservés comprennent **58 candidats PDF**, **72 signatures PE**, **17 LNK**, huit candidats Prefetch, cinq signatures ZIP et deux SQLite. Huit erreurs de parsing restent consignées. Quarante-huit PDF sont lisibles par `pdfinfo` et quarante-quatre donnent un texte non vide. PDFiD ne relève ni `/JS`, ni `/JavaScript`, ni `/Launch` dans les 58 candidats ; un `/OpenAction` correspond à une destination d’affichage sans script identifié. Ces contrôles ne garantissent pas l’innocuité de contenus tronqués ou non entièrement interprétés.

Les correspondances de noms d’outils distants dans les exécutables ont été qualifiées comme sous-chaînes sans lien établi avec ces produits. Les trois Prefetch décodés concernent des exécutables Windows ; ils ne révèlent pas d’exécution dans l’intervalle central. Les binaires non reconnus n’ont pas tous été décodés et les signatures numériques n’ont pas été exhaustivement validées.

Aucune date SI/FN des **380 384 entrées MFT non allouées**, ni aucune des **89 dates de mise à la corbeille**, ne se situe dans l’intervalle technique central. **Cela ne constitue pas un registre exhaustif des suppressions** : des entrées réutilisées, des opérations hors corbeille ou des données écrasées peuvent ne plus être représentées.

Les suppressions établies documentent les opérations **du 28 après ouverture**. Elles n’établissent pas une utilisation avant ouverture, une compromission antérieure à la perquisition ou un transfert vers un destinataire déterminé.

## 9. Indices de compromission et accès antérieurs à la perquisition

### 9.1. PDF détecté comme phishing en mai 2024

Le journal Defender conserve une détection et sa remédiation, reliées par le même identifiant :

| Événement | Date et heure de Paris | Données utiles |
|---|---|---|
| **1116, RecordID 920** | **15/05/2024 à 10:13:02.744935** | `Trojan:PDF/Phish.TSC!MTB`, protection en temps réel, utilisateur `fintm`, processus rapporté `RuntimeBroker.exe`. |
| **1117, RecordID 921** | **15/05/2024 à 10:13:58.078072** | Action **Quarantaine**, erreur `0x00000000`, opération déclarée réussie. |

Le fichier désigné est **`AppleID-977451TLU5I[58342].pdf`**, sous le cache de pièces jointes de l’application Windows de courrier. Le chemin de détection mentionne aussi un objet `PdfUri:0000`. Le libellé est une classification du moteur Defender ; le processus rapporté ne prouve pas l’exécution d’un programme malveillant ou l’ouverture d’un lien par la cliente.

Le PDF n’est plus présent à ce chemin et les dossiers de quarantaine ne contiennent aucun fichier dans l’image. Il n’a pas été retrouvé comme document récupérable. La recherche ciblée du fragment `AppleID-977451` dans le MBOX Takeout et les **5 875 messages MIME décodés des deux PST** ne le retrouve pas. Le résultat ne couvre pas un renommage, tous les encodages ou toutes les pièces jointes compressées, ni une messagerie disparue.

**L’exposition à un document détecté comme phishing est établie, avec mise en quarantaine déclarée réussie. Une compromission du PC, un vol d’identifiants ou une exfiltration consécutive ne sont pas démontrés.** Le succès de la remédiation n’exclut pas une consultation antérieure ou des actions hors de la détection conservée.

Les changements Defender examinés, dont des bascules rapides de paramètres `DisableBmNetworkSensor`, ne suffisent pas à identifier une désactivation malveillante ou une intervention humaine. Leur attribution exhaustive à des processus n’est pas établie.

### 9.2. Indices de téléassistance Rescue

Un raccourci du profil `fintm` contient une URL vers **`secure.logmeinrescue.eu/R`**, avec un code de session non reproduit ici. Sa modification NTFS est datée du **6 octobre 2023 à 12:40:41 Paris**. La chaîne du domaine est lisible dans les octets du fichier, indépendamment de son nom.

Les PST contiennent aussi **deux invitations Sage Assistance**, datées des **4 juillet et 14 novembre 2022**, proposant une connexion distante via un expéditeur déclaré du domaine `LogMeInRescue.com`. Le champ expéditeur ne certifie pas à lui seul l’authenticité du message.

Ces éléments constituent des **indices de recours possible à la téléassistance**. Ils ne prouvent ni une session effectivement établie, ni un contrôle distant, ni l’identité du technicien, ni le caractère autorisé de l’intervention. Les messages de 2022 ne sont pas reliés techniquement au raccourci de 2023. Aucun binaire ou lancement LogMeIn pertinent n’est identifié dans Amcache, Prefetch et UserAssist ; les occurrences Norton `RescueDisk` ne désignent pas LogMeIn Rescue.

### 9.3. Accès réseau, outils distants et persistance

Les recherches croisent registre, logiciels, **1 549 entrées Amcache**, **264 tâches**, services, événements, traces d’exécution, navigation et noms conservés dans toute la MFT. Les résultats sont les suivants :

| Axe | Résultat | Limite |
|---|---|---|
| Outils distants et de transfert ciblés | Aucun faisceau établissant l’installation ou le lancement d’AnyDesk, TeamViewer, RustDesk, VNC, ScreenConnect, Radmin, Splashtop, RemotePC, DWAgent, MeshAgent, NetSupport, ngrok, rclone, WinSCP ou FileZilla. | Recherche par noms et artefacts conservés, sans détection universelle de logiciels renommés ou inconnus. |
| RDP | Pas d’historique de serveurs dans Terminal Server Client pour `fintm`/`INVITES` ; `fDenyTSConnections=1` dans l’état acquis ; journaux RemoteConnectionManager/RDPClient présents mais vides. | L’état acquis ne certifie pas celui de 2024 et une téléassistance peut utiliser une session locale. |
| Sessions antérieures | **316 événements 21/22** sélectionnés portent `Address=LOCAL`. | Ne prouvent pas une connexion RDP distante ; n’excluent pas d’autres outils de contrôle. |
| Services | **180 installations 7045** antérieures sélectionnées ; aucun nom d’outil distant ciblé identifié. | Les signatures et octets de tous les services/pilotes ne sont pas validés exhaustivement. |
| Tâches et PowerShell | Pas d’outil ciblé dans les actions des 264 tâches ; **23 blocs 4104** antérieurs conservés de diagnostic Windows. | Des tâches supprimées ou des commandes non journalisées peuvent manquer. |
| WinRM | Énumérations et échecs de connexion ; aucun accès distant réussi et attribuable établi. | Sélection limitée aux événements conservés. |
| Navigation | Cinq visites ciblées vers l’assistance Free le 08/11/2021 ; pas de domaine ciblé de téléassistance/transfert dans la sélection. | Historique très clairsemé ; les 82 références de téléchargement examinées ne constituent pas un audit complet. |
| Démarrages automatiques | Présence notamment de Dropbox, OneDrive, NordVPN, Adobe, Teams, PaperCut et Norton. | La présence d’un client cloud ou d’un VPN ne démontre ni intrusion ni transfert d’un fichier déterminé. |

Deux événements **SMBServer 551**, les records 1 et 2, consignent des **échecs d’authentification** depuis **`192.168.1.139`**, le **26 mars 2024 à 15:20:36 et 15:21:12 Paris**, statut `0xC000006D`. L’inventaire Freebox associe cette IP à **`LAPTOP-205Q5H9C`**, MAC **`F8:28:19:77:42:71`**, actif le même jour. Il s’agit d’un candidat plausible, sans historique de bail garantissant cette attribution aux secondes exactes des tentatives. Ces échecs ne prouvent ni accès réussi, ni origine malveillante, ni exfiltration.

Le parcours du registre complet et des journaux de stockage ne rattache pas non plus à OP-01 le traitement Windows observé sur les cartes SD le 12 novembre 2024. L’absence de correspondance n’exclut pas ce PC, compte tenu des rotations et pertes d’historique.

### 9.4. Transferts réseau et caches cloud

La table réseau SRUM ne conserve que des lignes de **septembre–octobre 2026**. Les 127 lignes historiques d’énergie de 2021–2024 ne renseignent ni destinations réseau ni fichiers transmis. **Aucun volume d’octets envoyés ou reçus en 2024 ne peut être chiffré à partir de cette base.**

Le triage des caches cloud comprend neuf bases SQLite OneDrive et les compagnons disponibles. Il ne retrouve pas de ligne cible sur les noms L16B, archive/inventaire ou le volume Kingston. Les tentatives de lecture d’anciens ODL ne restituent pas de transferts de 2024. Ces résultats n’équivalent pas à un audit exhaustif de OneDrive, Dropbox ou de leurs usages web ; les historiques de sécurité des comptes et les journaux serveur ne sont pas disponibles.

Le nom de réseau **`ASUS_Z01RD`** conservé dans TP-02 ne permet pas d’identifier OP-01 comme point d’accès. Aucun lien technique positif ne transforme les traces Wi-Fi des téléphones en preuve de fonctionnement d’OP-01 pendant l’intervalle de rétention.

**Aucune chaîne complète exposition à une menace → prise de contrôle → transfert de données n’est reconstruite. L’absence de preuve de compromission ne permet pas d’affirmer que le PC n’a jamais été compromis.**

## 10. Limites générales et questions non résolues

### 10.1. Ce que les sources ne permettent pas de conclure

L’acquisition intervient près de deux ans après les faits, avec utilisation ultérieure du PC et interventions de préparation à l’acquisition. Les fichiers de mémoire `hiberfil.sys`, `pagefile.sys` et `swapfile.sys` portent des dates récentes et ne fournissent pas ici de mémoire historique de 2024. Security, USN et les compteurs réseau ne couvrent plus la période recherchée. Les données encore conservées ne constituent donc pas un historique exhaustif du système.

Les contrôles de structure, CRC, empreintes et compteurs vérifient des propriétés des pièces analysées. Ils ne permettent pas d’exclure une réécriture cohérente, une horloge erronée, une modification hors ligne, une lecture externe du SSD ou une trace définitivement écrasée. Les dates SI/FN peuvent être conservées lors de copies, restaurées ou manipulées ; les dernières valeurs de registre ne reconstituent pas toutes les valeurs antérieures.

Aucun compte local, nom de logiciel, numéro de volume ou rapprochement horaire ne suffit à identifier une personne ou à qualifier juridiquement son action. L’état matériel des scellés nécessite ses propres éléments de conservation et de procédure.

### 10.2. Examens dont les résultats restent limités

Les contrôles ne constituent pas un audit exhaustif des binaires, signatures, mécanismes de persistance, caches cloud ou formats propriétaires. L’analyse détaillée de ShimCache, la reconstruction de mémoire historique et le carving intégral de l’espace non alloué ne sont pas réalisés. Aucun scan antivirus exécuté sur le système acquis, aucune restauration de quarantaine et aucune restauration de cliché VSS ne sont présentés comme obtenus.

Les récupérations de fichiers portent sur une sélection explicite ; une lecture techniquement réussie ne certifie pas l’identité historique d’octets issus de clusters réutilisés.

Les notes de remise et d’acquisition comportent des divergences de dates ou de fuseaux qui restent documentées dans les pièces sources. Elles ne sont pas résolues par une reconstruction supposée et ne permettent pas de recalibrer l’horloge du PC en 2024.

### 10.3. Pièces nécessaires pour départager les questions ouvertes

| Question | Éléments nécessaires |
|---|---|
| Quels fichiers ont été définitivement saisis ? | CD d’inventaire, liste et empreintes finales, archive/support emporté et liste des rejets, comparés à L16B et aux contenus récupérés. |
| Quel support correspond à chaque opération ? | Identification physique ou images des trois Kingston, correspondance avec le volume `140B8328`, journaux d’outils et relevés de branchements disponibles. |
| Quelle est l’origine exacte des ensembles cloud et téléphones ? | Historiques de téléchargement/export et de sécurité des comptes, états historiques authentifiables, rapprochement des contenus avec les appareils et sauvegardes. |
| Une téléassistance a-t-elle réellement eu lieu ? | Pièces d’assistance Sage/Rescue, traces de session ou journaux du prestataire ; message et PDF d’origine pour la piste phishing. |
| Une intervention a-t-elle précédé l’ouverture des scellés ? | Heures individuelles de fermeture, documents de conservation, mouvements et interventions, éléments contemporains d’alimentation ou d’accès. |

Ces pièces ne sont pas présumées disponibles. Leur absence ne doit être remplacée ni par une attribution certaine ni par une hypothèse présentée comme un fait.

## 11. Conclusion technique

**OP-01 a repris Windows le 15 octobre 2024 vers 10:43, puis est entré en hibernation vers 10:53. La reprise suivante conservée est celle du 28 à 10:41:56, cohérente avec l’ouverture du PC à 10:41 consignée au PV. Aucune activité Windows intermédiaire corroborée n’est établie.** Le réveil du 16 à 05:51 est seulement programmé ; les dates iCloud et les dates SI anciennes de certains fichiers ne démontrent pas un fonctionnement local pendant l’intervalle.

Après l’ouverture du 28, les journaux, traces d’exécution, métadonnées, Jump Lists et contenus récupérés établissent des opérations sur les messageries et documents. Le regroupement L16B et les formats d’exports concordent substantiellement avec les opérations décrites par l’administration. Les trois identifiants Kingston et les références à l’archive, l’inventaire et les rejets fournissent des cibles précises de vérification, sans certifier le contenu définitivement emporté.

Les dix mises à la corbeille du 28 sont établies. L’archive de 94 fichiers et le document de gestion de mots de passe restent récupérables ; les 93 autres contenus correspondent exactement au dossier GDRIVE. Le texte des deux factures du PDF supprimé subsiste dans le PDF Sage. **Ces constats ne démontrent ni effacement sécurisé, ni destruction malveillante, ni auteur identifié.**

Aucun indice probant d’effacement volontaire des journaux destiné à masquer une activité, de compromission réussie ou d’exfiltration clandestine antérieure à la perquisition n’est établi. La détection de phishing de mai 2024 et les indices Rescue justifient des rapprochements complémentaires, sans constituer une preuve de prise de contrôle. La conservation partielle des traces empêche toute garantie d’absence historique de manipulation ou de compromission.

## 12. Pièces techniques et références

### 12.1. Sources permettant de contrôler les constats

Les pièces techniques restent conservées avec leurs scripts, sorties, erreurs et empreintes. Les scripts et journaux associés permettent d’en reproduire les contrôles.

| Domaine | Pièces de référence |
|---|---|
| Acquisition et environnement | [Journal d’acquisition](recherche-OP-01/environnement-acquisition.txt), [environnement EVTX](recherche-OP-01/integrite-evtx/environnement.txt) |
| Événements et couverture | [Inventaire et empreintes des sources](recherche-OP-01/inventory.json), [événements JSONL](recherche-OP-01/events.jsonl), [chronologie CSV](recherche-OP-01/chronologie.csv), [comptages](recherche-OP-01/summary.json), [rejets XML](recherche-OP-01/xml-errors.jsonl) |
| Minuteur de réveil | [Synthèse](recherche-OP-01/reveil-16oct/summary.json), [tâches](recherche-OP-01/reveil-16oct/tasks-inventory.json), [mentions de l’échéance](recherche-OP-01/reveil-16oct/due-time-mentions.json), [recherche dans les ruches](recherche-OP-01/reveil-16oct/hive-due-time-search.json) |
| Structure et récupération EVTX | [Structure](recherche-OP-01/integrite-evtx/structure-summary.json), [blocs et CRC](recherche-OP-01/integrite-evtx/chunks.jsonl), [récupération](recherche-OP-01/integrite-evtx/recovery-summary.json), [fragments décodés](recherche-OP-01/integrite-evtx/recovered-complete.jsonl), [audit et effacements](recherche-OP-01/integrite-evtx/clear-and-audit-complete.jsonl) |
| Artefacts indépendants | [Sources et empreintes](recherche-OP-01/integrite-evtx/independent/sources.json), [résultats](recherche-OP-01/integrite-evtx/independent/results.jsonl) |
| MFT, USN, VSS | [Synthèse MFT](recherche-OP-01/integrite-evtx/ntfs/mft-summary.json), [entrées de l’intervalle central](recherche-OP-01/integrite-evtx/ntfs/mft-gap-records.jsonl), [USN](recherche-OP-01/integrite-evtx/ntfs/usn-summary.json), [recoupement iCloud](recherche-OP-01/integrite-evtx/ntfs/usn-cloud-summary.json), [catalogue VSS](recherche-OP-01/integrite-evtx/ntfs/vss-catalog-summary.json) |
| Anciennes entrées EVTX | [Récupération](recherche-OP-01/integrite-evtx/ntfs/deleted-evtx-summary.json), [correspondances de blocs](recherche-OP-01/integrite-evtx/ntfs/deleted-chunk-correspondence.json) |
| L16B, exports et supports | [Inventaire L16B](recherche-OP-01/extractions-acces/l16b-inventory.json), [MFT de L16B](recherche-OP-01/extractions-acces/l16b-mft.jsonl), [archives](recherche-OP-01/extractions-acces/archives.json), [sections SetupAPI](recherche-OP-01/extractions-acces/setupapi-usb-sections.json), [volumes et points de montage](recherche-OP-01/extractions-acces/usb-mounteddevices-crosscheck.json) |
| PST et Jump Lists | [Compte rendu et contrôles détaillés](recherche-OP-01/operations-28oct/compte-rendu.md) |
| Recoupements réseau, PST, ZIP et décodage `$LogFile` | [Compte rendu transversal](../investigations/20261017-recroisements/compte-rendu.md) |
| Fichiers supprimés | [Synthèse](recherche-OP-01/fichiers-supprimes/summary.json), [sélection](recherche-OP-01/fichiers-supprimes/recovery-selection.jsonl), [récupérations](recherche-OP-01/fichiers-supprimes/recovery-results.jsonl), [paires de corbeille](recherche-OP-01/fichiers-supprimes/recycle-pairs.json), [comparaison Drive](recherche-OP-01/fichiers-supprimes/drive-content-comparison.json), [contre-lecture icat](recherche-OP-01/fichiers-supprimes/icat-crosscheck.txt) |
| Menaces et traces d’accès | [Sources contrôlées](recherche-OP-01/extractions-acces/source-verification.json), [quarantaine](recherche-OP-01/extractions-acces/quarantine-inventory.json), [recherche ciblée dans le MBOX](recherche-OP-01/extractions-acces/mbox-pdf-name-search.json), [SRUM](recherche-OP-01/extractions-acces/additional/srum-schema.json) |
| Procès-verbal et copie finale | [Lecture du PV](../investigations/20261108-analyse-pv/compte-rendu.md), [concordance technique de L16B](../investigations/20261109-controle-l16b-photos/compte-rendu.md) |
| Téléphones et intervention avant ouverture | [Rapprochements des téléphones](../investigations/20261110-telephones/compte-rendu.md), [comparaison des hypothèses](../investigations/20261110-revue-intervention-scelles/compte-rendu.md) |

### 12.2. Références de formats et d’interprétation

Ces références étayent les formats et principes utilisés ; les constats propres à OP-01 proviennent des pièces ci-dessus.

- Microsoft : [états d’alimentation Windows](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-system_power_state), [WakeToRun](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-waketorun-settingstype-element), [maintenance automatique](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence).
- Microsoft : [événement 4624 et types de session](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624), [effacement du journal Security, 1102](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-1102), [événements et remédiation Defender](https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus).
- libyal : [format EVTX](https://github.com/libyal/libevtx/blob/main/documentation/Windows%20XML%20Event%20Log%20%28EVTX%29.asciidoc), [format NTFS](https://github.com/libyal/libfsntfs/blob/main/documentation/New%20Technologies%20File%20System%20%28NTFS%29.asciidoc), [format VSS](https://github.com/libyal/libvshadow/blob/main/documentation/Volume%20Shadow%20Snapshot%20%28VSS%29%20format.asciidoc), [tables SRUM](https://github.com/libyal/esedb-kb/blob/main/documentation/System%20Resource%20Usage%20Monitor%20%28SRUM%29.asciidoc).
- Sleuth Kit : [fls](https://www.sleuthkit.org/sleuthkit/man/fls.html) et [icat](https://www.sleuthkit.org/sleuthkit/man/icat.html).
- Formats et contrôles statiques : [corbeille Windows, RBCmd](https://github.com/EricZimmerman/RBCmd) comme référence de format, [PDFiD](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pdfid.py), [journaux OneDrive ODL](https://github.com/ydkhatri/OneDrive/blob/main/odl.py).

### 12.3. Termes techniques

| Terme | Sens et usage dans ce rapport |
|---|---|
| Artefact | Trace conservée par un système ou une application : événement, clé de registre, raccourci, métadonnée ou contenu de fichier. Sa présence et sa portée doivent être interprétées selon son origine. |
| EWF | Format de l’image d’acquisition. Les segments permettent de reconstituer le flux du disque analysé. |
| EVTX / RecordID | Fichier de journal Windows / numéro d’enregistrement propre à ce journal. Un même numéro dans deux journaux ne désigne pas le même événement. |
| CRC / SHA-256 | Contrôle de cohérence d’une structure / empreinte utilisée pour comparer des contenus. Un résultat valide ou identique ne désigne pas leur auteur et ne certifie pas leur provenance historique. |
| MFT / SI / FN | Table NTFS des fichiers / attributs STANDARD_INFORMATION et FILE_NAME. Leurs dates décrivent des métadonnées distinctes, sans constituer un journal complet des actions. |
| Alloué / non alloué | Espace ou entrée actuellement utilisé / libéré dans le système de fichiers. Un ancien contenu non alloué peut être partiellement ou entièrement remplacé. |
| Prefetch / UserAssist | Traces Windows utilisées pour rechercher des lancements de programmes. Leur conservation est limitée ; elles ne prouvent pas à elles seules un geste humain. |
| LNK / Jump Lists | Raccourcis / listes de destinations mémorisées par Windows et les applications. Ils peuvent conserver des chemins et des métadonnées sans que la cible soit encore accessible. |
| Amcache | Inventaire d’applications et de fichiers. Une présence dans cet inventaire ne prouve pas à elle seule une exécution. |
| USN / `$LogFile` | Journaux NTFS de changements et d’opérations internes. Leurs données conservées ne couvrent ici que des périodes récentes, malgré d’éventuelles dates de fichiers plus anciennes embarquées. |
| VSS | Mécanisme de clichés de volume pouvant conserver des états antérieurs. Aucun contenu de cliché n’est récupéré dans cette analyse. |
| PST / EML / MBOX | Conteneur Outlook / fichier de message / conteneur de messages. Les dates des messages sont distinctes de celles d’export ou de copie de ces fichiers. |
| SRUM | Base Windows de statistiques d’utilisation des ressources. Chaque table a sa propre couverture temporelle ; des données d’énergie anciennes n’impliquent pas des données réseau de la même période. |
| Exfiltration | Transfert de données vers un destinataire extérieur dans un contexte de compromission. Un regroupement local ou un export ne suffit pas à l’établir. |
