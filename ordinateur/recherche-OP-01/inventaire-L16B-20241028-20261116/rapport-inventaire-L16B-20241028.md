# Inventaire des fichiers de C:\L16B d’après les traces Windows — 28 octobre 2024

**OP-01 — relevé établi le 16 novembre 2026.** La recherche porte sur les chemins des fichiers présents dans l’image acquise et sur les traces historiques conservées. Elle ne représente pas une capture du dossier réalisée le 28 octobre 2024.


## Réponse en langage courant

**Les 1 559 entrées sont des chemins historiques, pas 1 559 contenus présents simultanément ni 1 559 fichiers définitivement saisis.** J’ai distingué 1 555 chemins actuels avec création de nom le 28 octobre (A), trois anciens chemins supprimés dont les contenus sont récupérés (B), et un chemin de sortie PDF référencé sans fichier actuel à cet endroit (C). Le dossier actuel contient aussi trois créations de 2026, exclues de ce total historique.

Je privilégie un enchaînement de regroupements et de sorties intermédiaires, car les traces de corbeille et d’impression expliquent les anciens chemins. Leur rapport à l’inventaire de saisie relève du [contrôle exhaustif des contenus](../comparaison-L16B-inventaire-20261116/rapport-comparaison-L16B-inventaire.md), distinct de cette reconstitution de chemins.

## Résultat

**1 559 chemins de fichiers sont retenus comme identifiés ou référencés au cours du 28 octobre 2024**, avec trois niveaux de constat :

| Classe | Nombre | Constat |
|---|---:|---|
| A | **1 555** | Fichiers présents sous L16B dans l’image et portant une création FN le 28/10/2024. |
| B | **3** | Anciens chemins L16B explicitement enregistrés dans la corbeille comme supprimés le 28/10/2024 ; contenus récupérés. |
| C | **1** | Ancien chemin de sortie PDF consigné le 28/10/2024 dans PrintService et une Jump List, sans fichier actuellement à ce chemin. |

**La liste compte des chemins, pas des fichiers présents simultanément en fin de journée ni des contenus uniques.** Les trois fichiers de classe B ont été retirés avant la fin des opérations ; le chemin de classe C peut avoir porté des versions successives ou être lié à un déplacement.

## Accès aux listes intégrales

- [Liste complète lisible : tous les chemins, tailles et dates](liste-complete-fichiers-28oct2024.md).
- [CSV détaillé des 1 559 chemins, avec métadonnées et références](fichiers-rattaches-au-28oct2024.csv).
- [Liste texte : un chemin par ligne](liste-chemins-28oct2024.txt).
- [Traces de 2026 et chemins incertains exclus du total](traces-posterieures-ou-incertaines.csv).
- [Toutes les données et références structurées](inventaire-detaille.json).

Les CSV sont en UTF-8 avec BOM et séparateur point-virgule ; ils peuvent être ouverts et filtrés dans un tableur.

## Fichiers présents dans l’image : rattachement FN au 28 octobre

| Ensemble | Fichiers de classe A |
|---|---:|
| GDRIVE | 93 |
| iCloud Drive | 8 |
| LOCAL | 1389 |
| MESSAGERIES | 33 |
| SAGE | 1 |
| SHINE | 1 |
| TELEPHONES | 30 |

**1 558 fichiers** sont présents sous L16B dans l’inventaire de l’image. Parmi eux, **1 555** ont une création FN le 28/10/2024, pour un total de **4519451973 octets**. Les trois autres portent des créations FN en 2026 et sont présentés séparément. Les archives et les versions développées peuvent contenir les mêmes données ; le total ne mesure pas des données uniques.

## Anciens chemins du 28 octobre absents du dossier actuel

| Ancien chemin | Trace Windows datée | État du contenu / limite |
|---|---|---|
| C:\L16B\LOCAL\Téléchargements - Raccourci (2) - Copie.lnk | $I de la corbeille : suppression 2024-10-28T11:02:53.322000+01:00 | Contenu $R récupéré, 758 octets ; SHA-256 et copie dans le CSV détaillé. |
| C:\L16B\LOCAL\Téléchargements - Raccourci (2).lnk | $I de la corbeille : suppression 2024-10-28T11:02:53.315000+01:00 | Contenu $R récupéré, 758 octets ; SHA-256 et copie dans le CSV détaillé. |
| C:\L16B\Sage.pdf (aussi consigné `C:\L16B\sage.pdf`) | PrintService 307, records **2445** à **15:23:32** (205 pages) et **2450** à **15:28:33** (458 pages) ; Jump List à **15:28:29**. | Chemin de destination référencé ; contenu non retrouvé séparément à ce chemin. Il est distinct du chemin actuel `C:\L16B\SAGE\sage.pdf`. |
| C:\L16B\test.pdf | $I de la corbeille : suppression 2024-10-28T15:24:17.961000+01:00 | Contenu $R récupéré, 499320 octets ; SHA-256 et copie dans le CSV détaillé. |

Pour les trois fichiers de classe B, les dates FN détaillées sont celles de l’objet `$R` actuellement en corbeille ; l’ancien chemin et la date de suppression proviennent de son `$I`. Elles ne sont pas présentées comme les dates d’une entrée FN encore située au chemin d’origine.

`C:\L16B\test.pdf` est aussi corroboré par PrintService 307, record 2429 à 15:19:42, et une Jump List à 15:19:49. Les variations de casse `Sage.pdf` / `sage.pdf` à la racine sont regroupées ; le fichier du sous-dossier `SAGE` reste une entrée distincte.

## Traces exclues du rattachement au 28 octobre 2024

| Chemin | Motif |
|---|---|
| C:\L16B\GDRIVE (2).zip | Création FN 2026-07-27T19:07:00.041614+02:00 |
| C:\L16B\GDRIVE.zip | Création FN 2026-07-27T19:01:33.567163+02:00 |
| C:\L16B\MESSAGERIES\misssmalika@hotmail.com\CADA.pdf.pdf | Création FN 2026-10-02T19:23:38.845102+02:00 |
| C:\L16B\MESSAGERIES\misssmalika@hotmail.com\FA0004 ET FA0005 DE LADMINISTRATION.pdf | Création FN 2026-10-02T19:21:05.972976+02:00 ; suppression 2026-10-02T19:22:23.444000+02:00 ; création SI aussi en 2026 |

**Trois anciennes entrées MFT supplémentaires ont des chemins reconstruits incertains** :

- `C:\L16B\GDRIVE\DMM CONSEILS\Square44x44Logo.targetsize-24_altform-unplated.png` — MFT 736750, parent(s) incertain(s), dates conservées en 2022–2023. Aucune présence sous L16B le 28/10/2024 n’en est déduite.
- `C:\L16B\LOCAL\DMM\Paste.svg` — MFT 943485, parent(s) incertain(s), dates conservées en 2022–2023. Aucune présence sous L16B le 28/10/2024 n’en est déduite.
- `C:\L16B\LOCAL\DMM\Resize.svg` — MFT 961147, parent(s) incertain(s), dates conservées en 2022–2023. Aucune présence sous L16B le 28/10/2024 n’en est déduite.

Le raccourci `Nouveau dossier (2).lnk` désigne `C:\L16B\Nouveau dossier` et mémorise une création de cible le 28 octobre. Son attribut de cible `0x10` confirme qu’il s’agit d’un **répertoire**, pas d’un fichier ; il n’est pas compté parmi les 1 559 chemins. Les autres cibles de répertoires sont conservées dans le JSON.

## Méthode, portée et limites

- Croisement des **1 558 fichiers de l’inventaire L16B** avec leurs enregistrements MFT SI/FN et leurs inodes. Les dates sont converties depuis les UTC des extractions vers **Europe/Paris** ; le 28/10/2024, le décalage est UTC+1.
- Lecture de **380566 enregistrements sélectionnés lors du scan complet de la MFT** : toutes les entrées non allouées et les objets de corbeille retenus dans ce scan sont examinés pour les chemins L16B. Les alias courts DOS ne sont pas comptés comme des fichiers supplémentaires.
- Croisement avec les métadonnées `$I`, les contenus `$R` récupérés, les Jump Lists, les raccourcis Recent, PrintService et une extraction indépendante des événements Windows. Les timestamps de la cible mémorisés dans un LNK ne sont pas assimilés à la date d’utilisation du raccourci.
- **Une création FN du 28 octobre étaye le rattachement du chemin à cette journée ; elle ne certifie pas à elle seule l’immutabilité de ses octets depuis 2024.** Les dates SI peuvent être conservées d’une copie source. Les traces Windows ne sont pas des signatures inviolables ni un journal historique exhaustif.
- **1 fichiers de classe A** ont une modification SI postérieure au 28/10/2024. L’ensemble des champs SI/FN est conservé dans les listes pour permettre leur examen.
- Le PST `dmmconseils93300@hotmail.com.pst` est un exemple connu de distinction entre présence du chemin et identité du contenu : il porte des traces du 28 octobre, mais son SHA-512 courant diverge du CSV d’inventaire. Le PST DMM et le ZIP Takeout concordent avec leurs SHA-512 inventoriés ; voir le [rapport des correspondances et de l’intégrité](../correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md).
- Les noms disparus dont les entrées ont été réutilisées, les chemins dont les parents ne peuvent plus être reconstitués et les anciennes versions écrasées peuvent ne laisser aucune trace exploitable. **La liste couvre toutes les traces retenues dans les sources examinées ; elle ne garantit pas tous les fichiers ayant historiquement existé.**
- Le périmètre est celui des fichiers de `C:\L16B`, pas celui de chaque message contenu dans un PST ni de chaque membre interne d’une archive. Les flux NTFS nommés ne sont pas comptés comme des fichiers supplémentaires.
- Le document de gestion de mots de passe et le ZIP Drive récupérés sous `C:\Users\fintm\Downloads` ne sont pas ajoutés à L16B par simple rapprochement de contenu avec ses 93 fichiers GDRIVE.
- Ce relevé n’établit pas, à lui seul, la composition du jeu définitivement saisi ou le contenu de l’archive emportée. Aucun contenu de document, message ou mot de passe n’est reproduit.

## Sources et reproductibilité

- [ordinateur/recherche-OP-01/extractions-acces/l16b-inventory.json](../extractions-acces/l16b-inventory.json).
- [ordinateur/recherche-OP-01/extractions-acces/l16b-mft.jsonl](../extractions-acces/l16b-mft.jsonl).
- [ordinateur/recherche-OP-01/fichiers-supprimes/mft-deleted-records.jsonl](../fichiers-supprimes/mft-deleted-records.jsonl).
- [ordinateur/recherche-OP-01/fichiers-supprimes/mft-summary.json](../fichiers-supprimes/mft-summary.json).
- [ordinateur/recherche-OP-01/fichiers-supprimes/recovery-selection.jsonl](../fichiers-supprimes/recovery-selection.jsonl).
- [ordinateur/recherche-OP-01/fichiers-supprimes/recovery-results.jsonl](../fichiers-supprimes/recovery-results.jsonl).
- [ordinateur/recherche-OP-01/fichiers-supprimes/recycle-pairs.json](../fichiers-supprimes/recycle-pairs.json).
- [ordinateur/recherche-OP-01/operations-28oct/interactions-28oct.csv](../operations-28oct/interactions-28oct.csv).
- [ordinateur/recherche-OP-01/integrite-evtx/independent/results.jsonl](../integrite-evtx/independent/results.jsonl).
- [ordinateur/recherche-OP-01/samsung-almu-20261113/resultats/print-events-day.json](../samsung-almu-20261113/resultats/print-events-day.json).
- [investigations/20261019-retour-cliente/resultats/sift/events-16-29oct.json](../../../investigations/20261019-retour-cliente/resultats/sift/events-16-29oct.json).
- [ordinateur/recherche-OP-01/integrite-evtx/independent/raw/lnk/Users/fintm/AppData/Roaming/Microsoft/Windows/Recent/Nouveau dossier (2).lnk](../integrite-evtx/independent/raw/lnk/Users/fintm/AppData/Roaming/Microsoft/Windows/Recent/Nouveau dossier (2).lnk).

- [Script de production](generer_inventaire.py).
- [Empreintes des sources et des livrables](empreintes-provenance.json).

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe Donnat — Donnat Dev
