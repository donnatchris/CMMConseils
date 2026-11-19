# Générer la livraison documentaire du 18 novembre 2026

Les sources complémentaires de génération sont rangées dans `generer-pdf/annexes/`.
Les références Git, empreintes de référence et résultats de validation nécessaires aux
vérifications sont dans `generer-pdf/controles-documentaires/`. Le générateur et les
vérificateurs utilisent ces emplacements.

## Dossier de remise autonome `rendu/` — 19 novembre 2026

### Note de constats techniques et lettre d’accompagnement

Les textes courants sont `note-de-constat-technique.md` et
`lettre-d-accompagnement-du-constat-technique.md`. La commande suivante relit les
résultats existants, calcule les écarts sans écriture dans les preuves, puis prépare
les deux PDF dans `/tmp/dmm-documents-constat/` :

```bash
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/calculer-complements-note.py
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/generer-documents-constat.py
```

Le nombre de pages est synchronisé dans les deux Markdown. La page de présentation
et le tableau récapitulatif occupent chacun une page. Après rendu et contrôle visuel
de toutes les pages, enregistrer les SHA-256 des deux PDF dans
`/tmp/dmm-documents-constat/controle-visuel.json` sous `pdf_sha256`, puis publier :

```bash
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/generer-documents-constat.py --publish
```

La publication remplace la note, ajoute la lettre à la racine de `rendu/`, copie les
sources et les calculs utiles, et met à jour l’index, le manifeste et les empreintes.
La signature manuscrite de la lettre est laissée au prestataire. Le PDF de la note
du 18 novembre reste préservé dans les originaux. Pour un nouvel assemblage complet,
fournir son chemin à `generer-rendu.py --note-original CHEMIN` si son ancien
emplacement dans `pdfs/` n’existe plus.

### Ensemble des rapports

La sélection destinée à la cliente exclut les PDF listés dans
`generer-pdf/documents-internes.json` : journaux d’incidents, notices de reproduction,
guides de scripts et annexe de commandes. Les exemplaires retirés sont conservés
dans `pdfs/documents-internes/`, hors de `rendu/`. Les pièces Markdown référencées
restent disponibles pour la vérification des rapports ; les liens des PDF retenus
les visent directement. `generer-rendu.py` applique cette sélection dès la génération.

La sélection exclut également les 17 comptes rendus intermédiaires approuvés le
19 novembre, identifiés par leurs sources dans
`generer-pdf/documents-intermediaires-exclus.json`. Leurs Markdown et justificatifs
restent conservés ; les liens vers les anciennes éditions PDF visent ces sources.
La remise courante contient 36 documents PDF : 16 principaux et 20 subsidiaires.
Le script `retirer-rapports-intermediaires.py` prépare les corrections hors de la
remise ; son option `--publish DOSSIER` les applique après contrôle visuel.

Pour appliquer cette sélection à une livraison déjà assemblée :

```bash
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/alleger-rendu.py
```

La commande suivante sélectionne les documents de remise parmi le corpus de 69
sources, puis ajoute la note de constats techniques courante et sa lettre dans
`rendu/`, avec les sources, photographies et justificatifs
référencés dans `rendu/pieces/` :

```bash
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/generer-rendu.py --audit-only
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/generer-rendu.py
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/reorganiser-rendu.py
```

Utiliser un environnement disposant de Markdown 3.11.3, WeasyPrint 70.0 et pypdf 7.1.0 ;
le `PYTHONPATH` ci-dessus correspond aux dépendances déjà installées dans cette session.
L'assemblage refuse de remplacer un dossier `rendu/` existant. Il conserve à l'identique
les pièces copiées et le PDF original de la note dans `pieces/originaux/`, et adapte
uniquement les liens de sa version principale. L'ancien emplacement de la note est
supprimé seulement après validation de l'ensemble. Les dossiers de versions antérieures,
mémos internes et codes d'accès sont exclus.

La réorganisation conserve les rapports principaux, synthèses, notes et courriers
à la racine. Les autres PDF, les pièces et les fichiers de
contrôle sont regroupés dans `rendu/rapports-subsidiaires/`. Les liens PDF sont adaptés
sans régénérer les pages ; les dessins, les images et les textes sont comparés à la
version précédente. La commande refuse de réorganiser deux fois un même dossier.

L'index principal est `rendu/index.html`, et l'index complémentaire est
`rendu/rapports-subsidiaires/index.html`. Le manifeste distingue les documents et les
pièces sources avec leurs empreintes. Pour vérifier la livraison ou préparer les
planches de contrôle visuel (Poppler et Pillow requis) :

```bash
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/generer-rendu.py --verify
PYTHONPATH=/tmp/dmm-rapport-pdf-deps python3 generer-pdf/controler-rendu.py
```

Les planches et pages de contrôle sont écrites dans `/tmp/dmm-rendu-visuel/`, hors du
dossier destiné à la cliente. Le relevé d'empreintes permet aussi de contrôler la
livraison avec `sha256sum -c rapports-subsidiaires/SHA256SUMS.txt` depuis `rendu/`.

## Livraison datée historique

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

Christophe Donnat — Donnat Dev
