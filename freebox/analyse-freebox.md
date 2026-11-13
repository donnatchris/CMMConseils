# Rapport d’analyse technique de la Freebox Révolution

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine, DMM Conseils

**Prestataire :** Christophe Donnat — Donnat Dev — christophe@donnat.dev

**Équipement :** Freebox Révolution du domicile de la cliente

## 1. Objet et périmètre

Ce rapport présente la configuration réseau consignée, les identités d’équipements conservées par la Freebox et les indices éventuels d’accès non autorisé, de modification de configuration ou de transfert de données. Il examine les traces anciennes encore disponibles depuis **2021/2022**, avec une attention particulière à **octobre 2024** et aux rapprochements avec les appareils de la mission.

Les conclusions reposent sur les captures Freebox OS, les réponses API conservées et les recoupements documentés avec OP-01, TP-01/02/03 et les applications caméra. Les [mails de mission](../docs/mail.txt) et [complémentaires](../docs/mail-2.txt) définissent les demandes de la cliente ; ses déclarations sur les équipements et événements sont distinguées des constats techniques.

**Les données décrivent des relevés de septembre 2026 et des horodatages historiques résiduels. Elles ne constituent ni un état complet de la configuration en octobre 2024 ni un journal exhaustif des connexions, commandes ou transferts depuis 2021.** L’analyse est une investigation privée, sans désignation comme expertise judiciaire.

## 2. Synthèse des conclusions

| Question | Résultat technique | Portée et limite |
|---|---|---|
| Une intrusion est-elle démontrée ? | **Aucune trace positive conservée ne caractérise une intrusion, une administration non autorisée ou une exfiltration attribuable à une des identités examinées.** | Les journaux nécessaires à une exclusion exhaustive ne sont pas disponibles dans les données collectées. |
| Quels appareils anciens sont représentés ? | **74 fiches API**, dont **56** avec au moins une trace avant le 29 octobre 2024 ; **40** ont une connectivité IP datée avant cette borne et **16** seulement une trace générale antérieure. | Une fiche ou une MAC privée n’est pas nécessairement un appareil physique distinct. |
| Des présences sont-elles datées d’octobre 2024 ? | Cinq fiches ont leur première trace du **12 au 17 octobre**, dont trois avec des connectivités IP datées de la période. | Ces indices ne donnent ni utilisateur, ni service contacté, ni continuité de connexion. |
| Les appareils sont-ils identifiés ? | `LAPTOP-RMCOB2VU` est rattaché à **OP-01** ; une MAC correspond exactement à une configuration Xiaomi **mwc11**. | Le `DESKTOP-ICPNCMD` du 16 et les trois identités iPhone nocturnes restent non attribués. |
| La configuration expose-t-elle des services ? | Pas de redirection manuelle, DMZ, redirection UPnP active ou VPN intégré actif dans les relevés. **SMB local sans authentification et pare-feu IPv6 désactivé** sont consignés. | Ces paramètres permissifs ne prouvent pas une intrusion et ne certifient pas les réglages de 2024. |
| Un accès aux caméras ou aux fichiers est-il établi ? | Aucun journal conservé n’attribue une consultation de caméra ou de fichier SMB à une identité déterminée. Le disque exposé contient cinq enregistrements TV et leurs index. | Une possibilité technique d’accès local n’est pas un accès effectivement démontré. |
| Les volumes transférés en 2024 sont-ils quantifiables ? | **Non.** La requête de statistiques historiques échoue et les compteurs disponibles ne sont pas un historique par appareil de 2024. | Aucun volume anormal ou destinataire d’exfiltration ne peut être attribué à partir de ces seuls éléments. |

**Les traces établissent des détections et certaines connectivités IP historiques, sans permettre de qualifier l’activité d’un appareil de piratage ou de certifier l’absence de tout accès ancien.**

## 3. Sources, méthode et sens des traces

### 3.1. Données examinées

Les relevés proviennent de l’interface **Freebox OS** et de l’**API v16**, notamment de l’interface LAN **`pub`**. Les réponses brutes sont conservées sous [preuves-json](preuves-json/). La collecte API de référence est datée du **28 septembre 2026** ; les captures décrivent des instants distincts du même mois et ne sont pas assimilées à un unique état simultané.

L’accès de mission repose sur l’autorisation de la cliente. L’authentification API utilise une application associée avec validation physique sur le Server, puis un mécanisme challenge/réponse et un jeton de session. **Cette association technique de mission ne constitue pas une preuve d’accès ancien.** Les mots de passe et jetons ne sont pas reproduits dans ce rapport.

Les requêtes de consultation couvrent inventaire LAN, fiches détaillées, Wi-Fi, DHCP, connexion Internet, redirections, DMZ, VPN, téléchargements, envois et statistiques. Les réponses enregistrées constituent les pièces de contrôle ; elles ne sont pas une image physique de la Freebox ou de son disque.

### 3.2. Périmètre de l’inventaire historique

Une réponse d’interface annonce **75 hôtes**, mais l’inventaire détaillé retourne **74 fiches effectivement conservées**. L’écart peut tenir à un compteur non rafraîchi ou à une variation entre requêtes ; aucune fiche supplémentaire n’est reconstituée par hypothèse.

La sélection historique retient tout horodatage positif antérieur au **29/10/2024 à 00:00 Paris**, soit le seuil Unix **`1730156400`**. Elle examine `first_activity`, `last_activity`, `last_time_reachable` et les dates des adresses de `l3connectivities`.

| Nature de la trace | Ce qu’elle établit | Ce qu’elle n’établit pas |
|---|---|---|
| **Détection ou fiche seulement** | Une identité a un repère général conservé avant la limite. | Pas de connectivité IP ancienne datée dans les adresses encore présentes ; cela ne signifie pas qu’elle n’a jamais eu d’IP. |
| **Connectivité IP historique** | Au moins une IPv4 ou IPv6 conserve un horodatage antérieur à la limite. | Pas de détail des flux, fichiers, commandes, destinations ou utilisateurs. |
| **État actif/joignable** | État au moment du relevé. | Pas de présence continue entre deux dates historiques ni d’historique complet des associations. |

Les **56 fiches historiques**, dont **40 avec IP et 16 sans IP datée avant la limite**, sont reprises en section 13. Les **seize fiches ciblées** dans les sections 7 et 8 comprennent onze identités anciennes et cinq apparues en octobre ; ces ensembles ne s’ajoutent pas aux 74 fiches.

### 3.3. Conventions temporelles et identité réseau

Les valeurs API sont des **secondes Unix**, converties avec **Europe/Paris**, UTC+1 en hiver et UTC+2 en été. Les valeurs brutes sont prioritaires pour les rapprochements précis. Les retranscriptions anciennes appliquant une heure d’été à des dates d’hiver ne sont pas reprises comme référence.

Pour la fiche **`A6:14:3E:8A:34:ED`**, une retranscription donne le **4 mars 2024 à 00:14:41**, contre **23:14:41** après conversion de la valeur API. Cette divergence dépasse un simple effet de fuseau ; son origine de transcription ou d’affichage reste indéterminée. Les tableaux du présent rapport retiennent la valeur API, sans assimiler les deux indications à deux événements.

`first_activity` n’est pas une première connexion historique garantie : OP-01 conserve une connectivité de **janvier 2023** malgré une première activité de fiche en **juillet 2024** ; deux autres fiches ont `first_activity=0` malgré plusieurs adresses anciennes. Création ou recréation de fiche, conservation d’adresses et rapprochements internes sont des explications possibles, sans mécanisme précis démontré.

Les noms DHCP, mDNS ou WSD et les types affichés ne sont pas des identités physiques certifiées. Une MAC **localement administrée** peut être privée ou aléatoire ; elle ne permet pas une attribution fiable à un constructeur et n’est pas, par elle-même, suspecte. Plusieurs identités peuvent appartenir à un même appareil et une adresse IP peut changer de titulaire.

**Les premières et dernières valeurs d’une fiche ne sont ni des heures certaines de connexion/déconnexion ni la preuve d’une session continue entre ces bornes.**

## 4. Configuration de la Freebox dans les relevés

### 4.1. Connexion Internet et réseau local

| Paramètre | État consigné |
|---|---|
| Accès Internet | **FTTH actif** |
| IPv4 publique | **`88.178.32.36`**, ports attribués **0–16 383** |
| IPv6 affichée / préfixe principal | **`2a01:e0a:c88:900::1` / `2a01:e0a:c88:900::/64`** |
| Débits maximaux indiqués | **1 Gb/s descendant**, **900 Mb/s montant** |
| Compteurs affichés | **4,2 Go reçus**, **927,2 Mo émis** |
| Mode réseau / routeur LAN | Routeur, **`192.168.1.254`**, domaine **`home`** |
| Noms de service | `freebox-server` en DNS, `Freebox-Server` en mDNS, `Freebox_Server` en NetBIOS |
| Liaison optique | Lien et signal présents, alimentation OK ; SFP **TLE TUNG-LI OF001-003C**, série **2107071255** |

La plage IPv4 partielle signifie que **l’adresse seule peut être insuffisante pour attribuer une connexion** : l’heure et le port source sont aussi nécessaires lorsqu’ils sont disponibles. Les adresses, plages de ports, compteurs et débits de 2026 ne sont pas extrapolés à octobre 2024.

Le journal de connexion conservé ne contient que **deux événements du 16 septembre 2026**, lien FTTH à **09:48:05** puis connexion Internet publique à **09:48:26**. Aucun événement de 2024 n’y figure ; ce journal ne décrit pas l’activité individuelle des appareils.

### 4.2. Administration et applications autorisées

L’option d’authentification distante par mot de passe est activée pour la mission. L’état antérieur photographié ne l’avait pas activée, tout en indiquant que les applications autorisées et liens de partage pouvaient disposer de leurs propres accès. Ces voies ne sont donc pas confondues.

Trois applications autorisées sont consignées : **Freebox Connect « iPhone de dmm conseils »**, dernier accès du **21 février 2022**, **Freebox Connect « iPhone »**, dernier accès du **21 septembre 2026**, et **Free « iPhone »**, dernier accès du **8 avril 2026**. Les droits affichés sont nuls dans la capture consultée ; **cela ne reconstitue ni leurs droits passés ni un historique exhaustif de leurs accès**.

Une seule session Freebox OS est affichée et attribuée par le prestataire à son accès d’analyse. Cet écran est un état de sessions actives, pas un registre des anciennes connexions. Un abonnement de notification iPhone aux catégories « Périphériques réseaux » et « Mot de passe » porte une date voisine de l’accès Freebox Connect du 21 septembre 2026, sans attribution certaine à un geste précis.

Aucun élément de ces écrans ne relie un des seize appareils ciblés à une session ou modification de configuration. L’état de l’accès distant après la mission n’est pas certifié par ces seuls relevés.

### 4.3. Services entrants et paramètres de sécurité

| Fonction | État observé | Portée |
|---|---|---|
| Accès distant Freebox OS | HTTP **3591**, HTTPS **9717** actifs | Accès d’administration prévu dans le cadre de la mission ; pas preuve de sa configuration historique. |
| Redirections manuelles / DMZ | Aucune redirection ; DMZ désactivée | Pas d’exposition IPv4 par ces mécanismes dans les relevés. |
| UPnP IGD | Service activé, **aucune redirection active** | Une ouverture temporaire ancienne supprimée n’est pas exclue. |
| Serveurs VPN intégrés | PPTP, OpenVPN, IPsec/IKEv2 et WireGuard désactivés | Ne décrit pas les VPN propres aux appareils. |
| Client VPN intégré | Désactivé, configuration et journal vides dans les réponses | Aucun tunnel conservé attribuable, sans historique complet. |
| DNS dynamique | DynDNS, No-IP et OVH désactivés | État de configuration seulement. |
| Pare-feu IPv6 Freebox | **Désactivé** ; aucun Next Hop configuré | Ce filtrage entrant n’est pas appliqué par cette fonction ; accessibilité effective dépend aussi des appareils et services. |
| Services BitTorrent Freebox | Ports **9830 DHT** et **13035 principal** actifs | Présence de services intégrés ; ne démontre pas un transfert effectué. |

**Le pare-feu IPv6 désactivé est un paramètre permissif, sans preuve autonome qu’un appareil était effectivement accessible depuis Internet.** L’absence de NAT/DMZ active ne permet pas de conclure sur tous les chemins d’accès possibles ou sur des configurations anciennes.

### 4.4. Wi-Fi, DHCP et switch

Deux points d’accès sont exposés : **0 en 2,4 GHz** et **10 en 5 GHz**. Le relevé API contient **six stations sur le 2,4 GHz et aucune sur le 5 GHz** ; la capture 2,4 GHz indique canal **6**, largeur **20 MHz**, authentification **WPA2**. L’historique WPS visible est vide, sans preuve d’absence de tout usage ancien du WPS.

Le relevé DHCP API contient **cinq baux dynamiques et aucune réservation statique**. Les stations et baux ne se confondent pas : ils décrivent des sources et instants distincts. Les compteurs Wi-Fi concernent les associations conservées, pas les volumes historiques par appareil depuis 2022.

Le switch indique Ethernet **1, 2 et 4 actifs**, Ethernet **3 inactif**. Le port 4 ne fournit pas de MAC dans cette vue. Ces liaisons décrivent l’état observé, sans identifier toute l’histoire du câblage.

## 5. Disque interne et partage de fichiers

### 5.1. Support et contenu visible

| Élément | Valeur consignée |
|---|---|
| Disque interne | **HGST HCC545050A7E630**, capacité nominale **500,1 Go** |
| Série / firmware | **21GBJZ6T / GR2OA310** |
| Table annoncée / état | MBR / actif, **49 °C** |
| Opérations lecture / écriture | **2 801 220 / 160 336**, aucune erreur signalée |
| Volume exposé | « Disque dur », **ext4**, **244,9 Go**, 10,5 Go utilisés et 221,9 Go disponibles |

L’interface n’expose pas à elle seule toute la table de partitions et l’affectation de la capacité physique. Ces valeurs ne caractérisent pas les zones non visibles ou supprimées ; aucune analyse physique du disque n’est établie par cette consultation distante.

L’explorateur présente **cinq enregistrements télévisés**, chacun avec un index `.m2ts.idx` : quatre épisodes de **« Rénovation XXL — Bienvenue au château »**, associés à une diffusion du **10 juillet 2022**, et un reportage **Martin Weill au Mexique**, associé au **4 avril 2023**. Les caractéristiques de médias sont compatibles avec des enregistrements TV. L’échantillon documenté est un conteneur BDAV d’environ 49 min 44 s, vidéo AVC 720 × 576 et pistes AAC/télétexte.

**Aucun document personnel ou professionnel ni fichier inhabituel en lien avec la mission n’est relevé dans le contenu visible.** Cela ne vaut pas inventaire de secteurs supprimés ou de volumes non exposés.

### 5.2. Protocoles d’accès aux fichiers

Le **partage SMB2/SMB3 est activé sans authentification supplémentaire** sur le réseau local. Un appareil disposant déjà de cet accès réseau pouvait donc potentiellement parcourir les fichiers partagés sans compte SMB distinct. Aucune exposition directe du partage à Internet n’est relevée dans la configuration consignée.

Le serveur FTP et l’accès FTP distant sont désactivés ; ses ports configurés sont inactifs. Une configuration d’identification subsiste avec un mot de passe signalé insuffisamment robuste par l’interface, sans valeur reproduite ici. Aucun démarrage TFTP n’est configuré. Le partage spécifique macOS et le partage d’imprimantes sont désactivés ; un Mac peut néanmoins utiliser SMB.

**Une possibilité technique d’accès local ne démontre pas une lecture ou copie effective.** Aucun journal conservé ne relie un fichier ouvert via SMB à une IP, une MAC ou une personne, et aucun accès passé ne peut être exclu sur la seule absence d’un tel journal.

## 6. Équipements identifiés et cartographie des relevés

La cliente déclare notamment trois caméras chambre/salon/terrasse, une caméra de l’écosystème Xiaomi, plusieurs iPhone, des ordinateurs HP et ASUS, deux imprimantes et des appareils de visiteurs. Ces déclarations servent au rapprochement ; elles ne suffisent pas à attribuer chaque MAC à un matériel ou à une personne.

| Identité réseau | Présence ou rattachement documenté | Niveau d’identification |
|---|---|---|
| **`50:E0:85:63:41:5B` — `LAPTOP-RMCOB2VU`** | MAC exacte de l’interface WLAN d’**OP-01** ; IPv4 conservée `192.168.1.194` | **OP-01 identifié**, sans utilisateur identifié. |
| **`E0:A2:5A:0A:A3:F7`** | MAC exacte d’une configuration Xiaomi Home **`mxiang.camera.mwc11`** dans TP-02 | Configuration caméra identifiée ; pas de numéro physique ou carte SD associés. |
| **`E0:A2:5A:0D:06:DF` — `mxiang-camera-mwc10_miap06DE`** | `192.168.1.135`, Ethernet 1 ; configuration Xiaomi conservant `…:DE`, même IP | Rapprochement plausible, **MAC non identiques** ; interfaces non fusionnées par hypothèse. |
| **`98:AA:FC:13:18:93` — `STARVOX-98AAFC131893`** | `192.168.1.169`, Ethernet 2 | Centrale d’alarme déclarée et confirmée par la cliente, aujourd’hui inutilisée selon elle. |
| **`1C:90:FF:9D:B8:4A` — `wlan0`** | `192.168.1.159`, Wi-Fi 2,4 GHz | Appareil précis non identifié ; le nom ne démontre pas une imprimante. |
| **`6A:92:E3:54:E4:62` — `iPhone`** | `192.168.1.73`, Wi-Fi 2,4 GHz | Modèle et exemplaire non attribués. |
| **`D2:0E:25:1B:5B:B8` — `iPhone`** | `192.168.1.18`, Wi-Fi 2,4 GHz | Même limite. |
| **`70:70:AA:0D:EC:11` — `192-168-1-195` / `android2-home` selon le relevé** | `192.168.1.195`, Wi-Fi 2,4 GHz | Équipement précis non identifié. |
| **`C4:3C:B0:23:34:46`** | Station Wi-Fi, fabricant de module indiqué Shenzhen Bilian | Le fournisseur du module ne désigne pas une caméra ou imprimante physique. |
| **`CC:8C:BF:8E:33:8A`** | Station Wi-Fi, indication Tuya Smart | Écosystème d’objets connectés, sans identification physique certaine. |
| **Ethernet 4** | Lien actif, sans MAC affichée | Équipement non identifié. |

Les IPv4, ports et associations sont ceux des vues où ils sont relevés. Ils ne constituent pas un plan d’adressage historique fixe. Le classement « ordinateur fixe » d’une fiche ne prévaut pas sur une correspondance de MAC et ne certifie pas la nature du matériel.

## 7. Identités anciennes ciblées et traces depuis 2022

Onze fiches font l’objet d’un examen détaillé. **Sept conservent une connectivité IP antérieure à la limite et quatre seulement une trace de détection antérieure.** Deux sont désormais rattachées à OP-01 et à une configuration caméra ; l’absence initiale d’identification n’est pas une preuve de caractère malveillant.

| MAC et identité | Dates utiles, Paris | Constat et conclusion |
|---|---|---|
| **`50:E0:85:63:41:5B` — OP-01** | Connectivité dès **13/01/2023**, première activité de fiche **23/07/2024 15:37:02** ; autres dernières dates en septembre 2026 | Sept connectivités. L’ancienne IPv6 a une dernière activité au **13/01/2023 10:15:23** ; la fiche n’est pas un journal de première apparition. |
| **`E0:A2:5A:0A:A3:F7` — configuration mwc11** | **19/07/2024 21:02:47** | Détection générale, aucune `l3connectivity` conservée ; pas d’usage IP historique démontré par cette fiche. |
| **`A6:14:3E:8A:34:ED` — nom UUID** | Fiche **04/03/2024 23:14:41** ; IPv4 **02/05/2024 13:00:02** ; autres traces dès novembre 2024 et en 2025 | Dix connectivités ; appareil non identifié. Pas d’entrée du 15–28 octobre, sans exclusion de présence. |
| **`CE:04:84:BC:D2:4D`** | Repères **11/06/2024 14:00:54–14:25:49** | IPv4 `192.168.1.98` et quatre IPv6. Repères espacés de vingt-cinq minutes, sans continuité démontrée. |
| **`16:E8:85:01:02:FD`** | **02/05/2024 12:50:13** | Détection sans adresse IP conservée. |
| **`4E:B5:4A:B0:3F:04`** | **21/01/2024 13:20:29** | Détection sans adresse IP conservée. |
| **`DE:98:33:8D:2C:A2`** | Fiche **16/08/2023 17:05:18** ; activités les 21/25 septembre, 18 octobre et **11/12/2023 10:19:39** | IPv4 `192.168.1.75` et huit IPv6 ; connectivités répétées anciennes, sans trace de 2024 conservée. |
| **`E6:E1:90:ED:E4:94`** | **11/10/2022 16:24:30** | Détection sans adresse IP conservée. |
| **`56:96:03:FB:28:58`** | Repères **07/07/2022 19:00:35–19:21:38** | Deux IPv6 ; connectivité datée, sans détail des activités pendant l’intervalle. |
| **`F2:D1:B4:69:51:D8`** | **15/10/2022 05:52:22–01/02/2023 04:30:42** | IPv4 `192.168.1.131` et huit IPv6 malgré `first_activity=0`. |
| **`B6:BD:59:D2:25:62`** | **05/04/2022 21:37:27–02/05/2022 21:19:52** | Huit IPv6 malgré `first_activity=0` ; absence d’IPv4 ne signifie pas absence de connectivité. |

Neuf de ces onze MAC sont localement administrées. Les noms UUID et les adresses privées ne permettent pas d’attribuer un propriétaire ou un usage. **Aucune de ces onze fiches Freebox ne conserve une entrée explicitement datée du 15 au 28 octobre 2024**, mais cela ne nie pas les traces d’autres supports, notamment le WLAN d’OP-01, ni une présence dont la dernière date aurait été remplacée.

L’inventaire contient des traces depuis **mars 2022**, pas un historique complet de 2021. Les activités anciennes de 2022/2023 ne peuvent pas être qualifiées d’intrusion sur leur seule date ou sur la coïncidence avec le début du contrôle fiscal.

## 8. Fiches proches de la perquisition et présences nocturnes

### 8.1. Cinq identités apparues du 12 au 17 octobre 2024

| MAC / nom API | Première trace, Paris | Connectivités et dernière trace utile | Qualification avant le 29 octobre |
|---|---|---|---|
| **`96:8F:D6:BB:47:D7` — iPhone** | **12/10 23:15:06** | Huit IPv6 dont les dernières dates conservées sont en novembre/décembre | Détection avant la limite, sans IP d’octobre encore datée. |
| **`EA:21:6C:F7:47:E7` — iPhone** | **16/10 00:20:00** | IPv4 **`192.168.1.3`**, cinq IPv6 ; dernière trace retenue **17/10 00:57:02** | Connectivité IP datée pendant la période. |
| **`AC:ED:5C:DA:47:74` — DESKTOP-ICPNCMD** | **16/10 21:27:48** | IPv6 datées du 16, dernière trace retenue **23:25:55** ; autres données en 2026, IPv4 `192.168.1.41` | Connectivité IP datée ; ordinateur non identifié. |
| **`9C:64:8B:0A:BD:0C` — iPhone** | **17/10 01:00:57** | IPv4 **`192.168.1.55`**, cinq IPv6 ; dernière trace retenue **03:43:56** | Connectivité IP datée pendant la période. |
| **`FE:AA:76:95:AC:29` — iPhone** | **17/10 03:45:44** | Huit IPv6 dont les dernières dates sont en novembre/décembre | Détection avant la limite, sans IP d’octobre encore datée. |

**Trois fiches conservent donc une preuve IP de la période, et deux une détection générale seulement avant la limite.** Les dates postérieures des adresses de ces deux dernières n’effacent pas leur détection initiale ; elles ne permettent pas de reconstruire leurs connexions IP antérieures.

L’ordinateur `DESKTOP-ICPNCMD` conserve une indication de constructeur Intel, sans rattachement positif à OP-01 ou à un utilisateur. Son nom ne prouve pas une origine administrative. Une présence réseau ou un nom iPhone ne caractérise pas un accès sensible.

### 8.2. Succession des trois identités iPhone

Dans la nuit du **16 au 17 octobre**, les valeurs conservées décrivent la succession suivante :

| Repère de fiche, Paris | Identité | Écart avec le repère précédent |
|---|---|---|
| **17/10 00:57:02**, dernière trace retenue | `EA:21:6C:F7:47:E7` | — |
| **17/10 01:00:57**, première trace | `9C:64:8B:0A:BD:0C` | **3 min 55 s** |
| **17/10 03:43:56**, dernière trace retenue | `9C:64:8B:0A:BD:0C` | Repère de la même fiche, pas durée de session certifiée. |
| **17/10 03:45:44**, première trace | `FE:AA:76:95:AC:29` | **1 min 48 s** |

Les première et troisième MAC sont localement administrées ; celle commençant par `9C:64:8B` est attribuée à Apple et n’a pas ce bit d’administration locale. La succession peut correspondre à plusieurs iPhone ou à un changement de mode d’adresse privée, **sans permettre de fusionner les trois fiches ou de les rattacher à une personne**.

L’intervalle d’environ **24 h 37** entre les repères de la première fiche et celui d’environ **2 h 43** de la deuxième ne sont pas des durées certaines de connexion. **Ces valeurs ne datent pas non plus une extinction, une déconnexion volontaire ou un changement de téléphone.**

### 8.3. Situation des seize fiches au relevé API

Les seize fiches ciblées sont marquées **`active=false` et `reachable=false`** au relevé. Aucune ne figure dans les stations Wi-Fi, baux dynamiques ou réservations statiques de ce même contrôle ; aucun nom principal n’est marqué comme défini manuellement.

Ce constat décrit leur état au relevé, pas leur absence historique, et ne contredit pas les dates anciennes ou de 2026 conservées ailleurs dans leurs fiches. Il n’attribue pas les présences nocturnes à un matériel.

## 9. Rapprochements avec les appareils de la mission

### 9.1. OP-01 et les échecs SMB du 26 mars 2024

La MAC **`50:E0:85:63:41:5B`** est identique dans la fiche Freebox et les événements WLAN d’OP-01 du **15 octobre 2024**. Le rattachement de l’identité `LAPTOP-RMCOB2VU` à l’ordinateur est donc positif, même si la Freebox ne conserve pas de connectivité de cette date dans sa fiche. L’identité du matériel ne désigne pas son utilisateur.

OP-01 enregistre aussi deux **échecs d’authentification SMB**, le **26/03/2024 à 15:20:36 et 15:21:12 Paris**, depuis **`192.168.1.139`**, statut **`0xC000006D`**. La Freebox associe cette IP à **`LAPTOP-205Q5H9C`**, MAC **`F8:28:19:77:42:71`**, dont une dernière activité IPv4 est consignée le même jour à **15:48:20**.

C’est un **candidat étayé par l’adresse et la proximité temporelle**, pas une attribution certaine : aucun historique de bail couvrant les secondes des tentatives ne garantit le titulaire de l’IP à cet instant. **Les événements sont des échecs, sans accès réussi, intrusion ou exfiltration démontrés.** Ils concernent le service SMB d’OP-01, distinct du partage SMB de la Freebox.

### 9.2. Correspondances Wi-Fi des téléphones

Les préférences conservées de TP-02/TP-03 permettent **trois correspondances de MAC clientes distinctes** avec l’inventaire Freebox :

| Adresse cliente | Sauvegarde et rapprochement | Portée temporelle |
|---|---|---|
| **`0E:41:84:EF:66:27`** | État Wi-Fi privé de TP-02 ; ajout à **14:27:28.692**, première activité Freebox à **14:27:30** le 11 juin 2024 | Concordance précise de valeurs, sans étalonnage global ou preuve d’une session continue. |
| **`08:87:C7:76:C4:10`** | Égalité avec une préférence TP-02 | État du téléphone daté de 2025 face à une activité Freebox de 2024 ; une préférence actuelle n’est pas un historique complet. |
| **`C6:A2:88:AC:F8:CB`** | Égalité avec une adresse privée de TP-03 | Fiche de **septembre 2025**, sans preuve de présence sous cette MAC en octobre 2024. |

Aucun identifiant client Wi-Fi exploitable n’est obtenu pour **TP-01** dans les préférences examinées. Les en-têtes des trois sauvegardes ne fournissent pas trois identifiants Wi-Fi matériels complets permettant une exclusion universelle.

Les MAC **`EA:21:6C:F7:47:E7`**, **`9C:64:8B:0A:BD:0C`** et **`FE:AA:76:95:AC:29`** ne correspondent pas aux adresses clientes disponibles. **Elles restent non attribuées aux téléphones de la mission**, sans exclusion définitive de ces téléphones en raison de la rotation des MAC, de restaurations possibles et de pertes d’historique. SSID et BSSID de routeurs ne sont pas utilisés à la place des adresses clientes.

### 9.3. Réseau ASUS et séquences système des téléphones

TP-02 conserve des propriétés de configuration/association à **`ASUS_Z01RD` le 17 octobre vers 17:25**, puis deux BSSID associés à des dates du **28 octobre**. Les données ne certifient pas le point d’accès physique du 17. Le nom est absent des préférences TP-01/03 contrôlées, sans garantie d’exhaustivité historique.

OP-01 contient le même SSID dans des fragments compatibles avec des listes de réseaux visibles, **sans date ou connexion commune démontrée**. Ni le nom ASUS ni la marque du PC ne permettent d’en faire le point d’accès.

Les présences Freebox nocturnes n’ont pas d’identifiant matériel les reliant à la séquence TP-02 du 17 ou aux traitements TP-03 du **16 à 05:31**. **Elles ne constituent donc pas une corroboration matérielle de l’usage d’un téléphone scellé à ces heures.**

### 9.4. Caméras et cartes SD

La cliente situe l’installation des caméras après **mars 2023**, une réinitialisation rapportée de la chambre en **février 2024** et un fonctionnement continu de la terrasse. Ces déclarations ne datent pas une session réseau ou une commande à distance.

Les états LSC et Xiaomi conservés permettent certains rapprochements de configuration, sans historique complet de visionnage, de partage ou de changement de compte. Les catalogues LSC ne fournissent pas de référence de média du 15 au 28 octobre. **La présence d’un panneau caméra en cache sur TP-02 ne démontre pas une vidéo consultée.**

Les cartes SD présentent séparément des anomalies de dates, des défauts MP4, des suppressions et des lacunes. Elles n’établissent ni coupure de Freebox, ni effacement à distance, ni commande provenant d’un des téléphones. Les modèles exacts et firmwares des trois caméras ne sont pas identifiés par les caches applicatifs. Les correspondances Xiaomi ne rattachent pas une MAC à une carte SD précise.

Les caméras et cartes **n’étaient pas sous scellés**. Pour les téléphones, le PV situe la mise sous scellés après **14:19 le 15 octobre** puis l’ouverture à **11:30 le 28** ; pour le PC, l’ouverture est à **10:41**. Ces repères ne remplacent pas l’identification matérielle des appareils vus sur le réseau et ne calibrent pas toutes leurs horloges.

## 10. Administration, transferts et recherches d’activité sensible

### 10.1. Résultats disponibles par catégorie

| Axe | Constat | Conclusion limitée |
|---|---|---|
| Administration et paramètres | Aucune fiche LAN reliée à une session, une application autorisée ou une modification. Les deux routes GET de recherche d’historique testées retournent **404 / `invalid_request`**. | Aucun accès administratif ancien attribué ; absence d’historique exploitable via ces appels, pas preuve d’absence d’accès. |
| Redirections, UPnP, DMZ | Listes vides ; **DMZ `enabled=false`** | Aucune ouverture active attribuée dans les relevés ; une configuration ancienne supprimée reste indéterminée. |
| VPN intégré | Client désactivé, configuration et journal vides ; serveurs désactivés dans les captures | Pas de tunnel conservé identifié. Un VPN installé sur un appareil n’est pas couvert par ces seuls états. |
| Téléchargements et envois Freebox | Aucune tâche, aucun flux automatique de téléchargement et liste d’uploads vide | Aucun transfert attribué via ces gestionnaires. Cela ne couvre pas les transferts directs des ordinateurs/téléphones. |
| Fichiers SMB | Possibilité d’accès local sans compte supplémentaire, absence de journal par fichier/IP/MAC | Aucune consultation ou copie attribuable ; son absence n’est pas démontrée. |
| Trafic et exfiltration | Pas de statistiques historiques exploitables par appareil pour la période | Aucun volume anormal, contenu transmis ou destinataire identifié. |

La présence d’une identité sur le LAN ne crée pas de lien automatique avec une session Freebox OS. Les noms DHCP/mDNS/WSD, les ports exposés et les listes de tâches ne donnent pas l’identité d’une personne.

### 10.2. Statistiques historiques non obtenues

La requête RRD visant le **12 au 29 octobre 2024** retourne :

```json
{
  "success": false,
  "error_code": "db_error",
  "msg": "Erreur lors de la récupération des statistiques : Erreur lors de la lecture de la base RRD"
}
```

**Les données demandées ne sont donc pas exploitables dans cette réponse.** L’erreur ne fournit ni volume de trafic, ni preuve d’effacement intentionnel, ni cause d’indisponibilité certaine. Les statistiques RRD, même disponibles, seraient agrégées par connexion, switch ou Freebox et ne permettraient pas à elles seules d’attribuer un volume à une MAC déterminée.

Les compteurs `rx_bytes`/`tx_bytes` des stations Wi-Fi décrivent les associations conservées dans les relevés, où aucune des seize MAC ciblées n’est présente. Ils ne reconstituent pas leur trafic de 2022–2024. Les totaux globaux affichés par Freebox OS ne sont pas davantage des mesures d’exfiltration historique.

**Aucun siphonnage de données n’est démontré ou quantifiable ; son absence ne peut pas être déduite de ces données manquantes.**

## 11. Limites et conclusion technique

### 11.1. Ce que les données ne permettent pas d’établir

L’inventaire LAN conserve des identités, noms, adresses et dernières valeurs, sans journal exhaustif des sites/services contactés, ports TCP/UDP utilisés, flux, volumes historiques par appareil, fichiers ouverts ou commandes d’administration. Les listes de sessions et de configuration décrivent des états, pas l’histoire de leurs changements.

Les données de 2026 ne certifient pas les réglages ou adresses de 2024. Les bornes de fiche ne démontrent pas une présence continue. Les MAC privées, noms d’hôte, IP réattribuables et données transportables des sauvegardes limitent l’identification physique. Une correspondance exacte de MAC renforce un rapprochement mais ne désigne pas un utilisateur ou l’autorisation d’une action.

Les identifications OP-01, configurations Xiaomi et trois correspondances clientes des téléphones sont positives dans leur périmètre. Elles ne résolvent ni l’ordinateur du 16 octobre ni les iPhone nocturnes. L’absence de correspondance n’est pas une exclusion si les états historiques manquent.

### 11.2. Éléments discriminants pour les questions ouvertes

| Question | Éléments utiles |
|---|---|
| À quels matériels correspondent les fiches nocturnes et DESKTOP ? | Anciennes acquisitions/inventaires, MAC matérielles et privées historiques, journaux radio et DHCP contemporains. |
| Un appareil a-t-il administré la Freebox ou consulté un partage ? | Journaux d’audit, captures ou configurations contemporaines et traces concordantes sur l’appareil concerné. |
| Un transfert de données a-t-il eu lieu ? | Journaux de flux ou de service, historique de fichiers et destinations, données serveur ou acquisitions pertinentes. |
| Les mêmes équipements étaient-ils présents lors de la rétention ? | Identifiants matériels contemporains, documents de conservation et horaires indépendants, sans fusion par nom ou proximité temporelle. |
| Une caméra a-t-elle été commandée ou réinitialisée ? | Modèle/firmware, journaux historiques d’appareil/compte/application et source originale des observations signalées. |

La disponibilité de ces archives n’est pas présumée. Les paramètres de rétention, suppressions normales, renouvellements d’adresses et restaurations peuvent limiter les rapprochements. Les témoignages peuvent contextualiser les dates, sans remplacer un identifiant technique discriminant.

### 11.3. Conclusion

**La Freebox conserve 56 fiches avec au moins une trace antérieure au 29 octobre 2024, dont 40 avec une connectivité IP datée. Les cinq identités apparues du 12 au 17 octobre méritent un rapprochement matériel, particulièrement DESKTOP-ICPNCMD et les trois identités iPhone nocturnes. Elles ne sont pas identifiées comme les appareils scellés de la mission.** OP-01 et une configuration Xiaomi sont, en revanche, rattachés par MAC exacte.

L’état de configuration relevé ne présente pas de redirection manuelle, DMZ ou VPN intégré actif, mais comporte des réglages permissifs distincts : **SMB local sans authentification supplémentaire et pare-feu IPv6 désactivé**. Ils caractérisent des possibilités techniques, pas un accès effectivement réalisé ou un état historique garanti.

**Aucune trace conservée n’attribue à une des identités examinées une intrusion, une modification non autorisée, une consultation de caméra/fichier ou une exfiltration.** Les données nécessaires à une exclusion exhaustive — audit d’administration, accès SMB, flux et volumes par appareil — ne sont pas disponibles pour la période. L’absence de preuve positive ne certifie donc pas l’absence d’activité ancienne non autorisée.

## 12. Pièces techniques et termes de lecture

### 12.1. Sources des constats

| Domaine | Pièces de contrôle |
|---|---|
| Inventaire de référence | [Réponse brute des 74 fiches](preuves-json/lan-browser-pub-raw.json) ; réponses individuelles `preuves-json/suspect-*.json`, nommées selon la sélection d’origine, sans présomption d’intrusion. |
| Internet et connexion | [Journal de connexion](preuves-json/activity-connection-logs.json), [configuration de l’accès distant](images/freebox-9.png), [IPv6](images/freebox-10.png) |
| Applications et sessions | [Applications](images/freebox-3.png), [droits affichés](images/freebox-4.png), [session](images/freebox-5.png), [notifications](images/freebox-6.png) |
| Redirections, UPnP et DMZ | [Redirections manuelles](preuves-json/activity-port-forwarding.json), [UPnP](preuves-json/activity-upnp-redirections.json), [DMZ](preuves-json/activity-dmz.json) |
| Wi-Fi et DHCP | [Points d’accès](preuves-json/activity-wifi-aps.json), [stations 2,4 GHz](preuves-json/activity-wifi-ap-0-stations.json), [stations 5 GHz](preuves-json/activity-wifi-ap-10-stations.json), [baux dynamiques](preuves-json/activity-dhcp-dynamic-leases.json), [réservations](preuves-json/activity-dhcp-static-leases-v2.json) |
| VPN | [État client](preuves-json/activity-vpn-client-status.json), [configuration](preuves-json/activity-vpn-client-config.json), [journal](preuves-json/activity-vpn-client-log.json), [capture des serveurs](images/freebox-11.png) |
| Tâches de transfert | [Téléchargements](preuves-json/activity-downloads.json), [flux automatiques](preuves-json/activity-download-feeds.json), [envois](preuves-json/activity-uploads.json) |
| Statistiques historiques | [Réponse RRD et erreur](preuves-json/activity-rrd-net-2024-10-12_29-get.json) |
| Recherche d’historique administratif | [Réponse GET authorize](preuves-json/activity-login-authorize.json), [réponse GET session](preuves-json/activity-login-session-get.json) |
| Stockage et partages | [Disque](images/freebox-7.png), [explorateur](images/freebox-8.png), [FTP](images/freebox-21.png), [SMB](images/freebox-22.png), [partage macOS](images/freebox-23.png) |
| LAN physique et services | [DHCP](images/freebox-18.png), [switch](images/freebox-19.png), [UPnP](images/freebox-20.png), [WPS](images/freebox-17.png) |
| Identités OP-01, caméras et SMB | [Recoupements détaillés](../investigations/20261017-recroisements/compte-rendu.md), [identité OP-01](../investigations/20261017-recroisements/resultats/recoupements-v2/op01-freebox-identite.json), [deux échecs SMB](../investigations/20261017-recroisements/resultats/recoupements-v2/smb-26mars2024.json) |
| Téléphones et limites d’attribution | [Rapprochements des sauvegardes](../investigations/20261110-telephones/compte-rendu.md), [hypothèses avant ouverture](../investigations/20261110-revue-intervention-scelles/compte-rendu.md), [rapport TP-02](../telephones/analyse-TP-02.md) |
| Caméras et réseau ASUS | [Précisions de contexte](../investigations/20261019-retour-cliente/compte-rendu.md), [modèles et firmwares](../investigations/20261109-identification-cameras/compte-rendu.md), [ASUS sur OP-01](../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/compte-rendu.md) |

Les réponses brutes référencées ne contiennent pas les jetons de session. Les captures et pièces de recoupement conservent le détail des valeurs ; leur lecture ne constitue pas une nouvelle acquisition de la Freebox. Les versions et empreintes historiques des rapports concernent leurs textes respectifs, pas une signature du présent document.

### 12.2. Termes techniques

| Terme | Sens dans ce rapport |
|---|---|
| LAN / WAN | Réseau local / liaison extérieure. Une présence LAN ne décrit pas le trafic Internet ou les actions de l’appareil. |
| MAC / MAC privée | Adresse d’interface / adresse pouvant varier ou être administrée localement. Elle n’est pas une identité de personne. |
| IPv4 / IPv6 link-local | Protocoles d’adressage / adresse IPv6 à portée du lien local. L’absence d’IPv4 n’implique pas absence de communication IP. |
| SSID / BSSID | Nom Wi-Fi / adresse du point d’accès, distincts de la MAC cliente d’un iPhone. |
| DHCP / mDNS / WSD | Attribution d’adresses / annonce de noms / découverte de services. Leurs noms ne certifient pas un propriétaire. |
| NAT, redirection, DMZ | Mécanismes IPv4 pouvant exposer des services internes. Leur état présent ne retrace pas les ouvertures supprimées. |
| UPnP IGD | Fonction permettant aux équipements de demander des redirections de ports ; activation du service et redirection effective sont deux constats distincts. |
| SMB / VPN | Partage de fichiers / tunnel réseau. Leur disponibilité ou configuration ne prouve pas un usage effectif par une identité. |
| RRD | Statistiques agrégées de ressources ou de connexion, pas un journal détaillé de chaque flux ou MAC. |
| `first_activity` / `last_activity` | Valeurs encore conservées dans une fiche, pas des bornes garanties de première utilisation ou de connexion continue. |

### 12.3. Références de formats

La documentation Freebox des interfaces [LAN](https://dev.freebox.fr/sdk/os/lan/), [Wi-Fi](https://dev.freebox.fr/sdk/os/wifi/) et [RRD](https://dev.freebox.fr/sdk/os/rrd/) décrit les champs et compteurs utilisés. Les constats propres à cette Freebox reposent sur les réponses et captures conservées ; la documentation générale ne fournit pas son historique de 2024.

## 13. Inventaire des fiches ayant une trace antérieure au 29 octobre 2024

Le tableau reprend les **56 fiches** de l’inventaire de référence, avec leurs noms API, y compris lorsqu’un rattachement matériel est établi ailleurs dans le rapport. Les dates sont les **minimum et maximum encore présents avant la limite** dans les champs examinés ; elles ne sont pas les premières/dernières connexions réelles garanties. Les valeurs de joignabilité et d’activité peuvent différer de quelques secondes et les intervalles ne prouvent pas une continuité.

« Détection seulement » signifie **sans connectivité IP encore datée avant la limite**, pas absence de toute IP à toute époque. Les identifications et réserves des sections 6 à 9 restent applicables.

| Adresse MAC | Nom principal API | Première trace retenue | Dernière trace retenue avant la limite | Nature avant la limite |
|---|---|---|---|---|
| `A0:9D:C1:D1:B9:73` | android-d7cace0bd4fdd799 | 26/03/2022 23:56:24 | 29/03/2022 19:52:21 | IP effective |
| `B6:BD:59:D2:25:62` | — | 05/04/2022 21:37:27 | 02/05/2022 21:19:52 | IP effective |
| `10:8E:E0:58:1E:04` | Galaxy-Tab-A-8 | 06/04/2022 10:58:11 | 08/04/2022 13:47:48 | IP effective |
| `A6:0D:19:D5:05:58` | Galaxy-S20 | 06/04/2022 11:39:23 | 09/04/2022 19:58:53 | IP effective |
| `14:94:6C:65:5B:E8` | iPhone | 07/07/2022 18:54:10 | 07/07/2022 19:01:18 | IP effective |
| `56:96:03:FB:28:58` | — | 07/07/2022 19:00:35 | 07/07/2022 19:21:38 | IP effective |
| `3E:2B:7F:22:80:52` | 84b3bd87-59c0-4279-9cc4-643bbb2a7b6a | 07/07/2022 19:21:39 | 07/07/2022 19:21:44 | IP effective |
| `B0:22:7A:5F:5C:A9` | HPB0227A5F5CA8 | 13/08/2022 06:45:51 | 19/07/2024 22:16:55 | IP effective |
| `D6:58:E4:04:CA:0D` | S22-de-Cherifa | 18/08/2022 19:33:19 | 09/09/2023 23:37:57 | IP effective |
| `E6:E1:90:ED:E4:94` | — | 11/10/2022 16:24:30 | 11/10/2022 16:24:30 | détection seulement |
| `F2:D1:B4:69:51:D8` | — | 15/10/2022 05:52:22 | 01/02/2023 04:30:42 | IP effective |
| `36:6E:8E:DF:A3:3D` | ecb906e6-22e3-4cd1-996b-f1e9df24eedb | 01/12/2022 13:32:21 | 07/12/2022 11:38:55 | IP effective |
| `DA:10:04:69:3E:56` | iPhonedeDoudou | 03/12/2022 23:46:45 | 14/12/2023 23:42:25 | IP effective |
| `26:30:27:16:9F:92` | iPhone-2 | 08/12/2022 19:56:56 | 04/03/2024 14:04:23 | IP effective |
| `C0:D0:12:70:F6:F8` | iPhonedconseils | 10/12/2022 19:32:21 | 10/12/2022 21:55:21 | IP effective |
| `50:E0:85:63:41:5B` | LAPTOP-RMCOB2VU | 13/01/2023 10:15:08 | 23/07/2024 15:37:02 | IP effective |
| `54:EF:33:08:86:DF` | Android | 27/01/2023 22:29:56 | 19/02/2024 17:48:31 | IP effective |
| `F4:CA:E5:6A:25:89` | Freebox Player | 24/02/2023 00:41:50 | 19/07/2024 22:46:42 | IP effective |
| `52:60:FA:6C:6A:8C` | — | 24/03/2023 15:11:22 | 24/03/2023 15:11:22 | détection seulement |
| `3C:91:80:72:50:55` | LAPTOP-9UHPONKK | 29/03/2023 10:09:50 | 11/03/2024 15:17:29 | IP effective |
| `F8:28:19:77:42:71` | LAPTOP-205Q5H9C | 20/05/2023 19:02:43 | 26/03/2024 15:48:20 | IP effective |
| `7E:3D:31:A2:03:8C` | iPhone-33 | 17/06/2023 22:29:21 | 20/06/2023 00:40:17 | IP effective |
| `CC:8C:BF:8E:33:8A` | — | 20/06/2023 16:36:00 | 20/06/2023 16:36:00 | détection seulement |
| `C4:3C:B0:23:34:46` | — | 10/07/2023 16:13:21 | 10/07/2023 16:13:21 | détection seulement |
| `04:BA:8D:74:86:3A` | SM-J260F | 31/07/2023 14:49:10 | 31/07/2023 18:01:53 | IP effective |
| `72:4E:33:8A:6E:D5` | iPad-de-Gregory | 10/08/2023 00:39:31 | 10/08/2023 00:44:31 | IP effective |
| `86:D5:17:EE:D8:70` | Apple-Watch | 10/08/2023 01:02:02 | 10/08/2023 01:08:56 | IP effective |
| `E0:5F:45:73:03:3C` | iPhone | 14/08/2023 12:13:41 | 25/06/2024 02:36:34 | IP effective |
| `7C:A1:AE:B3:34:F9` | iPhonedeMalika | 16/08/2023 01:21:40 | 16/08/2023 13:17:10 | IP effective |
| `DE:98:33:8D:2C:A2` | — | 16/08/2023 17:05:18 | 11/12/2023 10:19:39 | IP effective |
| `84:AB:1A:E4:7A:BD` | iPhone | 21/09/2023 18:47:38 | 11/06/2024 13:57:02 | IP effective |
| `82:B1:82:5C:17:AC` | 57bfdd94-60cf-4bf0-87b0-0624b3f3f22d | 21/09/2023 20:09:53 | 11/12/2023 10:17:35 | IP effective |
| `1C:90:FF:9D:B8:4A` | wlan0 | 15/11/2023 13:51:18 | 15/11/2023 13:51:18 | détection seulement |
| `CC:8C:BF:08:23:84` | wlan0 | 15/11/2023 14:19:31 | 15/11/2023 14:19:31 | détection seulement |
| `2C:C3:E6:98:A4:2F` | — | 02/12/2023 18:07:47 | 02/12/2023 18:07:47 | détection seulement |
| `36:D0:F6:73:99:C7` | Apple-Watch | 12/12/2023 01:31:31 | 14/12/2023 21:12:08 | IP effective |
| `1E:A6:37:ED:10:7D` | Apple-Watch | 14/12/2023 21:15:26 | 19/12/2023 17:24:27 | IP effective |
| `D2:2E:29:52:CB:BD` | 2d4183c8-3c55-4589-85e2-805498ce616e | 18/01/2024 19:15:56 | 11/06/2024 13:51:21 | IP effective |
| `4E:B5:4A:B0:3F:04` | — | 21/01/2024 13:20:29 | 21/01/2024 13:20:29 | détection seulement |
| `70:70:AA:0D:EC:11` | android2-home | 21/01/2024 18:54:04 | 19/02/2024 17:49:14 | IP effective |
| `0E:A1:33:FB:02:46` | iPhone | 26/01/2024 19:48:37 | 26/01/2024 19:48:37 | détection seulement |
| `A6:14:3E:8A:34:ED` | 158742fd-de6e-43df-98be-e440d29c2673 | 04/03/2024 23:14:41 | 02/05/2024 13:00:02 | IP effective |
| `16:E8:85:01:02:FD` | — | 02/05/2024 12:50:13 | 02/05/2024 12:50:13 | détection seulement |
| `B2:D2:80:8B:78:FD` | 3f194c23-a33b-407a-b571-27f9475d7f83 | 25/05/2024 20:53:04 | 18/08/2024 14:44:12 | IP effective |
| `08:87:C7:76:C4:10` | iPhone | 11/06/2024 13:12:32 | 11/06/2024 14:00:33 | IP effective |
| `1A:4E:FD:7E:44:35` | 1f159da5-72f3-4ea3-995c-e2b6c48a7966 | 11/06/2024 13:33:43 | 11/06/2024 13:38:29 | IP effective |
| `CE:04:84:BC:D2:4D` | — | 11/06/2024 14:00:54 | 11/06/2024 14:25:49 | IP effective |
| `0E:41:84:EF:66:27` | iPhone | 11/06/2024 14:27:30 | 11/06/2024 14:27:30 | détection seulement |
| `E0:A2:5A:0D:06:DF` | mxiang-camera-mwc10_miap06DE | 19/07/2024 21:02:44 | 19/07/2024 21:02:44 | détection seulement |
| `E0:A2:5A:0A:A3:F7` | — | 19/07/2024 21:02:47 | 19/07/2024 21:02:47 | détection seulement |
| `98:AA:FC:13:18:93` | STARVOX-98AAFC131893 | 19/07/2024 22:16:11 | 19/07/2024 22:16:11 | détection seulement |
| `96:8F:D6:BB:47:D7` | iPhone | 12/10/2024 23:15:06 | 12/10/2024 23:15:06 | détection seulement avant la limite |
| `EA:21:6C:F7:47:E7` | iPhone | 16/10/2024 00:20:00 | 17/10/2024 00:57:02 | IP effective |
| `AC:ED:5C:DA:47:74` | DESKTOP-ICPNCMD | 16/10/2024 21:27:48 | 16/10/2024 23:25:55 | IP effective |
| `9C:64:8B:0A:BD:0C` | iPhone | 17/10/2024 01:00:57 | 17/10/2024 03:43:56 | IP effective |
| `FE:AA:76:95:AC:29` | iPhone | 17/10/2024 03:45:44 | 17/10/2024 03:45:44 | détection seulement avant la limite |
