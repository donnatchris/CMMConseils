# Méthodes, préservation et reproduction

**Campagne ciblée clôturée après audit complet du manifeste et analyse des 55 nouveaux fichiers déchiffrés. La totalité des contenus de la sauvegarde n’a pas été déchiffrée : les critères d’arrêt et les reliquats sont explicites.**

## Sources et ordre de travail

Lecture du cadrage `cmm-attentes-cliente`, du mail et de l’attestation ; examen de `telephones/analyse-TP-02.md`, des résultats et inventaires des campagnes, des deux études Wi-Fi/continuité et des scripts d’inventaire, extraction, analyses temporelles et recoupements. Les journaux `extraction-*/extraction.jsonl` indexent les pièces déjà déchiffrées. Aucun changement de `telephones/analyse-TP-02.md`.

Manifeste complet : `/mnt/data/forensic/SADEDINE-2026/ANALYSES/TP-02/Manifest-decrypted.db`, SHA-256 **cd34919ad3a2cb958e130b6ea7453e71f30fb02336d61f2e1dca0f2fb2b46eeb**, identique après audit. 202928 entrées : flags 1 = 137844, flags 2 = 64907, flags 4 = 177. Flags 1 est le filtre fichiers ordinaires repris de la bibliothèque ; les autres entrées ne sont pas déchiffrées comme fichiers. Tous les objets référencés ordinaires sont présents. Pas d’empreinte intégrale des 95 Gio. Un recensement des noms d’objets trouve 137844 objets et aucun non référencé (`backup-object-census.json`), sans lecture massive des contenus.

L’audit lit toutes les lignes Files avec domaine/chemin/flags/fileID/MBFile, dans tous les domaines. Il n’exporte que Size/Birth/LastModified, aucune clé de chiffrement. Regex thématiques et inclusion des noms opaques/sans extension dans tout domaine, avant toute assertion d’absence. Les types initiaux de `manifest-candidates.csv` sont **présumés** ; les trois colonnes campaign_extraction_status, verified_format et verified_plaintext_sha256 complètent les 55 contenus vérifiés, sans réécrire le statut d’extraction antérieur ; les répertoires/faux positifs restent visibles. `campaign-triage.csv` donne les décisions effectives. Les dates du manifeste ne sont pas utilisées comme événements historiques.

## Préservation et limites documentées

Sources chiffrées en lecture seule, aucune expérience sur TP-02. SQL analytique sur copies `/tmp` avec compagnons présents, `query_only`; aucun `immutable=1` sur ces copies. Les deux premiers audits du manifeste se sont ouverts `mode=ro` avec `query_only`; le dernier audit complet et le script livré utilisent une copie avec ses compagnons et `query_only`. Les WAL/SHM préexistants sont recensés. Le WAL du manifeste est **vide** ; leurs mtimes constatées (09:49:21 Paris) précèdent cette campagne. Les autres lectures analytiques du manifeste se font sur copie et compagnons. Les fichiers sources ne sont pas supprimés ou modifiés.

`source-verification.json` conserve SHA-256 avant/après et références d’extraction de 319 sources principales (312 IPS + 7 bases) et de leurs objets chiffrés : contrôles positifs. La recherche Photos possède son propre contrôle clair/chiffré avant/après, également positif. Les 123 préférences structurées portent un contrôle clair avant/après ; elles ne font pas toutes l’objet d’un nouveau contrôle chiffré dans ce script. Le contrôle de clé sur 3573 contenus est une recherche littérale bornée, pas une validation de toutes les interprétations possibles.

Python **3.14.4**, SQLite **3.46.1**, bibliothèque standard, plistlib/json et zoneinfo Europe/Paris. Bibliothèque de déchiffrement existante documentée 0.11.2 ; 55 nouvelles extractions exécutées avec getpass en TTY, aucun secret stocké dans les arguments/sources/journaux. Les versions et scripts hachés figurent dans les JSON d’opérations. Tous les rapports et pièces sont dans un répertoire 0700 ; fichiers créés sous umask 077. Pas de mot de passe, token, contenu de message, coordonnée ou secret réseau exporté.

Les timestamps IPS gardent les chaînes avec décalage explicite ; UTC et Europe/Paris sont calculés en tenant compte du changement d’heure du 27 octobre. Les colonnes SQL conservent les valeurs brutes et deux tests d’époque (Unix/Cocoa) ; les bornes et cohérences ne valident pas à elles seules la sémantique de chaque colonne. ZTOMBSTONE3 reste une hypothèse de conversion. Les ticks IPS restent bruts avec un contrôle empirique explicitement distinct d’une timebase prouvée.

## Reproduction des opérations effectuées

Depuis la racine du projet, exécuter dans cet ordre sur une **copie du répertoire de résultats** si l’on souhaite préserver cette passe : les scripts réécrivent leurs propres sorties, jamais les sources.

```sh
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/audit_manifest.py
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/analyze_system.py
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/inspect_preferences.py
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/recover_photo_metadata.py
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/crash_key_crosscheck.py
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/finalize_evidence.py
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/write_reports.py
python3 telephones/recherche-TP-02/investigation-systeme-oct2024/check_deliverables.py
```

Les scripts utilisent le chemin de sortie fixé à ce dossier : adapter O à un nouveau dossier pour une reproduction conservant la passe. La sélection d’extraction est conservée ; sa constitution exacte est documentée dans `selection-method.json`. Le manifeste ne sera pas déchiffré expérimentalement à nouveau.

La première exécution d’analyze_system a rencontré un scalaire non-BLOB dans FrontBoard ; correction du tri de signatures par type puis exécution complète réussie. La première sérialisation du résultat Photos a rencontré ZQUERYGEN binaire ; correction en export hex explicite puis exécution complète réussie. Ces erreurs concernent uniquement les scripts/copies et la création de résultats, pas les sources ni un déchiffrement. Les logs finaux couvrent les exécutions réussies.

## Déchiffrement exécuté et reproduction du complément

```sh
telephones/scripts/.venv-iphone/bin/python telephones/scripts/tp02_forensic.py extract \
  --inventory telephones/recherche-TP-02/investigation-systeme-oct2024/selection-extraction.csv \
  --max-priority 1 \
  --out telephones/recherche-TP-02/investigation-systeme-oct2024/extraction-nouveaux
```

Saisir le mot de passe **uniquement à l’invite interactive** du terminal, jamais dans la conversation/arguments/environnement/script. Sélection 48 fichiers, estimation 7050475 octets ; destination nouvelle. Inspecter chaque statut extraction.jsonl, vérifier clair/chiffré, garder les éventuels compagnons. L’extraction initiale est terminée, 48 statuts ok, zéro écart de taille. La sélection-pegasus.csv ajoute 7 fichiers, tous ok, vers extraction-pegasus. Les deux journaux sont conservés. Aucune saisie ou extraction n’est en attente.

## Références de format consultées

[Apple — JSON IPS](https://developer.apple.com/documentation/xcode/interpreting-the-json-format-of-a-crash-report), [champs et clé diagnostique](https://developer.apple.com/documentation/xcode/examining-the-fields-in-a-crash-report), [horloge absolue](https://developer.apple.com/documentation/kernel/1462446-mach_absolute_time), [SQLite — format et espaces internes](https://www.sqlite.org/fileformat.html). Elles définissent des formats généraux ; elles ne certifient pas les dates, l’origine physique ou le non-transfert de ces pièces particulières.

## Décodage final et vérifications complémentaires

Exécuter analyze_new_objects.py après les deux extractions : plist/NSKeyedArchive sans instanciation de classes, SQLite sur copies, SEGB1/2 avec signatures/bornes et CRC payload, Protobuf générique sans présumer les noms de champs, LZFSE décompressé sur copie. 55 fichiers, 24 SEGB, 14618 enveloppes : 9507 états 1/CRC valides, 5111 états 3/payload nul. 47 observations centrales, toutes le 28. Les offsets/valeurs brutes sont conservés ; les timestamps ne sont pas authentifiés par leur CRC de payload.

Le module lzfse 0.4.2 (archive publique de 48 kB) a été téléchargé ; l’installation Python sans build isolation a échoué faute de setuptools. Aucun échec de décodage forensic n’en découle : compilation locale de quatre fichiers C du décodeur de référence retenu, puis appel ctypes réussi. Archive source, licences et binaire conservés sous vendor ; compilation **cc Ubuntu 15.2.0-16ubuntu1**, sans modification de l’environnement Python existant. Le premier essai réseau dans le bac à sable a échoué en DNS ; téléchargement public autorisé ensuite, aucune donnée forensic envoyée.

Commande de compilation (noms de fichiers dans vendor/lzfse-0.4.2/lzfse/src) : `cc -shared -fPIC -O2 -I <src> <src>/lzfse_decode.c <src>/lzfse_decode_base.c <src>/lzvn_decode_base.c <src>/lzfse_fse.c -o vendor/liblzfse-tp02.so`. Les valeurs numériques des adresses/code/tailles ne sont pas des secrets. Les sources originales sont restées inchangées ; empreintes des 55 clairs et chiffrés avant/après et par comparaison aux extractions dans new-source-verification.json.

Ordre de reproduction après l’analyse initiale : analyze_new_objects.py, finalize_evidence.py, write_reports.py, close_campaign.py, check_deliverables.py. close_campaign.py applique les conclusions finales et reconstruit la chronologie à partir des nouvelles observations ; ne pas livrer les templates intermédiaires produits par write_reports.py seuls. La chronologie comporte 49 observations (2 du même IPS + 47 SEGB), pas 49 gestes ni preuves indépendantes. Les candidats résiduels ne sont pas tous déchiffrés.

Références primaires supplémentaires : [CCL — parseur SEGB](https://github.com/cclgroupltd/ccl-segb), [code v1](https://github.com/cclgroupltd/ccl-segb/blob/master/ccl_segb/ccl_segb1.py), [code v2](https://github.com/cclgroupltd/ccl-segb/blob/master/ccl_segb/ccl_segb2.py), [états/époque](https://github.com/cclgroupltd/ccl-segb/blob/master/ccl_segb/ccl_segb_common.py), [LZFSE de référence](https://github.com/lzfse/lzfse), [archive/bindings](https://github.com/m1stadev/lzfse). La page Cellebrite suggérée par CCL n’a pas pu être lue (403) et n’est pas utilisée comme preuve de sémantique. Le nom PegasusConfiguration désigne ici un domaine Apple de cette sauvegarde ; il n’est pas une identification de logiciel espion.
