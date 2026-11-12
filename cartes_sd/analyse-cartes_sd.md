# Analyse des cartes SD

**Relecture de cohérence : 12 novembre 2026.** Harmonisation avec le [rapport final réorganisé](../RAPPORT-FINAL-SADEDINE-2026.md), sans nouvelle acquisition ni nouvelle analyse des supports. Les campagnes et décomptes techniques conservent leurs dates et leurs périmètres. Le détail de cette révision et les empreintes actuelles figurent dans le [dossier de relecture](../investigations/20261112-coherence-rapports/compte-rendu.md).

## Actualisation du 10 novembre 2026 — lecture courante

Le PV est disponible et a été consulté. Les repères à retenir sont la mise sous scellés après 14 h 19 le 15 octobre, l’ouverture du PC à 10 h 41 et celle des téléphones à 11 h 30 le 28 ; 10 h 22 est l’arrivée de la cliente et 19 h 20 la clôture, sans heure individuelle de restitution. Les mentions d’indisponibilité et bornes déclaratives des sections datées ci-dessous décrivent leurs campagnes historiques. Les caméras et cartes n’étaient pas sous scellés. Les nouvelles traces système TP-03 ne prouvent ni un accès aux caméras ni une modification des vidéos. Cette relecture ne réexécute pas les scans/récupérations SD ; elle maintient les anomalies, lacunes et limites déjà établies. Voir la [relecture transversale](../investigations/20261110-telephones/compte-rendu.md), qui distingue les nouveaux contrôles des reprises documentaires. Les empreintes historiques des rapports restent attachées à leurs versions datées.


## Actualisation documentaire du 19 octobre 2026

Ce document conserve le compte rendu d’acquisition. Les nouvelles analyses du retour de la cliente figurent dans le [complément du 19 octobre](../investigations/20261019-retour-cliente/compte-rendu.md) et les rapports SD-01/02/03 et transversal. La cliente précise **février 2024, caméra de la chambre**, une installation après mars 2023 et un fonctionnement continu de la terrasse. Ces déclarations ne changent ni les empreintes ni les dates d’acquisition. Le PV n’était pas disponible lors de cette campagne d’octobre ; il a depuis été consulté le 8 novembre ; aucune réinitialisation ou suppression intentionnelle nouvelle n’est démontrée.


- **Auteur** : Christophe Donnat - DonnatDev - christophe@donnat.dev
- **Client** : Mme Sadedine Malika - DMM Conseils - dmmconseils@hotmail.com
- **Matériels examinés** : cartes SD-01, SD-02 et SD-03 (chambre, terrasse, salon)
- **Début de l'analyse** : 12 octobre 2026 à 10:06:00
- **Remarques** : RAS

### Carte SD-01

- **Référence forensic :** SD-01
- **Marque :** SanDisk 
- **Capacité commerciale :** 32 Go
- **Capacité détectée par Linux :** 29,7 Gio
- **Système de fichiers:** FAT32
- **Numéro de série USB déclaré	par le lecteur :** 121220160204

### Carte SD-02

- **Référence forensic :** SD-02
- **Marque :** SanDisk 
- **Capacité commerciale :** 32 Go
- **Capacité détectée par Linux :** 29,7 Gio
- **Système de fichiers:** FAT32
- **Numéro de série USB déclaré	par le lecteur :** 121220160204

### Carte SD-03

- **Référence forensic :** SD-03
- **Capacité commerciale :** 32 Go
- **Système de fichiers :** FAT32
- **Identification :** référence et description « salon » dans `SD03.info` ; aucun numéro de série matériel propre à la carte n’est établi.

La marque est transcrite **« ScanDisk » dans l’attestation**, **« SanDisk » dans les notes d’acquisition** ; cette divergence est conservée sans prétendre à une nouvelle vérification physique. Le numéro USB `121220160204` est celui du **lecteur**, pas un identifiant individuel des cartes.

### État antérieur

Les notes indiquent une remise le **07/10/2026 à 16h15**, avec adaptateur USB ; l’[attestation](../remise-documents/attestation-de-remise.md) est datée du **06/10/2026**. Cette divergence documentaire reste non résolue.

Le prestataire a inscrit les numéros 1, 2 et 3 dessus, correspondant aux identifiants attribués lors de la remise du matériel:

- **1** : Carte SD-01
- **2** : Carte SD-02
- **3** : Carte SD-03

---

## Acquisition des images des cartes SD

### Carte SD-01

#### Branchement sur le PC Linux du prestataire

Le 12/10/2026 à 10h00 environ, la carte SD-01 a été branchée sur le PC Linux du prestataire via l'adaptateur USB fourni par la cliente.

#### Acquisition de l'image disque avec Guymager

Le 12/10/2026 à 10h17 environ, le prestataire a lancé l'acquisition de l'image disque de la carte SD-01 avec le logiciel Guymager.

L'acquisition a été réalisée en mode "read-only" pour éviter toute modification des données présentes sur la carte SD.

#### Résultat de l'acquisition

SHA-256 du flux source SD-01 calculé pendant l’acquisition :
`42fa8f6d3351a4ba2446b267637f51a0c1e44df4abd31b002a1ac2212c023c09`

SHA-256 du flux relu dans l’image SD-01 :
`42fa8f6d3351a4ba2446b267637f51a0c1e44df4abd31b002a1ac2212c023c09`

> Le SHA-256 du flux acquis et celui du flux relu dans l’image SD-01 concordent ; Guymager indique une vérification de l’image réussie. `Source verification: off` : il ne s’agit pas d’une seconde lecture indépendante de contrôle de la carte après acquisition. Ces valeurs portent sur les données décompressées, pas sur les fichiers segments EWF.

Contenu du fichier `SD01.info`

```bash
GUYMAGER ACQUISITION INFO FILE
==============================

Guymager
========

Version            : 0.8.13-2build3                                                                                         
Version timestamp  : 2025-12-08-22.09.03 UTC                                                                                
Compiled with      : gcc 15.2.0                                                                                             
libewf version     : 20140816 (not used as Guymager is configured to use its own EWF module)                                
libguytools version: 2.1.0                                                                                                  
Host name          : chris-MS-7B48                                                                                          
Domain name        : (none)                                                                                                 
System             : Linux chris-MS-7B48 7.0.0-38-generic #38-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep  4 09:10:14 UTC 2026 x86_64


Device information
==================
Command executed: bash -c "search="`basename /dev/sdc`: H..t P.......d A..a de.....d" && dmesg | grep -A3 "$search" || echo "No kernel HPA messages for /dev/sdc""
Information returned:
----------------------------------------------------------------------------------------------------
   No kernel HPA messages for /dev/sdc

Command executed: bash -c "smartctl -s on /dev/sdc ; smartctl -a /dev/sdc"
Information returned:
----------------------------------------------------------------------------------------------------
   smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.0.0-38-generic] (local build)
   Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org
   
   /dev/sdc: Unknown USB bridge [0x14cd:0x1212 (0x100)]
   Please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary
   
   smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.0.0-38-generic] (local build)
   Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org
   
   /dev/sdc: Unknown USB bridge [0x14cd:0x1212 (0x100)]
   Please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary

Command executed: bash -c "hdparm -I /dev/sdc"
Information returned:
----------------------------------------------------------------------------------------------------
   /dev/sdc:
   
   ATA device, with non-removable media
   Standards:
   	Likely used: 1
   Configuration:
   	Logical		max	current
   	cylinders	0	0
   	heads		0	0
   	sectors/track	0	0
   	--
   	Logical/Physical Sector size:           512 bytes
   	device size with M = 1024*1024:           0 MBytes
   	device size with M = 1000*1000:           0 MBytes 
   	cache/buffer size  = unknown
   Capabilities:
   	IORDY not likely
   	Cannot perform double-word IO
   	R/W multiple sector transfer: not supported
   	DMA: not supported
   	PIO: pio0

Command executed: bash -c "CIDFILE=/sys/block/$(basename /dev/sdc)/device/cid; echo -n "CID: " ; if [ -e $CIDFILE ] ; then cat $CIDFILE  ; else echo "not available" ; fi "
Information returned:
----------------------------------------------------------------------------------------------------
   CID: not available

Hidden areas: unknown


Acquisition
===========

Linux device            : /dev/sdc                                                                                                          
Device size             : 31914983424 (31,9GB)                                                                                              
Format                  : Expert Witness Format, sub-format Guymager - file extension is .Exx                                               
Image meta data         
   Case number          : SADEDINE-2026                                                                                                     
   Evidence number      : SD-01                                                                                                             
   Examiner             : Christophe Donnat                                                                                                 
   Description          : Carte SD contenant les enregistrements des cam�ras                                                                
   Notes                : Identifiant s�rie d�clar� par le lecteur USB : 121220160204.
Num�ro de s�rie physique de la carte SD non confirm�.
Image path and file name: /mnt/data/forensic/SADEDINE-2026/SD-01/SD01.Exx                                                                   
Info  path and file name: /mnt/data/forensic/SADEDINE-2026/SD-01/SD01.info                                                                  
Hash calculation        : MD5 and SHA-256                                                                                                   
Source verification     : off                                                                                                               
Image verification      : on                                                                                                                

No bad sectors encountered during acquisition.
State: Finished successfully

MD5 hash                   : cf7837b9d9a3907f1a8db5b7d0b06922                                
MD5 hash verified source   : --                                                              
MD5 hash verified image    : cf7837b9d9a3907f1a8db5b7d0b06922                                
SHA1 hash                  : --                                                              
SHA1 hash verified source  : --                                                              
SHA1 hash verified image   : --                                                              
SHA256 hash                : 42fa8f6d3351a4ba2446b267637f51a0c1e44df4abd31b002a1ac2212c023c09
SHA256 hash verified source: --                                                              
SHA256 hash verified image : 42fa8f6d3351a4ba2446b267637f51a0c1e44df4abd31b002a1ac2212c023c09
Image verification OK. The image contains exactly the data that was written.

Acquisition started : 2026-10-12 10:17:52 (ISO format YYYY-MM-DD HH:MM:SS)    
Verification started: 2026-10-12 10:46:27                                     
Ended               : 2026-10-12 10:49:04 (0 hours, 31 minutes and 12 seconds)
Acquisition speed   : 17.75 MByte/s (0 hours, 28 minutes and 35 seconds)      
Verification speed  : 193.86 MByte/s (0 hours, 2 minutes and 37 seconds)      


Generated image files and their MD5 hashes
==========================================

No MD5 hashes available (configuration parameter CalcImageFileMD5 is off)
MD5                               Image file
n/a                               SD01.E01
n/a                               SD01.E02
```

### Carte SD-02

#### Branchement sur le PC Linux du prestataire

Le 12/10/2026 à 13h00 environ, la carte SD-02 a été branchée sur le PC Linux du prestataire via l'adaptateur USB fourni par la cliente.

#### Acquisition de l'image disque avec Guymager

Le 12/10/2026 à 13h07 environ, le prestataire a lancé l'acquisition de l'image disque de la carte SD-02 avec le logiciel Guymager.

L'acquisition a été réalisée en mode "read-only" pour éviter toute modification des données présentes sur la carte SD.

#### Résultat de l'acquisition

SHA-256 du flux source SD-02 calculé pendant l’acquisition :
`ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d`

SHA-256 du flux relu dans l’image SD-02 :
`ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d`

> Le SHA-256 du flux acquis et celui du flux relu dans l’image SD-02 concordent ; Guymager indique une vérification de l’image réussie. `Source verification: off` : il ne s’agit pas d’une seconde lecture indépendante de contrôle de la carte après acquisition. Ces valeurs portent sur les données décompressées, pas sur les fichiers segments EWF.

Contenu du fichier `SD02.info`

```bash
GUYMAGER ACQUISITION INFO FILE
==============================

Guymager
========

Version            : 0.8.13-2build3                                                                                         
Version timestamp  : 2025-12-08-22.09.03 UTC                                                                                
Compiled with      : gcc 15.2.0                                                                                             
libewf version     : 20140816 (not used as Guymager is configured to use its own EWF module)                                
libguytools version: 2.1.0                                                                                                  
Host name          : chris-MS-7B48                                                                                          
Domain name        : (none)                                                                                                 
System             : Linux chris-MS-7B48 7.0.0-38-generic #38-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep  4 09:10:14 UTC 2026 x86_64


Device information
==================
Command executed: bash -c "search="`basename /dev/sde`: H..t P.......d A..a de.....d" && dmesg | grep -A3 "$search" || echo "No kernel HPA messages for /dev/sde""
Information returned:
----------------------------------------------------------------------------------------------------
   shell-init: erreur de d�termination du r�pertoire actuel: getcwd : ne peut acc�der aux r�pertoires parents: Erreur d'entr�e/sortie
   job-working-directory: erreur de d�termination du r�pertoire actuel: getcwd : ne peut acc�der aux r�pertoires parents: Erreur d'entr�e/sortie
   No kernel HPA messages for /dev/sde

Command executed: bash -c "smartctl -s on /dev/sde ; smartctl -a /dev/sde"
Information returned:
----------------------------------------------------------------------------------------------------
   shell-init: erreur de d�termination du r�pertoire actuel: getcwd : ne peut acc�der aux r�pertoires parents: Erreur d'entr�e/sortie
   job-working-directory: erreur de d�termination du r�pertoire actuel: getcwd : ne peut acc�der aux r�pertoires parents: Erreur d'entr�e/sortie
   smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.0.0-38-generic] (local build)
   Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org
   
   /dev/sde: Unknown USB bridge [0x14cd:0x1212 (0x100)]
   Please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary
   
   smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.0.0-38-generic] (local build)
   Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org
   
   /dev/sde: Unknown USB bridge [0x14cd:0x1212 (0x100)]
   Please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary

Command executed: bash -c "hdparm -I /dev/sde"
Information returned:
----------------------------------------------------------------------------------------------------
   shell-init: erreur de d�termination du r�pertoire actuel: getcwd : ne peut acc�der aux r�pertoires parents: Erreur d'entr�e/sortie
   
   /dev/sde:
   
   ATA device, with non-removable media
   Standards:
   	Likely used: 1
   Configuration:
   	Logical		max	current
   	cylinders	0	0
   	heads		0	0
   	sectors/track	0	0
   	--
   	Logical/Physical Sector size:           512 bytes
   	device size with M = 1024*1024:           0 MBytes
   	device size with M = 1000*1000:           0 MBytes 
   	cache/buffer size  = unknown
   Capabilities:
   	IORDY not likely
   	Cannot perform double-word IO
   	R/W multiple sector transfer: not supported
   	DMA: not supported
   	PIO: pio0

Command executed: bash -c "CIDFILE=/sys/block/$(basename /dev/sde)/device/cid; echo -n "CID: " ; if [ -e $CIDFILE ] ; then cat $CIDFILE  ; else echo "not available" ; fi "
Information returned:
----------------------------------------------------------------------------------------------------
   shell-init: erreur de d�termination du r�pertoire actuel: getcwd : ne peut acc�der aux r�pertoires parents: Erreur d'entr�e/sortie
   CID: not available

Hidden areas: unknown


Acquisition
===========

Linux device            : /dev/sde                                                                                                          
Device size             : 31914983424 (31,9GB)                                                                                              
Format                  : Expert Witness Format, sub-format Guymager - file extension is .Exx                                               
Image meta data         
   Case number          : SADEDINE-2026                                                                                                     
   Evidence number      : SD-02                                                                                                             
   Examiner             : Christophe Donnat                                                                                                 
   Description          : Carte SD contenant les enregistrements vid�os des cam�ras (terrasse)                                              
   Notes                : Identifiant s�rie d�clar� par le lecteur USB : 121220160204.
Num�ro de s�rie physique de la carte SD non confirm�.
Image path and file name: /mnt/data/forensic/SADEDINE-2026/SD-02/SD02.Exx                                                                   
Info  path and file name: /mnt/data/forensic/SADEDINE-2026/SD-02/SD02.info                                                                  
Hash calculation        : MD5 and SHA-256                                                                                                   
Source verification     : off                                                                                                               
Image verification      : on                                                                                                                

No bad sectors encountered during acquisition.
State: Finished successfully

MD5 hash                   : d15c25a454693c2140a00c9da951e63d                                
MD5 hash verified source   : --                                                              
MD5 hash verified image    : d15c25a454693c2140a00c9da951e63d                                
SHA1 hash                  : --                                                              
SHA1 hash verified source  : --                                                              
SHA1 hash verified image   : --                                                              
SHA256 hash                : ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d
SHA256 hash verified source: --                                                              
SHA256 hash verified image : ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d
Image verification OK. The image contains exactly the data that was written.

Acquisition started : 2026-10-12 13:07:17 (ISO format YYYY-MM-DD HH:MM:SS)    
Verification started: 2026-10-12 13:36:49                                     
Ended               : 2026-10-12 13:40:06 (0 hours, 32 minutes and 48 seconds)
Acquisition speed   : 17.19 MByte/s (0 hours, 29 minutes and 31 seconds)      
Verification speed  : 154.50 MByte/s (0 hours, 3 minutes and 17 seconds)      


Generated image files and their MD5 hashes
==========================================

No MD5 hashes available (configuration parameter CalcImageFileMD5 is off)
MD5                               Image file
n/a                               SD02.E01
n/a                               SD02.E02
n/a                               SD02.E03
n/a                               SD02.E04
n/a                               SD02.E05
n/a                               SD02.E06
n/a                               SD02.E07
n/a                               SD02.E08
n/a                               SD02.E09
n/a                               SD02.E10
n/a                               SD02.E11
n/a                               SD02.E12
n/a                               SD02.E13
n/a                               SD02.E14
n/a                               SD02.E15
```

### Carte SD-03

#### Branchement sur le PC Linux du prestataire

Le 12/10/2026 à 14h00 environ, la carte SD-03 a été branchée sur le PC Linux du prestataire via l'adaptateur USB fourni par la cliente.

#### Acquisition de l'image disque avec Guymager

Le 12/10/2026 à 14h03 environ, le prestataire a lancé l'acquisition de l'image disque de la carte SD-03 avec le logiciel Guymager.

L'acquisition a été réalisée en mode "read-only" pour éviter toute modification des données présentes sur la carte SD.

#### Résultat de l'acquisition

SHA-256 du flux source SD-03 calculé pendant l’acquisition :
`7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0`

SHA-256 du flux relu dans l’image SD-03 :
`7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0`

> Le SHA-256 du flux acquis et celui du flux relu dans l’image SD-03 concordent ; Guymager indique une vérification de l’image réussie. `Source verification: off` : il ne s’agit pas d’une seconde lecture indépendante de contrôle de la carte après acquisition. Ces valeurs portent sur les données décompressées, pas sur les fichiers segments EWF.

Contenu du fichier `SD03.info`

```bash
GUYMAGER ACQUISITION INFO FILE
==============================

Guymager
========

Version            : 0.8.13-2build3                                                                                         
Version timestamp  : 2025-12-08-22.09.03 UTC                                                                                
Compiled with      : gcc 15.2.0                                                                                             
libewf version     : 20140816 (not used as Guymager is configured to use its own EWF module)                                
libguytools version: 2.1.0                                                                                                  
Host name          : chris-MS-7B48                                                                                          
Domain name        : (none)                                                                                                 
System             : Linux chris-MS-7B48 7.0.0-38-generic #38-Ubuntu SMP PREEMPT_DYNAMIC Fri Sep  4 09:10:14 UTC 2026 x86_64


Device information
==================
Command executed: bash -c "search="`basename /dev/sdc`: H..t P.......d A..a de.....d" && dmesg | grep -A3 "$search" || echo "No kernel HPA messages for /dev/sdc""
Information returned:
----------------------------------------------------------------------------------------------------
   No kernel HPA messages for /dev/sdc

Command executed: bash -c "smartctl -s on /dev/sdc ; smartctl -a /dev/sdc"
Information returned:
----------------------------------------------------------------------------------------------------
   smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.0.0-38-generic] (local build)
   Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org
   
   /dev/sdc: Unknown USB bridge [0x14cd:0x1212 (0x100)]
   Please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary
   
   smartctl 7.5 2025-04-30 r5714 [x86_64-linux-7.0.0-38-generic] (local build)
   Copyright (C) 2002-25, Bruce Allen, Christian Franke, www.smartmontools.org
   
   /dev/sdc: Unknown USB bridge [0x14cd:0x1212 (0x100)]
   Please specify device type with the -d option.
   
   Use smartctl -h to get a usage summary

Command executed: bash -c "hdparm -I /dev/sdc"
Information returned:
----------------------------------------------------------------------------------------------------
   /dev/sdc:
   
   ATA device, with non-removable media
   Standards:
   	Likely used: 1
   Configuration:
   	Logical		max	current
   	cylinders	0	0
   	heads		0	0
   	sectors/track	0	0
   	--
   	Logical/Physical Sector size:           512 bytes
   	device size with M = 1024*1024:           0 MBytes
   	device size with M = 1000*1000:           0 MBytes 
   	cache/buffer size  = unknown
   Capabilities:
   	IORDY not likely
   	Cannot perform double-word IO
   	R/W multiple sector transfer: not supported
   	DMA: not supported
   	PIO: pio0

Command executed: bash -c "CIDFILE=/sys/block/$(basename /dev/sdc)/device/cid; echo -n "CID: " ; if [ -e $CIDFILE ] ; then cat $CIDFILE  ; else echo "not available" ; fi "
Information returned:
----------------------------------------------------------------------------------------------------
   CID: not available

Hidden areas: unknown


Acquisition
===========

Linux device            : /dev/sdc                                                                                                          
Device size             : 31914983424 (31,9GB)                                                                                              
Format                  : Expert Witness Format, sub-format Guymager - file extension is .Exx                                               
Image meta data         
   Case number          : SADEDINE-2026                                                                                                     
   Evidence number      : SD-03                                                                                                             
   Examiner             : Christophe Donnat                                                                                                 
   Description          : Carte SD contenant les enregistrement vid�o des cam�ras (salon)                                                   
   Notes                : Identifiant s�rie d�clar� par le lecteur USB : 121220160204.
Num�ro de s�rie physique de la carte SD non confirm�.
Image path and file name: /mnt/data/forensic/SADEDINE-2026/SD-03/SD03.Exx                                                                   
Info  path and file name: /mnt/data/forensic/SADEDINE-2026/SD-03/SD03.info                                                                  
Hash calculation        : MD5 and SHA-256                                                                                                   
Source verification     : off                                                                                                               
Image verification      : on                                                                                                                

No bad sectors encountered during acquisition.
State: Finished successfully

MD5 hash                   : d0402e436587d9cb319f78575e81fec0                                
MD5 hash verified source   : --                                                              
MD5 hash verified image    : d0402e436587d9cb319f78575e81fec0                                
SHA1 hash                  : --                                                              
SHA1 hash verified source  : --                                                              
SHA1 hash verified image   : --                                                              
SHA256 hash                : 7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0
SHA256 hash verified source: --                                                              
SHA256 hash verified image : 7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0
Image verification OK. The image contains exactly the data that was written.

Acquisition started : 2026-10-12 14:03:19 (ISO format YYYY-MM-DD HH:MM:SS)    
Verification started: 2026-10-12 14:32:46                                     
Ended               : 2026-10-12 14:35:50 (0 hours, 32 minutes and 31 seconds)
Acquisition speed   : 17.23 MByte/s (0 hours, 29 minutes and 26 seconds)      
Verification speed  : 165.42 MByte/s (0 hours, 3 minutes and 4 seconds)       


Generated image files and their MD5 hashes
==========================================

No MD5 hashes available (configuration parameter CalcImageFileMD5 is off)
MD5                               Image file
n/a                               SD03.E01
n/a                               SD03.E02
n/a                               SD03.E03
n/a                               SD03.E04
n/a                               SD03.E05
n/a                               SD03.E06
n/a                               SD03.E07
n/a                               SD03.E08
n/a                               SD03.E09
n/a                               SD03.E10
n/a                               SD03.E11
n/a                               SD03.E12
```

---

