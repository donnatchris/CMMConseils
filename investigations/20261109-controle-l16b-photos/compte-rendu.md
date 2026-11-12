# Contrôle de concordance entre les extraits de PV et le dossier L16B

**Mission SADEDINE-2026 — 9 novembre 2026.**

## Conclusion

**Les données corroborent fortement les catégories, les formats et la chronologie des opérations décrites dans les trois photos. Elles ne permettent pas de certifier que chaque fichier actuel de L16B est exactement un fichier copié par l'administration en 2024, ni que rien d'autre n'a été copié ou définitivement saisi.**

Les photos désignent principalement des catégories et des dossiers de destination, deux PST et une archive Takeout. Elles ne contiennent pas une liste exhaustive de noms et d'empreintes permettant une comparaison fichier par fichier. La présence d'un document « en lien avec la fraude présumée » est une appréciation annoncée par les rédacteurs, pas un résultat que le seul classement dans L16B permet de vérifier.

Le dossier actuel comporte **1 558 fichiers / 4 643 450 972 octets**, avec les mêmes chemins et tailles que l'inventaire technique antérieur. **1 555 entrées ont une création NTFS `$FILE_NAME` au 28 octobre 2024 ; trois portent une création de 2026.** Ces dates, confrontées au PV et aux contenus, corroborent un regroupement pendant les opérations du 28. Elles ne constituent ni une signature inviolable, ni un journal identifiant chaque opérateur.

## Contrôle réellement effectué

- Lecture des trois images fournies par le prestataire, conservées dans `prive/extrait-pv-1.png` à `extrait-pv-3.png`.
- Relecture des inventaires et enregistrements MFT déjà extraits d'OP-01, des contrôles des PST, des correspondances GDRIVE et des comparaisons de factures.
- Nouvelle lecture du dossier L16B sur SIFT : contrôle préalable du montage de `/mnt/windows` en **lecture seule**, inventaire complet des chemins et tailles, SHA-256 des deux PST, du PDF Sage et des archives Takeout/SHINE avant et après les lectures.
- Lecture et contrôle CRC par décompression de tous les membres de Takeout et SHINE ; examen structurel CSV/OFX ; analyse des trente fichiers EML.

Les **cinq fichiers ciblés restent inchangés**. Les deux PST, Takeout et SHINE correspondent aux empreintes antérieures enregistrées ; Sage correspond aussi à l'empreinte publiée lors du complément du 8–9 novembre. Ces contrôles portent sur les données de l'image acquise en 2026 ; ils ne les authentifient pas rétroactivement en 2024. Aucun accès aux comptes bancaires ou de messagerie n'a été effectué.

Scripts : [contrôle SIFT](scripts/controle_sift.py), [consolidation locale](scripts/consolider.py). Résultats : [synthèse structurée](resultats.json), [empreintes des sources de consolidation](sources-controle.json), `prive/controle-sift.json` pour les résultats détaillés. Le premier essai SSH a été refusé par le bac à sable réseau ; la lecture a ensuite été exécutée avec l'autorisation technique requise. Aucun résultat de l'essai refusé n'est utilisé.

## Comparaison poste par poste

Les heures du tableau sont les créations FN relevées, converties en heure de Paris le 28 octobre 2024. Elles ne datent pas nécessairement la première création du contenu.

| Mention des photos | Contenu retrouvé et recoupement | Ce qui est établi et ce qui reste ouvert |
| --- | --- | --- |
| Documents des disques locaux → `C:\L16B\LOCAL` | **1 389 fichiers** ; créations FN **10:47:55–11:11:10**. Une recherche antérieure sur 40 documents a retrouvé 16 contreparties dans le profil local, toutes identiques par SHA-256. | Présence et regroupement de documents locaux fortement corroborés. L'échantillon ne certifie ni les 1 389 origines individuelles ni le périmètre de sélection. |
| Documents GDrive → `C:\L16B\GDRIVE` | **93 fichiers**, créations FN **14:50:40–14:50:46**. Les 93 correspondent par SHA-256 à 93 membres d'une archive de téléchargement supprimée et récupérée, qui en contenait 94. Des flux `Zone.Identifier` renvoient à cette archive de téléchargement. | Une chaîne technique téléchargement/décompression vers le dossier est fortement étayée. Le compte cloud, l'auteur et le motif du retrait du 94e document ne sont pas démontrés par cette identité. |
| Documents iCloud Drive → `C:\L16B\iCloud Drive` | **8 fichiers**, créations FN **14:30:23–14:37:51**, dans le dossier annoncé. | Destination et chronologie concordantes. Pas de comparaison cryptographique exhaustive avec une source iCloud historique authentifiée. Le nom du dossier ne prouve pas seul la provenance cloud. |
| `fint.ms@hotmail.com` → sous-dossier homonyme de `MESSAGERIES` | **14 EML**, tous analysables comme messages avec en-têtes expéditeur/destinataire ; créations FN au 28 octobre. | Format et chemin concordants. L'emplacement et les en-têtes ne certifient pas une extraction complète ou exclusive depuis cette boîte, ni la pertinence de chaque message. |
| `misssmalika@hotmail.com` → sous-dossier homonyme de `MESSAGERIES` | **16 EML**, tous analysables comme messages avec en-têtes expéditeur/destinataire ; créations FN au 28 octobre. Le même dossier contient aussi `CADA.pdf.pdf`, avec création FN en 2026. | Les seize EML concordent avec l'extraction annoncée ; le PDF supplémentaire doit être distingué de ce groupe de 2024. |
| `dmmconseils@hotmail.com` → PST homonyme | PST de **2 143 626 240 octets**, identique à celui déjà décodé ; **3 836 messages reparsés** lors de l'analyse antérieure. | Un véritable conteneur de messagerie est présent au chemin décrit, pas seulement un fichier portant une extension PST. L'exhaustivité, la sélection et l'identité de chaque message avec l'état serveur de 2024 ne sont pas certifiées. |
| Téléchargement Outlook de `dmmconseils93300@hotmail.com`, puis extraction → PST homonyme | PST de **1 156 260 864 octets**, identique à celui déjà décodé ; **2 039 messages reparsés**. Un diagnostic conservé décrit une synchronisation **15:04:42–15:12:02**, 937 éléments ajoutés, puis une erreur de ressources. | Concordance technique supplémentaire avec un téléchargement Outlook. Le diagnostic ne suffit pas à établir sa machine d'origine ni une synchronisation complète. Les 937 éléments ne sont pas le nombre total de messages du PST. |
| Gmail `rct93300@gmail.com` → `Takeout-20241028T114105Z-001.zip` | Archive retrouvée avec même nom à la casse initiale près ; **MBOX de 66 015 300 octets** et manifeste HTML. Les deux membres se décompressent sans erreur ; le manifeste mentionne le compte attendu. FN **12:46:29** ; nom d'archive correspondant à **12:41:05 Paris** ; manifeste portant **12:42:33 Paris**. | Concordance de nom, compte mentionné, format et chronologie. Le manifeste n'est pas une signature Google vérifiée ; la sélection de l'ensemble des messages reste à authentifier par les données de saisie. |
| Impressions PDF de factures SAGE 50 → `C:\L16B\SAGE` | `sage.pdf`, **42 818 862 octets**, FN **15:27:24** ; empreinte identique au contrôle antérieur. Les textes de deux factures FA0338/FA0339 d'un `test.pdf` supprimé correspondent aux pages textuelles 254/255 de ce PDF. | Le PDF contient bien des factures et conserve ces deux factures de travail. Ce n'est pas une validation de chaque facture contre la base Sage ni une identification certaine du processus d'impression. |
| Export SHINE, période 01/01/2023–15/10/2024 → `C:\L16B\SHINE` | `RCT_01-2023_15-10-2024_EXPORT.zip`, **1 769 414 octets**, FN **15:57:55**. **30 membres** se décompressent sans erreur : CSV, OFX, QIF et **27 PDF**. CSV : **94 lignes** ; OFX : **94 transactions**, `DTSTART=20230101000000`, `DTEND=20241015000000`. | L'export bancaire et la période annoncée sont corroborés par le contenu. L'archive ne contient pas seulement une liste de mouvements : elle inclut des justificatifs PDF. L'intitulé RCT et le titulaire du compte doivent être rapprochés des pièces bancaires ; le PV nommant Malika Sadedine n'authentifie pas à lui seul le titulaire de cet export. |

Le contrôle des champs de date lisibles du CSV SHINE retrouve 121 valeurs (dates de mouvements et d'ajout de pièces), du **1er février 2023 au 27 septembre 2024**, sans valeur analysée hors de la période du PV. Cela n'affirme pas l'existence de mouvements tous les jours de la période ni la complétude de l'export.

Les deux PST ont été décodés antérieurement avec `readpst` : le comptage de **5 875 messages** ne couvre pas tous les types d'objets Outlook ou les éléments supprimés. Ils comprennent des dossiers de réception, d'envoi, de brouillons, d'indésirables ou de synchronisation selon le conteneur ; ce ne sont pas des fichiers dont la seule appartenance à une sélection liée à la fraude serait démontrée. Une boîte source peut légitimement contenir plusieurs adresses dans les expéditeurs/destinataires : on ne confond pas ces adresses avec la provenance du conteneur.

## Éléments postérieurs et ensembles hors du cadrage des trois photos

Trois fichiers actuels portent des créations FN de **2026**, également cohérentes avec leurs créations SI :

| Fichier | Création FN, heure de Paris |
| --- | --- |
| `L16B/GDRIVE.zip` | **27/07/2026 19:01:33** |
| `L16B/GDRIVE (2).zip` | **27/07/2026 19:07:00** |
| `L16B/MESSAGERIES/misssmalika@hotmail.com/CADA.pdf.pdf` | **02/10/2026 19:23:38** |

Ces métadonnées imposent de ne pas attribuer automatiquement ces fichiers à une création par l'administration en octobre 2024. Elles sont compatibles avec des ajouts/recréations ultérieurs ; elles n'identifient pas leur auteur, ne démontrent pas une substitution et ne prouvent pas que leur contenu était historiquement absent sous toute autre forme.

Le dossier actuel comporte aussi **30 fichiers dans `TELEPHONES`**, absents des trois cadrages photographiques. Cette catégorie est décrite séparément dans le PV complet déjà examiné : son absence des photos ne constitue donc pas un dépassement démontré. De même, les 27 PDF de justificatifs inclus dans l'archive bancaire ne sont pas automatiquement des pièces étrangères aux mouvements exportés.

Pour GDRIVE, le 94e membre récupéré est un document de gestion de mots de passe absent du dossier développé conservé. Cette différence est réelle ; la présence du document dans le jeu définitivement saisi, son exclusion intentionnelle et le motif de l'exclusion ne sont pas établis. Les défauts des ZIP GDRIVE créés en 2026 ne sont pas assimilés à une altération par les agents en 2024.

## Attribution à l'administration et jeu définitif

Le PV complet déjà analysé décrit les opérations de copie par les agents, l'ouverture du PC le 28 à **10 h 41**, une sélection/exclusion avant copie sur une clé USB, l'authentification numérique des fichiers et la gravure d'inventaires sur CD. Les créations concentrées de L16B pendant cette séance corroborent matériellement ce récit. **La conclusion d'attribution repose sur le recoupement du PV et des artefacts, pas sur un journal technique individuel de chaque copie.**

Des Jump Lists référencent `E:\saddedine\Archive_saddedine.zip`, `Inventaire_saddedine.csv` et `Rejets_saddedine.txt` sur un volume KINGSTON, avec dernières interactions vers **17:26–17:27 Paris** le 28. Elles corroborent l'existence de cibles de travail, sans révéler le contenu de ces fichiers ni certifier que tous les éléments de L16B ont été emportés.

La page 13 du PV distingue les dossiers laissés sur le PC à titre informatif des fichiers saisis. **Le contenu actuel de L16B ne doit donc pas être assimilé au jeu final authentifié.** La présence de correspondances ou de pièces sans lien apparent dans L16B ne prouve pas à elle seule leur inclusion dans la saisie finale.

Pour répondre « ce sont exactement ces fichiers, et aucun autre », il manque principalement :

1. Le CD d'inventaire et ses empreintes, pour connaître la liste des fichiers finalement retenus.
2. Le contenu de l'archive/support définitivement saisi et, si disponible, la liste des rejets, pour comparer noms, chemins, tailles et empreintes avec L16B, y compris les fichiers supprimés récupérés.
3. Pour les sources cloud et bancaires, un état historique ou un export authentifiable permettant une comparaison de contenu et du titulaire ; pour la pertinence des pièces, le périmètre complet de l'autorisation et l'examen individuel des documents.

**Bilan : concordance matérielle substantielle avec les copies annoncées ; identité exhaustive du jeu de 2024, exclusivité de son contenu, auteur de chaque opération et équivalence avec la saisie finale non certifiés. Aucune substitution de fichiers par l'administration n'est démontrée par ce contrôle.**

## Références antérieures utilisées

- [Rapport OP-01, § 10 et § 11](../../ordinateur/analyse-ordinateur.md) et [inventaire](../../ordinateur/recherche-OP-01/extractions-acces/l16b-inventory.json).
- [Opérations du 28 octobre : PST et Jump Lists](../../ordinateur/recherche-OP-01/operations-28oct/compte-rendu.md).
- [Analyse du PV complet](../20261108-analyse-pv/compte-rendu.md), qui actualise les mentions historiques d'indisponibilité du PV dans les anciens rapports.
- [Comparaison des factures et reprise du 9 novembre](../20261108-complement-pv/reprise-20261109.md).
- [Recherche élargie des correspondances](../20261109-correspondances-elargies/compte-rendu.md), avec ses limites de couverture et la distinction L16B/jeu saisi.
