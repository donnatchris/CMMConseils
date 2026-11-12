# Complément transversal — 16 octobre 2026

Rapport : [analyse-cartes_sd-transversale.md](../../analyse-cartes_sd-transversale.md).

## Préservation et périmètre

Réexamen **local** des campagnes SD-01 du 15 octobre et de son complément, SD-02/SD-03 du 16 octobre. Aucun accès aux EWF, à SIFT, aux cartes physiques, à une caméra ou à un compte. Aucun scan exhaustif, carving ou montage FAT nouveau. Les anciennes campagnes et leurs manifestes restent inchangés. Les médias conservés ne sont ni réécrits ni réencodés.

Les tests de compteurs et de pistes utilisent des `memfd` Linux anonymes. Les tests d'unités H.264 résiduelles utilisent des flux en mémoire, avec les paramètres SPS/PPS du fichier source. Aucun temps supplémentaire n'est inventé et aucune vidéo « réparée » n'est présentée comme originale. Les résultats ne constituent pas un examen visuel des quatre images supplémentaires ni une écoute audio.

Hôte : Python 3.14.4, FFprobe/FFmpeg 8.0.1. Pas d'installation, pas de dépendance Python tierce. Les résultats distants antérieurs proviennent d'un autre environnement, documenté dans les campagnes sources.

## Reproduction dans un répertoire neuf

Depuis la racine du projet, avec les médias privés des campagnes historiques présents :

```bash
python3 cartes_sd/scripts/sd_transversal_20261016.py --out cartes_sd/recherche-transversale/20261016-reproduction
python3 cartes_sd/scripts/sd_transversal_complement.py cartes_sd/recherche-transversale/20261016-reproduction
python3 cartes_sd/scripts/sd_transversal_validation.py cartes_sd/recherche-transversale/20261016-reproduction
python3 cartes_sd/scripts/sd_transversal_nal_residuel.py cartes_sd/recherche-transversale/20261016-reproduction
```

Ne pas relancer sur la campagne livrée : les résultats JSON/CSV refusent l'écrasement. Les deux scripts de décodage peuvent prendre quelques minutes sur un poste lent. Les scripts attendent les chemins, géométries et formats particuliers des dérivés de cette affaire. Ne pas les appliquer à d'autres supports sans adaptation. Ils n'importent ni n'exécutent les collecteurs antérieurs.

Le premier script contrôle les SHA-256 des 37 médias contre les inventaires et reparcourt leurs tables. Il extrait aussi les dernières PTS des deux anomalies SD-01 avec FFprobe. Le deuxième complète les contre-lectures FAT SD-01, les mesures audio et le décodage ciblé du dernier clip SD-03. Le troisième vérifie les artefacts consommés contre les manifestes historiques, corrige la population de comparaison SD-02 et teste en RAM les compteurs audio/vidéo des onze cas. Le quatrième décode les seuls préfixes H.264 non indexés identifiés dans deux zones précises.

Les sorties de la reproduction doivent retrouver les valeurs, tailles, offsets et SHA-256 des médias et flux dérivés. Les adresses mémoire des outils, chemins absolus de commande, identifiants de descripteur et heures de traitement peuvent varier. Le rapport reste un texte d'interprétation à relire.

## Artefacts

| Fichier sous `inventaires/` | Portée |
| --- | --- |
| `tables-ciblees.json`, `.csv` | 37 fichiers / 74 pistes ; comptes, règles, offsets, bornes, longueurs NAL, essais audio seuls |
| `fat-2000.json` | Vingt slots, champs bruts, première vérification binaire de douze slots |
| `fat-SD01-contrelecture.json` | Les neuf slots SD-01 contrôlés via l'index historique ; huit contrôles binaires supplémentaires distincts |
| `chronologie-croisee.csv` | Fichiers aux jours ciblés et données nominales ; SD-02 ne fournit aucune séquence de ces jours |
| `frames-SD01-*.json` | Nouveaux relevés de 2 170 et 134 images produites pour les deux fichiers SD-01 anormaux |
| `fins-comparees.json` | Fin audio, fin de table vidéo et dernière PTS produite, séparées pour les onze cas |
| `compteurs-video-et-zones-non-indexees.json` | Sept excédents de 13/26 et deux zones non indexées, SHA-256 et octets non nuls |
| `test-index-audio-video.json` | Modifications de compteurs en RAM, octets changés et disparition de `wrong sample count` |
| `nal-non-indexes.json` | Offsets des trois unités SD-01 et d'une unité SD-03, tests indexés/étendus, quatre images décodées supplémentaires ; aucun temps original ajouté |
| `ecarts-audio-video.json` | Distribution SD-01 et SD-03 ; SD-02 absent de ce premier tableau car ses colonnes CSV diffèrent |
| `ecarts-audio-video-SD02.json` | Population intermédiaire mixte de 3 310 métadonnées ; **ne pas utiliser comme population active** |
| `ecarts-audio-video-SD02-actifs.json` | Population corrigée : 3 300 MP4 actifs analysables, utilisée dans le rapport |
| `audio-714049800.json` | Décodage PCM, durée, empreinte et énergie/pics par seconde ; aucune interprétation sémantique |
| `video-erreur-714049800.json` | Commande et voisinage des messages H.264 vers PTS 125,176 s |
| `conversion-1999.json` | Deux sens de conversion Paris/UTC, sans origine d'affichage authentifiée |
| `sources*.json` | Empreintes des entrées consommées |
| `verification-manifestes-historiques.json` | 4 391 concordances, zéro divergence, aucune entrée consommée non couverte dans le périmètre historique contrôlé |
| `contexte-transversal.json` | Métadonnées `System Volume Information` des trois cartes et empreintes des manifestes historiques |
| `controle-livraison.json` | Assertions de cohérence et liens du rapport |

Les scripts et leurs empreintes d'exécution sont référencés dans `journaux/`. Les commandes FFprobe/FFmpeg complètes figurent dans les JSON de chaque test. Le journal `decodage-showinfo-714049800.txt` conserve le décodage technique complet ; il ne contient pas d'images. Aucun PCM n'est conservé en clair comme nouveau fichier : son empreinte et ses mesures sont enregistrées.

## Incidents et populations intermédiaires

Deux premiers essais sont conservés sous `../20261016-essais/`, sans valeur de résultat final. Le premier avait sélectionné comme voisin une entrée temporaire supprimée de SD-01, limitée à un préfixe de 16 384 octets : le parseur strict a refusé sa boîte dépassant la taille. Le filtrage des voisins a été corrigé pour retenir les fichiers actifs. Une relance dans le même dossier a ensuite refusé d'écraser les relevés d'images déjà produits. La campagne finale a donc été exécutée dans un dossier neuf. Aucun de ces incidents n'a écrit dans les médias ou les images sources.

La population SD-02 de 3 310 métadonnées du complément incluait des fichiers supprimés récupérés. La validation reprend les seuls identifiants actifs de l'inventaire chronologique : 3 300 vidéos finalisées. Les deux tableaux sont conservés et explicitement distingués. Le zéro SD-02 dans le premier tableau signifie absence de colonnes audio/vidéo dans son CSV, pas absence de données audio ou vidéo.

Les corrections expérimentales de compteurs alignent `stsc` sur `stsz`. Leur succès dans FFprobe démontre la cause de cet avertissement, pas la validité historique de `stsz` ni la restauration complète du contenu. L'audio seul ne supprime pas les erreurs de compteurs vidéo des sept fichiers concernés. Un flux sans erreur de délimitation NAL peut encore produire des erreurs de décodage H.264 interne.

## Clôture et manifeste

Contrôle :

```bash
python3 cartes_sd/scripts/sd_transversal_qa.py
sha256sum -c cartes_sd/recherche-transversale/20261016/manifest-sha256.txt
```

Le manifeste de ce complément couvre le rapport transversal, les scripts nouveaux, ce dossier et les sorties des essais conservés. Il exclut son propre fichier. Les artefacts historiques ne sont pas dupliqués : leurs chemins, empreintes et manifestes sont référencés. La remise technique doit inclure les médias privés historiques, exclus de Git. Aucun commit, transfert cloud ou envoi à un tiers n'est réalisé par cette campagne.
