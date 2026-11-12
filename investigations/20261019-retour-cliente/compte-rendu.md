# Analyse du retour de la cliente et investigations complémentaires

**Mission SADEDINE-2026 — 19 octobre 2026.** Source nouvelle : [mail-2.txt](../../docs/mail-2.txt). Le prestataire confirme dans cette conversation ne pas disposer du PV. **Aucun procès-verbal n’a été consulté** : son contenu décrit dans le mail reste une déclaration de la cliente. Ce complément actualise les rapports, sans réécrire les pièces des campagnes antérieures.

## 1. Incidence du retour et réponses aux demandes

| Point du mail | Incidence et réponse |
|---|---|
| Installation après le cambriolage de mars 2023 | Repère déclaré. Recherche étendue aux dates disponibles ; les cartes acquises ne conservent pas un historique continu depuis mars 2023. Les anciennes données ne peuvent pas être recréées à partir de leur seule absence. |
| Réinitialisation de la chambre en février **2024** | L’année et la pièce sont désormais précisées par la cliente. SD-01 conserve une anomalie au 21 février et une autre au 1er mars, sans reset usine démontré. La présence d’un proche est une déclaration, sans lien technique établi avec ces anomalies. |
| Connexions, réappairages, changements de compte et partages LSC | Nouvel examen des dates de préférences et diagnostics, des catalogues et de la couverture. Pas d’historique complet des connexions ou partages reconstitué ; les états opaques restent non interprétés. |
| Terrasse en continu, sans arrêt volontaire habituel | Cette déclaration compte dans l’analyse. Le corpus conservé contient des lacunes ; il ne permet ni de confirmer une continuité 24 h/24 ni d’en attribuer la cause. Réutilisation circulaire et interruption d’acquisition sont des questions distinctes. |
| Accès distants et appareils associés depuis 2021 | OP-01 avait déjà été examiné sur cette fenêtre. Nouveau tri ciblé du manifeste TP-02, contrôle des profils, des préférences de compte et des fichiers d’appairage du PC. Aucun accès distant non autorisé nouveau établi. L’historique serveur des comptes et TP-01/03 restent indisponibles. |
| ASUS_Z01RD | Présence du nom dans OP-01, mais aucune première/dernière connexion du PC datable. Deux BSSID sont conservés dans TP-02 avec des associations datées du 28 ; ils ne certifient pas le point d’accès au 17. Restauration/synchronisation non exclues. |
| Réveil prévu le 16 | Toujours une échéance, pas un réveil constaté. La relecture générale des journaux ne trouve pas d’événement horodaté du 16 au 27. Aucun programmateur précis identifié par les recherches antérieures. |
| Correspondance aux scellés | OP-01 ↔ n° 1 concordant par modèle. TP-01 ↔ n° 2 seulement candidat, avec divergence noir/vert. TP-02/TP-03 ↔ n° 3/n° 4 indéterminé sans identifiants discriminants ; ne pas déduire une correspondance des numéros internes. |
| Détail des suppressions et activité après 19 h 20 | Dix mises à la corbeille revérifiées sur l’image avec chemins, heures et contenus. Aucun événement Windows après 19 h 20 le 28 dans les journaux lus ; des états du téléphone portent des heures ultérieures. Voir les contrôles distincts ci-dessous. |
| Outil branché aux téléphones et récupération de messages anciens | Fait rapporté, date encore « le 15 / le 28 ». Un appairage Apple ancien est présent sur OP-01 pour un autre UDID ; aucune extraction d’octobre 2024 ni outil précis identifié. Un message de 2016 ne date pas sa récupération. |
| Téléphones éteints puis rallumés vers 13 h 30 | Déclaration à conserver sans la transformer en preuve d’un état éteint continu du 15 au 28. L’examen ponctuel d’une image du salon ne démontre pas un démarrage de téléphone ni le rôle des personnes. |
| Téléphone n° 3 : « à compléter » | Aucun élément nouveau exploitable ; pas de nouvelle acquisition TP-03 identifiée dans le corpus SIFT. |
| Rendez-vous | Demande de créneaux de deux heures, à traiter par le prestataire selon son agenda ; aucun rendez-vous fixé ni message envoyé. |

## 2. Correspondance des appareils et des scellés

| Code de mission | Identité documentaire | Rapprochement possible avec le mail | Niveau de conclusion |
|---|---|---|---|
| OP-01 | ASUS UX333F, série KAN0CV116290436 | Scellé n° 1, ASUS UX333F | Modèle concordant ; numéro de série du PV non disponible. |
| TP-01 | iPhone 13 **vert**, série Q13QT4F164 | Scellé n° 2, iPhone 13 **noir** | Candidat par famille de modèle, **divergence de couleur non résolue** ; aucune identité certaine. |
| TP-02 | iPhone 13 mini rouge, série F5466LV9V7 ; sauvegarde concordante | Scellé n° 3 **ou** n° 4 | Les deux Mini rouges ne sont pas départageables avec le mail. |
| TP-03 | iPhone 13 mini rouge, série Y4Q9KGHG26 | Scellé n° 4 **ou** n° 3 | Même limite ; pas de sauvegarde analysable identifiée. |

L’insertion SIM rapportée à 11 h 45 sur le premier Mini est une piste de comparaison, pas un identifiant matériel. Les traces de remappage CommCenter déjà étudiées ne démontrent pas cette insertion. Ne pas renuméroter les supports et ne pas écrire « TP-02 = scellé n° 3 » sans pièce supplémentaire. L’attestation porte un champ « IMEI » de 19 chiffres pour TP-03 ; il reste à vérifier, sans correction arbitraire.

## 3. Opérations du 28 octobre : rapprochements désormais possibles

Les heures du 28 sont en **Europe/Paris, UTC+1** ; le 15 et le 17 sont en UTC+2. Le changement du 27 octobre interdit un décalage fixe de deux heures.

| Déclaration du nouveau mail | Trace technique conservée | Interprétation |
|---|---|---|
| Début général vers 10 h 22 dans le premier mail ; ouverture d’OP-01 à 10 h 41 dans le nouveau | Reprise Windows à 10:41:56 | Repères compatibles : début des opérations et ouverture de l’ordinateur ne sont pas nécessairement le même acte. Aucune calibration à la seconde par une heure déclarée à la minute. |
| Dossier C:\L16B laissé avec l’accord de la cliente | Arborescence et concentration de créations FN, dont LOCAL à 10:47–11:11 | Concordance substantielle ; sa présence n’est plus à présenter sans ce contexte déclaré. Elle n’identifie pas chaque opérateur. |
| Téléchargement de dmmconseils93300@hotmail.com dans Outlook | PST correspondant, créations FN à 15:35:26 et journal interne de synchronisation déjà documentés | Concordance avec un traitement de messagerie ; les heures du corps du journal restent sans fuseau explicite. |
| Takeout-20241028T114105Z-001.zip | Nom : 11:41:05 UTC = **12:41:05 Paris** ; manifeste : 11:42:33 UTC = **12:42:33 Paris** | Écart de **88 secondes**, compatible avec deux étapes d’un export. Le nom et le manifeste ne mesurent pas à eux seuls l’écart de l’horloge Windows : ils peuvent être produits côté service puis copiés. Aucune correction globale de l’horloge appliquée. |
| Une clé USB, déclarée Kingston par la cliente | Trois identifiants Kingston distincts dans SetupAPI ; volume KINGSTON 140B8328 dans les LNK/Jump Lists | Concordance de marque déclarée, **nombre et identité physique non réconciliés**. Ce n’est ni la preuve de trois copies ni la preuve d’une erreur du PV non consulté. Le numéro de volume n’est pas un numéro de série USB. |
| Inventaire sur CD, pièces non remises | Références à E:\saddedine\Inventaire_saddedine.csv, Rejets_saddedine.txt et Archive_saddedine.zip vers 17:26–17:27 | Les chemins sont des pistes concrètes. Ils ne prouvent pas la gravure d’un CD ni le contenu de l’archive externe. |
| Aucune suppression mentionnée dans le PV selon la cliente | Dix métadonnées de corbeille explicites | Différence entre les opérations techniques constatées et le récit fourni. Sans PV, aucune omission documentaire n’est directement vérifiée ; la nature juridique ou l’intention ne sont pas déduites. |

L’accord déclaré pour laisser `L16B` ne vaut pas autorisation documentée de chaque suppression. Inversement, une mise à la corbeille ne démontre ni effacement sécurisé, ni intention de dissimuler une pièce.

## 4. Dix mises à la corbeille : contre-lecture directe

Les **89 fichiers `$I`** présents dans la corbeille ont été relus sur le montage Windows en lecture seule. Les dix métadonnées du 28 sont identiques aux objets récupérés précédemment, et leurs **dix contenus `$R`** concordent par SHA-256. La date découle du champ FILETIME de suppression, pas d’une date SI/FN générique. Le SID est celui d’un profil Windows, pas l’identité de la personne au clavier.

| Heure Paris | Chemin d’origine complet | MFT `$I` |
|---|---|---|
| 11:02:53.315000 | `C:\L16B\LOCAL\Téléchargements - Raccourci (2).lnk` | 175042 |
| 11:02:53.322000 | `C:\L16B\LOCAL\Téléchargements - Raccourci (2) - Copie.lnk` | 175043 |
| 14:51:12.749000 | `C:\Users\fintm\Downloads\drive-download-20241028T134819Z-001\GESTION DES MOTS DE PASSES 2.docx` | 83278 |
| 14:52:25.983000 | `C:\Users\fintm\Downloads\drive-download-20241028T134819Z-001.zip` | 70741 |
| 15:12:28.791000 | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Etats\BANMAT [416611827712036]` | 171691 |
| 15:12:28.980000 | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Etats\My Little  [416611827712036]` | 172103 |
| 15:12:29.042000 | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Etats\Prestations de service~YARA [416611827712036]` | 172272 |
| 15:12:29.089000 | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Etats\RCT [416611827712036]` | 172368 |
| 15:12:29.137000 | `C:\ProgramData\Ciel\Applications\Ciel Gestion Commerciale\Compléments utilisateur\Etats\RCT Shine [416611827712036]` | 172384 |
| 15:24:17.961000 | `C:\L16B\test.pdf` | 25963 |

Détail machine, SHA-256, taille, index MFT et chemins de preuve : [corbeille-28-detail.json](resultats/local-v2/corbeille-28-detail.json). Les cinq fichiers Ciel sont des fichiers d’états, pas une base comptable dont la destruction serait démontrée. Les valeurs des documents contenant des identifiants ne sont pas reproduites.

## 5. Recherche des opérations postérieures à 19 h 20

### OP-01 : journaux Windows

La nouvelle lecture porte sur **359 fichiers EVTX et 275 577 enregistrements**. Les dates de tous les enregistrements lisibles ont été contrôlées ; les données du 16 au 29 octobre ont été conservées. **Aucun événement horodaté entre le 16 et le 27 inclus, ni après 19:20 le 28 avant minuit Paris, n’est retrouvé.** Le dernier événement du 28 parmi les résultats est à **17:37:50,842280 Paris** (Kernel-Power 107). Cela ne prouve pas que toute activité physique ou non journalisée ait cessé à cette seconde.

Le rendu XML de **285 événements** n’est pas accepté par le parseur XML strict. Ils n’ont pas été silencieusement exclus : leurs dates et identifiants ont été relus par les propriétés `pyevtx`, avec conservation du XML brut. Ils se répartissent en **108 le 28 et 177 le 29**, aucun après 19:20 le 28. Le complément ne valide pas sémantiquement tous leurs champs XML. Total de la fenêtre conservée après cette reprise : **6 072 événements le 28 et 3 594 le 29**. Les erreurs de rendu ne constituent pas une preuve d’altération volontaire des journaux.

Sources : [inventaire et bornes](resultats/sift/evtx-inventory.json), [événements](resultats/sift/events-16-29oct.json), [reprise des XML](resultats/sift/xml-fallback/summary.json), [empreintes avant/après](resultats/sift/sources.json). Les bornes extrêmes ne garantissent pas une conservation continue. Les journaux de sécurité ne couvrent plus octobre 2024.

### OP-01 : contrôle complet des dates MFT

Le parcours des **1 046 016 slots** (1 045 790 signatures FILE ; 665 406 entrées allouées et 380 384 non allouées) sélectionne **cinq fichiers** ayant au moins une date SI/FN strictement après 19:20 le 28 et avant minuit Paris. Tous sont sous `Users\fintm\iCloudPhotos\Photos` :

| MFT | Nom long | Date(s) ancienne(s) après 19:20, Paris | Nature |
|---|---|---|---|
| 91267 | `b1906834-2e58-4bae-be30-078269adc9cb.jpg` | 21:54:45 | Modification SI et FN, changement FN |
| 98830 | `d913d01f-9b49-47f5-9da7-73d4c54b3d34.jpg` | 21:54:45 | Modification/changement FN ; modification SI ultérieure en 2025 |
| 104344 | `IMG_1814(1).PNG` | 22:35:29 | Création/accès SI et FN |
| 75192 | `IMG_1815(1).PNG` | 23:54:37 | Création/accès SI et FN |
| 102645 | `95E259DA-40A2-4F0B-B416-933F894C2A63.jpg` | 23:56:36 | Création/modification/accès SI et dates FN |

Les cinq ont un **changement MFT SI le 02/10/2026 vers 19:45:43 UTC**, cohérent avec un traitement tardif de l’état acquis. **Ces dates anciennes ne sont donc pas attribuées à une opération locale d’OP-01 le 28 au soir** : synchronisation, import ou conservation de métadonnées restent possibles. Elles ne sont ni des suppressions datées ni une preuve d’utilisation sous scellés. Aucun autre fichier n’est sélectionné dans cette fenêtre par ce filtre SI/FN, ce qui ne couvre pas les métadonnées perdues/réutilisées ou les opérations sans date survivante.

Le sixième enregistrement du résultat est le fichier d’appairage, sélectionné **par son nom** et non par cette fenêtre. L’empreinte du flux MFT, `4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b`, concorde avec celle de la campagne antérieure. [Enregistrements et champs bruts](resultats/sift/mft-apres1920/mft-selected-records.jsonl), [compteurs](resultats/sift/mft-apres1920/mft-summary.json).

Les interactions Jump Lists avec les deux PST le **29 octobre vers 18:37 Paris**, déjà documentées, sont postérieures à la restitution déclarée ; elles ne doivent pas être imputées à une utilisation sous scellés. Aucun auteur n’est identifié par ces dates.

### TP-02 : dates postérieures présentes

Le filtre strictement postérieur à 19:20 relit trois chronologies antérieures, puis contrôle directement les préférences Wi-Fi et le cache LSC. Il ne constitue pas une nouvelle extraction exhaustive du téléphone. Les doublons entre chronologies et les repères déclaratifs ne sont pas comptés comme des opérations indépendantes.

| Heure Paris, le 28 | Source et constat | Limite |
|---|---|---|
| 19:27:56–19:34:33 | Dates de fin et de création de deux enregistrements Santé | Traitements potentiellement automatiques ; pas un geste ni une identification physique. |
| **19:39:46,059341** | CallHistory, ligne Z_PK=992 | Appel présent dans l’historique ; origine locale et personne non établies. |
| **19:40:02,126558** | `LinkDownTimestamp` de l’entrée **ASUS_Z01RD** | État Wi-Fi conservé, sans journal indépendant ni preuve de présence dans les locaux de l’administration. Ne pas confondre avec une nouvelle association. |
| **22:34:54,318385**, **22:35:06,157662**, **23:26:05,532493** | Trois champs `time` du cache LSC `Documents/panel/__access_time__.json`, interprétés en secondes Unix | Dates de cache de panneaux, **pas preuve de visionnage vidéo**, de commande de caméra ou d’accès extérieur. |
| 23:40:29–23:40:40 | Préférences Books/bookdatastored et statistiques | Activité de cache/service possible, pas consultation humaine démontrée. |

Ces traces sont **postérieures à la restitution telle que déclarée**. Leur provenance et leur horloge restent soumises aux limites de la sauvegarde. Elles ne démontrent pas une poursuite d’opérations par l’administration. Sources : [sélection des chronologies](resultats/local-v2/tp02-after1920.json), [contre-lecture Wi-Fi](resultats/plists/asus-dates-radio.json), [contre-lecture LSC](resultats/plists/lsc-after1920.json).

## 6. ASUS_Z01RD, synchronisation et réveil du 16

La nomenclature **ASUS_Z01RD** correspond bien à la famille **ZS620KL/ZS621KL**, selon le [manuel ASUS](https://dlcdnet.asus.com/pub/ASUS/ZenFone/ZS620KL/CZ13920_ZS620KL_2SIM_EM_WEB.pdf). Le nom est compatible avec un téléphone ASUS, mais les sources vérifiées ici ne certifient pas le **SSID par défaut d’un exemplaire déterminé**. Un SSID librement choisi n’identifie ni modèle physique, ni propriétaire, ni administration. La déclaration selon laquelle personne de connu n’utilise un ASUS renforce l’intérêt de cette piste, sans identifier son origine.

**Sur OP-01**, les cinq occurrences du nom dans `pagefile.sys` et les fragments décompressés restent compatibles avec un réseau visible. Les contrôles antérieurs des 65 profils, de NetworkList, de 6 512 événements réseau et de SRUM n’établissent **aucune connexion ni première/dernière date**. La marque ASUS de l’ordinateur ne suffit pas à en faire l’émetteur. Voir [datation OP-01](../../ordinateur/recherche-OP-01/wifi-ASUS_Z01RD/datation.md).

**Sur TP-02**, la série de la sauvegarde correspond à F5466LV9V7. Les propriétés ASUS incluent `AddReason=WiFi Settings`, `JoinedByUserAt` le **17 à 17:25:48,147446**, un ajout presque simultané, et une génération de MAC précédant le premier rattachement de **4,672320 secondes**. C’est une séquence technique cohérente, mais les propriétés proviennent d’un état acquis ultérieurement.

La contre-lecture donne deux BSSID : **22:B0:A5:94:1F:AF** (association conservée le **28 à 12:31:21**) et **32:0D:CA:FD:68:8C** (le **28 à 14:32:37**). Les deux ont le bit d’adresse localement administrée ; un constructeur ne peut pas être déduit de leur préfixe. Ils peuvent servir à une comparaison exacte avec d’autres pièces, **pas à attribuer rétrospectivement l’association du 17 à l’un d’eux**. Deux BSSID ne prouvent pas deux téléphones : interfaces/bandes/adresses variables restent possibles.

**Une synchronisation ou restauration ne peut toujours pas être exclue.** Un autre réseau marqué Cloud Sync conserve une date d’usage antérieure à son ajout ; des paramètres Wi-Fi historiques sont donc transportables dans ce corpus. La chaîne complète ASUS n’est pas reproduite par ce seul contre-exemple. Des migrations Photos portent l’UDID exact de TP-02, mais cela ne démontre pas une continuité matérielle sans restauration ni une horloge exacte le 17. Il manque une acquisition contemporaine attribuée au matériel, un journal de point d’accès indépendant ou une expérience témoin reproduisant les champs privés. L’inactivité déclarée sous scellés ne rend pas ces mécanismes impossibles.

**Pour le réveil du 16**, la valeur `WakeTimerDueTime` du 16/10 à 05:51:07,133163 Paris est une échéance inscrite dans un événement du 15. Les précédents examens des 264 tâches, du registre et des journaux n’en attribuent pas la programmation à une tâche précise. L’absence d’événements datés du 16 au 27 dans la nouvelle passe générale ne corrobore aucun réveil effectif. Un nom de tâche actuelle ou une échéance ne doit pas être transformé en activité historique.

## 7. Connexions à un ordinateur, outil d’extraction et comptes depuis 2021

### Un fichier d’appairage Apple sur OP-01

Deux fichiers sont présents sous `ProgramData/Apple/Lockdown` : un enregistrement nommé **00008110-001249321444801E.plist** et `SystemConfiguration.plist`. Le premier comporte `HostID`, `SystemBUID`, certificats et clés ; seules les métadonnées et les noms de champs ont été exportés. Son SHA-256 est `a6eb37fd5aac553440132a381550e4ee9fe960b7b6820fe37576eb32d1bfa930`. Sa modification exposée par le montage est le **14/12/2023 à 16:43:30,457909 Paris**. Le `SystemBUID` concorde avec la configuration Apple du PC. La MFT 113002 conserve une création SI au **04/07/2022 à 13:19:51 Paris**, mais une création FN au **14/12/2023 à 16:43:30 Paris** : ces champs différents ne sont pas fusionnés en une date certaine de premier appairage. La date de modification de décembre 2023 est concordante. Une contre-lecture par [istat](resultats/sift/istat-pairing-113002.txt) est conservée.

L’UDID du nom de fichier a pour SHA-256 `ccb3428f115ef6f7c6c5a9aa09385cf511792867fb4355ebe72c42e19d2bacef`, **différent de celui de TP-02** (`f10a800d625b9a3dce067ccfa5149582ad8d9eb3fce99e636465602044b20c72`). Ce rapprochement ne permet pas de nommer TP-01 ou TP-03 : leurs UDID indépendants manquent. La date de modification ne certifie ni le premier appairage ni la dernière connexion. Cet état étaye une relation de confiance Apple conservée sur le PC, **pas une extraction du 15/28 octobre 2024**, ni un outil forensique particulier. [Résultat](resultats/sift/apple-pairing-op01.json).

Apple décrit la relation de confiance permettant l’accès aux données et les sauvegardes, mais cela ne fournit pas un historique certifié de chaque connexion : [documentation Apple](https://support.apple.com/en-au/109054). Les certificats et clés privées n’ont pas été publiés.

### TP-02 et accès distants

Le tri du manifeste complet recherche explicitement les répertoires de pair records, les noms Cellebrite/UFED, GrayKey, Elcomsoft, Oxygen/Magnet et plusieurs applications de télécommande (TeamViewer, AnyDesk, LogMeIn, Splashtop, RustDesk, ScreenConnect/ConnectWise, AirDroid, Supremo, VNC). **Aucune correspondance dans ces catégories de noms de chemins**. Cette recherche n’identifie pas tout logiciel inconnu, outil renommé, accès Web ou extraction laissant des traces hors sauvegarde logique.

Les **47 candidats de noms relatifs à la gestion** comprennent des faux positifs de chemins WebKit. La relecture de **25 plist de profils/préférences de compte** montre notamment deux `ProfileTruth.plist` vides et `IsSupervised=false` dans l’état `CloudConfigurationDetails`. Ces états tardifs ne prouvent pas l’absence historique de gestion. Les deux fichiers FMIPAccounts trouvés ne fournissent pas une liste datée des appareils de confiance depuis 2021. Aucun identifiant d’ordinateur associé à une session d’octobre 2024 n’est établi côté téléphone.

Sources : [critères et résultats de tri](resultats/local-v2/tp02-manifest-targets.json), [structures de profils et comptes](resultats/plists/profiles-account-structure.json). Les contrôles portent sur des états locaux ; les historiques de connexions Apple/Microsoft/Google/LSC côté serveur ne sont pas présents.

Pour OP-01, les recherches antérieures couvrent les traces conservées depuis 2021 : navigateur très incomplet, Defender surtout depuis septembre 2023, Security récent, SRUM réseau de 2026. Les invitations Sage/LogMeIn Rescue des **4 juillet et 14 novembre 2022**, puis un raccourci du **6 octobre 2023**, restent des indices de téléassistance, sans session distante ni caractère non autorisé démontré. La détection de phishing de mai 2024 reste suivie d’une quarantaine déclarée réussie. **Aucune couverture exhaustive de 2021–2024 n’est revendiquée.**

## 8. Caméras depuis mars 2023 et continuité de la terrasse

### Bornes réellement disponibles

Le recalcul lit les inventaires complets conservés, y compris les lignes supprimées lorsqu’un nom reste exploitable. Les dates ci-dessous sont des **dates de noms valides**, pas des bornes d’enregistrement certifiées. Les métadonnées FAT de 2000 ne sont pas des vidéos historiquement filmées en 2000.

| Support | Première/dernière date de nom exploitable | Nombre de jours portant un nom vidéo | Conséquence |
|---|---|---:|---|
| SD-01 — chambre | 02/12/2023–28/10/2024 | 81 | Pas de vidéo nommée de mars 2023 ; 16 lignes de février 2024 et 37 du 15 octobre. |
| SD-02 — terrasse | 04/11/2024–12/11/2024, en incluant les vestiges nommés | 9 | Les vestiges du 4 ne sont pas tous récupérables. **Exception hors noms valides :** le clip au nom impossible `20242010` porte des images du **21/10/2024**, déjà vérifiées. Rien de récupéré pour le 15. |
| SD-03 — salon | 04/11/2023–31/10/2024 | 175 | 125 lignes de février 2024 et 65 du 15 octobre ; pas de couverture continue depuis mars 2023. |

Source : [couverture recalculée](resultats/local-v2/sd-coverage.json). Les nombres de lignes ne garantissent pas autant de vidéos complètes et intactes. Les bornes SD-02 excluent explicitement le nom de date impossible ; elles ne remplacent pas sa datation par les images.

### Terrasse : fonctionnement déclaré continu et corpus discontinu

La cliente indique un fonctionnement 24 h/24, sans arrêt habituel. Pour comparer cette déclaration au corpus, l’union des intervalles nominaux des MP4 **actifs à nom datable** a été recalculée par journée, en évitant de compter deux fois les recouvrements. Le calcul utilise les durées inventoriées ; il ne garantit pas que chaque image est lisible. Il ne comprend pas les clips supprimés récupérés ni le temporaire non finalisé.

| Jour caméra | Union nominale des vidéos actives datables | Part de 24 heures |
|---|---:|---:|
| 2024-11-05 | 16531.755 s | 19.134 % |
| 2024-11-06 | 53970.978 s | 62.466 % |
| 2024-11-07 | 54133.853 s | 62.655 % |
| 2024-11-08 | 56105.481 s | 64.937 % |
| 2024-11-09 | 42242.422 s | 48.892 % |
| 2024-11-10 | 44056.889 s | 50.992 % |
| 2024-11-11 | 45221.529 s | 52.340 % |
| 2024-11-12 | 51244.952 s | 59.311 % |

Les 5 et 12 novembre sont des journées de bord du corpus. Même au milieu de la période, l’union des intervalles ne couvre pas 24 heures. **Ce sont des lacunes du corpus actuel**, pas une mesure certaine du temps où la caméra était éteinte. Les causes à distinguer sont : réglage historique ou déclenchement, arrêt manuel/électrique, perte/écrasement/suppression, défaut de production ou datation. Le fonctionnement continu déclaré rend pertinente une vérification du réglage de l’époque ; il n’en constitue pas un journal technique.

La réutilisation de clusters et les suppressions anciennes demeurent fortement compatibles avec une gestion circulaire. Un enregistrement continu peut normalement remplacer ses anciens fichiers lorsque le stockage est plein : cette question est distincte d’une interruption du flux. L’absence du 15 octobre sur cette image n’établit donc ni coupure intentionnelle ni suppression ciblée ce jour-là. La présence déclarée d’une inspectrice sur la terrasse ne relie techniquement aucune action aux lacunes. [Détails journaliers](resultats/local-v2/sd-daily-nominal-coverage.json).

### Février 2024, chambre et dates 2000

Le signalement est désormais rattaché à la **chambre en février 2024**, ce qui précise le cadre des analyses existantes : fichier SD-01 du **21 février vers 23:41:04**, puis du **1er mars vers 04:05:05**, dates FAT de 2000 et défauts de finalisation. La signature audio commune à onze clips SD-01/SD-03 existe déjà en **novembre 2023**, donc avant le séjour rapporté et avant la perquisition. Elle ne constitue pas un marqueur spécifique de réinitialisation usine ou de changement de compte.

L’absence de dysfonctionnement remarqué par la cliente n’invalide pas les défauts binaires : certains clips restent lisibles malgré leurs erreurs de tables. Inversement, ces défauts ne prouvent pas un arrêt visible de l’appareil. Une coupure, une reprise de finalisation, un défaut logiciel ou un traitement ultérieur restent compatibles. Le nombre de clips anormaux n’est pas un nombre de réinitialisations. Les anciens commentaires « février sans année » sont remplacés dans les rapports courants par la précision du nouveau mail.

### LSC : états, médias et partages

Les **18 références de médias** de deux identifiants couvrent des dates du **24/08/2023 au 22/05/2025**, avec de grands intervalles sans référence. Il n’y a pas de référence de février 2024 ni du 15 au 28 octobre 2024 dans ces catalogues. Ce n’est pas un historique de tous les enregistrements SD ou de tous les visionnages.

Cinq champs `activeTimeKey` des préférences portent, sous hypothèse Unix, des valeurs de 2023. Leur sémantique n’est pas validée : ils ne sont pas présentés comme cinq dates d’appairage, de reset ou d’ajout de compte. `diagnostic.json` concerne le **16/05/2025** et `metric.json` le **10–11/08/2025**, hors période recherchée. Les deux caches `home/detailv1` et `home/list313` restent opaques ; les cinq APM ne sont pas décodés. Aucune liste historique des partages, comptes invités ou téléphones ajoutés n’est reconstruite. Les décalages d’horloge actuels des préférences LSC ne sont pas appliqués à 2024. [Résultats](resultats/local-v2/lsc-history.json).

Les données ne permettent donc pas de dater un réappairage ou changement de compte depuis mars 2023. La prochaine source discriminante serait un historique fournisseur ou une ancienne sauvegarde conservée, avec une rétention inconnue ; aucune connexion à un compte ni sollicitation d’un fournisseur n’a été effectuée.

## 9. Téléphones rallumés et image du salon

La cliente déclare que les téléphones étaient éteints lors de leur mise sous scellés et qu’une inspectrice les a rallumés pendant son absence vers 13 h 30 le 15. Le mail laisse aussi indéterminée la date du branchement de l’appareil d’extraction. Ces deux affirmations ne doivent pas être fusionnées en un seul événement techniquement prouvé.

Une contre-lecture visuelle ponctuelle a porté sur l’image conservée `714049800-138.88.png`, affichant **15/10/2024 13:30:21** (SHA-256 `8cc9a0f4c6654ffbbeb10c30b68eb5c808639cfb3c48e49947e4d67eec93366c`). Plusieurs personnes sont visibles dans la pièce et des objets rectangulaires sont sur la table. **Cette image seule ne démontre ni l’allumage d’un téléphone, ni un branchement, ni l’identité ou la fonction des personnes.** Aucun visionnage intégral ou analyse audio sémantique n’est revendiqué dans ce complément. Le temps affiché n’est pas calibré sur Windows/iOS.

La vidéo présente une erreur intermédiaire vers le temps nominal 13:30:05, puis des images jusqu’à environ 13:32:26 et une piste sonore plus longue. Cette proximité ne permet pas d’attribuer le défaut à une manipulation de téléphone. Le lien causal reste non établi.

## 10. Méthode, conservation et limites

Connexion SIFT via `ssh -F /home/chris/.ssh/config sift` ; consignes `/media/shared/AGENTS.md` lues. Le montage a utilisé EWF, loop en lecture seule, Dislocker `-r` puis NTFS `ro,norecover`. Aucun démarrage du Windows acquis, aucune écriture sur l’image ou les téléphones. Les nouveaux résultats sont isolés dans `investigations/20261019-retour-cliente/` et `/home/sansforensics/analysis/complement-20261019/`. Les anciennes versions des rapports sont conservées sous `rapports-avant/`.

Les journaux, métadonnées de corbeille, préférences et fichiers d’appairage consommés ont des contrôles SHA-256 avant/après. La MFT est parcourue en flux avec contrôle de structure et empreinte du flux comparée à l’empreinte antérieure. Les inventaires locaux sont des dérivés des acquisitions ; leur relecture n’est pas une acquisition indépendante. Aucun nouveau `ewfverify` intégral n’est revendiqué. Les sources et limites de chaque recherche sont listées dans les JSON et dans [README.md](README.md).

**La conservation cloud/disque client n’a pas été modifiée ou nouvellement attestée par ce complément.** Les lacunes documentées le 17 restent à traiter ; ce travail ne prouve pas que les deux copies demandées sont achevées. La durée contractuelle du cloud reste celle du devis à consulter.

Les éléments externes encore utiles sont précis : identité des deux Mini par série/IMEI dans les pièces de saisie, explication de la couleur de l’iPhone 13, date du branchement de l’outil, inventaire CD et éventuels rapports d’extraction, historiques de sauvegarde/restauration et de compte, réglages/modèles des caméras et contexte de l’affichage de réinitialisation. Le PV est **confirmé indisponible**, sans faire obstacle à la remise des constats techniques déjà établis.
