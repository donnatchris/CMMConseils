# Outils TP-02

Ces outils lisent la sauvegarde originale sans écriture. Les extractions utilisent `iphone_backup_decrypt` **0.11.2**, Python **3.14.4**, SQLite **3.46.1** dans `telephones/scripts/.venv-iphone`. Les outils d’inventaire et d’analyse utilisent la bibliothèque standard Python. Exécuter depuis la racine du projet.

Les destinations doivent être **nouvelles** : les outils refusent de remplacer un répertoire de résultats existant. L’extraction recueille le mot de passe avec `getpass` dans un terminal interactif ; aucun argument ou fichier de mot de passe n’est prévu. Les pièces déchiffrées peuvent contenir des données confidentielles : leurs permissions sont restreintes et `telephones/recherche-TP-02/` est exclu de Git par son `.gitignore`.

## Inventaire et sélection

```bash
python3 telephones/scripts/tp02_forensic.py inventory \
  --out telephones/recherche-TP-02/inventaire-reproduction
```

Sorties : `inventory.csv` (toutes les entrées du périmètre), `interesting-files.csv` (priorités 1 et 2), `metadata-time-candidates.csv` (dates du manifeste, distinctes des événements applicatifs), `summary.json` (couverture et compteurs). Le périmètre comprend les trois domaines caméras, tous les domaines non applicatifs et les applications Apple natives. Les types sont présumés tant que les signatures déchiffrées ne sont pas vérifiées. Les valeurs MBFile retenues excluent les clés de déchiffrement et les autres BLOB sensibles.

## Extraction sélective

Simulation, sans mot de passe ni écriture de contenus :

```bash
telephones/scripts/.venv-iphone/bin/python telephones/scripts/tp02_forensic.py extract \
  --inventory telephones/recherche-TP-02/inventaire-detaille/inventory.csv \
  --max-priority 2 \
  --domain AppDomain-com.lscsmartconnection.smart \
  --domain AppDomain-com.xiaomi.mihome \
  --domain AppDomainGroup-group.com.xiaomi.mihome \
  --out telephones/recherche-TP-02/extraction-cameras-reproduction \
  --dry-run
```

Retirer `--dry-run` pour déchiffrer. La sélection caméras de cette passe représente 525 fichiers, environ 320 Mo annoncés ; le volume réellement déchiffré diffère du manifeste. Le plafond global par défaut est de 1 Gio (`--max-bytes`). `--max-file-bytes` permet de limiter la taille individuelle, `--file-id` de sélectionner précisément une entrée ; les compagnons WAL/SHM/journal d’une base sélectionnée sont ajoutés depuis le CSV disponible. Le plafond global inclut ces compagnons. Les champs de taille absents ne fournissent pas d’estimation fiable.

Une sélection système déjà préparée est disponible dans `inventaire-detaille/system-priority-selection.csv`. Elle exclut les domaines caméras et les fichiers annoncés au-delà de 256 Mio, notamment `Photos.sqlite`. Elle peut être donnée à `extract --inventory` avec une destination distincte.

L’outil vérifie la correspondance exacte domaine/chemin/fileID dans le manifeste déchiffré de la bibliothèque et écarte une ambiguïté de sa sélection SQL `LIKE`. Il protège les chemins de sortie, conserve la structure logique et journalise SHA-256 du fichier chiffré, SHA-256 du contenu, taille réelle, statut et éventuel écart de taille. Les erreurs enregistrées ne contiennent que leur classe. Les écarts de taille restent documentés et les contenus sont conservés. **Vérifier les statuts de toutes les lignes de `extraction.jsonl`, même lorsque la commande se termine normalement.** Les fichiers `.partial` éventuels sont exclus de l’analyse et restent à examiner en cas d’échec.

## Analyse générale SQLite

```bash
python3 telephones/scripts/tp02_forensic.py analyze \
  --extracted telephones/recherche-TP-02/extraction-cameras-20261014 \
  --out telephones/recherche-TP-02/analyse-cameras-reproduction \
  --row-limit 1000000
```

Sorties : inventaire des contenus, inventaire des signatures SQLite exactes, schémas/tables/colonnes/compteurs, candidats temporels et état d’analyse. Les bases sont ouvertes sur des copies temporaires avec leurs compagnons disponibles. Les originaux extraits ne sont pas modifiés. Les scans utilisent `NOT INDEXED` pour éviter de dépendre de collations applicatives absentes ; aucune collation arbitraire n’est substituée. Un `quick_check` non réalisable n’est pas présenté comme réussi.

Les formats Unix et Apple/Cocoa sont des **hypothèses** de conversion. Les valeurs SQLite brutes et les rowid disponibles sont conservés. Seules les colonnes à nom temporel sont examinées ; la limite par table et les erreurs sont consignées. L’absence de candidats ne démontre pas l’absence d’activité.

## Chronologie ciblée et structures non SQLite

```bash
python3 telephones/scripts/tp02_targeted.py \
  --extracted telephones/recherche-TP-02/extraction-cameras-20261014 \
  --extracted telephones/recherche-TP-02/extraction-systeme-20261014 \
  --out telephones/recherche-TP-02/chronologie-reproduction
```

Cet outil lit les dates des plist/JSON, les en-têtes JSON des diagnostics, les timestamps de logs avec fuseau explicite, les tables OperatingDates, les appels et les champs temporels SMS. Il exporte les modèles Xiaomi sans jetons, mots de passe ou contenu des messages. Les lectures SQLite ciblées sont `immutable` : elles ne rejouent pas de WAL, contrairement à l’analyse générale. Les fichiers structurés/texte sont limités à 32 Mio. Les formats inconnus restent dans l’inventaire.

OperatingDates comporte un mois **0 à 11**, un jour **1 à 31** et aucune heure d’événement. L’outil produit un intervalle journalier UTC : le début affiché est une **borne de jour**, pas une heure d’utilisation. Les dates plist sont des valeurs de type date décodées ; les fichiers binaires d’origine sont conservés et hachés. Les nanosecondes SMS sont conservées brutes, les conversions affichées sont tronquées à la microseconde. Les états et dates synchronisés/restaurés peuvent provenir d’autres appareils.

Références de format : [WebKit OperatingDate](https://github.com/WebKit/WebKit/blob/main/Source/WebKit/NetworkProcess/Classifier/ResourceLoadStatisticsStore.h), [Apple époque de référence](https://developer.apple.com/documentation/foundation/date/timeintervalsincereferencedate-swift.property), [iLEAPP CallHistory](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/callHistory.py), [iLEAPP Wi-Fi](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/appleWifiPlist.py). Ces références ne remplacent pas la validation du comportement de la version installée sur TP-02.

## Vérification des empreintes

```bash
python3 telephones/scripts/tp02_verify.py \
  --extracted telephones/recherche-TP-02/extraction-cameras-20261014 \
  --extracted telephones/recherche-TP-02/extraction-systeme-20261014 \
  --out telephones/recherche-TP-02/verification-reproduction.json
```

Revérifie les empreintes chiffrées et déchiffrées contre celles enregistrées avant/pendant extraction. Il ne s’agit pas d’une empreinte intégrale des 96 Go. `tp02_results.py` consolide les répertoires nommés de la passe du 14/10/2026 ; c’est un outil de consolidation de cette campagne, distinct des outils génériques ci-dessus.

```bash
telephones/scripts/.venv-iphone/bin/python telephones/scripts/test_tp02_forensic.py
```

Les tests utilisent uniquement des données synthétiques. La campagne réelle a également exécuté le déchiffrement, l’identification de signatures, la lecture de schémas et la revérification des empreintes ; les résultats consolidés et limites se trouvent dans `telephones/recherche-TP-02/resultats-20261014/`.


## Compléments exécutés et rapport complet

La campagne complète du 14/10/2026 a déchiffré **3 890 fichiers**, dont Photos.sqlite, des plist complémentaires, 33 médias sélectionnés et deux bases WhatsApp. L’inventaire final contient **254 signatures SQLite**. Les répertoires `resultats-20261014` et `analyse-en-attente` décrivent des étapes antérieures ; la référence finale est `resultats-finaux-20261014`, avec le rapport `telephones/analyse-TP-02.md`.

- `tp02_followup.py --out <nouveau répertoire>` : Photos, Santé, Wi-Fi et provenance des appels ; il lit les répertoires nommés de cette campagne sous `--root`.
- `tp02_media_metadata.py --extracted <passe médias> --out <nouveau fichier JSON>` : Pillow pour JPEG et API libheif pour HEIC ; aucune image affichée, aucune exportation GPS.
- `tp02_consistency.py --extracted <passe> [--extracted <autre passe>] --out <nouveau JSON>` : comparaison empirique de Digest au SHA-1 chiffré et déchiffré. Dans cette campagne, les 1 307 Digest disponibles correspondent aux objets chiffrés. La première hypothèse limitée au clair a été explicitement corrigée ; elle ne doit pas être utilisée comme anomalie.
- `tp02_consistency.py --fresh-manifest ...` : redéchiffrement du manifeste depuis l’original, avec mot de passe interactif et suppression du fichier temporaire après comparaison SHA-256.

La vérification initiale a porté sur 3 888 objets, puis le complément WhatsApp sur deux autres. Toutes les empreintes sources et extraites correspondent à celles consignées lors de l’extraction. Les 94 différences de taille MBFile/contenu restent documentées ; elles ne sont pas corrigées artificiellement. Les cinq APM LSC demeurent dans un format non décodé. Les trois tests synthétiques et les contrôles réels complètent la vérification, sans prétendre à une couverture physique exhaustive du téléphone.
