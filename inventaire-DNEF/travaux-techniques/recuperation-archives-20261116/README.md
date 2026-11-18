# Recherche de récupération — OP-01 — 16 novembre 2026

Cette campagne recherche Archive_saddedine.zip, Rejets_saddedine.txt et Inventaire_saddedine.csv dans l’image interne d’OP-01. Elle complète les recherches par noms précédentes. Les sources restent en lecture seule ; les sorties antérieures sont conservées.

Le [rapport de résultat](../../rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md) distingue métadonnées descriptives et contenu récupéré. Les conclusions sont intégrées dans `telephones/analyse-TP-03.md` et au point 1.9 du rapport final. Leurs versions avant intégration sont conservées et hachées sous `prive/versions-rapports-avant-integration/`.

## Parcours reproductible

Les scripts utilisent les chemins du partage SIFT `/media/shared/codeProjects/DMMConseils/`. Ils refusent de remplacer leurs sorties : pour recommencer, adapter leurs destinations dans des copies vers un nouveau dossier. Les accès SSH utilisent `ssh -F /home/chris/.ssh/config sift`.

1. `monter.py` appelle le script existant de montage EWF/BitLocker/NTFS en lecture seule, avec saisie masquée. Aucun secret n’est enregistré.
2. `candidats.py`, `collecter_references.py` et `chercher_noms_mft_courante.py` contrôlent les candidats supprimés, tailles de cibles et toute la MFT actuelle.
3. `scanner_residus.py` utilise le moteur `signatures.c`, compilé en bibliothèque dans `prive/outils/`. Les vérifications du moteur et des parseurs ZIP/ZIP64 sont conservées. Seule la passe `balayage-v3` est complète ; les deux premières passes interrompues et leurs scripts restent disponibles.
4. `examiner_vss.py` construit une vue dérivée en mémoire excluant les deux entrées du cliché à en-tête invalide ; les octets sources ne sont pas modifiés. `qualifier_vss_mft.py` relit les noms NTFS du premier cliché accessible. Cette méthode ne garantit pas une restitution exhaustive des clichés d’origine.
5. `extraire_contexte.py`, `qualifier_shell_items.py` et `qualifier_fragments.py` distinguent les mentions et structures Windows du contenu des fichiers. `shell-items-v2.json` corrige l’ordre date/heure DOS de la première sortie conservée.
6. `comparer_repertoires_zip.py comparaison-zip-L16B-finale` compare les 982 répertoires centraux cohérents aux 1 558 fichiers de L16B. `examiner_correspondance_generique.py` vérifie le seul nom commun, loading.gif : GIF différents, dans des composants Sage sans PDF Mini.
7. `rediger_bilan.py` vérifie la couverture, les empreintes et les candidats, écrit le rapport puis le manifeste SHA-256. Les scripts et données sont conservés ; `prive/` est exclu de Git.

Le balayage final a lu 357 162 754 048 octets libres et 15 187 726 336 octets de fichiers logiques, sans erreur signalée. Aucun fichier cible n’a été récupéré. Les limites comprennent les archives fragmentées sans allocations conservées, les données écrasées, la compression mémoire non décodée et les zones non balayées décrites dans le rapport.
