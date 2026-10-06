REMISE_DIRECTORY := remise-documents
REMISE_PDF_SOURCE := $(REMISE_DIRECTORY)/attestation-de-remise.md
REMISE_PDF_OUTPUT := $(REMISE_DIRECTORY)/attestation-de-remise.pdf
REMISE_PHOTOS := $(REMISE_DIRECTORY)/photos

remise-pdf: remise-photos
	@echo "Génération du PDF de remise des documents"
	@pandoc $(REMISE_PDF_SOURCE) \
	  -o $(REMISE_PDF_OUTPUT) \
	  --pdf-engine=xelatex \
	  --syntax-highlighting=idiomatic \
	  --lua-filter=./generer-pdf/wrap-inline-code.lua \
	  -H ./generer-pdf/pdf-header.tex \
	  -V geometry:margin=0.7in
	@echo "PDF généré : $(REMISE_PDF_OUTPUT)"
	@echo "Pensez à vérifier le nombre de pages."
	@echo "Pensez à récupérer les mots de passe."

remise-photos:
	@echo "Conversion des fichiers HEIC en JPG"
	@for f in $(REMISE_PHOTOS)/*.HEIC; do \
		magick "$$f" "$${f%.HEIC}.jpg"; \
	done
	@echo "Conversion terminée."

.PHONY: remise-pdf remise-photos