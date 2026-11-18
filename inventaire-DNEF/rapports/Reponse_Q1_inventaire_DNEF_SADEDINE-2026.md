# Réponse technique à la question Q1 de la note DNEF

**Mission SADEDINE-2026 — 14 novembre 2026 — OP-01, TP-02 et TP-03.**


## Réponse en langage courant

**Question examinée (reformulation complète de Q1) : quelles sont les dates de création, les emplacements et les applications d’origine des vingt contenus PDF dans les sauvegardes de TP-02 et TP-03, et quel iPhone mini les aurait créés le 15 octobre 2024 entre 13 h 41 et 13 h 50 ?**

J’ai retrouvé les mêmes vingt contenus dans 72 exemplaires : 46 sur TP-02 et 26 sur TP-03. Les 27 fichiers de l’inventaire incluent des doublons. Leurs dates de création sauvegardées sont anciennes ; elles ne prouvent pas une création le 15 octobre. Je privilégie l’historique de données conservé dans TP-03 pour expliquer le rapprochement temporel, car 17 contenus portent un attribut de dernière utilisation dans cette fenêtre, dont 16 avec changement de statut rapproché. Aucun attribut équivalent contrôlé sur TP-02 ne tombe dans cette fenêtre.

Cette préférence ne démontre pas le téléphone physique source du transfert, une lecture du contenu ni un opérateur. Les dates de contenu, les dates de copie sauvegardées et les créations Windows du CSV sont comparées séparément dans les tableaux. L’archive finale, les journaux de collecte et une sauvegarde contemporaine permettraient de préciser le parcours.

## Conclusion

**Les 27 PDF de l’inventaire représentent bien 20 contenus distincts, retrouvés à l’identique par SHA-512 dans les deux sauvegardes. Aucune date de création `Birth` des 72 exemplaires examinés ne tombe le 15 octobre 2024 entre 13 h 41 et 13 h 50. Leurs métadonnées de création sont essentiellement anciennes, de 2019 à 2023.** Il faut donc distinguer la création du contenu PDF, la date de création conservée par sa copie sur le téléphone et la date de « création » figurant dans l’inventaire de saisie.

**Un élément nouveau favorise toutefois TP-03 : 17 des 20 contenus possèdent, dans cette sauvegarde, un attribut `com.apple.lastuseddate#PS` daté dans la même séquence du 15 octobre. Pour 16 de ces 17 objets, `LastStatusChange` tombe aussi dans cette fenêtre.** Ce rapprochement documentaire et temporel est plus discriminant que l’identité de contenu commune aux deux Mini. Aucun attribut de dernière utilisation des exemplaires TP-02 contrôlés ne tombe dans cette fenêtre.

La réponse à « lequel les a créés le 15 octobre ? » est donc : **une création ce jour-là n’est pas établie ; TP-03 est la piste la mieux étayée pour l’installation ayant conservé des traces d’utilisation ou de traitement de ces documents à ces heures.** Les données ne prouvent pas, à elles seules, que le téléphone physique TP-03 a été manipulé, que les 27 copies proviennent directement de lui, ni qui aurait effectué une opération. Les possibilités de copie, restauration, transport de métadonnées et d’horloge incorrecte restent ouvertes.

## Question et périmètre

La question Q1, § 3.4 de la [note cliente](../documents-recus/Note_analyse_inventaire_DNEF_SADEDINE-2026.docx), demande les dates de création, l’emplacement et l’application d’origine des 20 contenus dans TP-02 et TP-03, puis l’identification du Mini qui les aurait créés le 15 octobre entre 13 h 41 et 13 h 50. La présente réponse se limite à Q1. Elle ne conclut pas sur le déverrouillage, la possibilité d’une synchronisation avant premier déverrouillage ou le rattachement des traces TCC et PeopleSuggester, objets des questions suivantes.

| Code | Série | UDID de la sauvegarde |
| --- | --- | --- |
| TP-02 | F5466LV9V7 | `00008110-001C69A002BA801E` |
| TP-03 | Y4Q9KGHG26 | `00008110-001249321444801E` |

Les numéros de scellé 3 et 4 ne sont pas attribuables avec certitude à ces codes internes dans les pièces examinées.

## Contrôles réalisés

Les [rapports TP-02](../../telephones/analyse-TP-02.md#113-autres-téléphones-pdf-et-relation-de-confiance), [TP-03](../../telephones/analyse-TP-03.md#72-pdf-communs-aux-deux-mini) et [OP-01](../../ordinateur/analyse-ordinateur.md#62-les-3-461-entrées-datées-dans-lintervalle-central), ainsi que la [fiche Bourarach](../../investigations/20261109-clarification-correspondances/fiche-bourarach.md), ont servi de point de départ. Les anciennes réserves sur l’absence d’inventaire de saisie sont réévaluées ici pour les seuls 27 PDF grâce au CSV désormais fourni.

L’empreinte du [CSV fourni](../documents-recus/Inventaire_saddedine.csv) est exactement celle annoncée dans la note cliente :

```text
SHA-256 f2a4e9d05cca5c7b8082da42df76fca45e870f3e3acbbdf6ff03c07e68293c40
```

Sur SIFT, les PDF déjà déchiffrés lors des campagnes antérieures ont été relus. Leurs SHA-256 concordent avec les comparaisons antérieures, et leurs SHA-512 calculés cette fois concordent directement avec les 27 lignes du CSV. Les 20 contenus sont couverts sur chaque Mini : **46 objets dans TP-02 et 26 dans TP-03**. Il s’agit de 72 exemplaires correspondants, pas du nombre total de PDF de chaque sauvegarde. Les recherches antérieures sélectionnaient les candidats par nom normalisé ou taille déclarée ; elles ne constituent pas un hachage exhaustif de tous les objets des sauvegardes.

Les manifestes déchiffrés et leurs compagnons disponibles ont été copiés dans un nouveau dossier de travail, puis les copies ont été ouvertes en lecture seule. Les empreintes des sources sont identiques avant et après copie ; les deux copies donnent `quick_check=ok`. Les 72 `fileID`, domaines et chemins ont été revérifiés. Les champs `Birth`, `LastModified`, `LastStatusChange`, les attributs étendus et les champs internes PDF ont été extraits. Aucun déchiffrement nouveau ni accès aux comptes en ligne n’a été nécessaire.

| Manifeste déchiffré | SHA-256 |
| --- | --- |
| TP-02 | `cd34919ad3a2cb958e130b6ea7453e71f30fb02336d61f2e1dca0f2fb2b46eeb` |
| TP-03 | `334123a803c20b59c9610b459b8769a07d24cab7ea805e35c6f64caec65f365c` |

Les dates ci-dessous sont en **Europe/Paris**, avec le décalage applicable à chaque date. `Birth` est une métadonnée conservée dans la sauvegarde tardive, susceptible d’être héritée lors d’une copie ou restauration. Elle ne certifie pas la première apparition sur cet exemplaire physique du téléphone.

## Dates de création et origine déclarée des PDF

Le tableau donne les `Birth` de tous les exemplaires du stockage local Fichiers retrouvés. Les autres exemplaires applicatifs sont détaillés ensuite. Le nom le plus court d’un groupe de contenus identiques sert de libellé ; les variantes suffixées du CSV restent identifiées par leurs empreintes dans les pièces techniques.

| Contenu | Birth Fichiers TP-02 | Birth Fichiers TP-03 | Logiciel déclaré dans le PDF |
| --- | --- | --- | --- |
| C01 — TR Déposez votre capital social sur Qonto 📥.pdf | 03/02/2021 17:50:39 | 03/02/2021 17:50:39 | Mail |
| C02 — TR  Urgent.pdf | 03/01/2021 15:02:30 | 03/01/2021 15:02:30 | Mail |
| C03 — DEVIS DMM CONSEILS.pdf | 30/06/2020 10:29:57 | 30/06/2020 10:29:57 | Safari |
| C04 — FW  SOLDE CONTRAT.pdf | 18/02/2020 09:59:22 | 18/02/2020 09:59:22 | Mail |
| C05 — Rép  Dossier bourarach.pdf | 17/12/2019 19:20:21 | 17/12/2019 19:20:21 | Mail |
| C06 — RE  FINT.pdf | 29/11/2019 19:52:06 | 29/11/2019 19:52:06 | Mail |
| C07 — Facture - FA0334.pdf | 22/03/2022 11:40:04 | 22/03/2022 11:40:04 | Creator absent ; Producer Microsoft: Print To PDF |
| C08 — RE FEC Association mélodie de la seine.pdf | 13/04/2022 17:18:37 | 13/04/2022 17:18:37 | Mail |
| C09 — RE liste des factures.pdf | 11/10/2022 18:08:04 | 11/10/2022 18:08:04 | Mail |
| C10 — INV-184645.pdf | 20/10/2022 11:53:38 | 20/10/2022 11:53:38 | wkhtmltopdf 0.12.5 |
| C11 — INV-184645 2.pdf | 20/10/2022 11:55:51 | 20/10/2022 11:55:51 | wkhtmltopdf 0.12.5 |
| C12 — facture rct 0801.pdf | 03/05/2023 15:51:48 | 03/05/2023 15:51:48 | Microsoft® Word 2016 |
| C13 — Avis ECH 0423 SAS RCT.pdf | 31/03/2023 13:48:25 ; 06/02/2025 13:03:09 | 31/03/2023 13:48:25 | Microsoft® Word pour Microsoft 365 |
| C14 — Facture - FA0037.pdf | 01/02/2023 16:00:22 | 01/02/2023 16:00:22 | Creator absent ; Producer Microsoft: Print To PDF |
| C15 — FACTURE RCT OCTOBRE.pdf | 06/12/2022 16:40:58 | 06/12/2022 16:40:58 | Excel |
| C16 — FACTURE RCT NOVEMBRE.pdf | 23/11/2022 20:42:06 | 23/11/2022 20:42:06 | Excel |
| C17 — KEDY FACTURE 202210.pdf | 27/10/2022 18:10:07 | 27/10/2022 18:10:07 | Chrome 105 / ChromeOS (Skia) |
| C18 — Fattura-37_2022-SAS-RCT.pdf | 27/10/2022 16:05:22 ; 27/10/2022 16:05:23 | 27/10/2022 16:05:22 | Creator absent ; Producer FPDF |
| C19 — 2022100-rct-14-07-2022.pdf | 20/07/2022 11:26:43 | 20/07/2022 11:26:43 | WPS 表格 |
| C20 — Facture - FA0046.pdf | 13/05/2022 10:29:58 ; 17/05/2022 09:36:48 | 13/05/2022 10:29:58 ; 17/05/2022 09:36:48 | Creator absent ; Producer Microsoft: Print To PDF |


**Le champ `Creator` décrit le logiciel déclaré à l’intérieur du PDF, pas l’application qui l’aurait ouvert ou exporté le 15 octobre.** Sept contenus déclarent `Creator=Mail`, avec un `Producer` Quartz iOS 13.1.3, 14.2, 15.3.1 ou 15.6.1 et des dates PDF de 2019 à 2022. Cela étaye une ancienne génération de ces PDF par Mail. Les autres déclarent Safari sur macOS, Word, Excel, WPS, Chrome/Skia ou wkhtmltopdf ; plusieurs n’ont qu’un `Producer` Microsoft Print To PDF ou FPDF. Ces indications ne désignent ni l’utilisateur, ni le téléphone créateur, ni le mécanisme de transfert en octobre 2024.

Les différences de `Birth` entre copies d’un même contenu sont significatives : l’avis d’échéance possède dans TP-02 une copie supplémentaire datée de février 2025 ; FA0046 possède sur les deux Mini une copie du 13 mai et une du 17 mai 2022. Elles montrent qu’une date de copie n’est pas une date unique de création du contenu.

## Emplacements dans les sauvegardes

Les 20 contenus ont tous un exemplaire sous **`AppDomainGroup-group.com.apple.FileProvider.LocalStorage`**. Ce domaine désigne le stockage local géré par le fournisseur de Fichiers, interprété comme l’espace **« Sur mon iPhone »**. Le mot « Téléchargements » dans un chemin local ne le transforme pas en dossier iCloud Drive.

Les codes du tableau représentent les chemins sous `File Provider Storage/` : **R** = racine ; **D** = `Downloads/` ; **D/T** = `Downloads/Téléchargements/` ; **T** = `Téléchargements/`. La graphie « Téléchargements » est simplifiée pour la lecture ; les caractères Unicode exacts sont conservés dans l’annexe technique. **WA** = objet du domaine partagé WhatsApp, sous `Message/Media/` ; **WX** = objet de `AppDomain-com.tencent.xin`, sous `Documents/…/OpenData/…/1935.pdf`, correspondant au conteneur de WeChat.

| Contenu | TP-02 | TP-03 |
| --- | --- | --- |
| C01 | D, D/T | T |
| C02 | D, D/T | T |
| C03 | D, D/T | T |
| C04 | D, D/T | T |
| C05 | D, D/T | T |
| C06 | D, D/T | T |
| C07 | D, D/T | T |
| C08 | D, D/T | T |
| C09 | D, D/T | T |
| C10 | D, D/T | T |
| C11 | D, D/T, WA | T, WA |
| C12 | D, D/T, WA | T, WA |
| C13 | D, D/T, R | T |
| C14 | D, D/T | T |
| C15 | D, D/T, WA | T, WA |
| C16 | R, WA | R, WA |
| C17 | D, D/T | T |
| C18 | D, D/T, WX | T, WX |
| C19 | D/London/Qonto, D/T/London/Qonto | T/London/Qonto |
| C20 | D, D/T, R | R, T |


Pour **FACTURE RCT OCTOBRE**, les copies WA des deux Mini portent `Birth=23/11/2022 20:34:58`, tandis que les copies Fichiers portent `06/12/2022 16:40:58`. Pour **Fattura-37**, l’exemplaire WX porte `27/10/2022 16:05:22` dans les deux sauvegardes ; la copie TP-02 dans D/T porte une seconde de plus. Les autres dates WA sont identiques à celles du contenu correspondant dans Fichiers.

L’exemplaire local **FACTURE RCT NOVEMBRE** porte, sur les deux Mini, l’attribut `com.whatsapp.original` contenant le chemin du média WhatsApp identique retrouvé. C’est un indice d’association à un média WhatsApp, sans preuve autonome du sens ou de la date d’un export.

**Aucun des 72 objets correspondants examinés n’est situé dans un domaine iCloud Drive ou un magasin de pièces jointes Mail.** Cela décrit les exemplaires retrouvés ; la couverture d’une sauvegarde logique et la sélection de candidats ne permettent pas d’exclure un autre exemplaire ancien, supprimé, exclu de sauvegarde ou non sélectionné. L’application ayant réalisé chaque enregistrement ou export le 15 octobre reste indéterminée. La présence dans Fichiers, WhatsApp ou WeChat ne signifie pas que ces applications ont créé le contenu PDF.

## Rapprochement temporel nouveau avec TP-03

Les attributs `com.apple.lastuseddate#PS` sont présents sous forme de 16 octets. Leur décodage retenu est celui de deux entiers signés de 64 bits en ordre little endian : secondes Unix et nanosecondes. Les valeurs obtenues ont des nanosecondes valides et des dates cohérentes avec les autres métadonnées. Cette lecture est une interprétation technique des octets conservés, pas un journal certifié de gestes effectués sur le téléphone. Les octets bruts restent disponibles pour contre-vérification.

Dans TP-03, **17 objets représentant 17 contenus** portent cet attribut dans la fenêtre du 15 octobre. Le tableau compare sa valeur à la **première** date de création DNEF du même contenu. L’écart est « date DNEF moins attribut TP-03 ». Les doublons ultérieurs du CSV ne sont donc pas utilisés pour choisir artificiellement un meilleur écart.

| Contenu | Première création DNEF le 15/10 | Attribut lastused TP-03 | Écart | LastStatusChange TP-03 |
| --- | --- | --- | --- | --- |
| C01 | 13:41:15.08 | 13:41:24.049649000 | -8.970 s | 15/10/2024 13:41:24 |
| C02 | 13:42:07.43 | 13:41:56.911901950 | +10.518 s | 09/12/2024 17:41:25 |
| C03 | 13:42:17.78 | 13:42:15.709447860 | +2.071 s | 15/10/2024 13:42:15 |
| C04 | 13:42:42.91 | 13:42:36.864924907 | +6.045 s | 15/10/2024 13:42:36 |
| C05 | 13:42:57.93 | 13:42:55.987134933 | +1.943 s | 15/10/2024 13:42:56 |
| C06 | 13:43:14.37 | 13:43:10.405284881 | +3.965 s | 15/10/2024 13:43:10 |
| C07 | 13:43:49.39 | 13:43:46.159396171 | +3.231 s | 15/10/2024 13:43:46 |
| C08 | 13:43:59.91 | 17/09/2025 14:53:07 | hors fenêtre | 17/09/2025 14:53:07 |
| C09 | 13:44:27.28 | 13:44:26.779971122 | +0.500 s | 15/10/2024 13:44:26 |
| C10 | 13:44:42.58 | 13:44:35.959236145 | +6.621 s | 15/10/2024 13:44:35 |
| C11 | 13:44:58.12 | 09/12/2024 17:48:52 | hors fenêtre | 09/12/2024 17:48:52 |
| C12 | 13:46:40.81 | 09/12/2024 17:46:58 | hors fenêtre | 09/12/2024 17:46:58 |
| C13 | 13:47:09.27 | 13:47:07.667662143 | +1.602 s | 15/10/2024 13:47:07 |
| C14 | 13:48:00.48 | 13:47:58.336755990 | +2.143 s | 15/10/2024 13:47:58 |
| C15 | 13:48:21.63 | 13:48:17.026661872 | +4.603 s | 15/10/2024 13:48:17 |
| C16 | 13:48:33.54 | 13:48:32.444542884 | +1.095 s | 15/10/2024 13:48:32 |
| C17 | 13:48:58.6 | 13:48:56.503203868 | +2.097 s | 15/10/2024 13:48:56 |
| C18 | 13:49:59.36 | 13:49:59.141520023 | +0.218 s | 15/10/2024 13:49:59 |
| C19 | 13:50:13.57 | 13:50:11.148422956 | +2.422 s | 15/10/2024 13:50:11 |
| C20 | 13:50:25.86 | 13:50:23.397071838 | +2.463 s | 15/10/2024 13:50:23 |


Les 17 rapprochements se situent tous à moins de 11 secondes en valeur absolue. Pour **16** de ces objets, `LastStatusChange` est daté dans cette même séquence ; pour **TR Urgent**, ce champ a une date ultérieure mais l’attribut lastused conserve celle du 15 octobre. Les trois contenus dont l’attribut actuel est ultérieur sont C08, C11 et C12 : leur absence de valeur dans la fenêtre ne démontre pas une absence d’activité ce jour-là.

Exemple particulièrement précis : **Rép Dossier bourarach.pdf** a dans TP-03 `Birth=17/12/2019 19:20:21`, un attribut lastused au **15/10/2024 13:42:55,987134933**, puis `LastStatusChange=13:42:56`. Le CSV lui attribue une création à **13:42:57,930**. L’écart est de **1,943 seconde** environ. TP-02 contient deux copies identiques de ce PDF, mais leurs attributs lastused actuels sont datés du 28 octobre vers 23 h 36 et 23 h 53.

**Ce faisceau favorise l’historique de données conservé dans TP-03 pour la séquence de traitements du 15 octobre.** Il ne permet pas de transformer les dates DNEF en dates `Birth` du téléphone. Les attributs de dernière utilisation peuvent être réécrits ou transportés ; leur nom et leur proximité avec les dates de changement ne prouvent pas une consultation humaine ni un export direct. L’absence de valeur comparable dans l’état tardif de TP-02 ne prouve pas que TP-02 n’a jamais connu ces traitements.

## Portée de l’inventaire et réponse à l’identification du Mini

Le rapport OP-01 relevait pour les 27 PDF une création NTFS `$STANDARD_INFORMATION` le 15 octobre et une création `$FILE_NAME` le 28 octobre. **Le constat nouveau ne valide pas la déduction de la note cliente selon laquelle la date SI serait nécessairement la date de création sur le téléphone source.** Les `Birth` des exemplaires sauvegardés ne portent précisément pas ces dates du 15. Le mécanisme qui a produit la date de création inventoriée reste à établir.

Le CSV permet maintenant de dire que les **20 contenus**, sous les **27 chemins IPHONE13_MINI**, figurent dans l’inventaire fourni avec les mêmes SHA-512 que les PDF sauvegardés et déjà rapprochés de L16B. Cela lève pour ces entrées la seule réserve ancienne tenant à l’indisponibilité de cet inventaire. Le fichier CSV n’authentifie pas à lui seul le CD ou son origine administrative ; le contenu d’`Archive_saddedine.zip` et le support effectivement emporté n’ont pas été examinés ici.

Les sauvegardes sont postérieures aux faits : les métadonnées de TP-03 portent septembre 2025 et son `Info.plist` manque ; celles de TP-02 présentent des dates de septembre/octobre 2026 dont l’écart reste documenté dans son rapport. Elles ne constituent pas des acquisitions contemporaines d’octobre 2024. L’héritage ancien des dates et des fichiers communs empêche une attribution matérielle exclusive.

**Réponse Q1 utilisable :** les contenus existaient sous forme de PDF avec des métadonnées anciennes, et se retrouvent dans le stockage local Fichiers des deux Mini, avec des exemplaires supplémentaires WhatsApp et WeChat pour certains. Les métadonnées internes renseignent partiellement le logiciel de génération ancien. Une création des PDF le 15 octobre entre 13 h 41 et 13 h 50 n’est pas démontrée. Les attributs de 17 contenus constituent en revanche un indice temporel nouveau et concordant en faveur de TP-03 pour l’installation concernée par la séquence, sans certifier un transfert direct, une manipulation humaine, un auteur ou le numéro de scellé.

## Pièces et reproduction

- [Annexe privée des 72 objets](../travaux-techniques/recherche-Q1-20261114/prive/annexe-objets.md) : chemins exacts, `fileID`, empreintes, création, modification, changement, attribut lastused, métadonnées PDF et lignes du CSV.
- [Résultats structurés et attributs bruts](../travaux-techniques/recherche-Q1-20261114/prive/attributs-et-chronologie.json) et [résultats de la première passe](../travaux-techniques/recherche-Q1-20261114/prive/resultats.json). Les plists MBFile originaux extraits des manifestes sont conservés avec leurs copies de travail.
- [Script de vérification](../travaux-techniques/recherche-Q1-20261114/scripts/verifier_q1.py) et [script de rédaction et décodage](../travaux-techniques/recherche-Q1-20261114/scripts/rediger_q1.py). Le second export retire `EncryptionKey` de sa représentation JSON ; les preuves brutes restent privées.

Commandes exécutées sur SIFT, depuis le partage du projet :

```sh
python3 /media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/scripts/verifier_q1.py /media/shared/codeProjects/DMMConseils /media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive
python3 /media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/scripts/rediger_q1.py /media/shared/codeProjects/DMMConseils
```

Les scripts refusent de remplacer leurs sorties. Pour reproduire, adapter dans une copie les destinations vers un dossier neuf. Les accès SSH ont utilisé `ssh -F /home/chris/.ssh/config sift` : la commande simple `ssh sift` rencontrait une erreur locale de permissions sur la configuration SSH système. Une exploration préliminaire d’attributs a échoué sur l’agrégation des noms de clés ; elle a été corrigée, puis tous les attributs utiles ont été relus par le script conservé. Aucun résultat d’une passe échouée n’est utilisé comme preuve d’absence.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe DOnnat — Donnat Dev
