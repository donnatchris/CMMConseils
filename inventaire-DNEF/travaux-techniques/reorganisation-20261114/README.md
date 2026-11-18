# Réorganisation du dossier inventaire DNEF

Le 14 novembre 2026, à la demande de l’utilisateur, les fichiers ont été répartis entre `documents-recus/`, `rapports/` et `travaux-techniques/`.

Les sept documents reçus et tous les résultats bruts ont été déplacés sans modification de contenu. Les rapports et les scripts ont reçu uniquement les adaptations de liens et de chemins nécessaires à cette organisation. Les anciennes versions des fichiers adaptés sont conservées sous `prive/avant/`.

Le [journal détaillé](prive/journal-deplacement.json) contient, pour chacun des 331 fichiers déplacés, l’ancien chemin, le nouveau chemin et les empreintes avant/après. Il indique aussi le chemin de la version originale conservée lorsqu’un fichier a été adapté.

Les anciens `manifest-sha256.txt` et `verification-finale.json` ont été conservés intacts. Ils décrivent l’organisation historique. Le script suivant vérifie leurs entrées en tenant compte des déplacements et des versions originales archivées :

```sh
python3 inventaire-DNEF/travaux-techniques/reorganisation-20261114/verifier.py --historique
```

Sans option, le même script contrôle aussi les empreintes actuelles des 331 fichiers déplacés. Le [bilan](verification.json) et le [nouveau relevé d’empreintes](manifest-sha256-apres.txt) documentent le contrôle après rangement. Ce dernier s’utilise depuis la racine du projet :

```sh
sha256sum -c inventaire-DNEF/travaux-techniques/reorganisation-20261114/manifest-sha256-apres.txt
```

Le script `reorganiser.py` consigne l’opération exécutée. Il refuse de réutiliser ce dossier de journalisation ; il ne doit pas être relancé sur l’arborescence déjà réorganisée.
