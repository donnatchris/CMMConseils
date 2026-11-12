# Revue contradictoire — intervention humaine pendant la conservation sous scellés

**Affaire :** SADEDINE-2026. **Date :** 10 novembre 2026. **Périmètre :** OP-01, TP-01/02/03 et recoupements Freebox/cartes SD. Relecture des rapports et compléments existants, suivie de contrôles ciblés sur SIFT ; aucune nouvelle acquisition des appareils.

## 1. Réponse à la question

**Une intervention humaine avant l’ouverture demeure possible, mais aucune des traces examinées ne l’établit sur un appareil physique identifié. La piste la plus discriminante est TP-02 le 17 octobre à 17:25:47–17:25:52 : ses propriétés Wi-Fi associent une raison `WiFi Settings`, une date `JoinedByUserAt` et une séquence de génération de MAC puis d’association.** Les 22 appels marqués sortants dans son historique constituent une autre piste, dont l’origine matérielle reste indéterminée.

**TP-03 conserve bien une séquence système le 16 à 05:31:33–05:31:39. Son approfondissement favorise une explication par des traitements internes, sans prouver leur déclenchement automatique ni exclure une action humaine en amont.** Aucun SMS lu/envoyé ni déverrouillage n’a été identifié dans cette séquence. Une activité système, une interaction humaine, une attribution au téléphone physique et une rupture du scellé constituent quatre propositions distinctes.

On ne peut ni affirmer que les appareils sont restés inutilisés, ni déduire qu’ils ont été manipulés à partir de la seule présence de dates pendant leur conservation. Les opérations du 28 après ouverture ne démontrent pas une intervention pendant la fermeture des scellés.

## 2. Fenêtres et sources documentaires

Les [mail initial](../../docs/mail.txt), [mail complémentaire](../../docs/mail-2.txt), [attestation](../../remise-documents/attestation-de-remise.md), [lecture du PV](../20261108-analyse-pv/compte-rendu.md) et rapports techniques sont distingués :

- Le 15 octobre à 13 h 30 est la perte d’accès déclarée par la cliente. Le PV situe la mise sous scellés **après 14 h 19**, sans fermeture individuelle précisément horodatée.
- Le 28 octobre, 10 h 22 est l’arrivée de la cliente ; **10 h 41 est l’ouverture du PC**, **11 h 30 celle des téléphones**, puis insertion SIM à 11 h 45 sur le téléphone du scellé 3. La clôture à 19 h 20 ne fournit pas une restitution individuelle à la seconde.
- Les contrôles téléphoniques nouveaux utilisent **15 octobre 14:19 inclus → 28 octobre 11:30 exclu**, heure de Paris, avec changement UTC+2/UTC+1 le 27. C’est une fenêtre de sélection prudente, pas la preuve que chaque appareil était déjà fermé à 14:19. Les candidats recensés ici commencent le 15 à 18:50 pour les appels et le 17 pour le Wi-Fi.
- Les deux Mini ne sont pas attribuables aux scellés 3/4 par leur seule couleur. La divergence vert/noir de TP-01 demeure documentaire. Une conclusion portant sur un numéro de scellé exige un rapprochement matériel supplémentaire.
- Les caméras/cartes et la Freebox ne sont pas des appareils placés sous ces scellés. Leurs traces servent de recoupement, sans transposer aux téléphones leurs événements.

La déclaration de téléphones éteints puis rallumés le 15 vers 13 h 30 ne certifie pas leur état lors de la fermeture. Une preuve indépendante d’extinction à la fermeture serait déterminante : elle contredirait le scénario d’un appareil simplement resté allumé en arrière-plan. Elle ne suffirait toutefois pas à éliminer un import ultérieur de données datées ou une erreur d’horloge.

## 3. Comparaison des pistes avant ouverture

| Appareil / trace | Ce qui appuie une intervention possible | Contre-lecture et portée réelle |
|---|---|---|
| **TP-02, Wi-Fi le 17 à 17:25:47–52** | `AddReason=WiFi Settings`, `JoinedByUserAt=17:25:48.147446`, dates d’ajout identiques dans deux fichiers, génération puis première association espacées de 4,672320 s | Chaîne cohérente sur l’installation source ; pas de journal radio contemporain ni de liaison historique au matériel. Les propriétés liées ne sont pas des témoins indépendants. |
| **TP-02, 53 appels dont 22 marqués sortants, 15–26 octobre** | Événements de communication potentiellement initiés par une personne, répétés sur plusieurs jours | Historique transportable ; champs d’origine locale non renseignés pour ces 53 lignes dans le contrôle antérieur. Ni l’opérateur ni l’appareil physique ne sont établis. |
| **TP-02, Santé/PersonalAudio/TipKit/Photos le 17 vers 17:15–18** | Plusieurs magasins conservent des traitements proches, avant la chaîne Wi-Fi | Des services peuvent travailler sans geste humain. Les traitements CPL précèdent le rattachement ASUS conservé : ne pas prétendre qu’ils sont passés par ce réseau. |
| **TP-03, séquence du 16 à 05:31** | Deux créations Santé, événement PersonalAudio puis huit transactions Messages en six secondes | Mesures Santé du 15 ; échec CloudKit sans objet traité ; gestion de conseils récurrente, sans affichage attesté des trois conseils. Ni déplacement le 16, ni SMS lu/envoyé, ni authentification identifiés. |
| **TP-01, messages et métadonnées du 15–24** | Données portant des dates pendant la conservation | Groupe WhatsApp compatible avec arrivée différée le 28, métadonnées cloud non localisantes, caches d’origine non établie. Aucun geste local avant ouverture démontré. |
| **OP-01, échéance de réveil du 16 à 05:51** | Pourrait attirer l’attention sur un fonctionnement nocturne | Réveil seulement programmé dans un événement du 15 ; aucun réveil effectif corroboré. Les travaux Windows existants retrouvent une reprise le 28 à 10:41 après ouverture, pas une session intermédiaire établie. |
| **Freebox, appareils nocturnes les 16–17 et ordinateur non identifié le 16** | Présences réseau à examiner | Les trois iPhone nocturnes ne sont pas attribués aux TP ; `DESKTOP-ICPNCMD` n’est pas identifié à OP-01. First/last seen ne prouve pas une présence continue. |
| **SD-01/02/03, lacunes et anomalies vidéo** | Lacune SD-03 après le 15, suppressions et anomalies réelles | Aucun accès à une caméra depuis un téléphone scellé établi. SD-02 récupère notamment des vidéos du 5 novembre, hors intervalle. La signature de défaut vidéo existe dès 2023 ; aucune coupure volontaire attribuée. |

### TP-02 : ce que la comparaison Wi-Fi permet réellement

Le [rapport TP-02, § 7](../../telephones/analyse-TP-02.md) contient déjà des contrôles plus poussés que la lecture du libellé « utilisateur ». Un autre réseau marqué `Cloud Sync` conserve `JoinedByUserAt` au 15 avril alors que son ajout date du 11 juin : **une date utilisateur ancienne peut effectivement subsister dans un état ajouté plus tard**. Cependant, aucun des trois profils Cloud Sync comparés ne comporte une chaîne privée complète identique à ASUS. Un profil `System App` comporte également une séquence courte génération/association : la brièveté seule ne caractérise pas un geste humain.

Il faut donc distinguer : (a) action locale le 17, compatible avec la chaîne ASUS ; (b) simple arrivée d’un secret synchronisé, insuffisante à expliquer à elle seule tous les champs observés ; (c) migration/restauration d’un état complet, non exclue mais sans transfert postérieur au 17 identifié qui explique ce cas ; (d) horloge source erronée, non démontrée. La restauration de juin précédemment identifiée ne peut pas, à elle seule, expliquer des événements d’octobre.

Les deux BSSID conservés sont associés au **28**, pas figés au 17. Le nom ASUS ne prouve ni qu’OP-01 était le point d’accès, ni son propriétaire, ni la localisation. Les contrôles de conversion des dates écartent une erreur simple Cocoa/Unix/fuseau ; ils ne certifient pas l’horloge historique de l’appareil source. Aucun de ces constats ne suffit à qualifier une rupture de scellé.

### TP-03 : approfondissement déjà réalisé et résultat maintenu

L’[investigation détaillée](../20261110-tp03-intervention-humaine/compte-rendu.md) comprend les objets Santé, PersonalAudio, TipKit, les dates numériques de 1 548 bases, les plist, alarmes, communications, usages réseau, ATX et RecentAppLayouts. Les huit transactions du 16 correspondent à 14 changements de règles/paramètres/conseils ; leur profil existe dans **40 autres groupes**. Cette répétition est un argument pour un mécanisme interne, pas une expérience contrôlée démontrant l’absence de personne. Les classes de protection ne fournissent pas un horaire de déverrouillage. Les dernières valeurs d’usage conservées en novembre/décembre ne reconstituent pas exhaustivement octobre.

La cohérence de l’identité de l’installation renforce la continuité des données ; elle ne garantit pas que tout état historique a été produit sur le matériel physique actuellement identifié. Les tests présents ne valident donc pas la thèse humaine, et ne l’invalident pas pour toutes les opérations possibles.

## 4. Nouveaux contrôles exécutés dans cette revue

### 4.1. Communications : même fenêtre appliquée aux trois téléphones

Sur SIFT, copies nouvelles des bases SMS et CallHistory disponibles, avec leurs WAL/SHM présents, depuis les extractions de travail antérieures. Les bases copiées sont ouvertes avec `mode=ro`, sans `immutable` afin de ne pas ignorer le WAL. Les requêtes et empreintes des fichiers de travail sources figurent dans `prive/audit.json` ; aucune identité ni contenu de message n’est exporté dans les résultats.

| Contrôle | TP-01 | TP-02 | TP-03 |
|---|---:|---:|---:|
| Lignes SMS dont `date`, `date_read` ou `date_delivered` tombe dans la fenêtre | 0 | 0 | 0 |
| Appels dont `ZDATE` tombe dans la fenêtre | Base absente du chemin contrôlé | 53 | 0 |
| Parmi ces appels, `ZORIGINATED=1` | Non contrôlable ici | 22 | 0 |

Pour TP-02, bornes confirmées : **15 octobre 18:50:48.115369 → 26 octobre 17:14:34.075273**. Les 22 lignes sortantes se répartissent sur huit jours : 15 (8), 19 (1), 21 (2), 22 (1), 23 (3), 24 (1), 25 (4), 26 (2). **19 ont une durée positive.** Cela précise la répétition des communications conservées, sans localiser leur origine. Le champ `ZANSWERED=1` concerne 15 lignes, toutes entrantes dans ce lot ; il ne faut pas interpréter sa valeur zéro pour les sortants comme une preuve d’échec, alors que 19 portent une durée positive. Aucun taux de communications abouties n’en est déduit.

Ce contrôle ne couvre pas toutes les messageries ni les lignes supprimées non récupérées. Le zéro TP-03 porte sur une base ancienne et ne constitue pas un historique continu d’octobre. L’absence de base d’appels TP-01 n’est pas un résultat « zéro appel ».

### 4.2. Dates Wi-Fi étiquetées utilisateur

Recherche récursive de la clé exacte `JoinedByUserAt` portant une date plist native dans les fichiers connus TP-02/TP-03, avec mêmes bornes : **un seul candidat, TP-02 le 17 à 17:25:48.147446**. Fichier absent au chemin correspondant de TP-01 ; son ancien contrôle du fichier de secours de 37 réseaux reste distinct. Aucun secret Wi-Fi n’a été exporté. La reproduction donne le même objet JSON que le premier contrôle. Elle confirme la sélection, pas la sémantique exclusive du champ.

### 4.3. Préservation et reproduction

- Travail SIFT : `/home/sansforensics/analysis/revue-intervention-scelles-20261110/`. Script : `prive/controle.py`, exécuté avec Python 3 sur SIFT. Il refuse de réutiliser son dossier de sortie ; pour refaire l’opération, choisir un nouveau dossier et de nouvelles sorties sans écraser celles conservées.
- Wi-Fi : `prive/controle-wifi.py`, exécuté sur SIFT, sortie `prive/wifi-user-window-reproduction.json`, comparée au JSON initial. Lecture et empreintes avant/après des fichiers de travail.
- Résultats communications : `prive/results.json`, SHA-256 **4889c72342f0796501cf2da35f21ec40d43fb00c0216727605383fd53067b1e5** ; audit **9563e12eb9ce815af5043052c784434445bc1fc6676388907dfe3648a805e81e**. Les empreintes locales concordent avec les fichiers SIFT.
- Ces empreintes portent sur les extractions de travail et nouveaux résultats, **pas sur une nouvelle vérification intégrale des acquisitions chiffrées**. Leur provenance et les contrôles des acquisitions figurent dans les campagnes sources. Aucun original ni image maître n’a été modifié par ces contrôles.
- Versions des rapports avant cette mise à jour conservées dans `snapshots/`. Résultats détaillés et snapshots exclus de Git ; empreintes de cette campagne dans `SHA256SUMS.txt`.

La revue reprend les conclusions et contre-lectures des rapports Windows, Freebox et SD sans relancer leurs scans complets : aucune nouvelle piste datée et attribuée à un appareil scellé ne ressort de ces rapprochements. Elle ne revendique ni une nouvelle analyse intégrale de toutes les images, ni la récupération de traces déjà écrasées, ni un examen expérimental des mécanismes privés Apple.

## 5. Ce qui pourrait réellement départager les hypothèses

| Question encore ouverte | Pièce ou vérification discriminante | Limite actuelle |
|---|---|---|
| Les appels du 15–26 viennent-ils de TP-02 ? | Relevés opérateur avec IMEI/IMSI si disponibles ; comparaison des identifiants d’appels avec d’autres sauvegardes/appareils du compte | Un relevé de ligne seul ne désigne pas le téléphone physique ; pièces non disponibles ici. |
| Le réseau ASUS a-t-il été rejoint localement le 17 ? | Journal du point d’accès/DHCP du 17, correspondance contemporaine de MAC ; historique de migration/restauration | Les deux BSSID conservés du 28 ne comblent pas cette absence. |
| Une restauration transporte-t-elle cette chaîne précise ? | Expériences séparées sur appareils témoins de version pertinente : connexion manuelle, synchronisation seule, partage, restauration et migration ; acquisition avant/après | Aucun témoin équivalent disponible dans la campagne ; ne pas tester sur les pièces. Les expériences proposées dans le rapport TP-02 restent non réalisées. |
| TP-03 a-t-il été déverrouillé ou redémarré le 16 ? | Journaux contemporains d’authentification/démarrage, extraction d’époque, dossier de conservation et d’alimentation | Aucun marqueur discriminant retrouvé dans les artefacts disponibles ; un état tardif ne remplace pas un journal historique. |
| Un scellé a-t-il été matériellement ouvert ? | Identifiants des pièces/scellés, photographies, état à fermeture/ouverture, mouvements et interventions consignés | Une sauvegarde logique ne décrit pas l’intégrité matérielle d’un emballage. |

Ces compléments documentaires et expérimentaux ne sont pas présentés comme obtenus ou exécutés. **La conclusion actuelle est une possibilité humaine étayée surtout par TP-02, avec des alternatives non départagées ; aucune intervention humaine sous scellé fermé, identité d’auteur ou rupture matérielle n’est démontrée.**
