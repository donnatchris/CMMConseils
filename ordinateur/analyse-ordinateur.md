# Analyse de l'ordinateur OP-01

- **Auteur** : Christophe Donnat - DonnatDev - christophe@donnat.dev
- **Client** : Mme Sadedine Malika - DMM Conseils - dmmconseils@hotmail.com
- **Matériel examiné** : OP-01 (voir ci-dessous)
- **Début de l'analyse** : 08 octobre 2026 à 12:36:00
- **Remarques** : RAS

### Ordinateur portable OP-01

- **Marque :** ASUS
- **Modèle :** UX333F NOTEBOOK PC
- **Numéro de série :** KAN0CV116290436
- **Système d'exploitation :** WINDOWS 11 VERSION 23H2 X64
- **Quelques logiciels installés :** SAGE 50, ADOBE READER, ADOBE ACROBAT, CIEL PAYE EVOLUTION, WORD, EXCEL, OODRIVE_SIGN, OUTLOOK ,OPEN OFFICE 4.1.11, MICROSOFT TEAMS, PAPERCUT MF CLIENT, NORTON 360

### État antérieur

L'ordinateur a été remis au prestataire le 07/10/2026 à 16h15, avec câble d'alimentation et codes de dévérouillage.

---

## Acquisition de l'image disque

### Récupération de la clé BitLocker

L'ordinateur a été allumé par le prestataire le 08/10/2026 à 12h36 afin de récupérer la clé BitLocker et de vérifier l'état du système d'exploitation.

```powershell
Get-CimInstance Win32_Processor | Select-Object Name, Architecture
```

Intel(R) Core(TM) i7-8565U CPU @ 1.80Ghz

```powershell
msinfo32
```

![Résultat de la commande msinfo32](images/OP-01-2.jpg){ width=50% }

Clé BitLocker : `506066-581581-225214-156189-499972-226952-641421-274450`

### Désactivation de Secure Boot

Le 12/10/2026 à 8h55 environ, l'ordinateur a été redémarré et le Secure Boot a été désactivé dans le BIOS.

### Démarrage sur un support externe

Le 12/10/2026 à 8h57 environ, l'ordinateur a été démarré sur un SSD externe contenant un système d'exploitation Linux (Caine) pour permettre l'acquisition de l'image disque.

### Acquisition du disque avec Guymager

Le 12/10/2026 à 9h15 environ, l'acquisition du disque a été réalisée avec le logiciel Guymager. L'image disque a été sauvegardée sur un disque dur externe, dans sa partition `FORENSOC` de 1 To.

L'acquisition a été réalisée en mode "Read Only" pour éviter toute modification du disque source.

> L'image est enregistrée dans le fichier: `OP-01/OP01`	

### Empreinte SHA256 de l'image disque

L'empreinte SHA-256 calculée pendant l'acquisition correspond exactement à celle obtenue lors de la vérification de l'image.

`0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484`

### Contenu du fichier `OP01.info`

```bash
GUYMAGER ACQUISITION INFO FILE
==============================

Guymager
========

Version            : 0.8.13-1                                                                                       
Version timestamp  : 2021-08-04-17.00.00 UTC                                                                        
Compiled with      : gcc 8.3.0                                                                                      
libewf version     : 20140804 (not used as Guymager is configured to use its own EWF module)                        
libguytools version: 2.1.0                                                                                          
Host name          : caine                                                                                          
Domain name        : (none)                                                                                         
System             : Linux caine 6.8.0-52-generic #53-Ubuntu SMP PREEMPT_DYNAMIC Sat Jan 11 00:06:25 UTC 2025 x86_64


Device information
==================
Command executed: bash -c "search="`basename /dev/nvme0n1`: H..t P.......d A..a de.....d" && dmesg | grep -A3 "$search" || echo "No kernel HPA messages for /dev/nvme0n1""
Information returned:
----------------------------------------------------------------------------------------------------
   No kernel HPA messages for /dev/nvme0n1

Command executed: bash -c "smartctl -s on /dev/nvme0n1 ; smartctl -a /dev/nvme0n1"
Information returned:
----------------------------------------------------------------------------------------------------
   smartctl 7.4 2023-08-01 r5530 [x86_64-linux-6.8.0-52-generic] (local build)
   Copyright (C) 2002-23, Bruce Allen, Christian Franke, www.smartmontools.org
   
   NVMe device successfully opened
   
   Use 'smartctl -a' (or '-x') to print SMART (and more) information
   
   smartctl 7.4 2023-08-01 r5530 [x86_64-linux-6.8.0-52-generic] (local build)
   Copyright (C) 2002-23, Bruce Allen, Christian Franke, www.smartmontools.org
   
   === START OF INFORMATION SECTION ===
   Model Number:                       INTEL SSDPEKNW512G8
   Serial Number:                      BTNH93120FL8512A
   Firmware Version:                   002C
   PCI Vendor/Subsystem ID:            0x8086
   IEEE OUI Identifier:                0x5cd2e4
   Controller ID:                      1
   NVMe Version:                       1.3
   Number of Namespaces:               1
   Namespace 1 Size/Capacity:          512.110.190.592 [512 GB]
   Namespace 1 Formatted LBA Size:     512
   Local Time is:                      Mon Oct 12 10:21:57 2026 BST
   Firmware Updates (0x14):            2 Slots, no Reset required
   Optional Admin Commands (0x0017):   Security Format Frmw_DL Self_Test
   Optional NVM Commands (0x005f):     Comp Wr_Unc DS_Mngmt Wr_Zero Sav/Sel_Feat Timestmp
   Log Page Attributes (0x0f):         S/H_per_NS Cmd_Eff_Lg Ext_Get_Lg Telmtry_Lg
   Maximum Data Transfer Size:         32 Pages
   Warning  Comp. Temp. Threshold:     77 Celsius
   Critical Comp. Temp. Threshold:     80 Celsius
   
   Supported Power States
   St Op     Max   Active     Idle   RL RT WL WT  Ent_Lat  Ex_Lat
    0 +     3.50W       -        -    0  0  0  0        0       0
    1 +     2.70W       -        -    1  1  1  1        0       0
    2 +     2.00W       -        -    2  2  2  2        0       0
    3 -   0.0250W       -        -    3  3  3  3     5000    5000
    4 -   0.0040W       -        -    4  4  4  4     5000    9000
   
   Supported LBA Sizes (NSID 0x1)
   Id Fmt  Data  Metadt  Rel_Perf
    0 +     512       0         0
   
   === START OF SMART DATA SECTION ===
   SMART overall-health self-assessment test result: PASSED
   
   SMART/Health Information (NVMe Log 0x02)
   Critical Warning:                   0x00
   Temperature:                        30 Celsius
   Available Spare:                    100%
   Available Spare Threshold:          10%
   Percentage Used:                    2%
   Data Units Read:                    25.961.820 [13,2 TB]
   Data Units Written:                 16.861.871 [8,63 TB]
   Host Read Commands:                 389.140.275
   Host Write Commands:                311.344.116
   Controller Busy Time:               8.903
   Power Cycles:                       924
   Power On Hours:                     2.202
   Unsafe Shutdowns:                   13
   Media and Data Integrity Errors:    0
   Error Information Log Entries:      44
   Warning  Comp. Temperature Time:    0
   Critical Comp. Temperature Time:    0
   
   Error Information (NVMe Log 0x01, 16 of 256 entries)
   No Errors Logged
   
   Self-test Log (NVMe Log 0x06)
   Self-test status: No self-test in progress
   No Self-tests Logged

Command executed: bash -c "hdparm -I /dev/nvme0n1"
Information returned:
----------------------------------------------------------------------------------------------------
   /dev/nvme0n1:

Command executed: bash -c "CIDFILE=/sys/block/$(basename /dev/nvme0n1)/device/cid; echo -n "CID: " ; if [ -e $CIDFILE ] ; then cat $CIDFILE  ; else echo "not available" ; fi "
Information returned:
----------------------------------------------------------------------------------------------------
   CID: not available

Hidden areas: unknown


Acquisition
===========

Linux device            : /dev/nvme0n1                                                       
Device size             : 512110190592 (512,1GB)                                             
Format                  : Expert Witness Format, sub-format Guymager - file extension is .Exx
Image meta data         
   Case number          : SADEDINE-2026                                                      
   Evidence number      : OP-01                                                              
   Examiner             : Christophe Donnat                                                  
   Description          : Image disque du PC de Mme Sadedine                                 
   Notes                : BTNH93120FL8512A                                                   
Image path and file name: /media/sda3/OP-01/OP01.Exx                                         
Info  path and file name: /media/sda3/OP-01/OP01.info                                        
Hash calculation        : MD5 and SHA-256                                                    
Source verification     : off                                                                
Image verification      : on                                                                 

No bad sectors encountered during acquisition.
State: Finished successfully

MD5 hash                   : 10c9f3df1ecd999567a05beaa4056ace                                
MD5 hash verified source   : --                                                              
MD5 hash verified image    : 10c9f3df1ecd999567a05beaa4056ace                                
SHA1 hash                  : --                                                              
SHA1 hash verified source  : --                                                              
SHA1 hash verified image   : --                                                              
SHA256 hash                : 0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484
SHA256 hash verified source: --                                                              
SHA256 hash verified image : 0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484
Image verification OK. The image contains exactly the data that was written.

Acquisition started : 2026-10-12 10:21:57 (ISO format YYYY-MM-DD HH:MM:SS)    
Verification started: 2026-10-12 11:20:34                                     
Ended               : 2026-10-12 12:04:26 (1 hours, 42 minutes and 28 seconds)
Acquisition speed   : 138.86 MByte/s (0 hours, 58 minutes and 37 seconds)     
Verification speed  : 185.63 MByte/s (0 hours, 43 minutes and 51 seconds)     


Generated image files and their MD5 hashes
==========================================

No MD5 hashes available (configuration parameter CalcImageFileMD5 is off)
MD5                               Image file
n/a                               OP01.E01
n/a                               OP01.E02
n/a                               OP01.E03
n/a                               OP01.E04
n/a                               OP01.E05
n/a                               OP01.E06
n/a                               OP01.E07
n/a                               OP01.E08
n/a                               OP01.E09
n/a                               OP01.E10
n/a                               OP01.E11
n/a                               OP01.E12
n/a                               OP01.E13
n/a                               OP01.E14
n/a                               OP01.E15
n/a                               OP01.E16
n/a                               OP01.E17
n/a                               OP01.E18
n/a                               OP01.E19
n/a                               OP01.E20
n/a                               OP01.E21
n/a                               OP01.E22
n/a                               OP01.E23
n/a                               OP01.E24
n/a                               OP01.E25
n/a                               OP01.E26
n/a                               OP01.E27
n/a                               OP01.E28
n/a                               OP01.E29
n/a                               OP01.E30
n/a                               OP01.E31
n/a                               OP01.E32
n/a                               OP01.E33
n/a                               OP01.E34
n/a                               OP01.E35
n/a                               OP01.E36
n/a                               OP01.E37
n/a                               OP01.E38
n/a                               OP01.E39
n/a                               OP01.E40
n/a                               OP01.E41
n/a                               OP01.E42
n/a                               OP01.E43
n/a                               OP01.E44
n/a                               OP01.E45
n/a                               OP01.E46
n/a                               OP01.E47
n/a                               OP01.E48
n/a                               OP01.E49
n/a                               OP01.E50
n/a                               OP01.E51
n/a                               OP01.E52
n/a                               OP01.E53
n/a                               OP01.E54
n/a                               OP01.E55
n/a                               OP01.E56
n/a                               OP01.E57
n/a                               OP01.E58
n/a                               OP01.E59
n/a                               OP01.E60
n/a                               OP01.E61
n/a                               OP01.E62
n/a                               OP01.E63
n/a                               OP01.E64
n/a                               OP01.E65
n/a                               OP01.E66
n/a                               OP01.E67
n/a                               OP01.E68
n/a                               OP01.E69
n/a                               OP01.E70
n/a                               OP01.E71
n/a                               OP01.E72
n/a                               OP01.E73
n/a                               OP01.E74
```

### Remise en état de l'ordinateur

Le 12/10/2026 à 11h20 environ, l'ordinateur a été remis en état de fonctionnement:

- le Secure Boot a été réactivé dans le BIOS
- l'ordinateur a été redémarré et la clé BitLocker a été réactivée

---

## Analyse de l'image dans Swift

```bash
sansforensics@siftworkstation: ~
$ ewfinfo /media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01
ewfinfo 20140816

Acquiry information
	Case number:		SADEDINE-2026
	Description:		Image disque du PC de Mme Sadedine
	Examiner name:		Christophe Donnat
	Evidence number:	OP-01
	Notes:			BTNH93120FL8512A
	Acquisition date:	Mon Oct 12 09:21:57 2026
	System date:		Mon Oct 12 09:21:57 2026
	Operating system used:	6.8.0-52-generic
	Software version used:	guymager 0.8.13-1
	Password:		N/A
	Model:			INTEL SSDPEKNW512G8
	Serial number:		BTNH93120FL8512A

EWF information
	File format:		EnCase 6
	Sectors per chunk:	64
	Error granularity:	1
	Compression method:	deflate
	Compression level:	good (fast) compression

Media information
	Media type:		fixed disk
	Is physical:		yes
	Bytes per sector:	512
	Number of sectors:	1000215216
	Media size:		476 GiB (512110190592 bytes)

Digest hash information
	MD5:			10c9f3df1ecd999567a05beaa4056ace
```

```bash
sansforensics@siftworkstation: ~
$ sudo mmls /mnt/ewf/ewf1
GUID Partition Table (EFI)
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Safety Table
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  Meta      0000000001   0000000001   0000000001   GPT Header
003:  Meta      0000000002   0000000033   0000000032   Partition Table
004:  000       0000002048   0000534527   0000532480   EFI system partition
005:  001       0000534528   0000567295   0000032768   Microsoft reserved partition
006:  002       0000567296   0998472334   0997905039   Basic data partition
007:  -------   0998472335   0998473727   0000001393   Unallocated
008:  003       0998473728   1000210431   0001736704   
009:  -------   1000210432   1000215215   0000004784   Unallocated
```

```bash
sansforensics@siftworkstation: ~
$ sudo blkid -p -O $((567296 * 512)) /mnt/ewf/ewf1
/mnt/ewf/ewf1: VERSION="2" TYPE="BitLocker" USAGE="crypto"
```

```bash
sansforensics@siftworkstation: ~
$ sudo losetup -fP --read-only --show /mnt/ewf/ewf1
/dev/loop14
```

```bash
sansforensics@siftworkstation: ~
$ sudo lsblk -o NAME,SIZE,FSTYPE,TYPE,MOUNTPOINT /dev/loop14
NAME         SIZE FSTYPE    TYPE MOUNTPOINT
loop14     476.9G           loop 
├─loop14p1   260M vfat      part 
├─loop14p2    16M           part 
├─loop14p3 475.8G BitLocker part 
└─loop14p4   848M ntfs      part 

```

```bash
sansforensics@siftworkstation: ~
$ command -v dislocker
/usr/bin/dislocker
sansforensics@siftworkstation: ~
$ sudo dislocker -r \
  -V /dev/loop14p3 \
  -p \
  -- /mnt/dislocker
Enter the recovery password: XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX
Valid password format, continuing.
sansforensics@siftworkstation: ~
$ echo $?
0
sansforensics@siftworkstation: ~
$ sudo ls -lh /mnt/dislocker/
total 0
-r--r--r-- 1 root root 477G Jan  1  1970 dislocker-file
```

```bash
sansforensics@siftworkstation: ~
$ sudo mount -t ntfs-3g \
  -o ro,norecover \
  /mnt/dislocker/dislocker-file \
  /mnt/windows
sansforensics@siftworkstation: ~
$ sudo ls -lah /mnt/windows/
total 14G
drwxrwxrwx  1 root root 4.0K Mar 16  2021 '$Recycle.Bin'
drwxrwxrwx  1 root root 8.0K Oct  2 16:47  .
drwxr-xr-x 22 root root 4.0K Oct 13 11:48  ..
drwxrwxrwx  1 root root    0 Apr  3  2024  CIEL
drwxrwxrwx  1 root root    0 Jul  7  2020  Cache
drwxrwxrwx  1 root root    0 Apr  3  2024  CommonData
lrwxrwxrwx  2 root root   18 Oct 23  2019 'Documents and Settings' -> /mnt/windows/Users
-rwxrwxrwx  2 root root  12K May 22  2023  DumpStack.log
-rwxrwxrwx  2 root root  12K Oct 12 06:49  DumpStack.log.tmp
-rwxrwxrwx  1 root root    9 Oct 23  2019  Finish.log
drwxrwxrwx  1 root root    0 Oct  5  2022  HP
drwxrwxrwx  1 root root    0 Oct 12 06:49  Intel
drwxrwxrwx  1 root root 4.0K Jul 27 17:07  L16B
drwxrwxrwx  1 root root    0 Dec 19  2019  OneDriveTemp
drwxrwxrwx  1 root root    0 May  7  2022  PerfLogs
drwxrwxrwx  1 root root  12K Oct  2 15:23 'Program Files'
drwxrwxrwx  1 root root 8.0K Apr  3  2024 'Program Files (x86)'
drwxrwxrwx  1 root root 8.0K Oct  2 16:12  ProgramData
drwxrwxrwx  1 root root 4.0K Oct  2 15:23  Recovery
drwxrwxrwx  1 root root  20K Oct  2 16:19 'System Volume Information'
drwxrwxrwx  1 root root 4.0K Sep 28  2023  Users
drwxrwxrwx  1 root root  20K Dec  2  2024  Windows
drwxrwxrwx  1 root root 4.0K Oct 10  2024  adobeTemp
-rwxrwxrwx  1 root root  15K Oct 23  2019  devlist.txt
drwxrwxrwx  1 root root    0 Oct 23  2019  eSupport
-rwxrwxrwx  1 root root 7.9G Oct 12 06:51  hiberfil.sys
-rwxrwxrwx  1 root root 5.3G Oct 12 06:49  pagefile.sys
-rwxrwxrwx  1 root root  16M Oct 12 06:49  swapfile.sys
-rwxrwxrwx  2 root root    0 Oct  2 15:23  wal362836C5
```

```bash

```

