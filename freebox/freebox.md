# Fiche mémo – Réseau, Box et analyse forensic

## 1. LAN

**LAN = Local Area Network**

C’est le réseau local situé derrière la box.

Exemple :

```text
Internet
   |
Freebox
   |
   +-- PC
   +-- iPhone
   +-- Caméra
   +-- Alarme
```

Dans le cas d’une Freebox, les appareils utilisant des adresses comme :

```text
192.168.1.18
192.168.1.135
192.168.1.169
```

font partie du **LAN**.

Une adresse `192.168.x.x` est une adresse IP privée : elle n’est normalement pas directement accessible depuis Internet.

### Commandes utiles

Voir les interfaces réseau et leurs adresses :

**Linux :**

```bash
ip addr
```

Version courte :

```bash
ip -br addr
```

**macOS :**

```bash
ifconfig
```

Afficher uniquement les adresses IPv4 :

```bash
ifconfig | grep "inet "
```

Voir la table des voisins connus sur le LAN :

```bash
arp -a
```

Sous Linux :

```bash
ip neigh
```

---

## 2. WAN

**WAN = Wide Area Network**

Dans ce contexte, le WAN correspond essentiellement à la connexion entre la Freebox et Internet.

La Freebox possède donc :

* une adresse côté LAN ;
* une adresse IP publique côté WAN.

L’adresse publique permet à la box de communiquer avec Internet.

### Commandes utiles

Voir son IP publique :

```bash
curl ifconfig.me
```

ou :

```bash
curl https://api.ipify.org
```

Ajouter un retour à la ligne :

```bash
curl -s https://api.ipify.org ; echo
```

Attention : cette commande indique l’adresse IP publique vue depuis Internet, pas l’adresse IP locale de la machine.

---

## 3. Adresse IP

Une adresse IP identifie un équipement sur un réseau.

Exemple :

```text
192.168.1.135
```

Sur un réseau domestique, les équipements utilisent généralement des adresses privées.

Une adresse IP locale peut changer au cours du temps selon la configuration DHCP.

Il ne faut donc pas considérer une adresse IP seule comme une identité permanente de l’appareil.

### Commandes utiles

Afficher les IP locales sous Linux :

```bash
ip addr
```

ou :

```bash
hostname -I
```

Sous macOS :

```bash
ipconfig getifaddr en0
```

`en0` correspond souvent au Wi-Fi, mais cela dépend de la machine.

Lister les interfaces :

```bash
networksetup -listallhardwareports
```

Tester si une adresse répond :

```bash
ping 192.168.1.135
```

Limiter à quelques paquets :

```bash
ping -c 4 192.168.1.135
```

---

## 4. Adresse MAC

Une **adresse MAC** identifie l’interface réseau d’un appareil.

Exemple :

```text
E0:A2:5A:0D:06:DF
```

Elle est particulièrement utile pour suivre un appareil sur un réseau local.

Une adresse MAC peut parfois permettre d’identifier le constructeur grâce à son préfixe.

Attention : les smartphones modernes peuvent utiliser des **adresses MAC aléatoires ou privées**, notamment en Wi-Fi.

### Commandes utiles

Voir sa propre adresse MAC sous Linux :

```bash
ip link
```

Sous macOS :

```bash
ifconfig en0
```

Chercher la ligne :

```text
ether aa:bb:cc:dd:ee:ff
```

Afficher les MAC connues sur le LAN :

```bash
arp -a
```

ou sous Linux :

```bash
ip neigh
```

---

## 5. DHCP

**DHCP = Dynamic Host Configuration Protocol**

Le DHCP permet à la Freebox d’attribuer automatiquement une adresse IP aux appareils.

Exemple :

```text
iPhone
MAC : D2:0E:25:1B:5B:B8

↓ DHCP

IP : 192.168.1.18
```

La box peut conserver des informations sur les anciens appareils auxquels elle a attribué une adresse.

### Commandes utiles

Sous Linux, voir les informations DHCP via NetworkManager :

```bash
nmcli device show
```

Filtrer :

```bash
nmcli device show | grep -i dhcp
```

Sous macOS :

```bash
ipconfig getpacket en0
```

Cette commande peut montrer notamment :

* serveur DHCP ;
* adresse attribuée ;
* routeur ;
* durée du bail ;
* DNS.

---

## 6. Bail DHCP

Un **bail DHCP** correspond à l’attribution temporaire d’une adresse IP à un appareil.

Exemple :

```text
MAC : AA:BB:CC:DD:EE:FF
IP : 192.168.1.42
```

Le bail a généralement une durée limitée et peut être renouvelé.

### Commandes utiles

Sous macOS :

```bash
ipconfig getpacket en0
```

Chercher notamment :

```text
lease_time
server_identifier
yiaddr
```

Sous Linux avec NetworkManager :

```bash
nmcli device show
```

Les anciens baux des autres appareils sont surtout à chercher dans l’interface de la box ou ses journaux.

---

## 7. Nom d’hôte / hostname

Un appareil peut transmettre un nom à la box.

Exemples :

```text
iPhone
wlan0
STARVOX-98AAFC131893
mxiang-camera-mwc10_miap06DE
```

Ce nom peut aider à identifier l’équipement, mais il ne constitue pas une preuve absolue.

### Commandes utiles

Voir le nom de sa machine :

```bash
hostname
```

Sous macOS :

```bash
scutil --get ComputerName
```

et :

```bash
scutil --get LocalHostName
```

Faire une résolution inverse d’une IP :

```bash
nslookup 192.168.1.135
```

ou :

```bash
host 192.168.1.135
```

Cela ne fonctionnera que si un nom est disponible.

---

## 8. Ethernet

Ethernet désigne la connexion réseau filaire.

Un appareil connecté par câble à la Freebox peut apparaître sous :

```text
Ethernet 1
Ethernet 2
Ethernet 3
Ethernet 4
```

### Commandes utiles

Sous Linux :

```bash
ip link
```

Voir l’état d’une interface :

```bash
ethtool eth0
```

Par exemple :

```text
Speed: 100Mb/s
Duplex: Full
Link detected: yes
```

Sous macOS :

```bash
ifconfig
```

Pour connaître les ports matériels :

```bash
networksetup -listallhardwareports
```

---

## 9. 100Base-TX

`100Base-TX` est une norme Ethernet.

Elle signifie que la liaison fonctionne à :

```text
100 Mbit/s
```

Par exemple :

```text
100BaseTxFd
```

signifie :

```text
100Base-TX
Full Duplex
```

Ce n’est **pas le nom de l’appareil**.

### Commandes utiles

Sous Linux :

```bash
ethtool eth0
```

Filtrer :

```bash
ethtool eth0 | grep -E "Speed|Duplex|Link"
```

---

## 10. Full Duplex

**Full Duplex** signifie que l’appareil peut envoyer et recevoir des données simultanément.

Exemple :

```text
100BaseTxFd
```

correspond à :

```text
100 Mbit/s – Full Duplex
```

### Commande utile

```bash
ethtool eth0
```

Chercher :

```text
Duplex: Full
```

---

## 11. Wi-Fi 2,4 GHz

Le Wi-Fi 2,4 GHz est une bande de fréquence très utilisée par :

* smartphones ;
* imprimantes ;
* caméras ;
* alarmes ;
* objets connectés ;
* équipements domotiques.

### Commandes utiles

Sur macOS, informations sur le Wi-Fi :

```bash
system_profiler SPAirPortDataType
```

Voir l’interface Wi-Fi :

```bash
networksetup -getairportnetwork en0
```

Selon les versions de macOS, les outils disponibles peuvent varier.

Sous Linux :

```bash
iw dev
```

ou :

```bash
nmcli dev wifi
```

---

## 12. Wi-Fi 5 GHz

Le Wi-Fi 5 GHz permet généralement :

* de meilleurs débits ;
* moins d’interférences ;
* une portée plus courte.

### Commandes utiles

Sous Linux :

```bash
nmcli dev wifi
```

La fréquence ou le canal permet de déterminer la bande utilisée.

Exemples approximatifs :

```text
2412 MHz → 2,4 GHz
5180 MHz → 5 GHz
```

---

## 13. SSID

Le **SSID** est le nom du réseau Wi-Fi.

Exemple :

```text
FREEBOX_SADEDINE
```

### Commandes utiles

Sous macOS :

```bash
networksetup -getairportnetwork en0
```

Sous Linux :

```bash
iwgetid
```

ou :

```bash
nmcli -t -f active,ssid dev wifi
```

---

## 14. Clé Wi-Fi

La clé Wi-Fi est le mot de passe permettant de rejoindre le réseau.

Elle protège normalement l’accès au LAN.

La sécurité dépend notamment du protocole utilisé :

```text
WPA2
WPA3
```

### Commandes utiles

Il n’est généralement pas utile d’afficher le mot de passe en clair lors d’une analyse.

En revanche, on peut inspecter la configuration de l’interface Wi-Fi :

```bash
nmcli connection show
```

Sous macOS, les mots de passe enregistrés peuvent être stockés dans le Trousseau d’accès.

---

## 15. WPA / WPA2 / WPA3

Ce sont des protocoles de sécurité Wi-Fi.

Du plus ancien au plus récent :

```text
WPA
WPA2
WPA3
```

WEP est obsolète.

### Commandes utiles

Sous Linux :

```bash
nmcli -f SSID,SECURITY dev wifi
```

Exemple :

```text
SSID             SECURITY
MonWifi          WPA2
AutreWifi        WPA2 WPA3
```

---

## 16. WPS

**WPS = Wi-Fi Protected Setup**

Le WPS permet de connecter facilement un appareil au Wi-Fi sans saisir manuellement le mot de passe.

Selon la configuration, le WPS peut représenter une surface d’attaque supplémentaire.

### Commandes utiles

Sur une Freebox, la vérification du WPS se fait surtout dans l’interface d’administration.

On peut toutefois rechercher les informations Wi-Fi disponibles sous Linux :

```bash
nmcli dev wifi list
```

Pour une analyse générale des capacités Wi-Fi :

```bash
iw list
```

La présence du WPS sur un point d’accès nécessite généralement des outils d’analyse Wi-Fi spécialisés.

---

## 17. Routeur

La Freebox agit notamment comme **routeur**.

Elle assure :

* le routage ;
* le NAT ;
* le DHCP ;
* certaines fonctions de pare-feu.

### Commandes utiles

Voir la table de routage :

**Linux :**

```bash
ip route
```

**macOS :**

```bash
netstat -rn
```

ou :

```bash
route -n get default
```

---

## 18. NAT

**NAT = Network Address Translation**

Le NAT permet à plusieurs appareils privés d’utiliser une seule adresse IP publique.

```text
PC 192.168.1.10 ─┐
iPhone .1.20     ├── Freebox ── IP publique ── Internet
Caméra .1.30     ┘
```

### Commandes utiles

Comparer l’IP locale :

```bash
ipconfig getifaddr en0
```

avec l’IP publique :

```bash
curl -s https://api.ipify.org ; echo
```

Si les deux sont différentes, la machine est derrière une forme de NAT ou de routage intermédiaire.

---

## 19. Port réseau

Un port permet d’identifier un service réseau particulier.

Exemples :

```text
21     FTP
22     SSH
53     DNS
80     HTTP
443    HTTPS
3389   RDP
```

### Commandes utiles

Voir les ports ouverts localement :

**Linux :**

```bash
ss -lntup
```

Sous macOS :

```bash
lsof -i -P -n
```

Voir uniquement les services en écoute :

```bash
lsof -i -P -n | grep LISTEN
```

Tester un port sur une machine :

```bash
nc -vz 192.168.1.135 80
```

Exemple :

```bash
nc -vz 192.168.1.135 443
```

---

## 20. Redirection de port

Une **redirection de port** permet de rendre un service du LAN accessible depuis Internet.

Exemple :

```text
IP publique:8080
        ↓
192.168.1.135:80
```

### Commandes utiles

Les redirections de ports sont surtout à vérifier dans Freebox OS.

Pour vérifier localement qu’un service écoute :

```bash
lsof -i -P -n | grep LISTEN
```

ou :

```bash
ss -lnt
```

Une écoute locale ne signifie pas automatiquement que le service est exposé sur Internet.

---

## 21. UPnP

**UPnP = Universal Plug and Play**

UPnP permet à certains logiciels et appareils de demander automatiquement des ouvertures de ports.

### Commandes utiles

Sous Linux, si `miniupnpc` est installé :

```bash
upnpc -l
```

Sur macOS avec Homebrew :

```bash
brew install miniupnpc
```

Puis :

```bash
upnpc -l
```

Cela permet de lister certaines redirections UPnP visibles sur le routeur.

---

## 22. FTP

**FTP = File Transfer Protocol**

FTP permet de transférer des fichiers.

Port classique :

```text
21
```

### Commandes utiles

Tester si un serveur FTP répond :

```bash
nc -vz 192.168.1.254 21
```

Utiliser le client FTP si installé :

```bash
ftp 192.168.1.254
```

Scanner spécifiquement le port :

```bash
nmap -p 21 192.168.1.254
```

---

## 23. FTPS / SFTP

### FTPS

FTP protégé par TLS.

### SFTP

Transfert de fichiers via SSH.

SFTP n’est pas du FTP.

### Commandes utiles

Connexion SFTP :

```bash
sftp utilisateur@192.168.1.10
```

Tester SSH :

```bash
ssh utilisateur@192.168.1.10
```

Tester le port :

```bash
nc -vz 192.168.1.10 22
```

---

## 24. Accès distant

L’accès distant permet d’administrer un équipement depuis Internet.

Lors d’une analyse, il faut vérifier :

* activation ;
* port ;
* authentification ;
* services exposés ;
* restrictions éventuelles.

### Commandes utiles

Voir les services écoutant localement :

```bash
lsof -i -P -n | grep LISTEN
```

Sous Linux :

```bash
ss -lntup
```

Vérifier l’IP publique :

```bash
curl -s https://api.ipify.org ; echo
```

---

## 25. Freebox OS

Freebox OS est l’interface d’administration de la Freebox.

Elle permet notamment de consulter :

* les équipements ;
* DHCP ;
* Wi-Fi ;
* redirections ;
* disques ;
* téléchargements ;
* historique ;
* accès distant.

### Commandes utiles

Tester la présence d’une interface Web :

```bash
curl -I http://mafreebox.freebox.fr
```

ou :

```bash
curl -I http://192.168.1.254
```

Tester HTTPS :

```bash
curl -k -I https://mafreebox.freebox.fr
```

Afficher la résolution du nom :

```bash
ping mafreebox.freebox.fr
```

---

## 26. DNS

**DNS = Domain Name System**

Le DNS traduit un nom :

```text
example.com
```

en adresse IP.

### Commandes utiles

Résoudre un domaine :

```bash
dig example.com
```

ou :

```bash
nslookup example.com
```

Afficher uniquement l’IP :

```bash
dig +short example.com
```

Voir quels DNS sont utilisés sous macOS :

```bash
scutil --dns
```

Sous Linux :

```bash
resolvectl status
```

---

## 27. Passerelle / Gateway

La passerelle est l’équipement utilisé pour sortir du réseau local.

Dans un réseau domestique, il s’agit généralement de la box.

### Commandes utiles

Sous macOS :

```bash
route -n get default
```

Chercher :

```text
gateway: 192.168.1.254
```

Sous Linux :

```bash
ip route
```

Exemple :

```text
default via 192.168.1.254 dev eth0
```

---

## 28. Masque de sous-réseau

Le masque permet de déterminer quelles adresses appartiennent au même réseau.

Exemple :

```text
192.168.1.0/24
```

### Commandes utiles

Sous Linux :

```bash
ip addr
```

Exemple :

```text
inet 192.168.1.20/24
```

Sous macOS :

```bash
ifconfig
```

On peut voir par exemple :

```text
netmask 0xffffff00
```

qui correspond à :

```text
255.255.255.0
```

---

## 29. Switch

Un switch permet de relier plusieurs équipements Ethernet entre eux.

Un seul port de la Freebox peut donc éventuellement desservir plusieurs appareils si un switch est branché derrière.

### Commandes utiles

Il n’existe pas de commande universelle permettant de détecter automatiquement un switch non administrable.

On peut cependant inspecter les voisins :

```bash
arp -a
```

ou :

```bash
ip neigh
```

et comparer avec les ports physiques connus.

---

## 30. Caméra IP

Une caméra IP est une caméra connectée au réseau.

Elle peut être :

* Wi-Fi ;
* Ethernet ;
* locale ;
* cloud.

### Commandes utiles

Tester si la caméra répond :

```bash
ping 192.168.1.135
```

Voir quelques ports classiques :

```bash
nmap -p 80,443,554,8000,8080 192.168.1.135
```

Le port `554` est souvent associé à RTSP, mais sa présence ne prouve pas forcément qu’il s’agit d’une caméra.

Voir les services détectés :

```bash
nmap -sV 192.168.1.135
```

---

## 31. IoT

**IoT = Internet of Things**

Objets connectés :

* caméras ;
* alarmes ;
* ampoules ;
* prises ;
* thermostats ;
* etc.

Un appareil peut être commercialisé sous une marque mais utiliser un module Wi-Fi d’un autre constructeur.

### Commandes utiles

Lister les voisins réseau :

```bash
arp -a
```

Scanner les hôtes actifs du LAN avec `nmap` :

```bash
nmap -sn 192.168.1.0/24
```

Cela effectue une découverte des machines actives sans scanner tous leurs ports.

---

## 32. Tuya

Tuya est une plateforme utilisée par de nombreux objets connectés.

Un équipement détecté comme :

```text
Tuya Smart Inc.
```

ne permet pas de savoir s’il s’agit exactement :

* d’une caméra ;
* d’une prise ;
* d’un capteur ;
* d’une alarme.

### Commandes utiles

Rechercher l’appareil dans la table ARP :

```bash
arp -a
```

Puis tester son adresse :

```bash
ping IP_DE_L_APPAREIL
```

Et éventuellement :

```bash
nmap -sV IP_DE_L_APPAREIL
```

---

## 33. OUI / constructeur MAC

Les premiers octets d’une adresse MAC correspondent souvent à un fabricant enregistré.

Exemple :

```text
CC:8C:BF
```

### Commandes utiles

Avec `nmap`, lorsqu’il dispose d’une base de fabricants :

```bash
sudo nmap -sn 192.168.1.0/24
```

Sur un réseau Ethernet local, `nmap` peut parfois afficher :

```text
MAC Address: AA:BB:CC:DD:EE:FF (Manufacturer)
```

Sous Linux, on peut également chercher dans la base IEEE si elle est installée.

---

## 34. RDP

**RDP = Remote Desktop Protocol**

Protocole Microsoft de contrôle à distance.

Port classique :

```text
3389
```

### Commandes utiles

Tester si le port RDP répond :

```bash
nc -vz 192.168.1.20 3389
```

ou :

```bash
nmap -p 3389 192.168.1.20
```

Sous Windows, la recherche forensic des connexions RDP passe surtout par les journaux d’événements Windows.

---

## 35. SSH

**SSH = Secure Shell**

SSH permet d’administrer une machine distante de manière chiffrée.

Port classique :

```text
22
```

### Commandes utiles

Tester le port :

```bash
nc -vz 192.168.1.20 22
```

Identifier le service :

```bash
nmap -sV -p 22 192.168.1.20
```

Connexion :

```bash
ssh utilisateur@192.168.1.20
```

---

## 36. HTTP / HTTPS

HTTP et HTTPS sont utilisés pour les interfaces Web.

Ports courants :

```text
HTTP  : 80
HTTPS : 443
```

### Commandes utiles

Tester HTTP :

```bash
curl -I http://192.168.1.135
```

Tester HTTPS :

```bash
curl -k -I https://192.168.1.135
```

Voir les en-têtes complets :

```bash
curl -v http://192.168.1.135
```

Identifier les ports :

```bash
nmap -p 80,443 192.168.1.135
```

---

## 37. Pare-feu / Firewall

Un pare-feu contrôle les communications autorisées ou interdites.

### Commandes utiles

Sous Linux avec `ufw` :

```bash
sudo ufw status verbose
```

Avec nftables :

```bash
sudo nft list ruleset
```

Avec iptables :

```bash
sudo iptables -L -n -v
```

Sous macOS, voir les règles PF :

```bash
sudo pfctl -sr
```

Voir si PF est actif :

```bash
sudo pfctl -s info
```

---

## 38. Équipement actif / inactif

Il faut distinguer :

* actuellement connecté ;
* connu mais absent ;
* historique.

### Commandes utiles

Voir les voisins récemment connus :

```bash
arp -a
```

ou :

```bash
ip neigh
```

Tester directement :

```bash
ping -c 2 192.168.1.135
```

Attention : un appareil peut être actif sans répondre au ping.

---

## 39. Historique réseau

Les historiques de box sont généralement limités.

Ils peuvent néanmoins contenir :

* MAC ;
* IP ;
* nom ;
* première apparition ;
* dernière apparition ;
* trafic.

### Commandes utiles

Lorsqu’on exporte des fichiers texte ou logs, rechercher une IP :

```bash
grep -R "192.168.1.135" .
```

Chercher une adresse MAC :

```bash
grep -Ri "e0:a2:5a:0d:06:df" .
```

Chercher plusieurs variantes :

```bash
grep -REi "E0:A2:5A:0D:06:DF|E0-A2-5A-0D-06-DF" .
```

Afficher les fichiers contenant la chaîne :

```bash
grep -Ril "192.168.1.135" .
```

---

## 40. Trafic réseau

Le trafic réseau correspond aux données envoyées et reçues.

### Commandes utiles

Sous Linux :

```bash
ip -s link
```

Voir les connexions réseau ouvertes :

```bash
ss -tunap
```

Sous macOS :

```bash
netstat -an
```

Voir les connexions par processus :

```bash
lsof -i
```

Capture réseau avec tcpdump :

```bash
sudo tcpdump -i en0
```

Limiter à une IP :

```bash
sudo tcpdump -i en0 host 192.168.1.135
```

---

## 41. Upload et download

**Download** :

```text
Internet → appareil
```

**Upload** :

```text
appareil → Internet
```

### Commandes utiles

Sous Linux :

```bash
ip -s link
```

Donne notamment les compteurs :

```text
RX
TX
```

* RX = données reçues ;
* TX = données envoyées.

Avec `iftop` :

```bash
sudo iftop
```

Avec `nload` :

```bash
nload
```

---

## 42. Connexion locale vs connexion Internet

Deux appareils du LAN peuvent communiquer directement :

```text
PC → caméra
```

sans passer par Internet.

Une communication cloud passe en revanche par la box :

```text
caméra → serveur cloud
```

### Commandes utiles

Voir par où passerait un paquet :

```bash
route -n get 192.168.1.135
```

Sous Linux :

```bash
ip route get 192.168.1.135
```

Vers Internet :

```bash
traceroute 8.8.8.8
```

ou sous Linux :

```bash
tracepath 8.8.8.8
```

---

## 43. Adresse MAC privée sur iPhone

Les iPhone utilisent généralement une fonction appelée **Adresse Wi-Fi privée**.

Un même téléphone peut donc apparaître avec une adresse MAC qui ne ressemble pas à une MAC Apple classique.

### Commandes utiles

Depuis un ordinateur du LAN :

```bash
arp -a
```

permet de voir l’adresse MAC actuellement associée à l’adresse IP de l’iPhone.

Exemple :

```text
? (192.168.1.73) at 6a:92:e3:54:e4:62
```

---

## 44. Déconnexion physique

Débrancher un appareil est une bonne méthode d’identification empirique.

Exemple :

```text
avant : Ethernet 2 actif
débrancher appareil
après : Ethernet 2 inactif
```

### Commandes utiles

Sur une machine Linux directement concernée :

```bash
ethtool eth0
```

Chercher :

```text
Link detected: yes
```

puis après déconnexion :

```text
Link detected: no
```

Sur la Freebox, cette vérification se fait surtout dans l’interface réseau.

---

# Outils Bash particulièrement utiles

## `ping`

Tester rapidement si un équipement répond :

```bash
ping 192.168.1.135
```

Version limitée :

```bash
ping -c 4 192.168.1.135
```

---

## `arp`

Afficher les associations IP / MAC connues :

```bash
arp -a
```

Exemple :

```text
? (192.168.1.135) at e0:a2:5a:0d:06:df on en0
```

---

## `ip neigh`

Équivalent moderne de `arp` sous Linux :

```bash
ip neigh
```

---

## `nmap`

`nmap` est extrêmement utile pour cartographier un réseau.

Sur macOS :

```bash
brew install nmap
```

Découverte des appareils actifs :

```bash
nmap -sn 192.168.1.0/24
```

Scanner une machine :

```bash
nmap 192.168.1.135
```

Détecter les services :

```bash
nmap -sV 192.168.1.135
```

Scanner certains ports seulement :

```bash
nmap -p 21,22,80,443,554,3389 192.168.1.135
```

---

## `nc` / netcat

Tester rapidement si un port répond :

```bash
nc -vz 192.168.1.135 80
```

Exemple SSH :

```bash
nc -vz 192.168.1.135 22
```

Exemple FTP :

```bash
nc -vz 192.168.1.254 21
```

---

## `curl`

Tester des services Web :

```bash
curl http://192.168.1.135
```

Afficher seulement les en-têtes :

```bash
curl -I http://192.168.1.135
```

Pour HTTPS avec certificat non reconnu :

```bash
curl -k https://192.168.1.135
```

---

## `dig`

Tester le DNS :

```bash
dig google.com
```

Réponse courte :

```bash
dig +short google.com
```

---

## `traceroute`

Voir le chemin suivi vers une destination :

```bash
traceroute google.com
```

---

## `tcpdump`

Capturer du trafic réseau :

```bash
sudo tcpdump -i en0
```

Seulement une machine :

```bash
sudo tcpdump -i en0 host 192.168.1.135
```

Seulement le DNS :

```bash
sudo tcpdump -i en0 port 53
```

Seulement HTTP/HTTPS :

```bash
sudo tcpdump -i en0 'port 80 or port 443'
```

Écrire la capture dans un fichier :

```bash
sudo tcpdump -i en0 -w capture.pcap
```

Ce fichier peut ensuite être ouvert dans Wireshark.

---

## `lsof`

Voir les connexions réseau et les processus associés sous macOS :

```bash
lsof -i
```

Afficher les ports sans résolution de noms :

```bash
lsof -i -P -n
```

Uniquement les ports en écoute :

```bash
lsof -i -P -n | grep LISTEN
```

---

## `netstat`

Afficher les connexions réseau :

```bash
netstat -an
```

Afficher la table de routage :

```bash
netstat -rn
```

---

## `grep`

Très utile pour analyser des exports et journaux.

Chercher une IP :

```bash
grep -R "192.168.1.135" .
```

Chercher une MAC :

```bash
grep -Ri "E0:A2:5A:0D:06:DF" .
```

Avec numéro de ligne :

```bash
grep -Rni "STARVOX" .
```

---

## `find`

Chercher des fichiers :

```bash
find . -type f
```

Chercher des logs :

```bash
find . -type f -name "*.log"
```

Chercher par date de modification :

```bash
find . -type f -newermt "2024-10-15" ! -newermt "2024-10-29"
```

Très utile lors d’une analyse forensic.

---

## `stat`

Afficher les métadonnées d’un fichier :

```bash
stat fichier.log
```

Sous macOS :

```bash
stat -x fichier.log
```

---

## `shasum`

Calculer un hash :

```bash
shasum -a 256 fichier.img
```

Exemple :

```text
SHA-256
```

Très utile pour garantir l’intégrité d’un fichier ou d’une image forensic.

---

# Mini boîte à outils réseau pour macOS

Installer les outils principaux :

```bash
brew install nmap
brew install miniupnpc
```

Les outils suivants sont déjà présents sur macOS dans la plupart des cas :

```text
ping
arp
ifconfig
netstat
route
curl
nc
dig
traceroute
tcpdump
lsof
grep
find
shasum
```

---

# Commandes pratiques pour ton analyse Freebox

## Voir ton interface réseau

```bash
ifconfig
```

## Voir ton IP locale

```bash
ipconfig getifaddr en0
```

## Voir ta passerelle

```bash
route -n get default
```

## Voir les équipements récemment connus

```bash
arp -a
```

## Découvrir les équipements du réseau

```bash
nmap -sn 192.168.1.0/24
```

## Scanner un équipement inconnu

```bash
nmap -sV 192.168.1.195
```

## Tester un port

```bash
nc -vz 192.168.1.195 80
```

## Vérifier les ports courants d’une caméra

```bash
nmap -p 80,443,554,8000,8080 192.168.1.195
```

## Capturer les communications avec un appareil

```bash
sudo tcpdump -i en0 host 192.168.1.195
```

## Sauvegarder la capture

```bash
sudo tcpdump -i en0 host 192.168.1.195 -w appareil-192-168-1-195.pcap
```

## Rechercher une IP dans des exports

```bash
grep -Rni "192.168.1.195" .
```

## Rechercher une MAC dans des exports

```bash
grep -Rni "70:70:AA:0D:EC:11" .
```

---

# Point important en forensic

Une commande réseau montre généralement **l’état observable au moment où elle est exécutée**.

Par exemple :

```bash
arp -a
```

ne constitue pas un historique exhaustif des appareils ayant été connectés au réseau.

De même :

```bash
nmap -sn 192.168.1.0/24
```

permet surtout de découvrir les équipements actuellement joignables.

Il faut donc toujours distinguer :

```text
Observation actuelle
```

de :

```text
Trace historique
```

et :

```text
Déduction
```

Dans un rapport forensic, cette distinction est essentielle.

Une bonne formulation est par exemple :

> Au moment de l’analyse, l’équipement n’était pas détecté sur le réseau.

plutôt que :

> Cet équipement n’a jamais été connecté au réseau.

La seconde affirmation nécessiterait des traces historiques suffisamment complètes pour pouvoir l’établir.
