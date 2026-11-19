# Récupération d’anciens états et actif Photos 23769

**Campagne ciblée clôturée après audit complet du manifeste et analyse des 55 nouveaux fichiers déchiffrés. La totalité des contenus de la sauvegarde n’a pas été déchiffrée : les critères d’arrêt et les reliquats sont explicites.**

## Nouvelle information conservée dans l’historique actif

Photos.sqlite, fileID `12b144c0bd44f2b3dffd9186d3f9c05b917cee25`, SHA-256 clair `a2102dc95e855b57c77232a7bcfc6490025dab4633672d115563b0923e29e4b0`. L’actif 23769 est absent de ZASSET actuel. L’historique déjà connu contient création SpringBoard/ScreenshotServices et purge 124593. **Nouvel examen des colonnes tombstone**, filtré par **ZENTITY=3 (Asset)** pour ne pas confondre des clés 23769 d’autres entités :

```sql
SELECT * FROM ACHANGE
WHERE ZENTITY=3 AND ZENTITYPK=23769 AND ZCHANGETYPE=2;
```

Ligne **ACHANGE.Z_PK=1493606**, transaction **124593** :

| Champ | Valeur brute |
|---|---|
| ZTOMBSTONE0 | `1554B10C-EA7E-4491-BD89-42C514ED67D4` |
| ZTOMBSTONE1 | `1` |
| ZTOMBSTONE2 | `Deleting expired asset from trash` |
| ZTOMBSTONE3 | `751880805.776` |
| ZTOMBSTONE4 | `1` |
| ZTOMBSTONE5 | même UUID que ZTOMBSTONE0 |

Cocoa donne pour ZTOMBSTONE3 **29 octobre 2024 07:46:45.776 UTC / 08:46:45.776 Paris**. **Le mapping de propriété n’est pas validé : ce n’est pas une nouvelle date de mise à la corbeille démontrée.** Les valeurs UUID et le libellé sont conservés dans une ligne d’historique encore allouée, pas récupérés dans un secteur effacé. Aucune nouvelle suppression pendant la rétention ni intention d’effacement n’est établie. L’UUID est retrouvé deux fois dans le même enregistrement ; cela ne fait pas deux preuves.

## Recherche interne effectivement exécutée

La freelist Photos est nulle, mais cela ne signifie pas que toutes les zones inutilisées sont nulles. Sur une copie, `dbstat` a identifié **28606 pages** des tables ZASSET, ZADDITIONALASSETATTRIBUTES et ACHANGE. Lecture des zones entre fin du tableau de pointeurs de cellules et début du contenu, et des chaînes de freeblocks avec bornes contrôlées : **2390389 octets non alloués**, **3463 octets de payload freeblock**, **8098 octets non nuls**, zéro erreur de structure.

La recherche de l’UUID précis, en UTF-8 minuscule/majuscule, UTF-16LE et UUID binaire big/little-endian, donne **zéro correspondance** dans ces seules zones. Pas de reconstruction validée d’une ancienne ligne de l’actif. Une recherche de cet UUID dans **toutes les entrées du manifeste** donne zéro chemin correspondant. Cela n’exclut pas un fichier portant un autre nom ni un fragment sans UUID.

[SQLite documente les pages B-tree, zones non allouées et freeblocks](https://www.sqlite.org/fileformat.html). Le script n’analyse pas les secteurs physiques de l’iPhone, ne scanne pas les médias et ne promet pas de récupérer une image. Les gaps entre cellules, overflow et les autres tables/index ne sont pas carvés ; couverture expressément limitée à une recherche pertinente et reproductible. `photo-23769-recovery.json` et `photo-recovery-run.log` contiennent les mesures, empreintes et bornes.

## WAL, autres états et objets

Le manifeste complet contient **78 fichiers compagnons** selon les suffixes exacts : 34 WAL, 34 SHM, 10 journal. Aucun compagnon des sept bases ciblées ni de Photos.sqlite. Les seuls compagnons système/Apple repérés par ce filtre sont itunesstored2.sqlitedb.migrated WAL/SHM ; les autres sont surtout applicatifs et ne sont pas tous extraits. Le suffixe ne garantit pas le format. Les copies de travail préservent/rejouent les compagnons disponibles ; pas d’immutable sur les bases analytiques.

Le recensement par noms de fichiers de la racine et des 256 sous-répertoires hex trouve **137844 objets à nom de 40 caractères hex**, tous référencés, **zéro objet orphelin** et zéro objet ordinaire référencé manquant. Aucun média n’a été lu pour ce contrôle. Pièce : `backup-object-census.json`. Ce contrôle de présence/noms ne retrouve pas des versions historiques remplacées. Les flux de tombstone sélectionnés sont désormais déchiffrés et examinés, comme détaillé ci-dessous.

**Motif d’arrêt du ciblage 23769 :** nouvelles métadonnées d’historique extraites, aucun ancien enregistrement supplémentaire dans les zones examinées, pas de WAL Photos disponible. Image non récupérée ; récupération générale de données supprimées non démontrée et non promise.

## SEGB : anciens contenus effacés et tombstones conservés

Les 24 SEGB comportent **5111 états 3** dont les payloads sont nuls ; les anciens contenus ne sont pas récupérés. Les états 1 de tombstone sont au contraire des enregistrements **encore alloués et valides**, pas des fragments carvés. Pendant la rétention, 20 métadonnées d’état 3 (toutes le 28) gardent une date mais aucun contenu ; elles ne donnent ni texte ni activité d’origine. 27 marqueurs de tombstone valides du 28 à 15:50 portent parsecd et des références d’index.

Le chemin tombstone/ ne suffit pas à déterminer l’état interne : certaines entrées sont écrites et leur CRC est valide. Les CRC des données originales supprimées ne peuvent pas être validés lorsqu’ils ont été mis à zéro ; cela n’est pas présenté comme une corruption ou falsification. [CCL documente les structures et états par son parseur](https://github.com/cclgroupltd/ccl-segb). Le CRC porte le payload, pas l’authenticité du timestamp d’index.

**Limite nouvelle de récupération :** on ne peut rattacher sûrement les 27 tombstones à des événements originaux en réutilisant les seuls offsets ; 27 slots sont retrouvés mais 22 tailles diffèrent et des dates de slots sont plus tardives. Aucun ancien contenu original récupéré, aucune image supplémentaire de 23769. On observe des marqueurs de retrait/entretien, sans dater une action humaine, sans en attribuer l’auteur et sans établir un effacement de preuve.
