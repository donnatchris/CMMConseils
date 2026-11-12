# SD-01 — Campagne du 15 octobre 2026

Rapport principal : [analyse-cartes_sd-SD-01.md](../../analyse-cartes_sd-SD-01.md).

Les EWF maîtres sont lus dans SIFT, jamais écrits. Tous les résultats persistants sont dans le projet. Les scripts ouvrent la vue EWF en lecture seule et transmettent les données via stdout SSH. Les contrôles vidéo distants utilisent une copie anonyme en mémoire (`memfd`), sans fichier persistant sur la VM. Le montage EWF existant est `0444` ; aucune partition FAT n'est montée.

## Répertoire des résultats

- `journaux/` : commandes SSH horodatées et codes retour dans `commandes.jsonl`, sorties et erreurs, versions, acquisition originale copiée, `istat`, FFprobe et décodages. Les scripts locaux gardent leurs commandes FFmpeg/FFprobe dans les JSON correspondants. Les stdout des étapes locales sont aussi conservés.
- `inventaires/` : inventaire CSV, dates FAT normalisées, chronologie par nom et durée, structures MP4, contre-lecture FAT32, résidus et contrôles.
- `structures/` : MBR et prépartition, secteurs réservés FAT32, deux FAT, derniers secteurs de partition ; binaires ignorés par Git.
- `prive/extraits/` : extractions logiques de tous les fichiers ; nom préfixé par l'identifiant TSK. `export.json` relie chemin original, taille et SHA-256.
- `prive/cibles/` : neuf extractions prioritaires indépendantes, dont les trois temporaires et les quatre vidéos du 28. Les `.stderr` voisins sont des journaux vides, pas des médias.
- `prive/repertoires/` : copies brutes des secteurs de répertoire, avec identifiant TSK.
- `prive/residus/` : les 1 480 clusters libres non nuls, chacun de 16 384 octets, nommés par numéro de cluster ; adresses absolues et empreintes dans le scan.
- `prive/previsualisations*/` : dérivés visuels ; ils ne remplacent pas les vidéos extraites. Les images et vidéos sont sensibles, exclues de Git.
- `manifest-sha256.csv` : chemins relatifs au projet, tailles, SHA-256 de tous les artefacts présents et des scripts ; le manifeste s'exclut lui-même. Il inclut les fichiers ignorés par Git, mais pas le rapport Markdown évolutif.
- `rapport-sha256.txt` : empreinte séparée de la version livrée du rapport principal.

Le dossier représente environ 2,4 Gio. Pour remettre l'ensemble probatoire, copier aussi les fichiers ignorés : un clone Git seul est incomplet. Aucune publication, aucun ajout à Git ni transfert cloud n'est effectué par ces scripts.

## Reproduction dans une campagne neuve

Depuis la racine du projet. Ne pas relancer les collectes dans `20261015` : les scripts refusent d'écraser les artefacts. `SD01_RUN` doit être un nom de campagne (date puis caractères simples), jamais un chemin. Les destinations restent sous `cartes_sd/recherche-SD-01/`.

Préconditions : SSH `sift`, configuration explicite `/home/chris/.ssh/config`, accès `sudo -n`, EWF monté à `/mnt/ewf-sd01/ewf1`, partition à 8 192 secteurs de 512 octets, outils SIFT indiqués dans le rapport. Hôte de cette campagne : Python 3.14.4, FFmpeg 8.0.1 et Pillow déjà présents. Les chemins et la géométrie de SD-01 sont des constantes explicites dans les scripts, à ne pas appliquer à un autre support.

```bash
export SD01_RUN=20261015-reproduction
mkdir -p "cartes_sd/recherche-SD-01/$SD01_RUN/journaux"
python3 cartes_sd/scripts/sd01_collect.py integrite
python3 cartes_sd/scripts/sd01_collect.py inventaire
python3 cartes_sd/scripts/sd01_collect.py contexte
python3 cartes_sd/scripts/sd01_collect.py script cartes_sd/scripts/sd01_rawfat_remote.py inventaires/lecture-fat-independante-v2.json
python3 cartes_sd/scripts/sd01_collect.py mactime
python3 cartes_sd/scripts/sd01_receive.py
python3 cartes_sd/scripts/sd01_analyze.py
python3 cartes_sd/scripts/sd01_mp4.py
python3 cartes_sd/scripts/sd01_targets.py
python3 cartes_sd/scripts/sd01_priority.py
python3 cartes_sd/scripts/sd01_stbl.py
python3 cartes_sd/scripts/sd01_collect.py script cartes_sd/scripts/sd01_scan_remote.py inventaires/scan-non-alloue-v2.json
python3 cartes_sd/scripts/sd01_residual_receive.py
python3 cartes_sd/scripts/sd01_residual_analyze.py
python3 cartes_sd/scripts/sd01_collect.py allocation
python3 cartes_sd/scripts/sd01_qa.py boot
python3 cartes_sd/scripts/sd01_qa.py qualite
python3 cartes_sd/scripts/sd01_qa.py complement
python3 cartes_sd/scripts/sd01_packets.py
python3 cartes_sd/scripts/sd01_decode_remaining.py
python3 cartes_sd/scripts/sd01_collect.py final
python3 cartes_sd/scripts/sd01_verify.py
python3 cartes_sd/scripts/sd01_qa.py horloges
python3 cartes_sd/scripts/sd01_qa.py manifest
```

Avant une reproduction, lire les consignes du partage comme dans `journaux/consignes-distantes.txt` et vérifier la présence ainsi que le mode de la vue EWF ; les scripts ne recréent pas un montage absent. Le collecteur de fichiers refuse plus de 3 Gio déclarés, plus de 4 Gio de flux, un fichier supérieur à 256 Mio, une campagne dépassant 2 000 entrées ou une réserve inférieure à 8 Gio après le plafond de collecte. L'extraction de résidus est limitée à 64 Mio, avec vérification FAT et SHA-256 pour chaque cluster. Tout échec doit être lu dans son stderr avant de poursuivre ; ne pas assimiler une sortie partielle à un résultat final.

Les vidéos et les structures brutes doivent reproduire leurs empreintes. Les journaux peuvent différer selon l'heure, la version des outils et les numéros de descripteurs mémoire. Les outils hôte et VM ne doivent pas être confondus. Les dates FAT sont présentées sans fuseau civil établi ; UTC sert de convention numérique pour les bodyfiles et les journaux de procédure.

## Résultats de référence et variantes conservées

`fls.txt` : 770 lignes, dont quatre objets virtuels ; `inventaire.csv` : 766 entrées réelles. `export.json` : 680 fichiers extraits, plus les relevés de répertoires et objets techniques. `controle-final.json` : aucun écart d'empreinte ou de taille, 674 vidéos actives décodées et 1 480 clusters résiduels revérifiés. `concordance-horodatages.json` valide la convention de conversion sur 2 298 champs temporels ; les écarts de création de 0 à 1 seconde proviennent de la précision non rendue par TSK.

Les premières sorties sont conservées, mais les suivantes font foi pour les points concernés :

| Sortie conservée | Résultat à utiliser | Motif |
|---|---|---|
| `lecture-fat-independante.json` | `lecture-fat-independante-v2.json` | Privilégier le chemin actif quand un ancien nom supprimé pointe au même cluster |
| `scan-non-alloue.json`, sortie vide, stderr d'interruption | `scan-non-alloue-v2.json` | Premier scan trop lent interrompu ; v2 complet, blocs nuls vérifiés puis signatures évitées dans ces seuls blocs |
| `audit-allocation.json` | `audit-allocation-v2.json` | Ajout de la recherche dans les clusters alloués au-delà de la taille logique |
| `residus-caracterises.json` | `residus-caracterises-v2.json` | Ajout du détail des premiers désaccords et longueurs de préfixes, sans modifier les résidus |
| `verification-prioritaire.txt`, `verification-prioritaire-v2.txt` | `verification-prioritaire-v3.txt` et `inventaires/verification-prioritaire.json` | Deux erreurs de traitement dérivé corrigées ; planche originale et planche v3 conservées |

Les analyses ne datent pas les suppressions, ne restaurent pas une vidéo supplémentaire et n'attribuent aucune action à une personne. Lire le rapport pour les distinctions entre observations, interprétations, hypothèses et limites.
