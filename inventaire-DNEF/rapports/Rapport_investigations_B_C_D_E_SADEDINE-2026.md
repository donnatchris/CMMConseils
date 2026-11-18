# Investigations complémentaires sur TP 03 et le transfert des PDF vers OP 01

**Mission SADEDINE-2026 — 14 novembre 2026 — complément à la réponse Q1.**

**Complément du 17 novembre 2026 :** réponse à la question Q3 de la note cliente.

## Conclusions

Les investigations apportent des précisions importantes sur l’activité applicative de TP-03 et sur l’apparition des PDF dans OP-01. **Elles ne démontrent pas un premier déverrouillage le 15 octobre, et le logiciel ayant transféré les 27 PDF reste non identifié.**

| Investigation | Résultat établi | Limite décisive |
| --- | --- | --- |
| B — Déverrouillage | Les 26 exemplaires PDF TP-03 contrôlés sont de classe C dans le manifeste. La base TipKit de Mail et la base du modèle clavier sont aussi de classe C. | Une lecture réelle de ces contenus dans cette classe supposerait un premier déverrouillage. Les traces conservées ne certifient ni un redémarrage à 13 h 25, ni le lieu et l’instant matériel d’une écriture ou lecture. |
| C — Transfert | Le dossier Mini est créé le 28 octobre à 17:12:06. Les 27 PDF portent des créations FN entre 17:13:43,2355080 et 17:13:43,8934745, soit **0,6579665 seconde**. Les 27 dates de création du CSV correspondent exactement aux créations SI du PC. | Ce regroupement très bref étaye une arrivée groupée au dossier final. Il n’identifie ni la source intermédiaire, ni un transfert USB direct, ni le logiciel. |
| D — Traces indépendantes | TP-03 conserve des entrées TCC pour Mail à 13:25:26 et Fichiers à 13:29:50, puis 33 transactions TipKit de Mail entre 13:25:30 et 13:29:09. | Aucun identifiant de PDF ni événement de premier plan n’y rattache les 17 documents. PeopleSuggester ne contient ici qu’une date d’identifiant, pas une ouverture de partage. |
| E — Doublons et horloges | Les 72 objets ont été comparés, avec 63 paires entre téléphones. Les doublons identiques forment quatre groupes. Les conversions UTC/Paris sont cohérentes. | Aucun décalage d’horloge unique n’est démontré. Le nommage ne désigne ni une application ni un conflit iCloud ; l’origine des doublons reste indéterminée. |

**La formulation technique retenue est conditionnelle :** si des lectures ou écritures nouvelles des contenus de classe C ont réellement eu lieu sur l’installation de TP-03 après le redémarrage rapporté, avec cette protection déjà applicable, un état BFU strict serait incompatible avec ces opérations ordinaires. Les conditions nécessaires à cette démonstration ne sont pas toutes établies par la sauvegarde tardive. Il n’est donc pas possible d’annoncer une contradiction technique démontrée avec le récit de la cliente, ni d’identifier une personne ayant déverrouillé le téléphone.

## Sources et méthode

Ce complément prolonge la [réponse Q1](Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md), les rapports [TP-03](../../telephones/analyse-TP-03.md), [TP-02](../../telephones/analyse-TP-02.md) et [OP-01](../../ordinateur/analyse-ordinateur.md). Les nouvelles investigations ont été exécutées sur SIFT, avec des destinations nouvelles sous [investigations-B-E-20261114](../travaux-techniques/investigations-B-E-20261114). Les rapports antérieurs et la réponse Q1 ne sont pas remplacés.

OP-01 a été remonté depuis son image avec un loop en lecture seule, Dislocker `-r` et NTFS `ro,norecover`. La MFT entière a été parcourue deux fois : recherche par noms et outils, puis extension aux tailles des PDF pour détecter des fichiers intermédiaires de noms quelconques. Les deux parcours retrouvent **1 045 790 structures FILE**, dont **665 406 allouées et 380 384 non allouées**, sans erreur de parsing consignée. Leur SHA-256 est inchangé :

```text
4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b
```

Les bases des téléphones ont été copiées avec leurs compagnons disponibles avant lecture. La première passe inspecte **11 bases SQLite et 50 plists de TP-03**, puis des requêtes ciblées comparent TCC, Mail, FrontBoard, CoreDuet et le clavier à TP-02. Les formats binaires FrontBoard avec dates hors plage ont été relus avec le parseur tolérant déjà employé dans le projet, sans corriger les octets ni inventer de dates.

Un complément de **neuf objets natifs TP-03, soit 82 289 octets**, a été déchiffré après fourniture du mot de passe de sauvegarde. Les empreintes chiffrées avant/après et les empreintes claires sont conservées ; aucun mot de passe n’est inscrit dans les scripts ou le rapport. Un premier essai avec le code déjà présent au dossier n’avait pas abouti et sa destination a été conservée séparément.

Toutes les heures du récit ci-dessous sont celles de **Paris**. Les dates sauvegardées ne sont pas considérées comme des mesures d’horloge indépendantes.

## B — Le téléphone était il déverrouillé

### Protection effectivement relevée

| Objets de TP-03 | Valeur du manifeste | Conséquence possible |
| --- | --- | --- |
| 26 exemplaires PDF correspondant aux 20 contenus | `ProtectionClass=3`, classe C | Le contenu de ces fichiers, dans cette classe, est protégé jusqu’au premier déverrouillage après redémarrage. |
| TipKit de Mail et modèle clavier | Classe C | Une nouvelle opération sur leurs contenus protégés serait un indice d’accès à la clé de classe C, si son exécution locale et sa datation étaient établies. |
| TCC, PeopleSuggester, préférences coreduetd et FrontBoard | `ProtectionClass=4`, classe D | Leur présence ou modification ne constitue pas en elle-même une preuve que la protection de classe C a été levée. |

La correspondance numérique des classes est documentée dans la [référence APFS Apple, rubrique Protection Classes, pages imprimées 142–143](https://developer.apple.com/support/downloads/Apple-File-System-Reference.pdf#page=142). Apple précise qu’un fichier protégé jusqu’à la première authentification devient accessible après ce premier déverrouillage et peut le rester après un verrouillage ultérieur. **AFU ne signifie donc pas écran actuellement déverrouillé.** [Documentation Apple Foundation](https://developer.apple.com/documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication).

Cette propriété concerne l’accès au contenu protégé. Elle ne permet pas d’assimiler automatiquement une date `lastused`, une date de changement de statut ou un nom de fichier à une lecture du contenu. Apple distingue le chiffrement des métadonnées du système de fichiers et les clés de classe des contenus ; cela ne valide pas pour autant un scénario précis de réécriture BFU des attributs observés. **Les données disponibles ne permettent pas d’établir que ce scénario a produit les attributs observés.** [Apple Platform Security, Data Protection in Apple devices](https://support.apple.com/en-mide/guide/security/sece8608431d/web).

Les classes sont celles de l’état sauvegardé. Leur maintien inchangé depuis octobre 2024 n’est pas certifié. Le chiffrement de la sauvegarde et le déverrouillage historique du téléphone sont deux questions distinctes : pouvoir déchiffrer aujourd’hui la sauvegarde ne date pas un déverrouillage ancien.

### Démarrage et premier déverrouillage

Le parcours des deux manifestes ne retrouve aucun fichier régulier correspondant aux motifs contrôlés pour `knowledgeC.db`, base Powerlog, traces unifiées `.tracev3`, `.logarchive`, fichiers Biome ou journal nommé de verrouillage/keybag. Cette absence est bornée au contenu des sauvegardes et aux motifs de recherche ; elle ne décrit pas tous les fichiers ayant existé sur les appareils.

Deux fichiers `.FirstUnlock` sont présents dans TP-03. Leur contenu a été effectivement déchiffré :

| Conteneur applicatif | Date NSDate enregistrée, heure de Paris |
| --- | --- |
| `group.is.workflow.my.app` | **24/05/2024 11:59:27,075932** |
| `group.com.apple.shortcuts` | **17/09/2025 17:12:16,471633** |

Ce sont des marqueurs applicatifs, sans événement du 15 octobre. Leur nom ne suffit pas à en faire le journal exhaustif des premiers déverrouillages du système. Les préférences Fichiers et Quick Look nouvellement déchiffrées ne fournissent pas de date d’accès aux PDF. Les dates pertinentes trouvées dans les préférences Mail sont anciennes, de 2018, 2019 et 2023.

Les 92 diagnostics IPS déjà inventoriés, les préférences SpringBoard/backboardd et les états FrontBoard ne fournissent pas ici de marqueur certifié du redémarrage ou du premier déverrouillage à l’heure litigieuse. Le champ TCC `boot_uuid` des lignes examinées vaut `UNUSED` et ne relie donc pas ces lignes à une session de démarrage identifiée.

### Portée des indices après authentification

Les 33 transactions Mail et la mise à jour du modèle clavier sont enregistrées dans des magasins de classe C. **Si elles représentent de nouvelles écritures effectuées localement à leurs heures déclarées après le redémarrage rapporté, elles appuieraient un accès après première authentification**, au plus tard à l’heure de l’écriture concernée. Pour Mail, la première transaction conservée de cette séquence est à **13:25:30,661993** ; pour le clavier, le champ de mise à jour est à **13:35:42,098506**.

Mais il manque un événement de démarrage et de premier déverrouillage daté, ainsi qu’une garantie que ces historiques n’ont pas été transportés ou restaurés. Il manque aussi une preuve que le changement des attributs des 17 PDF exigeait, lui-même, la lecture de leur contenu. **Le premier déverrouillage après le redémarrage allégué reste donc non démontré ; son absence reste également non démontrée.**

**Réponse à Q3 — accès aux PDF avant le premier déverrouillage.** Dans l’état sauvegardé de TP-03, les PDF examinés relèvent de la classe C : leur contenu est normalement inaccessible avant la première authentification après redémarrage. Une synchronisation iCloud ne suffit donc pas, à elle seule, à expliquer un nouvel accès local à ce contenu dans un état strictement antérieur au premier déverrouillage. En revanche, une date de métadonnée ne démontre ni un tel accès ni une création de PDF. La sauvegarde tardive ne permet pas d’établir l’état de protection et le lieu de production des traces aux heures litigieuses. Elle ne permet donc pas de déterminer si TP-03 a effectivement été déverrouillé ou a produit localement les fichiers à ces heures. La question du nommage des doublons est examinée ci-dessous, dans la partie E.

## C — Comment les PDF sont ils arrivés dans OP 01

### Apparition du dossier et arrivée groupée

| Élément NTFS | Index MFT | Création FN, le 28 octobre 2024 |
| --- | --- | --- |
| `C:\L16B` | 76947 | **10:47:10,6339294** |
| `C:\L16B\TELEPHONES` | 139574 | **17:00:37,5120727** |
| `C:\L16B\TELEPHONES\IPHONE13_MINI` | 12529 | **17:12:06,6590911** |
| Les 27 PDF du dossier Mini | 27 enregistrements distincts | **17:13:43,2355080 à 17:13:43,8934745** |

Les parentés MFT de ces dossiers sont résolues sans incertitude de séquence. L’intervalle d’environ **658 millisecondes** pour les 27 créations FN soutient une copie, extraction ou mise en place groupée au dossier final. Il ne correspond pas aux neuf minutes de la séquence de dates SI du 15 octobre.

Les **27 dates « création » du CSV sont exactement égales aux créations SI NTFS**, avec comparaison entière des FILETIME et des fractions décimales. Cela établit leur correspondance avec cette métadonnée Windows. Cela ne permet pas de déterminer quel système a produit initialement ces valeurs, ni de les qualifier de dates de création natives sur iPhone. Aucun flux nommé n’est présent dans les 27 enregistrements MFT examinés ; aucune provenance `Zone.Identifier` n’y identifie le transfert.

Windows permet à un programme de rétablir des dates de création, accès et modification via `SetFileTime`. Cette possibilité explique pourquoi une ancienne création SI n’identifie pas, à elle seule, un outil ou une opération locale ancienne. **L’API réellement employée ici reste inconnue.** [Microsoft, SetFileTime](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-setfiletime).

### Autres exemplaires déjà présents sur le PC

La recherche par tailles parcourt tous les enregistrements MFT alloués et retient **45 fichiers accessibles**, ensuite lus et hachés. Outre les 27 PDF du dossier Mini, elle retrouve à l’identique :

| Contenu | Autre emplacement OP-01 | Métadonnée de création SI de cet exemplaire |
| --- | --- | --- |
| FACTURE RCT OCTOBRE | Cache de pièces jointes de l’application Courrier Windows, fichier `FACTURE RCT OCTOBRE[71609].pdf` | **26/03/2024** |
| FACTURE RCT NOVEMBRE | Même cache, fichier `FACTURE RCT NOVEMBRE[71607].pdf` | **26/03/2024** |
| Avis ECH 0423 SAS RCT | Même application, autre sous-dossier de pièces jointes, fichier `Avis ECH 0423 SAS RCT[62736].pdf` | **12/10/2023** |
| KEDY FACTURE 202210 | `Users\fintm\Downloads` ; également regroupé dans `L16B\LOCAL\Téléchargement` | **27/10/2022** pour l’exemplaire Downloads |

Ces dates sont des métadonnées, pas une preuve indépendante de présence physique continue depuis ces années. L’identité binaire des contenus est toutefois établie par SHA-512.

Parmi **18 candidats ZIP contemporains**, 17 sont ouvrables ; le dernier est un fichier `$I` de métadonnées de corbeille, dont l’extension `.zip` ne fait pas une archive. Dans les deux exemplaires de l’export SHINE, deux autres contenus sont identiques à ceux des PDF Mini : **FA0037** et **facture rct 0801**, soit quatre occurrences de membres dans deux conteneurs. Aucun de ces candidats ne reconstitue un conteneur des 27 PDF Mini.

Ainsi, **au moins six des vingt contenus ont aussi un équivalent ailleurs sur OP-01**, hors du dossier Mini, en fichier ou dans SHINE. Cela renforce la nécessité de ne pas attribuer un contenu à un téléphone sur sa seule empreinte. Cela ne prouve pas que ces autres exemplaires ont servi à constituer le dossier Mini.

### Outils, USB et sortie Kingston

Les **887 Prefetch** conservés ont été relus sans erreur, ainsi que les UserAssist de `fintm` et `INVITES`, dix journaux SetupAPI, le pair record Apple, les exports Amcache et les traces déjà extraites de Jump Lists et d’événements Windows.

Un pair record correspond exactement à l’UDID de **TP-03**, avec le même `SystemBUID` que la configuration Apple d’OP-01. SetupAPI documente une installation de ce téléphone le **14 décembre 2023**, puis des suppressions d’instances le **14 mars 2024**. Ces éléments démontrent une relation ancienne avec le PC. Ils ne datent pas un branchement le 15 ou le 28 octobre. Aucun nouvel événement d’installation Apple de ces deux journées n’est retrouvé dans les sections retenues ; SetupAPI n’étant pas un journal exhaustif de chaque reconnexion, cela n’exclut pas un branchement.

iTunes et ses composants sont présents dans les traces d’installation/exécution. Le UserAssist iTunes conserve une date de **juillet 2022** ; les exécutions AppleMobileDeviceProcess et iTunesMobileDeviceLauncher retenues dans les Prefetch sont en **2026**. Elles ne prouvent pas un lancement iTunes pendant la copie du 28. Aucun artefact contrôlé ne rattache les PDF Mini à Apple Devices, iMazing, 3uTools, Cellebrite ou un autre outil d’extraction précisément identifié. Les correspondances de simples fragments de noms dans des fichiers sans rapport ont été écartées.

Le UserAssist de **`D:\LdSD-1.0.4\bin\Win64\LdSD.bat`** porte **17:15:40,172**, après l’arrivée des 27 PDF au dossier final. Il constitue une piste d’outil externe, dont le script/binaire et l’éditeur ne sont pas disponibles. La seule date de dernière exécution ne prouve ni une exécution unique, ni sa fonction, ni sa responsabilité dans la copie antérieure.

Les trois identifiants Kingston sont retrouvés dans SetupAPI aux repères déjà documentés : **16:27:54**, **17:00:07** et **17:14:51**. Les références Jump Lists à `E:\saddedine\Inventaire_saddedine.csv`, `Rejets_saddedine.txt` et `Archive_saddedine.zip` vers **17:26–17:27** restent des références de cibles externes. Elles ne donnent pas la liste des membres de l’archive et ne relient pas chaque PDF à un support matériel précis.

Les analyses NTFS antérieures demeurent applicables : **USN couvre octobre 2026, pas octobre 2024** ; les structures datables décodées du `$LogFile` se rapportent aussi à 2026. Le contrôle actuel de l’empreinte MFT ne rend pas disponibles les anciennes transactions de copie. Aucun rejeu de journal n’a été effectué.

**Chaîne reconstituée :** contenus présents dans les deux sauvegardes et parfois ailleurs sur le PC → origine des métadonnées du 15 encore inconnue → étape intermédiaire non identifiée → dossier Mini créé à 17:12:06 le 28 → 27 fichiers regroupés à 17:13:43 → références ultérieures à l’inventaire et à l’archive sur Kingston. L’outil et le canal intermédiaires restent à établir.

## D — Les traces applicatives sont elles liées aux PDF

### TCC

Les lignes TCC suivantes sont individualisées dans TP-03 :

| Heure le 15 octobre | Client | Service et valeurs conservés |
| --- | --- | --- |
| 13:25:26 | `com.apple.mobilemail` | `kTCCServiceUbiquity`, `auth_value=2`, `auth_reason=4` |
| 13:29:50 | `com.apple.DocumentsApp` | Même service et mêmes valeurs |
| 13:40:52 | `com.apple.Music` | Même service et mêmes valeurs |

La ligne de 13:40:52, déjà évoquée dans les rapports, concerne donc **Musique**. Les deux autres lignes précisent la séquence avant les PDF. `Ubiquity` concerne le service d’accès cloud ; aucune de ces lignes ne désigne un document, un chemin, un fichier PDF, un destinataire ou une action de partage. Les nombres d’autorisation conservés ne sont pas traités comme une preuve d’acceptation d’une boîte de dialogue par une personne. Aucune ligne TCC correspondante n’est retrouvée dans l’état TP-02 pour la fenêtre 13:20–14:05.

### Mail

Les transactions **8164 à 8196**, attribuées à `MobileMail` / `com.apple.mobilemail`, sont datées de **13:25:30,661993 à 13:29:09,106157**. Les changements associés portent sur **35 mises à jour de règles et 13 de paramètres TipKit**. Aucun changement de donation d’événement n’est identifié dans cette sélection. Les deux conseils conservés ont `ZLASTDISPLAYED=NULL`. Le nom actuel d’une définition d’événement `mail-sent` ne prouve pas un envoi ce jour-là.

Il s’agit d’un indice d’activité logicielle rattachée à Mail, plus précis qu’une préférence générique. **Ce n’est pas une preuve de Mail au premier plan, de message consulté, de PDF généré ou de partage effectué.** Les transactions se terminent avant la séquence 13:41–13:50. Aucune transaction Mail n’est retrouvée dans cette dernière fenêtre. TP-02 conserve des états de conseils Mail, mais aucune transaction dans la fenêtre 13:20–14:05 examinée.

### PeopleSuggester, CoreDuet et clavier

Le fichier PeopleSuggester contient **`DeviceId` et `DeviceIdDate`**, ce dernier à **13:41:02,145052**. Sa métadonnée de création/modification est **13:41:06**. Il ne contient ni liste de partages, ni application émettrice, ni identifiant de document, ni événement prouvant l’ouverture du menu de partage. Il faut donc retirer à cette date toute portée de preuve de geste de partage.

Les dates coreduetd de **13:50:40,668150 et 13:50:40,668330** concernent des clés de maintenance/throttling et de notification de tombstonage du flux `/app/activity`. Elles n’identifient ni une application au premier plan, ni les événements supprimés, ni une suppression de document par une personne. Les **8 interactions et 8 647 pièces jointes** conservées dans la base CoreDuet TP-03 ne fournissent aucun rattachement nominal aux PDF recherchés dans les champs contrôlés.

Le modèle clavier porte une mise à jour à **13:35:42,098506** sur le compteur cumulé `tium.totalWordsTypedInSecondaryLanguage`. Il n’y a ni texte saisi ni valeur antérieure permettant d’isoler un ajout à cet instant. Ce compteur ne peut pas être rattaché à un PDF ni à une saisie de code de déverrouillage.

Les états FrontBoard de Fichiers et Mail ont été décodés, y compris les archives auparavant opaques. Ils ne fournissent aucune date native d’octobre 2024 exploitable. Deux valeurs brutes de dimensions et de dernière interaction de fenêtre sont exactement communes aux deux Mini ; sans session de démarrage ni unité temporelle validée, elles ne constituent pas des événements indépendants datés du 15.

**Conclusion D :** des traces spécifiques de Mail et Fichiers existent dans TP-03 avant la séquence des PDF. Aucun lien documentaire direct ou événement de premier plan ne permet de les rattacher aux 17 contenus. Les anciens intitulés « PeopleSuggester/menu de partage » et « CoreDuet/activité » doivent rester des pistes de composants, pas des descriptions de gestes démontrés.

## E — Doublons, précision et propagation des attributs

### Doublons réellement identiques

| Groupe de même SHA-512 dans le CSV | Nombre de fichiers | Intervalles successifs des créations SI |
| --- | --- | --- |
| Qonto | 2 | **31,78 s** |
| facture rct 0801 | 3 | **8,98 s ; 9,40 s** |
| Avis ECH 0423 SAS RCT | 4 | **8,39 s ; 8,20 s ; 8,06 s** |
| KEDY FACTURE 202210 | 2 | **49,33 s** |

Ces quatre groupes expliquent les sept exemplaires supplémentaires : 27 fichiers pour 20 contenus. **`INV-184645.pdf` et `INV-184645 2.pdf` ont des contenus différents** ; leur suffixe ne suffit pas à en faire des doublons.

Les variantes répétées de Qonto, de la facture rct, de l’avis et de KEDY ne sont pas retrouvées sous tous leurs noms suffixés dans les exemplaires de sauvegarde examinés. Certains de ces noms ont pu être créés à une autre étape ou ne plus être conservés. Le fait qu’un nom manque dans une sauvegarde tardive ne date pas sa création ni sa disparition.

La documentation Apple indique que `FileManager.copyItem` échoue lorsque la destination existe ; le choix d’un suffixe peut donc relever de la couche applicative au-dessus de cette API. Windows propose aussi une option de renommage en cas de collision. **La forme « espace 2/3/4 » n’est pas, à elle seule, une signature suffisante d’iOS ou de Fichiers.** [Apple, copyItem](https://developer.apple.com/documentation/foundation/filemanager/copyitem(at:to:)), [Microsoft, FOF_RENAMEONCOLLISION](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-shfileopstructa).

**Réponse à Q3 — origine des doublons.** Les suffixes « 2 », « 3 » et « 4 » sont compatibles avec plusieurs mécanismes de copie ou de gestion de noms identiques. Ils ne permettent pas de distinguer des enregistrements répétés d’un mécanisme de conflit iCloud. Aucun élément retrouvé n’identifie ici un conflit iCloud comme origine des exemplaires de contenu identique, ni les conditions de sa survenue. La présence des contenus dans le stockage local Fichiers des deux Mini ne reconstitue pas leur circulation antérieure. **L’origine exacte des doublons reste indéterminée ; les éléments disponibles ne permettent ni de confirmer ni d’exclure une contribution d’iCloud.**

### Horloges

Le **15 octobre**, Paris est à **UTC+2** ; le **28 octobre**, à **UTC+1**. Les conversions ont été recalculées avec `Europe/Paris`. Les dates DNEF du 15 ont une granularité affichée au centième de seconde, celles des FILETIME une représentation à 100 ns et l’attribut lastused deux entiers secondes/nanosecondes. **La précision de représentation ne certifie pas l’exactitude physique des horloges.**

Pour les 17 correspondances TP-03, la différence « première création DNEF moins lastused » varie de **−8,969649 s à +10,51809805 s**, avec une médiane de **+2,14324401 s**. Cette dispersion, avec des signes différents, ne démontre pas un retard d’horloge constant. Les deux champs peuvent dater des étapes différentes d’un traitement. Aucun ajustement de quelques secondes n’a été appliqué pour améliorer artificiellement les rapprochements.

La correction d’horloge Windows d’environ **−9,238 secondes le 28 à 11:19:30**, déjà documentée, ne calibre pas l’horloge de TP-03 le 15. Les intervalles des doublons ne doivent pas être lus comme des durées de gestes humains mesurées indépendamment.

### Comparaison de tous les attributs

La comparaison porte sur les champs MBFile de **46 objets TP-02 et 26 TP-03**, et sur les attributs étendus décodés. Les enveloppes de clés sont comparées par empreinte, sans publier leur contenu. Les 63 paires possibles de même contenu entre les deux téléphones ont été examinées.

- `Birth` est identique pour **54 paires sur 63** ; `LastModified` pour **56 sur 63**. Aucun inode n’est identique entre les deux sauvegardes dans ces paires. Des dates de contenu anciennes peuvent être conservées malgré des objets de stockage distincts.
- TP-02 contient **36 objets dont le changement de statut est daté du 11 juin 2024**, date d’une restauration déjà documentée. Cette concentration est compatible avec une propagation ou reconstruction de métadonnées, sans identifier à elle seule toutes ses étapes.
- TP-03 conserve **16 changements de statut le 15 octobre** et **17 lastused dans la séquence litigieuse**. D’autres états ont été remplacés par des dates de décembre 2024 ou septembre 2025. Les attributs lastused sont présents sur 22 objets TP-03 et 38 TP-02 ; les exemplaires sans cet attribut ont aussi été comptés.
- Tous les objets TP-03 sont de classe C. TP-02 en a 45 de classe C et un de classe B, une copie supplémentaire de l’avis datée de 2025. Cette différence interdit de traiter toutes les copies comme une seule métadonnée native et immuable.

**Un mécanisme uniforme unique expliquant les 72 objets n’est pas établi.** Les profils mettent en évidence une conservation partielle de dates anciennes, des regroupements de changements de statut et des états ultérieurs différents. Ils confortent les réserves sur la propagation des métadonnées, tout en maintenant la spécificité temporelle des 17 attributs de TP-03. Ils ne permettent pas de trancher entre des enregistrements successifs initiaux et une réutilisation ultérieure de dates lors d’un transfert groupé. L’étape finale groupée sur OP-01 est, elle, nettement étayée.

## Pièces de vérification et suites discriminantes

Les résultats détaillés restent dans le sous-dossier privé, exclu de Git :

- [Schémas et première lecture TP-03](../travaux-techniques/investigations-B-E-20261114/prive/telephones-passe1/resultats.json), [requêtes et comparaison TP-02/TP-03](../travaux-techniques/investigations-B-E-20261114/prive/telephones-passe2/resultats.json), [FrontBoard décodé](../travaux-techniques/investigations-B-E-20261114/prive/telephones-passe2/frontboard-decode.json), [complément natif](../travaux-techniques/investigations-B-E-20261114/prive/complement-natif-v2/analyse.json).
- [MFT ciblée complète](../travaux-techniques/investigations-B-E-20261114/prive/op01-mft-tailles/records.jsonl), [Prefetch, UserAssist, USB et traces d’outils](../travaux-techniques/investigations-B-E-20261114/prive/op01-artefacts/resultats.json), [identités PC, archives et SI/FN](../travaux-techniques/investigations-B-E-20261114/prive/recoupements-finaux/resultats.json).
- [Comparaison des 72 objets](../travaux-techniques/investigations-B-E-20261114/prive/attributs/objets.json), [63 comparaisons entre téléphones](../travaux-techniques/investigations-B-E-20261114/prive/attributs/comparaisons.json), [calculs d’horloge](../travaux-techniques/investigations-B-E-20261114/prive/attributs/horloges.json), [classes des artefacts natifs](../travaux-techniques/investigations-B-E-20261114/prive/attributs/protection-artefacts.json).
- [Scripts de reproduction de l’analyse](../travaux-techniques/investigations-B-E-20261114/scripts), [contrôle final d’intégrité](../travaux-techniques/investigations-B-E-20261114/verification-finale.json) et [empreintes des nouveaux résultats](../travaux-techniques/investigations-B-E-20261114/manifest-sha256.txt).

Pour lever les incertitudes restantes, les pièces les plus discriminantes sont les journaux et la version de l’outil de transfert, le contenu de l’archive finale et des supports intermédiaires, ainsi que des traces contemporaines du démarrage et de l’authentification de TP-03. Aucune identité d’opérateur ni qualification juridique n’est déduite des seuls rapprochements techniques.
