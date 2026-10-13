# Analyse informatique de l’ordinateur OP-01

**Affaire :** SADEDINE-2026

**Cliente :** Mme Malika Sadedine — DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev — christophe@donnat.dev

**Début des interventions :** 8 octobre 2026

**Acquisition :** 12 octobre 2026

**Investigations décrites :** état des travaux au 13 octobre 2026

**Périmètre de cette version :** allumage et utilisation pendant la rétention du 15 au 28 octobre 2024 ; recherche de traces d’effacement ; exports/copies de données et indices de compromission antérieure à la perquisition, avec examen des traces encore conservées depuis 2021/2022.

## 1. Synthèse des conclusions

**Les éléments examinés sont cohérents avec une hibernation d’OP-01 du 15 octobre 2024 vers 10 h 53 jusqu’au 28 octobre vers 10 h 41, heure de Paris. Aucune activité Windows corroborée n’a été retrouvée dans l’intervalle technique central défini ci-dessous. Cela ne prouve pas que l’ordinateur n’a subi aucune manipulation pendant sa rétention.**

| Question | Réponse étayée par les investigations | Limite à conserver |
|---|---|---|
| Le PC a-t-il fonctionné le jour de la saisie ? | Oui : reprise le **15/10 à 10 h 43**, activité Windows et session locale, puis hibernation vers **10 h 53**. | L’heure de fermeture effective des scellés n’est pas connue ; cette activité ne peut pas être positionnée précisément par rapport au scellement. |
| A-t-il repris Windows entre cette hibernation et l’ouverture déclarée ? | **Aucune trace corroborée retrouvée** entre le **15/10 à 10:53:09** et le **28/10 à 10:22**, selon les horodatages conservés. | Les journaux ne couvrent pas toutes les opérations possibles, notamment hors ligne ou sur un autre système. |
| A-t-il été utilisé le 28 avant restitution ? | Oui : reprise à **10:41:56**, puis indices forts d’interaction dans Outlook, corroborés par des exécutions et des traces de session. | Cette activité est postérieure à l’ouverture déclarée à 10:22 ; elle ne démontre pas une utilisation antérieure à l’ouverture. |
| La date du 16/10 à 05:51:07 prouve-t-elle un réveil ? | Non : c’est une **échéance programmée sur secteur** présente dans un événement enregistré le 15. | Le moment où ce minuteur a été défini ou armé et son demandeur ne sont pas établis. |
| Des journaux ont-ils été effacés ou falsifiés pour masquer une activité ? | **Aucun indice probant établi** : pas d’événement explicite d’effacement retrouvé, CRC et séquences conservées cohérents. | Des anomalies d’en-tête existent ; des traces anciennes peuvent être perdues. Une réécriture cohérente ne peut pas être exclue. |
| Existe-t-il des dates de fichiers pendant la rétention ? | Oui : **3 461 entrées MFT** portent au moins une date dans l’intervalle central, dans iCloud Photos ou `L16B`. | Ces dates ne constituent pas une preuve autonome d’allumage : divergences SI/FN, copies possibles et changements de métadonnées ultérieurs. |
| Peut-on identifier l’opérateur ? | Non. Le compte local observé est **`fintm`**. | Un compte, un nom de logiciel ou une concordance horaire n’identifie pas la personne qui opérait le PC. |

**Seconde étape — données et compromission (§ 10) :** `L16B` contient 4,64 Go de fichiers, dont des archives d’export ; 1 555 créations FN sont datées du 28/10/2024. Trois supports Kingston apparaissent dans les anciens journaux ce jour-là. Une détection de PDF de phishing le 15/05/2024, suivie d’une quarantaine déclarée réussie, et un raccourci Rescue daté du 06/10/2023 constituent des pistes antérieures. **Aucune compromission réussie ni exfiltration antérieure à la perquisition n’est établie.**

Cette analyse informatique privée ne détermine ni l’intégrité matérielle des scellés, ni le caractère autorisé d’une intervention. La confrontation avec les procès-verbaux reste nécessaire.

## 2. Sources, équipement et chronologie déclarée

### 2.1. Sources documentaires et techniques

Les demandes et dates communiquées par la cliente figurent dans [le mail](../docs/mail.txt). L’identification officielle de l’équipement et les conditions de remise figurent dans [l’attestation de remise](../remise-documents/attestation-de-remise.md), datée du **06/10/2026**, qui prévoit une restitution au plus tard le **06/11/2026**.

Les constats techniques proviennent de l’image disque OP-01, du fichier d’acquisition **`OP01.info`**, des journaux Windows, des tâches planifiées, des ruches de registre et des métadonnées du système de fichiers. Les commandes, scripts, sorties brutes et empreintes sont conservés sous [recherche-OP-01](recherche-OP-01/). Le présent document expose les résultats et leur méthode ; ces pièces permettent d’en contrôler le détail.

Les procès-verbaux de saisie, fermeture et ouverture des scellés n’ont pas été vérifiés dans cette analyse. Les horaires du mail sont donc des **déclarations de la cliente**, distinctes des horodatages techniques.

### 2.2. Identification d’OP-01

| Élément | Identification |
|---|---|
| Équipement | ASUS UX333F NOTEBOOK PC — **OP-01** |
| Numéro de série du portable | **KAN0CV116290436** |
| Système indiqué dans l’attestation | Windows 11 version 23H2 x64 ; cette indication de 2026 n’établit pas à elle seule la version installée en octobre 2024. |
| Nom Windows observé dans les événements | **LAPTOP-RMCOB2VU** |
| Compte local observé | **fintm** ; SID associé dans System : `S-1-5-21-1394434332-468722268-2897565647-1001` |
| Processeur observé lors de l’intervention du 08/10/2026 | Intel Core i7-8565U CPU @ 1.80 GHz |
| Support acquis | SSD NVMe **INTEL SSDPEKNW512G8**, série **BTNH93120FL8512A** — identifiant distinct de celui du portable |

Les logiciels mentionnés à la remise comprennent Sage 50, Ciel Paye Evolution, Adobe Reader/Acrobat, Word, Excel, Outlook, OpenOffice 4.1.11, Microsoft Teams, Oodrive Sign, PaperCut MF Client et Norton 360. Leur présence ne prouve pas leur utilisation pendant la période étudiée.

### 2.3. Dates déclarées et fenêtres d’examen

| Événement déclaré | Date et heure de Paris | Précision |
|---|---|---|
| Perquisition fiscale | **15/10/2024** | Date corrigée par la cliente ; ne pas retenir le 14. |
| Perte d’accès au PC | Dès le début de la perquisition | Heure exacte et heure de fermeture des scellés non fournies. |
| Perte d’accès aux téléphones | 15/10 vers 13:30 | Déclaration concernant les téléphones, pas une borne de saisie du PC. |
| Début de l’ouverture des scellés | **28/10 vers 10:22** | Dans les locaux de l’administration ; horaire approximatif. |
| Récupération des appareils | **28/10 vers 19:20** | Horaire approximatif. |

Deux fenêtres sont utilisées :

- **Fenêtre élargie :** du 14 au 29 octobre inclus en date civile française, soit **`[2024-10-13T22:00:00Z ; 2024-10-29T23:00:00Z[`**. Elle inclut les jours adjacents pour les recoupements.
- **Intervalle technique central :** **`[2024-10-15T08:53:09Z ; 2024-10-28T09:22:00Z[`**, soit le 15 à 10:53:09 jusqu’au 28 à 10:22 à Paris. Son début est situé après la dernière séquence Windows connue du 15 ; **ce n’est pas une heure de scellement démontrée**.

Les événements du 15 avant l’hibernation et ceux du 28 après l’ouverture déclarée sont analysés séparément. Toutes les dates UTC originales sont conservées. Les conversions utilisent **`Europe/Paris`**, UTC+2 le 15 et UTC+1 le 28, après le changement d’heure du 27 octobre. L’horloge du PC n’a pas été calibrée contre une source externe.

## 3. Interventions de 2026 et acquisition de l’image

### 3.1. Interventions consignées sur le matériel

Les notes d’intervention mentionnent une remise le **07/10/2026 à 16:15**, avec alimentation et codes d’accès, alors que l’attestation est datée du **06/10/2026**. Cette divergence documentaire n’est pas résolue ici.

| Intervention consignée | Horaire inscrit dans les notes | Opération |
|---|---|---|
| 08/10/2026 | 12:36 | Allumage par le prestataire, récupération de la clé BitLocker et vérification du système ; commandes `Get-CimInstance Win32_Processor` et `msinfo32`. |
| 12/10/2026 | Vers 08:55 | Redémarrage et désactivation du Secure Boot dans le BIOS. |
| 12/10/2026 | Vers 08:57 | Démarrage sur un SSD externe contenant Caine/Linux. |
| 12/10/2026 | Vers 09:15 | Acquisition avec Guymager, support source annoncé en lecture seule, sauvegarde sur une partition externe de 1 To notée « FORENSOC ». |
| 12/10/2026 | Vers 11:20 | Notes indiquant réactivation du Secure Boot, redémarrage et remise en service de BitLocker ; détail des opérations sur les protecteurs non consigné. |

Ces horaires de notes ne sont pas tous associés à un fuseau explicitement confirmé. **Ils ne sont pas entièrement raccordés aux horaires automatiques de Guymager** exposés ci-dessous. Ils sont conservés sans réécriture supposée de la chronologie. Les interventions sous Windows de 2026 peuvent produire des traces récentes et contribuer à la rotation des journaux ; elles ne sont pas attribuées aux faits de 2024.

La clé BitLocker n’est pas reproduite dans ce rapport. Elle doit être disponible séparément pour reproduire le déchiffrement. Elle figurait dans une version antérieure du document ; son retrait de la version courante n’efface pas les anciennes copies.

La capture de contrôle du système est conservée : [OP-01-2.jpg](images/OP-01-2.jpg).

### 3.2. Acquisition et vérification Guymager

| Paramètre | Valeur enregistrée |
|---|---|
| Logiciel | **Guymager 0.8.13-1**, machine Caine |
| Source | `/dev/nvme0n1`, SSD identifié en § 2.2 |
| Taille | **512 110 190 592 octets**, **1 000 215 216 secteurs de 512 octets** |
| Format | EWF, format EnCase 6 indiqué par `ewfinfo`, compression deflate |
| Dossier et pièce | SADEDINE-2026 / OP-01 ; examinateur Christophe Donnat |
| Image | **74 segments `OP01.E01` à `OP01.E74`**, avec `OP01.info` |
| Chemin initial dans Caine | `/media/sda3/OP-01/OP01.Exx` |
| Chemin dans SIFT | **`/media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01`** |
| État | Acquisition terminée avec succès ; aucun mauvais secteur rencontré. |
| Vérification image | **Activée et réussie** : « Image verification OK ». |
| Seconde vérification de la source | **Désactivée** : `Source verification : off`, champs « verified source » non renseignés. |

Empreintes du flux disque calculées pendant l’acquisition, puis retrouvées identiques lors de la vérification de l’image :

```text
MD5     10c9f3df1ecd999567a05beaa4056ace
SHA-256 0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484
```

Ces valeurs ne sont pas les empreintes individuelles des fichiers segments. Guymager indique que le calcul MD5 par segment était désactivé. La correspondance acquisition/image ne constitue pas une seconde relecture de contrôle du disque source.

Les horaires automatiques sont : début acquisition **12/10/2026 10:21:57**, début vérification **11:20:34**, fin **12:04:26**, dans le journal Guymager. Sa sortie SMART indique **BST** ; si le même fuseau s’applique à ces trois horaires, ils correspondent respectivement à **09:21:57, 10:20:34 et 11:04:26 UTC**, donc **11:21:57, 12:20:34 et 13:04:26 à Paris**. `ewfinfo` affiche le début à **09:21:57**, cohérent avec cette conversion. Ce rapprochement ne résout pas les horaires approximatifs des notes du § 3.1.

La sortie SMART conservée annonce notamment : santé **PASSED**, avertissement critique 0, 924 cycles d’alimentation, 2 202 heures sous tension, 13 arrêts non sûrs et 0 erreur de média/intégrité. Ces compteurs cumulés ne datent pas une utilisation en octobre 2024.

Le journal complet d’acquisition est repris dans [environnement-acquisition.txt](recherche-OP-01/environnement-acquisition.txt). **Aucune nouvelle vérification complète par `ewfverify` n’a été exécutée pendant ces investigations.** La vérification de 2026 à l’acquisition ne contrôle pas une altération ultérieure des segments.

## 4. Environnement SIFT, accès et préservation

L’analyse est réalisée dans une VM **SIFT Workstation**, depuis l’hôte Ubuntu. L’alias SSH `sift` observé sur l’hôte vise `127.0.0.1`, port `2222`, utilisateur `sansforensics`. Une VM Windows 11/Autopsy est disponible mais n’a pas été utilisée pour les investigations présentées ici.

| Outil sur SIFT | Version relevée |
|---|---|
| `ewfinfo` | 20140816 |
| `evtxexport`, `evtxinfo`, `pyevtx` | 20251118 |
| Python | 3.12.3 |
| `pyfsntfs` | 20251028 |
| `pyregf` | 20240421 |
| `pyscca` | 20250915 |
| `pylnk` | 20240423 |
| SQLite | 3.45.1 |
| `vshadowinfo` | 20240504 |

Aucune dépendance installée pendant l’analyse. Le module `python-evtx` n’était pas présent ; la lecture EVTX utilise **libevtx/pyevtx**, un outil différent. Les contrôles de versions et de montages sont conservés dans [environnement-acquisition.txt](recherche-OP-01/environnement-acquisition.txt) et [integrite-evtx/environnement.txt](recherche-OP-01/integrite-evtx/environnement.txt).

### 4.1. Structure du disque et chaîne de lecture

`mmls` identifie une table GPT :

| Partition GPT | Secteur de départ | Taille approximative | Identification |
|---|---:|---:|---|
| 000 | 2 048 | 260 Mio | EFI System |
| 001 | 534 528 | 16 Mio | Microsoft Reserved |
| 002 | **567 296** | 475,84 Gio | Partition Windows, BitLocker version 2 |
| 003 | 998 473 728 | 848 Mio | NTFS, probable partition de récupération |

Offset de la partition Windows : **567 296 × 512 = 290 455 552 octets**. La chaîne utilisée est :

```text
OP01.E01 … OP01.E74
  → ewfmount : /mnt/ewf/ewf1 (vue du disque physique)
  → loop en lecture seule : /dev/loop14, partition /dev/loop14p3
  → dislocker -r : /mnt/dislocker/dislocker-file (vue NTFS déchiffrée)
  → ntfs-3g -o ro,norecover : /mnt/windows
```

Le numéro **loop14 est celui observé**, pas un identifiant permanent. `dislocker-file` est une vue virtuelle d’environ 477 Go, pas une copie supplémentaire. Sa date du 01/01/1970 ne date pas une utilisation du PC.

Les montages montrent `/mnt/windows` en **ro**, le loop avec **RO=1**, et Dislocker lancé avec **`-r`**. Les façades FUSE `/mnt/ewf` et `/mnt/dislocker` apparaissent en `rw` dans `findmnt` : le contrôle ne doit pas se limiter à ces libellés, mais inclure le loop, les options de Dislocker et le montage NTFS.

**Limite réelle : `/media/shared`, qui héberge les segments originaux, est monté en `rw`.** Il ne constitue pas un blocage d’écriture des fichiers d’acquisition. Aucune commande de ces investigations n’y écrit ; les analyses portent sur les vues protégées et les exports sont séparés. Pour une reproduction, protéger également ce support en lecture seule lorsque l’environnement le permet.

Les fichiers `hiberfil.sys` (~7,9 Gio), `pagefile.sys` (~5,3 Gio) et `swapfile.sys` (~16 Mio) sont présents avec des dates récentes du 12/10/2026. Leur contenu n’a pas été analysé pour reconstituer une mémoire historique de 2024.

### 4.2. Reconstituer le montage si nécessaire

**Les commandes de cette section sont à exécuter dans SIFT.** Depuis l’hôte, ouvrir une session interactive :

```bash
ssh -t -F /home/chris/.ssh/config sift
```

L’option `-F` utilise explicitement la configuration utilisateur : la commande simple `ssh sift` rencontrait une erreur de permissions sur un fichier SSH système de l’hôte. Aucun fichier de configuration n’a été modifié.

Vérifier l’état avant de recréer un montage :

```bash
findmnt /media/shared
findmnt /mnt/ewf
findmnt /mnt/dislocker
findmnt /mnt/windows
sudo losetup -l
sudo ls /mnt/windows/Windows/System32/winevt/Logs/System.evtx
```

**Ne pas relancer les étapes déjà en place.** Pour une chaîne absente, les commandes essentielles utilisées sont :

```bash
sudo mkdir -p /mnt/ewf /mnt/dislocker /mnt/windows
sudo ewfmount /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01 /mnt/ewf
sudo mmls /mnt/ewf/ewf1
sudo blkid -p -O 290455552 /mnt/ewf/ewf1

OP01_LOOP=$(sudo losetup -fP --read-only --show /mnt/ewf/ewf1)
sudo lsblk -o NAME,SIZE,FSTYPE,RO,TYPE,MOUNTPOINT "$OP01_LOOP"
sudo dislocker -r -V "${OP01_LOOP}p3" -p -- /mnt/dislocker
sudo mount -t ntfs-3g -o ro,norecover \
  /mnt/dislocker/dislocker-file /mnt/windows
findmnt /mnt/windows
sudo losetup -l "$OP01_LOOP"
```

Le déchiffrement requiert la clé BitLocker, saisie **au prompt interactif**, sans l’ajouter à la ligne de commande, au rapport ou aux journaux. Le déchiffrement initial avait terminé avec un code retour 0.

Pour lire les métadonnées et, éventuellement, faire une nouvelle vérification EWF :

```bash
ewfinfo /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01
# Contrôle complémentaire proposé ; non exécuté dans les travaux rapportés :
sudo ewfverify /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01
```

## 5. Investigations sur les événements Windows et les sessions

### 5.1. Méthode, couverture et qualité des exports

Répertoire source : **`/mnt/windows/Windows/System32/winevt/Logs/`**, **359 fichiers EVTX**. Une première lecture texte de System avait trouvé **774 événements sur les dates UTC du 15 au 28 inclus**, dont 80 le 15 et 694 le 28. Ce résultat exploratoire a été remplacé par le contrôle structuré des 359 journaux avec les bornes françaises du § 2.3 ; il ne doit pas être confondu avec les comptages finaux.

Chaque EVTX a été lu par **`evtxexport -f xml`**, en mode par défaut **items**, donc enregistrements alloués. Extraction du fournisseur, de l’Event ID, de la version, de l’**EventRecordID**, de `TimeCreated/@SystemTime` et des données nommées `EventData`/`UserData`. Un RecordID est propre à un journal ; le rapport l’accompagne toujours du journal et du fournisseur.

**275 577 enregistrements alloués** ont été contrôlés : 274 638 exports XML interprétés et 939 rejetés par le parseur XML. Les rejets ont été conservés puis relus séparément dans les neuf journaux concernés. Tous possèdent un `SystemTime` extractible ; 285 sont dans la fenêtre élargie et **aucun dans l’intervalle central**. Des caractères invalides ou des balises mal formées dans un export ne prouvent pas à eux seuls une corruption du fichier EVTX source.

| Date civile Europe/Paris | XML interprétés | Rejets XML datés | Total daté contrôlé |
|---|---:|---:|---:|
| 14/10/2024 | 0 | 0 | 0 |
| 15/10/2024 | 412 | 0 | 412 |
| 16 au 27/10/2024 | 0 | 0 | 0 |
| 28/10/2024 | 5 964 | 108 | 6 072 |
| 29/10/2024 | 3 417 | 177 | 3 594 |

Les **9 793 événements structurés sélectionnés** appartiennent à 91 journaux. Les dates UTC EVTX à sept chiffres décimaux sont conservées ; les conversions locales et certaines dates dérivées par Python sont limitées à la microseconde. Les bornes minimum/maximum d’un journal ne prouvent pas une couverture continue entre ces dates.

Pièces : [inventaire et SHA-256 des 359 sources](recherche-OP-01/inventory.json), [événements XML](recherche-OP-01/events.xml), [JSONL](recherche-OP-01/events.jsonl), [chronologie CSV](recherche-OP-01/chronologie.csv), [rejets bruts](recherche-OP-01/xml-errors.jsonl), [comptages](recherche-OP-01/summary.json). Huit journaux principaux ont aussi été copiés exactement sous `recherche-OP-01/evtx/`, puis vérifiés par empreinte.

### 5.2. Chronologie technique consolidée

Les heures Paris ci-dessous sont celles obtenues par conversion des horodatages Windows ; elles ne sont pas une calibration indépendante de l’horloge.

| Date et heure Paris | UTC | Source et identifiants | Constat |
|---|---|---|---|
| **10/10 22:34:30** | 10/10 20:34:30 | System, Power-Troubleshooter / 1, RecordID **37385** enregistré le 15 | `SleepTime` rapporté lors de la reprise du 15. |
| **15/10 10:43:00–02** | 15/10 08:43:00–02 | System, Kernel-General / 1 **37368**, Power-Troubleshooter / 1 **37385** | Reprise ; `WakeTime=2024-10-15T08:43:00.851496500Z`, état effectif 5. L’horloge ancienne était celle du 10. |
| **15/10 10:43:01–02** | 15/10 08:43:01–02 | TerminalServices-LocalSessionManager/Operational / 21–22, **1805–1806** | Compte `LAPTOP-RMCOB2VU\fintm`, session 2, adresse **LOCAL**, séquence de session et de shell. |
| **15/10 10:43:03** | 15/10 08:43:03 | Même journal / 36, **1807** | `StateName=DesktopLocked`, `EventName=EvDesktopLocked` : état de bureau verrouillé. |
| 15/10 10:43:28 puis 10:52:42 | 15/10 08:43:28 puis 08:52:42 | System, Kernel-Power / 506 **37393**, / 507 **37437** | Capot signalé fermé puis ouvert ; secteur absent. Ces valeurs ne permettent pas d’identifier un opérateur. |
| **15/10 10:53:05–08** | 15/10 08:53:05–08 | System, Kernel-Power / 524 **37443**, / 42 **37445**, / 107 **37447** | Batterie à **2 %**, secteur absent, transition vers **S4/hibernation** (`TargetState=5`, `EffectiveState=5`). |
| **16/10 05:51:07** | 16/10 03:51:07 | Donnée contenue dans **37447**, pas un événement autonome du 16 | Échéance de réveil programmé sur secteur ; voir § 6. |
| **28/10 10:41:56–58** | 28/10 09:41:56–58 | System, Kernel-General / 1 **37448**, Kernel-Power / 105 **37452**, Power-Troubleshooter / 1 **37466** | Reprise, secteur présent ; `SleepTime` du 15 à 08:53:05 UTC, `WakeTime` du 28 à 09:41:56 UTC, états cible/effectif 5. |
| 28/10 10:42:30 | 28/10 09:42:30 | Winlogon/Operational / 811–812, **9935–9938** | Notifications `Event=5`, compatibles avec un déverrouillage ; code numérique non validé contre le schéma local. Indice de recoupement seulement. |
| 28/10 10:50:44, 10:53:35 et 11:01:54 | 28/10 09:50:44, 09:53:35 et 10:01:54 | OAlerts, Office 16 Alerts / 300, **247, 249, 251** | Activité WINWORD, EXCEL et OUTLOOK ; pas de preuve autonome d’ouverture d’un document précis. |
| **28/10 13:08:11–13:12:54** | 28/10 12:08:11–12:12:54 | OAlerts / 300, **257–264** | Huit demandes Outlook de confirmation de suppression définitive. |
| **28/10 13:26:30–13:39:05** | 28/10 12:26:30–12:39:05 | OAlerts / 300, **265–281** | Dix-sept demandes d’enregistrement de propriétés modifiées de messages, dont certains portent le sujet `RELEVES CE DMM CONSEILS`. |
| **28/10 15:38:14** | 28/10 14:38:14 | OAlerts / 300, **284** | Nouvelle demande de confirmation de suppression définitive. |
| **28/10 17:37:47** | 28/10 16:37:47 | TerminalServices-LocalSessionManager/Operational / 23 et 24, **1808, 1812** | Fin puis déconnexion de la session locale 2 sous `fintm`. |

La reprise du 28 est enregistrée **environ vingt minutes après l’ouverture déclarée** des scellés. Les alertes Outlook constituent des indices forts d’interaction : elles ne prouvent pas la réponse donnée, la réussite des suppressions ou le contenu effectivement modifié.

### 5.3. Sessions, horloge et exécutions : précisions

**Security.evtx** contient 34 472 événements, du **07/09/2026 19:33:43.236504 UTC** au **12/10/2026 06:50:38.6282135 UTC**. Les événements de 2024 n’y sont plus conservés. Les authentifications 4624/4625, fermetures 4634/4647, identifiants explicites 4648, privilèges 4672, processus 4688 et verrouillages 4800/4801 ne peuvent donc pas y être vérifiés pour octobre 2024. Dans 4624, les types 2, 7, 10 et 11 distingueraient notamment interaction locale, déverrouillage, connexion distante et connexion interactive en cache ; **aucun type n’est ici attribué à une session de 2024 à partir de Security**.

La séquence locale du 15 apparaît lors d’une reprise, avec bureau ensuite verrouillé : elle ne suffit pas à prouver une saisie de mot de passe ou une consultation humaine. Le nom du fournisseur **TerminalServices** ne signifie pas automatiquement un accès RDP. Les journaux RemoteConnectionManager et RDPClient présents sont vides ; cela n’exclut pas d’autres formes d’accès distant.

Winlogon contient aussi des notifications `Event=4` et `Event=5` le 28 autour de **14:20:38** et **14:21:04 à Paris**. La correspondance numérique n’a pas été validée : aucun manifeste correspondant trouvé sous `System32/winevt/Manifests`, et le manifeste WinSxS retrouvé porte un en-tête compressé `DCM`, non lisible directement comme XML. Ces notifications ne sont pas utilisées seules comme preuve de déverrouillage.

Les ajustements d’horloge sont cohérents avec les reprises : **37448** passe de `OldTime=2024-10-15T08:53:08.371274500Z` à `NewTime=2024-10-28T09:41:56.500000000Z`. Les événements **37449–37450** actualisent ensuite le biais du fuseau après le changement d’heure. Le champ CMOS initial ne doit pas être utilisé directement comme heure civile de Paris. Le 28 à **11:19:30 à Paris**, `svchost.exe` corrige l’horloge d’environ **−9,238 secondes**, d’après OldTime/NewTime ; le champ numérique `TimeDeltaInMs` de cet événement est aberrant et n’est pas utilisé pour ce calcul.

PowerShell enregistre le 28 vers **11:02–11:03 à Paris** des tests d’environnement et d’historique Windows Update, puis vers **11:23:47–52** :

```powershell
Get-AppxPackage C27EB4BA.DropboxOEM | Remove-AppxPackage
Get-AppxProvisionedPackage -Online |
  Where-Object DisplayName -In "C27EB4BA.DropboxOEM" |
  Remove-ProvisionedAppxPackage -Online
```

Ces traces d’exécution peuvent provenir d’opérations automatiques ; elles ne sont pas assimilées à une saisie humaine. Les commandes complètes et HostId figurent dans les exports. Aucun événement PowerShell de cette nature n’est retrouvé du 16 au 27 dans les journaux actuels.

## 6. Réveil programmé du 16 octobre : nature, date et origine

### 6.1. Identification du champ

**System / Microsoft-Windows-Kernel-Power / Event ID 107 / version 1 / RecordID 37447**, enregistré le **15/10/2024 à 08:53:08.371843800 UTC** :

```xml
<Data Name="TargetState">5</Data>
<Data Name="EffectiveState">5</Data>
<Data Name="WakeFromState">5</Data>
<Data Name="ProgrammedWakeTimeAc">2024-10-16T03:51:07.133163100Z</Data>
<Data Name="ProgrammedWakeTimeDc">1601-01-01T00:00:00.000000000Z</Data>
<Data Name="WakeRequesterTypeAc">2</Data>
<Data Name="WakeRequesterTypeDc">0</Data>
```

**`ProgrammedWakeTimeAc` désigne une échéance programmée côté secteur**, différente du champ `WakeTime` de Power-Troubleshooter, qui rapporte une reprise. La date future n’établit donc pas un réveil effectif le 16. La valeur DC à l’époque FILETIME 1601 est compatible avec une absence d’échéance sur batterie ; elle ne date pas un usage historique.

L’événement suivant de System, **37448**, est celui de la reprise du 28. Les deux RecordIDs sont consécutifs ; le rattrapage d’horloge et Power-Troubleshooter relient également l’hibernation du 15 à la reprise du 28.

### 6.2. Recherche du moment de programmation

Investigations réalisées : **264 définitions XML de tâches**, **2 265 clés de registre ciblées**, dont **260 clés TaskCache/Tasks**, export complet de System, TaskScheduler/Maintenance, WindowsUpdateClient/Operational et BackgroundTaskInfrastructure/Operational, puis recherche de l’échéance sur toute l’histoire allouée des **359 EVTX**.

Une seule mention de l’échéance à la seconde est retrouvée : **37447**. Recherche des formes UTC et locale avec `T` ou espace ; aucune autre mention ne donne un processus ou une tâche demandeuse. L’échéance exacte correspond au FILETIME **133735242671331631**, octets little-endian **`2f1960a17e1fdb01`**. Ces octets et les formes ISO UTC ASCII/UTF-16LE sont absents des ruches SYSTEM/SOFTWARE actuelles et des valeurs extraites. Cela ne couvre pas un délai relatif, une autre représentation ou une donnée disparue depuis 2024.

TaskScheduler/Maintenance contient 805 événements, sans événement le 15 ou le 16. Avant la saisie, les RecordIDs **711–715**, ID 808, du 10 octobre nomment les tâches NGEN ; le dernier est à **20:19:42.5873131 UTC**. Le suivant, **716**, est du 28 à **09:42:08.7225863 UTC**. Le journal détaillé TaskScheduler/Operational est absent de l’image, et les audits Security **4698/4702** de création/modification de tâche ne sont plus conservés pour 2024.

Huit définitions acquises ont `WakeToRun=true` :

| Tâche sous Microsoft/Windows | Enabled dans le XML acquis | Déclencheur ou indication conservée |
|---|---|---|
| `.NET Framework/.NET Framework NGEN v4.0.30319 Critical` | false | IdleTrigger ; fichier modifié le 02/12/2024. |
| `.NET Framework/.NET Framework NGEN v4.0.30319 64 Critical` | false | Même limite ; les deux tâches sont nommées dans Maintenance avant la saisie. |
| `InstallService/WakeUpAndContinueUpdates` | false | Déclencheurs vides ; fichier modifié le 14/03/2024. |
| `InstallService/WakeUpAndScanForUpdates` | false | Répétition PT24H, délai aléatoire PT24H, StartBoundary `2014-01-01T00:00:00Z`. |
| `SharedPC/Account Cleanup` | false | Déclencheurs vides ; fichier modifié le 28/09/2023. |
| `UpdateOrchestrator/Backup Scan` | Non explicite | StartBoundary `2021-07-21T10:53:35+02:00`. |
| `UpdateOrchestrator/Reboot_AC` | Non explicite | StartBoundary `2022-10-07T23:45:19+02:00`. |
| `UpdateOrchestrator/Schedule Wake To Work` | false | StartBoundary `2024-12-03T05:12:00+01:00`, fichier et clé TaskCache datés du 02/12/2024. |

Cet état est celui acquis en **2026**, pas une reconstitution de 2024. Dates d’enregistrement, LastWrite et échéances des déclencheurs ne datent pas l’armement du minuteur. Les NGEN portent notamment une date XML de 2010 et des modifications de fichier/clé en 2024. Les données binaires Triggers/DynamicInfo sont conservées sans attribuer une date de création du minuteur à partir d’un schéma non validé.

Des Kernel-Power 107 antérieurs ont déjà le même type de programmation AC avec `WakeRequesterTypeAc=2` :

| Enregistrement UTC | RecordID | Échéance AC indiquée, UTC |
|---|---:|---|
| 04/09/2024 11:47:49.4617200 | 33550 | 04/09/2024 23:57:30.8619679 |
| 03/10/2024 18:53:26.8280877 | 36455 | 04/10/2024 00:28:30.6121493 |
| 07/10/2024 11:18:52.5256316 | 36554 | 08/10/2024 00:26:30.3796958 |
| 15/10/2024 08:53:08.3718438 | 37447 | 16/10/2024 03:51:07.1331631 |

Le précédent 107 du 10, **37367**, porte les dates AC/DC à 1601, mais un `TargetState=6`, différent de celui du 15. **Il ne fixe pas une borne inférieure certaine de programmation.** On ne peut pas conclure que le minuteur a forcément été créé entre le 10 et le 15.

**Conclusion : l’échéance est attestée dans l’événement du 15 à 10:53:08 à Paris ; sa date de création/armement et son demandeur restent inconnus.** Maintenance ou Windows Update sont des possibilités techniques, pas des origines démontrées. Le sens détaillé de `WakeRequesterTypeAc=2` et la raison interne de la présence de l’ID 107 dans cette séquence ne sont pas établis.

Pièces : [résumé de cette recherche](recherche-OP-01/reveil-16oct/summary.json), [tâches](recherche-OP-01/reveil-16oct/tasks-inventory.json), [registre](recherche-OP-01/reveil-16oct/registry-selected.json), [mentions de l’échéance](recherche-OP-01/reveil-16oct/due-time-mentions.json), [recherche binaire](recherche-OP-01/reveil-16oct/hive-due-time-search.json), [événements pertinents](recherche-OP-01/reveil-16oct/relevant-events.jsonl).

## 7. Effacement, structure et récupération des EVTX

### 7.1. Événements d’effacement et conservation

Les **275 577 enregistrements alloués** ont été examinés avec le fournisseur et l’ID conjointement : Microsoft-Windows-Eventlog **104, 1100, 1101, 1102, 1104, 1105, 1108**, et Microsoft-Windows-Security-Auditing **4719** (audit), **4616** (horloge).

**Aucun 104 ou 1102 d’effacement retrouvé** dans l’histoire allouée, dans les fragments interprétables récupérés ou dans les blocs décodés depuis les anciennes entrées MFT. Le filtre sur les alloués retourne seulement deux 1100 et trois 4616, tous en **octobre 2026**, aucun dans la période étudiée. Un 1100 n’est pas assimilé à un effacement. Une absence d’événement ancien ne suffit pas à exclure une suppression ou une modification hors ligne.

Configuration acquise :

| Clé | Valeurs | LastWrite UTC |
|---|---|---|
| SYSTEM `ControlSet001/Services/Eventlog/Security` | MaxSize **20 Mio**, Retention **0** | 28/09/2023 17:56:55.709909 |
| SYSTEM `ControlSet001/Services/Eventlog/System` | MaxSize **20 Mio**, Retention **0** | 02/10/2026 15:32:15.976366 |
| SOFTWARE `…/WINEVT/Channels/Microsoft-Windows-TaskScheduler/Operational` | Enabled **0**, MaxSize **10 Mio** | 07/05/2022 05:27:59.604179 |

L’écrasement des anciens événements et la désactivation du journal détaillé sont des **explications normales possibles** des lacunes. Les valeurs acquises et leurs LastWrite ne démontrent pas une configuration inchangée depuis 2024.

### 7.2. Contrôle binaire et anomalies d’en-tête

Contrôle indépendant des signatures de fichier/bloc, tailles et copies de taille finale des enregistrements, bornes, FILETIME externes et identifiants. CRC32 calculés sur les zones du format : fichier **octets 0–119** ; en-tête de bloc **0–119 puis 128–511** ; données de bloc **512 à free_offset**.

**Résultats pour les EVTX actuels :** 359 CRC d’en-tête valides, 2 951 blocs signés avec CRC d’en-tête et de données valides, 275 577 enregistrements binaires correspondant aux nombres libevtx. Aucune anomalie de taille/trailer, aucune discordance des premiers/derniers IDs de bloc, aucune rupture interne de séquence, aucun ID dupliqué ou manquant entre le minimum et le maximum conservés dans chaque fichier. L’ordre physique circulaire n’est pas confondu avec l’ordre des identifiants.

| Journal | Enregistrements | IDs conservés |
|---|---:|---|
| System | 36 445 | 5 446–41 890 |
| Security | 34 472 | 1 567 448–1 601 919 |
| Application | 21 577 | 1–21 577 |
| Winlogon/Operational | 2 506 | 8 411–10 916 |
| TerminalServices-LocalSessionManager/Operational | 1 748 | 244–1 991 |
| TaskScheduler/Maintenance | 805 | 1–805 |

Dans System, **37447 et 37448 sont consécutifs**, sans numéro manquant entre le 15 et le 28. Aucun FILETIME externe alloué n’est dans l’intervalle central. Un CRC peut cependant être recalculé et un compteur réécrit : ces contrôles ne garantissent pas l’authenticité historique.

**Anomalies relevées : 41 fichiers signalés « corrupted » par libevtx, 59 avec flag dirty.**

- 39 ont dans l’en-tête un premier numéro de bloc supérieur au dernier : System **46/45**, Security **25/24**, malgré des CRC valides.
- Les deux autres sont Application, **168 blocs déclarés / 177 présents**, et Ntfs/Operational, **69 / 81** ; données plus récentes au-delà des bornes déclarées, flag dirty.
- Des next_record_id sont en retrait des derniers IDs physiques : System **41691** annoncé contre **41890** trouvé, Security **1600823** contre **1601919**.

Ces états sont compatibles avec des en-têtes non actualisés ou une clôture incomplète, situations connues des outils de lecture. **La cause historique n’est pas démontrée.** Ils sont consignés, sans convertir le mot « corrupted » en preuve de falsification volontaire.

### 7.3. Fragments dans l’espace libre des blocs

Deux lectures complémentaires : récupération indexée par `pyevtx.get_recovered_record(index)` et balayage binaire de l’espace après free_offset, avec signature, tailles cohérentes, FILETIME plausible et conservation des octets/offsets.

**7 587 candidats** : **4 120 interprétés**, **3 467 illisibles**, avec au moins un échec dans 79 fichiers. Les erreurs portent notamment sur des modèles BinXML écrasés ou des fragments incomplets ; chaque échec est consigné puis la lecture continue. La première passe exploratoire arrêtait certains fichiers au premier fragment illisible ; la passe finale indexée l’a remplacée. Elle a également examiné tous les alloués, sans échec sur les 275 577.

| Journal | Candidats | Interprétés | Illisibles |
|---|---:|---:|---:|
| System | 50 | 11 | 39 |
| Application | 84 | 8 | 76 |
| Security | 0 | 0 | 0 |

**Aucun FILETIME externe candidat, y compris illisible, et aucun TimeCreated récupéré interprétable dans l’intervalle central.** Les dates de la fenêtre élargie sont uniquement celles du 15, 28 ou 29, pas du 16 au 27.

Ces fragments ne sont pas autant d’événements supprimés volontairement : **6 040 ont le même triplet journal/RecordID/FILETIME que des alloués** ; les 7 587 ne représentent que **7 160 triplets distincts**. Leur présence dans l’espace libre ne date pas leur retrait de la zone utilisée.

Pièces : [structure](recherche-OP-01/integrite-evtx/structure-summary.json), [blocs/CRC](recherche-OP-01/integrite-evtx/chunks.jsonl), [index binaire](recherche-OP-01/integrite-evtx/records-binary.jsonl), [récupération finale](recherche-OP-01/integrite-evtx/recovery-summary.json), [fragments décodés](recherche-OP-01/integrite-evtx/recovered-complete.jsonl), [candidats bruts](recherche-OP-01/integrite-evtx/slack-candidates.jsonl), [erreurs](recherche-OP-01/integrite-evtx/recovery-errors.jsonl), [événements d’audit](recherche-OP-01/integrite-evtx/clear-and-audit-complete.jsonl), [configuration](recherche-OP-01/integrite-evtx/independent/log-config.json).

## 8. Recoupements indépendants des journaux Windows

### 8.1. Exécutions, registre utilisateur, raccourcis et navigation

Copies exactes et empreintes de **887 Prefetch**, **268 LNK récents** et **cinq bases de navigation** ; lecture de NTUSER.DAT pour **fintm** et **INVITES**, branches UserAssist, RecentDocs et RunMRU. Les ruches utilisateur sont identifiées par SHA-256, sans copie intégrale dans cette extraction. Les fichiers bruts sont sous `integrite-evtx/independent/raw/`.

| Artefact | Étendue | Résultat pour l’intervalle central | Limite |
|---|---|---|---|
| Prefetch | 887 fichiers, **3 889 dates d’exécution non nulles** | Aucune dans l’intervalle central | Dernières exécutions conservées seulement ; absence possible de Prefetch. |
| UserAssist | **313 valeurs**, dont **285 de 72 octets** | Aucun dernier lancement daté dans cet intervalle | Le dernier lancement remplace les précédents. |
| LNK récents | 268 fichiers, mtime et dates intégrées de cible | Aucune date examinée dans cet intervalle | Les dates de cible ne prouvent pas une ouverture humaine du raccourci. |
| Edge | 3 bases, **374 visites** | Aucune visite d’octobre 2024 conservée | Rétention insuffisante pour cette période. |
| Firefox | 2 bases, **15 749 + 17 visites** | Aucune dans l’intervalle ; **11 visites le 29/10** dans la fenêtre élargie | Suppression, navigation privée ou autre profil possibles. |

Les bases et éventuels WAL/SHM/journal sont copiés puis interrogés sur des copies de travail. Dates Edge : microsecondes depuis 1601 ; Firefox : microsecondes Unix. Profils Firefox : `y5rcl384.default-release` pour fintm, `qphdqdxy.default-release` pour INVITES. UserAssist : schéma du plugin RegRipper `userassist.pl` installé, nom ROT13, compteur à l’offset 4 et FILETIME à l’offset 60 pour 72 octets ; octets bruts conservés, autres tailles non artificiellement interprétées selon ce schéma.

Recoupements positifs :

| Trace | Date UTC | Heure Paris et portée |
|---|---|---|
| Prefetch SHELLEXPERIENCEHOST.EXE | 15/10 08:43:14.334934 | **10:43:14**, cohérent avec la reprise. |
| Prefetch WERFAULT.EXE | 15/10 08:53:08.198988 | **10:53:08**, cohérent avec la dernière séquence du 15. |
| Prefetch EXCEL.EXE | 28/10 09:53:34.793767 | **10:53:34**, juste avant l’alerte Office Excel à 10:53:35. |
| Prefetch WINWORD.EXE | 28/10 09:59:15.536473 | **10:59:15**, même seconde que l’alerte Office Word. |
| Notepad : UserAssist / Prefetch | 28/10 16:26:19.201 / 16:26:19.282789 | **17:26:19**, concordance à environ 82 ms. |
| UserAssist `D:\LdSD-1.0.4\bin\Win64\LdSD.bat` | 28/10 16:15:40.172 | **17:15:40** : nom et trace consignés, sans conclure à une extraction. |
| UserAssist `D:\WD Drive Unlock.exe` | 28/10 16:31:37.672 | **17:31:37** : ne prouve pas à lui seul une copie de données. |

Huit valeurs UserAssist de fintm portent un dernier lancement le 28 entre ouverture et restitution déclarées, notamment Outlook. Des exécutions peuvent être automatiques ; leur présence ne suffit pas à identifier un opérateur. **WEVTUTIL.EXE** et **EVENTVWR.EXE** sont présents, mais avec des dates conservées en **2026**, aucune pendant la rétention de 2024. Prefetch ne donne pas ici les arguments ; ces outils ne prouvent pas un effacement.

### 8.2. MFT : dates de fichiers pendant la rétention

Lecture de **1 046 016 emplacements de 1 024 octets**, `$MFT` de **1 071 120 384 octets**, SHA-256 :

```text
4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b
```

Signatures FILE, fixups de secteur et bornes d’attribut contrôlés ; dates de **STANDARD_INFORMATION (SI)** et **FILE_NAME (FN)** lues séparément. **1 045 790 FILE exploitables**, 665 406 alloués et 380 384 non alloués, sans échec de fixup/bornage relevé. Conservation des 1 024 octets bruts des entrées pertinentes et des références de parents ; les chemins inconnus ou séquences incertaines sont signalés. Quatre exemples ont été relus par libfsntfs avec les mêmes quatre dates SI.

**3 461 entrées allouées portent des dates dans l’intervalle central :**

| Ensemble | Entrées | Observations |
|---|---:|---|
| `Users/fintm/iCloudPhotos/Photos/…` | **3 434** | Toutes ont leur date SI de changement MFT en **2026** ; divergences SI/FN. |
| `L16B/TELEPHONES/IPHONE13_MINI/…` | **27** | SI création le **15/10/2024** pour toutes ; FN création le **28/10/2024** pour toutes ; SI changement MFT le 28 pour 2, le 29 pour 25. |

**Aucune date SI de changement d’entrée MFT de ces 3 461 n’est dans l’intervalle central.** Les 472 entrées nommant des EVTX n’ont aucune date SI/FN dans cet intervalle. Ces constats n’authentifient pas les métadonnées, mais évitent de confondre une date de contenu avec une opération locale démontrée.

Exemples contrôlés par deux lecteurs :

| MFT et fichier | Dates significatives, UTC | Interprétation limitée |
|---|---|---|
| **118**, iCloud `f855c571c12545b49d0858626e1e3831.mp4` | SI modification **27/10/2024 00:44:58** ; SI changement MFT **02/10/2026 19:46:49.958440** ; FN modification **08/09/2024 15:06:59** | Divergence, pas une preuve d’utilisation locale le 27. |
| **15292**, iCloud `IMG_9802(1).PNG` | SI création/modification/accès **27/10/2024 00:45:02** ; changement MFT **02/10/2026 19:48:56.224535** | Dates historiques avec changement ultérieur ; origine à recouper. |
| **26217**, `L16B/TELEPHONES/IPHONE13_MINI/Avis ECH 0423 SAS RCT 2.pdf` | SI création **15/10/2024 11:47:17.660** ; quatre dates FN **28/10/2024 16:13:43.235508** ; changement MFT **29/10/2024 00:41:39.618146** | Compatible avec une copie après ouverture conservant une date antérieure ; ne prouve pas un PC actif le 15 à 13:47 à Paris. |
| **56416**, `…/FACTURE RCT OCTOBRE.pdf` | SI création **15/10/2024 11:48:21.630** ; changement MFT **28/10/2024 16:13:43.393146** | Même prudence sur la création conservée. |

Les dates iCloud ou `L16B` peuvent provenir de métadonnées préservées depuis un autre appareil, d’un service cloud ou d’une copie ultérieure. **Le mécanisme exact n’est pas entièrement démontré et reste un point ouvert.** Le nom `IPHONE13_MINI` ne distingue pas TP-02 de TP-03 ; aucun équipement officiel n’est attribué à partir de ce seul nom.

### 8.3. USN : couverture récente et recoupement iCloud

Le flux nommé `$Extend/$UsnJrnl:$J` n’était pas accessible directement par la syntaxe du montage. Après inspection des attributs NTFS, **pyfsntfs en lecture** a extrait sa fin non creuse, avec droits nécessaires sur Dislocker. Taille logique **24 453 277 672 octets** ; seules **34 039 784 octets** ont été extraites à partir de l’offset **24 419 237 888**, évitant l’export des gigaoctets creux.

**325 252 USN V2 valides**, aucun candidat invalide, du **02/10/2026 18:42:39.367257 UTC** au **12/10/2026 06:51:00.398932 UTC** ; 489 nomment des EVTX. **Aucun USN conservé ne couvre octobre 2024**, donc ce journal ne vérifie pas directement un effacement pendant les scellés.

Recoupement par référence MFT **séquence comprise** : **3 252 des 3 434 fichiers iCloud** retrouvés dans **54 678 événements USN**, tous avec **BASIC_INFO_CHANGE**, du **02/10/2026 18:42:39.385276** au **02/10/2026 20:05:26.549898 UTC**. Aucun de ces événements ne porte DATA_OVERWRITE/DATA_EXTEND/DATA_TRUNCATION. Cela atteste des modifications de métadonnées en 2026, sans identifier les dates affectées, le logiciel demandeur ou la première apparition des métadonnées de 2024.

### 8.4. Clichés VSS

`vshadowinfo` échoue : **« invalid store block list header identifier »**, notamment au store header à l’offset **128630341632**. Aucun cliché monté ni réparé. Une lecture indépendante de **quatre blocs du catalogue** donne deux créations :

- `b764a044-a79c-11f1-8dc9-50e08563415f` : **02/10/2026 15:43:39.295713 UTC**.
- `2d9169d8-be7b-11f1-8dc9-50e08563415f` : **02/10/2026 16:11:15.212981 UTC**.

Ces dates sont les FILETIME du catalogue, pas une déduction depuis les GUID. Aucun état de volume d’octobre 2024 n’y est référencé. Ces clichés récents pourraient contenir des fichiers plus anciens, mais leur contenu n’a pas été récupéré. La cause de l’échec n’est pas attribuée à une falsification.

### 8.5. Tentative de récupération d’anciens fichiers EVTX

Parmi les **472 entrées MFT nommant des EVTX**, **103 sont non allouées**. Leurs dates SI présentes sont en 2022–2023 : **ce ne sont pas des dates de suppression établies**. Lecture de leurs données encore référencées : **136 998 912 octets**, sans erreur ni fichier omis. Les clusters peuvent avoir été réutilisés ; le nom ancien n’authentifie pas leur contenu actuel.

Les anciennes entrées System **627984**, Application **669277** et Security **669409** ne commencent plus par une signature EVTX. Sur les 103 lectures, un seul en-tête ElfFile et **37 blocs ElfChnk** sont retrouvés :

| Ancienne entrée MFT | Fournisseur réellement décodé | Enregistrements |
|---|---|---:|
| `NordUpdate.evtx`, **670685** | TerminalServices-LocalSessionManager | 749 |
| Kernel-WHEA/Operational, **677328** | AppXDeployment | 560 |
| AppxPackaging/Operational, **677534** | Crypto-DPAPI | 2 358 |
| AppReadiness/Operational, **677544** | PrintService | 870 |

**35/37 blocs sont identiques par SHA-256 à des blocs actuels** ; les deux autres ont un CRC d’en-tête valide mais de données invalide. Les **4 537 enregistrements décodés** ne sont donc pas autant de nouveaux événements anciens indépendants. Les fournisseurs différents et les correspondances exactes attestent une réutilisation des emplacements, sans prouver une falsification des fichiers portant ces anciens noms.

Pour lire les blocs isolés, des **conteneurs dérivés** ont été créés : en-tête de fichier **synthétique**, blocs récupérés **inchangés**. `derived-containers/*.derived.evtx` est un auxiliaire de parsing, **pas une preuve EVTX originale**. Données avant transformation, offsets et empreintes sont conservés séparément.

**Aucun de ces enregistrements n’a de FILETIME externe ni de TimeCreated dans l’intervalle central, et aucun 104/1102 d’effacement n’est retrouvé.** La tentative ne restitue pas les anciens journaux System/Security de 2024.

Pièces : [artefacts indépendants](recherche-OP-01/integrite-evtx/independent/results.jsonl), [sources et empreintes](recherche-OP-01/integrite-evtx/independent/sources.json), [Firefox](recherche-OP-01/integrite-evtx/independent/firefox-period-visits.jsonl), [résumé MFT](recherche-OP-01/integrite-evtx/ntfs/mft-summary.json), [dates MFT de l’intervalle](recherche-OP-01/integrite-evtx/ntfs/mft-gap-records.jsonl), [contrôle libfsntfs](recherche-OP-01/integrite-evtx/ntfs/mft-crosscheck.json), [USN](recherche-OP-01/integrite-evtx/ntfs/usn-summary.json), [recoupement iCloud](recherche-OP-01/integrite-evtx/ntfs/usn-cloud-summary.json), [catalogue VSS](recherche-OP-01/integrite-evtx/ntfs/vss-catalog-summary.json), [erreur VSS](recherche-OP-01/integrite-evtx/ntfs/vshadowinfo.txt), [anciennes entrées](recherche-OP-01/integrite-evtx/ntfs/deleted-evtx-summary.json), [correspondances de blocs](recherche-OP-01/integrite-evtx/ntfs/deleted-chunk-correspondence.json), [décodage](recherche-OP-01/integrite-evtx/ntfs/deleted-chunks-decoded.jsonl).

## 9. Reproduction des investigations

### 9.1. Préconditions et lectures ponctuelles

La reproduction requiert la même image complète, la clé BitLocker pour un montage absent, les outils du § 4 et les scripts conservés dans `ordinateur/recherche-OP-01/`. Elle n’exige aucun fichier de notes externe pour définir les bornes ou interpréter les résultats.

**Dans SIFT**, après contrôle des protections du § 4 :

```bash
df -h /tmp
command -v evtxexport evtxinfo vshadowinfo
python3 -c 'import pyevtx,pyregf,pyfsntfs,pyscca,pylnk,sqlite3'

sudo evtxinfo /mnt/windows/Windows/System32/winevt/Logs/System.evtx
sudo evtxinfo /mnt/windows/Windows/System32/winevt/Logs/Security.evtx
sudo evtxexport -f xml /mnt/windows/Windows/System32/winevt/Logs/System.evtx
sudo evtxexport -f xml /mnt/windows/Windows/System32/winevt/Logs/Security.evtx
# Tentative de récupération offerte par le même outil :
sudo evtxexport -m recovered -f xml \
  /mnt/windows/Windows/System32/winevt/Logs/System.evtx
```

La récupération effectivement menée dans les scripts utilise l’API équivalente `pyevtx`, par index, pour continuer après chaque candidat illisible. Les lectures ponctuelles ci-dessus ne remplacent pas ce traitement exhaustif.

**Dans SIFT**, pour contrôler l’entrée USN avant extraction :

```bash
sudo ntfsinfo -f -F '/$Extend/$UsnJrnl' /mnt/dislocker/dislocker-file
sudo ntfscat -f -n '$Max' /mnt/dislocker/dislocker-file '/$Extend/$UsnJrnl'
sudo vshadowinfo /mnt/dislocker/dislocker-file
```

L’option `-f` a servi à lire les attributs malgré le verrou d’accès parallèle au volume monté ; elle n’est utilisée ici que sur la vue Dislocker et le volume **protégés en lecture seule**. L’extraction USN ne passe pas par un export intégral de `$J` : le script sélectionne ses étendues non creuses. Les bibliothèques accèdent à l’entrée MFT **155201**, vérifiée comme celle d’UsnJrnl dans cette image ; cet index doit être recontrôlé pour une autre acquisition.

### 9.2. Exécuter les campagnes dans l’ordre

**Commandes ci-dessous exécutées depuis l’hôte**, à la racine du projet. Les scripts distants ont des destinations de travail **fixes** : `/tmp/OP-01-scelles-20261013`, `/tmp/OP-01-reveil-20261013`, `/tmp/OP-01-integrite-20261013`. Une nouvelle exécution remplace leurs sorties distantes. Préserver une campagne antérieure ou adapter les variables `out` des copies de scripts avant une nouvelle campagne ; ne jamais utiliser les répertoires des E01 comme destination.

Exécuter les étapes séquentiellement, vérifier chaque code retour et ne pas poursuivre une étape dépendante après un échec. L’échec d’ouverture VSS est consigné par le script de catalogue, qui peut néanmoins terminer sa lecture du catalogue.

Créer un dossier local distinct pour les nouveaux résultats :

```bash
cd /home/chris/codeProjects/CMMConseils
OP01_SCRIPTS="$PWD/ordinateur/recherche-OP-01"
OP01_REPRO=$(mktemp -d /tmp/OP-01-reproduction.XXXXXX)
mkdir -p "$OP01_REPRO/evtx" "$OP01_REPRO/reveil-16oct" \
  "$OP01_REPRO/integrite-evtx"
cp -a "$OP01_SCRIPTS/scripts" "$OP01_REPRO/"
cp -a "$OP01_SCRIPTS/reveil-16oct/scripts" "$OP01_REPRO/reveil-16oct/"
cp -a "$OP01_SCRIPTS/integrite-evtx/scripts" "$OP01_REPRO/integrite-evtx/"
```

**A — Inventaire, fenêtre temporelle et rejets XML.** Le second script dépend de l’inventaire produit par le premier :

```bash
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/scripts/evtx_scan.py" > "$OP01_REPRO/scan.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/scripts/check_xml_errors.py" \
  > "$OP01_REPRO/xml-errors-scan.log"
```

**B — Origine du réveil programmé.** Collecte des tâches/ruches/journaux, puis recherche de l’échéance dans les 359 EVTX et les octets des ruches :

```bash
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/reveil-16oct/scripts/collect_wake.py" \
  > "$OP01_REPRO/reveil-16oct/collect.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/reveil-16oct/scripts/search_wake_mentions.py" \
  > "$OP01_REPRO/reveil-16oct/search.log"
```

**C — Structure, récupération et artefacts indépendants.** `recover_audit.py` produit la récupération finale indexée ; les sorties intermédiaires d’`audit_evtx.py` ne doivent pas être prises pour une récupération complète :

```bash
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/audit_evtx.py" \
  > "$OP01_REPRO/integrite-evtx/audit.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/recover_audit.py" \
  > "$OP01_REPRO/integrite-evtx/recovery.log"
ssh -F /home/chris/.ssh/config sift 'python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/independent.py" \
  > "$OP01_REPRO/integrite-evtx/independent.log"
```

**D — NTFS, VSS et fichiers supprimés.** Les droits administrateur servent à lire la vue Dislocker et à écrire dans le dossier de travail NTFS. MFT avant son contrôle et avant la récupération ; récupération avant le décodage :

```bash
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/usn.py" \
  > "$OP01_REPRO/integrite-evtx/usn.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/vss_catalog.py" \
  > "$OP01_REPRO/integrite-evtx/vss.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/mft_scan.py" \
  > "$OP01_REPRO/integrite-evtx/mft-scan.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/mft_crosscheck.py" \
  > "$OP01_REPRO/integrite-evtx/mft-crosscheck.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/deleted_evtx.py" \
  > "$OP01_REPRO/integrite-evtx/deleted-evtx.log"
ssh -F /home/chris/.ssh/config sift 'sudo -n python3 -' \
  < "$OP01_SCRIPTS/integrite-evtx/scripts/decode_deleted_chunks.py" \
  > "$OP01_REPRO/integrite-evtx/deleted-decode.log"
```

Dans les scripts, les ruches actuelles sont ouvertes sans rejeu de transactions. Les dates d’UsnJrnl sont lues en USN V2 ; le lecteur MFT vérifie les fixups pour les entrées de 1 024 octets de cette image. La récupération des anciennes données a des plafonds de taille : aucun n’a été atteint dans la campagne rapportée, ce qui doit être vérifié à nouveau dans `deleted-evtx-summary.json`.

### 9.3. Récupérer les résultats et produire les synthèses locales

Ces transferts lisent les fichiers de travail de SIFT et écrivent dans le nouveau dossier local, **pas dans les acquisitions**. En Bash/Zsh, activer le contrôle des pipelines pour ne pas masquer un échec SSH :

```bash
set -o pipefail
ssh -F /home/chris/.ssh/config sift \
  'tar -C /tmp/OP-01-scelles-20261013 -cf - .' \
  | tar -xf - -C "$OP01_REPRO"
ssh -F /home/chris/.ssh/config sift \
  'tar -C /tmp/OP-01-reveil-20261013 -cf - .' \
  | tar -xf - -C "$OP01_REPRO/reveil-16oct"
ssh -F /home/chris/.ssh/config sift \
  'tar -C /tmp/OP-01-integrite-20261013 -cf - .' \
  | tar -xf - -C "$OP01_REPRO/integrite-evtx"
```

Copier également les huit journaux principaux pour contrôler leurs empreintes contre l’inventaire :

```bash
ssh -F /home/chris/.ssh/config sift \
  'tar -C /mnt/windows/Windows/System32/winevt/Logs -cf - System.evtx Security.evtx Application.evtx OAlerts.evtx Microsoft-Windows-Winlogon%4Operational.evtx Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx "Windows PowerShell.evtx" Microsoft-Windows-PowerShell%4Operational.evtx' \
  | tar -xf - -C "$OP01_REPRO/evtx"

python3 "$OP01_REPRO/reveil-16oct/scripts/summarize_wake.py"
python3 "$OP01_REPRO/integrite-evtx/scripts/query_firefox.py"
python3 "$OP01_REPRO/integrite-evtx/scripts/usn_cloud_crosscheck.py"
python3 "$OP01_REPRO/scripts/summarize.py"
```

`summarize.py` produit la chronologie CSV, les comptages et le manifeste SHA-256, et compare les copies EVTX aux empreintes source. `query_firefox.py` utilise des copies de travail sous `/tmp/OP01-firefox`, sans modifier les bases brutes ; `usn_cloud_crosscheck.py` relie les références complètes de fichiers aux USN.

Pour vérifier la livraison **déjà conservée dans le projet**, sans recalculer ni remplacer son manifeste :

```bash
cd /home/chris/codeProjects/CMMConseils/ordinateur/recherche-OP-01
sha256sum -c SHA256SUMS
```

Le succès de cette commande vérifie les fichiers référencés du jeu de résultats depuis la génération du manifeste ; il ne vérifie pas les 74 segments EWF originaux. Les erreurs initiales de sérialisation des multichaînes du registre, d’accès sans droits à Dislocker et d’écriture MFT dans un dossier administrateur ont été corrigées, puis les passes concernées terminées. Les échecs de décodage de fragments et d’ouverture VSS restent, eux, des limites effectives consignées.

## 10. Extractions de données et accès antérieurs à la perquisition

### 10.1. Questions, méthode et couverture réelle

Cette seconde campagne, menée le **13/10/2026**, répond à la demande de rechercher sur **OP-01** des traces de copie/export de données et de compromission antérieure à la perquisition du **15/10/2024**, en remontant à **2021/2022** lorsque des traces subsistent. Elle examine aussi le **28/10/2024**, car les principaux indices de regroupement de données se situent ce jour-là. Une opération du 28 ne doit pas être présentée comme antérieure à la perquisition.

La recherche distingue **présence de données exportées**, **regroupement local**, **connexion de supports**, **transfert effectif vers un destinataire**, **exposition à une menace** et **compromission réussie**. Ces propositions nécessitent des preuves différentes. L’image n’offre ni capture réseau de 2024, ni historique des connexions des comptes cloud, ni contenu des supports externes de l’époque.

Les opérations ont porté sur : inventaire des fichiers `L16B` et lecture de leurs enregistrements MFT ; catalogues et empreintes des 17 ZIP ; manifeste d’un export Takeout ; registre SYSTEM/SOFTWARE et deux NTUSER ; logiciels et démarrages automatiques ; **1 549 entrées Amcache** ; actions des **264 tâches** déjà extraites ; Prefetch/UserAssist/raccourcis déjà conservés ; historique Firefox ; anciens `setupapi` ; journaux Defender, PowerShell, services, sessions, WinRM, SMB et réseaux ; schéma et dates de toutes les tables de SRUM. Les logiciels et scripts de l’image n’ont pas été exécutés.

Les résultats sont sous [extractions-acces](recherche-OP-01/extractions-acces/). Les sources copiées sont assorties de SHA-256 ; [source-verification.json](recherche-OP-01/extractions-acces/source-verification.json) contrôle **32 correspondances** entre copies et empreintes source. Quatre ruches ont été lues directement et hachées sans être recopiées dans cette campagne. Aucun échec de décodage n’est consigné dans `errors.json` ou `additional/errors.json` pour ces deux collecteurs ; cela ne garantit pas l’exhaustivité historique des sources.

| Source examinée | Couverture utile constatée | Limite pour 2021–2024 |
|---|---|---|
| Firefox `fintm` | **3 844 visites** du 04/01/2021 au 06/09/2024 dans la fenêtre avant le 15 ; base complète depuis 2019. | Seulement **5 visites en 2023 et 23 en 2024** dans la base complète : couverture très clairsemée. Les bases Edge conservées ne couvrent pas 2024. |
| Defender | Événements collectés depuis le **28/09/2023** ; **2 028 événements avant le 15/10/2024**. | N’établit pas l’absence de menaces en 2021/2022 ou hors des détections conservées. |
| PowerShell Operational | Depuis le **28/09/2023** ; **338 événements antérieurs**, dont **23 blocs 4104**. | La journalisation ne représente pas toutes les commandes ni tous les interpréteurs. |
| LocalSessionManager | Depuis le **20/11/2023** ; **1 559 événements antérieurs**. | Les comptes et adresses de session ne couvrent pas tous les outils de téléassistance. |
| WinRM | Depuis le **04/12/2023** ; **1 375 événements antérieurs**. | Des opérations d’énumération et des échecs ne prouvent pas un accès distant réussi. |
| Services System / installations Application | **180 événements 7045 antérieurs** dans la sélection ; installations Application conservées depuis octobre 2023. | Le nom d’un service ne valide pas sa signature ou son intégrité binaire. |
| `setupapi.dev.*.log` | Quatre anciennes rotations couvrent les sections du **28/09/2023 au 03/12/2024**. | Journal d’installation/nettoyage, pas journal de chaque branchement ni de chaque copie. |
| SRUM réseau | **682 lignes**, du **03/09/2026 au 08/10/2026**. | Aucun volume réseau de 2024 exploitable dans cette table. |
| SRUM énergie long terme | **127 lignes historiques**, du **16/10/2021 au 28/10/2024**, parmi 133 lignes totales. | Statistiques d’énergie/batterie ; aucune destination réseau ni liste de fichiers transmis. |
| Security et USN | Conservation de 2026, détaillée plus haut. | Ne permettent pas de reconstituer les authentifications ou les copies de 2024. |

Pour les recherches locales Firefox, « avant le 15 » signifie **avant le 15/10/2024 à 00:00 à Paris**, soit le **14/10 à 22:00 UTC**. Pour les tableaux de sélection EVTX, le filtre des scripts est la date **15/10 à 00:00 UTC** ; les constats positifs cités ici sont en mars, mai et octobre 2023/2024, loin de cette différence de deux heures. Aucune borne ne représente l’heure réelle de début de perquisition, toujours inconnue.

### 10.2. Regroupement `L16B` : données et chronologie

[L’inventaire](recherche-OP-01/extractions-acces/l16b-inventory.json) dénombre **1 558 fichiers**, totalisant **4 643 450 972 octets** (4,64 Go décimaux). Les ensembles principaux sont `LOCAL` (**1 389 fichiers**), `GDRIVE` (**93**), `MESSAGERIES` (**34**), `TELEPHONES` (**30**) et `iCloudDrive` (**8**). S’ajoutent deux ZIP GDRIVE, un fichier SAGE et un ZIP SHINE. Le total additionne les archives et leurs contenus déjà présents séparément ; il ne mesure pas une quantité unique de données copiées ni un volume transmis.

La lecture binaire de **1 558 enregistrements MFT**, avec contrôle des fixups et conservation des enregistrements bruts dans [l16b-mft.jsonl](recherche-OP-01/extractions-acces/l16b-mft.jsonl), n’a rencontré aucune erreur. Les dates de création **FN** du premier nom conservé se répartissent ainsi : **1 555 au 28/10/2024**, deux au 27/07/2026 et une au 02/10/2026. Les 1 555 dates du 28 s’étendent de **09:47:55 à 16:13:43 UTC**, soit **10:47:55 à 17:13:43 à Paris**.

| Ensemble | Dates FN de création observées le 28, heure de Paris | Lecture possible |
|---|---|---|
| `LOCAL` | **10:47:55–11:11:10**, 1 389 fichiers | Regroupement concentré de documents locaux après la reprise Windows. |
| `GDRIVE`, dossier développé | **14:50:40–14:50:46**, 93 fichiers | Création groupée d’un ensemble de documents ; les dates SI de création sont majoritairement atypiques. |
| `TELEPHONES` | **17:01:10–17:13:43**, 30 fichiers | Présence de données de téléphones regroupées sur OP-01 ; ne prouve pas leur extraction directe depuis un téléphone connecté à OP-01. |
| `SAGE/sage.pdf` | **15:27:24** | Présence d’un PDF de 42 818 862 octets, sans validation de son processus de génération. |
| ZIP `SHINE` | **15:57:55** | Archive contenant des formats d’export bancaire et des documents. |

Les **27 créations SI du 15/10** signalées dans l’étape précédente sont toutes associées à des créations FN du 28. **93 créations SI sont au 31/12/1979**, alors que leurs FN sont au 28/10/2024 ; les ZIP GDRIVE comprennent une date DOS minimale au 01/01/1980. Le changement de fuseau peut faire passer une date minimale à la veille en UTC. Ces incohérences et les nombreuses dates SI plus anciennes sont compatibles avec des métadonnées préservées/restaurées lors de copies ou décompressions. Elles empêchent de dater l’opération locale à partir du seul SI.

Une comparaison de contenu a porté sur **40 documents**, sélectionnés de façon déterministe parmi **1 232 PDF/Office de moins de 4 Mio** de `LOCAL`, avec recherche directe dans Desktop/Documents/Downloads. **16 ont une contrepartie encore présente dans le profil `fintm`, et les 16 paires ont des SHA-256 identiques** ; voir [local-source-sample.json](recherche-OP-01/extractions-acces/local-source-sample.json). Cela confirme que cet échantillon contient des documents identiques aux données locales actuelles, sans établir seul le sens de copie ou l’auteur. Les 24 autres n’ont pas été trouvés aux chemins candidats ; cette recherche limitée ne prouve pas leur suppression. Aucun résultat de l’échantillon n’est extrapolé aux 1 558 fichiers.

**Conclusion : un regroupement local de données le 28 octobre est fortement étayé par la concentration des créations FN et les formats présents. L’origine exacte des fichiers, le procédé utilisé et la personne ayant opéré ne sont pas établis par ces seules métadonnées.** Les dates peuvent aussi être manipulées ; les FN ne sont pas des signatures inviolables.

### 10.3. Exports de messageries, Google Drive et banque

La lecture des catalogues ZIP et le calcul des empreintes, sans exécution ni extraction générale du contenu, sont conservés dans [archives.json](recherche-OP-01/extractions-acces/archives.json).

- Deux fichiers de messagerie **PST**, de **2 143 626 240** et **1 156 260 864 octets**, sont présents dans `MESSAGERIES`. Leur extension et leur taille suggèrent des conteneurs Outlook ; leurs messages et leur structure interne n’ont pas été validés dans cette campagne. Leur présence ne démontre pas un export Outlook exécuté localement à l’heure de copie.
- `takeout-20241028T114105Z-001.zip`, **41 828 775 octets**, contient réellement `Takeout/Mail/L16.mbox` (**66 015 300 octets décompressés**) et `Takeout/archive_browser.html` (**197 837 octets**). Les dates DOS des deux membres sont au **01/01/1980**, donc non utilisables comme date effective d’export.
- Le [manifeste HTML Takeout](recherche-OP-01/extractions-acces/takeout-archive_browser.html) nomme le compte `rct93300@gmail.com`, décrit un export Google Mail et affiche **28/10/2024, 04:42:33 UTC−7**, soit **11:42:33 UTC / 12:42:33 Paris**. Son SHA-256 est `a81d350c7c347e78a18756ed5bda77faee3d2b1eb278c40050408a096cda4f83`. Des textes génériques « aucune donnée trouvée / 0 fichier exporté » figurent également dans le HTML ; le catalogue ZIP apporte la preuve distincte de la présence du MBOX. Ce manifeste n’authentifie pas cryptographiquement le producteur et n’identifie pas l’auteur de la demande d’export.
- `GDRIVE.zip` et `GDRIVE (2).zip` mesurent chacun **61 847 396 octets** et contiennent **97 membres**, dont **93 fichiers**. Leurs SHA-256 diffèrent, mais les catalogues comparés (noms, tailles, CRC, tailles comprimées, dates et indicateur de chiffrement) sont identiques. Cela ne suffit pas à affirmer l’identité de tous leurs octets ni celle des données décompressées sans comparaison complémentaire. Les dates des membres sont surtout au 28 ; une entrée au 29 et une au 01/01/1980 illustrent les limites des dates internes ZIP, sans fuseau explicite.
- Le ZIP SHINE, dont le nom désigne une période comptable **01/2023–15/10/2024**, contient **30 membres**, notamment CSV et OFX. Les dates de ses membres sont au **28/10/2024**. La date de fin comptable dans le nom ne représente pas la date technique d’export.
- Trois ZIP de conversations WhatsApp figurent dans `TELEPHONES/IPHONE13`. Les dates de leurs médias remontent notamment à 2020–2023 ; elles ne datent pas leur importation sur OP-01. Aucun identifiant physique de téléphone n’a été attribué à ces archives dans cette campagne.

**Des données sous forme d’exports sont donc présentes dans l’image. Le manifeste Takeout apporte un indice explicite d’export le 28 octobre. Aucune preuve de transmission sortante de ces ensembles, de leur destination finale ou d’exfiltration clandestine antérieure au 15 n’est établie.** Un export cloud peut avoir été créé ailleurs puis copié sur OP-01.

### 10.4. Supports externes et limites d’une attribution de copie

Le registre actuel contient cinq périphériques USBSTOR. Une clé PHILIPS, identifiant `3160421182141263758&0`, porte des valeurs FILETIME de propriétés `0064/0065/0066` au **29/10/2024 à 23:38:33 UTC**, soit **30/10 à 00:38:33 Paris**. Ce constat est postérieur à la restitution déclarée. Les dates des propriétés ne constituent pas un historique de tous les branchements. Les autres entrées USBSTOR observées sont datées de décembre 2024 ou de 2026.

L’analyse des **10 journaux setupapi conservés**, incluant les anciennes rotations, est déterminante : **trois identifiants Kingston DataTraveler 3.0 distincts** sont enregistrés dans `setupapi.dev.20241203_223829.log` avec installation matérielle `SWD\WPDBUSENUM` :

| Identifiant de support dans le journal | Début de section du 28/10/2024, heure locale consignée |
|---|---|
| `E0D55EA493C4F3A178B11467&0` | **16:27:54.063** |
| `E0D55EA49333E49089B402AD&0` | **17:00:07.167** |
| `0026188879D7F250D72E0E88&0` | **17:14:51.903** |

Les sections se terminent avec succès et mentionnent le démarrage du périphérique. Les heures setupapi sont enregistrées sans fuseau dans le texte ; elles sont interprétées ici comme heures locales de Windows, cohérentes avec Paris et la chronologie du 28, mais conservées brutes dans [setupapi-usb-sections.json](recherche-OP-01/extractions-acces/setupapi-usb-sections.json). Ce sont des traces de présence/installation de supports, **pas des preuves de copie de fichiers**.

Ces identifiants ne sont plus dans USBSTOR actuel. Les journaux montrent leur suppression le **03/12/2024 vers 22:38**, par `cleanmgr.exe /autocleanstoragesense /d C:`. Cette commande de nettoyage consignée explique une perte de traces de périphériques ; son nom et sa date ne prouvent pas une volonté d’effacer les traces de la perquisition. Une entrée de suppression `USB\VID_1058&PID_264F` est également conservée ; elle ne date pas son usage du 28.

Le recoupement **MountedDevices ↔ MountPoints2** est conservé dans [usb-mounteddevices-crosscheck.json](recherche-OP-01/extractions-acces/usb-mounteddevices-crosscheck.json). Il relie les volumes `{b0643ceb-9537-11ef-8dc8-50e08563415f}`, `{b0643e9f-9537-11ef-8dc8-50e08563415f}` et `{b0643fa4-9537-11ef-8dc8-50e08563415f}` aux trois identifiants Kingston ci-dessus, avec des dernières écritures utilisateur le 28. Il relie aussi `{b06440d5-9537-11ef-8dc8-50e08563415f}` à **`SCSI#CdRom&Ven_WD&Prod_Virtual_CD_264F`**. Sa branche AutoRun, écrite le **28/10 à 16:30:31 UTC / 17:30:31 Paris**, contient **`"D:\WD Drive Unlock.exe" autoplay=true`**. Il s’agit du **CD virtuel de déverrouillage WD**, pas d’une identification de la partition de données externe ni d’une preuve de déverrouillage réussi. Ce recoupement illustre aussi pourquoi une lettre de lecteur n’identifie pas durablement un support.

Les indices UserAssist déjà documentés restent pertinents : lancement de `D:\LdSD-1.0.4\bin\Win64\LdSD.bat` à **17:15:40 Paris** et de `D:\WD Drive Unlock.exe` à **17:31:37** le 28. **La fonction et l’éditeur de LdSD n’ont pas été identifiés de manière fiable.** Il ne doit pas être qualifié d’outil d’extraction ou attribué à l’administration sans pièce complémentaire. La lettre `D:` ne permet pas d’identifier automatiquement l’une des trois clés, le disque Western Digital ou le destinataire d’une copie.

### 10.5. Menace détectée avant la perquisition : PDF de phishing

Le journal **Microsoft-Windows-Windows Defender/Operational** contient une paire d’événements antérieurs au 15 octobre :

| Événement | Date à Paris | Données utiles |
|---|---|---|
| **1116, record 920** | **15/05/2024 10:13:02.744935** | Menace `Trojan:PDF/Phish.TSC!MTB`, protection en temps réel, utilisateur `LAPTOP-RMCOB2VU\fintm`, processus indiqué `C:\Windows\System32\RuntimeBroker.exe`. |
| **1117, record 921** | **15/05/2024 10:13:58.078072** | Même Detection ID `{895D1E06-B4BC-4D45-8DD8-670E59900D31}` ; action **Quarantaine**, erreur `0x00000000`, opération déclarée réussie. |

Le fichier désigné est **`AppleID-977451TLU5I[58342].pdf`**, dans le cache de pièces jointes de l’application Windows de courrier : `Users\fintm\AppData\Local\Packages\microsoft.windowscommunicationsapps_8wekyb3d8bbwe\LocalState\Files\S0\438\Attachments\`. Le chemin de détection mentionne aussi un objet **`PdfUri:0000`**. `RuntimeBroker.exe` est le processus rapporté par Defender ; ce champ n’établit pas l’exécution d’un programme malveillant ni l’ouverture d’un lien par la cliente. Le libellé de menace est la classification du moteur, pas une analyse indépendante du PDF.

Le PDF n’est plus présent à ce chemin dans l’image. Les dossiers de quarantaine Defender existent mais **ne contiennent aucun fichier** à l’acquisition, selon [quarantine-inventory.json](recherche-OP-01/extractions-acces/quarantine-inventory.json). Aucune récupération du contenu du PDF ni de son URL cible n’a donc été obtenue par cette voie.

Une recherche complémentaire du fragment ASCII **`AppleID-977451`**, sans distinction de casse, a lu les **66 015 300 octets** du MBOX Takeout avec contrôle CRC de décompression : **aucune occurrence**. Le MBOX décompressé a pour SHA-256 `41cf8b7688150909f195164d0f9ffc01570cb54dd7c2d17d34f3998ff3b0f3ef` ; les paramètres et le résultat sont dans [mbox-pdf-name-search.json](recherche-OP-01/extractions-acces/mbox-pdf-name-search.json). Il s’agit d’une recherche ciblée de nom, qui ne valide pas chaque message ni les encodages MIME ; elle n’exclut pas le document sous un autre nom/encodage ou dans une autre messagerie. Les PST n’ont pas été fouillés.

**Conclusion : une exposition à un document détecté comme phishing avant la perquisition est établie par le journal, avec mise en quarantaine déclarée réussie. Une compromission du PC, un vol d’identifiants ou une exfiltration consécutive ne sont pas démontrés.** Le succès de la quarantaine ne permet pas non plus d’exclure une consultation antérieure ou des actions hors de la détection conservée. La documentation [Microsoft des événements Defender](https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus) distingue détection et action de remédiation.

Les changements de configuration Defender n’ont pas été ignorés : une sélection de **56 événements 5004/5007** et paramètres contenant notamment `Disable` est conservée dans [defender-configuration-changes.json](recherche-OP-01/extractions-acces/defender-configuration-changes.json). On observe notamment des bascules `DisableBmNetworkSensor` 0→1→0 à moins d’une seconde d’écart. Ces champs ne sont pas, à eux seuls, une preuve de désactivation malveillante ou de responsabilité humaine ; cette campagne n’attribue pas chaque modification de sécurité à un processus.

### 10.6. Téléassistance, accès distants et persistance

Un raccourci conservé dans `Users/fintm/AppData/Roaming/Microsoft/Windows/Recent` contient dans ses octets une URL **`https://secure.logmeinrescue.eu/R`**, accompagnée d’un code de session. Sa date de modification NTFS est **06/10/2023 10:40:41.274903 UTC**, soit **12:40:41 Paris**. Le parseur LNK initial ne restituait pas la cible dans son champ `target` ; une lecture de la chaîne UTF-16LE dans le fichier brut établit le domaine, indépendamment du nom du raccourci.

LogMeIn Rescue est un service de téléassistance proposant une connexion par code, comme le décrit [le guide officiel de connexion](https://www.logmeinrescue.com/-/media/6a893c89d119416e9595cb8ad18514a2.pdf). **Ce raccourci est une piste d’utilisation de téléassistance avant la perquisition. Il ne prouve ni une session effectivement établie, ni un contrôle distant, ni l’identité du technicien, ni son caractère autorisé.** La date de modification du raccourci n’est pas une heure de connexion certifiée. Aucun binaire ou lancement LogMeIn n’a été identifié dans les éléments Amcache, Prefetch et UserAssist examinés ; les occurrences « Rescue » d’Amcache correspondent au dossier Norton `RescueDisk` de 2026.

Une recherche des noms dans **toute la MFT** a également examiné **1 046 016 emplacements**, dont **380 384 entrées FILE non allouées**. Elle retrouve **42 entrées ciblées**, dont 23 non allouées : le raccourci Rescue est la seule correspondance pertinente avec les outils recherchés ; les 41 autres sont notamment des noms de composants Windows `*peeradmin*/*serveradmintools*` et JavaScript `_wrapperClone.js`, faux positifs de `radmin/rclone`. **Aucun nom du PDF détecté ni binaire des outils ciblés n’a été retrouvé dans ces entrées conservées.** L’empreinte MFT complète est identique à celle de la campagne précédente. Les [résultats MFT ciblés](recherche-OP-01/extractions-acces/mft-targets/mft-target-records.jsonl) conservent SI/FN et les parents incertains des noms supprimés. Les clés héritées `gap_records/gap_hits` du script de scan désignent ici les correspondances de noms, et non des événements pendant l’intervalle sous scellés. L’absence de nom ne permet pas d’exclure un fichier ancien dont l’entrée a été réutilisée.

Les contrôles croisés donnent les résultats suivants :

- Recherche ciblée de noms d’outils de téléassistance et transfert dans le registre, les logiciels, Amcache, les tâches, les événements et les traces d’exécution : aucun faisceau établissant une installation/lancement d’AnyDesk, TeamViewer, RustDesk, VNC, ScreenConnect, Radmin, Splashtop, RemotePC, DWAgent, MeshAgent, NetSupport, ngrok, rclone, WinSCP ou FileZilla. Les correspondances textuelles ont été revues : `ConsentPromptBehaviorAdmin` et `MamCache/RoamCache` sont des faux positifs lexicaux, pas des produits Radmin/Amcache. Ce filtrage par noms ne détecte pas tous les logiciels renommés ou inconnus.
- Les clés **Terminal Server Client** de `fintm` et `INVITES` ne contiennent pas d’historique de serveurs RDP. Le paramètre actuel `fDenyTSConnections=1` indique une désactivation actuelle du service de connexion RDP entrant ; il ne décrit pas nécessairement son état en 2024.
- Les **316 événements 21/22** LocalSessionManager antérieurs sélectionnés indiquent **`Address=LOCAL`**. Ils ne démontrent pas de sessions RDP distantes ; une téléassistance peut toutefois intervenir à l’intérieur d’une session locale et ne pas apparaître comme une nouvelle connexion RDP.
- Les **180 installations de services 7045** antérieures ont été extraites. Les noms et chemins comprennent principalement pilotes Windows/Defender `MpKsl*`, Adobe, ASUS, Intel, Apple, impression et Dropbox ; aucun nom d’outil distant recherché n’a été retrouvé. Les signatures et octets de chaque pilote/service n’ont pas fait l’objet d’une validation exhaustive : un nom familier ne suffit pas à exclure une usurpation.
- Les actions des **264 tâches** sont décodées sans erreur ; aucune correspondance avec les outils ciblés. Les tâches SMB utilisant PowerShell pointent vers `DisableUnusedSmb1.ps1`. L’état actuel des tâches ne reconstitue pas des tâches anciennes déjà supprimées.
- Les **23 blocs PowerShell 4104** antérieurs conservés désignent `CL_Utility.ps1` sous des dossiers temporaires `SDIAG_*`, avec contenu de fonctions de diagnostic Windows. Aucun transfert ou commande d’outil distant ciblé n’est identifié dans ces blocs. Le contenu est conservé dans les XML ; les chemins et IDs sont indexés dans [powershell-historic-index.json](recherche-OP-01/extractions-acces/powershell-historic-index.json). Une absence dans 4104 ne signifie pas absence de commande exécutée.
- WinRM montre surtout des énumérations de `wsman/1/config/listener` et des échecs de connexion ; aucun accès distant réussi et attribuable n’est établi dans cette sélection.
- **Deux échecs d’authentification SMB**, événement **551**, records **1 et 2**, proviennent de **`192.168.1.139`** le **26/03/2024 à 14:20:36 et 14:21:12 UTC** (**15:20:36 et 15:21:12 Paris**), avec statut `0xc000006d` et message `session setup failed`. Ils établissent des tentatives échouées depuis une adresse privée. Ils ne prouvent ni intrusion réussie, ni exfiltration, ni origine malveillante. L’équipement correspondant à cette adresse n’est pas identifié par l’image.
- Firefox : la recherche par domaines/chemins, de 2021 à la veille du 15 octobre, retourne **5 visites ciblées**, toutes le **08/11/2021**, concernant des pages Free de contact/assistance. Aucun domaine ciblé de téléassistance/transfert/cloud n’est retrouvé dans cette sélection. Les **164 annotations** de téléchargement, correspondant à **82 références**, ne montrent pas de correspondance avec ces outils ; cela ne constitue pas un audit complet de chaque téléchargement. Les requêtes des URL sont omises des sorties de recherche afin de ne pas divulguer de jetons éventuels.
- Les démarrages automatiques actuels comprennent notamment **Dropbox, OneDrive et NordVPN**, ainsi que Adobe, Teams, PaperCut et Norton. La présence de synchronisation cloud ou d’un VPN n’établit ni copie d’un fichier déterminé, ni vol de données, ni intrusion. Aucun historique de transferts Dropbox/OneDrive de 2024 n’a été reconstitué dans cette campagne.

**À ce stade, une compromission réussie ou une exfiltration antérieure à la perquisition n’est pas établie. Les deux pistes positives à confronter à d’autres sources sont le raccourci LogMeIn Rescue de 2023 et le PDF détecté en mai 2024. La faible conservation des historiques interdit de conclure que le PC n’a jamais été compromis.**

### 10.7. SRUM et impossibilité de quantifier une exfiltration de 2024

La base `Windows/System32/sru/SRUDB.dat` a été copiée et lue avec `pyesedb`, en conservant le schéma réel et les valeurs brutes. Les dates OLE ont été converties depuis l’origine **30/12/1899**, suivant la [spécification libyal SRUM](https://github.com/libyal/esedb-kb/blob/main/documentation/System%20Resource%20Usage%20Monitor%20%28SRUM%29.asciidoc).

La table réseau `{973F5D5C-1D90-4944-BE8E-24B94231A174}` ne conserve que septembre–octobre **2026**. Les tables d’utilisation des applications et de connectivité réseau examinées ne fournissent pas de lignes datées de 2024. **Il n’est donc pas possible d’utiliser cette base pour chiffrer les octets envoyés ou reçus lors de la perquisition ou avant celle-ci.**

La table d’énergie long terme `{FEE4E14F-02A9-4550-B5CE-5FA2DA202E37}LT` conserve cependant 127 lignes de 2021–2024 : elles concernent notamment temps sur batterie/secteur, capacité et cycles. Elles ne doivent pas être confondues avec des compteurs réseau. Les données et plages par table sont conservées dans [srum-schema.json](recherche-OP-01/extractions-acces/additional/srum-schema.json), `srum-historic.jsonl` et `srum-idmap.json`. La présence de dates anciennes dans une table ne confère pas cette couverture aux autres tables.

### 10.8. Reproduire cette campagne et préserver ses résultats

Après remontage de l’image selon le § 4, vérifier **NTFS `ro`**, Dislocker `-r` et le loop en lecture seule. Les scripts emploient un répertoire de travail persistant dans SIFT : **`/home/sansforensics/analysis/OP-01/extractions-acces-20261013`**. Ils requièrent `pyregf`, `pyevtx` et `pyesedb`, déjà disponibles sur la VM. Pour une nouvelle reproduction, modifier la variable `out` vers un nouveau répertoire afin de ne pas remplacer ces résultats.

Depuis le projet local :

```bash
scp -F /home/chris/.ssh/config \
  ordinateur/recherche-OP-01/extractions-acces/scripts/{collect_phase2,amcache_srum,archives,l16b_mft,followup,mft_targets,source_matches,mbox_name_search}.py \
  sift:/home/sansforensics/

ssh -F /home/chris/.ssh/config sift \
  'python3 /home/sansforensics/collect_phase2.py && python3 /home/sansforensics/amcache_srum.py'
ssh -F /home/chris/.ssh/config sift \
  'python3 /home/sansforensics/archives.py && python3 /home/sansforensics/l16b_mft.py && python3 /home/sansforensics/followup.py && python3 /home/sansforensics/mft_targets.py && python3 /home/sansforensics/source_matches.py && python3 /home/sansforensics/mbox_name_search.py'

set -o pipefail
ssh -F /home/chris/.ssh/config sift \
  'tar -C /home/sansforensics/analysis/OP-01/extractions-acces-20261013 -cf - .' \
  | tar -xf - -C ordinateur/recherche-OP-01/extractions-acces

python3 ordinateur/recherche-OP-01/extractions-acces/scripts/firefox_history.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/setupapi_usb.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/usb_mapping.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/tasks_index.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/summarize_phase2.py
python3 ordinateur/recherche-OP-01/extractions-acces/scripts/validate_sources.py
```

`firefox_history.py` effectue ses lectures SQLite sur des **copies temporaires**, avec les éventuels WAL/SHM, et non sur les fichiers bruts conservés. `archives.py` liste les membres ZIP et calcule leurs empreintes ; les dates internes restent des champs sans fuseau. `l16b_mft.py` utilise les numéros d’inode de l’inventaire pour lire directement les entrées MFT. `mft_targets.py` parcourt toute la MFT, y compris les entrées non allouées, et reconstruit les chemins en signalant les parents incertains. La présence d’un ancien nom ne garantit pas la récupération de son contenu.

L’extraction du manifeste Takeout dans `archives.py` utilise `zipfile.ZipFile(...).read('Takeout/archive_browser.html')`. La recherche complémentaire `mbox_name_search.py` lit le MBOX en flux pour le seul fragment de nom décrit au § 10.5. `source_matches.py` compare les documents échantillonnés aux chemins candidats, sans écrire sur le volume analysé. Le fichier extrait est une pièce de travail ; son empreinte est indiquée au § 10.3. Les chaînes URL du raccourci Rescue sont lisibles avec `read_bytes().decode('utf-16le', errors='ignore')` ; la cible n’a pas été visitée et le code n’a pas été soumis au service.

**Incident de travail :** SIFT s’est interrompue durant le rapatriement initial ; les sorties temporaires de `/tmp` ont disparu après redémarrage. Les collecteurs ont été relancés intégralement après rétablissement du montage en lecture seule, vers le répertoire persistant ci-dessus. Les journaux `collect.log`, `amcache-srum.log` et `recollect.log` permettent de distinguer les passes. Aucun résultat partiel perdu n’est nécessaire pour soutenir les constats finaux ; l’intégrité matérielle de l’acquisition n’est pas déduite du seul succès du redémarrage. Le contrôle des copies de travail ne remplace pas la vérification EWF de l’acquisition.

### 10.9. Conclusions de cette étape et suites ciblées

**Les constats positifs sont :** des exports et un regroupement de données autour du 28 octobre 2024 ; trois identifiants de supports Kingston présents ce jour-là ; une détection de PDF de phishing en mai 2024 et une piste de téléassistance Rescue en octobre 2023. **Aucun transfert sortant de fichiers déterminés, aucune compromission réussie et aucune exfiltration antérieure au 15 octobre ne sont démontrés dans les artefacts examinés.**

Les suites utiles sont de rapprocher les identifiants Kingston et l’ensemble `L16B` des opérations détaillées au procès-verbal du 28 ; rechercher, si les supports ou leurs images existent, les copies correspondantes et leurs empreintes ; obtenir les historiques de sécurité/connexions/export des comptes Google, Microsoft, Dropbox et Apple encore disponibles ; confronter la piste Rescue à une éventuelle intervention d’assistance le 06/10/2023 et rechercher ses traces complémentaires ; rechercher le message d’origine du PDF de mai 2024 et son contenu dans les archives de messagerie disponibles, sans supposer que les PST/MBOX présents le contiennent. La Freebox pourrait aider à identifier `192.168.1.139` si un historique de bail de mars 2024 subsiste, ce qui n’est pas établi ici.

Restent non réalisés : audit exhaustif de chaque binaire/signature et mécanisme de persistance, validation et recherche interne des PST/MBOX, audit des caches de synchronisation cloud, contenu des autres équipements ou des supports Kingston, analyse détaillée des Jump Lists et de ShimCache, récupération `$LogFile`, mémoire historique et carving intégral de l’espace non alloué. Aucun scan antivirus exécuté sur le système acquis ni restauration de quarantaine n’a été effectué.

## 11. Conclusion et suites utiles

**OP-01 a repris Windows le 15 octobre vers 10 h 43 puis le 28 vers 10 h 41. Son utilisation le 28 après ouverture déclarée et avant restitution est étayée par plusieurs familles d’artefacts. Aucune activité Windows corroborée n’a été établie dans l’intervalle central entre l’hibernation et l’ouverture déclarée.**

Le champ du 16 octobre est une échéance programmée, pas une preuve de réveil. Sa programmation n’est pas datée. Les contrôles n’établissent pas d’effacement ou de falsification destiné à masquer une activité, malgré des anomalies d’en-tête documentées. Les dates de fichiers pendant la rétention existent et ont été examinées ; leur provenance et leurs changements ultérieurs empêchent de les transformer en preuve d’allumage local à ces dates.

La conclusion ne permet pas d’exclure : réécriture cohérente des journaux/CRC/compteurs, horloge erronée, activité non journalisée, démarrage externe, lecture hors ligne du SSD, traces définitivement écrasées ou opérations ne laissant pas les artefacts recherchés. Security et USN ne couvrent plus 2024 ; l’acquisition intervient près de deux ans après les faits. Les dates et compteurs ne constituent pas des signatures inviolables.

Pour consolider le rapprochement factuel, obtenir les procès-verbaux précisant **début de perquisition, fermeture des scellés, ouverture, opérations réalisées le 28 et restitution**. Clarifier également les divergences des notes de remise et des horaires d’acquisition de 2026, et la provenance des ensembles iCloud/L16B.

La seconde étape (§ 10) établit la présence de données exportées et un regroupement daté principalement du 28 octobre, ainsi que des installations de supports Kingston ce jour-là. Elle documente une détection de PDF de phishing en mai 2024 et une piste de téléassistance Rescue en octobre 2023, sans établir de compromission réussie ni d’exfiltration antérieure à la perquisition. Les recherches non réalisées et les suites ciblées figurent au § 10.9. Aucun cliché VSS illisible n’a été restauré.

Les résultats décrits sont conservés localement dans le projet ; la conservation cloud pour la durée contractuelle et la copie sur le disque neuf fourni par la cliente ne sont pas réalisées par ces seules investigations et restent à organiser séparément.

## 12. Références techniques

Les références ci-dessous étayent la méthode et les interprétations de format ; les constatations propres à OP-01 proviennent des pièces d’analyse citées dans le document.

- [Microsoft — SYSTEM_POWER_STATE](https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-system_power_state) : valeur 5, S4/hibernation.
- [Microsoft — événement 4624 et types de session](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624).
- [Microsoft — notifications Winlogon](https://learn.microsoft.com/en-us/windows/win32/secauthn/winlogon-notification-events) : description des notifications, pas validation locale des codes numériques 4/5.
- [Microsoft — WakeToRun](https://learn.microsoft.com/en-us/windows/win32/taskschd/taskschedulerschema-waketorun-settingstype-element), [SetWaitableTimer](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer), [maintenance automatique](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence) et [RegistrationInfo.Date](https://learn.microsoft.com/en-us/windows/win32/taskschd/registrationinfo-date).
- [Microsoft — événement 4702](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4702), [1102](https://learn.microsoft.com/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-1102) et [wevtutil / conservation](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wevtutil).
- [libevtx — format EVTX](https://github.com/libyal/libevtx/blob/main/documentation/Windows%20XML%20Event%20Log%20%28EVTX%29.asciidoc) : en-têtes, CRC, enregistrements et incohérences connues.
- [libfsntfs — format NTFS](https://github.com/libyal/libfsntfs/blob/main/documentation/New%20Technologies%20File%20System%20%28NTFS%29.asciidoc) : SI/FN, références MFT et USN.
- [libvshadow — format VSS](https://github.com/libyal/libvshadow/blob/main/documentation/Volume%20Shadow%20Snapshot%20%28VSS%29%20format.asciidoc) : catalogue et dates de création.

- [Microsoft — détection/remédiation Defender 1116/1117 et changements de configuration](https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus).
- [LogMeIn Rescue — connexion à une session par code](https://www.logmeinrescue.com/-/media/6a893c89d119416e9595cb8ad18514a2.pdf).
- [libyal — schéma des tables SRUM et dates OLE](https://github.com/libyal/esedb-kb/blob/main/documentation/System%20Resource%20Usage%20Monitor%20%28SRUM%29.asciidoc).
- [MemProcFS — Amcache et limite présence/exécution](https://github.com/ufrisk/MemProcFS/wiki/FS_Forensic_Amcache) : l’inventaire Amcache ne prouve pas à lui seul l’exécution.
