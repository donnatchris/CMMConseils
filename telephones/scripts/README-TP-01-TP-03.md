# Outils TP-01, TP-03 et recoupements du 10 novembre 2026

Les scripts lisent les sources et travaillent dans des destinations **nouvelles**, hors acquisitions. Les sauvegardes originales ne sont jamais une destination. Les résultats peuvent contenir des données personnelles : conserver les répertoires avec accès restreint, hors Git. Aucun mot de passe dans les arguments ou les fichiers ; les collecteurs chiffrés utilisent `getpass` dans un terminal interactif.

Environnement réellement utilisé : SIFT, Python 3.12.3, SQLite 3.45.1. TP-03 : `iphone_backup_decrypt` 0.11.2 et pycryptodome 4.4.0 installés dans `/home/sansforensics/analysis/tp03-dependencies-20261110`, sans modifier la source. La création initiale d’un venv a échoué faute d’ensurepip ; son dossier n’est pas utilisé.

## TP-01 non chiffré

Depuis le projet accessible à SIFT, remplacer SOURCE et DESTINATION par des chemins appropriés :

```bash
python3 telephones/scripts/tp01_inventory.py SOURCE DESTINATION
python3 telephones/scripts/tp01_scan.py DESTINATION DESTINATION/scan
python3 telephones/scripts/tp01_targeted.py DESTINATION
python3 telephones/scripts/tp01_supplement.py DESTINATION SOURCE
```

Pour la campagne réalisée, SOURCE est `/media/shared/forensic/SADEDINE-2026/TP-01/00008110-000A70993407801E` et DESTINATION `/home/sansforensics/analysis/tp01-20261110`. Ne pas réutiliser ce dossier comme nouvelle destination.

La collecte inventorie tout le manifeste et vérifie la présence des objets `flags=1`. Elle copie bases SQLite présumées, compagnons, logs et préférences sélectionnées, puis compare SHA-256 source avant/après/copie. Le complément ajoute le suffixe Wi-Fi `.plist.backup` et les ressources `.ahe` ciblées.

La première passe du scanner interrompait l’analyse de certaines bases lorsque `quick_check` rencontrait un tokenizer/collation absent. La version courante consigne cette limite et lit les tables ordinaires disponibles ; `scan-v2` est la passe de référence TP-01. Les tables virtuelles ne sont pas réputées interprétées.

Le complément auxiliaire a été reproduit avec les bornes exactes dans un nouveau dossier :

```bash
python3 telephones/scripts/tp01_supplement.py DESTINATION SOURCE supplement-v2
```

Les résultats structurés sont identiques ; la première passe reste conservée. Les requêtes natives de `tp01_targeted.py` et les bornes du scanner étaient déjà calculées depuis `Europe/Paris`.

## TP-03 chiffré

Configurer le chemin des dépendances de travail sur SIFT sans modifier HOME :

```bash
TP03_DEPENDENCIES=/home/sansforensics/analysis/tp03-dependencies-20261110
PYTHONPATH="$TP03_DEPENDENCIES" python3 telephones/scripts/tp03_collect.py SOURCE DESTINATION
PYTHONPATH="$TP03_DEPENDENCIES" python3 telephones/scripts/tp03_priority.py SOURCE DESTINATION/Manifest.db PRIORITE PROJET
python3 telephones/scripts/tp01_scan.py DESTINATION DESTINATION/scan
python3 telephones/scripts/tp01_scan.py PRIORITE PRIORITE/scan
python3 telephones/scripts/tp03_findings.py PRIORITE PRIORITE/findings
python3 telephones/scripts/telephones_plists.py DESTINATION DESTINATION/plists
python3 telephones/scripts/tp03_correlations.py DESTINATION
python3 telephones/scripts/tp03_final_checks.py DESTINATION PRIORITE
```

Valeurs de la campagne : SOURCE `/media/shared/forensic/SADEDINE-2026/TP-03/00008110-001249321444801E`, DESTINATION `/home/sansforensics/analysis/tp03-20261110`, PRIORITE `/home/sansforensics/analysis/tp03-priority-20261110`, PROJET : racine du dépôt monté sur la VM. Ces destinations sont déjà occupées : en choisir d’autres pour reproduire.

`tp03_collect.py` conserve le manifeste chiffré et enregistre le manifeste clair séparément, ainsi que l’absence d’Info.plist. Les extractions utilisent l’API par domaine/chemin après vérification du fileID. Les messages de différence de taille de la bibliothèque sont informatifs ; les tailles ne sont pas forcées.

`tp03_priority.py` utilise un accès exact par fileID au manifeste interne, `FilePlist`, l’unwrapping de classe et `_decrypt_file_to_disk` de la version 0.11.2 inspectée. La sélection porte sur bases natives, Wi-Fi, états caméra non multimédias et PDF de nom ou taille comparables à L16B. Les sources sont hachées avant/après ; les contenus déchiffrés reçoivent SHA-256. Les **62 objets communs** à cette passe et à la collecte générale ont des SHA-256 chiffrés et clairs identiques. Les **32 contrôles finaux** et les signatures/taille d’en-tête SQLite complètent cette validation. Les clés et mots de passe ne sont pas exportés.

Le scanner est un outil de tri, pas un classificateur de gestes : six hypothèses époque/unité, filtre de noms de colonnes, puis validation des schémas et requêtes ciblées. La version courante élimine les échelles impossibles au moyen des minima/maxima numériques des colonnes pour éviter des lectures répétitives inutiles. Les bornes viennent du fuseau Paris. Les BLOB, payloads propriétaires, chaînes non prises en charge et espaces supprimés ne sont pas exhaustivement analysés.

Les bases analytiques sont ouvertes en `mode=ro` avec les WAL disponibles sur les copies. `immutable=1` n’est utilisé que pour le manifeste d’inventaire, pas pour ignorer les WAL des bases d’activité. Les éventuels auxiliaires SQLite de lecture appartiennent aux copies de travail, jamais aux sources chiffrées.

## Recoupements

```bash
python3 telephones/scripts/telephones_crosschecks.py PROJET NOUVEAUX_CROISEMENTS
```

Ce script utilise les dossiers SIFT de campagne et l’extraction TP-02 existante, lit les exports Freebox déjà conservés et compare l’UDID TP-03 au résultat de pair record OP-01 du 19 octobre. Il ne contacte aucun service. Pour une reproduction dans d’autres chemins, adapter les racines fixes dans une copie du script. Les adresses clientes et BSSID sont distingués ; l’absence de MAC cliente exploitable de TP-01 limite l’attribution.

Les résultats JSON sont rapatriés dans les dossiers `recherche-TP-01`, `recherche-TP-03` et `investigations/20261110-telephones/prive`. Les archives intermédiaires et les passes initiales restent conservées. Les commandes, scripts et choix de couverture décrits dans les rapports permettent de distinguer analyse nouvelle, contre-lecture et reprise documentaire. Les anciennes campagnes ne sont pas relancées à l’identique.

## Approfondissement TP-03 : intervention humaine le 16 octobre

Le [compte rendu spécifique](../../investigations/20261110-tp03-intervention-humaine/compte-rendu.md) donne les résultats, contre-arguments et limites. Les commandes ci-dessous sont exécutées sur SIFT. GENERAL et PRIORITE désignent les deux copies initiales ; les destinations supplémentaires doivent être **neuves**, car les dossiers de campagne existent déjà.

```bash
python3 telephones/scripts/tp03_human_sequence.py GENERAL PRIORITE NOUVELLE_PASSE_1 TP02_SYSTEME
python3 telephones/scripts/tp03_window_all_columns.py GENERAL PRIORITE NOUVELLE_PASSE_COLONNES
python3 telephones/scripts/tp03_human_controls.py GENERAL PRIORITE NOUVELLE_PASSE_1 NOUVEAUX_CONTROLES
python3 telephones/scripts/tp03_recover_preferences.py GENERAL NOUVELLE_REPRISE_PLISTS
```

`TP02_SYSTEME` vaut `$PROJET/telephones/recherche-TP-02/extraction-systeme-20261014`, où `PROJET` désigne la racine du dépôt sur la VM. Le dernier argument de la première commande est facultatif. Les SQL et empreintes des requêtes ciblées sont conservés ; les SHM des lecteurs sont distingués des bases/WAL. Les échecs du parseur plist standard restent visibles, même après la reprise des trois fichiers concernés.

`tp03_window_all_columns.py` teste les colonnes sans filtre de nom : minima/maxima numériques puis six échelles/époques sur le 16 octobre Paris. Les colonnes explicitement textuelles/BLOB et tables virtuelles restent hors interprétation exhaustive. Une valeur candidate n’est pas automatiquement une preuve d’activité.

`tp03_human_controls.py` compare la répartition des types de changements TipKit pour des groupes du même auteur espacés d’au plus deux secondes. Le profil identique ne signifie ni contenu binaire identique ni gestes identiques. Les valeurs actuelles des paramètres ne reconstituent pas leurs anciennes valeurs.

La sélection supplémentaire conservée dans `investigations/20261110-tp03-intervention-humaine/prive/selection.json` contient exactement `ATXBackupData` et `RecentAppLayouts.pb.lzfse`. Pour une reproduction, contrôler les fileID/domaine/chemin dans l’inventaire avant de réutiliser cette sélection. Déchiffrement avec saisie masquée :

```bash
PYTHONPATH=/home/sansforensics/analysis/tp03-dependencies-20261110 python3 telephones/scripts/tp03_collect_selected.py SOURCE NOUVEAUX_EXTRAS SELECTION_JSON
```

Un décodeur isolé a été installé avec `python3 -m pip install --only-binary=:all: --no-deps --target /home/sansforensics/analysis/tp03-human-dependencies-20261110 lzfse==0.4.2`. Ne pas réinstaller dans ce dossier occupé pour une nouvelle campagne. Décodage :

```bash
PYTHONPATH=/home/sansforensics/analysis/tp03-human-dependencies-20261110 python3 telephones/scripts/tp03_decode_atx.py NOUVEAUX_EXTRAS NOUVEAU_DECODAGE_ATX
```

Le format d’enveloppe ATX est inféré de ce fichier et vérifié par consommation complète des 45 entrées, validation de 44 plists et `quick_check` SQLite. Les huit octets de métadonnées par entrée ne sont pas interprétés. Les champs protobuf de RecentAppLayouts restent numérotés, sans noms fonctionnels inventés ; le décodage de cadrage ne vaut pas validation de toutes leurs significations.

Destinations réellement utilisées : `/home/sansforensics/analysis/tp03-human-20261110`, `tp03-human-window-20261110`, `tp03-human-controls-20261110`, `tp03-human-plist-recovery-20261110`, `tp03-human-extra-20261110`, `tp03-human-atx-20261110` (ces cinq derniers noms ont le même parent `analysis`). Une exploration préliminaire par signatures est conservée dans `tp03-human-extra-20261110/decoded/` ; ses échecs sur des blocs internes incomplets ne sont pas des constats de corruption. La seconde passe structurée `tp03-human-atx-v2-20261110` ajoute le contrôle de toutes les 112 colonnes numériques de la base ATX et constitue la référence finale ; `tp03-human-atx-20261110` reste conservé.

La reprise `tp03_recover_preferences.py` utilise l’API privée de `plistlib` de Python 3.12 pour conserver une date binaire hors plage comme marqueur brut. Elle n’altère pas le fichier, ne remplace pas l’année 0000 par une date plausible et ne répare pas les preuves. L’XML concerné est relu par éléments date.
