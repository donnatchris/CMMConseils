# Générer la livraison documentaire du 18 novembre 2026

La sélection explicite de [livraison-20261118.json](livraison-20261118.json) contient 69 documents : 68 rendus des textes courants et le PDF d’origine de l’attestation, copié sans régénération. Les rapports par appareil, compléments, annexes exhaustives et notices sont inclus. Les cours, mémos, codes d’accès, correspondance ancienne et versions supprimées sont exclus.

## Préparer puis générer

Depuis la racine du projet, avec Python 3 et les bibliothèques système nécessaires à WeasyPrint :

```bash
python3 -m venv /tmp/dmm-pdf-venv
/tmp/dmm-pdf-venv/bin/pip install markdown==3.11.3 weasyprint==70.0 pypdf==7.1.0
/tmp/dmm-pdf-venv/bin/python generer-pdf/verifier-livraison.py --skip-pdf
/tmp/dmm-pdf-venv/bin/python generer-pdf/generer-rapports.py
/tmp/dmm-pdf-venv/bin/python generer-pdf/verifier-livraison.py
/tmp/dmm-pdf-venv/bin/python generer-pdf/preparer-livraison.py
```

Le générateur écrit uniquement dans `pdfs/livraison-20261118/`. Il refuse de remplacer des sorties existantes sans `--replace`. Pour régénérer cette livraison après correction, ajouter `--replace` ; pour un seul texte, ajouter aussi `--only chemin/rapport.md`. Les PDF antérieurs et manifestes historiques restent en place. Aucun générateur historique d’analyse SD ou Sage n’est exécuté : ils pourraient remplacer les textes révisés.

## Manifestes et contrôle visuel

`manifest-20261118.json` contient les SHA-256 des sources et PDF, pagination, tailles et limites de page contrôlées. Les liens entre rapports livrés visent les nouveaux PDF ; les références aux pièces techniques nécessitent le dossier de travail correspondant. Les secrets ne font partie ni des sources sélectionnées ni des commandes de génération.

Le vérificateur contrôle les liens/ancres, les colonnes des tableaux, la conservation des données de preuve, les références Git des suppressions, les empreintes des Markdown hors corpus rétablis, le texte de l’attestation et les PDF. La synthèse du rapport final doit occuper trois pages, avant la section 2.

Après toute modification de texte ou de style, rendre les pages de contrôle avec Poppler, par exemple :

```bash
pdftoppm -f 1 -l 3 -scale-to 1500 -png pdfs/livraison-20261118/RAPPORT-FINAL-SADEDINE-2026.pdf /tmp/synthese-revisee
```

Examiner également les pages de tableaux et d’images affectées. Les journaux de rendu restent dans le répertoire temporaire affiché par le générateur. Le manifeste global de livraison est distinct des anciens relevés d’empreintes ; ne pas recalculer ceux-ci comme s’ils décrivaient les textes du 18 novembre.

## Conversion d’une nouvelle photographie

Les photographies d’origine de l’attestation sont préservées. Pour un nouveau dérivé, écrire un nouveau fichier :

```bash
magick SOURCE.HEIC /CHEMIN/NOUVEAU-DERIVE.jpg
```

Christophe DOnnat — Donnat Dev
