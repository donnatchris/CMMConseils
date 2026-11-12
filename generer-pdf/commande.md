# Commandes

## Régénérer tous les rapports DMMConseils

Depuis la racine du projet, la commande suivante convertit les 11 rapports courants dans `pdfs/`. Elle conserve les tableaux et illustrations, ajoute les en-têtes DMMConseils et la pagination, puis actualise `pdfs/manifest.json` avec les empreintes SHA-256 des sources et des PDF.

```bash
python3 -m venv /tmp/dmm-pdf-venv
/tmp/dmm-pdf-venv/bin/pip install markdown weasyprint pypdf
/tmp/dmm-pdf-venv/bin/python generer-pdf/generer-rapports.py
```

Le script retrouve automatiquement la racine du projet et conserve les journaux de conversion dans un dossier temporaire dont il affiche le chemin. Les chemins historiques normalisés sont des références documentaires ; ils ne signifient pas que les répertoires physiques ont été renommés.

## Générer un PDF à partir d'un fichier Markdown

Commande à exécuter à la racine du projet pour générer un PDF à partir d'un fichier Markdown :

```bash
SOURCE=<source.md>
OUTPUT=<output.pdf>
pandoc $SOURCE \
  -o $OUTPUT \
  --pdf-engine=xelatex \
  --syntax-highlighting=idiomatic \
  --lua-filter=./generer-pdf/wrap-inline-code.lua \
  -H ./generer-pdf/pdf-header.tex \
  -V geometry:margin=0.7in
```

exemple:

```bash
SOURCE=remise-documents/attestation-de-remise.md 
OUTPUT=remise-documents/attestation-de-remise.pdf
pandoc $SOURCE \
  -o $OUTPUT \
  --pdf-engine=xelatex \
  --syntax-highlighting=idiomatic \
  --lua-filter=./generer-pdf/wrap-inline-code.lua \
  -H ./generer-pdf/pdf-header.tex \
  -V geometry:margin=0.7in
```

## Changer les .HEIC en .JPG

```bash
for f in remise-documents/photos/*.HEIC; do
  magick "$f" "${f%.HEIC}.jpg"
done
```
