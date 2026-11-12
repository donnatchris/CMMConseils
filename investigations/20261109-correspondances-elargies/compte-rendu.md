# Recherche élargie des correspondances et contrôle documentaire

**Mission SADEDINE-2026 — 9 novembre 2026. Campagne clôturée sur les résultats prioritaires à la demande du prestataire ; OCR non exhaustif.**

## Objet et portée

Cette campagne prolonge la lecture du PV et la comparaison des PDF Mini. Elle recherche des échanges et documents juridiques au-delà des noms de la liste manuscrite, puis les rapproche de leurs emplacements, doublons et traces de fichiers. Elle ne qualifie pas juridiquement les documents comme protégés ou irrégulièrement saisis.

Le prestataire indique ne pas croire disposer de l’ordonnance ni d’une proposition de rectification. Aucun fichier de ce nom n’a été identifié dans les documents de cadrage locaux. Des pièces fiscales **antérieures** ont en revanche été retrouvées dans le corpus : elles sont distinguées de l’ordonnance de visite et d’une éventuelle rectification postérieure aux opérations d’octobre 2024. Le CD d’inventaire reste indisponible.

## Méthode et préservation

OP-01 est remonté sur SIFT avec boucle en lecture seule, Dislocker `-r` et NTFS `ro,norecover`. Les messages proviennent des huit mbox extraits des deux PST, des trente EML présents dans L16B et du mbox Takeout. Les documents indépendants de L16B aux formats sélectionnés sont également inclus. La campagne ne porte pas sur tous les fichiers du disque ni sur l’espace non alloué ; elle ne constitue pas une nouvelle acquisition.

La collecte dénombre **6 206 occurrences de messages**, **5 300 contenus binaires distincts** et **1 487 fichiers sources suivis**. Les SHA-256 avant et après collecte sont identiques pour ces sources. Les pièces jointes sans nom sont prises en compte par leur contenu ; les images intégrées sont incluses. La déduplication SHA-256 évite de compter plusieurs copies identiques comme des documents indépendants. Une expansion bornée des archives ajoute des contenus à ce corpus ; ses limites sont conservées séparément.

Une première collecte a échoué sur un en-tête malformé ; elle est conservée comme tentative incomplète. La version aboutie conserve la valeur brute de l’en-tête si son analyse structurée échoue. La connexion SSH de la première passe OCR s’est interrompue ; 1 650 résultats journalisés ont été préservés, puis les éléments restants ont été relancés dans un nouveau dossier, avec journal persistant sur SIFT. Les fichiers sources et les sorties partielles antérieures ont été conservés.

Les scripts et journaux sont dans `scripts/` et `journaux/`, les contenus et index détaillés dans `prive/`. Aucun mot de passe n’est inscrit dans les scripts ou rapports.

Le décodage utilise Poppler pour les PDF, les parties XML des formats bureautiques récents, antiword pour les anciens Word, xlrd pour les classeurs XLS et une lecture approximative des RTF. L’OCR Tesseract français/anglais vise les images suffisamment grandes et les pages PDF dont le texte extractible est inférieur à soixante caractères hors espaces. Les PDF comportant déjà du texte ne sont donc pas intégralement soumis à OCR : un élément image au sein d’une page textuelle peut rester non reconnu. 

Le bilan final comprend **3 841 résultats avec une méthode de décodage, 395 sans décodage et 2 erreurs**. Un statut « décodé » ne garantit pas une lecture complète. Tesseract a produit **2 576 OCR de pages PDF et 543 OCR d’images**. Les limites journalisées comprennent 298 petites images non OCRisées, 91 formats non pris en charge, six échecs de lecture native PDF avec nombre de pages non vérifié, deux lectures RTF approximatives, une erreur de valeur et un dépassement de délai. Les catégories peuvent se recouper ; voir `resultats/bilan-extraction.json`. Une tentative d’expansion d’un fichier `.gz` comme archive ZIP a échoué ; ce contenu n’est pas réputé examiné. Les petites images, formats non pris en charge, délais d’exécution dépassés et échecs sont explicitement consignés. L’OCR peut produire des erreurs ; les candidats ne sont pas assimilés automatiquement à des correspondances d’avocats.

## Résultats documentaires vérifiés

### Échanges supplémentaires

La lecture des en-têtes et des corps a confirmé des échanges absents du premier repérage par noms :

- **Mustapha Khallouki** : dissolution/radiation d’EXPERT 2 MOBILE, état civil du liquidateur, échanges avec un expert-comptable et transferts de la correspondance ;
- **Nicolay Fakiroff / Roosevelt Avocats**, avec Olivier Legrand en copie de certains messages : rendez-vous, acompte et justificatif concernant ALMU ;
- **Marc-Alexandre Wahrheit** : virements et confirmations pour ALMU. Un autre message porte une adresse orthographiée `wahreit`, conservée telle quelle et non attribuée automatiquement au même cabinet ;
- plusieurs messages adressés à **Véronique Duffay**, à **Pascal Coriou** ou à un destinataire incomplet « Cabinet » utilisent « Maître ». Leur qualité et rôle doivent être vérifiés : ce titre seul n’établit pas une correspondance avocat-client.

La sélection comporte **41 occurrences de messages**, et non 41 conversations distinctes ni 41 correspondances juridiquement protégées. Le [tableau des messages](tableau-messages.md) donne une ligne par occurrence sélectionnée, avec date d’en-tête, sujet, nature et question à soumettre à l’avocate. Les chaînes citées peuvent se répéter entre messages ; leur date ne date pas l’extraction, la lecture ou la copie lors de la saisie. Les Message-ID, sources, index et empreintes des enregistrements exportés sont conservés dans `prive/table-messages-preuves.json`.

### Documents à distinguer selon leur nature

La passe native sur les PDF a repéré **62 contenus distincts** comportant un terme de profession juridique ou de procédure fiscale. Ils ne sont pas tous des documents sensibles : on y trouve des conditions générales, prévisionnels, avis fiscaux avec formules standard, un CV et même des mentions du fruit « avocat ». La consolidation avec les résultats OCR, les autres formats et les deux titres contrôlés séparément porte le [tableau des documents](tableau-documents.md) à **87 contenus distincts**, y compris les faux positifs documentés.

Les éléments utiles comprennent notamment la proposition de services Aston, le PDF reproduisant l’échange avec Pascoët, le PDF Mini reproduisant les échanges avec Guillou, mais aussi des courriers de **Jonathan Rubio adressés à l’administration fiscale en septembre 2022**. La première page de quatre PDF ciblés a été rendue et examinée pour vérifier les en-têtes et la nature des documents. Le nom de Rubio est visible dans un en-tête graphique que le texte natif ne restituait pas.

**Un courrier d’avocat adressé à l’administration ne doit pas être confondu avec un échange confidentiel entre l’avocat et son client.** La qualification et l’usage possible de chaque document doivent être examinés séparément. De même, un paiement à un cabinet dans un relevé bancaire n’est pas en lui-même une correspondance avocat-client.

Le décodage de l’ancien fichier Word `221115  fac.doc`, joint au message M02611, révèle un état de frais et honoraires de Marc-Alexandre Wahrheit pour ALMU, daté du 15 novembre 2022, concernant l’étude du dossier, un rendez-vous et la rédaction d’un contrat. Il complète les échanges et justificatifs de virement ; sa protection et son inclusion dans le jeu saisi restent à vérifier.

La note `220301 ALMU HONORAIRES.pdf` porte sur des honoraires de commissaires-priseurs judiciaires (Kapandji Morhange), et non d’avocats ; la première page de `ASSIGNATION AUBERVILLIERS.pdf` est un avis de renvoi d’audience. Le titre de fichier ne suffit donc pas à classer ces pièces.

### Pièces fiscales antérieures retrouvées

**Découverte confirmée visuellement :** `RECTIFICATION JUILLET 2022.pdf` est un scan de 56 pages dont la première porte « Proposition de rectification suite à une vérification de comptabilité », la date du **29 juillet 2022**, le nom de **DMM CONSEILS** et la période **01/01/2019–31/12/2020**. Chemin dans l’image : `C:\L16B\LOCAL\DMM\RECTIFICATION JUILLET 2022.pdf`. SHA-256 : `df165f7996f1f8cbd637d30692a034f04e676884fa74dbc429e26b91e69c143d`. Il s’agit d’une pièce disponible dans le corpus, même si elle n’avait pas été fournie séparément parmi les documents de cadrage. Cette date portée sur le scan ne constitue pas une authentification indépendante du document.

Le corpus comporte des courriers de prorogation et de désignation de bénéficiaires de septembre 2022, des observations du contribuable du 11 octobre 2022, une réclamation relative à un AMR du 28 novembre 2023, un courrier à Audire Conseil du 29 novembre 2023 et une requête DMM reçue au tribunal administratif de Montreuil le 16 juin 2024. Ils renvoient à une proposition de rectification du 29 juillet 2022 ; une référence au 20 juillet figure aussi dans l’objet d’un courrier et n’est pas harmonisée artificiellement.

**Ces pièces préexistantes ne démontrent pas l’utilisation des données saisies en octobre 2024 pour fonder une rectification ultérieure.** Les clauses génériques d’avis d’impôt mentionnant une proposition de rectification sont écartées comme preuve de la présence de la proposition recherchée. Les circulaires générales sur les scellés et les procès-verbaux descriptifs immobiliers de 2019 ne sont pas l’ordonnance de visite de cette affaire.

### Exports WhatsApp

Les trois textes WhatsApp ont été recherchés avec les noms et termes élargis. Un seul texte correspond, sur un emploi non juridique du mot « maître » ; il est écarté comme faux positif. Aucune correspondance d’avocat n’est identifiée par ces motifs dans ces trois textes. Ce résultat ne porte pas sur les éventuels médias absents des exports et ne vaut pas preuve d’absence universelle. Les empreintes des archives avant et après ce contrôle sont identiques.

## Emplacements et traces : exemple du PDF Guillou

Le contenu `Rép  Dossier bourarach.pdf` est identifié sous `L16B/TELEPHONES/IPHONE13_MINI/`, SHA-256 `2e82aa66ecbc307a98ce2a170799bed53af49c0de9dd9c0c2da00c87c530df3c`. Son identité avec un PDF de TP-02 a été établie lors du complément précédent.

Les métadonnées NTFS `$FILE_NAME` portent le **28 octobre 2024 à 17 h 13 min 43,799497 s, heure de Paris** ; `$STANDARD_INFORMATION` conserve une création du **15 octobre à 13 h 42 min 57,930 s** et une modification de 2019. Ces champs ne permettent pas de dater à eux seuls une extraction depuis le téléphone : certaines dates peuvent être conservées lors d’une copie.

Deux références Jump List pointent vers ce fichier ; leurs dernières dates d’interaction conservées se situent le **29 octobre vers 1 h 45 min 21 s, heure de Paris**, donc après la restitution consignée le 28. **Elles ne prouvent pas une lecture par un agent pendant les opérations.** Le champ `TrackerCreatedOn` n’est pas assimilé à une ouverture du document. Le rapprochement avec les dix paires de corbeille connues ne retrouve pas d’identité de contenu pour ce PDF ; ce résultat limité ne prouve pas l’absence de toute suppression antérieure ou sur un autre support.

Les chemins des pièces indépendantes, leurs métadonnées MFT, références Jump Lists et rapprochements avec les empreintes de corbeille sont consignés dans `prive/table-documents-preuves.json`. Pour une pièce jointe, l’identification du message et de son conteneur ne devient pas une preuve de consultation individuelle de la pièce.

## Ce que ces recherches permettent — et ce qui manque

La recherche élargie apporte une liste plus précise de correspondances, de documents connexes et de faux positifs. Elle montre pourquoi le seul filtrage par les noms manuscrits ne permet pas de recenser tous les documents à examiner. Elle **ne démontre pas que l’administration s’est limitée à ce filtre**, ni qu’elle a conservé les documents repérés dans le jeu final.

Le contrôle décisif reste la comparaison avec l’inventaire et les fichiers définitivement saisis. L’ordonnance complète est nécessaire pour examiner leur rattachement aux agissements autorisés ; une éventuelle proposition de rectification postérieure et ses annexes seraient nécessaires pour examiner leur utilisation fiscale. Aucun de ces documents n’est réputé absent de l’administration du seul fait qu’il n’est pas disponible dans cette mission.

## Clôture priorisée et travaux restant possibles

À la demande du prestataire (« c’est trop long, termine le plus important et documente tout dans les rapports »), la passe exhaustive a été arrêtée le **9 novembre 2026 à 08:42 UTC (09:42 à Paris)**. **4 238 résultats d’extraction sur 5 365 contenus** sont journalisés ; **1 127 contenus n’ont pas de résultat terminé dans cette passe**. Ils ne sont pas réputés négatifs. Certains ont néanmoins été lus lors de la passe native ou des vérifications ciblées, notamment la première page de la proposition de rectification de 2022. Les résultats terminés, les sorties partielles et la liste précise des contenus restants sont conservés. Aucun travail OCR ne reste présenté comme achevé à tort.

Le fichier `prive/restant-a-traiter.json` permet une reprise ciblée ; `resultats/arret-documente.json` décrit l’arrêt. Pour la proposition de rectification de 56 pages, seule l’identification et les éléments de première page sont ici retenus : aucune analyse complète de ses motifs fiscaux n’est revendiquée.

Les suites les plus utiles sont : obtenir l’ordonnance et le jeu définitif saisi ; confronter les documents prioritaires aux fichiers emportés et aux rejets ; faire qualifier les échanges par l’avocate ; reprendre ensuite, si nécessaire, les seules pièces restantes pertinentes. L’achèvement d’un OCR massif ne remplacerait pas les pièces de procédure manquantes.

La recherche automatique sur les extractions terminées produit **396 candidats documentaires et 541 occurrences de messages candidats** au sens large (noms, termes généraux, corps ou pièces jointes). Ces nombres ne sont pas des nombres de correspondances d’avocats. Les tableaux de 87 documents et 41 messages constituent la sélection contrôlée ; les candidats larges restants sont conservés en annexe privée sans qualification automatique. Les deux occurrences supplémentaires du mot « avocate » concernent des programmes d’événements commerciaux (M03119 et M03138), non des consultations.

## Livrables et conservation de cette campagne

- `tableau-messages.md` : 41 occurrences sélectionnées, avec qualification documentaire et question à vérifier.
- `tableau-documents.md` : 87 contenus distincts, dont les faux positifs explicitement écartés ; les pièces prioritaires sont placées en tête.
- `prive/table-messages-preuves.json` et `prive/table-documents-preuves.json` : références complètes, sources, empreintes, métadonnées et rapprochements.
- `prive/extraction.jsonl`, `prive/restant-a-traiter.json`, `prive/recherche/` et `prive/extracted/` : 4 238 résultats, liste des 1 127 éléments restants, candidats automatiques et textes des 396 candidats documentaires. La passe native et les contrôles visuels sont conservés séparément.
- `resultats/` : bilans chiffrés, contrôle de collecte, arrêt documenté et empreintes des transferts ; `journaux/` : montage et progression OCR ; `scripts/` : procédures utilisées.
- Sur SIFT : `/home/sansforensics/analysis/elargi-20261109-v2` conserve les copies de travail et la passe initiale ; `/home/sansforensics/analysis/elargi-20261109-final` conserve la reprise arrêtée et les textes produits. Le nom « final » désigne ce dossier de travail, pas une extraction exhaustive.
- `rapports-avant/` conserve le rapport principal antérieur à cette mise à jour ; `prive/tableaux-intermediaires/` conserve l’état intermédiaire des tableaux. Les images forensiques sources n’ont pas été modifiées par cette campagne.

Contrôle final : les **403 fichiers de résultats transférés** ont les mêmes SHA-256 sur SIFT et dans le dossier local. Les décomptes, la partition terminé/restant et les liens locaux des rapports ont été contrôlés. Ce contrôle de transfert ne remplace pas l’authentification du jeu saisi par l’administration.
