# TP-02 — tailles MBFile, contenus SQLite et fiabilité

## Résultat

Les écarts ne proviennent pas d’une conversion d’unité de taille par `iphone_backup_decrypt`. Le code local lit directement `MBFile.Size` comme entier et déchiffre l’objet complet en retirant seulement son padding. **Les nouveaux profils d’en-tête rendent plausible une réécriture/sérialisation des bases lors de leur sauvegarde ; ils ne démontrent ni son mécanisme exact ni une falsification.** La lecture des lignes conservées reste étayée ; l’exhaustivité de l’instantané et des données supprimées ne peut pas être certifiée.

## Audit de la bibliothèque réellement utilisée

Version locale 0.11.2, fichiers et SHA-256 consignés dans `backup-details.json` :

- `utils.py`, `FilePlist.__init__` : `self.filesize = int(self._data.get("Size"))` (ligne 120).
- `iphone_backup.py`, `_decrypt_file_to_disk` : déchiffrement chunked de l’objet, puis comparaison de taille (lignes 259–268) ; aucune troncature à la taille MBFile.
- `utils.py`, `aes_decrypt_chunked` : longueur AES multiple de 16, validation/retrait du padding final, écriture des blocs et comptage de taille (lignes 384–439).

Le [code amont de l’auteur](https://github.com/jsharkey13/iphone_backup_decrypt/blob/master/src/iphone_backup_decrypt/iphone_backup.py) documente lui-même des différences de taille fréquentes sur des bases actives ; il évoque un bug iOS ou une course comme hypothèses. Ce commentaire ne prouve pas la cause dans ce dossier. Le code **local haché** est la référence pour le comportement exécuté, l’amont ayant pu évoluer.

## Résultats nouveaux sur les cinq bases prioritaires

Toutes ont des pages de 4 096 octets, en-têtes read/write version 2 (mode WAL), change_counter=version_valid_for=2, version SQLite inscrite 3043002, **zéro page de freelist**. La taille en pages de l’en-tête correspond au contenu déchiffré. Les différences sont des nombres entiers de pages :

| Base | MBFile moins contenu | Pages d’écart | Compagnon WAL/SHM/journal référencé |
|---|---:|---:|---|
| Photos.sqlite | 65 183 744 octets | 15 914 | aucun |
| healthdb.sqlite | 61 440 | 15 | aucun |
| healthdb_secure.sqlite | 1 245 184 | 304 | aucun |
| sms.db | 524 288 | 128 | aucun |
| CallHistory.storedata | 159 744 | 39 | aucun |

Pour Photos : 835 297 280 octets annoncés, 770 113 536 en clair, 188 016 pages. Le contenu chiffré ne dépasse le clair que du padding attendu ; 65 Mo ne sont pas dissimulés dans un retrait de padding de 1–16 octets. Les vérifications de SHA-256 chiffrés/déchiffrés ont été refaites pour ces cibles, en conservant les contrôles Digest/SHA-1 déjà exécutés, sans refaire le déchiffrement général.

**Profil plus large inédit :** les 254 bases de l’inventaire confirmé ont toutes zéro page libre déclarée ; **185** partagent exactement `(change_counter=2, freelist=0, version_valid_for=2, sqlite_version=3043002)`. Les autres profils sont conservés dans `sqlite-header-patterns.json`. Un tel profil transversal est compatible avec la production de copies SQLite normalisées plutôt qu’avec les tailles et compteurs de fichiers actifs inchangés. Ce constat ne prouve pas l’usage d’une API particulière. Une base naturellement petite ou nouvellement créée peut également avoir ces valeurs.

Les 92 écarts de la passe principale vont dans **les deux sens** : MBFile plus grand dans 73 cas, plus petit dans 19. Le complément WhatsApp déjà contrôlé porte le total précédent à 94. Une explication universelle par simple suppression de pages ne rendrait pas compte, à elle seule, des deux signes. Les raisons possibles peuvent différer selon les fichiers.

## WAL, transactions et explications documentées

SQLite documente que des transactions validées peuvent résider dans un [WAL séparé](https://www.sqlite.org/wal.html), et que la [copie d’une base active par API de sauvegarde](https://www.sqlite.org/backup.html) produit un instantané sans assimiler une copie brute du seul fichier principal à l’état actif. Ici le manifeste ne référence aucun compagnon pour les cinq bases. Cela interdit de présenter un WAL « retrouvé » ou de prétendre rejouer des transactions absentes ; cela ne démontre pas qu’un WAL existait ou non sur le téléphone au moment de la sauvegarde.

SQLite documente aussi qu’un [VACUUM INTO](https://www.sqlite.org/lang_vacuum.html) peut créer une copie plus compacte avec le même contenu logique et purger des espaces de données supprimées. Cette propriété démontre qu’une différence de taille n’implique pas nécessairement la perte de lignes vivantes. **Aucun VACUUM n’a été lancé sur les pièces, et son utilisation par Apple n’est pas démontrée.** Le profil d’en-tête et de freelist soutient seulement la famille d’explications « copie reconstruite/sérialisée ». Une capture des métadonnées avant une modification de base, une course de sauvegarde ou une copie incrémentale incohérente restent possibles ; leur choix nécessite des sources contemporaines.

Les transactions `ATRANSACTION` de Photos sont des lignes historiques applicatives **à l’intérieur** de la base, distinctes des frames WAL de SQLite. Leur conservation n’implique pas que le WAL de 2024 soit encore présent. Les opérations récentes de l’acquisition ne peuvent pas être datées à partir du seul numéro de version de l’en-tête.

## Incidence sur les conclusions

| Proposition | État après contrôle |
|---|---|
| « Les octets analysés sont ceux de l’extraction enregistrée » | Revérifié par SHA-256 pour les cibles ; les objets chiffrés correspondants concordent également |
| « Les 65 Mo Photos manquent parce que le déchiffreur tronque à une mauvaise taille » | Rejeté par code et relation chiffré/clair |
| « Les lignes et jointures conservées sont lisibles et reproductibles » | Étayé ; contrôles SQLite précédents conservés, lectures ciblées reproductibles |
| « Toute l’activité et toutes les suppressions de 2024 sont représentées » | Non établi ; les lignes peuvent être purgées, champs remplacés, WAL/espaces libres exclus |
| « Les dates conservées sont des dates de gestes sur TP-02 » | Non établi ; sémantique et provenance restent à démontrer séparément |
| « Les écarts prouvent une falsification » | Non soutenu |

Les écarts ne justifient pas de déplacer arbitrairement les timestamps extraits. Ils empêchent toutefois d’assimiler la copie logique à un instantané physique complet ou d’inférer une absence d’événement à partir d’une absence de ligne. La séquence ScreenshotServices dont l’actif a disparu mais dont l’historique persiste illustre concrètement cette différence de couverture, sans démontrer une cause liée aux écarts de taille.

La meilleure vérification consiste à comparer, sur une **nouvelle acquisition documentée** ou une sauvegarde historique disponible, métadonnées MBFile, copie SQLite produite par le logiciel, fichiers originaux/WAL et journal Mac. Une nouvelle extraction par une autre implémentation peut contrôler le retrait du padding, mais n’expliquera pas seule pourquoi l’objet sauvegardé est plus petit que Size. Si elle devient nécessaire, le mot de passe devra être saisi interactivement ; aucune clé persistante n’a été créée ici.
