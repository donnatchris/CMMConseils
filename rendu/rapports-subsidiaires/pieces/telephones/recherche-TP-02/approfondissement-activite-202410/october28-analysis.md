# TP-02 — 28 octobre : traitements, messages et interfaces

Dates Paris UTC+01. L’ouverture à 10:22 et la restitution à 19:20 sont des déclarations, à vérifier par PV. La chronologie conserve les valeurs UTC et brutes. Les identifiants fileID et empreintes se trouvent dans `timeline-correlated.csv` ; les pièces détaillées sont citées ci-dessous.

## Résultat principal nouveau : les transactions Photos séparent plusieurs mécanismes

`Photos.sqlite` conserve `ATRANSACTION`, `ATRANSACTIONSTRING` et `ACHANGE`, non étudiées dans le précédent rapport. Les colonnes texte de `ATRANSACTION` sont souvent NULL ; les noms se retrouvent en joignant **ZAUTHORTS, ZBUNDLEIDTS, ZCONTEXTNAMETS et ZPROCESSIDTS** aux clés de `ATRANSACTIONSTRING`. Une simple lecture des colonnes texte aurait masqué les contextes.

345 transactions sont datées dans la période centrale, dont **343 le 28 octobre**, entre 12:26:15 et 17:32:00 environ. Leurs changements, entités, clés primaires et masques de colonnes sont dans `photos-transaction-correlations.json`. Ce sont des changements de magasin persistant, pas autant d’actions humaines. Apple décrit la [transaction d’historique Core Data](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction) comme un ensemble de changements de sauvegarde de contexte ou d’opération par lot. Les champs author/context sont applicatifs, sans identification d’une personne.

## Corrélation des séquences

| Heure Paris | Fait vérifié | Interprétation et contre-hypothèse |
|---|---|---|
| 11:39:27 | `CKStartupTime=1730111967` dans iBooks et `com.apple.bookdatastored.plist` | Deux états du même service Books ; ne date pas un boot iPhone ni une lecture de livre |
| 11:57:22 puis 12:01:56 | Création Santé différée et lot de 24 intervalles | Reprise/calcul ou import possibles ; ce sont des créations d’objets, distinctes des périodes représentées |
| 12:01:32–45 ; 12:01:49 | Intervalle pas/distance puis découverte Wi-Fi | Compatible avec transport et activité réseau ; aucune action tactile nécessaire |
| 12:03–12:46 | Trois SMS et champs de lecture | État lu conservé ; l’appareil et le mécanisme de marquage restent indéterminés |
| 12:26:29 | Diagnostic WidgetKit | Activité technique ; pas de déclenchement humain établi |
| 12:27:17–12:29:43 | Transactions de nettoyage, récupération d’état cloud et partages Photos | Causes automatiques explicitement nommées dans les contextes |
| 12:31:21 ; 14:32:37 | Associations Wi-Fi | Compatibles avec reconnexion système ; propriétaire/opérateur non identifié |
| **13:36:10–14** | Séquence SpringBoard puis ScreenshotServicesService | Indice spécifique d’une opération de capture d’écran dans la bibliothèque source ; beaucoup plus informatif qu’une simple date ZDATECREATED |
| **17:31:44** | Travail LocalVideoKeyFrameRecipe relié au même actif que la miniature | Génération de ressource établie ; visionnage de la vidéo non établi |
| **17:31:58 ; 17:32:00** | Deux transactions « PhotoKit changes: com.apple.mobileslideshow (Photos) » | Requêtes attribuées au client Photos ; interaction compatible, ouverture au premier plan non prouvée |
| 17:39:17 | Cache du panneau LSC et fichiers de ressources | Chargement/actualisation compatible avec un affichage ou préchargement ; aucun événement de lecture de flux daté |
| 17:39:47–17:41:22 ; 17:40:50 | Intervalle Santé et métadonnées AppConfig Xiaomi | Activités proches ; pas de relation causale démontrée entre mouvement, panneaux et caméra |

Les transactions de Photos de la journée contiennent **277 contextes mediaanalysisd-service, 42 photoanalysisd**, 11 « moment library », trois CPL, cinq contextes de maintenance/récupération, un SpringBoard, un ScreenshotServices, un travail de miniature et deux Photos. La majorité se prête donc à une explication automatique directe par les noms conservés. Ces noms ne prouvent pas l’exhaustivité des déclencheurs.

## SMS : champs et contexte de clavier

`sms-input-details.json` conserve les seules colonnes techniques des messages 74688–74690 : tous `service=SMS`, `version=10`, `is_from_me=0`, `is_read=1`, `is_finished=1`, `is_delivered=1`, `date_delivered=0`, `ck_sync_state=1`, `did_notify_recipient=0`. `version=10` est une valeur de ligne, pas la preuve que le téléphone exécutait iOS 10. L’acquisition sous iOS 18.5 peut conserver un schéma migré depuis 2024.

Les délais date→date_read sont **4.043459072, 1.821332992 et 2.173361152 secondes**. Les nanosecondes Apple entières sont préservées ; l’affichage est limité à la microseconde. Un champ de lecture entrant représente ici un état local de base ; ce n’est pas un accusé de lecture SMS envoyé au correspondant. Apple précise que les [accusés de lecture ne sont pas supportés en SMS](https://support.apple.com/en-ca/guide/personal-safety/-ipsdccb7919d/web).

La date du clavier **12:03:18.492020** précède le premier `date_read` de **302.316 ms**, avec un écart de **3.741143 s** après la réception. La clé est un `ID_CK_…_SETTIME` de `UITextInputContextIdentifiers.plist` ; sa valeur associée est une préférence de mode/langue, pas du texte saisi.

**Test nouveau :** aucun rapprochement n’a été trouvé parmi **12 956 SHA-1 candidats** calculés sur les colonnes chat_identifier/guid/group_id/original_group_id et handle.id/uncanonicalized_id en UTF-8/UTF-16LE. Cette dérivation n’est pas validée comme celle d’Apple : l’échec exclut seulement les formes testées. Le contexte n’est donc **pas relié à ces trois messages** par ce test. De plus, 74689 et 74690 n’ont aucune jointure conservée dans `chat_message_join` ; seul 74688 est rattaché au chat 1063, dont le dernier timestamp de lecture actuel est ultérieur. Voir `input-context-linkage-test.json`.

Apple documente [Messages in iCloud](https://support.apple.com/en-ie/guide/security-pdf/sec2c21e7f49/1/web/1) et le partage de l’historique entre appareils. `ck_sync_state=1` est retenu brut, sans lui attribuer un sens exclusif non validé. Un état de lecture peut être transporté par synchronisation/restauration ; le chemin exact d’écriture de `date_read` dans cette version n’a pas été obtenu. Une application déjà ouverte, une commande « marquer lu », un autre appareil et un état restauré restent à départager. Aucun test ici ne démontre qu’une simple notification reçue remplit automatiquement `date_read`. Inversement, `did_notify_recipient=0` ne prouve pas qu’aucune notification n’a existé en 2024.

**Bilan :** réception et état lu vérifiés ; consultation locale probable seulement sous hypothèse de continuité de l’installation et d’origine locale des mises à jour. La proximité du clavier soutient une investigation, sans preuve de saisie, de déverrouillage ou d’auteur. Journaux Messages/SpringBoard/UI ou acquisition contemporaine seraient nécessaires pour trancher.

## Photos : faits plus spécifiques et limites

À **13:36:10.800948**, transaction **117456**, contexte `PhotoKit changes: com.apple.springboard (SpringBoard)`, changements de type brut 0 pour Asset 23769, AdditionalAssetAttributes 23769 et les ressources associées. À **13:36:14.432556**, transaction **117461**, contexte `com.apple.ScreenshotServicesService`, changements de type brut 1 sur le même actif. Des transactions CPL et moment library encadrent la séquence à la seconde près. La correspondance 0/1 avec insertion/mise à jour est cohérente avec l’[énumération Core Data](https://developer.apple.com/documentation/coredata/nspersistenthistorychangetype?language=objc) ; les codes bruts sont conservés.

L’actif 23769 **n’existe plus dans ZASSET actuel**. Son historique garde ensuite une transaction cloud entrante le 29/10 à 10:05:52, puis un changement brut 2 sous `PLExpiredCleanupMaintenanceTask` le **29/11/2024 à 02:21:38** (transaction 124593). Cela explique pourquoi l’analyse des seules lignes d’actifs actuelles ne retrouvait pas cette opération. La purge conservée ne date pas le geste initial de mise à la corbeille et n’en donne pas le motif. Aucune récupération d’image ni interprétation de son contenu n’a été faite.

À **17:31:44.885448**, transaction **117587**, contexte `PLPrimaryResourceDataStoreLocalVideoKeyFrameRecipe _runNextJob`, `ACHANGE` vise **Asset 23729** et **InternalResource 85746**. Asset 23729 correspond exactement à `IMG_1773.MP4`, dont le chemin de miniature est daté à la seconde 17:31:44 dans MBFile. **Le lien entre le travail interne et la miniature est donc vérifié**, au-delà d’une simple concordance horaire. La date CPL de rappel 17:31:38.131411 le précède de 6.754037 s ; son lien causal n’est pas démontré.

À **17:31:58.026875 et 17:32:00.403479**, transactions **117588–117589**, contextes attribués à Photos, changement sur **AdditionalAssetAttributes 23703** : il s’agit d’un **autre actif que la vidéo 23729**. La valeur actuelle de dernière vue de cet autre actif est ultérieure à 2024. Le masque de propriétés n’est pas décodé : ces requêtes ne sont pas qualifiées de consultations de cette vidéo.

Toutes les **5 958** lignes dont la modification tombe dans la période centrale possèdent un `ZCLOUDASSETGUID`, ainsi que les 85 ajouts. C’est une association à l’état cloud actuel, pas la preuve que chaque modification était synchronisée. Au 28 avant restitution, les valeurs actuelles donnent **zéro ZMODIFICATIONDATE, zéro ZLASTVIEWEDDATE et un ZADDEDDATE**, alors que 343 transactions historiques existent : les champs d’actifs ont pu évoluer après coup ou les lignes disparaître. Leur absence ne permet donc pas de conclure à l’absence de traitement le 28. Les gros regroupements des autres jours se lisent comme des mises à jour de bibliothèque, sans compter des retouches humaines. La [synchronisation des modifications Photos](https://support.apple.com/en-us/108782) est documentée ; elle ne démontre pas le transport de tout l’historique Core Data, tandis qu’une restauration de base complète reste possible.

## LSC : nature du panneau et portée du cache

L’examen fonctionnel de `0000000432_2.51.0/main.jsbundle` dépasse le comptage de mots. `panel-code-details.json` conserve les positions et courts extraits des chemins `ipcCommonState`, `p2pIsConnected`, `reGetStream`, `showVideoLoad`, `ipcLocalViewTime` et `uiPhase:'preview'`, avec `ui_source:'0000000432'`. Un chemin de stockage de temps de vue local prend un identifiant d’équipement en argument et une constante « 600 ». **Le panneau contient bien des fonctions de caméra IP/connexion P2P et de prévisualisation**, plutôt qu’une identification fondée sur le seul mot camera. Il n’est pas relié pour autant à un modèle ou exemplaire précis ni à une exécution le 28. La constante 600 n’est pas exportée comme une durée regardée.

`main.jsbundle.meta` est un contenu opaque de **21 octets**, non reconnu comme plist ou JSON dans les essais ; son rôle n’est pas démontré. Son empreinte est conservée ; aucune clé de décodage n’a été obtenue. Il ne faut pas inventer une date de consultation à partir de ces octets.

À 17:39:17.525519, `__access_time__.json` mentionne le panneau ; les métadonnées de 485 ressources sont regroupées à la seconde 17:39:17. Constitution/mise à jour d’un cache, téléchargement ou affichage de panneau restent compatibles. Le cache ne conserve pas ici un événement runtime « flux connecté », première image reçue, durée de lecture ou session datée de 2024. Les APM déjà sondés demeurent non décodés ; aucun nouveau décodage n’est revendiqué. **Une consultation de caméra n’est pas établie.**

## Attribution finale des interactions

Les séquences ScreenshotServices et les requêtes explicitement attribuées à Photos sont les indices nouveaux les plus spécifiques d’une activité d’interface compatible avec une intervention humaine sur **l’appareil source de la bibliothèque**. Un appel de service ne constitue toutefois pas un journal tactile, et une restauration complète peut transporter l’historique : l’identité physique TP-02 en 2024 doit encore être reliée à cet historique. Books, analyses Photos, nettoyage, génération de miniature, Santé et reconnexions réseau ont des explications automatiques crédibles. Aucune personne n’est identifiée.
