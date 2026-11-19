# TP-02 et TP-03 — 15 octobre 2024, 13:25–13:51

Contrôle complémentaire du 16 novembre 2026. Toutes les heures sont en Europe/Paris, soit UTC+2 le jour étudié. Les fractions indiquent la précision des valeurs conservées, pas une exactitude d'horloge établie.


## Réponse en langage courant

**J’ai retrouvé des transactions de Mail/Fichiers et des métadonnées PDF dans la séquence du 15 octobre entre 13 h 25 et 13 h 51.** Elles attestent des enregistrements logiciels, sans prouver une ouverture d’application, une lecture du contenu ou une consultation humaine. Les dix-sept métadonnées de dernière utilisation favorisent l’historique conservé dans TP-03 ; les fichiers sont aussi présents dans TP-02. Les classes de protection actuelles ne datent pas un déverrouillage ancien. Cette note est une analyse produite pendant la mission, distincte des pièces reçues ; Q1 et B–E donnent les sources, comparaisons et limites.

## Réponse

**Oui, TP-03 conserve des traces datées d'activité logicielle liées à Mail et à Fichiers, ainsi que des attributs de dernière utilisation de 17 PDF. Aucun événement explicite ne démontre sur ce créneau un premier déverrouillage après redémarrage, un déverrouillage d'écran, une ouverture du menu de partage, un enregistrement ou une impression PDF.** Les contrôles comparables de TP-02 ne retrouvent pas cette séquence. Leur résultat négatif ne démontre pas une inactivité passée de TP-02.

Ces constats concernent les données sauvegardées et leur historique susceptible de suivre une sauvegarde ou une restauration. Ils ne constituent pas une attribution certaine de chaque événement au téléphone physique, à une personne ou à un geste d'interface.

## Traces et portée

| Objet de la recherche | TP-03 | TP-02 et limites |
|---|---|---|
| Premier déverrouillage après redémarrage | Aucun événement système daté identifié. Les deux marqueurs applicatifs `.FirstUnlock` déchiffrés portent les dates du 24/05/2024 à 11:59:27,075932 et du 17/09/2025 à 17:12:16,471633. | Aucun événement explicite du créneau identifié dans les investigations disponibles. Les marqueurs applicatifs présents au manifeste ne sont pas un historique exhaustif de déverrouillage. |
| Déverrouillage d'écran | Aucun événement daté identifié. Les états FrontBoard analysés antérieurement ne donnent pas de chronologie native exploitable d'octobre. | Même limite. Aucun code saisi, événement Face ID ou journal tactile identifié. |
| Mail | TCC, ligne 39529, à **13:25:26**, service `kTCCServiceUbiquity`. **33 transactions TipKit, 8164–8196**, attribuées au processus `MobileMail`, de **13:25:30,661993 à 13:29:09,106157**. | Aucune ligne TCC ni transaction TipKit Mail sélectionnée dans le créneau. Dans TP-03, les changements TipKit concernent 35 règles et 13 paramètres ; ils ne prouvent ni application au premier plan, ni lecture ou envoi d'un message. |
| Fichiers | TCC, ligne 39532, à **13:29:50**. **Cinq transactions TipKit, 254–258**, attribuées au processus `Files`, de **13:29:50,324222 à 13:29:50,341425**. | Aucune ligne TCC ni transaction TipKit Fichiers sélectionnée dans TP-02. Dans TP-03, sept changements de règles sont associés ; aucun chemin, PDF ou geste d'enregistrement n'est identifié. |
| Menu de partage | PeopleSuggester conserve `DeviceIdDate=13:41:02,145052`. | Le fichier ne contient que `DeviceId` et `DeviceIdDate` : ce n'est pas un événement d'ouverture du menu, de partage ou de désignation de destinataire. |
| PDF | **17 objets / 17 contenus** portent `com.apple.lastuseddate#PS` entre **13:41:24,049649000 et 13:50:23,397071838**. Pour 16, `LastStatusChange` tombe aussi dans la fenêtre. | Aucun `lastused` ou `LastStatusChange` de cette fenêtre parmi les 46 objets PDF TP-02 contrôlés. Aucun `Birth` des 72 objets comparés n'y tombe. Ces métadonnées ne prouvent ni génération, ni enregistrement, ni impression PDF. |

**Élément nouveau par rapport à la synthèse B–E précédente : les cinq transactions TipKit Fichiers de TP-03.** La base déchiffrée existait dans l'extraction générale. Le contrôle direct l'a interrogée sur la fenêtre exacte. Les lignes `ACHANGE` 403–409 visent exclusivement `CoreRuleRecord`. Les tables actuelles de donations et d'événements sont vides et l'unique conseil a `ZLASTDISPLAYED=NULL`. Le texte actuel de ce conseil, relatif au partage familial, ne démontre pas qu'il ait été affiché ni qu'un partage ait eu lieu.

La ligne TCC à **13:40:52** concerne **Musique**, et ne doit pas être attribuée à Mail ou Fichiers. Les lignes TCC ont `boot_uuid=UNUSED` et ne sont donc pas rattachées à une session de démarrage identifiée. Leurs valeurs d'autorisation ne prouvent pas un clic sur une boîte de dialogue.

Le modèle clavier conserve une mise à jour du compteur cumulé `tium.totalWordsTypedInSecondaryLanguage` à **13:35:42,098506**. Sans texte ni valeur précédente, ce champ ne date pas une saisie de code. Les préférences coreduetd étudiées antérieurement portent deux dates vers **13:50:40,668**, relatives à la maintenance et au tombstonage du flux `/app/activity`, sans geste documentaire identifié.

## Ce que les classes de protection permettent d'inférer

Le manifeste TP-03 attribue `ProtectionClass=3`, classe C, aux bases TipKit **Mail et Fichiers**, au modèle clavier et aux 26 exemplaires PDF contrôlés. TCC est de classe D (`ProtectionClass=4`).

La [documentation Apple](https://developer.apple.com/documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication) indique que les fichiers protégés jusqu'à la première authentification deviennent accessibles après ce premier déverrouillage et peuvent le rester après un verrouillage ultérieur. **Un accès après première authentification ne signifie donc pas que l'écran est actuellement déverrouillé.** Voir aussi les [classes de protection Apple](https://support.apple.com/en-mt/guide/security/secb010e978a/web).

**Si** les transactions conservées correspondent à de nouvelles écritures de contenu effectuées localement sur TP-03, à leurs heures déclarées, après un redémarrage, avec cette protection déjà applicable, elles appuieraient un état après première authentification, au plus tard à la première transaction Mail de **13:25:30,661993**. Les transactions Fichiers fournissent un indice supplémentaire de même nature à **13:29:50**.

La sauvegarde tardive ne certifie ni cette exécution locale historique, ni la continuité des classes depuis 2024, ni l'absence de transport ou de restauration de l'historique. Une date `lastused` ou de changement de statut n'établit pas à elle seule une lecture du contenu protégé. **Le premier déverrouillage reste donc non démontré ; son absence n'est pas démontrée non plus.**

La [note de constatation vidéo](../../NOTE-DE-CONSTATION-téléphones.md) relève des logos Apple à **13:25:19**, compatibles avec une séquence de démarrage, mais sans déverrouillage visible établi. Les horloges de la vidéo et des téléphones n'ont pas été étalonnées indépendamment ; la proximité des horaires ne suffit pas à relier formellement les transactions à ce démarrage.

## Méthode, vérification et sources

Les requêtes ont été exécutées sur **SIFT par SSH**, dans les acquisitions déjà déchiffrées. Aucun nouveau déchiffrement n'a été nécessaire. Les bases ont été ouvertes avec `mode=ro&immutable=1`, après vérification que leurs WAL présents étaient vides. Aucun rejeu de journal ni écriture dans les preuves n'a été réalisé.

Le contrôle principal a relu les TCC, TipKit Mail et Fichiers, le modèle clavier, PeopleSuggester, les deux manifestes et les marqueurs `.FirstUnlock` TP-03 déjà déchiffrés. Les **20 fichiers suivis ont des SHA-256 avant/après identiques**. Le complément Fichiers confirme également l'identité avant/après de sa base et du manifeste TP-03. Les requêtes et empreintes exactes sont dans les résultats JSON.

La recherche de marqueurs au sein des fichiers réguliers des manifestes est bornée aux motifs enregistrés dans le script : `.FirstUnlock`, knowledgeC, Powerlog, traces unifiées, Biome, keybag/lockstate, Print Center et fichiers nommés d'impression. Elle ne fournit pas de journal système du créneau. Le fichier `printing-settings.plist` de SumUp dans TP-02 porte des métadonnées du **12 novembre 2024**, hors fenêtre ; son nom ne démontre pas une impression le 15 octobre. L'absence d'un chemin dans une sauvegarde logique n'est pas la preuve de son absence historique sur l'appareil.

La sélection des 72 PDF repose sur les identités SHA-512 déjà établies dans la recherche Q1. Le présent contrôle relit leurs métadonnées directement dans les deux manifestes ; il ne recalcule pas une nouvelle fois toutes les empreintes des contenus PDF.

- [Contrôle SIFT : script](../documents-recus/verification-20241015-1325-1351/verifier_sift.py) et [résultats, requêtes, empreintes](../documents-recus/verification-20241015-1325-1351/resultats-sift-v2.json). La première sortie `resultats-sift.json` est conservée ; la version 2 corrige uniquement l'affichage du décalage UTC des attributs `lastused` hors fenêtre en heure d'hiver. Les valeurs brutes et les résultats du 15 octobre sont inchangés.
- [Complément Fichiers : script](../documents-recus/verification-20241015-1325-1351/complement_fichiers_sift.py) et [résultats](../documents-recus/verification-20241015-1325-1351/complement-fichiers-sift.json).
- [Analyse TP-03, sections 7.2 à 7.4](../../telephones/analyse-TP-03.md).
- [Rapport B–E antérieur](Rapport_investigations_B_C_D_E_SADEDINE-2026.md), pour les contre-épreuves système, FrontBoard et CoreDuet. Les cinq transactions Fichiers ci-dessus complètent sa synthèse.

**Conclusion utilisable :** dans l'état sauvegardé de TP-03, des traces datées de Mail, de Fichiers et de dernière utilisation de PDF existent entre 13:25 et 13:51 le 15 octobre 2024. Elles soutiennent une activité logicielle conservée dans cet historique, sans établir un déverrouillage daté, une consultation humaine, un partage, un enregistrement ou une impression PDF, ni leur auteur. Aucun équivalent n'est retrouvé dans les sources comparables contrôlées de TP-02 ; cela n'en démontre pas l'inactivité.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe Donnat — Donnat Dev
