# Comparaison exhaustive de L16B et de l’inventaire DNEF

**OP-01 — 16 novembre 2026.** Comparaison des chemins dans les deux sens, puis lecture et calcul SHA-512 de chaque fichier inventorié dans l’image montée en lecture seule sur SIFT.


## Réponse en langage courant

**Trois fichiers diffèrent de l’inventaire par leur contenu : le raccourci USB2, `FACT 2018 SUITE.pdf` et le PST 93300.** J’ai retrouvé les 1 555 chemins attendus et recalculé leurs empreintes : 1 552 concordent et trois divergent. Un chemin retrouvé établit la présence d’un nom ; une empreinte concordante établit l’identité des octets comparés au CSV. Pour les trois différences, je ne peux pas classer version différente, modification ultérieure ou erreur d’inventaire sans disposer des fichiers correspondant aux empreintes attendues.

Les trois fichiers supplémentaires datés de 2026 et les anciens chemins intermédiaires du 28 octobre ne sont pas trois nouveaux manquements au CSV. Ils relèvent de périmètres et d’étapes différents, explicités ci-dessous. Le contrôle exhaustif conserve tous les chemins et empreintes ; l’archive finale et le support d’origine du CSV restent les pièces prioritaires.

## Introduction — Ce qui est comparé

### L’inventaire de saisie fourni

Le fichier [Inventaire_saddedine.csv](../../../inventaire-DNEF/documents-recus/Inventaire_saddedine.csv) est le **CSV d’inventaire transmis pour les opérations de saisie du 28 octobre 2024**. Son en-tête porte les mentions « inventaire de saisie », « 28 octobre 2024 » et « saddedine » comme nom de machine.

Il recense **1 555 fichiers**, avec, pour chacun, un **chemin Windows**, des **dates de création, de modification et d’accès**, ainsi qu’une **empreinte SHA-512**. Cette empreinte est une valeur calculée à partir des octets du fichier : elle permet de vérifier si un fichier retrouvé correspond au contenu décrit par l’inventaire, au-delà de son seul nom. Le présent contrôle utilise ce CSV tel qu’il a été fourni ; son support d’origine n’a pas été examiné.

### Le dossier L16B sur l’ordinateur OP-01

**`C:\L16B` est un dossier de regroupement situé sur le disque interne de l’ordinateur OP-01.** Le [procès-verbal de saisie](../../../docs/PV%20DE%20SAISIE.pdf) décrit sa constitution lors des opérations du 28 octobre 2024, après ouverture du scellé de l’ordinateur. Il rassemble notamment des copies de documents locaux, des données Google Drive et iCloud, des exports de messageries, des documents Sage et SHINE, ainsi que des fichiers et conversations provenant des téléphones.

Le PV décrit ensuite une sélection, un filtrage et une copie finale sur un support de l’administration. Il précise que les dossiers créés sont **laissés sur l’ordinateur à titre informatif**, avec l’accord de Mme Sadedine. **La seule présence d’un fichier dans L16B ne certifie donc pas qu’il a été retenu dans le jeu définitivement emporté.** La comparaison à l’inventaire et aux empreintes sert précisément à dépasser ce seul constat de présence locale.

Le dossier analysé ici est celui conservé dans **l’image du disque d’OP-01 acquise en 2026**, qui contient **1 558 fichiers sous L16B**. Dans ce rapport, les expressions « actuellement présent » et « fichier dans l’image » désignent cet état de l’image, et non une observation directe du dossier au 28 octobre 2024. Des traces Windows permettent de retrouver aussi d’anciens chemins et des suppressions ; certains fichiers portent par ailleurs des dates de création en 2026.

### Les questions auxquelles répond la comparaison

Le rapport rapproche **la liste et les empreintes du CSV de 2024** des **fichiers présents dans l’image de 2026**, en complétant ce rapprochement par les traces Windows historiques :

1. **Comparaison des chemins dans les deux sens :** quels fichiers de L16B ne sont pas inscrits dans le CSV, et quels chemins inscrits dans le CSV ne sont plus retrouvés dans L16B ?
2. **Comparaison des contenus :** pour chaque chemin inventorié retrouvé, le SHA-512 du fichier de l’image est-il identique à celui du CSV ? Un même nom peut désigner un contenu différent.
3. **Examen des anciens chemins :** des fichiers supprimés ou des chemins intermédiaires sont-ils attestés le 28 octobre 2024, sans figurer dans l’inventaire ? Les traces postérieures et les chemins incertains sont distingués de ces constats.

**Un écart de liste ne révèle pas, à lui seul, la raison du filtrage.** Il peut notamment concerner un fichier apparu plus tard, un doublon, un fichier temporaire, un ancien chemin ou une suppression. Le fichier de rejets et l’archive finale n’ayant pas été récupérés, les écarts constatés ne sont pas présentés comme une liste officielle de documents volontairement écartés. Une concordance SHA-512 établit l’identité du contenu retrouvé avec l’empreinte du CSV fourni ; elle ne démontre pas sa lecture par une personne ni son utilisation ultérieure.

## Réponse

**Aucun fichier du CSV n’est absent de L16B par son chemin : les 1 555 chemins de l’inventaire sont tous présents dans l’image.** Ces chemins correspondent exactement au groupe des 1 555 fichiers actuels portant une création FN du 28/10/2024 dans le relevé Windows précédent.

**L16B contient trois fichiers supplémentaires**, dont les créations FN sont datées de 2026. Les traces Windows du 28/10/2024 identifient en outre **quatre anciens chemins** absents du CSV. **Ces écarts ne constituent pas une liste officielle de fichiers écartés lors du filtrage.**

**Sur les 1 555 contenus contrôlés, 1 552 SHA-512 sont identiques au CSV et 3 divergent.** Les trois fichiers divergents existent au chemin inventorié, mais leurs octets actuels ne correspondent pas à l’empreinte qui figure dans cet inventaire.

| Contrôle | Résultat |
|---|---:|
| Lignes de fichiers dans le CSV / chemins distincts | **1 555 / 1 555** |
| Fichiers actuellement présents sous L16B dans l’image | **1 558** |
| Chemins communs au CSV et à L16B | **1 555** |
| Chemins du CSV absents de L16B | **0** |
| Fichiers actuels de L16B absents du CSV | **3** |
| Anciens chemins du 28/10/2024 absents du CSV | **4** |
| SHA-512 identiques / divergents / erreurs de lecture | **1 552 / 3 / 0** |

## 1. Fichiers actuellement dans L16B mais absents du CSV

| Chemin | Taille (octets) | Création FN, heure de Paris |
|---|---:|---|
| `C:\L16B\GDRIVE (2).zip` | 61847396 | 2026-07-27T19:07:00.041614+02:00 |
| `C:\L16B\GDRIVE.zip` | 61847396 | 2026-07-27T19:01:33.567163+02:00 |
| `C:\L16B\MESSAGERIES\misssmalika@hotmail.com\CADA.pdf.pdf` | 304207 | 2026-10-02T19:23:38.845102+02:00 |

**Ces trois chemins portent des créations FN en 2026.** Leur absence d’un inventaire daté du 28 octobre 2024 ne permet donc pas de les présenter comme des fichiers rejetés en 2024. Les deux ZIP GDRIVE sont distincts du dossier développé GDRIVE, dont les 93 fichiers figurent dans le CSV.

## 2. Anciens chemins du 28 octobre 2024 absents du CSV

| Ancien chemin | Trace Windows | Contenu et portée |
|---|---|---|
| `C:\L16B\LOCAL\Téléchargements - Raccourci (2) - Copie.lnk` | Suppression vers la corbeille 2024-10-28T11:02:53.322000+01:00 | Contenu récupéré ; son SHA-512 ne correspond à aucune des 1 555 empreintes du CSV. |
| `C:\L16B\LOCAL\Téléchargements - Raccourci (2).lnk` | Suppression vers la corbeille 2024-10-28T11:02:53.315000+01:00 | Contenu récupéré ; son SHA-512 ne correspond à aucune des 1 555 empreintes du CSV. |
| `C:\L16B\Sage.pdf` | PrintService 307 : 205 pages à 15:23:32, 458 pages à 15:28:33 ; Jump List à 15:28:29. | Chemin intermédiaire référencé ; contenu non récupéré séparément à cette racine. |
| `C:\L16B\test.pdf` | Suppression vers la corbeille 2024-10-28T15:24:17.961000+01:00 | Contenu récupéré ; son SHA-512 ne correspond à aucune des 1 555 empreintes du CSV. |

Les deux raccourcis supprimés ont un contenu binaire identique entre eux ; leurs deux chemins sont distincts. `test.pdf` est un PDF de deux factures dont le texte est repris dans le PDF Sage final, selon le contrôle déjà documenté : l’absence de ce fichier autonome dans le CSV ne prouve pas l’absence de ces factures dans les données conservées.

**Ne pas confondre** `C:\L16B\Sage.pdf` avec `C:\L16B\SAGE\sage.pdf`. Le second figure dans le CSV et son SHA-512 est concordant. Les graphies `Sage.pdf` / `sage.pdf` à la racine sont regroupées comme un même chemin Windows ; le mécanisme exact reliant ce chemin intermédiaire au fichier du sous-dossier n’est pas établi ici.

Une suppression dans le dossier de travail, un doublon ou un changement de chemin peut expliquer un écart de liste sans correspondre à une décision de filtrage. Le fichier `Rejets_saddedine.txt` et l’archive finale n’ont pas été récupérés. **Le motif de l’absence de ces quatre chemins du CSV n’est pas déterminé.**

## 3. Fichiers inventoriés présents au chemin attendu mais de contenu divergent

| Chemin inventorié | Ligne du CSV | Taille actuelle (octets) | SHA-512 |
|---|---:|---:|---|
| `C:\L16B\LOCAL\cle usb\USB2 (D) - Raccourci.lnk` | 426 | 940 | **DIVERGENT** |
| `C:\L16B\LOCAL\FACT 2018 SUITE.pdf` | 481 | 924117 | **DIVERGENT** |
| `C:\L16B\MESSAGERIES\dmmconseils93300@hotmail.com.pst` | 1497 | 1156260864 | **DIVERGENT** |

Les deux nouveaux écarts, le raccourci USB2 et le PDF FACT 2018 SUITE, sont confirmés par un calcul indépendant `sha512sum` sur SIFT. Le PST 93300 avait déjà été confirmé indépendamment ; son empreinte actuelle est inchangée par rapport à ce contrôle. La date, la cause et l’auteur des différences ne sont pas déterminés par cette comparaison.

**Il n’y a donc aucun chemin manquant dans L16B, mais trois contenus actuels qui ne correspondent pas à leur version inventoriée.** Cela ne prouve pas que les versions inventoriées sont absentes de toute l’image ou d’un autre support ; elles ne sont pas retrouvées à l’identique dans les fichiers actuellement présents à ces trois chemins.

### Empreintes complètes des trois divergences

#### C:\L16B\LOCAL\cle usb\USB2 (D) - Raccourci.lnk

Inventaire :

```text
4d58c12d456e7496db41ea2dc6c5b0274b406f48585ad775ccd027c951b22508f4d1b5b690c63af0f33ce02385c57e413d11a2223899dc3f1476d03a714f4e55
```

Fichier dans l’image :

```text
54da56d32e0f1a700fa3c2c20ff918884e9054cfcb74d45b6c1aff1eea4a9660158391872994e1352d1e66f33e77d6bdc1da1c90a19835db7ec59a3ed51948a3
```

#### C:\L16B\LOCAL\FACT 2018 SUITE.pdf

Inventaire :

```text
21ff3ab5c808251a475bb442317ae3aa07b115e3050e082228d506425b37301f7833680f0b5c698554c821e78527f0ce51554f5d3b9776dc3be39affb2cee524
```

Fichier dans l’image :

```text
dd4705eb6ca387aeef77eae149b758c11bfbc7e7d97d1c235adb14c17fd3df31e01a996716cfc91f06022f381fadaf666039f9b3fb60c5775329f082ccd95084
```

#### C:\L16B\MESSAGERIES\dmmconseils93300@hotmail.com.pst

Inventaire :

```text
9a523a8a621bd4364caea02e0a7c0a8953a6e3ca57d1d31d85df03932ad9a9b9c70aec6516a97ad09ec4131a3cf7ee16bcbb0c6573a870d0522affc8b11cb62c
```

Fichier dans l’image :

```text
1949987f20fced4a2b0a3c6c4000e5afb8a54e5ec8b08c667ed5397feab60ad18b87fe0a78348ee4b992306cfd8773eb53a3560e6ba82bd6d86e79523ec03361
```

## 4. Autres traces qui ne démontrent pas un écart de 2024

- Le chemin historique `C:\L16B\MESSAGERIES\misssmalika@hotmail.com\FA0004 ET FA0005 DE LADMINISTRATION.pdf`, également absent du CSV, est connu par une création et une suppression **du 2 octobre 2026**. Il est conservé dans le relevé Windows, mais pas présenté comme un fichier de L16B du 28/10/2024.
- Trois anciens chemins reconstruits à partir de parents MFT incertains (`Square44x44Logo.targetsize-24_altform-unplated.png`, `Paste.svg`, `Resize.svg`) ne sont pas retenus comme fichiers L16B établis en 2024.

## 5. Méthode et limites

- CSV fourni : `inventaire-DNEF/documents-recus/Inventaire_saddedine.csv`, **1 555 lignes de fichiers**, sans doublon de chemin. SHA-256 du CSV : `f2a4e9d05cca5c7b8082da42df76fca45e870f3e3acbbdf6ff03c07e68293c40`.
- Comparaison de tous les chemins Windows, sans tenir compte de leur casse ; les séparateurs sont harmonisés. Les chaînes de chemins du CSV sont également identiques à celles des 1 555 entrées de classe A du relevé Windows.
- Inventaire direct du dossier `L16B` de l’image montée : **1 558 fichiers**. Contrôle du montage NTFS **en lecture seule** et de la boucle EWF **en lecture seule** avant tout calcul.
- Lecture intégrale et SHA-512 de chacun des **1 555 fichiers inventoriés**, soit **4519451973 octets**. Les tailles, inodes et dates de modification restent identiques pendant la lecture ; **aucune erreur** n’est enregistrée.
- Le CSV a la même empreinte avant et après le contrôle. Les trois SHA-512 de messageries déjà contrôlés concordent avec la nouvelle passe exhaustive.
- Pour les trois fichiers de corbeille du 28/10/2024, SHA-512 des copies récupérées et comparaison à toutes les empreintes du CSV : aucune correspondance exacte ailleurs dans cet inventaire.
- Le rapprochement porte sur les fichiers et les empreintes de **l’inventaire fourni**. Il ne certifie pas à lui seul l’authentification du support d’origine du CSV, la composition ou la conservation actuelle de l’archive finale, ni les raisons du filtrage.

## 6. Références et livrables

- [CSV d’inventaire fourni](../../../inventaire-DNEF/documents-recus/Inventaire_saddedine.csv).
- [Comparaison exhaustive des 1 555 SHA-512 — CSV filtrable](comparaison-SHA512-tous-les-fichiers.csv).
- [Écarts de chemins — CSV](ecarts-de-chemins.csv).
- [Résultats complets et paramètres du montage](resultats-comparaison-L16B-inventaire.json).
- [Calculs individuels journalisés](comparaison-SHA512-complete.jsonl).
- [Confirmations indépendantes et contenus récupérés](confirmations-independantes.json).
- [Relevé des fichiers datables du 28 octobre et exclusions](../inventaire-L16B-20241028-20261116/rapport-inventaire-L16B-20241028.md).
- [Rapport des correspondances et de leur concordance à l’inventaire](../correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md).
- [Analyse OP-01, suppressions et PDF Sage](../../analyse-ordinateur.md).
- [Recherche de récupération de l’archive finale et des rejets](../../../inventaire-DNEF/rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md).
- [Script de comparaison sur SIFT](comparer_sift.py).

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe DOnnat — Donnat Dev
