# Cours — Disques, partitions et systèmes de fichiers

## Objectifs

À la fin de ce cours, vous saurez :

* distinguer un disque, une partition et un système de fichiers ;
* reconnaître les principaux types de disques ;
* comprendre les tables de partitions MBR et GPT ;
* choisir un système de fichiers adapté ;
* identifier, partitionner, formater et monter un disque sous Linux ;
* comprendre les rôles de LVM, du RAID et du chiffrement ;
* surveiller la santé d'un disque et adopter de bonnes pratiques de sauvegarde.

> **Attention :** plusieurs commandes de ce cours peuvent détruire définitivement des données. Avant d'utiliser `fdisk`, `parted`, `mkfs`, `wipefs` ou `dd`, vérifiez toujours le nom du périphérique avec `lsblk`. Dans les exemples, `/dev/sdX` désigne volontairement un disque fictif.

---

## 1. La grande analogie : un immeuble de rangement

On peut comparer un disque à un immeuble :

```text
Disque physique       = le terrain et l'immeuble
Table de partitions   = le plan général de l'immeuble
Partition             = un appartement délimité sur ce plan
Système de fichiers   = la méthode de classement dans l'appartement
Fichier               = un objet rangé dans l'appartement
Point de montage      = la porte permettant d'entrer dans l'appartement
```

Cette distinction est fondamentale :

```text
Disque → table de partitions → partition → système de fichiers → fichiers
```

Un disque peut contenir plusieurs partitions. Chaque partition peut avoir son propre système de fichiers. Une partition formatée ne devient accessible sous Linux qu'après avoir été **montée** dans l'arborescence.

Il existe aussi des cas particuliers :

* un système de fichiers peut occuper un disque entier sans table de partitions ;
* une partition peut contenir du swap, un volume chiffré ou un volume LVM au lieu d'un système de fichiers directement utilisable ;
* plusieurs disques peuvent être regroupés avec RAID ou LVM ;
* un fichier peut lui-même servir de disque virtuel.

---

## 2. Les grandes familles de supports

### 2.1 Le disque dur mécanique — HDD

**HDD** signifie *Hard Disk Drive*.

Un HDD contient des plateaux magnétiques qui tournent et une tête de lecture qui se déplace. Il ressemble à une immense bibliothèque dans laquelle un petit robot doit physiquement rejoindre la bonne étagère.

Avantages :

* grande capacité pour un prix modéré ;
* adapté à l'archivage, aux sauvegardes et aux gros volumes ;
* bonne endurance pour les écritures répétées.

Inconvénients :

* plus lent, surtout pour de nombreux petits fichiers ;
* sensible aux chocs lorsqu'il fonctionne ;
* bruit, vibrations et consommation électrique ;
* pièces mécaniques sujettes à l'usure.

Vitesses courantes de rotation : `5 400 tr/min` et `7 200 tr/min`.

### 2.2 Le disque à mémoire flash — SSD

**SSD** signifie *Solid-State Drive*.

Il stocke les données dans de la mémoire flash et ne possède aucune pièce mobile. C'est comme remplacer le robot de la bibliothèque par un système électronique capable d'ouvrir presque instantanément n'importe quel casier.

Avantages :

* accès très rapide ;
* silencieux ;
* faible consommation ;
* résiste mieux aux chocs physiques.

Inconvénients :

* prix par téraoctet généralement supérieur à celui d'un HDD ;
* cellules flash ayant un nombre limité de cycles d'écriture ;
* récupération de données parfois difficile après une panne électronique.

Un SSD répartit les écritures entre ses cellules, technique appelée **wear leveling**. Il conserve aussi souvent une réserve invisible appelée **over-provisioning**.

### 2.3 SATA, SAS, NVMe : interfaces et protocoles

Il ne faut pas confondre la technologie de stockage et son moyen de communication.

* **SATA** : très courant pour les HDD et SSD 2,5 pouces ;
* **SAS** : surtout utilisé dans les serveurs, robuste et prévu pour un usage intensif ;
* **NVMe** : protocole conçu pour la mémoire flash, généralement transporté par PCI Express ;
* **USB** : permet de connecter des boîtiers externes, clés USB et cartes mémoire ;
* **iSCSI** : présente un stockage distant sur le réseau comme un périphérique bloc local.

Un SSD peut donc être un SSD SATA ou un SSD NVMe. **M.2** décrit surtout un format physique : un module M.2 peut utiliser SATA ou NVMe.

### 2.4 Clés USB, cartes SD et disques externes

Ces supports utilisent aussi de la mémoire flash ou un disque mécanique, mais leur contrôleur et leur qualité varient beaucoup. Ils conviennent au transport et à l'échange, mais une clé USB ordinaire ne doit pas être considérée comme une sauvegarde unique et permanente.

### 2.5 Stockage réseau

Un **NAS** est une machine qui partage des fichiers sur le réseau, par exemple avec SMB ou NFS. Ce n'est pas simplement un disque : c'est un ordinateur spécialisé qui peut contenir plusieurs disques.

Différence utile :

```text
Stockage bloc   : le système voit des blocs bruts, comme avec un disque local ou iSCSI.
Stockage fichier: le système accède à des fichiers partagés, comme avec NFS ou SMB.
```

---

## 3. Capacité, secteurs et blocs

### 3.1 Bits, octets et unités

Un octet contient 8 bits.

Les fabricants utilisent généralement les unités décimales :

```text
1 kB = 1 000 octets
1 MB = 1 000 000 octets
1 GB = 1 000 000 000 octets
1 TB = 1 000 000 000 000 octets
```

Linux peut aussi afficher les unités binaires :

```text
1 KiB = 1 024 octets
1 MiB = 1 024 KiB
1 GiB = 1 024 MiB
1 TiB = 1 024 GiB
```

C'est pourquoi un disque vendu comme « 1 TB » apparaît avec environ `931 GiB`. Aucune capacité n'a disparu : les unités diffèrent.

### 3.2 Les secteurs

Le disque est découpé en petites unités adressables appelées **secteurs**. Les tailles courantes sont :

* 512 octets pour les anciens disques ;
* 4 096 octets pour les disques modernes dits *Advanced Format*.

Le système repère les secteurs à l'aide d'adresses logiques appelées **LBA** (*Logical Block Addressing*), comme des numéros de maisons dans une rue.

### 3.3 Les blocs du système de fichiers

Le système de fichiers regroupe généralement les données en blocs, souvent de 4 KiB. Le bloc du système de fichiers et le secteur du disque sont deux notions différentes.

Un fichier d'un octet peut donc occuper un bloc entier. À l'inverse, un fichier « creux » ou **sparse file** peut avoir une taille apparente supérieure à l'espace réellement occupé.

Comparer les deux :

```bash
ls -lh fichier.img
du -h fichier.img
```

### 3.4 L'alignement

Les partitions doivent commencer sur des limites adaptées aux secteurs physiques et aux SSD. Un mauvais alignement peut forcer plusieurs opérations physiques pour une seule écriture logique et réduire les performances.

Les outils modernes alignent normalement les partitions sur des multiples de 1 MiB.

---

## 4. Comment Linux nomme les disques

Linux représente les périphériques dans `/dev`.

Exemples fréquents :

```text
/dev/sda      premier disque SATA, SAS ou USB
/dev/sdb      deuxième disque SATA, SAS ou USB
/dev/sda1     première partition du disque /dev/sda
/dev/sda2     deuxième partition du disque /dev/sda

/dev/nvme0n1    premier espace de noms du premier disque NVMe
/dev/nvme0n1p1  première partition de ce disque NVMe

/dev/mmcblk0    carte SD ou stockage eMMC
/dev/mmcblk0p1  première partition correspondante

/dev/vda      disque virtuel fréquent dans une machine virtuelle
/dev/loop0    périphérique boucle associé à un fichier
```

Les noms `/dev/sda` ou `/dev/sdb` peuvent changer selon l'ordre de détection. Pour une configuration permanente, on préfère généralement les identifiants UUID disponibles dans `/dev/disk/by-uuid/`.

### Commandes d'identification

Afficher les périphériques sous forme d'arbre :

```bash
lsblk
```

Afficher les systèmes de fichiers, labels et UUID :

```bash
lsblk -f
```

Afficher le modèle, la taille et le type de rotation :

```bash
lsblk -o NAME,MODEL,SERIAL,SIZE,TYPE,FSTYPE,MOUNTPOINTS,ROTA
```

Dans la colonne `ROTA`, `1` désigne normalement un disque rotatif et `0` un SSD.

Obtenir des informations sur les signatures présentes :

```bash
sudo blkid
```

Lister les liens stables vers les disques :

```bash
ls -l /dev/disk/by-id/
ls -l /dev/disk/by-uuid/
```

Voir les derniers messages du noyau après avoir branché un disque :

```bash
sudo dmesg --follow
```

Sur certains systèmes, l'accès à `dmesg` est restreint. On peut alors utiliser :

```bash
sudo journalctl -kf
```

> **Réflexe de sécurité :** débranchez le disque externe, exécutez `lsblk`, rebranchez-le, puis exécutez de nouveau `lsblk`. Le nouveau périphérique est probablement le bon, mais vérifiez également son modèle et sa taille.

---

## 5. La table de partitions

La table de partitions est le plan du disque. Elle indique où chaque partition commence, où elle se termine et quel est son type.

Les deux formats principaux sont **MBR** et **GPT**.

### 5.1 MBR — Master Boot Record

MBR, aussi appelé table `dos` par certains outils, est un ancien format créé pour les PC utilisant le BIOS.

Caractéristiques :

* table située au début du disque ;
* limite pratique d'environ 2 TiB avec des secteurs de 512 octets ;
* quatre entrées de partitions principales maximum ;
* possibilité de contourner cette limite avec une partition étendue contenant des partitions logiques ;
* pas de copie de secours native de la table.

Analogie : le MBR est un ancien formulaire ne possédant que quatre cases. Pour créer plus de pièces, une case doit contenir un sous-plan appelé partition étendue.

Types de partitions MBR :

* **primaire** : partition normale, quatre maximum ;
* **étendue** : conteneur occupant une des quatre entrées ;
* **logique** : partition créée à l'intérieur de la partition étendue.

### 5.2 GPT — GUID Partition Table

GPT est le format moderne associé à l'UEFI.

Caractéristiques :

* prend en charge les très grands disques ;
* accepte généralement 128 partitions ou plus ;
* donne un identifiant unique, ou GUID, à chaque partition ;
* conserve une copie de la table au début et une autre à la fin du disque ;
* utilise des sommes de contrôle pour détecter certaines corruptions ;
* contient un MBR protecteur pour éviter qu'un ancien outil ne considère le disque comme vide.

Analogie : GPT est un plan moderne dupliqué dans deux coffres, avec un contrôle permettant de détecter une modification accidentelle.

### 5.3 GPT ou MBR ?

Pour une nouvelle installation, **GPT est généralement le meilleur choix**, même pour un disque inférieur à 2 TiB.

MBR reste utile surtout pour :

* certains très anciens ordinateurs ;
* certains appareils embarqués exigeant ce format ;
* des besoins précis de compatibilité.

### 5.4 BIOS, UEFI et partitions de démarrage

Le BIOS traditionnel charge du code placé dans le MBR. L'UEFI cherche plutôt des fichiers de démarrage dans une **partition système EFI**, ou ESP.

Une ESP est généralement :

* formatée en FAT32 ;
* marquée comme partition EFI ;
* d'une taille de quelques centaines de MiB ;
* montée sous Linux sur `/boot/efi`.

Avec GPT et un démarrage BIOS, GRUB peut nécessiter une minuscule partition spéciale `bios_grub` non formatée.

### Commandes utiles

Afficher la table de partitions :

```bash
sudo fdisk -l
```

Afficher celle d'un disque précis :

```bash
sudo fdisk -l /dev/sdX
```

Vue synthétique avec `parted` :

```bash
sudo parted /dev/sdX print
```

Afficher les informations GPT avec `gdisk` :

```bash
sudo gdisk -l /dev/sdX
```

> Lire une table avec `fdisk -l` ou `parted ... print` est sans danger. En revanche, enregistrer des modifications de partitionnement peut rendre les données inaccessibles.

---

## 6. Les partitions

Une partition est une plage de secteurs contigus définie dans la table de partitions. Elle donne l'impression que chaque zone du disque est un support indépendant.

On peut, par exemple, organiser un disque ainsi :

```text
Disque GPT de 1 TiB
├── partition 1 : 512 MiB, système EFI, FAT32
├── partition 2 : 100 GiB, système Linux, ext4
├── partition 3 : 16 GiB, swap
└── partition 4 : espace restant, données, ext4
```

### Pourquoi créer plusieurs partitions ?

* séparer le système des données personnelles ;
* installer plusieurs systèmes d'exploitation ;
* utiliser des systèmes de fichiers différents ;
* isoler certaines données ou certains usages ;
* réserver un espace de récupération ou de démarrage.

Mais un trop grand nombre de partitions rigides peut gaspiller de l'espace. LVM apporte davantage de souplesse.

### Créer une table GPT et une partition avec `parted`

> **DANGER : les commandes suivantes détruisent le partitionnement existant de `/dev/sdX`.**

```bash
sudo parted /dev/sdX --script mklabel gpt
sudo parted /dev/sdX --script mkpart primary ext4 1MiB 100%
```

Demander au noyau de relire la table :

```bash
sudo partprobe /dev/sdX
```

Contrôler le résultat :

```bash
lsblk /dev/sdX
sudo parted /dev/sdX print
```

### Utiliser `fdisk` en mode interactif

```bash
sudo fdisk /dev/sdX
```

Commandes internes courantes de `fdisk` :

```text
p  afficher la table
g  créer une table GPT
o  créer une table MBR
n  créer une partition
d  supprimer une partition
t  changer le type d'une partition
v  vérifier la table
w  écrire les changements et quitter
q  quitter sans enregistrer
```

Rien n'est écrit tant que l'on n'utilise pas `w`, mais il faut tout de même rester prudent.

### Sauvegarder la structure des partitions

Pour une table compatible avec `sfdisk` :

```bash
sudo sfdisk --dump /dev/sdX > partitions-sdX.txt
```

Restaurer cette structure est une opération destructive et ne restaure pas le contenu des fichiers :

```bash
sudo sfdisk /dev/sdX < partitions-sdX.txt
```

Pour GPT, `sgdisk` peut sauvegarder les données de partitionnement :

```bash
sudo sgdisk --backup=table-gpt.bin /dev/sdX
```

---

## 7. Le système de fichiers

Une partition brute ressemble à un entrepôt vide sans rayonnages ni inventaire. Le **formatage** y crée une méthode de classement : le système de fichiers.

Un système de fichiers gère notamment :

* les noms de fichiers et de répertoires ;
* l'emplacement des données ;
* l'espace libre ;
* les dates ;
* les permissions et propriétaires ;
* parfois la journalisation, les instantanés, la compression et les sommes de contrôle.

### 7.1 ext4

`ext4` est un choix courant et polyvalent sous Linux.

* stable et largement pris en charge ;
* journalisé ;
* compatible avec les permissions Linux ;
* outils de réparation éprouvés.

Il constitue souvent le choix par défaut pour un poste ou un serveur Linux classique.

### 7.2 XFS

`XFS` est très performant pour les gros volumes et fichiers, et fréquent sur les serveurs.

* excellente montée en charge ;
* agrandissement à chaud ;
* journalisation robuste ;
* ne se réduit pas simplement.

### 7.3 Btrfs

`Btrfs` propose des fonctions avancées :

* instantanés ;
* sous-volumes ;
* sommes de contrôle des données et métadonnées ;
* compression transparente ;
* envoi et réception d'instantanés.

Il est puissant, mais demande de comprendre son fonctionnement et ses recommandations d'administration.

### 7.4 ZFS

ZFS combine gestion de volumes et système de fichiers.

* intégrité de bout en bout ;
* pools de stockage ;
* instantanés, compression, réplication ;
* réparation automatique possible avec de la redondance.

Il consomme davantage de ressources et n'est pas intégré de la même manière à toutes les distributions Linux.

### 7.5 FAT32

`FAT32` est extrêmement compatible : Windows, macOS, Linux, téléviseurs, appareils photo et consoles.

Limites importantes :

* un fichier ne peut pas dépasser 4 GiB ;
* pas de permissions Unix natives ;
* pas de journalisation ;
* moins robuste en cas de débranchement brutal.

Il reste le format classique des partitions EFI.

### 7.6 exFAT

`exFAT` est conçu pour les supports flash et les échanges entre systèmes.

* fichiers supérieurs à 4 GiB ;
* bonne compatibilité avec les systèmes récents ;
* pas de permissions Unix natives ;
* pas de journalisation classique.

C'est souvent un bon choix pour un disque externe partagé entre Linux, Windows et macOS.

### 7.7 NTFS

`NTFS` est le système de fichiers principal de Windows.

* journalisé ;
* gère permissions, compression et grands fichiers ;
* pris en charge sous Linux, notamment grâce au pilote `ntfs3` sur les noyaux récents.

Il convient aux disques principalement utilisés sous Windows. Pour un disque d'échange simple, exFAT peut être plus universel.

### 7.8 Swap

Le swap n'est pas un système de fichiers ordinaire. Il sert d'extension à la mémoire vive et peut être utilisé pour l'hibernation.

Le swap peut être :

* une partition dédiée ;
* un fichier ;
* un volume logique.

Voir le swap actif :

```bash
swapon --show
free -h
```

### 7.9 Tableau de choix rapide

| Besoin | Choix fréquent | Remarque |
|---|---|---|
| Système Linux généraliste | ext4 | Simple, robuste et très répandu |
| Gros serveur de fichiers | XFS | Très bon pour les volumes importants |
| Instantanés et compression sous Linux | Btrfs | Fonctions avancées intégrées |
| Pool avancé avec forte intégrité | ZFS | Administration et mémoire à prévoir |
| Échange entre systèmes récents | exFAT | Grands fichiers, bonne compatibilité |
| Compatibilité avec appareils anciens | FAT32 | Limite de 4 GiB par fichier |
| Disque principalement Windows | NTFS | Natif sous Windows |
| Partition système EFI | FAT32 | Standard attendu par l'UEFI |

---

## 8. Formater une partition

Formater signifie créer un système de fichiers. Cela efface les structures précédentes de la partition et rend généralement les anciennes données inaccessibles.

> **DANGER : vérifiez trois fois le nom de la partition. `mkfs` ne demande pas toujours confirmation. On formate normalement `/dev/sdX1`, et non le disque entier `/dev/sdX`.**

Créer un système ext4 avec un label :

```bash
sudo mkfs.ext4 -L DONNEES /dev/sdX1
```

Créer un système XFS :

```bash
sudo mkfs.xfs -L DONNEES /dev/sdX1
```

Créer un système FAT32 :

```bash
sudo mkfs.vfat -F 32 -n PARTAGE /dev/sdX1
```

Créer un système exFAT :

```bash
sudo mkfs.exfat -n PARTAGE /dev/sdX1
```

Créer un système NTFS :

```bash
sudo mkfs.ntfs -f -L DONNEES /dev/sdX1
```

Créer et activer un swap :

```bash
sudo mkswap -L SWAP /dev/sdX1
sudo swapon /dev/sdX1
```

Afficher le résultat :

```bash
lsblk -f /dev/sdX
sudo blkid /dev/sdX1
```

### Labels et UUID

Le **label** est un nom lisible choisi par l'administrateur, par exemple `PHOTOS`. Il n'est pas nécessairement unique.

L'**UUID** est un identifiant généré lors du formatage. Il est conçu pour identifier le système de fichiers de manière stable.

```bash
sudo blkid /dev/sdX1
```

Exemple de résultat :

```text
/dev/sdX1: LABEL="DONNEES" UUID="1234-abcd-..." TYPE="ext4"
```

---

## 9. Monter et démonter un système de fichiers

Sous Windows, une partition reçoit souvent une lettre telle que `D:`. Sous Linux, tous les fichiers appartiennent à une seule arborescence commençant par `/`.

Le **montage** attache un système de fichiers à un répertoire appelé **point de montage**.

Analogie : le système de fichiers est une pièce préfabriquée et le point de montage est la porte que l'on installe dans la maison Linux pour y accéder.

### Montage manuel

Créer un point de montage :

```bash
sudo mkdir -p /mnt/donnees
```

Monter la partition :

```bash
sudo mount /dev/sdX1 /mnt/donnees
```

Vérifier :

```bash
findmnt /mnt/donnees
df -hT /mnt/donnees
```

Démonter avant de débrancher :

```bash
sudo umount /mnt/donnees
```

La commande s'écrit bien `umount`, sans `n` après le `u`.

Si le système répond « target is busy », rechercher les processus qui l'utilisent :

```bash
sudo fuser -vm /mnt/donnees
```

ou :

```bash
sudo lsof +D /mnt/donnees
```

Il vaut mieux fermer proprement ces processus plutôt que forcer le démontage.

### Montage automatique avec `/etc/fstab`

Le fichier `/etc/fstab` décrit les montages permanents.

Obtenir l'UUID :

```bash
sudo blkid /dev/sdX1
```

Exemple de ligne pour ext4 :

```fstab
UUID=12345678-1234-1234-1234-123456789abc /mnt/donnees ext4 defaults,nofail 0 2
```

Signification des champs :

```text
UUID=...       système de fichiers à monter
/mnt/donnees   point de montage
ext4           type de système de fichiers
defaults       options ordinaires
nofail         ne bloque pas le démarrage si le disque est absent
0              ancien indicateur de sauvegarde dump
2              ordre de vérification par fsck
```

Après avoir modifié `/etc/fstab`, tester **avant de redémarrer** :

```bash
sudo mount -a
findmnt --verify
```

Afficher tous les montages :

```bash
findmnt
```

### Propriétaires et permissions

Le montage et les permissions sont deux questions différentes. Avec ext4, XFS ou Btrfs, les propriétaires et permissions sont enregistrés dans le système de fichiers.

Exemple :

```bash
sudo chown -R alice:alice /mnt/donnees
chmod 750 /mnt/donnees
```

> Remplacez `alice` par l'utilisateur réel. Évitez `chmod -R 777`, qui donne à tout le monde tous les droits et masque souvent le vrai problème.

FAT32, exFAT et NTFS ne représentent pas les permissions Unix de la même façon. On définit souvent le propriétaire et les masques au montage :

```fstab
UUID=ABCD-1234 /mnt/partage exfat defaults,nofail,uid=1000,gid=1000,umask=022 0 0
```

---

## 10. Mesurer l'espace utilisé

### `df` : vue du système de fichiers

`df` répond à la question : « combien de place reste-t-il dans chaque système de fichiers monté ? »

```bash
df -h
df -hT
```

### `du` : vue des fichiers

`du` répond à la question : « quels fichiers et répertoires occupent cette place ? »

```bash
du -sh /var/log
du -h --max-depth=1 /var | sort -h
```

Chercher les gros fichiers sur un même système de fichiers :

```bash
sudo find /var -xdev -type f -size +500M -printf '%s %p\n' | sort -n
```

### Pourquoi `df` et `du` peuvent différer

Causes fréquentes :

* un processus conserve ouvert un fichier qui a été supprimé ;
* blocs réservés au superutilisateur sur ext4 ;
* instantanés ;
* fichiers creux ;
* répertoires masqués par un montage ;
* métadonnées du système de fichiers.

Voir les fichiers supprimés mais encore ouverts :

```bash
sudo lsof +L1
```

### Les inodes

Sur certains systèmes de fichiers, chaque fichier consomme une structure appelée **inode**. Il est possible d'avoir encore des gigaoctets libres mais de ne plus pouvoir créer de fichier si tous les inodes sont utilisés.

```bash
df -ih
```

---

## 11. Vérifier et réparer un système de fichiers

Une coupure de courant, un câble défectueux ou un support vieillissant peut endommager les métadonnées.

La journalisation aide à rétablir un état cohérent, mais elle ne remplace ni la vérification ni la sauvegarde.

### ext4

> Un système de fichiers doit généralement être démonté avant une vérification ou une réparation.

Vérification sans modification :

```bash
sudo e2fsck -fn /dev/sdX1
```

Vérification et réparation interactive :

```bash
sudo e2fsck -f /dev/sdX1
```

### XFS

Vérification sans modification :

```bash
sudo xfs_repair -n /dev/sdX1
```

Réparation :

```bash
sudo xfs_repair /dev/sdX1
```

### FAT

```bash
sudo fsck.vfat -n /dev/sdX1
```

### Commande générique

```bash
sudo fsck -N /dev/sdX1
```

Avec `-N`, `fsck` indique ce qu'il ferait sans exécuter la vérification.

> Une réparation peut supprimer ou déplacer des éléments irrécupérables pour retrouver une structure cohérente. Si les données sont importantes, réaliser d'abord une image du support défaillant.

---

## 12. LVM : des volumes plus souples

**LVM**, *Logical Volume Manager*, ajoute une couche entre les partitions et les systèmes de fichiers.

Analogie : les partitions classiques sont des murs en béton. LVM remplace ces murs par des cloisons modulaires plus faciles à déplacer ou agrandir.

Les trois niveaux principaux sont :

```text
PV — Physical Volume : disque ou partition confié à LVM
VG — Volume Group    : réserve commune constituée d'un ou plusieurs PV
LV — Logical Volume  : volume découpé dans cette réserve
```

Schéma :

```text
/dev/sdb1 ─┐
           ├─ VG "stockage" ─┬─ LV "documents" → ext4
/dev/sdc1 ─┘                  └─ LV "sauvegardes" → XFS
```

Commandes de consultation :

```bash
sudo pvs
sudo vgs
sudo lvs
sudo lvdisplay
```

Exemple de création :

> **DANGER : ces commandes réaffectent entièrement `/dev/sdX1` à LVM.**

```bash
sudo pvcreate /dev/sdX1
sudo vgcreate stockage /dev/sdX1
sudo lvcreate -L 100G -n documents stockage
sudo mkfs.ext4 /dev/stockage/documents
```

Agrandir un volume logique et son système de fichiers ext4 :

```bash
sudo lvextend -L +20G /dev/stockage/documents
sudo resize2fs /dev/stockage/documents
```

Sur de nombreux systèmes, `-r` permet de redimensionner aussi le système de fichiers :

```bash
sudo lvextend -r -L +20G /dev/stockage/documents
```

Réduire un volume est beaucoup plus risqué : tous les systèmes de fichiers ne le permettent pas, et le système de fichiers doit être réduit **avant** son conteneur. Une sauvegarde est indispensable.

Les instantanés LVM sont utiles pour obtenir une vue cohérente à un instant donné, mais ne constituent pas à eux seuls une sauvegarde indépendante.

---

## 13. RAID : performance et tolérance aux pannes

Le **RAID** combine plusieurs disques.

Analogie : plusieurs personnes recopient ou se partagent un registre.

### RAID 0 — répartition sans sécurité

Les données sont réparties sur plusieurs disques.

* capacité additionnée ;
* bonnes performances ;
* aucune redondance ;
* la panne d'un seul disque détruit l'ensemble.

### RAID 1 — miroir

Chaque donnée est copiée sur deux disques.

* tolère généralement la panne d'un disque ;
* capacité utile proche de celle d'un seul disque ;
* lecture potentiellement améliorée.

### RAID 5 — parité simple

Nécessite au moins trois disques et répartit données et parité.

* tolère la panne d'un disque ;
* capacité utile équivalente à `N - 1` disques ;
* reconstruction longue et exigeante sur de gros disques.

### RAID 6 — double parité

* nécessite au moins quatre disques ;
* tolère la panne de deux disques ;
* capacité utile équivalente à `N - 2` disques.

### RAID 10 — miroirs répartis

* nécessite généralement au moins quatre disques ;
* bonnes performances et redondance ;
* environ 50 % de la capacité brute est utilisable.

Sous Linux, le RAID logiciel est souvent géré avec `mdadm`.

Afficher l'état des ensembles :

```bash
cat /proc/mdstat
sudo mdadm --detail /dev/md0
```

> **RAID n'est pas une sauvegarde.** Il protège surtout contre la panne d'un disque. Il ne protège pas contre l'effacement accidentel, le rançongiciel, le vol, l'incendie, une corruption propagée ou une mauvaise commande.

---

## 14. Chiffrement avec LUKS

Le chiffrement protège les données lorsque le disque est éteint ou volé. Sous Linux, on utilise couramment **LUKS** avec `cryptsetup`.

Organisation fréquente :

```text
partition → conteneur LUKS → volume déchiffré → système de fichiers
```

Créer un conteneur :

> **DANGER : cette opération écrase la signature précédente de `/dev/sdX1`. Une phrase secrète perdue peut rendre les données définitivement inaccessibles.**

```bash
sudo cryptsetup luksFormat /dev/sdX1
```

Ouvrir le conteneur :

```bash
sudo cryptsetup open /dev/sdX1 donnees_chiffrees
```

Créer un système de fichiers dans le volume ouvert :

```bash
sudo mkfs.ext4 /dev/mapper/donnees_chiffrees
```

Fermer proprement :

```bash
sudo umount /mnt/donnees
sudo cryptsetup close donnees_chiffrees
```

Afficher les informations LUKS :

```bash
sudo cryptsetup luksDump /dev/sdX1
```

Sauvegarder l'en-tête LUKS sur un autre support sécurisé est prudent :

```bash
sudo cryptsetup luksHeaderBackup /dev/sdX1 --header-backup-file luks-header.img
```

Cette sauvegarde d'en-tête est sensible et doit être protégée.

---

## 15. Surveiller la santé du matériel

### SMART

La plupart des HDD et SSD exposent des indicateurs **SMART**. Ils donnent des indices, mais ne prédisent pas toutes les pannes.

Afficher le rapport complet :

```bash
sudo smartctl -a /dev/sdX
```

Afficher l'état synthétique :

```bash
sudo smartctl -H /dev/sdX
```

Lancer un test court :

```bash
sudo smartctl -t short /dev/sdX
```

Lancer un test long :

```bash
sudo smartctl -t long /dev/sdX
```

Lire ensuite les résultats :

```bash
sudo smartctl -l selftest /dev/sdX
```

Pour un disque NVMe :

```bash
sudo nvme smart-log /dev/nvme0
```

Indicateurs HDD à surveiller :

* secteurs réalloués ;
* secteurs en attente ;
* secteurs incorrigibles ;
* erreurs de lecture ;
* température ;
* erreurs de liaison, parfois dues au câble.

Indicateurs SSD/NVMe utiles :

* pourcentage d'usure ;
* quantité totale écrite ;
* erreurs de média ;
* température ;
* réserve disponible.

> Une valeur SMART inquiétante impose d'abord une sauvegarde. Tester intensivement un disque mourant avant de copier les données peut accélérer sa panne.

### Observer les erreurs du noyau

```bash
sudo journalctl -k -p warning
```

Suivre les nouveaux messages :

```bash
sudo journalctl -kf
```

Rechercher des erreurs d'entrée-sortie :

```bash
sudo journalctl -k | grep -Ei 'I/O error|ata|nvme|reset|sector'
```

---

## 16. SSD, TRIM et entretien

Lorsqu'un fichier est supprimé, le système de fichiers sait que ses blocs sont libres, mais le SSD doit aussi en être informé. La commande **TRIM** transmet cette information au contrôleur.

Vérifier le planificateur périodique sur les distributions utilisant systemd :

```bash
systemctl status fstrim.timer
```

Lancer TRIM sur les systèmes compatibles montés :

```bash
sudo fstrim -av
```

Un TRIM périodique hebdomadaire est généralement préférable à l'option de montage `discard` en continu, sauf besoin spécifique.

La défragmentation classique est rarement utile sur un SSD et génère des écritures supplémentaires. Certains systèmes de fichiers disposent néanmoins d'outils ciblés pour des cas particuliers.

---

## 17. Performances et diagnostic

### Observer les entrées-sorties

Si le paquet `sysstat` est installé :

```bash
iostat -xz 1
```

Afficher les processus qui effectuent des entrées-sorties :

```bash
sudo iotop
```

### Mesurer avec prudence

Test simple de lecture en cache direct avec `hdparm` :

```bash
sudo hdparm -Tt /dev/sdX
```

Tester une écriture dans un **fichier temporaire** sur le système monté :

```bash
dd if=/dev/zero of=/mnt/donnees/test.bin bs=1M count=1024 conv=fdatasync status=progress
```

Puis supprimer le fichier de test :

```bash
rm /mnt/donnees/test.bin
```

Ce test est rudimentaire et peut être influencé par les caches. `fio` permet des mesures plus sérieuses, mais une mauvaise configuration peut écraser un périphérique. Utilisez uniquement un fichier de test clairement identifié.

> Ne lancez jamais un test d'écriture directement sur `/dev/sdX` ou `/dev/sdX1` contenant des données.

---

## 18. Sauvegarder, cloner et restaurer

### Une copie n'est pas toujours une sauvegarde

Une bonne sauvegarde est :

* distincte de l'original ;
* vérifiée ;
* historisée lorsque c'est utile ;
* restaurable ;
* protégée contre l'effacement simultané.

La règle **3-2-1** recommande :

* 3 copies des données ;
* sur 2 types de supports ;
* dont 1 copie hors site.

### Copier des fichiers avec `rsync`

```bash
rsync -aHAX --info=progress2 /source/ /sauvegarde/
```

Le slash final de `/source/` signifie « copier le contenu du répertoire ».

Faire d'abord une simulation :

```bash
rsync -aHAXn --delete /source/ /sauvegarde/
```

> L'option `--delete` supprime dans la destination ce qui n'existe plus dans la source. Elle est utile pour un miroir, mais dangereuse si les chemins sont inversés. Le mode simulation `-n` est fortement recommandé.

### Copier un disque sain avec `dd`

`dd` copie des blocs sans comprendre les fichiers.

```bash
sudo dd if=/dev/sdX of=/chemin/image-disque.img bs=64K status=progress conv=fsync
```

* `if` signifie *input file*, la source ;
* `of` signifie *output file*, la destination.

> **DANGER : inverser `if` et `of` peut détruire instantanément le mauvais disque.**

Une image brute occupe normalement la taille totale du disque, même si celui-ci est presque vide.

### Copier un disque défaillant avec GNU ddrescue

Pour un support qui produit des erreurs, `ddrescue` est préférable à `dd`. Il copie d'abord les zones faciles et conserve un journal permettant de reprendre.

Première passe :

```bash
sudo ddrescue -f -n /dev/sdX image.img sauvetage.map
```

Nouvelle tentative sur les zones difficiles :

```bash
sudo ddrescue -d -f -r3 /dev/sdX image.img sauvetage.map
```

Le fichier `sauvetage.map` est essentiel pour reprendre l'opération.

Avec des données irremplaçables, un disque qui clique, disparaît ou ne tourne plus doit être confié à un laboratoire spécialisé. Le rallumer à répétition peut aggraver les dommages.

### Monter une image en lecture seule

Associer l'image à un périphérique boucle et détecter ses partitions :

```bash
sudo losetup --find --show --partscan image-disque.img
```

La commande renvoie par exemple `/dev/loop0`. Monter une partition en lecture seule :

```bash
sudo mkdir -p /mnt/image
sudo mount -o ro /dev/loop0p1 /mnt/image
```

Après utilisation :

```bash
sudo umount /mnt/image
sudo losetup -d /dev/loop0
```

---

## 19. Effacement et réutilisation d'un disque

### Supprimer des fichiers n'efface pas immédiatement leur contenu

Une suppression ordinaire retire surtout la référence au fichier. Les blocs peuvent rester lisibles jusqu'à leur réutilisation.

### Voir les signatures présentes

Lecture seule :

```bash
sudo wipefs /dev/sdX
```

Effacer les signatures connues :

> **DANGER : la commande suivante rend les systèmes de fichiers et tables de partitions difficiles ou impossibles à retrouver normalement.**

```bash
sudo wipefs --all /dev/sdX
```

### HDD contre SSD

Sur un HDD, un écrasement complet peut être utilisé dans certains contextes. Sur un SSD, le wear leveling signifie que le système ne contrôle pas directement l'emplacement physique de chaque écriture : `shred` n'y garantit donc pas l'effacement de toutes les anciennes cellules.

Pour un SSD, privilégier lorsque nécessaire :

* les fonctions *secure erase* ou *sanitize* du constructeur et du protocole ;
* le chiffrement intégral activé dès le départ, puis la destruction des clés ;
* la destruction physique par un prestataire adapté pour les données très sensibles.

Avant toute procédure d'effacement sécurisé, consulter la documentation exacte du matériel. Une erreur peut cibler le mauvais disque ou rendre le support inutilisable.

---

## 20. Scénario complet : préparer un nouveau disque de données

Supposons qu'un nouveau disque vide soit détecté comme `/dev/sdb`. L'objectif est de créer une seule partition GPT en ext4 montée sur `/srv/donnees`.

### Étape 1 — identifier sans ambiguïté le disque

```bash
lsblk -o NAME,MODEL,SERIAL,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

Vérifier qu'il n'est pas monté et qu'il s'agit bien du nouveau disque.

### Étape 2 — examiner l'existant

```bash
sudo fdisk -l /dev/sdb
sudo wipefs /dev/sdb
```

La deuxième commande, sans `--all`, ne fait qu'afficher les signatures.

### Étape 3 — créer la table et la partition

> À partir d'ici, le contenu antérieur de `/dev/sdb` est sacrifié.

```bash
sudo parted /dev/sdb --script mklabel gpt
sudo parted /dev/sdb --script mkpart primary ext4 1MiB 100%
sudo partprobe /dev/sdb
```

### Étape 4 — formater

```bash
sudo mkfs.ext4 -L DONNEES /dev/sdb1
```

### Étape 5 — monter et tester

```bash
sudo mkdir -p /srv/donnees
sudo mount /dev/sdb1 /srv/donnees
findmnt /srv/donnees
df -hT /srv/donnees
```

### Étape 6 — attribuer les droits

Pour donner le répertoire à l'utilisateur courant :

```bash
sudo chown "$USER":"$(id -gn)" /srv/donnees
```

### Étape 7 — rendre le montage permanent

Récupérer l'UUID :

```bash
sudo blkid /dev/sdb1
```

Ajouter dans `/etc/fstab`, en remplaçant l'UUID :

```fstab
UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx /srv/donnees ext4 defaults,nofail 0 2
```

Tester la configuration :

```bash
sudo umount /srv/donnees
sudo mount -a
findmnt --verify
findmnt /srv/donnees
```

---

## 21. Erreurs fréquentes à éviter

### Confondre disque et partition

```text
/dev/sdb   = disque entier
/dev/sdb1  = première partition
```

Un `mkfs` sur `/dev/sdb` au lieu de `/dev/sdb1` peut écraser la table de partitions.

### Se fier uniquement au nom `/dev/sdX`

L'ordre peut changer. Vérifiez modèle, numéro de série et taille. Utilisez les UUID dans `/etc/fstab`.

### Débrancher sans démonter

Des écritures peuvent encore être en cache. Toujours démonter proprement :

```bash
sync
sudo umount /point/de/montage
```

`umount` attend normalement la fin des écritures ; `sync` apporte une précaution visible supplémentaire.

### Croire que formater répare une panne physique

Le formatage reconstruit des structures logiques. Il ne répare ni une tête de lecture, ni de la mémoire flash usée, ni un câble défectueux.

### Croire que RAID remplace une sauvegarde

Le RAID améliore la disponibilité. La sauvegarde permet de revenir à une copie indépendante ou antérieure.

### Réparer avant de sauvegarder

Sur un support instable, commencez par copier ou imager les données. Une réparation modifie le support et peut rendre certaines récupérations ultérieures plus difficiles.

### Remplir un système de fichiers à 100 %

Un système totalement plein peut ralentir, empêcher les journaux de s'écrire et perturber les services. Gardez une marge libre, en particulier sur les SSD et les systèmes utilisant des instantanés.

---

## 22. Aide-mémoire des commandes

### Identifier

```bash
lsblk -f
lsblk -o NAME,MODEL,SERIAL,SIZE,TYPE,FSTYPE,MOUNTPOINTS,ROTA
sudo blkid
sudo fdisk -l
sudo parted /dev/sdX print
```

### Monter et examiner

```bash
sudo mount /dev/sdX1 /mnt/donnees
sudo umount /mnt/donnees
findmnt
df -hT
du -sh /chemin
```

### Créer

```bash
sudo parted /dev/sdX --script mklabel gpt
sudo parted /dev/sdX --script mkpart primary ext4 1MiB 100%
sudo mkfs.ext4 -L DONNEES /dev/sdX1
```

### Vérifier

```bash
sudo e2fsck -fn /dev/sdX1
sudo smartctl -a /dev/sdX
sudo journalctl -kf
```

### Espace et activité

```bash
df -hT
df -ih
du -h --max-depth=1 /chemin | sort -h
iostat -xz 1
sudo iotop
```

### Sauvegarder

```bash
rsync -aHAX --info=progress2 /source/ /sauvegarde/
sudo ddrescue -f -n /dev/sdX image.img sauvetage.map
```

---

## 23. Questions de révision

1. Quelle différence y a-t-il entre un disque, une partition et un système de fichiers ?
2. Pourquoi GPT est-il généralement préféré à MBR ?
3. Quelle différence existe entre `/dev/sda` et `/dev/sda1` ?
4. Pourquoi utilise-t-on un UUID dans `/etc/fstab` ?
5. Quelle commande affiche les systèmes de fichiers et leurs points de montage ?
6. Quelle différence y a-t-il entre `df` et `du` ?
7. Pourquoi RAID 1 ne constitue-t-il pas une sauvegarde ?
8. Pourquoi faut-il démonter un disque avant de le débrancher ?
9. À quoi sert TRIM sur un SSD ?
10. Pourquoi `ddrescue` est-il préférable à `dd` pour un disque endommagé ?

### Réponses courtes

1. Le disque est le support, la partition une zone délimitée et le système de fichiers la méthode d'organisation des fichiers.
2. GPT accepte de plus grands disques, davantage de partitions et possède des mécanismes de redondance et de contrôle.
3. `/dev/sda` représente le disque entier ; `/dev/sda1`, sa première partition.
4. L'UUID reste stable même si le nom `/dev/sdX` change.
5. `lsblk -f` et `findmnt` donnent des vues complémentaires.
6. `df` mesure l'occupation du système de fichiers ; `du` additionne l'espace utilisé par des fichiers visibles.
7. Un effacement ou une corruption est reproduit sur le miroir.
8. Pour terminer les écritures en attente et conserver un système de fichiers cohérent.
9. À signaler au SSD quels blocs ne contiennent plus de données utiles.
10. `ddrescue` traite mieux les erreurs, privilégie les zones lisibles et peut reprendre grâce à son fichier journal.

---

## Conclusion

Retenez la chaîne suivante :

```text
matériel → périphérique bloc → table de partitions → partition
         → éventuel RAID/LVM/chiffrement → système de fichiers
         → point de montage → fichiers
```

Avant toute opération, la meilleure habitude est toujours la même :

1. identifier précisément le matériel avec `lsblk` ;
2. comprendre quelle couche on s'apprête à modifier ;
3. sauvegarder ce qui compte ;
4. relire la commande, surtout sa cible ;
5. vérifier le résultat à chaque étape.

Un disque peut être remplacé. Les données uniques, elles, ne le peuvent pas.
