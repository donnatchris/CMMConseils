# Commandes

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
