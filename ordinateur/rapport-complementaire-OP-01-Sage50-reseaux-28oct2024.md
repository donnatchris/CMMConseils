# OP-01 — Rapport complémentaire : Sage 50 et connexions réseau du 28 octobre 2024

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine / DMM Conseils  
**Équipement :** OP-01, ASUS UX333F, série `KAN0CV116290436` ; nom Windows `LAPTOP-RMCOB2VU`  
**Date des recherches complémentaires et du rapport :** 13 novembre 2026  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Nature :** analyse technique complémentaire de l’image disque ; rapport autonome, sans modification des rapports antérieurs.

## 1. Réponses aux trois questions

| Question | Résultat | Limite essentielle |
|---|---|---|
| Où sont les données Sage 50 sur le disque ? | Six fichiers `CDMDATA` existent sous **`C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\`**, dans les dossiers ALMU, BANMAT, DMM CONSEILS, FINT, MY LITTLE MARKET et RCT. | Ces stockages locaux doivent être distingués du dossier distant Sage « Données Mobiles » référencé par les alias. Leur présence ne certifie ni leur complétude ni leur état exact en 2024. |
| Existe-t-il des traces d’authentification ou de licence le 28 octobre ? | **Oui.** Le journal natif enregistre un échange avec le service de souscription à **15:10:30–31**, puis une requête **`POST id.sage.com/oauth/token` à 15:11:48**, suivie du résultat **200 à 15:11:49**. | Le journal établit la requête et son résultat déclaré ; il ne conserve pas le corps de réponse, l’adresse électronique, le mot de passe ou le type d’octroi OAuth. Une saisie manuelle d’identifiants et une attribution à une personne ne sont pas démontrées. |
| À quels réseaux le PC a-t-il été connecté ? | Les profils **« Réseau 2 »** puis **« Réseau 3 »** sont enregistrés sur des interfaces de type **Ethernet**, avec une capacité Internet signalée par Windows. Les événements USB/RNDIS étayent fortement un **partage de connexion USB d’un appareil Samsung**, série **`R58RB2ETQER`**. | Le rapprochement Samsung repose sur plusieurs événements concordants ; la correspondance persistante directe entre chaque GUID d’interface opérationnelle et le numéro de série USB n’est plus disponible. Aucun propriétaire, opérateur mobile, réseau amont ou IP publique n’est établi. |

**Aucune connexion Wi-Fi à `ASUS_Z01RD` n’est établie sur OP-01 le 28 octobre 2024.** Le journal Wi-Fi conserve ce jour-là une déconnexion de `Freebox-537E9F` au réveil du PC, sans association Wi-Fi réussie ultérieure pendant la journée civile française. La connexion Freebox suivante conservée est le **29 octobre à 00:02:25**, hors de la journée demandée.

Les heures de cette synthèse sont celles de Paris. Les précautions horaires et la différence entre connexion Ethernet logique et câble réseau physique sont détaillées ci-dessous.

## 2. Objet, sources et préservation

La demande porte sur l’emplacement local des données Sage 50, ses traces d’authentification ou de souscription et les connexions réseau d’OP-01 le **28 octobre 2024**. La déclaration de la cliente selon laquelle l’ouverture exige Internet et des identifiants Sage est un élément à vérifier, et non une preuve autonome d’une authentification particulière.

L’examen a été réalisé par SSH sur la VM `sift`, à partir des 74 segments `OP01.E01` à `OP01.E74`, situés dans `/media/shared/forensic/SADEDINE-2026/OP-01/`. L’image a été remontée avec la chaîne :

```text
EWF → ewfmount → /dev/loop16, RO=1 → BitLocker / dislocker -r
    → /mnt/windows, montage NTFS ro,norecover
```

Le contrôle initial et le contrôle final confirment la lecture seule du volume Windows et du périphérique loop. Les fichiers de travail ont été écrits dans un nouveau dossier SIFT, puis rapatriés dans [le dossier de preuves et résultats de cette recherche](recherche-OP-01/sage-reseaux-20261113/). Aucun programme Sage issu de l’image n’a été lancé ; aucune connexion à un compte Sage ni aux URL trouvées dans les journaux n’a été effectuée.

Le partage hébergeant les segments EWF est monté en écriture : la protection constatée concerne la chaîne de lecture, et ne constitue pas un verrouillage des fichiers d’acquisition sur leur stockage. L’empreinte du flux disque annoncée à l’acquisition est `0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484` ; elle n’a pas été recalculée intégralement lors de ce complément.

L’examen comprend :

- **359 journaux EVTX, 275 577 enregistrements alloués**, dont **6 072** dans la journée civile française du 28 ; recherche des références Sage/Ciel et des identifiants réseau ;
- l’inventaire de **8 982 fichiers** des arborescences Sage/Ciel examinées, le journal natif `Standard.SgLog`, les alias et les métadonnées des données ;
- les clés réseau et Sage des ruches SYSTEM, SOFTWARE et NTUSER du profil `fintm`, ainsi que les noms de **65 profils Wi-Fi XML**, sans extraction de leurs clés de sécurité ;
- les sections SetupAPI du 28, les traces Prefetch et les journaux ETL de configuration réseau disponibles ;
- un balayage de la MFT : **1 046 016 emplacements**, avec **147 entrées ciblées** Sage/ETL, dont **135 allouées et 12 non allouées**.

La MFT présente le SHA-256 `4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b`, identique à celui du précédent inventaire NTFS du dossier. Cela confirme la concordance de ce fichier de référence ; ce n’est pas une nouvelle vérification de tous les segments EWF.

Les extractions EVTX principales n’ont signalé aucune erreur. Les **19 copies locales** des pièces retenues ont été contrôlées par SHA-256. Les **65 événements essentiels** de NetworkProfile, WLAN, NCSI, Application et System ont également été relus avec un second décodeur, distinct de libevtx. Les limites de ce contrôle figurent en section 8.

## 3. Convention horaire et correction de l’horloge

La journée recherchée est **`[2024-10-27T23:00:00Z ; 2024-10-28T23:00:00Z[`**. Le 28 octobre, Paris est en **UTC+1**, après le changement d’heure du 27. Un événement à `2024-10-28T23:02:25Z` appartient donc au **29 octobre à 00:02:25 à Paris**.

Les EVTX conservent les heures UTC. Le journal Sage et SetupAPI utilisent des heures sans suffixe de fuseau. Leur lecture en heure locale est corroborée notamment par :

- le début du processus WGC à **14:10:12.609476 UTC**, soit **15:10:12 à Paris**, suivi des premières requêtes Sage à **15:10:19** ;
- la modification de l’alias ALMU à **14:12:18.990852 UTC**, soit **15:12:18**, après l’échange d’authentification ;
- l’échec de fin de session Sage à **17:28:57**, à la même seconde locale que les événements Windows de défaillance WGC à **16:28:57 UTC**.

Une correction de l’horloge est conservée dans **System, Kernel-General/1, RecordID 37549** : l’heure passe de `10:19:39.4274816Z` à `10:19:30.1890932Z`, soit un recul d’environ **9,238 secondes**. Les événements Time-Service **37/35, RecordIDs 37547/37550**, rapportent une source `time.windows.com`, adresse distante `51.145.123.29:123`. Cette adresse est celle du serveur de temps déclaré, **pas l’IP publique d’OP-01**.

Les heures antérieures à cette correction sont reproduites telles qu’enregistrées ; elles ne sont pas corrigées silencieusement. Les heures constituent des indications techniques de l’horloge de la machine, sans certification métrologique externe. Voir [les événements d’horloge et réseau System](recherche-OP-01/sage-reseaux-20261113/resultats/systeme-reseau-horloge.json).

## 4. Emplacement des données Sage 50

### 4.1. Programme et fichiers de données locaux

Le journal Application identifie le programme utilisé le 28 :

```text
C:\Program Files (x86)\Ciel\Gestion Commerciale\WGC.exe
Version rapportée : 28.81.0.1201
```

Le dossier d’installation du programme est distinct des fichiers de données. Les six fichiers suivants ont été retrouvés et hachés dans l’image :

| Dossier société | Chemin local complet | Taille en octets | Dernière modification du contenu, UTC |
|---|---|---:|---|
| ALMU | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\ALMU\CDMDATA` | 10 510 459 | 02/10/2026 16:25:47 |
| BANMAT | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\BANMAT\CDMDATA` | 7 560 105 | 13/08/2024 11:06:30 |
| DMM CONSEILS | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\DMM CONSEILS\CDMDATA` | 7 664 869 | 17/06/2024 11:36:32 |
| FINT | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\FINT\CDMDATA` | 8 543 274 | 30/06/2023 14:25:18 |
| MY LITTLE MARKET | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\MY LITTLE MARKET\CDMDATA` | 10 315 198 | 26/05/2023 11:46:44 |
| RCT | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\RCT\CDMDATA` | 8 949 259 | 25/09/2024 11:44:48 |

Ces fichiers portent l’en-tête binaire `CamBFile`. Ils constituent les stockages de données locaux identifiés dans l’environnement Sage/Ciel. Leur structure propriétaire n’a pas fait l’objet d’une reconstruction des tables métier ou d’une validation dans Sage. **Ils ne sont donc pas présentés comme six sauvegardes autonomes, complètes et directement restaurables.** Leurs empreintes intégrales figurent dans [l’inventaire des données Sage](recherche-OP-01/sage-reseaux-20261113/resultats/sage-databases.json).

La recherche MFT retrouve les mêmes chemins. Les fichiers `.SgWgc` alloués identifiés sont des modèles et sociétés exemples du logiciel ; aucune base métier locale classique `ALMU.SgWgc`, `RCT.SgWgc` ou `DMM CONSEILS.SgWgc` n’a été identifiée par cette recherche de noms. Les douze correspondances non allouées sont des alias, dont certains ont des parents MFT non résolus ; elles ne sont pas des bases supplémentaires récupérées.

### 4.2. Référence à des données hébergées

Les trois alias ALMU modifiés le 28 contiennent cette chaîne exacte, décodée en Windows-1252 :

```text
!Srv!<Smart>/S:/Données Ciel/Dossiers/ALMU/Ciel Gestion Commerciale/ALMU.SgWgc
```

Ils se trouvent sous :

```text
C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Alias\
```

| Alias | Modification UTC | Heure de Paris |
|---|---|---|
| `cdm0003ZS - ALMU.SgWgcAlias` | 14:12:18.990852 | **15:12:18** |
| `cdm00040E - ALMU.SgWgcAlias` | 15:00:22.897187 | **16:00:22** |
| `cdm0003ZH - ALMU.SgWgcAlias` | 15:02:48.839341 | **16:02:48** |

Le préfixe de service, les noms CDM, la présence de `CDMDATA` et les requêtes `cws-cdm.sage.fr` sont cohérents avec un usage de **Ciel Données Mobiles**. La documentation Sage décrit ce service comme un hébergement des dossiers sur des serveurs en ligne. Cette documentation explique le mécanisme ; elle ne remplace pas les traces de cette machine. [Sage — Ciel Données Mobiles](https://fr-kb.sage.com/portal/app/portlets/results/viewsolution.jsp?solutionid=210905150095223).

**Le `S:` de cet alias ne doit pas être présenté comme un volume local identifié d’OP-01.** Il s’agit ici d’une référence logique au sein du service. Les chemins `C:\…\CDMDATA` répondent à la question de la présence locale ; la référence `!Srv!<Smart>/S:/…` documente séparément le dossier utilisé via le service. Une récupération certifiée de l’état complet du dossier hébergé en octobre 2024 nécessiterait les données ou archives du service Sage.

### 4.3. Utilisation ALMU le 28

Des modifications concernent aussi les fichiers d’impression du dossier :

```text
C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\ALMU.1296571903\Dernières impressions\
```

`Facture - FA0338.sgdoc` est modifié à **15:18:36 Paris** ; `_sans nom_.sgdoc` à **15:19:21**, puis plusieurs autres impressions entre **15:21:08 et 15:27:06**. Ces éléments corroborent une activité sur le dossier ALMU après l’échange d’authentification enregistré. Ils ne datent pas la création des opérations commerciales ni leur éventuelle modification dans les données métier. L’état actuel de `ALMU\CDMDATA`, modifié en 2026, ne permet pas de reconstituer à lui seul son état au 28 octobre 2024.

## 5. Authentification, souscription et activité Sage

### 5.1. Source native

La source principale est :

```text
C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Logs\Standard.SgLog
```

Taille : **206 815 octets**. SHA-256 :

```text
bc1f1357eed5d58959ae987599110a9379caaaf77de61e36e05ecd0c242271fd
```

Ce fichier conserve **199 lignes datées du 28/10/2024**, numérotées **1824 à 2022** dans le journal décodé. Ses dates NTFS récentes ne signifient pas que toutes ses lignes ont été écrites en 2026 : son contenu conserve une chronologie plus ancienne. Le [relevé intégral des lignes du 28](recherche-OP-01/sage-reseaux-20261113/resultats/sage-log-day.json) permet de vérifier la séquence, et la copie brute est conservée parmi les preuves.

### 5.2. Chronologie utile

| Heure Paris | UTC correspondante | Trace native | Référence / portée |
|---|---|---|---|
| **15:10:12.609476** | 14:10:12.609476 | Création du processus WGC, calculée depuis `ProcessCreationTime=0x01db29431ac2f9b1` | Application/1000, **18857** ; champ rapporté lors de la défaillance de 17:28. |
| **15:10:19–21** | 14:10:19–21 | Test `…TechnicalRepository.svc/Test/Ping/TimeStamp`, résultat **200** | Lignes **1824–1827**. |
| **15:10:21–30** | 14:10:21–30 | Lecture de `ProdLuWS50S_.json`, résultat **200** | **1828–1831** ; consultation de ressource applicative. |
| **15:10:30–31** | 14:10:30–31 | `GET …/ControlSouscription/sls.svc/subgetlogscp`, résultat **200** | **1832–1833** ; communication avec le service de souscription. |
| **15:11:48–49** | 14:11:48–49 | **`POST …id.sage.com/oauth/token`**, résultat **200** | **1834–1836** ; trace centrale de l’échange d’authentification OAuth. |
| **15:11:50–51** | 14:11:50–51 | `GET …cws-cdm.sage.fr/api/v1/CDMSelector/[identifiant numérique]`, résultat **200** | **1837–1839** ; échange CDM suivant immédiatement l’authentification. |
| **15:13:35–37** | 14:13:35–37 | `BeginSession`, `GetActions`, `SendActionsResults`, résultats **200** | **1884–1892**, service `cielws.ciel.com/EST/EST.svc/`. |
| **16:01:41–42 et 16:03:43–44** | 15:01:41–42 et 15:03:43–44 | Autres échanges `GetActions` / `SendActionsResults`, résultats **200** | **1937–1942** et **1987–1992**. |
| **17:04:49–50** | 16:04:49–50 | Lecture de flux de contenu Sage, résultat **200** | **2013–2016** ; accès applicatif réussi encore déclaré avant la déconnexion de 17:14. |
| **17:28:56–57** | 16:28:56–57 | Deux tentatives `EndSession`, résultat **0**, erreur **0x00002EE7** : résolution du serveur impossible | **2017–2022** ; échec de réseau/DNS, et non preuve d’identifiants refusés. |
| **17:28:57–17:29:00** | 16:28:57–16:29:00 | Exception non gérée / défaillance WGC | Application/1026, 1000, 1001 : **18856–18859**. |

Les requêtes sont reproduites selon ce que le logiciel journalise. Le préfixe `http://` présent dans ces lignes ne suffit pas à déterminer les redirections, le chiffrement réellement utilisé sur le réseau ou le contenu transmis.

### 5.3. Ce que l’authentification et la « licence » permettent de conclure

La succession `POST /oauth/token` → résultat 200 → requête CDM avec résultat 200 est un **indice fort d’un échange de jeton abouti et d’un accès au service**. En OAuth, un jeton peut également être obtenu par renouvellement ; le type d’octroi et le corps de réponse sont nécessaires pour distinguer les mécanismes. [IETF — OAuth 2.0, notamment sections 5.1 et 6](https://www.rfc-editor.org/rfc/rfc6749).

Le journal permet donc de dater précisément l’échange, mais **ne démontre pas qu’une personne a saisi l’adresse électronique et le mot de passe à 15:11**. Il ne permet pas d’identifier la personne au clavier, le titulaire du compte utilisé ou une éventuelle réutilisation d’une session. La documentation Sage décrit d’ailleurs une option de maintien de connexion, mais son existence générale ne prouve pas son emploi ce jour-là sur OP-01. [Sage — Authentification automatique Flex](https://fr-kb.sage.com/portal/app/portlets/results/viewsolution.jsp?solutionid=211010160102909), fiche modifiée le 15 novembre 2024.

L’appel au service `ControlSouscription` est une **trace de souscription/licence au sens fonctionnel**. Son résultat 200 confirme le succès HTTP déclaré par le journal, **pas le contenu des droits retournés, une nouvelle activation ou une acquisition de licence**. Le fichier vide `C:\ProgramData\Ciel\Données Communes\AlreadyConnectedOnSageID` existe, mais sa dernière modification est du **2 octobre 2026** ; il n’est pas utilisable comme preuve d’une authentification le 28 octobre 2024.

Enfin, les événements de gestion de l’« Imprimante PDF Sage v5.5 » ne sont pas des événements de licence et ne prouvent pas, à eux seuls, une impression humaine. Les Prefetch WGC encore présents retiennent des dernières exécutions de **2026**, pas celle du 28 ; la datation de cette exécution repose sur le journal natif et les événements de défaillance Windows.

## 6. Réseaux et interfaces du 28 octobre

### 6.1. Connexions établies par NetworkProfile et NCSI

| Heure Paris enregistrée | Profil / interface | Constat et références |
|---|---|---|
| **10:41:56–10:41:59** | `Freebox-537E9F`, Wi-Fi Intel | **Déconnexion** au réveil : NetworkProfile/10001 **7007**, WLAN/8003 **2116** ; ce n’est pas une nouvelle association à la Freebox. |
| **11:18:55–11:18:56** | **Réseau 2**, interface `{01D72DD1-9584-43CE-B52E-BC555D29936A}` | NetworkProfile/4002 **7020**, /10000 **7021**. NCSI/4042 **1760**, puis **1761 à 11:18:56.722328** : capacité IPv4 de 0 à 1, puis **2 (Internet)**. |
| **11:35:44** | Réseau 2 | Déconnexion : NetworkProfile/10001 **7023** ; NCSI **1762** repasse de 2 à 0. |
| **11:35:45–11:35:46** | **Connexion au réseau local 2**, interface `{3FE87BE0-2003-4582-91EC-342B21078FBB}` | Connexion brève : /4002 **7027**, /10000 **7028**, puis /10001 **7029**. Aucun état Internet NCSI retrouvé pour cet épisode. |
| **11:47:31–11:47:32** | **Réseau 3**, interface `{479CF457-AF75-4CDC-8C88-124C0693B5F6}` | NetworkProfile/4002 **7034**, /10000 **7035**. NCSI **1763 à 11:47:32.497755** : capacité IPv4 **2 (Internet)**. |
| **16:27:50** | Réseau 3 | Déconnexion : /10001 **7037** ; NCSI **1764**, capacité de 2 à 0. |
| **16:27:53** | Réseau 3, même interface | Reconnexion : /4002 **7042**, /10000 **7043** ; NCSI **1765 à 16:27:53.817775**, capacité 2. |
| **17:14:11** | Réseau 3 | Déconnexion : /10001 **7045** ; NCSI **1766**, capacité de 2 à 0. |

La chronologie UTC complète et les données des événements sont conservées dans [la sélection réseau du 28](recherche-OP-01/sage-reseaux-20261113/resultats/chronologie-reseau-28oct.json). NCSI renseigne l’évaluation de connectivité de Windows : un changement d’état ne constitue pas une capture de tous les paquets ni une garantie d’accès permanent à chaque service entre deux événements. [Microsoft — Fonctionnement de NCSI](https://learn.microsoft.com/en-us/windows-server/networking/ncsi/ncsi-overview).

Les heures avant 11:19:30 précèdent la correction de l’horloge décrite en section 3. La synchronisation NTP et les résultats applicatifs Sage complètent les indications de NCSI.

### 6.2. Pourquoi il s’agit d’interfaces Ethernet, sans preuve d’un câble RJ45

Le journal **Wcmsvc/Operational** classe explicitement les interfaces concernées dans la liste des connexions **`Ethernet`** : RecordIDs **5491, 5496 et 5500**, à **11:18:55, 11:35:45 et 11:47:31**. Les créations d’interfaces sont également présentes dans les événements **1009**, notamment **5486/5490** pour le premier épisode et **5499** pour Réseau 3 ; les données exactes sont fournies dans [le recoupement par GUID](recherche-OP-01/sage-reseaux-20261113/resultats/network-guid-events.json).

**Ethernet désigne ici une catégorie d’interface Windows. Ce terme ne démontre pas une liaison physique à une prise réseau des locaux.** Un téléphone partageant Internet par USB peut fournir une interface réseau de cette famille. RNDIS est précisément un mécanisme réseau sur USB documenté par Microsoft. [Microsoft — Remote NDIS](https://learn.microsoft.com/en-us/windows-hardware/drivers/network/remote-ndis--rndis-2).

### 6.3. Recoupement avec le partage USB Samsung

Plusieurs sources indépendantes au niveau des artefacts convergent :

1. **11:18:34** : SetupAPI, ligne **45589**, puis Kernel-PnP/Configuration, RecordID **893**, identifient `USB\VID_04E8&PID_6860\R58RB2ETQER`.
2. **11:18:53–54** : SetupAPI, ligne **45747**, décrit `USB\VID_04E8&PID_6863&MI_00\7&95c02d9&0&0000`, parent `USB\VID_04E8&PID_6863\R58RB2ETQER`, avec le pilote **« Remote NDIS based Internet Sharing Device »**, service **`usbrndis6`**. System/7045 **37541** enregistre l’installation de « USB RNDIS6 Adapter ».
3. **11:18:55** : System/NDIS/10317 **37542** nomme cette interface RNDIS avec le GUID `{054B7EF2-DF55-45F0-8CB6-19E42A42EEB3}`. Réseau 2 apparaît dans la même seconde, mais sur le GUID opérationnel distinct `{01D72DD1-…}`.
4. **11:35:43–46** : SetupAPI, lignes **46038** et **46223**, décrit la mise à jour des pilotes du même périphérique. System/7045 **37649** nomme **« SAMSUNG Mobile USB Composite Device Driver (DEVGURU Ver.) »**. La brève connexion « Connexion au réseau local 2 » accompagne cette reconfiguration. System/NDIS/10317 **37651** désigne explicitement son GUID `{3FE87BE0-…}` comme **« Remote NDIS based Internet Sharing Device #2 »**.
5. **11:47:30–32** : reconfiguration du même numéro de série, SetupAPI ligne **46273**, puis apparition de Réseau 3. Le fichier de pilote `Windows\INF\oem161.inf` attribue ces identifiants à **SAMSUNG** et décrit le PID `6863` comme un mode **RNDIS Only**.
6. **17:14:11.399631** : Kernel-PnP/Device Management, événement **1010**, RecordID **1493**, enregistre une opération de retrait concernant `USB\VID_04E8&PID_6863\R58RB2ETQER`. Réseau 3 se déconnecte environ **0,19 seconde après**, à 17:14:11.588420 ; NCSI perd sa capacité Internet à 17:14:11.744032.

Le rapprochement est donc **fortement étayé** : partage USB Samsung configuré, interfaces Ethernet contemporaines, accès Internet, changement de pilote, puis retrait du même périphérique immédiatement suivi de la perte réseau. La simple installation d’un pilote aurait été insuffisante ; c’est l’ensemble de la séquence qui soutient cette interprétation.

La limite doit toutefois rester explicite : **les clés réseau actuellement allouées ne conservent plus l’association directe des deux GUID opérationnels `{01D72DD1-…}` et `{479CF457-…}` à ce numéro de série USB**. Les GUID RNDIS explicitement nommés par NDIS sont `{054B7EF2-…}` et `{3FE87BE0-…}`. Le rapport ne transforme pas ces quatre GUID en une identité technique démontrée sans réserve. Les événements 10317 et les erreurs de démarrage du pilote ne prouvent pas, isolément, que chacune de ces interfaces a fonctionné correctement.

Il n’est pas possible d’établir à partir de ces traces : le propriétaire de l’appareil Samsung, son modèle commercial exact, sa carte SIM, son opérateur, son accès amont par données mobiles ou Wi-Fi, son IP publique, ni la personne ayant activé le partage. Les identifiants **Réseau 2/Réseau 3 ne prouvent pas deux accès Internet physiques distincts** : une reconfiguration du même appareil peut créer plusieurs profils.

### 6.4. Profils du registre, passerelles et Wi-Fi

Le registre SOFTWARE corrobore la création de ces profils le 28, avec des dates SYSTEMTIME sans fuseau explicite cohérentes avec les heures locales des EVTX :

| Profil | Création locale conservée | Dernière connexion conservée | MAC de passerelle mémorisée |
|---|---|---|---|
| Réseau 2 | 11:18:55.962 | 11:18:56.009 | `4A:8D:17:2E:F2:AA` |
| Connexion au réseau local 2 | 11:35:45.737 | 11:35:45.737 | Champ vide |
| Réseau 3 | 11:47:31.921 | 16:27:53.305 | `72:AD:DB:12:18:6D` |

Ces valeurs proviennent de `NetworkList\Profiles` et `NetworkList\Signatures\Unmanaged` ; voir [les profils et dates décodées](recherche-OP-01/sage-reseaux-20261113/resultats/reseau-profils-registre.json). La dernière connexion du registre correspond au dernier rattachement conservé du profil, pas à l’heure de déconnexion.

Les deux adresses sont des **MAC de passerelle**, pas des BSSID Wi-Fi établis. Elles sont localement administrées et ne permettent pas une attribution fiable à une marque ou à une personne par leur préfixe. Elles ne doivent notamment pas être comparées comme des identifiants équivalents aux BSSID `ASUS_Z01RD` relevés sur un autre appareil.

Les **65 profils Wi-Fi XML** et les clés réseau examinés ne contiennent aucun profil `ASUS_Z01RD`. Le journal WLAN, qui conserve **1 325 événements** entre mars 2024 et octobre 2026, ne comporte pour la journée française du 28 que la déconnexion Freebox déjà citée. Sa connexion suivante conservée est le **29 octobre à 00:02:25.768038 Paris**, WLAN/8001 **2122**. Une borne min/max ne garantit pas une conservation continue ; l’absence d’événement ne permet pas d’exclure absolument une connexion dont la trace aurait disparu.

Les fragments `ASUS_Z01RD` retrouvés précédemment dans le fichier d’échange ne sont ni un profil de connexion ni une trace datée du 28. La présente recherche ne permet toujours pas de dater une première connexion d’OP-01 à ce réseau. Voir, pour la nature de ces fragments, le [compte rendu antérieur consacré à ASUS_Z01RD](recherche-OP-01/wifi-ASUS_Z01RD/compte-rendu.md), utilisé comme référence et laissé inchangé.

## 7. Rapprochement Sage / réseau et portée des conclusions

Le processus WGC est créé vers **15:10:12**, et les échanges de souscription puis d’authentification interviennent entre **15:10 et 15:12**. Cette séquence se trouve dans l’intervalle où **Réseau 3 est connecté et où NCSI signale Internet**, de 11:47:32 à 16:27:50. Les requêtes Sage encore réussies à **17:04:50** se situent après la reconnexion de Réseau 3 à **16:27:53** et avant sa déconnexion de **17:14:11**. Les tentatives de fin de session à 17:28 échouent ensuite en résolution de nom.

**L’usage connecté de Sage le 28 octobre est ainsi étayé par ses propres échanges et par les traces réseau Windows.** Le réseau opérationnel nommé par Windows pendant l’authentification est **Réseau 3**, de type Ethernet ; le rapprochement avec le partage USB Samsung décrit ci-dessus est fort. Aucun journal de socket ou paquet conservé n’associe toutefois individuellement la requête OAuth à une interface précise : il s’agit d’un recoupement chronologique, non d’une capture réseau du processus WGC.

Le nom de réseau, le compte Windows `fintm`, les événements Sage et le numéro de série USB ne désignent pas l’opérateur humain. Ces résultats n’établissent ni un accès non autorisé, ni le cadre juridique des opérations, ni la communication d’un mot de passe à l’administration. Ils apportent des horaires et identifiants objectifs à rapprocher des pièces de procédure et, si disponibles, des journaux Sage ou de l’appareil Samsung.

## 8. Limites et vérifications effectuées

L’image a été acquise près de deux ans après les événements et contient des usages et mises à jour ultérieurs. Les données suivantes ne permettent pas de compléter un historique exhaustif de 2024 :

- **Security** : les événements conservés concernent 2026 ; aucun audit Windows complet des authentifications de 2024 n’est disponible dans ce journal. Une authentification Windows ne serait, de toute façon, pas une authentification Sage.
- **SRUM** : l’analyse déjà conservée au dossier ne fournit des lignes réseau que pour septembre–octobre 2026. Les anciennes données d’énergie ne donnent ni SSID ni volumes de transfert réseau de 2024. Voir [le contrôle SRUM antérieur](recherche-OP-01/wifi-ASUS_Z01RD/datation.md) et les tableaux associés du même dossier.
- **DHCP et Wired-AutoConfig** : aucun événement alloué du 28 dans les journaux examinés ne fournit une attribution IP exploitable ou la preuve autonome d’une prise Ethernet physique ; un journal Wired vide n’exclut pas l’Ethernet non authentifié.
- **ETL** : NetSetup conserve des références aux GUID lors de configurations ultérieures, notamment en décembre 2024 ; NetCore contient une liste Ethernet de ces GUID en octobre 2026. Ces événements ne sont pas présentés comme des connexions du 28. La trace fournisseur Intel `WifiDriverIHVSession.etl.002` n’a pas pu être décodée avec le lecteur employé : aucun résultat négatif exhaustif n’en est tiré.
- **Sage** : aucun corps de requête/réponse, secret d’authentification ou journal serveur n’est utilisé pour prouver une saisie d’identifiants. L’option de renouvellement de jeton reste indéterminée. La présence de fichiers locaux ne certifie pas le contenu historique complet des données hébergées.

La vérification indépendante porte sur les **RecordID, EventID, heures et champs textuels utiles**, notamment noms de profils, SSID et capacité NCSI. Les heures des deux lecteurs concordent à quelques microsecondes près, sans impact sur les horaires à la seconde exposés ici. Les représentations textuelles de GUID du lecteur secondaire présentent une différence d’ordre des octets ; elles ne sont pas utilisées pour établir les correspondances de GUID de ce rapport. Le lecteur secondaire parcourt aussi des enregistrements supplémentaires de chunks NCSI ; son décompte brut n’est pas assimilé au nombre d’événements alloués exposé en section 2.

Les fichiers [de vérification des transferts](recherche-OP-01/sage-reseaux-20261113/resultats/verification-transfert.json) et [de décodage indépendant](recherche-OP-01/sage-reseaux-20261113/resultats/verification-decodeur-independant.json) détaillent ces contrôles. Les heures et les conclusions ne sont pas fondées sur les références ETL non décodées.

## 9. Pièces techniques et reproductibilité

Tous les nouveaux travaux sont regroupés sous :

```text
ordinateur/recherche-OP-01/sage-reseaux-20261113/
```

| Pièce | Contenu |
|---|---|
| [Résumé de collecte](recherche-OP-01/sage-reseaux-20261113/resultats/summary.json) | Périmètre, décomptes et absence d’erreur du lecteur EVTX principal. |
| [Journal Sage du 28](recherche-OP-01/sage-reseaux-20261113/resultats/sage-log-day.json) | Les 199 lignes avec leur numéro dans le journal natif. |
| [Bases Sage locales](recherche-OP-01/sage-reseaux-20261113/resultats/sage-databases.json) | Chemins, tailles, en-têtes et SHA-256 des six `CDMDATA`. |
| [Entrées MFT ciblées](recherche-OP-01/sage-reseaux-20261113/resultats/mft/mft-target-records.jsonl) | Métadonnées SI/FN, chemins reconstruits, allocation et enregistrements sources. |
| [Sections SetupAPI du 28](recherche-OP-01/sage-reseaux-20261113/resultats/setupapi-day-blocks.json) | Sections complètes et numéros de première ligne. |
| [Événements réseau avec contexte](recherche-OP-01/sage-reseaux-20261113/resultats/network-events.json) | Données et XML des événements sélectionnés. |
| [Recoupement des GUID et du numéro USB](recherche-OP-01/sage-reseaux-20261113/resultats/network-guid-events.json) | Recherche ciblée dans les 359 EVTX. |
| [Profils Wi-Fi sans secrets](recherche-OP-01/sage-reseaux-20261113/resultats/wifi-profiles-sans-secrets.json) | Noms, paramètres non secrets et empreintes des XML. |
| [Sources principales](recherche-OP-01/sage-reseaux-20261113/resultats/sources.json), [complément Sage](recherche-OP-01/sage-reseaux-20261113/resultats/complement-sources.json), [complément réseau](recherche-OP-01/sage-reseaux-20261113/resultats/reseau-complement-sources.json), [fin de collecte](recherche-OP-01/sage-reseaux-20261113/resultats/fin-sources.json) | Chemins sources et empreintes ; seule la sélection probante a été rapatriée en copie brute locale. |
| [Preuves brutes sélectionnées](recherche-OP-01/sage-reseaux-20261113/preuves/) | Journaux EVTX, Sage, SetupAPI, INF, Prefetch et ETL. |
| [Manifeste SHA-256](recherche-OP-01/sage-reseaux-20261113/manifest-sha256.json) | Empreintes des fichiers du nouveau dossier de recherche. |
| [Scripts](recherche-OP-01/sage-reseaux-20261113/scripts/) | Montage en lecture seule, collecte, sélection MFT, analyse ETL et vérifications. |

Outils principaux : Python 3, `pyevtx/libevtx`, `pyregf`, `pyscca`, lecture binaire NTFS avec contrôle des fixups, `dissect.eventlog` **3.11** et `dissect.etl` **3.14**. Les lectures ETL sont détaillées dans [leur résumé](recherche-OP-01/sage-reseaux-20261113/resultats/etl-summary.json) et [leurs limites de décodage](recherche-OP-01/sage-reseaux-20261113/resultats/etl-errors.json). Les références documentaires Sage et Microsoft ont été consultées le 13 novembre 2026 ; elles expliquent les mécanismes sans certifier la configuration historique de la machine.

Le rapport répond aux trois demandes sur les traces accessibles. Les points restant indéterminés — identité du compte et de l’opérateur, droits de licence retournés, réseau amont du Samsung, association directe des GUID opérationnels et historique Wi-Fi exhaustif — ne doivent pas être présentés comme établis.
