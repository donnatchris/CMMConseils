# SD-01 — Complément ciblé du 16 octobre 2026

Rapport actualisé : [analyse-cartes_sd-SD-01.md](../../analyse-cartes_sd-SD-01.md), en particulier § 1–3 (contexte/périmètre), § 8.1 (février/1999), § 8.2 (15 octobre), § 13.1 (classification) et § 15 (conclusions).

**Contexte corrigé : les caméras n'étaient pas sous scellés.** L'objet porte exclusivement sur la récupération de vidéos effacées, les modifications anormales/malveillantes et les deux événements apparents de réinitialisation. L'origine précise de l'interrogation de la cliente est inconnue ; les métadonnées ne sont qu'une piste.

## Méthode et préservation

Aucune connexion à SIFT/FORENSIC pour ce complément. Réutilisation des dérivés du 15/10, sans modifier les anciens fichiers ni leur manifeste. Aucune nouvelle vérification EWF complète, aucun carving, scan disque ou décodage intégral supplémentaire. Les sources documentaires consultées sont référencées et empreintées dans `sources/fichiers-consultes.json`.

- Relecture des 936 slots bruts déjà collectés. Les neuf slots aux dates 2000 ont été décodés de nouveau et vérifiés sur les octets des copies de répertoire préservées. Quatre sont des alias `.`/`..`, sans événement indépendant.
- Comparaison des 81 dossiers journaliers aux premières et dernières fins estimées des clips. Le schéma de dates du dossier du 15 se retrouve sur 79 jours ; les deux exceptions sont février/mars aux dates 2000.
- Réexamen borné de 45 vidéos extraites : 37 du 15 et huit témoins. SHA-256 revérifiés, ouverture des boîtes MP4 et comparaison exacte des descriptions de codecs `stsd` ; aucun réencodage.
- Analyse des temps des paquets du 15 : six contrôles antérieurs réutilisés, 31 lectures FFprobe complémentaires sans décodage. L'intervalle maximal de 0,138 s porte sur les paquets vidéo consécutifs à l'intérieur d'un clip, sans information sur la caméra entre deux clips.

Les anciennes propriétés audio/vidéo et les anciens contrôles de corruption restent les résultats de la campagne du 15 ; seules les comparaisons nouvelles sont datées du 16. Les deux nouveaux scripts écrivent des sorties nouvelles et refusent l'écrasement.

## Artefacts et interprétation

| Fichier | Objet |
|---|---|
| `sources/contexte-et-observations.md` | Correction de contexte et réponse de l'utilisateur sur l'origine inconnue |
| `sources/recherche-origine-evenements.txt` | Occurrences documentaires avec fichiers et lignes, à lire selon la nature primaire/secondaire de chaque source |
| `sources/fichiers-consultes.json` | Chemins, tailles, SHA-256 ; contrôles contre le manifeste initial pour les dérivés utilisés |
| `inventaires/traces-fat-1999-2000.{json,csv}` | Neuf slots, dates exactes avec centièmes, offsets absolus, alias, octets bruts et localisation dans la copie de répertoire |
| `inventaires/chronologie-fevrier-mars.csv` | Clips de février et du début mars, horodatages et intervalles |
| `inventaires/chronologie-20241015.csv` | Les 37 clips du jour, propriétés et contrôles antérieurs |
| `inventaires/repertoires-premier-dernier-clip.csv` | Comparaison des dates de répertoires et des fins de clips sur 81 jours |
| `inventaires/medias-cibles.json` | Structures, codecs, empreintes des 45 clips, dates et descriptions `stsd` |
| `inventaires/paquets-video-20241015.json` | DTS/PTS, six réemplois et 31 nouvelles lectures FFprobe, commandes et empreintes des sorties brutes |
| `inventaires/synthese-complement.json` | Comptes, intervalles, plages d'écart FAT/fin vidéo et absence d'incohérence de tables le 15 |
| `journaux/` | Commandes, méthodes, stdout et éventuelles erreurs |
| `rapport-sha256.txt`, `manifest-sha256.csv` | Empreinte du rapport actualisé et manifeste du complément |

Le manifeste de 20261015 reste inchangé. Son ancienne empreinte de rapport concerne la version retirée à la demande de l'utilisateur ; sa copie archivée a été supprimée. Elle ne correspond pas au Markdown mis à jour. Le nouveau manifeste couvre le rapport courant, les nouveaux scripts et les fichiers de ce complément, hors le manifeste lui-même.

## Reproduction ciblée

Depuis la racine du projet, consulter les deux scripts avant exécution. Ils utilisent explicitement les chemins du jeu de résultats du 15 et du complément du 16 :

```bash
python3 cartes_sd/scripts/sd01_complement_20261016.py
python3 cartes_sd/scripts/sd01_complement_paquets.py
```

Ces commandes ne doivent pas être relancées sur les sorties livrées : elles refusent de les écraser. Pour une contre-vérification, utiliser une copie distincte du projet ou adapter le répertoire `OUT` dans une copie des scripts, en conservant les sources `OLD` inchangées. Le premier script importe le parseur MP4 déjà utilisé le 15 ; il n'exécute pas son point d'entrée de collecte. Le second requiert FFprobe local déjà présent (8.0.1 lors de ce complément).

La recherche documentaire enregistrée est reproductible avec les arguments de `journaux/recherche-origine-evenements.json`. Elle porte sur les pièces textuelles nommées, pas sur un historique de compte caméra ou des captures non fournies. Le contexte corrigé provient de la conversation et reste explicitement distinct du mail.

**Portée :** les dates aberrantes et la corruption ne démontrent pas une intention ; la conversion possible vers 1999 ne démontre pas son utilisation par le logiciel inconnu ; les métadonnées cohérentes du 15 ne prouvent pas l'absence de redémarrage entre clips. Aucun des deux événements n'est confirmé comme une réinitialisation effective et aucune nouvelle vidéo effacée n'est récupérée par ce complément.
