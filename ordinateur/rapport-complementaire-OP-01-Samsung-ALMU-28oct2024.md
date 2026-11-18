# OP-01 — Antériorité du Samsung et sorties des données ALMU

**Affaire :** SADEDINE-2026 — Mme Malika Sadedine / DMM Conseils  
**Support :** OP-01, ASUS UX333F, série `KAN0CV116290436`, nom Windows `LAPTOP-RMCOB2VU`  
**Date :** 13 novembre 2026 — recherches complémentaires dans l’image disque, depuis SIFT  
**Prestataire :** Christophe Donnat — Donnat Dev  
**Statut :** rapport autonome ; aucun rapport antérieur modifié.

## 1. Réponses

**Samsung.** La première reconnaissance documentée du numéro de série exact **`R58RB2ETQER`** est le **28 octobre 2024 à 11:18:34, heure enregistrée par le PC**. Aucun événement ni section SetupAPI antérieur n’a été retrouvé pour ce numéro. Une clé du registre le désigne comme **« XCover 5 de David »**. Les traces ne mettent pas en évidence un usage habituel avant le 28 ; elles restent insuffisantes pour certifier qu’il s’agissait de sa toute première connexion depuis la mise en service de l’ordinateur.

**ALMU. Oui, des sorties PDF effectives sont établies, au-delà des dates des fichiers de paramètres ou d’impression.** Les travaux d’impression Windows sont corroborés par trois PDF dont les contenus ont été examinés :

- **15:18:42** : facture ALMU **FA0338**, une page, dans le `test.pdf` du Bureau OneDrive ;
- **15:19:42** : factures ALMU **FA0338 et FA0339**, deux pages, dans `C:\L16B\test.pdf`, ensuite retrouvé dans la corbeille ;
- **15:28:33** : document final de **458 pages**, toutes portant le nom ALMU, actuellement dans **`C:\L16B\SAGE\sage.pdf`**.

Il s’agit de **générations de fichiers par l’imprimante virtuelle Microsoft Print to PDF**. Une impression sur papier, la copie intégrale de la base Sage ou le transfert de ce PDF précis sur une clé USB ne sont pas établis par les éléments examinés.

## 2. Méthode et conventions

Les recherches prolongent le [complément Sage 50 et réseaux](rapport-complementaire-OP-01-Sage50-reseaux-28oct2024.md), conservé sans modification. L’image EWF d’OP-01 est lue dans SIFT par la chaîne EWF → loop en lecture seule → Dislocker `-r` → NTFS monté `ro,norecover` sur `/mnt/windows`. Aucune application issue du disque n’a été exécutée. Les sorties sont conservées dans un nouveau dossier [samsung-almu-20261113](recherche-OP-01/samsung-almu-20261113/).

L’examen a porté sur les **359 EVTX et leurs 275 577 événements alloués**, les **dix journaux SetupAPI conservés**, les clés de périphériques SYSTEM/SOFTWARE, les données et impressions ALMU, les traces récentes déjà extraites, ainsi que la MFT. Le balayage des **1 046 016 emplacements MFT** a retenu **739 entrées ciblées**, dont 698 allouées et 41 non allouées. Il ne s’agit pas de 739 exports ALMU : la sélection inclut des fichiers, alias et noms apparentés ou des extensions recherchées.

Le SHA-256 de la MFT reste `4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b`, identique à celui des analyses précédentes. Les **22 fichiers de preuve rapatriés** ont été contrôlés par SHA-256. Les **54 événements principaux** ont été relus avec un second décodeur EVTX ; les données sources et les contrôles sont conservés en annexe technique.

Toutes les heures exposées sont celles de **Paris, UTC+1 le 28 octobre et le 3 décembre 2024**. Le 28, une correction d’horloge d’environ **−9,238 secondes** est enregistrée à 11:19:30 ; les heures de reconnaissance du Samsung, antérieures à cette correction, sont reproduites telles qu’enregistrées. Les impressions de 15 h sont postérieures à cette correction. Les heures UTC originales figurent dans les résultats ; aucune précision à la seconde n’est assimilée à une certification indépendante de l’horloge.

## 3. Le Samsung était-il déjà connu avant le 28 ?

### 3.1. Recherche du numéro exact dans tous les journaux conservés

Le balayage retrouve **18 événements portant explicitement `R58RB2ETQER`** : **16 le 28 octobre** et **deux le 3 décembre 2024**. Aucun n’est antérieur au 28. Les autres correspondances par identifiants d’interface ou de conteneur sont comptées séparément : un identifiant de pilote ou de famille USB ne suffit pas à reconnaître ce téléphone particulier.

| Repère | Source | Portée |
|---|---|---|
| **28/10, 11:18:34.352547** | Kernel-PnP/Configuration, événement **430**, RecordID **893** : `USB\VID_04E8&PID_6860\R58RB2ETQER` | Première occurrence du numéro exact dans les EVTX alloués conservés. |
| **28/10, 11:18:34.392** | `setupapi.dev.20241203_223829.log`, ligne **45589**, section `Device Install (Hardware initiated)` | Installation/configuration matérielle du même identifiant. |
| **28/10, 11:18:36.174023** | SOFTWARE, clé Windows Portable Devices, dernière écriture UTC `10:18:36.174023` | Enregistrement du nom de périphérique décrit ci-dessous. |
| **28/10, 11:18:53–11:47:31** | SetupAPI et Kernel-PnP | Passage en mode RNDIS, mise à jour de pilote et reconfiguration ; mêmes références de série parent. |
| **28/10, 17:14:11.399631** | Kernel-PnP/Device Management, événement **1010**, RecordID **1493** | Opération de retrait relative à `USB\VID_04E8&PID_6863\R58RB2ETQER`, concordante avec la déconnexion réseau décrite dans le premier complément. |
| **03/12, 22:38:36.038766 et 22:38:39.635256** | Kernel-PnP/Configuration, événement **420**, RecordIDs **975/991** | Suppression des instances de périphérique, et non preuve d’un nouveau branchement le 3 décembre. |

Les éléments complets sont conservés dans [les événements Samsung](recherche-OP-01/samsung-almu-20261113/resultats/samsung-events.json) et [les sections SetupAPI](recherche-OP-01/samsung-almu-20261113/resultats/setupapi-samsung.json).

### 3.2. Couverture antérieure de SetupAPI

Les rotations du journal d’installation des périphériques contiennent des sections successives depuis septembre 2023 :

| Fichier `Windows\INF\…` | Bornes des débuts de sections, heures locales consignées | Numéro exact retrouvé ? |
|---|---|---|
| `setupapi.dev.20240130_130906.log` | 28/09/2023 → 30/01/2024 | Non |
| `setupapi.dev.20240319_220333.log` | 30/01/2024 → 19/03/2024 | Non |
| `setupapi.dev.20240614_021232.log` | 19/03/2024 → 14/06/2024 | Non |
| `setupapi.dev.20241203_223829.log` | 14/06/2024 → 03/12/2024 | **Oui ; première section le 28/10 à 11:18:34.392** |
| `setupapi.dev.log` | 03/12/2024 → 12/10/2026 | Oui, dans les suppressions du 03/12 |

Les cinq autres journaux, relatifs notamment à l’installation hors ligne ou à la mise à niveau Windows en 2022/2023, ne contiennent pas le numéro exact. Leurs bornes et empreintes figurent dans [l’inventaire SetupAPI](recherche-OP-01/samsung-almu-20261113/resultats/setupapi-inventory.json).

Cette succession de rotations apporte une couverture utile avant le 28, mais **SetupAPI journalise des installations et reconfigurations, pas systématiquement chaque branchement d’un périphérique déjà installé**. Ses bornes ne garantissent pas non plus l’absence de lacune, d’ancien journal disparu ou d’utilisation avant septembre 2023.

### 3.3. Nom conservé et disparition des propriétés de première installation

La clé suivante est encore allouée dans SOFTWARE :

```text
Microsoft\Windows Portable Devices\Devices\USB#VID_04E8&PID_6860#R58RB2ETQER
FriendlyName = XCover 5 de David
Dernière écriture : 2024-10-28T10:18:36.174023Z
```

Le numéro exact relie le libellé à l’appareil recherché. **« XCover 5 de David » reste un nom de périphérique configurable** : il ne certifie pas l’identité du propriétaire ni, à lui seul, le modèle commercial. La dernière écriture de la clé n’est pas une date certaine de création de la clé ou de première connexion.

Windows peut conserver une propriété **`DEVPKEY_Device_FirstInstallDate`** distincte de la dernière installation d’un pilote. Microsoft précise que cette propriété date la première installation de l’instance et n’est pas réécrite à chaque mise à jour du pilote. [Microsoft — FirstInstallDate](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/devpkey-device-firstinstalldate).

**Aucune valeur de première installation rattachable à cette série n’a été retrouvée dans les clés actuellement allouées examinées.** Les recherches de périphérique dans SYSTEM sont négatives ; la seule correspondance active sélectionnée est la clé Portable Devices ci-dessus. Un contrôle exact des octets ASCII et UTF-16LE du numéro dans SYSTEM, SYSTEM.LOG1 et SYSTEM.LOG2 ne trouve pas non plus d’occurrence permettant d’ancrer une récupération de cette instance. Ce contrôle n’est pas une reconstruction de toutes les anciennes versions du registre.

L’absence actuelle de ces instances s’explique par une trace explicite :

```text
03/12/2024 22:38:35.685 : Delete Device - USB\VID_04E8&PID_6860\R58RB2ETQER
03/12/2024 22:38:39.472 : Delete Device - USB\VID_04E8&PID_6863\R58RB2ETQER
cmd: "C:\WINDOWS\system32\cleanmgr.exe" /autocleanstoragesense /d C:
Exit status: SUCCESS
```

Ces sections de `setupapi.dev.log`, lignes **12 et 156**, documentent un nettoyage Windows des instances. Elles ne prouvent ni intervention manuelle ni intention de dissimulation. Elles expliquent pourquoi l’état du registre acquis en 2026 ne permet pas de relire directement toutes les propriétés de l’instance de 2024.

### 3.4. Conclusion sur l’antériorité

La formulation soutenue par les traces est :

> **Le Samsung R58RB2ETQER, enregistré sous le nom « XCover 5 de David », est reconnu pour la première fois dans les traces conservées le 28 octobre 2024 vers 11:18:34. Aucun usage antérieur ni habituel de cet appareil avec OP-01 n’est mis en évidence. Sa première connexion absolue à cet ordinateur ne peut cependant pas être certifiée.**

Le scénario d’une première reconnaissance le 28 est compatible avec les traces d’installation. Il ne faut pas transformer cette compatibilité en certitude sur toute la vie du PC.

## 4. Des données ALMU ont-elles réellement été sorties de Sage ?

### 4.1. Cinq travaux d’impression terminés, tous vers PDF

L’extraction complète de `PrintService/Operational` pour la journée française du 28 contient **36 événements**, dont **cinq événements 307 `DocumentPrinted`**. Les champs sont lus dans `UserData`, et pas seulement dans `EventData`. Microsoft décrit les champs correspondants comme le document, l’utilisateur, l’imprimante, le port, la taille du travail et son nombre de pages. [Microsoft — Structure des données de travail imprimé](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/b4a22048-7837-460e-b1bd-8d34f4270f29).

| Heure Paris de fin | RecordID 307 / numéro de travail | Imprimante et chemin de sortie déclaré | Pages | Corroboration du contenu |
|---|---|---|---:|---|
| **15:16:31.761026** | **2419**, travail 2 | Microsoft Print to PDF → `C:\Users\fintm\OneDrive\Bureau\test.pdf` | **1** | État initial non retrouvé comme contenu distinct ; ne pas lui attribuer une facture précise. |
| **15:18:42.668038** | **2424**, travail 3 | Microsoft Print to PDF → même chemin du Bureau | **1** | PDF d’une page **ALMU FA0338**, titre et date interne concordants. |
| **15:19:42.030103** | **2429**, travail 4 | Microsoft Print to PDF → `C:\L16B\test.pdf` | **2** | PDF retrouvé dans la corbeille : **FA0338 + FA0339**, titre `Facture - FA0339`. |
| **15:23:32.738380** | **2445**, travail 2 | Microsoft Print to PDF → `C:\L16B\Sage.pdf` | **205** | Fin de travail enregistrée ; ancien état non retrouvé comme PDF autonome dans la sélection examinée. |
| **15:28:33.649956** | **2450**, travail 3 | Microsoft Print to PDF → `C:\L16B\sage.pdf` | **458** | PDF final de **458 pages ALMU**, métadonnées concordantes ; actuellement sous `C:\L16B\SAGE\sage.pdf`. |

Les numéros de travail sont réutilisés dans le journal : un numéro « 2 » ou « 3 » ne suffit pas à fusionner deux travaux à des horaires différents. Les chemins `Sage.pdf`/`sage.pdf` ne désignent pas nécessairement deux fichiers distincts sous Windows ; leur contenu a pu être remplacé au fil des opérations. Les volumes de pages **ne doivent pas être additionnés comme autant de documents distincts**, car plusieurs sorties se recouvrent.

Pour chaque événement 307, les événements voisins **842** indiquent `Microsoft Print to PDF` avec `ErrorCode=0x00000000` ; les événements **805** fournissent les paramètres de rendu. Les tailles de travaux, par exemple **3 721 914 octets** pour le travail de 458 pages, sont des tailles de traitement d’impression, **pas la taille finale du PDF**, qui est de 42 818 862 octets.

Une tentative intermédiaire nommée **`Facture - FA0543`**, travail 5, se termine à **15:21:33** par l’événement **824, RecordID 2435**, erreur `0x80070057`. Elle ne doit pas être présentée comme une impression réussie. Les opérations sur le pilote Adobe PDF dans le même intervalle sont également distinguées des travaux terminés.

### 4.2. Les PDF eux-mêmes corroborent les événements

| Pièce vérifiée | Contenu, métadonnées et rattachement | SHA-256 |
|---|---|---|
| **MFT 181043**, chemin reconstruit `Users\fintm\OneDrive\Bureau\test.pdf` ; 405 202 octets | Extrait directement du volume NTFS, entrée allouée. **Une page FA0338**, en-tête « SAS ALMU » ; producteur Microsoft Print To PDF ; création interne **28/10 à 15:18:42 Paris**. | `db0129d05ab52950fc9625934373d922ed2550d3982f0514ff433bdcc1b5f6c5` |
| **MFT 166334**, `$Recycle.Bin\…\$R2RYNYS.pdf` ; 499 320 octets | **Deux pages FA0338 et FA0339**, en-têtes ALMU ; producteur Microsoft Print To PDF ; création interne **15:19:42**. Le fichier `$I2RYNYS.pdf` restitue le chemin original **`C:\L16B\test.pdf`** et une mise à la corbeille à **15:24:17.961 Paris**. | `f2cb8dbbbb28fe11eaddc59d31045152218516a1585109bd529a075e48dd8201` |
| **MFT 30590**, `C:\L16B\SAGE\sage.pdf` ; 42 818 862 octets | **458 pages** ; les 458 textes de page contiennent ALMU. Titre `Facture - FA0543` ; producteur Microsoft Print To PDF ; création/modification internes **15:28:33**. Modification NTFS du contenu à **15:28:33.485057**, immédiatement avant l’événement 307 de fin de travail. | `0718f1b0819210c2def92a8097bafb1a7c0586673cf37848afbbf55c943728a6` |

Les métadonnées PDF ne sont pas utilisées seules : **le contenu métier, les dates internes, les dates NTFS et les événements du spouleur concordent**. Le champ auteur `malika sadedine` est une métadonnée du document ; il ne permet pas d’identifier la personne ayant effectué l’opération.

La comparaison du texte, après retrait des espaces et sauts de ligne, donne :

- la page unique du `test.pdf` du Bureau correspond à la **page 254** du PDF final ;
- les deux pages du `test.pdf` de L16B correspondent aux **pages 254 et 255** du PDF final ;
- ces pages sont les factures **FA0338 et FA0339**, qui ont aussi été contrôlées visuellement. Leurs dates commerciales de mars 2022 ne sont pas les dates de génération des PDF en 2024.

Cette comparaison établit des correspondances textuelles, pas une identité binaire entre les PDF ni une validation des écritures de la base comptable. Les résultats page par page, métadonnées et empreintes figurent dans [l’analyse des PDF](recherche-OP-01/samsung-almu-20261113/resultats/pdf-content.json) et [les correspondances](recherche-OP-01/samsung-almu-20261113/resultats/pdf-page-comparison.json).

**Il est donc établi qu’un contenu ALMU a été matérialisé en fichiers PDF le 28.** Les fichiers `.sgdoc` et leurs dates ne sont plus le seul fondement de cette conclusion.

### 4.3. Impression papier, copie de base et transfert externe

**Impression papier.** Aucun des cinq travaux terminés de la journée dans le journal conservé ne vise une imprimante physique : ils visent tous Microsoft Print to PDF. Une génération PDF est établie ; une remise de feuilles sur papier n’est pas démontrée. Cela n’exclut pas une autre impression dont la trace aurait disparu ou qui aurait eu lieu sur une autre machine.

**Export de données lisibles.** Les trois PDF conservés attestent des sorties de factures ALMU ; le document final comporte 458 pages. Ce constat ne démontre pas un export de toutes les tables, de toutes les pièces ou de la totalité du dossier Sage. La présence d’une facture donnée dans un PDF ne valide pas son exhaustivité ou sa conformité avec l’ensemble des données de la base.

**Copie du fichier de base.** La présence des six stockages `CDMDATA` déjà identifiés ne fournit pas la preuve d’une copie intégrale d’ALMU le 28. La recherche MFT et les artefacts examinés n’établissent pas une telle copie. Une copie effectuée sous un autre nom ou sans trace conservée ne peut être exclue.

**Copie vers une clé ou un tiers.** Le PDF final est présent dans le dossier local L16B. Les Jump Lists conservent notamment des références à l’ancien `C:\L16B\Sage.pdf`, modifié à **15:23:32**, et au chemin dans `SAGE`, avec les métadonnées de l’état final. Elles corroborent les états et chemins locaux sans identifier une copie externe du PDF.

Les analyses antérieures documentent des clés Kingston et des références à `E:\saddedine\Archive_saddedine.zip` et `Inventaire_saddedine.csv`. **Le contenu de cette archive externe et son inventaire final ne sont pas disponibles pour cette comparaison.** Ni leur présence dans les raccourcis, ni les branchements USB ne prouvent à eux seuls que les 458 pages ALMU ont effectivement été emportées. Le rapprochement avec le CD d’inventaire et ses empreintes reste nécessaire pour répondre à cette question précise ; la présente recherche ne le remplace pas.

## 5. Limites et pièces de contrôle

Les journaux ont été acquis en 2026, après des utilisations, mises à jour et nettoyages. Un résultat négatif porte sur les traces conservées, et non sur un historique intégral du PC. Les propriétés d’instances USB supprimées ne sont pas reconstituées ; aucun premier branchement absolu n’est affirmé. Les enregistrements non alloués de tous les EVTX n’ont pas été récupérés exhaustivement par cette nouvelle campagne.

Le registre est analysé par clés et valeurs de périphérique ciblées. La recherche résiduelle SYSTEM ne produit que des comptes d’occurrences du numéro exact, sans copie de fragments indifférenciés. Aucun compte utilisateur ni service distant n’a été sollicité pour cette recherche.

Le PDF final prouve la présence de données ALMU lisibles dans une sortie de 458 pages ; **il ne prouve pas une impression papier ni la copie complète de la base ou son transfert sur un support déterminé**. Le compte Windows `fintm`, le nom de téléphone et l’auteur PDF ne suffisent pas à identifier un opérateur humain.

Les nouvelles pièces sont regroupées dans [le dossier technique](recherche-OP-01/samsung-almu-20261113/), notamment :

| Pièce | Objet |
|---|---|
| [Résumé](recherche-OP-01/samsung-almu-20261113/resultats/summary.json) | Décomptes, première occurrence Samsung et erreurs de lecture. |
| [Registre Samsung](recherche-OP-01/samsung-almu-20261113/resultats/samsung-registry.json) | Clé exacte et nom « XCover 5 de David ». |
| [Couverture du registre](recherche-OP-01/samsung-almu-20261113/resultats/registry-coverage.json) et [présence résiduelle du numéro](recherche-OP-01/samsung-almu-20261113/resultats/registry-serial-presence.json) | Périmètre et résultats négatifs précisément délimités. |
| [Événements d’impression](recherche-OP-01/samsung-almu-20261113/resultats/print-events-day.json) | Les 36 événements, champs `UserData` et XML original. |
| [Contrôle NTFS direct](recherche-OP-01/samsung-almu-20261113/resultats/ntfs-direct-check.json) et [MFT ciblée](recherche-OP-01/samsung-almu-20261113/resultats/mft/mft-target-records.jsonl) | Rattachement des PDF aux entrées et chemins du volume. |
| [Information de corbeille](recherche-OP-01/samsung-almu-20261113/resultats/recycle-info.json) | Chemin original et suppression du PDF de deux pages. |
| [Sélection Jump Lists](recherche-OP-01/samsung-almu-20261113/resultats/jumplists-sage-selection.json) | États locaux anciens et final du PDF ; sélection issue de l’extraction antérieure inchangée. |
| [Sources et empreintes](recherche-OP-01/samsung-almu-20261113/resultats/sources.json) | Sources analysées ; les copies brutes sont limitées aux pièces utiles. |
| [Vérification des transferts](recherche-OP-01/samsung-almu-20261113/resultats/verification-transfert.json) et [lecture indépendante](recherche-OP-01/samsung-almu-20261113/resultats/verification-evenements-independante.json) | Contrôles de concordance. |
| [Scripts](recherche-OP-01/samsung-almu-20261113/scripts/) et [manifeste SHA-256](recherche-OP-01/samsung-almu-20261113/manifest-sha256.json) | Reproductibilité et intégrité du nouveau dossier. |

Outils : Python, libevtx/pyevtx, pyregf, libfsntfs/pyfsntfs, lecture binaire MFT, Poppler `pdfinfo`/`pdftotext`/`pdftoppm` et `dissect.eventlog` 3.11 pour la seconde lecture. Les quelques microsecondes d’écart de conversion entre lecteurs ne changent pas les conclusions à la seconde ; les représentations GUID du lecteur secondaire ne servent pas à l’identification des interfaces. Les pages de documentation Microsoft citées ont été consultées le 13 novembre 2026.
