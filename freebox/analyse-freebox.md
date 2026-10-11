# Analyse de la Freebox Révolution

- **Auteur** : Christophe Donnat - DonnatDev - christophe@donnat.dev
- **Client** : Mme Sadedine Malika - DMM Conseils - dmmconseils@hotmail.com
- **Matériel examiné** : Freebox Révolution du domicile de Mme Sadedine
- **Début de l'analyse** : 16 septembre 2026 à 07:38:38
- **Remarques** : L'analyse a été réalisée à distance via l'interface **Freebox OS**. Les informations présentées ci-dessous reflètent l'état de la Freebox et de la connexion Internet au moment du constat.

## Accès à distance

L'accès à distance à l'interface **Freebox OS** a été activé par Mme Sadedine à ma demande le **15 septembre 2026 à 12h27** pour me permettre d'explorer l'interface. Cette activation a été confirmée par un message affiché sur l'écran de la Freebox, indiquant que l'accès à distance était désormais disponible.

### État antérieur

Au moment du constat, l'option « Activer l'authentification par mot de passe » permettant l'accès distant à l'interface Freebox OS n'était pas activée. Les ports d'accès distant HTTP et HTTPS étaient néanmoins configurés. L'interface indique par ailleurs que l'accès distant demeure possible pour les applications autorisées et les liens de partage.

![État antérieur de la Freebox avant l'activation de l'accès à distance - photo transmise par Mme Sadedine](images/freebox-1.jpeg){ width=50% }

### Activation de l'accès à distance

Mme Sadedine m'a remis l'**adresse de connexion à distance**, ainsi que le **mot de passe** associé, afin que je puisse accéder à l'interface **Freebox OS** pour effectuer l'analyse.

**Il faudra désactiver l'accès à distance et modifier le mot de passe après la fin de l'analyse**, afin de sécuriser l'accès à la Freebox et de protéger les informations personnelles de Mme Sadedine.

![Activation de l'accès à distance sur la Freebox - photo transmise par Mme Sadedine](images/freebox-2.jpeg){ width=50% }

## État de la Freebox et de la connexion Internet

Lors du contrôle de l'interface **Freebox OS**, la Freebox apparaît connectée à Internet au moyen d'une liaison **FTTH (Fiber To The Home)**.

### État de la connexion Internet

L'écran d'état de la connexion Internet indique les informations suivantes au moment du constat :

- connexion Internet : **active** ;
- type de connexion : **FTTH** ;
- adresse IPv4 publique affichée : **88.178.32.36** ;
- plage de ports IPv4 attribuée : **0 à 16383** ;
- adresse IPv6 affichée : **2a01:e0a:c88:900::1** ;
- volume de données reçu : **4,2 Go** ;
- volume de données émis : **927,2 Mo** ;
- débit maximal indiqué : **1 Gb/s descendant** et **900 Mb/s montant**.

La mention d'une plage de ports IPv4 limitée à **0-16383** indique que l'adresse IPv4 affichée est utilisée avec une attribution partielle de ports.

> En conséquence, dans le cadre de l'analyse de journaux de connexion, une adresse IPv4 seule peut ne pas être suffisante pour attribuer une connexion à cette Freebox : l'**horodatage** et, lorsqu'il est disponible, le **numéro de port source** constituent également des éléments importants.

### État de la liaison fibre

Concernant la liaison fibre, Freebox OS indique :

- état du lien : **Up** ;
- module fibre présent : **Oui** ;
- signal optique : **Présent** ;
- alimentation : **OK** ;
- fabricant du module SFP : **TLE TUNG-LI** ;
- modèle : **OF001-003C** ;
- numéro de série : **2107071255**.

Ces informations décrivent **l'état de la Freebox au moment du constat**. Elles ne permettent pas, à elles seules, de déterminer l'état de la connexion, l'adresse IP attribuée ou la plage de ports utilisée à une date antérieure, notamment en octobre 2024. Toute conclusion concernant cette période devra donc être fondée sur des journaux historiques ou d'autres éléments techniques permettant une corrélation temporelle.

### Historique de connexion

L'historique de connexion consulté fait apparaître, pour le **16 septembre 2026**, deux événements successifs :

- à **09:48:05**, établissement du **lien FTTH**, avec un état « Connecté » et un débit de liaison indiqué de **1 Gb/s en réception** et **900 Mb/s en émission** ;
- à **09:48:26**, établissement de la **connexion Internet FTTH publique**, également indiquée comme « Connectée ».

## Gestion des accès

### Applications

3 applications sont actuellement autorisées à accéder à la Freebox via l'interface **Freebox OS** :

1. Freebox Connect (iPhone de dmm conseils) : dernier accès le 21/02/2022 à 00:23:12 ;
2. Freebox Connect (iPhone) : dernier accès le 21/09/2026 à 12:17:20 ;
3. Free (iPhone) : dernier accès le 08/04/2026 à 01:31:09.

![Gestion des accès : Applications](images/freebox-3.png){ width=50% }

#### Droits d'accès des applications

**Au moment du constat, les droits d'accès des applications autorisées étaient nuls**, ce qui signifie qu'aucune application n'avait la possibilité de modifier la configuration de la Freebox ou d'accéder à des informations sensibles.

**Cela ne préjuge pas de l'état des droits d'accès à une date antérieure, notamment en octobre 2024.** Il est donc nécessaire de vérifier les journaux historiques pour déterminer si des applications avaient des droits d'accès à cette période.

![Droits d'accès des applications](images/freebox-4.png){ width=50% }

### Sessions

Lors du constat, l'onglet « Sessions » de la gestion des accès faisait apparaître **une seule session active** à l'interface Freebox OS. Cette session, ouverte le 22 septembre 2026 à 07:38:38, était associée à l'adresse IPv6 2001:861:51c4:5820:4034:8cbe:15e9:b1be.

Cette session correspond à l'accès à distance que j'avais ouvert pour effectuer l'analyse. Elle était toujours active au moment du constat, ce qui indique que l'accès à distance n'avait pas été désactivé depuis mon intervention. Cette ligne de session est donc parfaitement cohérente et normale.

Cet écran décrit les sessions actives au moment du constat et ne constitue pas, à lui seul, un historique des connexions antérieures.

![Sessions actives](images/freebox-5.png){ width=50% }

### Notifications

L'onglet « Notifications » fait apparaître un iPhone enregistré auprès du service de notification de Freebox Connect. Cet appareil est abonné aux catégories « Périphériques réseaux » et « Mot de passe ». La dernière utilisation enregistrée est datée du 21 septembre 2026 à 12:17:18. Cet horaire est cohérent avec le dernier accès relevé à 12:17:20 pour une application Freebox Connect associée à un iPhone.

- Appareil : iPhone
- Identifiant technique de notification : `6FE961F4-05AF-478D-9640-E57C7B9F3D80-notification`
- URL du serveur : <https://api.scw.iliad.fr/notifications/freebox/connect>
- Type de notification : firebase
- Type de message : notification
- Abonnements :
  - Périphériques réseaux
  - Mot de passe
- Dernière utilisation : hier à 12:17:18

> Le 21 septembre 2026 vers 12:17, l'application Freebox Connect associée à un iPhone a enregistré un accès à 12:17:20. Le service de notifications associé au même type d'appareil a enregistré une dernière utilisation à 12:17:18. Ces horaires sont cohérents avec les opérations de configuration réalisées par Mme Sadedine à cette période, notamment l'accès aux paramètres de la Freebox. Cette corrélation temporelle ne permet toutefois pas, à elle seule, d'attribuer précisément ces événements à une action déterminée.

![Notifications](images/freebox-6.png){ width=50% }

## Connexion internet

### Configuration

La configuration au moment de l'analyse correspond bien à celle affichée dans la capture d'écran envoyée par Mme Sadedine après l'activation de l'accès à distance. On retrouve notamment :

- Port accès distant (HTTP) : 3591
- Port accès distant (HTTPS) : 9717

![Configuration de l'accès à distance](images/freebox-9.png){ width=50% }

### Configuration IPv6

La configuration IPv6 de la Freebox fait apparaître un préfixe principal `2a01:e0a:c88:900::/64` ainsi que plusieurs préfixes secondaires successifs. Aucun « Next Hop » n'était configuré pour ces sous-réseaux au moment du constat. Le pare-feu IPv6 intégré à la Freebox apparaissait désactivé.

Le pare-feu IPv6 intégré à la Freebox était désactivé au moment du constat. En conséquence, la Freebox n'appliquait pas de filtrage IPv6 entrant via cette fonction. La seule désactivation de ce pare-feu ne permet toutefois pas d'établir qu'un équipement du réseau était effectivement accessible depuis Internet, cette accessibilité dépendant également de la configuration IPv6, des services exposés et des mécanismes de filtrage propres à chaque appareil.

![Configuration IPv6](images/freebox-10.png){ width=50% }

### DNS dynamique

Le service de DNS dynamique intégré à la Freebox n'était pas configuré au moment du constat. Les trois fournisseurs proposés par l'interface - DynDNS, No-IP et OVH - apparaissaient désactivés.

### Serveur VPN et client VPN

La Freebox dispose de fonctions de serveur VPN prenant en charge plusieurs protocoles, notamment PPTP, OpenVPN, IPsec IKEv2 et WireGuard. Lors du constat, l'ensemble de ces services apparaissait désactivé. Aucun accès au réseau local via le serveur VPN intégré de la Freebox n'était donc actif au moment de l'examen.

![Configuration serveur VPN](images/freebox-11.png){ width=50% }

Lors du constat, le client VPN intégré à la Freebox était indiqué comme inactif. Le journal de connexion associé ne contenait aucune entrée visible. Aucun tunnel VPN sortant actif ni aucune trace de connexion antérieure n'a donc été relevé dans cette section de Freebox OS au moment de l'examen.

![Configuration client VPN](images/freebox-12.png){ width=50% }

### Redirection de ports et gestion de ports

La configuration de gestion des ports ne faisait apparaître aucune redirection de port active ou configurée. La fonction DMZ était également désactivée. Aucun équipement du réseau local n'était donc exposé via ces mécanismes IPv4 au moment du constat.

L'examen de la gestion des ports fait apparaître plusieurs services entrants gérés automatiquement par Freebox OS. Au moment du constat, les accès distants à Freebox OS étaient indiqués comme actifs sur les ports 3591 et 9717. Les ports associés au client BitTorrent intégré de la Freebox étaient également actifs (9830 pour le mécanisme DHT et 13035 pour le port principal).

Les services FTP ainsi que l'ensemble des protocoles de serveur VPN proposés par la Freebox (PPTP, OpenVPN, IPsec/IKEv2 et WireGuard) apparaissaient inactifs.

Par ailleurs, aucune redirection de port manuelle et aucune DMZ n'étaient configurées. Ces constatations décrivent l'état de la configuration au moment de l'examen et ne permettent pas de déterminer si des services différents avaient été activés antérieurement.

![Redirection de ports](images/freebox-13.png){ width=50% }

![Gestion des ports](images/freebox-14.png){ width=50% }

![Gestion des ports](images/freebox-15.png){ width=50% }

## Réseau local

### Liste des équipements connectés fournie par Mme Sadedine

Mme Sadedine m'a fourni la liste des équipements connectés chez elle.

Voici la liste propre des équipements que Mme Sadedine m'a signalés comme étant les siens ou présents régulièrement chez elle :

- Caméra terrasse - caméra Action
- Caméra salon - caméra Action
- Caméra chambre - caméra Action, utilisée surtout lors des absences/voyages
- Caméra entrée - système Xiaomi Home
- iPhone 13 vert - encore utilisé, avec numéro anglais
- iPhone 13 mini - téléphone courant, acheté en 2025
- iPhone 11 Pro - utilisé ponctuellement, environ une fois par mois, avec numéro étranger
- Ordinateur portable HP
- Ordinateur Asus - anciennement saisi, rallumé récemment
- Imprimante Samsung connectée
- Imprimante HP - non utilisée depuis plusieurs semaines

Appareils de tiers pouvant apparaître ponctuellement sur le réseau :

- Samsung de Cherifa
- iPhone « doudou » / Daklia

Noms d'iPhone mentionnés par Mme Sadedine :

- iPhone de Malika
- iPhone de dmm conseils

### Mode réseau

La Freebox était configurée en mode routeur. Son adresse IPv4 sur le réseau local était `192.168.1.254` et le domaine local configuré était `home`. Le serveur Freebox était annoncé sous différents noms selon les mécanismes de résolution utilisés : `freebox-server` pour DNS, `Freebox-Server` pour mDNS et `Freebox_Server` pour NetBIOS.

### Wi-Fi

La Freebox disposait de deux interfaces Wi-Fi actives, en 2,4 GHz et 5 GHz. L'interface 2,4 GHz observée utilisait le canal 6 avec une largeur de bande de 20 MHz et une authentification WPA2. Plusieurs stations étaient associées ou récemment actives, notamment deux iPhone ainsi que plusieurs équipements identifiés par Freebox OS comme provenant de fabricants de modules ou objets connectés, dont Tuya Smart Inc. et Shenzhen Bilian Electronic Co., Ltd. Les adresses MAC, niveaux de signal, durées de connexion et volumes de données associés ont été relevés.

6 appareils / stations Wi-Fi ont été identifiés au moment du constat :

- wlan0 - MAC `1C:90:FF:9D:B8:4A`
- iPhone - MAC `6A:92:E3:54:E4:62`
- 192-168-1-195 - MAC `70:70:AA:0D:EC:11`
- Shenzhen Bilian Electronic Co., Ltd - MAC `C4:3C:B0:23:34:46`
- Tuya Smart Inc. - MAC `CC:8C:BF:8E:33:8A`
- iPhone - MAC `D2:0E:25:1B:5B:B8`

![Wi-Fi](images/freebox-16.png){ width=50% }

### WPS

L'historique des sessions WPS de la Freebox était vide au moment du constat. Aucune association d'appareil via WPS n'était donc visible dans l'historique disponible. Cette absence d'entrée ne permet toutefois pas d'exclure un usage antérieur du WPS qui ne serait plus conservé par la Freebox.

![Historique WPS](images/freebox-17.png){ width=50% }

### DHCP

L'examen des baux DHCP actifs a permis d'établir une correspondance entre plusieurs adresses MAC et adresses IPv4 locales. Deux iPhone disposaient respectivement des adresses `192.168.1.18` et `192.168.1.73`. Une caméra identifiée par la Freebox sous le nom `mxiang-camera-mwc10_miap06DE` disposait de l'adresse `192.168.1.135`. Trois autres équipements, identifiés sous les noms `wlan0`, `STARVOX-98AAFC131893` et `192-168-1-195`, disposaient respectivement des adresses `192.168.1.159`, `192.168.1.169` et `192.168.1.195`.

Cela permet d'établir des correspondances pour identifier les équipements connectés au réseau local de la Freebox. Les informations relevées sont les suivantes :

- wlan0 - MAC `1C:90:FF:9D:B8:4A` - IP `192.168.1.159` - appareil encore non identifié précisément ; peut être l'imprimante
- iPhone - MAC `6A:92:E3:54:E4:62` - IP `192.168.1.73` - téléphone
- 192-168-1-195 - MAC `70:70:AA:0D:EC:11` - IP `192.168.1.195`
- Shenzhen Bilian Electronic Co., Ltd - MAC `C4:3C:B0:23:34:46` - fabricant de module Wi-Fi, Bluetooth ou carte réseau ; probablement une caméra ou l'imprimante ; appareil encore non identifié précisément
- Tuya Smart Inc. - MAC `CC:8C:BF:8E:33:8A` - plateforme/écosystème IoT utilisé par de nombreux fabricants d'objets connectés ; probablement une caméra ; appareil encore non identifié précisément
- iPhone - MAC `D2:0E:25:1B:5B:B8` - IP `192.168.1.18` - téléphone

J'ai aussi identifié un autre équipement qui n'était pas dans la liste initiale :

- `mxiang-camera-mwc10_miap06DE` - MAC `E0:A2:5A:0D:06:DF` - IP `192.168.1.135` - probablement la caméra Xiaomi Home de l'entrée (le morceau `camera` indique clairement un équipement caméra, et le préfixe `mxiang` / `mi...` est compatible avec l'écosystème Xiaomi/Mijia)

> Les équipements connectés semblent correspondre à ceux signalés par Mme Sadedine, mais il faudrait avoir la liste des adresses MAC de tous les appareils pour confirmer l'identité de chacun. Les correspondances établies sont basées sur les informations disponibles au moment du constat.

![Baux DHCP actifs](images/freebox-18.png){ width=50% }

### Switch

L'examen du switch intégré à la Freebox fait apparaître trois ports disposant d'une liaison physique active. Le port Ethernet 1 dessert l'équipement `mxiang-camera-mwc10_miap06DE`, identifié par l'adresse MAC `E0:A2:5A:0D:06:DF` et précédemment associé à l'adresse IPv4 `192.168.1.135`. Le port Ethernet 2 dessert l'équipement `STARVOX-98AAFC131893`, adresse MAC `98:AA:FC:13:18:93`, associé à l'adresse IPv4 `192.168.1.169`. Le port Ethernet 3 était inactif. Le port Ethernet 4 présentait une liaison active, sans adresse MAC affichée dans cette vue au moment du constat.

- `mxiang-camera-mwc10_miap06DE` - MAC `E0:A2:5A:0D:06:DF` - IP `192.168.1.135` - Ethernet 1
- `STARVOX-98AAFC131893` - MAC `98:AA:FC:13:18:93` - IP `192.168.1.169` - Ethernet 2 - équipement très probablement lié à un système d'alarme/télésurveillance Surtec Starvox
- équipement non identifié - MAC non affichée - IP non déterminée - Ethernet 4
- Ethernet 3 inactif

> Le préfixe MAC `98:AA:FC:1...` correspond à une plage attribuée à Surtec. Starvox est le nom d'un système d'alarme/télésurveillance commercialisé par Surtec : une centrale sans fil destinée à la protection anti-intrusion, avec transmission téléphonique/GSM et fonctions de télésurveillance.

![Switch](images/freebox-19.png){ width=50% }

### UPnP IGD

Le service UPnP IGD était activé sur la Freebox, permettant théoriquement aux équipements du réseau local de demander automatiquement l'ouverture de ports entrants. Toutefois, aucune redirection UPnP active n'était présente au moment du constat.

Cela ne permet pas de dire qu'aucune redirection UPnP n'a jamais existé auparavant, seulement qu'il n'y en avait aucune d'active à cet instant.

![UPnP IGD](images/freebox-20.png){ width=50% }

### Cartographie des équipements actuels trouvés à ce stade

- **mxiang-camera-mwc10_miap06DE**
  - Adresse MAC : `E0:A2:5A:0D:06:DF`
  - IPv4 : `192.168.1.135`
  - Connexion : Ethernet 1
  - Identité probable : caméra IP, probablement la caméra Xiaomi Home de l'entrée - à confirmer.
- **STARVOX-98AAFC131893**
  - Adresse MAC : `98:AA:FC:13:18:93`
  - IPv4 : `192.168.1.169`
  - Connexion : Ethernet 2
  - Identité probable : très probablement centrale / équipement d'alarme Starvox.
- **wlan0**
  - Adresse MAC : `1C:90:FF:9D:B8:4A`
  - IPv4 : `192.168.1.159`
  - Connexion : Wi-Fi 2,4 GHz
  - Identité probable : appareil embarqué non identifié ; imprimante ou objet connecté possible.
- **iPhone**
  - Adresse MAC : `6A:92:E3:54:E4:62`
  - IPv4 : `192.168.1.73`
  - Connexion : Wi-Fi 2,4 GHz
  - Identité probable : un des iPhone de Mme Sadedine - modèle à déterminer.
- **iPhone**
  - Adresse MAC : `D2:0E:25:1B:5B:B8`
  - IPv4 : `192.168.1.18`
  - Connexion : Wi-Fi 2,4 GHz
  - Identité probable : un des iPhone de Mme Sadedine - modèle à déterminer.
- **192-168-1-195**
  - Adresse MAC : `70:70:AA:0D:EC:11`
  - IPv4 : `192.168.1.195`
  - Connexion : Wi-Fi 2,4 GHz
  - Identité probable : appareil non identifié ; activité réseau importante, possiblement caméra ou autre équipement.
- **Shenzhen Bilian Electronic Co., Ltd**
  - Adresse MAC : `C4:3C:B0:23:34:46`
  - IPv4 : non déterminée à ce stade
  - Connexion : Wi-Fi 2,4 GHz
  - Identité probable : objet connecté utilisant un module Wi-Fi Bilian ; caméra possible.
- **Tuya Smart Inc.**
  - Adresse MAC : `CC:8C:BF:8E:33:8A`
  - IPv4 : non déterminée à ce stade
  - Connexion : Wi-Fi 2,4 GHz
  - Identité probable : objet connecté Tuya ; caméra possible.
- **Équipement non identifié**
  - Adresse MAC : non affichée
  - IPv4 : non déterminée
  - Connexion : Ethernet 4
  - Identité probable : équipement physiquement connecté, mais non identifié dans cette vue.

### Précisions sur STARVOX-98AAFC131893

Après vérification auprès de Mme Sadedine, l'équipement identifié par la Freebox sous le nom `STARVOX-98AAFC131893` correspond bien à la centrale d'alarme Starvox aujourd'hui inutilisée, mais qui était installée dans le logement.

## Disque dur

La Freebox comporte un disque dur interne HGST modèle HCC545050A7E630 d'une capacité nominale de 500,1 Go, utilisant une table de partitions de type MBR. Au moment du constat, le disque était indiqué comme actif, avec une température de 49 °C. Freebox OS faisait état de 2 801 220 opérations de lecture et 160 336 opérations d'écriture, sans erreur de lecture ni d'écriture signalée. Une partition nommée « Disque dur », formatée en ext4, d'une capacité de 244,9 Go était visible, dont 10,5 Go utilisés et 221,9 Go disponibles.

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

L'interface distante Freebox OS permet l'observation des volumes logiques exposés par la Freebox, mais ne permet pas à elle seule d'établir la table de partitions physique complète du disque interne ni l'affectation de l'intégralité de sa capacité. Une analyse physique du support serait nécessaire pour caractériser précisément les zones non visibles depuis l'interface.

![Disque dur](images/freebox-7.png){ width=50% }

### Explorateur de fichiers

L'explorateur de fichiers intégré à Freebox OS permet d'accéder aux fichiers stockés sur le disque dur interne. Au moment du constat, il contenait uniquement des fichiers liés à des enregistrements TV. Aucun autre fichier n'était visible dans l'explorateur de fichiers.

Les enregistrements identifiés sont :

- quatre épisodes de « Rénovation XXL - Bienvenue au château », diffusés sur Chérie 25 le 10 juillet 2022 ;
- un épisode de « Les reportages de Martin Weill - Mexique : avoir 20 ans sous les Narcos (n°2) », diffusé sur TMC le 4 avril 2023.

Il y a donc **5 enregistrements TV**, chacun accompagné de son fichier d'index `.m2ts.idx`.

Les fichiers vidéo ont été examinés et présentent des caractéristiques compatibles avec des enregistrements de programmes télévisés. Aucun élément particulier en lien avec l'objet de la mission n'a été relevé dans ces fichiers. Les fichiers `.m2ts.idx` associés correspondent à des fichiers d'index techniques utilisés pour la gestion et la lecture des enregistrements.

```text
# Échantillon d'examen de fichier vidéo avec mediainfo
General
ID                                       : 45770 (0xB2CA)
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
Scan order                               : Top Field First

Audio #1
ID                                       : 130 (0x82)
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
Format                                   : AAC LC SBR
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
Format                                   : AAC LC SBR
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
Format                                   : Teletext Subtitle
Language                                 : French
Language, more info                      : For hearing impaired people

Text #2
ID                                       : 140 (0x8C)-889
Format                                   : Teletext Subtitle
Language                                 : French
```

![Explorateur de fichiers](images/freebox-8.png){ width=50% }

### FTP

**Serveur FTP** - Le serveur FTP intégré à la Freebox était désactivé au moment du constat. L'accès FTP distant était également désactivé. Une configuration d'identification existait néanmoins avec l'utilisateur `freebox`, le mot de passe associé étant signalé par Freebox OS comme insuffisamment robuste. Les ports FTP configurés (477 pour le contrôle et 12448 pour les données en mode passif) étaient précédemment constatés comme inactifs. Aucun démarrage réseau par TFTP n'était configuré, les champs relatifs au serveur TFTP et au fichier de démarrage étant vides.

Cela ne permet pas d'exclure qu'un accès FTP ait été actif à une date antérieure, mais aucun accès FTP n'était visible dans les journaux au moment du constat.

![FTP](images/freebox-21.png){ width=50% }

### Partage de fichiers

#### Partage SMB

Les protocoles SMB2/SMB3 ainsi que le partage de fichiers étaient activés sur la Freebox. L'accès authentifié était désactivé au moment du constat, permettant un accès au partage depuis le réseau local sans identification supplémentaire au niveau de la Freebox. Le partage d'imprimantes était désactivé.

Le partage SMB n'était pas exposé directement à Internet dans la configuration observée. En revanche, un équipement ayant accès au réseau local, notamment par Wi-Fi ou Ethernet, pouvait potentiellement accéder aux fichiers partagés sans authentification supplémentaire au niveau de la Freebox.

Au moment du constat, le disque dur interne de la Freebox ne contenait que des fichiers liés aux enregistrements TV, et aucun autre fichier n'était visible dans l'explorateur de fichiers.

![Partage SMB](images/freebox-22.png){ width=50% }

#### Partage de fichiers Mac OS

Le service de partage de fichiers spécifique à macOS était désactivé au moment du constat. Aucun accès via ce protocole n'était donc actif. Cette désactivation n'empêche toutefois pas un Mac d'accéder aux fichiers partagés de la Freebox via SMB, qui était pour sa part activé.

![Partage de fichiers Mac OS](images/freebox-23.png){ width=50% }

## Synthèse intermédiaire

- pas de redirection de port manuelle ;
- pas de DMZ ;
- aucune redirection UPnP active ;
- aucun serveur VPN actif ;
- client VPN inactif et journal vide ;
- aucune session Freebox OS inconnue actuellement ouverte ;
- pas d'application associée avec des droits d'accès anormaux visibles ;
- pas de DNS dynamique configuré ;
- serveur FTP désactivé et accès FTP distant désactivé ;
- aucun démarrage réseau TFTP configuré ;
- partage de fichiers Mac OS désactivé ;
- partage SMB2/SMB3 activé sur le réseau local, sans authentification supplémentaire au niveau de la Freebox ;
- le partage SMB observé concerne le stockage exposé par la Freebox et n'apparaît pas directement accessible depuis Internet ;
- le pare-feu IPv6 de la Freebox était désactivé au moment du constat ; cet état mérite d'être relevé, sans permettre à lui seul de conclure qu'un équipement était effectivement exposé depuis Internet ;
- aucun fichier inhabituel relevé sur le disque ; les fichiers examinés correspondent à des enregistrements télévisés et à leurs fichiers d'index ;
- équipements réseau visibles globalement compatibles avec ceux déclarés par la cliente, sous réserve de l'identification définitive de certains appareils ;
- aucun historique WPS visible au moment du constat.

> **À ce stade de l'analyse, l'examen de la configuration actuelle de la Freebox n'a mis en évidence aucun élément caractérisant une intrusion active, un accès distant non autorisé ou une exposition manifestement anormale du réseau local.** Certains réglages, notamment le partage SMB sans authentification supplémentaire sur le réseau local et la désactivation du pare-feu IPv6, constituent néanmoins des paramètres permissifs qui doivent être distingués d'une preuve d'intrusion. Cette constatation porte sur l'état observable au moment de l'examen et ne permet pas, à elle seule, d'exclure un accès antérieur ou une activité qui ne serait plus conservée dans les journaux disponibles.

---

## Périphériques réseau

L'analyse porte sur les périphériques non identifiés par Mme Sadedine susceptibles de s'être connectés à la Freebox et d'avoir accédé au réseau local en 2021 ou 2022 — période correspondant au début de son contrôle fiscal — ainsi qu'en octobre 2024, au moment de la perquisition. L'objectif est de déterminer si des périphériques inconnus ont pu se connecter à la Freebox et, dans la mesure du possible, de les identifier.

![Liste des périphériques réseau](images/freebox-24.png){ width=50% }

### Périphériques non identifiés

Pour chaque équipement, les informations ci-dessous reprennent les données affichées par Freebox OS. Les adresses IPv6 suivies de points de suspension sont tronquées dans les captures et ne peuvent pas être reconstituées de manière fiable.

#### E0:A2:5A:0A:A3:F7

**Informations générales**

- Adresse MAC : `E0:A2:5A:0A:A3:F7`
- Constructeur : Shanghai Mo xiang Network Technology CO.,ltd
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun nom renseigné (`.home`)
- Première connexion : 19/07/2024 à 21:02:47
- Dernière joignabilité : jamais

**Connectivités observées**

- Aucune connexion disponible.

> **Analyse.** La Freebox a enregistré l'existence de cette adresse MAC le 19 juillet 2024 à 21:02:47. En l'absence d'adresse IPv4 ou IPv6 associée et de période de joignabilité, cette fiche atteste une détection par la Freebox, mais ne suffit pas à établir que l'équipement a obtenu une connectivité IP effective sur le réseau local.

#### LAPTOP-RMC0B2VU

**Informations générales**

- Adresse MAC : `50:E0:85:63:41:5B`
- Constructeur : Intel Corporate
- Type indiqué par Freebox OS : Ordinateur portable
- Nom principal : `LAPTOP-RMC0B2VU`
- Nom de domaine local : `laptop-rmc0b2vu.home`
- Première connexion : 23/07/2024 à 15:37:02
- Dernière joignabilité : jeudi 03 septembre à 15:48:25

**Noms observés**

- `LAPTOP-RMC0B2VU` — source DHCP
- `LAPTOP-RMC0B2VU` — source mDNS
- Une troisième occurrence du même nom apparaît, mais sa source n'est pas renseignée sur la capture.

**Connectivités observées**

- `192.168.1.194` — IPv4 privée locale ; injoignable depuis 03/09 à 15:48:20 ; inactive depuis 15:48:20.
- `fe80::a1b7:11f0:16bd:b6d` — IPv6 link-local ; injoignable depuis 13/01/2023 à 11:15:08 ; inactive depuis 11:15:23.
- `fe80::7517:2b03:9301:5e7e` — IPv6 link-local ; injoignable depuis 03/09 à 15:47:57 ; inactive depuis 15:48:02.
- `2a01:e0a:c88:900:1779:93d3:…` — IPv6 publique ; injoignable et inactive depuis 03/09 à 15:43:57.
- `2a0d:e487:15ef:3ee4:356c:a…` — IPv6 publique ; injoignable et inactive depuis 03/09 à 13:28:19.
- `2a0d:e487:15ef:3ee4:9481:2…` — IPv6 publique ; injoignable et inactive depuis 03/09 à 13:28:19.
- `2a01:e0a:c88:900:71a2:a4f5:…` — IPv6 publique ; injoignable et inactive depuis 03/09 à 15:48:25.

> **Analyse.** Les adresses IPv4 et IPv6 conservées établissent que cet équipement a disposé d'une connectivité IP effective sur le réseau local. Une incohérence chronologique est toutefois visible : une activité est datée du 13 janvier 2023, alors que le champ « Première connexion » indique le 23 juillet 2024. Ce champ ne peut donc pas être interprété comme la première apparition historique certaine de la machine. Il peut notamment correspondre à la création ou à la recréation de la fiche, à la fusion d'identités, à la conservation d'une ancienne connectivité ou à une évolution de la manière dont Freebox OS rattache les adresses au périphérique.

#### 158742fd-de6e-43df-98be-e440d29c2673

**Informations générales**

- Adresse MAC : `A6:14:3E:8A:34:ED`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : `158742fd-de6e-43df-98be-e440d29c2673`
- Nom de domaine local : non précisé dans les éléments retranscrits
- Source du nom : mDNS
- Première connexion : 04/03/2024 à 00:14:41
- Dernière joignabilité : 14/09/2025 à 18:46:05
- Adresse MAC localement administrée : oui

**Connectivités observées**

- `192.168.1.100` — IPv4 privée locale ; dernière joignabilité : 02/05/2024 à 13:00:02 ; dernière activité : 02/05/2024 à 13:00:02.
- `192.168.1.57` — IPv4 privée locale ; dernière joignabilité : 05/11/2024 à 16:02:17 ; dernière activité : 05/11/2024 à 16:02:17.
- `fe80::10ea:4e7a:ce79:822b` — IPv6 link-local ; dernière joignabilité : 05/11/2024 à 16:02:23 ; dernière activité : 05/11/2024 à 16:02:23.
- `fe80::4c1:c65d:8305:6df8` — IPv6 link-local ; dernière joignabilité : 26/11/2024 à 21:34:07 ; dernière activité : 26/11/2024 à 21:34:07.
- `fe80::14f6:a597:4a04:4c05` — IPv6 link-local ; dernière joignabilité : 13/09/2025 à 20:47:39 ; dernière activité : 13/09/2025 à 20:47:39.
- `fe80::85b:917f:f9f1:10ad` — IPv6 link-local ; dernière joignabilité : 14/09/2025 vers 18:46 ; dernière activité : 14/09/2025 à 18:46:49.
- `2a01:e0a:c88:900:60a8:90c1:…` — IPv6 publique ; dernière joignabilité : 04/11/2024 à 19:23:41 ; dernière activité : 04/11/2024 à 19:23:41.
- `2a01:e0a:c88:900:a8fa:a40c:…` — IPv6 publique ; dernière joignabilité : 26/11/2024 à 21:34:01 ; dernière activité : 26/11/2024 à 21:34:01.
- `2a01:e0a:c88:900:909b:ec16:…` — IPv6 publique ; dernière joignabilité : 09/12/2024 à 09:12:26 ; dernière activité : 09/12/2024 à 09:12:26.

Une autre ligne de connectivité est visible, mais ses données ne sont pas retranscrites dans les éléments disponibles.

> **Analyse.** Les adresses IPv4 et IPv6 conservées établissent que cet équipement a disposé à plusieurs reprises d'une connectivité IP effective sur le réseau local. Son adresse MAC est localement administrée, ce qui est compatible avec l'emploi d'une adresse privée ou aléatoire et explique l'absence d'attribution fiable à un constructeur. Son nom mDNS présente la forme atypique d'un UUID et ne permet pas d'identifier la nature du terminal. Des activités sont visibles les 2 mai, 4, 5 et 26 novembre et 9 décembre 2024, puis les 13 et 14 septembre 2025. Freebox OS affichant principalement la dernière activité connue de chaque adresse, ces données ne constituent pas un journal exhaustif : l'absence d'une entrée datée entre le 15 et le 28 octobre 2024 ne suffit donc pas, à elle seule, à exclure la présence de cet équipement durant cette période.

#### CE:04:84:BC:D2:4D

**Informations générales**

- Adresse MAC : `CE:04:84:BC:D2:4D`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : non précisé dans les éléments retranscrits
- Première connexion : 11/06/2024 à 14:00:54
- Dernière joignabilité : 11/06/2024 à 14:25:49
- Adresse MAC localement administrée : oui
- Adressage relevé : une adresse IPv4 privée, une adresse IPv6 link-local et au moins trois adresses IPv6 publiques commençant par `2a01:e0a:c88:900:…`

**Connectivités observées**

- `192.168.1.98` — IPv4 privée locale ; dernière activité : 11/06/2024 à 14:25:35.
- `fe80::148e:7f35:4ff7:c240` — IPv6 link-local ; dernière activité : 11/06/2024 à 14:25:35.
- `2a01:e0a:c88:900:4c20:2070...` — IPv6 publique ; dernière activité : 11/06/2024 à 14:24:56.
- `2a01:e0a:c88:900:1d53:85bc...` — IPv6 publique ; dernière activité : 11/06/2024 à 14:25:18.
- `2a01:e0a:c88:900:4815:28ed...` — IPv6 publique ; dernière activité : 11/06/2024 à 14:25:49.

> **Analyse.** Les adresses IPv4 et IPv6 conservées établissent que cet équipement a disposé d'une connectivité IP effective sur le réseau local le 11 juin 2024. La première connexion est enregistrée à 14:00:54 et la dernière joignabilité à 14:25:49, soit une présence visible d'environ vingt-cinq minutes. L'adresse MAC est localement administrée, donc compatible avec un mécanisme de randomisation et inexploitable pour attribuer avec certitude un constructeur, une nature ou un propriétaire au périphérique.

#### 16:E8:85:01:02:FD

**Informations générales**

- Adresse MAC : `16:E8:85:01:02:FD`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun
- Première connexion : 02/05/2024 à 12:50:13
- Dernière joignabilité : jamais
- Adresse MAC localement administrée : oui

**Connectivités observées**

- Aucune connexion disponible.

> **Analyse.** La Freebox a créé une fiche pour cette adresse MAC avec une première connexion enregistrée le 2 mai 2024 à 12:50:13. Toutefois, aucun nom d'hôte, aucune adresse IPv4 ou IPv6 et aucune période de joignabilité ne sont conservés. Cette entrée atteste une détection par la Freebox, mais ne suffit pas à démontrer que l'équipement a obtenu une adresse IP ou établi une communication réseau complète. L'adresse MAC localement administrée ne permet pas d'identifier fiablement son constructeur.

#### 4E:B5:4A:B0:3F:04

**Informations générales**

- Adresse MAC : `4E:B5:4A:B0:3F:04`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun
- Première connexion : 21/01/2024 à 14:20:29
- Dernière joignabilité : jamais
- Adresse MAC localement administrée : oui

**Connectivités observées**

- Aucune connexion disponible.

> **Analyse.** La Freebox a créé une fiche pour cette adresse MAC avec une première connexion enregistrée le 21 janvier 2024 à 14:20:29. Toutefois, aucun nom d'hôte, aucune adresse IPv4 ou IPv6 et aucune période de joignabilité ne sont conservés. Cette entrée atteste une détection par la Freebox, mais ne suffit pas à démontrer qu'une communication IP effective a été réalisée. L'adresse MAC localement administrée ne permet pas d'identifier fiablement son constructeur.

#### DE:98:33:8D:2C:A2

**Informations générales**

- Adresse MAC : `DE:98:33:8D:2C:A2`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun
- Première connexion : 16/08/2023 à 17:05:18
- Dernière joignabilité : 11/12/2023 à 11:19:39
- Périodes d'activité visibles : septembre, octobre et décembre 2023
- Adresse MAC localement administrée : oui

**Connectivités observées**

- `192.168.1.75` — IPv4 privée locale ; dernière activité : 11/12/2023 à 11:19:21.
- `fe80::9b:5038:2324:abcd` — IPv6 link-local ; dernière activité : 21/09/2023 à 18:15:30.
- `fe80::2c:c0ba:2091:321e` — IPv6 link-local ; dernière activité : 25/09/2023 à 11:48:16.
- `fe80::1003:fff:5a99:f7a2` — IPv6 link-local ; dernière activité : 18/10/2023 à 18:03:58.
- `fe80::1ca7:f17b:771e:ca2a` — IPv6 link-local ; dernière activité : 11/12/2023 à 11:19:25.
- `2a01:e0a:c88:900:fcf5:d136:…` — IPv6 publique ; dernière activité : 21/09/2023 à 18:19:17.
- `2a01:e0a:c88:900:2010:28d6:…` — IPv6 publique ; dernière activité : 25/09/2023 à 11:41:37.
- `2a01:e0a:c88:900:50f3:73af:…` — IPv6 publique ; dernière activité : 18/10/2023 à 18:03:58.
- `2a01:e0a:c88:900:5488:f574:…` — IPv6 publique ; dernière activité : 11/12/2023 à 11:19:39.

> **Analyse.** Les adresses IPv4 et IPv6 conservées établissent que cet équipement a disposé d'une connectivité IP effective sur le réseau local à plusieurs reprises, les 21 et 25 septembre, le 18 octobre et le 11 décembre 2023. Sa dernière joignabilité est enregistrée le 11 décembre 2023 à 11:19:39. L'adresse MAC localement administrée est compatible avec une adresse privée ou aléatoire et ne permet pas d'identifier fiablement le constructeur, la nature exacte ou le propriétaire de l'équipement.

#### E6:E1:90:ED:E4:94

**Informations générales**

- Adresse MAC : `E6:E1:90:ED:E4:94`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun
- Première connexion : 11/10/2022 à 16:24:30
- Dernière joignabilité : jamais
- Adresse MAC localement administrée : oui

**Connectivités observées**

- Aucune connexion disponible.

> **Analyse.** La Freebox a créé une fiche pour cette adresse MAC avec une première connexion enregistrée le 11 octobre 2022 à 16:24:30. Toutefois, aucun nom d'hôte, aucune adresse IPv4 ou IPv6 et aucune période de joignabilité ne sont conservés. Cette entrée atteste une détection par la Freebox, mais ne suffit pas à démontrer qu'une connectivité IP effective a été établie. L'adresse MAC localement administrée ne permet pas d'identifier fiablement son constructeur.

#### 56:96:03:FB:28:58

**Informations générales**

- Adresse MAC : `56:96:03:FB:28:58`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun
- Première connexion : 07/07/2022 à 19:00:35
- Dernière joignabilité : 07/07/2022 à 19:20:58
- Adresse MAC localement administrée : oui

**Connectivités observées**

- `fe80::47:d6f:9c8:cab6` — IPv6 link-local ; dernière activité : 07/07/2022 à 19:21:38.
- `2a01:e0a:2ac:31c0:51c:d253:…` — IPv6 publique ; dernière activité : 07/07/2022 à 19:20:56.

> **Analyse.** Les deux adresses IPv6 conservées établissent qu'une connectivité IP effective a été observée sur le réseau local le 7 juillet 2022. La première connexion est enregistrée à 19:00:35, la dernière joignabilité à 19:20:58 et la dernière activité visible à 19:21:38, soit une présence visible d'environ vingt minutes. L'adresse MAC localement administrée est compatible avec une adresse privée ou aléatoire et ne permet pas d'identifier fiablement le constructeur ou le propriétaire du périphérique.

#### F2:D1:B4:69:51:D8

**Informations générales**

- Adresse MAC : `F2:D1:B4:69:51:D8`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun
- Première connexion : jamais
- Dernière joignabilité : 01/02/2023 à 05:30:41
- Adresse MAC localement administrée : oui

**Connectivités observées**

- `192.168.1.131` — IPv4 privée locale ; dernière activité : 01/02/2023 à 05:30:42.
- `fe80::871:7789:4e19:8cb9` — IPv6 link-local ; dernière activité : 15/10/2022 à 05:52:22.
- `fe80::89a:aedd:644d:a1a7` — IPv6 link-local ; dernière activité : 17/11/2022 à 20:55:01.
- `fe80::18b5:f541:cfb3:4366` — IPv6 link-local ; dernière activité : 30/12/2022 à 00:49:11.
- `fe80::ef:40d2:49e3:8851` — IPv6 link-local ; dernière activité : 01/02/2023 à 05:30:42.
- `2a01:e0a:2ac:31c0:19cf:319d:…` — IPv6 publique ; dernière activité : 30/12/2022 à 09:24:46.
- `2a01:e0a:2ac:31c0:480a:a36…` — IPv6 publique ; dernière activité : 30/12/2022 à 00:49:11.
- `2a01:e0a:2ac:31c0:e82e:221…` — IPv6 publique ; dernière activité : 24/01/2023 à 14:25:16.
- `2a01:e0a:2ac:31c0:61cb:f875…` — IPv6 publique ; dernière activité : 01/02/2023 à 05:18:45.

> **Analyse.** Les adresses IPv4 et IPv6 conservées établissent qu'une connectivité IP effective a été observée entre le 15 octobre 2022 et le 1er février 2023. Le champ « Première connexion » indique pourtant « Jamais » : cette contradiction montre que ce champ ne constitue pas un historique exhaustif et ne doit pas être interprété isolément. La dernière activité visible est datée du 1er février 2023 à 05:30:42. L'adresse MAC localement administrée ne permet pas d'identifier fiablement le constructeur ou le propriétaire du périphérique.

#### B6:BD:59:D2:25:62

**Informations générales**

- Adresse MAC : `B6:BD:59:D2:25:62`
- Constructeur : inconnu
- Type indiqué par Freebox OS : Ordinateur fixe
- Nom principal : aucun
- Nom de domaine local : aucun
- Première connexion : jamais
- Dernière joignabilité : 02/05/2022 à 21:19:52
- Adresse MAC localement administrée : oui

**Connectivités observées**

- `fe80::8a7:990a:8f9:7d7c` — IPv6 link-local ; dernière activité : 05/04/2022 à 21:37:27.
- `fe80::1c6f:7df7:4086:ea17` — IPv6 link-local ; dernière activité : 24/04/2022 à 20:07:18.
- `fe80::85b:6e97:8d8a:69af` — IPv6 link-local ; dernière activité : 01/05/2022 à 18:40:59.
- `fe80::862:b6c9:857c:cc5c` — IPv6 link-local ; dernière activité : 02/05/2022 à 21:19:52.
- `2a01:e0a:2ac:31c0:5c5b:510…` — IPv6 publique ; dernière activité : 02/05/2022 à 21:11:12.
- `2a01:e0a:2ac:31c0:25fa:1d5…` — IPv6 publique ; dernière activité : 02/05/2022 à 21:11:50.
- `2a01:e0a:2ac:31c0:e4a5:185…` — IPv6 publique ; dernière activité : 02/05/2022 à 21:15:31.
- `2a01:e0a:2ac:31c0:d87f:9e7…` — IPv6 publique ; dernière activité : 02/05/2022 à 21:19:26.

> **Analyse.** Les adresses IPv6 conservées établissent qu'une connectivité IP effective a été observée entre le 5 avril et le 2 mai 2022, bien qu'aucune adresse IPv4 ne soit visible. Le champ « Première connexion » indique pourtant « Jamais » : cette contradiction montre que ce champ ne constitue pas un historique exhaustif et ne doit pas être interprété isolément. La dernière activité et la dernière joignabilité visibles sont datées du 2 mai 2022 vers 21:19. L'adresse MAC localement administrée ne permet pas d'identifier fiablement le constructeur ou le propriétaire du périphérique.

### Synthèse des périphériques non identifiés

- Une connectivité IP effective est établie pour sept équipements : `LAPTOP-RMC0B2VU`, `158742fd-de6e-43df-98be-e440d29c2673`, `CE:04:84:BC:D2:4D`, `DE:98:33:8D:2C:A2`, `56:96:03:FB:28:58`, `F2:D1:B4:69:51:D8` et `B6:BD:59:D2:25:62`.
- Pour `E0:A2:5A:0A:A3:F7`, `16:E8:85:01:02:FD`, `4E:B5:4A:B0:3F:04` et `E6:E1:90:ED:E4:94`, les fiches conservées attestent une détection par la Freebox, mais aucune adresse IP ni période de joignabilité ne permet d'établir une connectivité IP effective.
- Neuf des onze équipements utilisent une adresse MAC localement administrée. Ce mécanisme, courant pour les adresses privées ou aléatoires, empêche généralement d'attribuer fiablement le terminal à un constructeur et ne constitue pas, en lui-même, un indice d'activité malveillante.
- Les incohérences relevées dans les champs « Première connexion » montrent que l'inventaire Freebox OS ne doit pas être assimilé à un journal chronologique exhaustif. Il permet d'établir certaines présences, mais pas d'exclure une présence à une date pour laquelle aucune ligne n'est affichée.
- Parmi les données retranscrites, une activité est explicitement datée du 18 octobre 2023, mais aucune ne l'est d'octobre 2024. Cette absence ne permet toutefois pas, à elle seule, d'exclure une connexion durant la période de la perquisition.

> **Conclusion.** Les données disponibles confirment la présence historique de plusieurs périphériques non identifiés sur le réseau local, sans permettre d'en déterminer le propriétaire ni d'en déduire une activité malveillante. Les traces les plus probantes sont les connectivités IPv4 ou IPv6 associées à sept équipements. Pour les quatre autres, seule l'existence d'une fiche est établie. En raison du caractère partiel de l'inventaire et des incohérences de certains champs, aucune conclusion définitive sur la présence ou l'absence d'un équipement à une date précise ne peut être tirée de ces seuls éléments.

![Périphériques non identifiés](images/freebox-25.png){ width=25% }
![Périphériques non identifiés](images/freebox-26.png){ width=25% }
![Périphériques non identifiés](images/freebox-27.png){ width=25% }
![Périphériques non identifiés](images/freebox-28.png){ width=25% }
![Périphériques non identifiés](images/freebox-29.png){ width=25% }
![Périphériques non identifiés](images/freebox-30.png){ width=25% }
![Périphériques non identifiés](images/freebox-31.png){ width=25% }
![Périphériques non identifiés](images/freebox-32.png){ width=25% }
![Périphériques non identifiés](images/freebox-33.png){ width=25% }
![Périphériques non identifiés](images/freebox-34.png){ width=25% }
![Périphériques non identifiés](images/freebox-35.png){ width=25% }
![Périphériques non identifiés](images/freebox-36.png){ width=25% }
![Périphériques non identifiés](images/freebox-37.png){ width=25% }
![Périphériques non identifiés](images/freebox-38.png){ width=25% }
![Périphériques non identifiés](images/freebox-39.png){ width=25% }
![Périphériques non identifiés](images/freebox-40.png){ width=25% }
![Périphériques non identifiés](images/freebox-41.png){ width=25% }
![Périphériques non identifiés](images/freebox-42.png){ width=25% }
![Périphériques non identifiés](images/freebox-43.png){ width=25% }
![Périphériques non identifiés](images/freebox-44.png){ width=25% }
![Périphériques non identifiés](images/freebox-45.png){ width=25% }
![Périphériques non identifiés](images/freebox-46.png){ width=25% }
![Périphériques non identifiés](images/freebox-47.png){ width=25% }
![Périphériques non identifiés](images/freebox-48.png){ width=25% }
![Périphériques non identifiés](images/freebox-49.png){ width=25% }
![Périphériques non identifiés](images/freebox-50.png){ width=25% }

---

## Accès à l'api de la Freebox

L’accès à l’API de la Freebox a été réalisé au moyen du mécanisme d’authentification prévu par Freebox OS. Une demande d’association a d’abord été initiée depuis un ordinateur connecté au réseau local de la cliente, ce qui a généré un identifiant d’application (app_id) et un jeton applicatif (app_token). Cette demande a ensuite été validée physiquement sur le Freebox Server, permettant l’autorisation de l’application.

Depuis le poste d’analyse distant, l’API publique de la Freebox a ensuite été interrogée via son nom de domaine d’accès distant et son port HTTPS. L’ouverture de session a reposé sur un mécanisme de challenge-réponse: la Freebox fournit une valeur temporaire (challenge), à partir de laquelle une réponse HMAC-SHA1 est calculée en utilisant l’app_token comme clé secrète. Cette réponse est transmise à l’endpoint de connexion de l’API, qui retourne alors un session_token. Ce jeton de session a ensuite été utilisé dans l’en-tête X-Fbx-App-Auth pour effectuer des requêtes en lecture sur les différents endpoints de l’API, notamment ceux relatifs au réseau local, au Wi-Fi, au DHCP, au NAT et aux services VPN.

```bash
APP_TOKEN='Ocs6IU76SZgJTjGw2dGjpqzOe15y4TQrdICciCdB+AB8qc60gERrflVb6sde/Gki'
APP_ID='fr.donnat.freebox.forensic'
BASE_URL='https://v28vy0w8.fbxos.fr:9717/api/v16'
```

Pour obtention du session_token, la requête POST suivante a été effectuée sur l’endpoint `/login/session` :

```bash
CHALLENGE=$(curl -sk "$BASE_URL/login/" | jq -r '.result.challenge')

PASSWORD=$(printf '%s' "$CHALLENGE" | openssl dgst -sha1 -hmac "$APP_TOKEN" | awk '{print $NF}')

SESSION_JSON=$(curl -sk -X POST "$BASE_URL/login/session/" \
  -H 'Content-Type: application/json' \
  -d "{\"app_id\":\"$APP_ID\",\"app_version\":\"1.0\",\"password\":\"$PASSWORD\"}")

echo "$SESSION_JSON" | jq

SESSION_TOKEN=$(printf '%s' "$SESSION_JSON" | jq -r '.result.session_token')
```

Pour vérifier:

```bash
curl -sk "$BASE_URL/system/" \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN" | jq
```

On doit obtenir: `"success": "true"`

---

# Analyse de l'historique des appareils par l'API Freebox

- Date de collecte : 28 septembre 2026
- Source : API Freebox OS v16, interface LAN `pub`
- Date limite demandée : avant le 29 octobre 2024 à 00:00:00, heure de Paris
- Seuil Unix correspondant : `1730156400`
- Document comparé : `freebox/freebox.md`

---

## Objet et méthode

L'objectif est de recenser les appareils pour lesquels l'API conserve au moins une trace antérieure au 29 octobre 2024, puis de comparer cet inventaire avec les onze appareils qualifiés de « suspects » dans `freebox/freebox.md`.

Les appels à l'API ont été effectués séquentiellement. Aucun appel parallèle ni boucle de requêtes n'a été utilisé. Une seule requête a servi à récupérer l'inventaire complet de l'interface `pub`, puis une requête distincte a été effectuée pour chacun des onze appareils suspects. Les filtrages, tris et conversions de dates ont ensuite été réalisés localement sur les réponses enregistrées.

Pour chaque fiche, les champs suivants ont été examinés : `first_activity`, `last_activity`, `last_time_reachable`, ainsi que `last_activity` et `last_time_reachable` de chaque entrée `l3connectivities`.

Deux niveaux de preuve sont distingués :

- **IP effective** : au moins une connectivité IPv4 ou IPv6 conserve un horodatage antérieur à la date limite ;
- **détection seulement** : la fiche contient une trace générale antérieure à la date limite, mais aucune connectivité IP antérieure n'est encore conservée dans `l3connectivities`.

Cette seconde catégorie ne signifie pas que l'appareil n'a jamais eu d'adresse IP. L'API conserve essentiellement le dernier état ou le dernier horodatage associé à chaque adresse, et non un journal exhaustif de toutes les connexions.

Les horodatages Unix ont été convertis avec le fuseau historique `Europe/Paris`, donc avec CET en hiver et CEST en été.

---

## Commandes exécutées

### Authentification et vérification

Les variables `APP_TOKEN`, `APP_ID` et `BASE_URL` ont été chargées depuis `freebox/api.md`. Les valeurs sensibles du jeton applicatif et du jeton de session ne sont pas reproduites dans ce rapport.

```bash
curl -sk "$BASE_URL/login/" -o /tmp/freebox_login.json -w '%{http_code}\n'

CHALLENGE=$(jq -r '.result.challenge' /tmp/freebox_login.json)
PASSWORD=$(printf '%s' "$CHALLENGE" | openssl dgst -sha1 -hmac "$APP_TOKEN" | awk '{print $NF}')

curl -sk -X POST "$BASE_URL/login/session/" \
  -H 'Content-Type: application/json' \
  -d "{\"app_id\":\"$APP_ID\",\"app_version\":\"1.0\",\"password\":\"$PASSWORD\"}" \
  -o /tmp/freebox_session.json -w '%{http_code}\n'

SESSION_TOKEN=$(jq -r '.result.session_token' /tmp/freebox_session.json)

curl -sk "$BASE_URL/system/" \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN" \
  -o /tmp/freebox_system.json -w '%{http_code}\n'
```

Résultats : les trois requêtes HTTP ont retourné `200`; les réponses d'ouverture de session et de vérification contenaient `"success": true`.

### Inventaire LAN

```bash
curl -sk "$BASE_URL/lan/browser/interfaces/" \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN" \
  -o /tmp/freebox_lan_interfaces.json -w '%{http_code}\n'

curl -sk "$BASE_URL/lan/browser/pub/" \
  -H "X-Fbx-App-Auth: $SESSION_TOKEN" \
  -o freebox/preuves-json/lan-browser-pub-raw.json -w '%{http_code}\n'
```

Résultats : les deux requêtes ont retourné `200` et `"success": true`. La première réponse annonçait `75` hôtes sur `pub`; la seconde a retourné `74` fiches. Cet écart d'une fiche peut correspondre à un compteur non rafraîchi ou à une modification de l'inventaire entre les deux appels. Le présent rapport repose sur les 74 fiches effectivement retournées et conservées dans `freebox/preuves-json/lan-browser-pub-raw.json`.

### Requêtes détaillées des onze appareils suspects

Toutes les commandes suivantes ont été exécutées séparément, dans l'ordre, et ont retourné HTTP `200` avec `"success": true` :

```bash
curl -sk "$BASE_URL/lan/browser/pub/ether-e0%3Aa2%3A5a%3A0a%3Aa3%3Af7" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-e0-a2-5a-0a-a3-f7.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-50%3Ae0%3A85%3A63%3A41%3A5b" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-50-e0-85-63-41-5b.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-a6%3A14%3A3e%3A8a%3A34%3Aed" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-a6-14-3e-8a-34-ed.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-ce%3A04%3A84%3Abc%3Ad2%3A4d" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-ce-04-84-bc-d2-4d.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-16%3Ae8%3A85%3A01%3A02%3Afd" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-16-e8-85-01-02-fd.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-4e%3Ab5%3A4a%3Ab0%3A3f%3A04" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-4e-b5-4a-b0-3f-04.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-de%3A98%3A33%3A8d%3A2c%3Aa2" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-de-98-33-8d-2c-a2.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-e6%3Ae1%3A90%3Aed%3Ae4%3A94" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-e6-e1-90-ed-e4-94.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-56%3A96%3A03%3Afb%3A28%3A58" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-56-96-03-fb-28-58.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-f2%3Ad1%3Ab4%3A69%3A51%3Ad8" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-f2-d1-b4-69-51-d8.json -w '%{http_code}\n'
curl -sk "$BASE_URL/lan/browser/pub/ether-b6%3Abd%3A59%3Ad2%3A25%3A62" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/suspect-b6-bd-59-d2-25-62.json -w '%{http_code}\n'
```

---

## Appareils présentant une trace avant le 29 octobre 2024

L'API contient 56 fiches ayant au moins un horodatage positif antérieur au seuil : 40 avec une connectivité IP historique conservée et 16 avec uniquement une trace de détection ou de fiche antérieure au seuil.

Les colonnes « première » et « dernière trace retenue » désignent les horodatages minimum et maximum encore présents dans la fiche avant la date limite. Elles ne constituent pas nécessairement les véritables première et dernière connexions historiques.

| Adresse MAC | Nom principal API | Première trace retenue | Dernière trace retenue avant la limite | Nature de la preuve | Dans la liste suspecte |
|---|---|---:|---:|---|---|
| `A0:9D:C1:D1:B9:73` | android-d7cace0bd4fdd799 | 26/03/2022 23:56:24 | 29/03/2022 19:52:21 | IP effective | non |
| `B6:BD:59:D2:25:62` | — | 05/04/2022 21:37:27 | 02/05/2022 21:19:52 | IP effective | oui |
| `10:8E:E0:58:1E:04` | Galaxy-Tab-A-8 | 06/04/2022 10:58:11 | 08/04/2022 13:47:48 | IP effective | non |
| `A6:0D:19:D5:05:58` | Galaxy-S20 | 06/04/2022 11:39:23 | 09/04/2022 19:58:53 | IP effective | non |
| `14:94:6C:65:5B:E8` | iPhone | 07/07/2022 18:54:10 | 07/07/2022 19:01:18 | IP effective | non |
| `56:96:03:FB:28:58` | — | 07/07/2022 19:00:35 | 07/07/2022 19:21:38 | IP effective | oui |
| `3E:2B:7F:22:80:52` | 84b3bd87-59c0-4279-9cc4-643bbb2a7b6a | 07/07/2022 19:21:39 | 07/07/2022 19:21:44 | IP effective | non |
| `B0:22:7A:5F:5C:A9` | HPB0227A5F5CA8 | 13/08/2022 06:45:51 | 19/07/2024 22:16:55 | IP effective | non |
| `D6:58:E4:04:CA:0D` | S22-de-Cherifa | 18/08/2022 19:33:19 | 09/09/2023 23:37:57 | IP effective | non |
| `E6:E1:90:ED:E4:94` | — | 11/10/2022 16:24:30 | 11/10/2022 16:24:30 | détection seulement | oui |
| `F2:D1:B4:69:51:D8` | — | 15/10/2022 05:52:22 | 01/02/2023 04:30:42 | IP effective | oui |
| `36:6E:8E:DF:A3:3D` | ecb906e6-22e3-4cd1-996b-f1e9df24eedb | 01/12/2022 13:32:21 | 07/12/2022 11:38:55 | IP effective | non |
| `DA:10:04:69:3E:56` | iPhonedeDoudou | 03/12/2022 23:46:45 | 14/12/2023 23:42:25 | IP effective | non |
| `26:30:27:16:9F:92` | iPhone-2 | 08/12/2022 19:56:56 | 04/03/2024 14:04:23 | IP effective | non |
| `C0:D0:12:70:F6:F8` | iPhonedconseils | 10/12/2022 19:32:21 | 10/12/2022 21:55:21 | IP effective | non |
| `50:E0:85:63:41:5B` | LAPTOP-RMCOB2VU | 13/01/2023 10:15:08 | 23/07/2024 15:37:02 | IP effective | oui |
| `54:EF:33:08:86:DF` | Android | 27/01/2023 22:29:56 | 19/02/2024 17:48:31 | IP effective | non |
| `F4:CA:E5:6A:25:89` | Freebox Player | 24/02/2023 00:41:50 | 19/07/2024 22:46:42 | IP effective | non |
| `52:60:FA:6C:6A:8C` | — | 24/03/2023 15:11:22 | 24/03/2023 15:11:22 | détection seulement | non |
| `3C:91:80:72:50:55` | LAPTOP-9UHPONKK | 29/03/2023 10:09:50 | 11/03/2024 15:17:29 | IP effective | non |
| `F8:28:19:77:42:71` | LAPTOP-205Q5H9C | 20/05/2023 19:02:43 | 26/03/2024 15:48:20 | IP effective | non |
| `7E:3D:31:A2:03:8C` | iPhone-33 | 17/06/2023 22:29:21 | 20/06/2023 00:40:17 | IP effective | non |
| `CC:8C:BF:8E:33:8A` | — | 20/06/2023 16:36:00 | 20/06/2023 16:36:00 | détection seulement | non |
| `C4:3C:B0:23:34:46` | — | 10/07/2023 16:13:21 | 10/07/2023 16:13:21 | détection seulement | non |
| `04:BA:8D:74:86:3A` | SM-J260F | 31/07/2023 14:49:10 | 31/07/2023 18:01:53 | IP effective | non |
| `72:4E:33:8A:6E:D5` | iPad-de-Gregory | 10/08/2023 00:39:31 | 10/08/2023 00:44:31 | IP effective | non |
| `86:D5:17:EE:D8:70` | Apple-Watch | 10/08/2023 01:02:02 | 10/08/2023 01:08:56 | IP effective | non |
| `E0:5F:45:73:03:3C` | iPhone | 14/08/2023 12:13:41 | 25/06/2024 02:36:34 | IP effective | non |
| `7C:A1:AE:B3:34:F9` | iPhonedeMalika | 16/08/2023 01:21:40 | 16/08/2023 13:17:10 | IP effective | non |
| `DE:98:33:8D:2C:A2` | — | 16/08/2023 17:05:18 | 11/12/2023 10:19:39 | IP effective | oui |
| `84:AB:1A:E4:7A:BD` | iPhone | 21/09/2023 18:47:38 | 11/06/2024 13:57:02 | IP effective | non |
| `82:B1:82:5C:17:AC` | 57bfdd94-60cf-4bf0-87b0-0624b3f3f22d | 21/09/2023 20:09:53 | 11/12/2023 10:17:35 | IP effective | non |
| `1C:90:FF:9D:B8:4A` | wlan0 | 15/11/2023 13:51:18 | 15/11/2023 13:51:18 | détection seulement | non |
| `CC:8C:BF:08:23:84` | wlan0 | 15/11/2023 14:19:31 | 15/11/2023 14:19:31 | détection seulement | non |
| `2C:C3:E6:98:A4:2F` | — | 02/12/2023 18:07:47 | 02/12/2023 18:07:47 | détection seulement | non |
| `36:D0:F6:73:99:C7` | Apple-Watch | 12/12/2023 01:31:31 | 14/12/2023 21:12:08 | IP effective | non |
| `1E:A6:37:ED:10:7D` | Apple-Watch | 14/12/2023 21:15:26 | 19/12/2023 17:24:27 | IP effective | non |
| `D2:2E:29:52:CB:BD` | 2d4183c8-3c55-4589-85e2-805498ce616e | 18/01/2024 19:15:56 | 11/06/2024 13:51:21 | IP effective | non |
| `4E:B5:4A:B0:3F:04` | — | 21/01/2024 13:20:29 | 21/01/2024 13:20:29 | détection seulement | oui |
| `70:70:AA:0D:EC:11` | android2-home | 21/01/2024 18:54:04 | 19/02/2024 17:49:14 | IP effective | non |
| `0E:A1:33:FB:02:46` | iPhone | 26/01/2024 19:48:37 | 26/01/2024 19:48:37 | détection seulement | non |
| `A6:14:3E:8A:34:ED` | 158742fd-de6e-43df-98be-e440d29c2673 | 04/03/2024 23:14:41 | 02/05/2024 13:00:02 | IP effective | oui |
| `16:E8:85:01:02:FD` | — | 02/05/2024 12:50:13 | 02/05/2024 12:50:13 | détection seulement | oui |
| `B2:D2:80:8B:78:FD` | 3f194c23-a33b-407a-b571-27f9475d7f83 | 25/05/2024 20:53:04 | 18/08/2024 14:44:12 | IP effective | non |
| `08:87:C7:76:C4:10` | iPhone | 11/06/2024 13:12:32 | 11/06/2024 14:00:33 | IP effective | non |
| `1A:4E:FD:7E:44:35` | 1f159da5-72f3-4ea3-995c-e2b6c48a7966 | 11/06/2024 13:33:43 | 11/06/2024 13:38:29 | IP effective | non |
| `CE:04:84:BC:D2:4D` | — | 11/06/2024 14:00:54 | 11/06/2024 14:25:49 | IP effective | oui |
| `0E:41:84:EF:66:27` | iPhone | 11/06/2024 14:27:30 | 11/06/2024 14:27:30 | détection seulement | non |
| `E0:A2:5A:0D:06:DF` | mxiang-camera-mwc10_miap06DE | 19/07/2024 21:02:44 | 19/07/2024 21:02:44 | détection seulement | non |
| `E0:A2:5A:0A:A3:F7` | — | 19/07/2024 21:02:47 | 19/07/2024 21:02:47 | détection seulement | oui |
| `98:AA:FC:13:18:93` | STARVOX-98AAFC131893 | 19/07/2024 22:16:11 | 19/07/2024 22:16:11 | détection seulement | non |
| `96:8F:D6:BB:47:D7` | iPhone | 12/10/2024 23:15:06 | 12/10/2024 23:15:06 | détection seulement avant la limite | non |
| `EA:21:6C:F7:47:E7` | iPhone | 16/10/2024 00:20:00 | 17/10/2024 00:57:02 | IP effective | non |
| `AC:ED:5C:DA:47:74` | DESKTOP-ICPNCMD | 16/10/2024 21:27:48 | 16/10/2024 23:25:55 | IP effective | non |
| `9C:64:8B:0A:BD:0C` | iPhone | 17/10/2024 01:00:57 | 17/10/2024 03:43:56 | IP effective | non |
| `FE:AA:76:95:AC:29` | iPhone | 17/10/2024 03:45:44 | 17/10/2024 03:45:44 | détection seulement avant la limite | non |

---

## Résultats détaillés concernant les appareils définis précédemment comme "suspects"

### `E0:A2:5A:0A:A3:F7`

- `first_activity` : 19/07/2024 à 21:02:47 CEST ;
- constructeur : Shanghai Mo xiang Network Technology CO.,ltd ;
- aucune entrée `l3connectivities` ;
- conclusion : détection par la Freebox confirmée, sans preuve IP conservée. Cela concorde avec `freebox.md`.

### `50:E0:85:63:41:5B` — `LAPTOP-RMCOB2VU`

- nom exact renvoyé par l'API : `LAPTOP-RMCOB2VU`, alors que `freebox.md` écrit `LAPTOP-RMC0B2VU` ;
- constructeur : Intel Corporate ;
- `first_activity` de la fiche : 23/07/2024 à 15:37:02 CEST ;
- sept connectivités conservées ;
- trace antérieure incohérente avec `first_activity` : `fe80::a1b7:11f0:16bd:b6d`, dernière activité le 13/01/2023 à 10:15:23 CET ;
- les six autres adresses conservées ont leur dernière activité le 03/09/2026 : IPv4 `192.168.1.194`, IPv6 link-local `fe80::7517:2b03:9301:5e7e`, IPv6 publiques `2a01:e0a:c88:900:1779:93d3:f657:a8e6`, `2a0d:e487:15ef:3ee4:356c:a2a7:2623:3fe9`, `2a0d:e487:15ef:3ee4:9481:22e2:6cb5:46ec` et `2a01:e0a:c88:900:71a2:a4f5:4a6b:622f` ;
- conclusion : la connexion IP historique antérieure à juillet 2024 est confirmée. Le champ `first_activity` n'est pas une première apparition historique fiable. Cela confirme l'analyse de `freebox.md`.

### `A6:14:3E:8A:34:ED` — `158742fd-de6e-43df-98be-e440d29c2673`

- adresse MAC localement administrée ;
- `first_activity` : 04/03/2024 à 23:14:41 CET ;
- dix connectivités conservées ;
- avant la date limite : IPv4 `192.168.1.100`, dernière activité le 02/05/2024 à 13:00:02 CEST ;
- après la date limite : IPv4 `192.168.1.57`, deux IPv6 publiques et deux link-local en novembre 2024, une IPv6 publique en décembre 2024, puis trois IPv6 en septembre 2025 ;
- l'adresse supplémentaire non retranscrite dans `freebox.md` est `2a01:e0a:c88:900:506:d96e:b844:b892`, dernière activité le 14/09/2025 à 18:46:05 CEST ;
- conclusion : présence IP certaine le 2 mai 2024, puis à partir du 4 novembre 2024. Aucune entrée conservée n'est datée du 15 au 28 octobre 2024, mais l'API n'étant pas un journal exhaustif, cette absence ne permet pas d'exclure une présence durant cet intervalle. L'analyse de fond de `freebox.md` est confirmée.

### `CE:04:84:BC:D2:4D`

- adresse MAC localement administrée ;
- `first_activity` : 11/06/2024 à 14:00:54 CEST ;
- cinq connectivités conservées : IPv4 `192.168.1.98`, IPv6 link-local `fe80::148e:7f35:4ff7:c240` et IPv6 publiques `2a01:e0a:c88:900:4c20:2070:917:73b2`, `2a01:e0a:c88:900:1d53:85bc:6259:483c`, `2a01:e0a:c88:900:4815:28ed:effd:6392` ;
- dernière activité : 11/06/2024 à 14:25:49 CEST ;
- conclusion : connectivité IP effective pendant environ vingt-cinq minutes, comme indiqué dans `freebox.md`.

### `16:E8:85:01:02:FD`

- adresse MAC localement administrée ;
- `first_activity` : 02/05/2024 à 12:50:13 CEST ;
- aucune entrée `l3connectivities` ;
- conclusion : détection confirmée, sans preuve IP conservée. Cela concorde avec `freebox.md`.

### `4E:B5:4A:B0:3F:04`

- adresse MAC localement administrée ;
- `first_activity` : 21/01/2024 à 13:20:29 CET ;
- aucune entrée `l3connectivities` ;
- conclusion : détection confirmée, sans preuve IP conservée. Cela concorde avec `freebox.md` sur le fond.

### `DE:98:33:8D:2C:A2`

- adresse MAC localement administrée ;
- `first_activity` : 16/08/2023 à 17:05:18 CEST ;
- neuf connectivités conservées : IPv4 `192.168.1.75`, quatre IPv6 link-local et quatre IPv6 publiques ;
- activités conservées les 21 et 25 septembre 2023, le 18 octobre 2023 et le 11 décembre 2023 ;
- dernière activité : 11/12/2023 à 10:19:39 CET ;
- conclusion : connexions IP historiques répétées confirmées. Aucune trace de 2024 n'est conservée pour cette fiche. L'analyse de `freebox.md` est confirmée.

### `E6:E1:90:ED:E4:94`

- adresse MAC localement administrée ;
- `first_activity` : 11/10/2022 à 16:24:30 CEST ;
- aucune entrée `l3connectivities` ;
- conclusion : détection confirmée, sans preuve IP conservée. Cela concorde avec `freebox.md`.

### `56:96:03:FB:28:58`

- adresse MAC localement administrée ;
- `first_activity` : 07/07/2022 à 19:00:35 CEST ;
- deux connectivités IPv6 : `2a01:e0a:2ac:31c0:51c:d253:9380:753e` et `fe80::47:d6f:9c8:cab6` ;
- dernière activité : 07/07/2022 à 19:21:38 CEST ;
- conclusion : connectivité IP effective pendant environ vingt et une minutes, comme indiqué dans `freebox.md`.

### `F2:D1:B4:69:51:D8`

- adresse MAC localement administrée ;
- `first_activity` vaut `0`, malgré neuf connectivités conservées ;
- IPv4 `192.168.1.131`, quatre IPv6 link-local et quatre IPv6 publiques ;
- activités conservées entre le 15/10/2022 à 05:52:22 CEST et le 01/02/2023 à 04:30:42 CET ;
- conclusion : la connectivité IP effective est confirmée et démontre que `first_activity = 0` ne signifie pas une absence de connexion. L'analyse de `freebox.md` est confirmée.

### `B6:BD:59:D2:25:62`

- adresse MAC localement administrée ;
- `first_activity` vaut `0`, malgré huit connectivités conservées ;
- quatre IPv6 link-local et quatre IPv6 publiques ;
- activités conservées entre le 05/04/2022 à 21:37:27 CEST et le 02/05/2022 à 21:19:52 CEST ;
- conclusion : la connectivité IP effective est confirmée. L'analyse de `freebox.md` est confirmée.

---

## Écarts d'horodatage avec `freebox.md`

Les horodatages API bruts sont des secondes Unix. Leur conversion avec `Europe/Paris` concorde avec `freebox.md` pour les dates en heure d'été. Pour plusieurs dates d'hiver, `freebox.md` affiche une heure de plus que la conversion historique correcte, comme si UTC+2 avait été appliqué toute l'année. Exemples :

| Événement | API convertie Europe/Paris | `freebox.md` |
|---|---:|---:|
| `50:E0:85:63:41:5B`, IPv6 link-local | 13/01/2023 10:15:23 CET | 13/01/2023 11:15:23 |
| `4E:B5:4A:B0:3F:04`, `first_activity` | 21/01/2024 13:20:29 CET | 21/01/2024 14:20:29 |
| `F2:D1:B4:69:51:D8`, dernière activité | 01/02/2023 04:30:42 CET | 01/02/2023 05:30:42 |
| `DE:98:33:8D:2C:A2`, dernière activité | 11/12/2023 10:19:39 CET | 11/12/2023 11:19:39 |

Une autre divergence concerne `A6:14:3E:8A:34:ED` : l'API donne le 04/03/2024 à 23:14:41 CET pour `first_activity`, tandis que `freebox.md` indique le 04/03/2024 à 00:14:41. Cette différence ne peut pas être expliquée par le seul passage CET/CEST et doit être traitée comme une divergence de retranscription ou d'affichage à vérifier sur la capture source.

Ces écarts n'affectent pas la conclusion sur l'antériorité au 29 octobre 2024, mais les horodatages Unix bruts conservés dans les fichiers JSON doivent être privilégiés pour toute corrélation précise.

---

## Appareils d'octobre 2024 absents de la liste suspecte

Cinq fiches non incluses dans les onze appareils suspects ont une première trace entre le 12 et le 17 octobre 2024. Trois possèdent une connectivité IP explicitement datée avant la limite ; pour deux autres, la première détection est antérieure à la limite mais les connectivités actuellement conservées ont des dates ultérieures.

| Adresse MAC | Nom | Première trace | Résultat utile | Appréciation |
|---|---|---:|---|---|
| `96:8F:D6:BB:47:D7` | iPhone | 12/10/2024 23:15:06 CEST | MAC locale ; les huit IPv6 conservées ont leurs dernières activités en novembre/décembre 2024 | Détection certaine avant la limite, mais pas d'horodatage IP d'octobre encore conservé |
| `EA:21:6C:F7:47:E7` | iPhone | 16/10/2024 00:20:00 CEST | IPv4 `192.168.1.3` et cinq IPv6 ; dernière activité le 17/10/2024 à 00:57:02 CEST | Connexion IP effective pendant la période |
| `AC:ED:5C:DA:47:74` | DESKTOP-ICPNCMD | 16/10/2024 21:27:48 CEST | Intel Corporate ; IPv6 datées du 16/10/2024 ; la fiche est encore utilisée en 2026 avec IPv4 `192.168.1.41` | Connexion IP effective pendant la période ; pourrait correspondre à un ordinateur connu, à confirmer par son adresse MAC |
| `9C:64:8B:0A:BD:0C` | iPhone | 17/10/2024 01:00:57 CEST | Apple, Inc. ; IPv4 `192.168.1.55` et cinq IPv6 ; dernière activité le 17/10/2024 à 03:43:56 CEST | Connexion IP effective pendant la période |
| `FE:AA:76:95:AC:29` | iPhone | 17/10/2024 03:45:44 CEST | MAC locale ; les huit IPv6 conservées ont leurs dernières activités en novembre/décembre 2024 | Détection certaine avant la limite, mais pas d'horodatage IP d'octobre encore conservé |

Ces cinq fiches sont plus directement proches de la période d'octobre 2024 que les onze fiches initialement qualifiées de suspectes. Elles ne constituent pas pour autant une preuve d'intrusion : plusieurs peuvent correspondre aux iPhone de Mme Sadedine ou de visiteurs, et `DESKTOP-ICPNCMD` peut correspondre à l'un des ordinateurs connus. Leur identification devrait être prioritaire par comparaison avec les adresses MAC des appareils physiques et, si disponible, avec tout inventaire ou sauvegarde datant de 2024.

---

## Comparaison et conclusions

1. **Les onze appareils précédemment identifiés comme "suspects" figurent tous dans l'inventaire antérieur au 29 octobre 2024.** Sept disposent d'une connectivité IP historique conservée : `50:E0:85:63:41:5B`, `A6:14:3E:8A:34:ED`, `CE:04:84:BC:D2:4D`, `DE:98:33:8D:2C:A2`, `56:96:03:FB:28:58`, `F2:D1:B4:69:51:D8` et `B6:BD:59:D2:25:62`. Quatre ne disposent que d'une trace de détection : `E0:A2:5A:0A:A3:F7`, `16:E8:85:01:02:FD`, `4E:B5:4A:B0:3F:04` et `E6:E1:90:ED:E4:94`.

2. **L'API confirme l'essentiel des conclusions déjà rédigées**, notamment le caractère non exhaustif de `first_activity`, la présence de traces IP malgré `first_activity = 0`, et l'impossibilité d'attribuer un propriétaire à partir d'une adresse MAC localement administrée.

3. **Aucun des onze appareils suspects ne possède une entrée conservée explicitement datée du 15 au 28 octobre 2024.** Pour `A6:14:3E:8A:34:ED`, une activité est conservée le 2 mai 2024 puis à partir du 4 novembre 2024. Cette absence d'entrée dans l'intervalle ne permet pas d'exclure une connexion, car l'API ne fournit pas un journal exhaustif de chaque association.

4. **Cinq autres appareils, non classés suspects dans `freebox.md`, apparaissent entre le 12 et le 17 octobre 2024.** Trois ont une preuve IP conservée pendant cette période. Ils doivent être rapprochés en priorité de l'inventaire matériel connu de Mme Sadedine.

5. **Aucune donnée collectée ne permet, à elle seule, de caractériser une intrusion ou une activité malveillante.** Les traces établissent des présences ou détections réseau, mais pas l'identité de l'utilisateur, l'action effectuée ni l'autorisation ou non de la connexion.

6. **La précision temporelle doit reposer sur les valeurs Unix brutes.** Les divergences d'une heure observées sur les dates d'hiver et la divergence plus importante du 4 mars 2024 justifient de ne pas reprendre sans contrôle les heures affichées ou retranscrites dans l'interface.

---

## Fichiers de preuve conservés

- `freebox/preuves-json/lan-browser-pub-raw.json` : réponse brute de l'inventaire des 74 fiches ;
- `freebox/preuves-json/suspect-*.json` : onze réponses brutes individuelles, une par appareil suspect.

Ces fichiers ne contiennent pas le jeton de session utilisé pour les requêtes.

---

## Analyse complémentaire de l'activité potentiellement suspecte

### Objet de l'analyse

Cette analyse complémentaire cherche à déterminer si l'un des onze appareils initialement qualifiés de suspects, ou l'un des cinq appareils apparus entre le 12 et le 17 octobre 2024, a laissé une trace compatible avec :

- un accès non autorisé à l'administration de la Freebox ;
- une modification de sa configuration ;
- l'ouverture d'un accès entrant, d'une redirection de port, d'une DMZ ou d'un tunnel VPN ;
- l'utilisation du gestionnaire de téléchargements ou du mécanisme d'envoi de fichiers de la Freebox ;
- un transfert de données anormal ou une exfiltration de données ;
- toute autre activité pouvant évoquer un piratage.

Les seize appareils examinés sont :

- les onze appareils suspects déjà étudiés : `E0:A2:5A:0A:A3:F7`, `50:E0:85:63:41:5B`, `A6:14:3E:8A:34:ED`, `CE:04:84:BC:D2:4D`, `16:E8:85:01:02:FD`, `4E:B5:4A:B0:3F:04`, `DE:98:33:8D:2C:A2`, `E6:E1:90:ED:E4:94`, `56:96:03:FB:28:58`, `F2:D1:B4:69:51:D8` et `B6:BD:59:D2:25:62` ;
- les cinq appareils apparus en octobre 2024 : `96:8F:D6:BB:47:D7`, `EA:21:6C:F7:47:E7`, `AC:ED:5C:DA:47:74`, `9C:64:8B:0A:BD:0C` et `FE:AA:76:95:AC:29`.

### Limites techniques déterminantes

La [documentation officielle de l'API LAN Freebox](https://dev.freebox.fr/sdk/os/lan/) montre que la fiche d'un appareil contient essentiellement son identité réseau, ses noms, ses adresses IP, son état courant et les derniers horodatages d'activité ou de joignabilité. Elle ne contient pas :

- la liste des sites ou services contactés ;
- les ports TCP ou UDP utilisés par l'appareil ;
- les flux entrants ou sortants ;
- le volume historique transmis par appareil ;
- les fichiers consultés sur un partage SMB ;
- les commandes d'administration exécutées ;
- l'identité de la personne utilisant l'appareil.

La [documentation Wi-Fi officielle](https://dev.freebox.fr/sdk/os/wifi/) expose des compteurs `rx_bytes` et `tx_bytes` pour les stations actuellement conservées par un point d'accès. Ces compteurs décrivent une association Wi-Fi courante et ne constituent pas un historique par appareil remontant à 2022, 2023 ou 2024.

Les statistiques [RRD](https://dev.freebox.fr/sdk/os/rrd/) sont agrégées au niveau de la connexion, du switch ou de la Freebox. Même lorsqu'elles sont disponibles, elles ne permettent pas d'attribuer un volume à une adresse MAC déterminée. La tentative de lecture de la période du 12 au 29 octobre 2024 a en outre échoué avec `error_code: "db_error"`, ce qui indique que les données demandées ne sont plus lisibles dans la base RRD actuelle.

Enfin, l'API exposée ne fournit pas de journal d'audit historique reliant une modification de configuration à une adresse IP ou MAC locale. Il est donc possible de rechercher des traces positives conservées, mais pas de démontrer l'absence absolue d'une action ancienne qui n'aurait laissé aucune trace persistante.

### Requêtes complémentaires exécutées

Toutes les requêtes ont été effectuées séparément, en lecture seule, avec le même mécanisme d'authentification que celui décrit précédemment.

```bash
curl -sk "$BASE_URL/connection/logs/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-connection-logs.json
curl -sk "$BASE_URL/downloads/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-downloads.json
curl -sk "$BASE_URL/downloads/feeds/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-download-feeds.json
curl -sk "$BASE_URL/upload/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-uploads.json
curl -sk "$BASE_URL/fw/redir/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-port-forwarding.json
curl -sk "$BASE_URL/upnpigd/redir/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-upnp-redirections.json
curl -sk "$BASE_URL/fw/dmz/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-dmz.json
curl -sk "$BASE_URL/wifi/ap/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-wifi-aps.json
curl -sk "$BASE_URL/wifi/ap/0/stations/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-wifi-ap-0-stations.json
curl -sk "$BASE_URL/wifi/ap/10/stations/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-wifi-ap-10-stations.json
curl -sk "$BASE_URL/vpn_client/status" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-vpn-client-status.json
curl -sk "$BASE_URL/vpn_client/log" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-vpn-client-log.json
curl -sk "$BASE_URL/vpn_client/config/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-vpn-client-config.json
curl -sk "$BASE_URL/dhcp/static_lease/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-dhcp-static-leases-v2.json
curl -sk "$BASE_URL/dhcp/dynamic_lease/" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-dhcp-dynamic-leases.json
curl -sk "$BASE_URL/rrd/?db=net&date_start=1728684000&date_end=1730156400&precision=1" -H "X-Fbx-App-Auth: $SESSION_TOKEN" -o freebox/preuves-json/activity-rrd-net-2024-10-12_29-get.json
```

Deux routes essayées pour obtenir un historique des autorisations et sessions d'administration, `GET /login/authorize/` et `GET /login/session/`, ont retourné HTTP `404` avec `error_code: "invalid_request"`. Elles ne fournissent donc pas, sur cette version de la Freebox, une liste exploitable des anciennes sessions ou des modifications réalisées.

### Résultats par catégorie d'activité

#### Administration de la Freebox et modification de paramètres

Aucune réponse de l'API LAN ne relie l'un des seize appareils à une session Freebox OS, à une application autorisée ou à une modification de configuration.

L'ouverture d'une application API Freebox repose sur un jeton applicatif et, lors de la première association, sur une validation physique depuis le Freebox Server. Les fiches LAN des appareils ne contiennent toutefois aucun identifiant permettant de les relier à une application autorisée. Les constats antérieurs consignés dans `freebox.md` montraient trois applications autorisées, sans droit d'accès actif anormal au moment de l'examen. Ils ne permettent pas de reconstituer leurs droits en 2024.

**Conclusion limitée :** aucune trace positive ne montre qu'un des seize appareils a administré ou modifié la Freebox. En l'absence de journal d'audit historique, il n'est pas possible de démontrer qu'aucune modification ancienne n'a eu lieu, ni d'attribuer une éventuelle modification à une adresse MAC.

#### Redirections de ports, UPnP et DMZ

- `GET /fw/redir/` : aucune redirection manuelle retournée ;
- `GET /upnpigd/redir/` : aucune redirection UPnP retournée ;
- `GET /fw/dmz/` : `enabled: false` et aucune adresse IP de DMZ ;
- aucune des seize fiches ne porte de nom provenant d'une source `upnp` ; les seuls noms conservés proviennent de DHCP, mDNS ou WSD.

**Conclusion limitée :** aucun appareil suspect n'est actuellement ciblé par une redirection ou une DMZ, et aucune redirection UPnP active ne lui est attribuée. Ces endpoints décrivent l'état actuel et ne conservent pas l'historique des redirections supprimées ; ils ne permettent donc pas d'exclure une ouverture de port ancienne et temporaire.

#### VPN

- état du client VPN : `enabled: false` ;
- aucune configuration de client VPN retournée ;
- journal du client VPN vide ;
- le constat antérieur de `freebox.md` indiquait également que les serveurs VPN intégrés étaient désactivés.

**Conclusion limitée :** aucune trace conservée ne montre l'utilisation du client VPN intégré de la Freebox ou un tunnel VPN configuré par l'un des appareils. Cela n'exclut pas qu'un appareil ait utilisé son propre logiciel VPN, trafic qui ne serait pas détaillé dans l'inventaire LAN.

#### Téléchargements et envois de fichiers gérés par la Freebox

- `GET /downloads/` : réponse positive ne contenant aucune tâche ;
- `GET /downloads/feeds/` : aucun abonnement ou flux de téléchargement automatique ;
- `GET /upload/` : liste vide ;
- l'examen antérieur du disque de la Freebox n'avait trouvé que cinq enregistrements télévisés et leurs fichiers d'index.

**Conclusion limitée :** aucune tâche conservée n'indique qu'un appareil a utilisé le gestionnaire de téléchargements ou le mécanisme d'envoi de fichiers de la Freebox pour déposer ou récupérer des données. Ces résultats ne couvrent pas les téléchargements réalisés directement par un ordinateur ou un téléphone sur Internet, ni la lecture de fichiers via SMB.

#### Partage SMB et accès aux fichiers

Le partage SMB était activé sans authentification supplémentaire sur le réseau local au moment du constat décrit dans `freebox.md`. Un appareil déjà connecté au réseau local pouvait donc techniquement parcourir les fichiers partagés par la Freebox sans compte SMB distinct.

La Freebox ne fournit pas, dans les données collectées, de journal historique indiquant quelle adresse MAC ou IP a ouvert, lu ou copié un fichier par SMB. Aucun des fichiers disponibles ne peut donc établir ou exclure une consultation par l'un des seize appareils. Le contenu visible du disque était limité aux enregistrements TV déjà décrits ; aucun document personnel ou professionnel n'avait été relevé dans l'explorateur de la Freebox.

**Conclusion limitée :** la possibilité technique d'un accès local au partage existait, mais aucune trace ne montre qu'un appareil suspect a effectivement lu ou copié un fichier. Aucun élément conservé ne caractérise un siphonnage des fichiers de la Freebox.

#### Volumes réseau et exfiltration de données

La lecture RRD visant la période du 12 au 29 octobre 2024 a retourné :

```json
{
  "success": false,
  "error_code": "db_error",
  "msg": "Erreur lors de la récupération des statistiques : Erreur lors de la lecture de la base RRD"
}
```

Les deux points d'accès Wi-Fi actuels sont `0` — 2,4 GHz — et `10` — 5 GHz. Six stations étaient conservées sur le point d'accès 2,4 GHz et aucune sur le 5 GHz. Aucune des seize adresses MAC examinées ne figurait parmi ces stations. Les compteurs actuels ne peuvent donc pas être utilisés pour estimer leur trafic historique.

Les cinq baux DHCP dynamiques actuels et l'absence de bail statique ont également été vérifiés. Aucun des seize appareils ne possède actuellement de bail DHCP actif ou réservé.

**Conclusion limitée :** aucun volume anormal ne peut être attribué à l'un des seize appareils. Les données nécessaires pour quantifier leur trafic de 2022 à 2024 ne sont plus disponibles. Il est donc impossible de prouver un siphonnage de données, mais également impossible de l'exclure uniquement à partir de la Freebox.

#### Journal de la connexion Internet

Le journal `/connection/logs/` ne contient que deux événements : l'établissement du lien FTTH le 16 septembre 2026 à 09:48:05 et l'établissement de la connexion Internet publique le même jour à 09:48:26. Il ne contient aucun événement de 2024 et n'est de toute façon pas attribué aux appareils du réseau local.

### Situation actuelle des seize appareils

Au moment de la collecte de l'inventaire :

- les seize fiches avaient `active: false` ;
- les seize fiches avaient `reachable: false` ;
- aucune n'avait de bail DHCP dynamique actif ;
- aucune n'était présente dans les listes de stations Wi-Fi actuelles ;
- aucune ne possédait de réservation DHCP statique ;
- aucun nom principal n'avait été défini manuellement dans la fiche Freebox (`primary_name_manual: false`).

Il n'existe donc aucun signe d'activité actuelle de ces appareils sur le réseau au moment de cette analyse.

### Analyse individuelle des onze appareils initialement suspects

| Appareil | Activité conservée | Recherche d'activité suspecte | Appréciation |
|---|---|---|---|
| `E0:A2:5A:0A:A3:F7` | Détection le 19/07/2024 ; aucune IP | Aucun flux, volume, service ou accès d'administration conservé | Aucun indice positif ; l'absence de connectivité IP conservée empêche toute analyse d'usage |
| `50:E0:85:63:41:5B` — LAPTOP-RMCOB2VU | Une IPv6 en janvier 2023 ; nouvelles adresses en septembre 2026 | Aucun événement attribué entre ces périodes ; aucune redirection, tâche ou session reliée | Profil compatible avec un ordinateur revenant sur le réseau ; aucune activité malveillante démontrée |
| `A6:14:3E:8A:34:ED` — UUID mDNS | IPv4 le 02/05/2024, puis activités à partir du 04/11/2024 et en 2025 | Aucun événement conservé du 15 au 28/10/2024 ; aucun volume ou service détaillé | Appareil non identifié et récurrent, à identifier physiquement ; aucune trace technique de piratage |
| `CE:04:84:BC:D2:4D` | Connexion IP d'environ vingt-cinq minutes le 11/06/2024 | Aucune activité ultérieure, redirection ou tâche attribuée | Visite brève compatible avec un appareil de passage ; aucune action suspecte démontrée |
| `16:E8:85:01:02:FD` | Détection le 02/05/2024 ; aucune IP | Aucun usage réseau observable | Aucun indice positif ; analyse d'activité impossible faute de connectivité conservée |
| `4E:B5:4A:B0:3F:04` | Détection le 21/01/2024 ; aucune IP | Aucun usage réseau observable | Aucun indice positif ; analyse d'activité impossible faute de connectivité conservée |
| `DE:98:33:8D:2C:A2` | Connexions répétées de septembre à décembre 2023 | Aucun événement conservé en 2024 ; aucun service, volume ou transfert attribué | Présence répétée mais ancienne ; aucune trace de piratage ou d'administration de la Freebox |
| `E6:E1:90:ED:E4:94` | Détection le 11/10/2022 ; aucune IP | Aucun usage réseau observable | Aucun indice positif ; analyse d'activité impossible faute de connectivité conservée |
| `56:96:03:FB:28:58` | Deux IPv6 pendant environ vingt et une minutes le 07/07/2022 | Aucun autre événement attribué | Connexion brève ; aucune activité suspecte démontrée |
| `F2:D1:B4:69:51:D8` | Connexions IPv4/IPv6 d'octobre 2022 à février 2023 | Aucun événement conservé après février 2023 | Présence récurrente ancienne ; aucune trace d'accès sensible, de modification ou d'exfiltration |
| `B6:BD:59:D2:25:62` | Connexions IPv6 d'avril à mai 2022 | Aucun événement conservé après mai 2022 | Présence récurrente ancienne ; aucune trace d'accès sensible, de modification ou d'exfiltration |

### Analyse individuelle des cinq appareils d'octobre 2024

| Appareil | Activité conservée | Recherche d'activité suspecte | Appréciation |
|---|---|---|---|
| `96:8F:D6:BB:47:D7` — iPhone | Première détection le 12/10/2024 ; dernières activités IP conservées en novembre et décembre 2024 | Pas de connectivité IP d'octobre encore datée ; aucune tâche ou ouverture attribuée | Présence avant la période confirmée, usage précis indéterminable ; aucune action malveillante démontrée |
| `EA:21:6C:F7:47:E7` — iPhone | Du 16/10/2024 à 00:20:00 au 17/10/2024 à 00:57:02 ; IPv4 `192.168.1.3` et cinq IPv6 | Connexion IP effective, mais aucun port, volume, fichier ou accès d'administration journalisé | Présence réseau certaine pendant environ 24 h 37 ; aucune preuve d'activité sensible ou de piratage |
| `AC:ED:5C:DA:47:74` — DESKTOP-ICPNCMD | Du 16/10/2024 à 21:27:48 à 23:25:55 ; plusieurs IPv6 ; nouvelle activité en 2026 | Connexion IP effective ; aucune redirection, tâche, VPN ou session d'administration attribuée | Appareil à identifier en priorité, possiblement l'un des ordinateurs connus ; aucune activité malveillante démontrée |
| `9C:64:8B:0A:BD:0C` — iPhone Apple | Du 17/10/2024 à 01:00:57 à 03:43:56 ; IPv4 `192.168.1.55` et cinq IPv6 | Connexion IP effective, sans détail des flux ou services utilisés | Présence réseau certaine pendant environ 2 h 43 ; aucune preuve d'accès sensible ou d'exfiltration |
| `FE:AA:76:95:AC:29` — iPhone | Première détection le 17/10/2024 à 03:45:44 ; activités IP conservées en novembre/décembre 2024 | Pas de connectivité IP d'octobre encore datée ; aucune tâche ou ouverture attribuée | Usage précis indéterminable ; aucune action malveillante démontrée |

### Succession des identités iPhone dans la nuit du 16 au 17 octobre 2024

Une séquence temporelle mérite d'être signalée :

1. `EA:21:6C:F7:47:E7` cesse d'être actif le 17/10/2024 à 00:57:02 ;
2. `9C:64:8B:0A:BD:0C` apparaît à 01:00:57, soit 3 minutes et 55 secondes plus tard ;
3. `9C:64:8B:0A:BD:0C` cesse d'être actif à 03:43:56 ;
4. `FE:AA:76:95:AC:29` apparaît à 03:45:44, soit 1 minute et 48 secondes plus tard.

Les trois fiches portent le nom `iPhone`. `EA:21:6C:F7:47:E7` et `FE:AA:76:95:AC:29` sont des adresses MAC localement administrées, compatibles avec des adresses Wi-Fi privées. `9C:64:8B:0A:BD:0C` est attribuée à Apple et n'est pas localement administrée.

Cette succession peut correspondre à plusieurs iPhone distincts, ou éventuellement à un changement de mode d'adresse privée d'un même appareil. Les données Freebox ne permettent pas de fusionner ces identités ni d'établir qu'elles appartiennent à la même personne. La proximité temporelle constitue un point à rapprocher des appareils physiques et des témoignages, mais **elle ne constitue pas une preuve de piratage**.

---

# Conclusion générale sur une éventuelle activité de piratage

**Aucune trace positive conservée dans la Freebox ne démontre qu'un des seize appareils a :**

- ouvert une session d'administration Freebox OS ;
- modifié un paramètre de la Freebox ;
- créé une redirection de port ou une DMZ ;
- utilisé le client VPN intégré ;
- lancé une tâche de téléchargement ou d'envoi de fichier via la Freebox ;
- accédé à un fichier précis du partage SMB ;
- transmis un volume de données anormal ;
- exfiltré ou « siphonné » des données.

**Il n'est donc pas possible, sur la base des données disponibles, de qualifier l'activité de l'un de ces appareils de piratage.**

**Cette conclusion ne signifie toutefois pas qu'une activité ancienne non autorisée est techniquement exclue. Les données manquantes sont précisément celles qui seraient nécessaires pour l'établir: journal d'audit des modifications, historique des sessions d'administration, journal des accès SMB, historique des flux par appareil et compteurs de trafic par adresse MAC. La Freebox n'a pas conservé ou n'expose pas ces informations pour la période examinée.**

> Les démarches les plus utiles pour poursuivre l'attribution seraient :
> 
> 1. relever les adresses MAC matérielles et privées des iPhone, ordinateurs et appareils connus de Mme Sadedine ;
> 2. identifier en priorité `DESKTOP-ICPNCMD` et les trois identités iPhone successives de la nuit du 16 au 17 octobre 2024 ;
> 3. rechercher sur les ordinateurs concernés les journaux Windows, historiques Wi-Fi, historiques de navigateur, traces SMB et événements de connexion de la période ;
> 4. rechercher, si elles existent, des sauvegardes de configuration Freebox ou des captures d'écran contemporaines d'octobre 2024 ;
> 5. corréler les horaires avec les présences physiques connues au domicile.

### Fichiers bruts complémentaires

Les réponses complémentaires sont conservées dans les fichiers `freebox/preuves-json/activity-*.json`. Elles ne contiennent pas le jeton de session. Les fichiers les plus directement utiles sont :

- `freebox/preuves-json/activity-connection-logs.json` ;
- `freebox/preuves-json/activity-downloads.json` et `freebox/preuves-json/activity-download-feeds.json` ;
- `freebox/preuves-json/activity-uploads.json` ;
- `freebox/preuves-json/activity-port-forwarding.json` ;
- `freebox/preuves-json/activity-upnp-redirections.json` ;
- `freebox/preuves-json/activity-dmz.json` ;
- `freebox/preuves-json/activity-wifi-ap-0-stations.json` et `freebox/preuves-json/activity-wifi-ap-10-stations.json` ;
- `freebox/preuves-json/activity-vpn-client-status.json`, `freebox/preuves-json/activity-vpn-client-config.json` et `freebox/preuves-json/activity-vpn-client-log.json` ;
- `freebox/preuves-json/activity-dhcp-static-leases-v2.json` et `freebox/preuves-json/activity-dhcp-dynamic-leases.json` ;
- `freebox/preuves-json/activity-rrd-net-2024-10-12_29-get.json`.
