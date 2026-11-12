# Reproduire l'investigation SD-02

Référence de données : image décompressée SHA-256 `ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d`. Les scripts, paramètres effectivement utilisés et leurs sorties sont conservés. Le rapport canonique est `cartes_sd/analyse-cartes_sd-SD-02.md`.

## Préservation et destinations

Exécuter depuis la racine du projet, jamais depuis FORENSIC. L'hôte `sift` utilise la configuration utilisateur explicite. Les scripts distants sont transmis sur stdin ; leurs résultats sont reçus dans le projet. SIFT n'enregistre aucun média persistant. Ne pas rediriger les sorties dans le dossier des acquisitions.

Pour une nouvelle campagne, choisir un nom distinct et exporter `SD02_RUN=AAAAMMJJ-relecture`. Le collecteur et le récepteur refusent de remplacer les résultats existants. Le générateur de rapport écrit explicitement le rapport canonique : ne le relancer que pour une mise à jour voulue de celui-ci. Les exemples ci-dessous omettent le préfixe `python3 cartes_sd/scripts/` pour alléger le tableau ; chaque nom `.py` est un script conservé dans ce répertoire.

Vérifier l'existence et le mode de `/mnt/ewf-sd02/ewf1`. Si absent, créer uniquement le point de montage et utiliser `sudo -n ewfmount SOURCE/SD02.E01 /mnt/ewf-sd02` ; aucune partition FAT montée et aucune réparation. Contrôler suffisamment d'espace : le récepteur impose une réserve de 8 Gio, des plafonds par étape et 256 Mio par membre. La plus grande vidéo déclarée de cette image reste sous 27 Mo.

## Ordre reproductible

| Étape | Commande/paramètres |
| --- | --- |
| Provenance, versions, géométrie | `sd02_collect.py etat` |
| Intégrité EWF et SHA-256 logique | `sd02_collect.py integrite` |
| Empreintes des quinze segments | `sd02_collect.py segments` |
| Inventaire TSK et chronologie | `sd02_collect.py fls`, puis `body`, puis `mactime` |
| Contre-lecture FAT | `sd02_collect.py script cartes_sd/scripts/sd02_rawfat_remote.py inventaires/lecture-fat.json` |
| Répertoires orphelins | `sd02_collect.py script cartes_sd/scripts/sd02_orphanfat_remote.py inventaires/lecture-fat-v2.json` |
| Slots de 108 fichiers orphelins | `sd02_collect.py script cartes_sd/scripts/sd02_orphan_slots_remote.py inventaires/orphelins-slots.json` |
| Paramètres de structures | `sd02_parameters.py structures` |
| Export de structures | `sd02_receive.py cartes_sd/scripts/sd02_structures_remote.py structures DOSSIER/inventaires/parametres-structures.json` |
| Jointure et plan final | `sd02_plan.py` |
| Analyse de tous les fichiers | `sd02_receive.py cartes_sd/scripts/sd02_media_remote.py medias DOSSIER/inventaires/plan-medias.json` |
| Contrôle prioritaire ciblé | `sd02_parameters.py priorite`, puis réception `sd02_priority_remote.py` label `priorite` paramètres `plan-priorite.json` |
| Audit des allocations/slack | réception `sd02_allocation_remote.py` label `allocation` paramètres `parametres-structures.json` |
| Balayage intégral libre | `sd02_collect.py script cartes_sd/scripts/sd02_scan_remote.py inventaires/espace-libre.json` |
| Export libre borné | `sd02_parameters.py residus`, puis réception `sd02_residual_remote.py` label `residus` paramètres `parametres-residus.json` |
| Classification libre | `sd02_classify.py` |
| Récupérations complètes | `sd02_parameters.py recuperations`, puis réception `sd02_recover_remote.py` label `recuperations` paramètres `plan-recuperations.json` |
| Blocs sans référence/chaîne temporaire/istat | `sd02_parameters.py complements`, puis réception `sd02_complements_remote.py` label `complements` paramètres `plan-complements.json` |
| Recoupement des emplacements réutilisés | `sd02_overlap.py` |
| Synthèse des résidus | `sd02_residual_summary.py` |
| Restauration temporaire | `sd02_parameters.py finalisation`, puis réception `sd02_finalize_temp_remote.py` label `finalisation` paramètres `plan-finalisation.json` |
| Aperçus ciblés | `sd02_parameters.py apercus`, puis réception `sd02_previews_remote.py` label `apercus` paramètres `plan-apercus.json` |
| Fragment terminal du douzième fichier | `sd02_parameters.py fragment-final`, puis réception `sd02_partial_remote.py` label `fragment-final` paramètres `plan-fragment-final.json` |
| Contrôle de préservation | `sd02_collect.py final`, comparer les quinze lignes avec `segments-sha256.txt` |
| Synthèse finale, après fin des médias | `sd02_analyze.py` |
| Complément premier témoin du 12 novembre | `sd02_parameters.py supplement`, puis réception `sd02_supplement_remote.py` label `supplement` paramètres `plan-supplement.json` |
| Contrôle des deux clips au chevauchement maximal | `sd02_parameters.py ecarts`, puis réception `sd02_ecarts_remote.py` label `ecarts` paramètres `plan-ecarts.json` |
| Rapport canonique | `sd02_report.py` |
| Contrôle des artefacts et liens | `sd02_qa.py` |
| Manifeste de fin | `sd02_manifest.py` |

`DOSSIER` désigne le répertoire **local** `cartes_sd/recherche-SD-02/$SD02_RUN`. Les paramètres et identifiants des recherches ciblées sont spécifiques à cette image vérifiée ; ne pas les appliquer aveuglément à une autre carte. Les deux premiers essais de jointure conservés dans cette campagne ont motivé la lecture des slots orphelins. Une reproduction propre peut suivre directement la jointure finale, sans recréer les échecs initiaux.

## Interprétation et contrôles

Les noms/horloges caméra sont déclaratifs. `mactime -z UTC` fixe une représentation, pas une synchronisation démontrée. FAT ne donne ni date d'effacement ni auteur. Les identifiants TSK sont reliés aux offsets de slots dans l'inventaire. Les sources et sorties des commandes, heures UTC et codes de retour figurent dans `journaux/commandes.jsonl`.

`sd02_receive.py` préfixe les seules fonctions pures du parseur `sd01_mp4.py`, sans exécuter son programme principal ; leur SHA-256 est journalisé. `sd02_stbl_helpers.py` conserve séparément la grammaire inférée des journaux. Les codes sources des étapes distantes et les paramètres complets sont nécessaires à la reproduction, pas seulement le journal synthétique.

Le plan effectivement exécuté conserve aussi certains alias `.MP4` majuscules dans sa sélection bornée (le critère de sélection `.mp4` était sensible à la casse). Ce sont des extractions diagnostiques, dont plusieurs pointent sur des données ultérieures, **pas des vidéos récupérées**. Le nombre de vidéos supprimées lisibles se déduit uniquement des contrôles spécifiques de récupération, jamais du nombre de fichiers exportés.

Onze fichiers complets : tous les clusters utilisés, exclusions, SHA-256, tailles, vérifications des tables et FFmpeg sont dans `inventaires/recuperations.json`. La chaîne FAT historique étant perdue, l'ordre physique est une hypothèse explicitement vérifiée par les tables et le décodage. Dix concordent intégralement avec `icat -r`. Le onzième exclut un journal que `icat -r` incorporait. Le fragment du douzième et le temporaire ont des métadonnées reconstruites : ce ne sont pas leurs conteneurs originaux intacts.

L'essai `temp-chaine-complete.mp4` est **NON VALIDÉ** (erreurs H.264/AAC malgré retour zéro). Le fichier `temp-taille-logique.mp4`, 68,992 s, est le dérivé validé. Ne pas présenter l'essai défaillant comme une suite récupérée.

Les PNG ont fait l'objet d'un examen visuel par l'assistant, décrit dans le rapport. Les métadonnées et décodages ne constituent pas un visionnage intégral de toutes les vidéos. Aucun PhotoRec SD-02 n'a été lancé ; les recherches spécialisées sont tracées sans transférer le résultat PhotoRec SD-01.

Les empreintes finales de segments ont été réalisées pendant la dernière partie de l'examen vidéo, après les lectures structurelles et récupérations. Les dernières analyses médias ont poursuivi les mêmes opérations strictement en lecture seule. Les heures exactes sont conservées dans le journal.

## Contenu du manifeste

`manifest-sha256.txt` référence les fichiers de cette campagne, le rapport canonique, les scripts SD-02 et leurs dépendances explicitement identifiées, ainsi que les sources documentaires citées. Chemins relatifs à la racine du projet. Il exclut son propre fichier et son index récapitulatif pour éviter une référence circulaire. Vérification depuis la racine : `sha256sum -c cartes_sd/recherche-SD-02/20261016/manifest-sha256.txt`. L'index contient l'empreinte du manifeste et les totaux. Les médias/blocs privés restent dans le projet et exclus de Git ; un clone Git seul ne suffit donc pas à restituer tous les artefacts.
