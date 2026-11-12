# Complément technique à la lecture du PV — 8 novembre 2026

**Dossier : SADEDINE-2026. État au 8 novembre : contrôles partiels. Mise à jour du 9 novembre : résultats SIFT récupérés et vérifiés ; voir la [reprise détaillée](reprise-20261109.md), qui actualise les passages ci-dessous relatifs à l’indisponibilité de SIFT. Mise à jour ultérieure : déchiffrement réussi au huitième essai, 46 PDF extraits et 27/27 PDF de L16B retrouvés identiques dans TP-02 ; voir la reprise détaillée.**

Ce complément exécute les vérifications proposées dans la [lecture du PV](../20261108-analyse-pv/compte-rendu.md). Il distingue les résultats acquis des sélections automatiques restant à examiner. Le CD d’inventaire est confirmé indisponible par le prestataire. Aucune équivalence entre le dossier informatif L16B et le jeu définitivement saisi n’est présumée.

## 1. Préservation et méthode

OP-01 a été monté sur SIFT par EWF, boucle en lecture seule, Dislocker en lecture seule, puis NTFS avec les options `ro,norecover`. Le journal de montage est dans `journaux/montage.txt`. Les recherches portent sur des extractions existantes et le système de fichiers ainsi monté. Les bases SMS et Manifest de TP-02 ont été copiées dans un répertoire de travail isolé avant interrogation ; les empreintes des fichiers sources contrôlés avant et après sont identiques. Les scripts sont conservés dans `scripts/`. Les documents, chemins détaillés et images contenant des données privées sont dans `prive/`, exclu de Git.

La version antérieure du rapport final est conservée dans `rapports-avant/`. Les rapports historiques ne sont pas réécrits. Les sorties anciennes ou les tentatives échouées sont conservées et explicitement distinguées des résultats utilisables.

## 2. Messageries et noms de l’annexe au PV

La recherche sur SIFT s’est terminée sans erreur signalée dans stderr. Son résumé, reçu avant la perte de connexion, est conservé dans [sift-resume-provisoire.json](resultats/sift-resume-provisoire.json). Il annonce :

- 6 206 messages parcourus, huit fichiers mbox, trente EML et un mbox Takeout ; trois textes WhatsApp ;
- 6 419 pièces jointes, dont 3 971 avec texte décodé et 2 448 entrées de limitation/erreur à qualifier ;
- dix-sept messages candidats à identifiants distincts, aucun résultat dans les trois textes WhatsApp ;
- cinq occurrences pour Pascoet, six pour Meyer, une pour Dress, cinq pour Negrevergne et une pour Liwer. Un message peut correspondre à plusieurs motifs ; ces nombres ne s’additionnent donc pas en dix-sept messages distincts ;
- vingt-sept PDF du dossier Mini traités ; empreintes avant/après annoncées identiques pour toutes les sources contrôlées.

**Ces résultats sont des candidats lexicaux, pas des correspondances d’avocats confirmées.** Les motifs recherchent principalement des noms de famille, parfois ambigus ; la lecture manuscrite de certains noms doit également être vérifiée. Les pièces jointes non décodées et les documents image sans OCR empêchent toute conclusion d’exhaustivité. La recherche est bornée aux formats et limites du script `analyse_sift.py`.

Les fichiers détaillés, contextes privés, empreintes individuelles et textes PDF sont restés dans `/home/sansforensics/analysis/complement-pv-20261108` sur SIFT. Lors de la reprise, la connexion `ssh -F /home/chris/.ssh/config sift` est refusée sur le port 2222. Leur examen est donc **en attente**, sans conclusion sur un manquement au filtrage annoncé dans le PV. Même une présence dans L16B ne démontrerait pas la présence dans le jeu définitivement saisi.

## 3. Inventaire externe et documents comptables

La recherche nominale sur les répertoires alloués visés par le script ne signale aucun fichier correspondant aux noms d’inventaire, de rejets, d’archive externe ou à LdSD recherchés. Ce résultat ne constitue pas une recherche exhaustive de l’espace supprimé ni une preuve d’absence historique. Les références Windows déjà documentées restent valides.

Le CD étant indisponible, le contrôle de l’inventaire final et des empreintes de saisie reste impossible. Le texte de `sage.pdf` a été demandé sur SIFT ; la comparaison page par page avec les deux factures de `test.pdf` récupéré reste à réaliser après récupération des résultats. Aucun résultat de cette comparaison n’est annoncé ici.

## 4. TP-02 : fenêtre de vérification Apple et PDF

La fenêtre examinée est le **28 octobre 2024 de 11 h 30 à 12 h 15, heure de Paris**, par date de message ou date de lecture. Deux SMS reçus sont enregistrés à 12 h 03 min 14,750877 s et 12 h 10 min 04,455466 s ; les champs de lecture sont respectivement datés de 12 h 03 min 18,794336 s et 12 h 10 min 06,276799 s.

**Correction méthodologique :** le champ `text` est NULL pour ces deux messages, tandis que `attributedBody` contient respectivement 991 et 1 004 octets. Le premier résumé automatisé avait marqué `apple_mentioned: false` sur la seule colonne `text`. Ce résultat n’est pas interprétable comme une absence de message Apple. Le [résumé corrigé](resultats/sms-fenetre-resume-corrige.json) remplace ce booléen par une valeur indéterminée. À la date de ce complément, le décodage du corps restait à effectuer. Le [contrôle ultérieur du 9 novembre](../20261109-sms-lecture/compte-rendu.md) extrait les chaînes des corps : le premier message mentionne un code de réinitialisation Microsoft et le second un code de validation Google ; un troisième SMS à 12 h 46, hors de cette fenêtre, mentionne aussi un code de validation Google. Les dates de lecture proviennent du champ `date_read` de `sms.db` ; les deux lignes portent aussi `is_read=1`. Il s’agit donc d’horodatages conservés, et pas seulement d’un état « lu » observé lors de l’analyse. Ils ne prouvent ni une lecture humaine locale sur TP-02 à ces instants ni l’identité d’un lecteur : un marquage, une synchronisation depuis un autre appareil ou une restauration restent possibles.

Le parcours de toutes les entrées de fichiers réguliers du Manifest déchiffré dénombre **2 189 PDF**. Une sélection par identité de taille OU de nom normalisé avec les vingt-sept PDF de `L16B/TELEPHONES/IPHONE13_MINI` produit **46 fichiers candidats, représentant 8 026 257 octets**. La sélection et ses critères sont conservés dans `prive/pdf-selection.csv` et `prive/pdf-selection-matches.json` ; script reproductible : `scripts/selection_pdf.py`.

Le mot de passe proposé par le prestataire a été essayé une fois via saisie masquée. La bibliothèque retourne `IncorrectPassphraseError` lors de l’initialisation ; aucun des 46 PDF n’a été déchiffré par cette tentative. Le secret n’est pas enregistré dans les scripts ou rapports. Un mot de passe exact est nécessaire pour poursuivre.

Une correspondance de nom ou de taille ne constitue pas une identité de contenu. Aucune attribution du premier Mini du PV à TP-02 n’est tirée de cette sélection. Même une identité future de contenu devra être appréciée avec les possibilités de copie ou de synchronisation entre appareils.

## 5. Dernier clip du salon

Le clip examiné est `714049800_20241015_132800_10_0277.mp4`, déjà extrait de SD-03. Des planches ont été produites à raison d’une image toutes les cinq secondes sur le clip, puis d’une image par seconde sur sa dernière minute environ. Les planches ont été examinées visuellement ; ce contrôle est un **échantillonnage**, pas une lecture image par image de l’intégralité du flux.

Les images montrent plusieurs personnes manipulant notamment des documents. Vers 13 h 31–13 h 32 selon l’incrustation caméra, une personne tient un petit objet rectangulaire compatible avec un téléphone. La résolution ne permet pas de constater son état d’alimentation, un déverrouillage, son numéro de série ou son propriétaire. Aucun acte de fermeture de scellé ni manipulation directe de la caméra n’est établi par ces vues. Un geste bref entre les images échantillonnées ne peut être exclu.

Une piste MP3 mono à 16 kHz a été dérivée pour une tentative de transcription locale. Le modèle Whisper small, langue française et détection vocale activée, a produit **zéro segment**. Le résultat et les paramètres sont dans [transcription-meta.json](resultats/transcription-meta.json). La première tentative a échoué sur une incompatibilité PyAV ; la seconde a utilisé un décodage PCM par ffmpeg. **Aucune écoute humaine validée n’a été réalisée et aucune absence de parole n’est déduite de cet échec de transcription.**

Les conclusions techniques antérieures restent inchangées : dernière image décodée vers 13 h 32 min 26 s selon la caméra, piste sonore de 277,760 secondes, écart audio/vidéo de 11,589 secondes et défaut structurel récurrent sur d’autres clips. Ni coupure volontaire, ni allumage de téléphone, ni identité d’auteur ne sont démontrés.

## 6. Conséquences pour la synthèse et suite précise

Le rapport final est corrigé pour intégrer le PV désormais lu : arrivée à 10 h 22 distincte de l’ouverture du scellé du PC à 10 h 41, téléphones à 11 h 30, manipulation SIM à 11 h 45 et clôture à 19 h 20 distincte d’une heure individualisée de restitution. Il distingue la copie consignée par les agents de sa vérification technique incomplète.

Il reste à récupérer les sorties SIFT, qualifier les dix-sept messages et les limitations d’extraction, comparer les factures et examiner les métadonnées des vingt-sept PDF. Le déchiffrement des 46 candidats nécessite le bon mot de passe. Le CD indisponible constitue une limite documentaire indépendante. Aucun de ces travaux en attente n’est présenté comme achevé ou comme preuve d’irrégularité.
