# Analyse de la Freebox Révolution

- **Matériel examiné** : Freebox Révolution du domicile de Mme Sadedine
- **Début de l’analyse** : 16 septembre 2026 à 07:38:38
- **Remarques** : L’analyse a été réalisée à distance via l’interface **Freebox OS**. Les informations présentées ci-dessous reflètent l’état de la Freebox et de la connexion Internet au moment du constat.

---

## Accès à distance

L’accès à distance à l’interface **Freebox OS** a été activé par Mme Sadedine le **15 septembre 2026 à 12h27** pour me permettre d'explorer l'interface. Cette activation a été confirmée par un message affiché sur l’écran de la Freebox, indiquant que l’accès à distance était désormais disponible.

### État antérieur

Au moment du constat, l’option « Activer l’authentification par mot de passe » permettant l’accès distant à l’interface Freebox OS n’était pas activée. Les ports d’accès distant HTTP et HTTPS étaient néanmoins configurés. L’interface indique par ailleurs que l’accès distant demeure possible pour les applications autorisées et les liens de partage.

![État antérieur de la Freebox avant l'activation de l'accès à distance](images/freebox-1.jpeg){ width=50% }

### Activation de l’accès à distance

Mme Sadedine m'a remis l'**adresse de connexion à distance**, ainsi que le **mot de passe** associé, afin que je puisse accéder à l’interface **Freebox OS** pour effectuer l’analyse.

**Il faudra désactiver l’accès à distance et modifier le mot de passe après la fin de l’analyse**, afin de sécuriser l’accès à la Freebox et de protéger les informations personnelles de Mme Sadedine.

![Activation de l’accès à distance sur la Freebox](images/freebox-2.jpeg){ width=50% }

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
