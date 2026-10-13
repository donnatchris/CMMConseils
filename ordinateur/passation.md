# PASSATION À CODEX — INVESTIGATION FORENSIC OP-01

**Affaire :** SADEDINE-2026  
**Pièce :** OP-01 — Ordinateur portable Windows de Mme Malika Sadedine  
**Date de la passation :** 13 octobre 2026  
**État :** Acquisition terminée, image E01 déchiffrée et montée en lecture seule. Analyse des journaux Windows commencée.

## 1. Contexte et objectifs de la mission

Mme Sadedine a fait l'objet d'une perquisition fiscale le 15 octobre 2024. Son ordinateur portable et ses téléphones ont été placés sous scellés avant de lui être restitués le 28 octobre 2024.

La mission est une investigation informatique privée, et non une expertise judiciaire ordonnée par une juridiction.

La cliente souhaite déterminer, dans la mesure où les artefacts disponibles le permettent :

- Si son ordinateur a été allumé, déverrouillé ou utilisé pendant la période de rétention.
- Si des utilisateurs ont ouvert une session Windows.
- Si des documents ont été consultés, copiés, déplacés, modifiés ou supprimés.
- Si des périphériques USB ou supports externes ont été connectés.
- Si des logiciels d'extraction, d'administration ou de prise en main à distance ont été utilisés.
- Si des traces permettent de détecter des connexions inhabituelles avant ou pendant la période de la perquisition.
- Si les événements observés sont compatibles avec une utilisation normale, une opération technique ou une intervention extérieure.

Les constatations doivent rester objectives. Il ne faut pas attribuer une opération à une personne sans preuves suffisantes.

### Dates communiquées par la cliente

| Date | Événement |
|---|---|
| 15/10/2024 | Perquisition fiscale ; la cliente perd l'accès au PC dès le début de l'intervention |
| 28/10/2024 vers 10h22 | Début de l'ouverture des scellés dans les locaux de l'administration |
| 28/10/2024 vers 19h20 | Restitution des appareils |

Période prioritaire : **15 au 28 octobre 2024**, avec extension au 14 et au 29 octobre pour éviter les erreurs de bornes temporelles et faciliter les recoupements.

Toutes les heures des événements Windows doivent être conservées en UTC et converties en heure française avec `Europe/Paris`.

Attention au changement d'heure du 27 octobre 2024 :

- 15 octobre : UTC+2.
- 28 octobre : UTC+1.

## 2. Environnement de travail

Machine hôte : Ubuntu.

Machines virtuelles disponibles :

- **SIFT Workstation**, utilisée actuellement pour l'analyse.
- Windows 11 avec Autopsy, disponible pour les analyses ultérieures.

Outils déjà employés :

- Guymager pour l'acquisition.
- `ewfinfo`
- `ewfmount`
- `mmls`
- `blkid`
- `losetup`
- `dislocker`
- `ntfs-3g`
- `evtxexport` (libevtx version 20251118)
- `awk`

Le module Python `python-evtx` n'est pas installé dans le Python système de SIFT. Il n'a pas été nécessaire de l'installer puisque `evtxexport` fonctionne.

## 3. Acquisition forensic du PC

L'acquisition a été réalisée avec Guymager le 12 octobre 2026.

Métadonnées récupérées par `ewfinfo` :

```text
Case number:          SADEDINE-2026
Description:          Image disque du PC de Mme Sadedine
Examiner name:        Christophe Donnat
Evidence number:      OP-01
Acquisition date:     Mon Oct 12 09:21:57 2026
Software:             guymager 0.8.13-1
Model:                INTEL SSDPEKNW512G8
Serial number:        BTNH93120FL8512A
File format:          EnCase 6
Compression method:   deflate
Bytes per sector:     512
Number of sectors:    1000215216
Media size:           476 GiB (512110190592 bytes)
MD5:                  10c9f3df1ecd999567a05beaa4056ace
```

Le MD5 ci-dessus est l'empreinte enregistrée dans les métadonnées EWF. Aucune vérification complète par `ewfverify` n'a encore été rapportée.

### Emplacement des acquisitions

L'image est composée de 74 segments :

```text
OP01.E01
OP01.E02
...
OP01.E74
OP01.info
```

Chemin dans la VM SIFT :

```bash
/media/shared/forensic/SADEDINE-2026/OP-01/
```

Image principale :

```bash
/media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01
```

Le répertoire `/media/shared/` est un partage provenant du disque de l'hôte Ubuntu.

**Précaution :** vérifier que le partage contenant les acquisitions est bien en lecture seule. Les originaux ne doivent jamais être modifiés.

## 4. Montage de l'image E01

### Étape 1 : montage EWF

Commandes réalisées :

```bash
sudo mkdir -p /mnt/ewf

sudo ewfmount \
  /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01 \
  /mnt/ewf
```

Résultat :

```text
/mnt/ewf/ewf1
```

Ce fichier virtuel expose l'image du disque physique complet.

Le montage FUSE nécessite actuellement des droits root pour l'accès.

### Étape 2 : identification des partitions

Commande :

```bash
sudo mmls /mnt/ewf/ewf1
```

Structure GPT identifiée :

| Partition GPT | Secteur de départ | Taille | Type |
|---|---:|---:|---|
| 000 | 2048 | 260 Mio | EFI System |
| 001 | 534528 | 16 Mio | Microsoft Reserved |
| 002 | 567296 | 475,84 Gio | Basic Data |
| 003 | 998473728 | 848 Mio | Probable récupération Windows |

Le disque utilise des secteurs logiques de 512 octets.

La partition principale débute donc à l'offset :

```text
567296 × 512 = 290455552 octets
```

### Étape 3 : identification de BitLocker

Commande :

```bash
sudo blkid -p -O $((567296 * 512)) /mnt/ewf/ewf1
```

Résultat :

```text
/mnt/ewf/ewf1: VERSION="2" TYPE="BitLocker" USAGE="crypto"
```

Le chiffrement BitLocker a donc été confirmé.

## 5. Création du périphérique loop

Un périphérique loop a été créé en lecture seule avec `losetup`.

Commande utilisée :

```bash
sudo losetup -fP --read-only --show /mnt/ewf/ewf1
```

Le périphérique obtenu est :

```text
/dev/loop14
```

Vérification :

```bash
sudo lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT /dev/loop14
```

Résultat :

```text
NAME         SIZE FSTYPE    TYPE MOUNTPOINT
loop14     476.9G           loop
├─loop14p1   260M vfat      part
├─loop14p2    16M           part
├─loop14p3 475.8G BitLocker part
└─loop14p4   848M ntfs      part
```

Partition principale à analyser :

```text
/dev/loop14p3
```

Les numéros de loop peuvent changer après redémarrage. Ne pas supposer que `/dev/loop14` sera permanent.

## 6. Déverrouillage BitLocker

Outil : Dislocker.

Répertoires :

```bash
sudo mkdir -p /mnt/dislocker /mnt/windows
```

Commande réalisée :

```bash
sudo dislocker -r \
  -V /dev/loop14p3 \
  -p \
  -- /mnt/dislocker
```

La clé de récupération BitLocker à 48 chiffres a été saisie localement. Elle ne doit pas être inscrite dans les scripts, les journaux de commandes ou le rapport.

Résultat :

```text
Valid password format, continuing.
```

Code retour :

```text
0
```

Le répertoire `/mnt/dislocker/` contient :

```text
-r--r--r-- 1 root root 477G Jan 1 1970 dislocker-file
```

Le fichier `dislocker-file` est une vue virtuelle déchiffrée, pas une copie de 477 Go.

La date du 1er janvier 1970 correspond à la représentation technique du fichier virtuel et ne doit pas être considérée comme un indice d'activité.

## 7. Montage NTFS déchiffré

Commande exécutée avec succès :

```bash
sudo mount -t ntfs-3g \
  -o ro,norecover \
  /mnt/dislocker/dislocker-file \
  /mnt/windows
```

Le système de fichiers Windows est maintenant accessible via :

```text
/mnt/windows/
```

Principaux dossiers observés :

```text
/mnt/windows/Windows
/mnt/windows/Users
/mnt/windows/Program Files
/mnt/windows/Program Files (x86)
/mnt/windows/ProgramData
/mnt/windows/Recovery
/mnt/windows/System Volume Information
```

Autres éléments observés :

```text
hiberfil.sys     7.9G
pagefile.sys     5.3G
swapfile.sys      16M
```

Ces fichiers portent des dates de modification du 12 octobre 2026. Ils pourront être analysés ultérieurement si cela présente un intérêt.

**Important :** le système de fichiers est actuellement monté en lecture seule. Il faut conserver cette protection pendant l'investigation.

## 8. Découverte des journaux EVTX

Répertoire :

```bash
/mnt/windows/Windows/System32/winevt/Logs/
```

Nombre de fichiers EVTX :

```text
359
```

Trois journaux principaux identifiés :

| Fichier | Taille | Date de modification affichée |
|---|---:|---|
| `System.evtx` | 21 Mo | 12/10/2026 |
| `Security.evtx` | 21 Mo | 12/10/2026 |
| `Application.evtx` | 12 Mo | 12/10/2026 |

Ces dates correspondent aux métadonnées des fichiers et non aux bornes temporelles des événements.

### Outil de lecture

La VM SIFT possède :

```text
/usr/bin/evtxexport
```

Version :

```text
evtxexport 20251118
```

Lecture :

```bash
sudo evtxexport -f text \
  /mnt/windows/Windows/System32/winevt/Logs/System.evtx
```

La sortie contient les champs :

```text
Event number
Creation time
Written time
Event version
Event level
Computer name
Source name
Channel name
Event identifier
Number of strings
String: 1...
```

Nom Windows observé :

```text
LAPTOP-RMCOB2VU
```

## 9. Première extraction chronologique

Le journal `System.evtx` contient notamment des événements à partir du 7 octobre 2024.

Un filtrage a été réalisé pour les événements datés du 15 au 28 octobre 2024 inclus, sur la base des dates UTC.

Résultat :

```text
Total événements trouvés : 774
```

Répartition :

- 15 octobre 2024 : 80 événements.
- 28 octobre 2024 : 694 événements.
- Aucun événement retourné du 16 au 27 octobre 2024 dans ce journal avec ce filtre.

Ces chiffres concernent uniquement `System.evtx`, et non l'ensemble des 359 journaux.

Le filtre ne couvre pas non plus les portions UTC adjacentes qui peuvent correspondre à des dates civiles françaises. Une analyse définitive devra appliquer les bornes en heure `Europe/Paris`.

### Événements importants identifiés

**15 octobre 2024 :**

- 08:43 UTC : activité `Kernel-General`, `Kernel-Boot`, `Kernel-Power`, `Winlogon`, `Power-Troubleshooter`.
- 08:53 UTC : événements `Kernel-Power` liés à l'alimentation et à la veille.

**28 octobre 2024 :**

- 09:41:56 UTC : nouvelle activité `Kernel-General`, `Kernel-Boot`, `Kernel-Power`.
- 09:41:58 UTC : événement `Power-Troubleshooter`.

Ces événements ont ensuite été extraits intégralement.

## 10. Analyse approfondie des quatre événements remarquables

### Événement 37385 — Power-Troubleshooter

```text
Event number : 37385
Creation time : Oct 15, 2024 08:43:02.169062300 UTC
Source name : Microsoft-Windows-Power-Troubleshooter
Event identifier : 1

String: 1 : 2024-10-10T20:34:30.164899500Z
String: 2 : 2024-10-15T08:43:00.851496500Z
```

Interprétation préliminaire :

- Entrée dans un état de veille ou faible consommation le 10 octobre à 22h34min30s (heure française).
- Reprise le 15 octobre à 10h43min00s (heure française).

Ces valeurs sont cohérentes avec les champs usuels SleepTime et WakeTime de Power-Troubleshooter, à confirmer par l'examen XML des noms des champs.

### Événement 37445 — Kernel-Power

```text
Event number : 37445
Creation time : Oct 15, 2024 08:53:07.255679100 UTC
Source name : Microsoft-Windows-Kernel-Power
Event identifier : 42

String: 1 : 5
String: 2 : 5
String: 3 : 2
String: 4 : 0
String: 5 : 4
```

Cet événement est associé à une transition vers un état de veille.

Horaire français de l'événement : **15 octobre 2024 à 10h53min07s**.

Les valeurs numériques doivent être interprétées avec le schéma du fournisseur Windows correspondant à cette version de l'événement.

### Événement 37447 — Kernel-Power

```text
Event number : 37447
Creation time : Oct 15, 2024 08:53:08.371843800 UTC
Source name : Microsoft-Windows-Kernel-Power
Event identifier : 107

String: 1 : 5
String: 2 : 5
String: 3 : 5
String: 4 : 2024-10-16T03:51:07.133163100Z
String: 5 : 1601-01-01T00:00:00.000000000Z
String: 6 : 2
String: 7 : 0
```

### POINT CRITIQUE À APPROFONDIR — DATE DU 16 OCTOBRE 2024

**Le champ `String: 4` mentionne explicitement :**

```text
2024-10-16T03:51:07.133163100Z
```

Cela correspond au :

**16 octobre 2024 à 05h51min07s, heure française (UTC+2).**

Or :

- L'événement lui-même est daté du **15 octobre à 10h53min08s**.
- La date contenue dans `String: 4` est postérieure de près de 19 heures à son horodatage.
- Cette date se situe pendant la période où la cliente n'avait plus accès à son ordinateur.
- Aucun événement daté du 16 octobre n'a été trouvé dans le filtrage précédent de `System.evtx`.

**Il ne faut absolument pas interpréter cette valeur comme la preuve d'une activité du PC le 16 octobre.**

C'est une valeur contenue dans les données de l'événement, dont la signification technique doit être établie.

Missions prioritaires pour Codex :

1. Extraire cet événement au format XML.
2. Identifier le schéma Microsoft-Windows-Kernel-Power, Event ID 107, version 1.
3. Retrouver le nom du champ correspondant à `String: 4`.
4. Déterminer s'il s'agit d'une date de réveil, d'une date prévue, d'une valeur issue du firmware, d'un horodatage interne ou d'un autre champ.
5. Comprendre pourquoi une date postérieure figure dans un événement enregistré le 15 octobre.
6. Rechercher des artefacts indépendants susceptibles de confirmer ou d'infirmer une activité effective le 16 octobre.
7. Documenter explicitement cette anomalie dans les notes d'investigation, sans conclure prématurément.

L'autre date :

```text
1601-01-01T00:00:00.000000000Z
```

correspond à l'époque utilisée par les horodatages Windows FILETIME et peut servir de valeur nulle ou sentinelle. Sa signification exacte dans cet événement reste à vérifier.

**Ne pas perdre de vue cet événement : il constitue un point de recherche ouvert.**

### Événement 37466 — Power-Troubleshooter

```text
Event number : 37466
Creation time : Oct 28, 2024 09:41:58.563879200 UTC
Source name : Microsoft-Windows-Power-Troubleshooter
Event identifier : 1

String: 1 : 2024-10-15T08:53:05.821076800Z
String: 2 : 2024-10-28T09:41:56.825085600Z
```

Conversion en heure française :

- `String: 1` : 15 octobre 2024 à 10h53min05s.
- `String: 2` : 28 octobre 2024 à 10h41min56s.

Interprétation préliminaire :

Le journal signale une transition de faible consommation commencée le 15 octobre et terminée le 28 octobre.

Cela est cohérent avec une période prolongée sans reprise normale enregistrée.

Cependant, ces deux valeurs ne prouvent pas à elles seules que la machine est restée continuellement inactive ou qu'aucune autre opération n'a eu lieu.

## 11. Chronologie provisoire

| Date et heure française | Événement | Certitude |
|---|---|---|
| 10/10/2024 22h34 | Début de veille indiqué dans l'événement 37385 | Horodatage présent ; interprétation à confirmer en XML |
| 15/10/2024 10h43 | Reprise enregistrée par Power-Troubleshooter | Forte pour la présence de l'événement |
| 15/10/2024 10h53 | Kernel-Power 42, transition vers la veille | Forte pour la présence de l'événement |
| 15/10/2024 10h53 | Kernel-Power 107 contenant une date du 16 octobre | Signification du champ non résolue |
| 16/10/2024 05h51 | Date mentionnée dans String: 4 de l'événement 37447 | **Ne constitue pas un événement autonome confirmé** |
| 28/10/2024 10h41 | Reprise enregistrée par Power-Troubleshooter | Forte pour la présence de l'événement |

La reprise du 28 octobre à 10h41 intervient environ 20 minutes après l'ouverture des scellés annoncée à 10h22.

Cette concordance temporelle est intéressante mais ne permet pas d'attribuer la manipulation à un intervenant identifié.

## 12. Dernière opération proposée, pas encore exécutée

Nous étions sur le point d'interroger `Security.evtx` afin d'identifier les ouvertures de sessions Windows.

Commande proposée :

```bash
sudo evtxexport -f text \
  /mnt/windows/Windows/System32/winevt/Logs/Security.evtx \
  | awk '
    BEGIN { RS=""; FS="\n" }
    /Creation time[[:space:]]*:[[:space:]]*Oct (15|28), 2024/ {
      event=""; date=""; id=""
      for (i=1; i<=NF; i++) {
        if ($i ~ /^Event number/) event=$i
        if ($i ~ /^Creation time/) date=$i
        if ($i ~ /^Event identifier/) id=$i
      }
      if (id ~ /\((4624|4625|4634|4647|4648|4672|4688|1102)\)/) {
        print event " | " date " | " id
      }
    }
  '
```

Cette commande n'a pas encore été exécutée dans la conversation.

Elle est utile comme premier filtrage, mais Codex devrait privilégier une extraction structurée (XML, JSON ou CSV) plutôt que des analyses complexes fondées uniquement sur le texte brut.

### Event ID à rechercher dans Security.evtx

| Event ID | Signification |
|---|---|
| 4624 | Ouverture de session réussie |
| 4625 | Échec d'ouverture de session |
| 4634 | Fermeture de session |
| 4647 | Déconnexion initiée par un utilisateur |
| 4648 | Authentification avec identifiants explicites |
| 4672 | Privilèges spéciaux attribués |
| 4688 | Création d'un processus si audit activé |
| 1102 | Effacement du journal de sécurité |

Pour `4624`, examiner particulièrement :

- `LogonType 2` : session interactive locale.
- `LogonType 3` : ouverture de session réseau.
- `LogonType 7` : déverrouillage de session.
- `LogonType 10` : session Remote Desktop.
- `LogonType 11` : connexion interactive avec identifiants en cache.

Il faut aussi examiner les noms de comptes, SID, Logon ID, adresses IP éventuelles et corrélations temporelles.

## 13. Travaux recommandés pour la suite

### Priorité 1 — Consolider la chronologie système

Extraire les événements complets et structurés de `System.evtx` pour la période étudiée.

Rechercher notamment :

- Démarrages.
- Arrêts.
- Entrées et sorties de veille.
- Changements d'horloge.
- Modifications de services.
- Événements susceptibles de révéler des interruptions ou des anomalies.

Examiner les fournisseurs et identifiants conjointement, et non les Event ID isolément.

### Priorité 2 — Résoudre l'anomalie du 16 octobre

Étudier l'événement 37447, en particulier :

```text
String: 4 : 2024-10-16T03:51:07.133163100Z
```

Cette recherche est explicitement prioritaire et doit rester ouverte jusqu'à identification documentée du champ.

### Priorité 3 — Analyser Security.evtx

Déterminer :

- Si des sessions interactives ont été ouvertes le 15 et le 28 octobre.
- À quelles heures.
- Sous quels comptes.
- Si des authentifications réseau ou distantes apparaissent.
- Si des événements de sécurité inhabituels ont été enregistrés.

### Priorité 4 — Chercher les traces de consultation et d'extraction

Artefacts Windows à examiner :

- `$MFT`
- `$UsnJrnl`
- `$LogFile`
- Prefetch
- Amcache
- ShimCache
- LNK
- Jump Lists
- USBSTOR
- `setupapi.dev.log`
- SRUM
- Registres SYSTEM, SOFTWARE et NTUSER.DAT
- Journaux PowerShell et TerminalServices
- Éventuelles traces d'exécution d'outils d'acquisition, de copie ou de prise en main distante

Attention : chaque artefact possède ses propres limites. Une date d'accès à un fichier, une trace d'exécution ou une présence USB ne démontrent pas automatiquement une consultation humaine ou une extraction effective.

### Priorité 5 — Préparer les résultats exploitables

Conserver les sorties d'analyse dans un répertoire de travail distinct des preuves originales.

Structure suggérée :

```text
SADEDINE-2026/
└── analysis/
    └── OP-01/
        ├── exports/
        │   ├── evtx/
        │   ├── registry/
        │   ├── filesystem/
        │   └── usb/
        ├── timelines/
        ├── findings/
        ├── hashes/
        └── scripts/
```

Produire une chronologie CSV avec, au minimum :

```text
timestamp_utc
timestamp_europe_paris
artifact
event_id
provider
record_id
account
description
source_file
interpretation
confidence
```

Les interprétations doivent être clairement distinguées des données brutes.

## 14. Précautions de méthode forensic

- Ne jamais modifier les fichiers E01 d'origine.
- Maintenir la chaîne EWF / loop / Dislocker / NTFS en lecture seule.
- Vérifier l'intégrité EWF avec `ewfverify`.
- Calculer et conserver les empreintes des éléments extraits si utilisés dans le rapport.
- Documenter les commandes, versions d'outils, dates et résultats.
- Préserver les données brutes avant traitement.
- Conserver les horodatages UTC originaux.
- Produire les heures françaises uniquement par conversion explicite.
- Ne jamais assimiler absence d'événement et absence d'activité.
- Ne pas attribuer une action à une personne sans recoupement.
- Ne pas qualifier un accès d'autorisé ou non autorisé sur la seule base d'un journal technique.
- Ne pas exposer la clé BitLocker dans les fichiers générés.

## 15. Instruction de reprise pour Codex

Reprendre cette investigation à partir de l'état actuel de la VM SIFT, en avançant étape par étape.

**Objectif immédiat :** déterminer les ouvertures de sessions Windows du 15 et du 28 octobre 2024, puis approfondir la signification du champ du 16 octobre dans l'événement Kernel-Power 107.

Commencer par vérifier la disponibilité des montages :

```bash
findmnt /mnt/windows
sudo ls /mnt/windows/Windows/System32/winevt/Logs/System.evtx
sudo ls /mnt/windows/Windows/System32/winevt/Logs/Security.evtx
```

Si les montages ne sont plus présents, les reconstruire en lecture seule selon les opérations décrites précédemment.

Ne pas relancer `losetup` ou `dislocker` inutilement si leurs montages existent déjà.

Ne pas lancer d'extraction massive, de conversion intégrale ou d'installation de dépendances sans avoir vérifié les outils disponibles, la destination des résultats et l'espace de stockage.

L'utilisateur souhaite comprendre les méthodes forensic employées. Expliquer les commandes et leur raison d'être avant les étapes importantes.

**Point à ne pas oublier :**

```text
Event number : 37447
Source : Microsoft-Windows-Kernel-Power
Event ID : 107
Event timestamp : 2024-10-15 08:53:08 UTC
String: 4 : 2024-10-16T03:51:07.133163100Z
```

Cette date du 16 octobre doit être investiguée et interprétée techniquement, sans la présenter prématurément comme une preuve d'utilisation de l'ordinateur.

**Fin de passation.**