# Complément technique consolidé à la lecture du PV — contrôles des 8 et 9 novembre 2026

**Question examinée :** les documents locaux et les PDF permettent-ils de préciser la copie décrite au PV et les suppressions du 28 octobre 2024 ?

**J’ai retrouvé le texte des deux factures supprimées dans le PDF Sage, déchiffré les 46 PDF sélectionnés de TP-02 et retrouvé un équivalent binaire pour chacun des 27 PDF Mini de L16B.** Le déchiffrement réussi remplace les blocages des premiers essais. Leurs journaux sans secrets restent dans `resultats/` ; les sorties partielles ne sont pas les résultats définitifs.

Les contrôles du 14 novembre ont ensuite retrouvé les mêmes vingt contenus dans TP-03 ; ceux du 16 novembre ont confirmé les 27 PDF au CSV. L’identité du contenu ne désigne donc pas un Mini exclusif. Les trois divergences de l’inventaire et les statuts de messageries sont exposés dans les rapports actuels [Q1](../../inventaire-DNEF/rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md) et [correspondances](../../ordinateur/recherche-OP-01/correspondances-avocats-20261116/rapport-correspondances-et-integrite-20261116.md).

## 1. Préservation et méthode

OP-01 a été monté sur SIFT par EWF, boucle en lecture seule, Dislocker en lecture seule, puis NTFS avec les options `ro,norecover`. Le journal de montage est dans `journaux/montage.txt`. Les recherches portent sur des extractions existantes et le système de fichiers ainsi monté. Les bases SMS et Manifest de TP-02 ont été copiées dans un répertoire de travail isolé avant interrogation ; les empreintes des fichiers sources contrôlés avant et après sont identiques. Les scripts sont conservés dans `scripts/`. Les documents, chemins détaillés et images contenant des données privées sont dans `prive/`, exclu de Git.

Les versions antérieures du rapport final restent conservées dans l’historique Git, notamment au commit `8dd5a85`. Le dossier `rapports-avant/` a été retiré de l’arborescence de travail. Les conclusions historiques restent inchangées. Les sorties anciennes ou les tentatives échouées sont conservées et explicitement distinguées des résultats utilisables. La normalisation éditoriale des noms et chemins du 12 novembre 2026 est tracée dans `../../generer-pdf/correction-denomination-20261112.json`.


## 2. Factures : contenu conservé après suppression

### Factures récupérées

Les deux pages du document supprimé `test.pdf` correspondent respectivement aux pages **254 et 255** du texte extrait de `L16B/SAGE/sage.pdf` (458 pages textuelles non vides). Les factures portent les références **FA0338 et FA0339**.

La comparaison utilise `pdftotext -layout` et supprime seulement les caractères d’espacement avant comparaison, sans ignorer la casse ni la ponctuation. Les deux textes normalisés sont strictement identiques. Le [résultat reproductible](resultats/comparaison-factures.json) et le script `scripts/comparer_factures.py` sont conservés.

**Conséquence : le contenu textuel des deux factures subsiste dans le PDF Sage de L16B.** La mise à la corbeille de `test.pdf` reste un fait ; elle ne démontre pas la disparition de ces factures du corpus local conservé. Ce contrôle ne porte pas sur l’identité binaire des PDF ou le rendu graphique, et n’établit ni le motif de la suppression ni le contenu du support définitivement saisi.

SHA-256 de `test.pdf` récupéré : `f2cb8dbbbb28fe11eaddc59d31045152218516a1585109bd529a075e48dd8201`. SHA-256 de `sage.pdf` relevé sur SIFT le 8 novembre : `0718f1b0819210c2def92a8097bafb1a7c0586673cf37848afbbf55c943728a6`.


## 3. Qualification des candidats de la recherche initiale

### Correspondances : portée du contrôle

Les dix-sept messages candidats ont des Message-ID distincts. Cela ne signifie pas dix-sept conversations distinctes ni dix-sept correspondances protégées. Les références privées (source, index, Message-ID, contexte) sont conservées dans `prive/sift-recupere/prive/lawyer-candidates.json`.

Cinq messages du dossier **Éléments envoyés**, dans l’extraction du PST dmm, portent comme destinataire l’adresse du cabinet Negrevergne. Leurs en-têtes sont datés des **23 août, 6 septembre, 12 septembre, 3 octobre et 8 octobre 2024**. Ils constituent des occurrences directes dans les en-têtes, et non de simples coïncidences lexicales dans une pièce jointe. Le dossier et les en-têtes ne prouvent toutefois ni la remise effective au destinataire ni l’identité de la personne ayant envoyé le message.

Quatre autres candidats sont des avis de non-remise des 4 et 5 septembre 2024, dont le contenu cite Christian Pascoet dans une copie de message. Un cinquième rapprochement avec ce nom figure dans une pièce jointe au message du 3 octobre déjà compté parmi les cinq destinés au cabinet Negrevergne. La notification AR24 du 24 janvier 2024 annonce un recommandé envoyé à la demande de Charlotte Liwer ; sa présence ne donne pas le contenu du recommandé.

La contre-lecture des pièces jointes précise les autres candidats :

- une proposition de services du cabinet Aston nomme **Rachel Dress**, présentée comme avocate associée ; il s’agit d’un document professionnel pertinent pour le contrôle, et non d’une homonymie ;
- cinq messages contiennent, sous forme PDF ou DOCX et avec répétitions de contenu, une demande de report d’audience citant **Georges Meyer comme représentant de la partie adverse**. Leur présence ne constitue pas une correspondance directe entre la cliente et cet avocat ;
- un livre contient une occurrence de « Meyer » sans lien établi avec l’avocat de la liste : ce candidat est écarté de ce rapprochement ;
- la pièce jointe du message du 3 octobre reproduit un échange où **Christian Pascoët** est explicitement identifié comme expéditeur. Ce constat est plus précis qu’une simple mention de son nom.

Les seize candidats provenant des PST ont été relus directement dans les mbox et leurs Message-ID vérifiés. La notification Takeout a été examinée dans les en-têtes et contextes extraits le 8 novembre, sans réouverture de l’archive lors de cette reprise. Le [classement des dix-sept candidats](resultats/qualification-candidats.json) est conservé ; les contenus restent privés. Deux premières contre-lectures ont été interrompues pour éviter la réindexation répétée des mêmes archives ; la version achevée est `scripts/revoir_candidats_v3.py`, avec sortie dans `prive/verification-20261109-v3/review.json`.

**Ces éléments justifient un examen ciblé du filtrage annoncé au PV, mais ne démontrent pas un manquement.** Le PV distingue le dossier L16B laissé à titre informatif et les fichiers finalement saisis après exclusion. Le contrôle du CSV fourni confirme désormais les conteneurs DMM et Takeout, tandis que 93300 diverge. Le contenu du support de destination et les exclusions restent à contrôler. Leur qualification juridique n’est pas tranchée par cette analyse technique.

### Limites des pièces jointes

Les 2 448 entrées anciennement regroupées sous « erreurs » comprennent **2 441 formats/extensions non pris en charge** et **7 échecs de lecture PDF**. Il ne s’agit donc pas de 2 448 fichiers démontrés corrompus. Les entrées correspondent à des occurrences de pièces jointes et ne sont pas dédupliquées. Les images n’ont pas été soumises à OCR ; les documents bureautiques anciens et archives imbriquées ne sont pas couverts par le décodage de ce script. Le détail est dans [limites-pieces-jointes.json](resultats/limites-pieces-jointes.json).


## Déchiffrement réussi et comparaison des PDF

Le huitième mot de passe communiqué a permis le déchiffrement. Les **46 PDF sélectionnés ont été extraits sans erreur**, dans un nouveau dossier de travail. Le secret n’est inscrit ni dans les scripts ni dans les rapports.

Les **27 PDF de `L16B/TELEPHONES/IPHONE13_MINI` possèdent tous au moins un équivalent strictement identique par SHA-256 parmi ces fichiers de la sauvegarde TP-02**. La comparaison porte sur les octets déchiffrés, et non seulement les noms, tailles ou textes. Les correspondances détaillées restent dans `prive/comparaison-pdf-identites.json`. Le résultat public est dans [comparaison-pdf-tp02.json](resultats/comparaison-pdf-tp02.json) et la méthode reproductible dans `scripts/verifier_pdf_extraits.py`.

Les empreintes des 46 fichiers chiffrés sources, recalculées après extraction, sont identiques à celles relevées avant leur déchiffrement. Les empreintes des sorties ont également été recalculées ; toutes correspondent au journal d’extraction et toutes les sorties portent une signature PDF. Aucun fichier source n’a été remplacé.

**Portée :** ce résultat établit un contenu commun entre L16B et la sauvegarde identifiée comme TP-02. Il renforce le rapprochement du dossier Mini avec cet appareil, mais ne démontre pas que les fichiers proviennent exclusivement de ce téléphone, qu’ils étaient présents sur lui à la date de la saisie, ou qu’ils ont été copiés directement de ce téléphone vers OP-01. Des copies ou synchronisations restent possibles. Le PV ne fournissant pas les numéros de série des deux Mini, leur correspondance avec les scellés ne devient pas certaine par ce seul résultat.

Le mot de passe n’est plus un blocage pour cette comparaison, désormais achevée. Le support d’origine du CSV et l’archive finale restent à examiner ; le CSV fourni a depuis été comparé intégralement aux contenus locaux le 16 novembre.

## Lecture thématique des 27 PDF

La lecture du texte extrait montre 27 fichiers, correspondant à **20 contenus binaires distincts** (déduplication SHA-256). Ils regroupent des factures commerciales, loyers, devis Apple, factures NordVPN et des courriels bancaires, comptables ou juridiques exportés en PDF.

**Point complémentaire important :** `Rép  Dossier bourarach.pdf` reproduit des échanges de juillet-août 2017 avec **Me Isabelle Guillou**, concernant un recours au tribunal administratif de Montreuil, des justificatifs et des honoraires. Ce nom ne figurait pas dans les motifs de la recherche initiale fondée sur la liste manuscrite. L’absence de correspondance à ces motifs dans les 27 PDF ne signifie donc pas l’absence de documents contenant des échanges avec un avocat. Ce constat documentaire ne prouve toujours pas l’inclusion du PDF dans le jeu définitivement saisi.

La facture Technocity `facture rct 0801.pdf` et ses deux doublons portent le libellé « CAMERA INSTALLATION », une date imprimée du 02/05/2023 et un total de 1 500 euros pour RCT. Elle constitue une piste documentaire relative à une installation de caméra, sans identifier les caméras de la mission ni démontrer leur date effective d’installation.


## 5. Dernier clip du salon

Le clip examiné est `714049800_20241015_132800_10_0277.mp4`, déjà extrait de SD-03. Des planches ont été produites à raison d’une image toutes les cinq secondes sur le clip, puis d’une image par seconde sur sa dernière minute environ. Les planches ont été examinées visuellement ; ce contrôle est un **échantillonnage**, pas une lecture image par image de l’intégralité du flux.

Les images montrent plusieurs personnes manipulant notamment des documents. Vers 13 h 31–13 h 32 selon l’incrustation caméra, une personne tient un petit objet rectangulaire compatible avec un téléphone. La résolution ne permet pas de constater son état d’alimentation, un déverrouillage, son numéro de série ou son propriétaire. Aucun acte de fermeture de scellé ni manipulation directe de la caméra n’est établi par ces vues. Un geste bref entre les images échantillonnées ne peut être exclu.

Une piste MP3 mono à 16 kHz a été dérivée pour une tentative de transcription locale. Le modèle Whisper small, langue française et détection vocale activée, a produit **zéro segment**. Le résultat et les paramètres sont dans [transcription-meta.json](resultats/transcription-meta.json). La première tentative a échoué sur une incompatibilité PyAV ; la seconde a utilisé un décodage PCM par ffmpeg. **Aucune écoute humaine validée n’a été réalisée et aucune absence de parole n’est déduite de cet échec de transcription.**

Les conclusions techniques antérieures restent inchangées : dernière image décodée vers 13 h 32 min 26 s selon la caméra, piste sonore de 277,760 secondes, écart audio/vidéo de 11,589 secondes et défaut structurel récurrent sur d’autres clips. Ces planches du clip commençant à 13:28 ne démontrent ni coupure volontaire ni identité d’auteur ; le démarrage antérieur des téléphones est traité séparément dans la note de constatation du 16 novembre.


## 6. SMS expliqués et pièces encore utiles

Les corps des trois SMS du 28 ont été contrôlés le 9 novembre. Mme Sadedine explique dans son [courriel du point 3](../../docs/mail-3.txt) les démarches de réinitialisation Microsoft et de validation Google qu’elle a effectuées. Le [contrôle SMS](../20261109-sms-lecture/compte-rendu.md) est une justification technique conservée ; ce point ne reste pas une piste suspecte.

L’explication privilégiée des deux factures est leur conservation dans la sortie Sage malgré la suppression de `test.pdf`, sur la base de la comparaison textuelle normalisée. Elle ne prouve pas l’identité graphique ou binaire de ces deux PDF. Pour le parcours des PDF Mini et les exclusions annoncées, les journaux du logiciel de collecte, l’archive finale, les rejets et le support d’inventaire sont nécessaires. L’écoute humaine validée du clip salon n’est pas présentée comme réalisée ; zéro segment de transcription automatique ne signifie pas absence de parole.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe Donnat — Donnat Dev
