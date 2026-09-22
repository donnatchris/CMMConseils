# Analyse de la Freebox Révolution

- **Matériel examiné** : Freebox Révolution du domicile de Mme Sadedine
- **Début de l’analyse** : 16 septembre 2026 à 07:38:38
- **Remarques** : L’analyse a été réalisée à distance via l’interface **Freebox OS**. Les informations présentées ci-dessous reflètent l’état de la Freebox et de la connexion Internet au moment du constat.

---

## Accès à distance

L’accès à distance à l’interface **Freebox OS** a été activé par Mme Sadedine à ma demande le **15 septembre 2026 à 12h27** pour me permettre d'explorer l'interface. Cette activation a été confirmée par un message affiché sur l’écran de la Freebox, indiquant que l’accès à distance était désormais disponible.

### État antérieur

Au moment du constat, l’option « Activer l’authentification par mot de passe » permettant l’accès distant à l’interface Freebox OS n’était pas activée. Les ports d’accès distant HTTP et HTTPS étaient néanmoins configurés. L’interface indique par ailleurs que l’accès distant demeure possible pour les applications autorisées et les liens de partage.

![État antérieur de la Freebox avant l'activation de l'accès à distance - photo transmise par Mme Sadedine](images/freebox-1.jpeg){ width=50% }

### Activation de l’accès à distance

Mme Sadedine m'a remis l'**adresse de connexion à distance**, ainsi que le **mot de passe** associé, afin que je puisse accéder à l’interface **Freebox OS** pour effectuer l’analyse.

**Il faudra désactiver l’accès à distance et modifier le mot de passe après la fin de l’analyse**, afin de sécuriser l’accès à la Freebox et de protéger les informations personnelles de Mme Sadedine.

![Activation de l’accès à distance sur la Freebox - photo transmise par Mme Sadedine](images/freebox-2.jpeg){ width=50% }

---

## État de la Freebox et de la connexion Internet

Lors du contrôle de l’interface **Freebox OS**, la Freebox apparaît connectée à Internet au moyen d’une liaison **FTTH (Fiber To The Home)**.

### État de la connexion Internet

L’écran d’état de la connexion Internet indique les informations suivantes au moment du constat :

* connexion Internet : **active** ;
* type de connexion : **FTTH** ;
* adresse IPv4 publique affichée : **88.178.32.36** ;
* plage de ports IPv4 attribuée : **0 à 16383** ;
* adresse IPv6 affichée : **2a01:e0a:c88:900::1** ;
* volume de données reçu : **4,2 Go** ;
* volume de données émis : **927,2 Mo** ;
* débit maximal indiqué : **1 Gb/s descendant** et **900 Mb/s montant**.

La mention d’une plage de ports IPv4 limitée à **0–16383** indique que l’adresse IPv4 affichée est utilisée avec une attribution partielle de ports.

> En conséquence, dans le cadre de l’analyse de journaux de connexion, une adresse IPv4 seule peut ne pas être suffisante pour attribuer une connexion à cette Freebox : l’**horodatage** et, lorsqu’il est disponible, le **numéro de port source** constituent également des éléments importants.

### État de la liaison fibre

Concernant la liaison fibre, Freebox OS indique :

* état du lien : **Up** ;
* module fibre présent : **Oui** ;
* signal optique : **Présent** ;
* alimentation : **OK** ;
* fabricant du module SFP : **TLE TUNG-LI** ;
* modèle : **OF001-003C** ;
* numéro de série : **2107071255**.

Ces informations décrivent **l’état de la Freebox au moment du constat**. Elles ne permettent pas, à elles seules, de déterminer l’état de la connexion, l’adresse IP attribuée ou la plage de ports utilisée à une date antérieure, notamment en octobre 2024. Toute conclusion concernant cette période devra donc être fondée sur des journaux historiques ou d’autres éléments techniques permettant une corrélation temporelle.

### Historique de connexion

L’historique de connexion consulté fait apparaître, pour le **16 septembre 2026**, deux événements successifs :

- à **09:48:05**, établissement du **lien FTTH**, avec un état « Connecté » et un débit de liaison indiqué de **1 Gb/s en réception** et **900 Mb/s en émission** ;
- à **09:48:26**, établissement de la **connexion Internet FTTH publique**, également indiquée comme « Connectée ».

---

## Gestion des accès

### Applications

3 applications sont actuellement autorisées à accéder à la Freebox via l’interface **Freebox OS** :

1. Freebox Connect (iPhone de dmm conseils) : dernier accès le 21/02/2022 à 00:23:12 ;
2. Freebox Connect (iPhone) : dernier accès le 21/09/2026 à 12:17:20 ;
3. Free (iPhone) : dernier accès le 08/04/2026 à 01:31:09.

![Gestion des accès: Applications](images/freebox-3.png){ width=50% }

#### Droits d'accès des applications

**Au moment du constat, les droits d’accès des applications autorisées étaient nuls**, ce qui signifie qu’aucune application n’avait la possibilité de modifier la configuration de la Freebox ou d’accéder à des informations sensibles.

**Cela ne préjuge pas de l’état des droits d’accès à une date antérieure, notamment en octobre 2024.** Il est donc nécessaire de vérifier les journaux historiques pour déterminer si des applications avaient des droits d’accès à cette période.

![Droits d'accès des applications](images/freebox-4.png){ width=50% }

### Sessions

Lors du constat, l’onglet « Sessions » de la gestion des accès faisait apparaître **une seule session active** à l’interface Freebox OS. Cette session, ouverte le 22 septembre 2026 à 07:38:38, était associée à l’adresse IPv6 2001:861:51c4:5820:4034:8cbe:15e9:b1be.

Cette session correspond à l’accès à distance que j’avais ouvert pour effectuer l’analyse. Elle était toujours active au moment du constat, ce qui indique que l’accès à distance n’avait pas été désactivé depuis mon intervention. Cette ligne de session est donc parfaitement cohérente et normale.

Cet écran décrit les sessions actives au moment du constat et ne constitue pas, à lui seul, un historique des connexions antérieures.

![Sessions actives](images/freebox-5.png){ width=50% }

### Notifications

L’onglet « Notifications » fait apparaître un iPhone enregistré auprès du service de notification de Freebox Connect. Cet appareil est abonné aux catégories « Périphériques réseaux » et « Mot de passe ». La dernière utilisation enregistrée est datée du 21 septembre 2026 à 12:17:18. Cet horaire est cohérent avec le dernier accès relevé à 12:17:20 pour une application Freebox Connect associée à un iPhone.

- Appareil : iPhone
- un identifiant technique de notification : (6FE961F4-05AF-478D-9640-E57C7B9F3D80-notification)
- URL du serveur : https://api.scw.iliad.fr/notifications/freebox/connect
- Type de notification : firebase
- Type de message : notification
- Abonnements :
- Périphériques réseaux
- Mot de passe
- Dernière utilisation : hier à 12:17:18

> Le 21 septembre 2026 vers 12:17, l’application Freebox Connect associée à un iPhone a enregistré un accès à 12:17:20. Le service de notifications associé au même type d’appareil a enregistré une dernière utilisation à 12:17:18. Ces horaires sont cohérents avec les opérations de configuration réalisées par Mme Sadedine à cette période, notamment l’accès aux paramètres de la Freebox. Cette corrélation temporelle ne permet toutefois pas, à elle seule, d’attribuer précisément ces événements à une action déterminée.

![Notifications](images/freebox-6.png){ width=50% }

---

## Disque dur

La Freebox comporte un disque dur interne HGST modèle HCC545050A7E630 d’une capacité nominale de 500,1 Go, utilisant une table de partitions de type MBR. Au moment du constat, le disque était indiqué comme actif, avec une température de 49 °C. Freebox OS faisait état de 2 801 220 opérations de lecture et 160 336 opérations d’écriture, sans erreur de lecture ni d’écriture signalée. Une partition nommée « Disque dur », formatée en ext4, d’une capacité de 244,9 Go était visible, dont 10,5 Go utilisés et 221,9 Go disponibles.

- Disque physique : Disque interne 0 de 500,1 Go
- Modèle : HGST HCC545050A7E630
- Numéro de série : 21GBJZ6T
- Firmware : GR2OA310
- Table de partitions : MBR
- Température : 49 °C
- État : Actif
- Compteur de lectures : 2 801 220
- Erreurs de lecture : 0
- Compteur d'écritures : 160 336
- Erreurs d'écriture : 0

L’interface distante Freebox OS permet l’observation des volumes logiques exposés par la Freebox, mais ne permet pas à elle seule d’établir la table de partitions physique complète du disque interne ni l’affectation de l’intégralité de sa capacité. Une analyse physique du support serait nécessaire pour caractériser précisément les zones non visibles depuis l’interface.

![Disque dur](images/freebox-7.png){ width=50% }

### Explorateur de fichiers

L'explorateur de fichiers intégré à Freebox OS permet d’accéder aux fichiers stockés sur le disque dur interne. Au moment du constat, il contenait uniquement des fichiers liés à des enregistrements TV. Aucun autre fichier n’était visible dans l’explorateur de fichiers.

Les enregistrements identifiés sont:

- quatre épisodes de « Rénovation XXL – Bienvenue au château », diffusés sur Chérie 25 le 10 juillet 2022 ;
- un épisode de « Les reportages de Martin Weill – Mexique : avoir 20 ans sous les Narcos (n°2) », diffusé sur TMC le 4 avril 2023.

Il y a donc **5 enregistrements TV**, chacun accompagné de son fichier d’index `.m2ts.idx`.

Les fichiers vidéo ont été examinés et présentent des caractéristiques compatibles avec des enregistrements de programmes télévisés. Aucun élément particulier en lien avec l’objet de la mission n’a été relevé dans ces fichiers. Les fichiers .m2ts.idx associés correspondent à des fichiers d’index techniques utilisés pour la gestion et la lecture des enregistrements.

```bash
# Échantillon d'examinen de fichier vidéo avec mediainfo
CMMConseils git:(main) ✗ mediainfo ~/Downloads/TMC\ -\ Les\ reportages\ de\ Martin\ Weill\ \(Mexique\ avoir\ 20\ ans\ sous\ les\ Narcos\ \(n°2\)\)\ -\ 04-04-2023\ 22h00\ 55m\ \(5\).m2ts
General
ID                                       : 45770 (0xB2CA)
Complete name                            : /Users/christophedonnat/Downloads/TMC - Les reportages de Martin Weill (Mexique avoir 20 ans sous les Narcos (n°2)) - 04-04-2023 22h00 55m (5).m2ts
Format                                   : BDAV
Format/Info                              : Blu-ray Video
File size                                : 695 MiB
Duration                                 : 49 min 44 s
Overall bit rate mode                    : Variable
Overall bit rate                         : 1 953 kb/s
Frame rate                               : 25.000 FPS

Video
ID                                       : 120 (0x78)
Menu ID                                  : 45770 (0xB2CA)
Format                                   : AVC
Format/Info                              : Advanced Video Codec
Format profile                           : High@L4
Format settings                          : CABAC / 4 Ref Frames
Format settings, CABAC                   : Yes
Format settings, Reference frames        : 4 frames
Codec ID                                 : 27
Duration                                 : 49 min 43 s
Width                                    : 720 pixels
Height                                   : 576 pixels
Display aspect ratio                     : 16:9
Frame rate                               : 25.000 FPS
Standard                                 : PAL
Color space                              : YUV
Chroma subsampling                       : 4:2:0
Bit depth                                : 8 bits
Scan type                                : MBAFF
Scan type, store method                  : Interleaved fields
Scan order                               : Top Field First

Audio #1
ID                                       : 130 (0x82)
Menu ID                                  : 45770 (0xB2CA)
Format                                   : AAC LC
Format/Info                              : Advanced Audio Codec Low Complexity
Format version                           : Version 2
Muxing mode                              : ADTS
Codec ID                                 : 15-2
Duration                                 : 49 min 44 s
Bit rate mode                            : Variable
Channel(s)                               : 2 channels
Channel layout                           : L R
Sampling rate                            : 48.0 kHz
Frame rate                               : 46.875 FPS (1024 SPF)
Compression mode                         : Lossy
Delay relative to video                  : -507 ms
Language                                 : French

Audio #2
ID                                       : 131 (0x83)
Menu ID                                  : 45770 (0xB2CA)
Format                                   : AAC LC SBR
Format/Info                              : Advanced Audio Codec Low Complexity with Spectral Band Replication
Commercial name                          : HE-AAC
Format version                           : Version 2
Format settings                          : Implicit
Muxing mode                              : ADTS
Codec ID                                 : 15-2
Duration                                 : 49 min 44 s
Bit rate mode                            : Variable
Channel(s)                               : 2 channels
Channel layout                           : L R
Sampling rate                            : 48.0 kHz
Frame rate                               : 23.438 FPS (2048 SPF)
Compression mode                         : Lossy
Delay relative to video                  : -195 ms
Language                                 : qaa

Audio #3
ID                                       : 132 (0x84)
Menu ID                                  : 45770 (0xB2CA)
Format                                   : AAC LC SBR
Format/Info                              : Advanced Audio Codec Low Complexity with Spectral Band Replication
Commercial name                          : HE-AAC
Format version                           : Version 2
Format settings                          : Implicit
Muxing mode                              : ADTS
Codec ID                                 : 15-2
Duration                                 : 49 min 43 s
Bit rate mode                            : Variable
Channel(s)                               : 2 channels
Channel layout                           : L R
Sampling rate                            : 48.0 kHz
Frame rate                               : 23.438 FPS (2048 SPF)
Compression mode                         : Lossy
Delay relative to video                  : -299 ms
Language                                 : qad

Text #1
ID                                       : 140 (0x8C)-888
Menu ID                                  : 45770 (0xB2CA)
Format                                   : Teletext Subtitle
Language                                 : French
Language, more info                      : For hearing impaired people

Text #2
ID                                       : 140 (0x8C)-889
Menu ID                                  : 45770 (0xB2CA)
Format                                   : Teletext Subtitle
Language                                 : French
```

![Explorateur de fichiers](images/freebox-8.png){ width=50% }

---

## Connexion internet

### Configuration

La configuration au moment de l'analyse correspond bien à celle affichée dans la capture d'écran envoyée par Mme Sadedine après l'activation de l'accès à distance. On retrouve notamment:

- Port accès distant (HTTP) : 3591
- Port accès distant (HTTPS) : 9717

![Configuration de l'accès à distance](images/freebox-9.png){ width=50% }

### Configuration ipv6

La configuration IPv6 de la Freebox fait apparaître un préfixe principal 2a01:e0a:c88:900::/64 ainsi que plusieurs préfixes secondaires successifs. Aucun « Next Hop » n’était configuré pour ces sous-réseaux au moment du constat. Le pare-feu IPv6 intégré à la Freebox apparaissait désactivé.

Le pare-feu IPv6 intégré à la Freebox était désactivé au moment du constat. En conséquence, la Freebox n’appliquait pas de filtrage IPv6 entrant via cette fonction. La seule désactivation de ce pare-feu ne permet toutefois pas d’établir qu’un équipement du réseau était effectivement accessible depuis Internet, cette accessibilité dépendant également de la configuration IPv6, des services exposés et des mécanismes de filtrage propres à chaque appareil.

![Configuration ipV6](images/freebox-10.png){ width=50% }

### DNS Dynamique

Le service de DNS dynamique intégré à la Freebox n’était pas configuré au moment du constat. Les trois fournisseurs proposés par l’interface — DynDNS, No-IP et OVH — apparaissaient désactivés.

### Serveur VPN et Client VPN

La Freebox dispose de fonctions de serveur VPN prenant en charge plusieurs protocoles, notamment PPTP, OpenVPN, IPsec IKEv2 et WireGuard. Lors du constat, l’ensemble de ces services apparaissait désactivé. Aucun accès au réseau local via le serveur VPN intégré de la Freebox n’était donc actif au moment de l’examen.

Lors du constat, le client VPN intégré à la Freebox était indiqué comme inactif. Le journal de connexion associé ne contenait aucune entrée visible. Aucun tunnel VPN sortant actif ni aucune trace de connexion antérieure n’a donc été relevé dans cette section de Freebox OS au moment de l’examen.

![Configuration serveur VPN](images/freebox-11.png){ width=50% }

![Configuration client VPN](images/freebox-12.png){ width=50% }

### Redirection de Ports et Gestion de Ports

La configuration de gestion des ports ne faisait apparaître aucune redirection de port active ou configurée. La fonction DMZ était également désactivée. Aucun équipement du réseau local n’était donc exposé via ces mécanismes IPv4 au moment du constat.

L’examen de la gestion des ports fait apparaître plusieurs services entrants gérés automatiquement par Freebox OS. Au moment du constat, les accès distants à Freebox OS étaient indiqués comme actifs sur les ports 3591 et 9717. Les ports associés au client BitTorrent intégré de la Freebox étaient également actifs (9830 pour le mécanisme DHT et 13035 pour le port principal).

Les services FTP ainsi que l’ensemble des protocoles de serveur VPN proposés par la Freebox (PPTP, OpenVPN, IPsec/IKEv2 et WireGuard) apparaissaient inactifs.

Par ailleurs, aucune redirection de port manuelle et aucune DMZ n’étaient configurées. Ces constatations décrivent l’état de la configuration au moment de l’examen et ne permettent pas de déterminer si des services différents avaient été activés antérieurement.

![Redirection de Ports](images/freebox-13.png){ width=50% }

![Gestion des Ports](images/freebox-14.png){ width=50% }

![Gestion des Ports](images/freebox-15.png){ width=50% }

---

## Réseau local

### Mode Réseau

La Freebox était configurée en mode routeur. Son adresse IPv4 sur le réseau local était 192.168.1.254 et le domaine local configuré était home. Le serveur Freebox était annoncé sous différents noms selon les mécanismes de résolution utilisés : freebox-server pour DNS, Freebox-Server pour mDNS et Freebox_Server pour NetBIOS.

### Wi-Fi

La Freebox disposait de deux interfaces Wi-Fi actives, en 2,4 GHz et 5 GHz. L’interface 2,4 GHz observée utilisait le canal 6 avec une largeur de bande de 20 MHz et une authentification WPA2. Plusieurs stations étaient associées ou récemment actives, notamment deux iPhone ainsi que plusieurs équipements identifiés par Freebox OS comme provenant de fabricants de modules ou objets connectés, dont Tuya Smart Inc. et Shenzhen Bilian Electronic Co., Ltd. Les adresses MAC, niveaux de signal, durées de connexion et volumes de données associés ont été relevés.

6 appareils / stations Wi-Fi ont été identifiés au moment du constat:

- wlan0 — MAC 1C:90:FF:9D:B8:4A
- iPhone — MAC 6A:92:E3:54:E4:62
- 192-168-1-195 — MAC 70:70:AA:0D:EC:11
- Shenzhen Bilian Electronic Co., Ltd — MAC C4:3C:B0:23:34:46
- Tuya Smart Inc. — MAC CC:8C:BF:8E:33:8A
- iPhone — MAC D2:0E:25:1B:5B:B8

![Wi-Fi](images/freebox-16.png){ width=50% }








# Schéma du réseau local

```text
Internet
   │
   ▼
FREEBOX
   │
   ├── Freebox OS distant
   │     ├── port 3591  ACTIF
   │     └── port 9717  ACTIF
   │
   ├── BitTorrent
   │     ├── port 9830   ACTIF
   │     └── port 13035  ACTIF
   │
   ├── FTP             INACTIF
   │
   ├── VPN serveur     INACTIF
   │
   ├── DMZ             INACTIVE
   │
   ├── Redirections
   │     manuelles     AUCUNE
   │
   └── LAN
         ├── PC
         ├── iPhone
         ├── caméras
         └── ...
```