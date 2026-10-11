REMISE_DIRECTORY := remise-documents
REMISE_PDF_SOURCE := $(REMISE_DIRECTORY)/attestation-de-remise.md
REMISE_PDF_OUTPUT := $(REMISE_DIRECTORY)/attestation-de-remise.pdf
REMISE_PHOTOS := $(REMISE_DIRECTORY)/photos

GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[1;31m
RESET := \033[0;0m

.PHONY: clean-all

###################################################################################################
# Clean commands
###################################################################################################

git-status:
	@printf "$(YELLOW)Vérification de l'état du dépôt\n$(RESET)"
	@git fetch --quiet
	@GIT_STATUS=$$(git status --porcelain); \
	if [ -n "$$GIT_STATUS" ]; then \
		printf "$(RED)ABORTED: Repository is not clean.\n$(RESET)"; \
		exit 1; \
	fi
	@if ! git rev-parse --verify '@{upstream}' >/dev/null 2>&1; then \
		printf "$(RED)ABORTED: No upstream branch configured.\n$(RESET)"; \
		exit 1; \
	fi
	@if [ "$$(git rev-parse HEAD)" != "$$(git rev-parse '@{upstream}')" ]; then \
		printf "$(RED)ABORTED: Repository is not synchronized with remote.\n$(RESET)"; \
		exit 1; \
	fi
	@printf "$(GREEN)Repository clean and synchronized.\n$(RESET)"

clean-tracked: git-status
	@printf "$(YELLOW)Suppression of tracked files\n$(RESET)"
	@git ls-files -z -- ':!Makefile' | xargs -0 rm -f --
	@printf "$(GREEN)Tracked files removed.\n$(RESET)"

clean-all: clean-tracked
	@printf "$(GREEN)All tracked files have been removed. Restore with 'git restore .'\n$(RESET)"

git-restore:
	@printf "$(YELLOW)Restoring tracked files\n$(RESET)"
	@git restore .
	@printf "$(GREEN)Tracked files restored.\n$(RESET)"

###################################################################################################
# PDF generation commands
###################################################################################################

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

.PHONY: remise-pdf remise-photos git-status clean-tracked clean-all git-restore
