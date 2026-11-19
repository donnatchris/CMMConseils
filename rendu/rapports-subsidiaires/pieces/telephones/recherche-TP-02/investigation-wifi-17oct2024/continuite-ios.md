# Continuité de l'installation iOS — investigation nouvelle du 14 octobre 2026

Le rapprochement matériel le plus significatif est nouveau : les **sept** lignes de `Photos.sqlite.ZMIGRATIONHISTORY.ZDEVICEUNIQUEID` contiennent exactement l'UDID de TP-02 présent dans les en-têtes de sauvegarde. Elles encadrent octobre 2024. Il ne s'agit pas simplement du même modèle d'iPhone. Le journal binaire de migration, désormais décodé, confirme les sept lignes. Une restauration iCloud est effectivement documentée, mais elle est datée du **11 juin 2024**, avant la période litigieuse. Aucune restauration après le 17 octobre n'est démontrée par ces résultats.

## Résultats et pièces

Les valeurs sources et conversions sont dans [installation-restoration-details.json](installation-restoration-details.json), [identifier-comparisons.json](identifier-comparisons.json), [photos-continuity-and-journal.json](photos-continuity-and-journal.json). Les empreintes, chemins déchiffrés, domaines et fileID sont dans [source-verification.json](source-verification.json). Les identifiants sont comparés intégralement en mémoire ; les sorties de synthèse publient leurs SHA-256.

**MobileBackup.** `HomeDomain/Library/Preferences/com.apple.MobileBackup.plist`, fileID `2f0b2af6ff2371fcfaf405572b94d0e8551c5659` :

- `RestoreInfo.RestoreDate` : 2024-06-11 12:00:31 UTC, soit 14:00:31 Europe/Paris ; `WasCloudRestore=true` ; versions source et destination `21F90`.
- `RestoreStateInfo.date` : 12:00:50.334277 UTC / 14:00:50.334277 Paris ; `isCloud=true`, `progress=1.0`, `state=4`, puis `AirTrafficFinishedRestoring=true`. Le sens exact de l'énumération 4 n'est pas indispensable à la constatation : les autres propriétés caractérisent explicitement une restauration cloud.
- Ni `DeviceTransferInfo` ni la variante `DeviceTrransferInfo` ne figurent dans ce fichier. Ce constat ponctuel ne constitue pas un historique exhaustif des transferts.
- `MegaBackupFlowStartDate` porte déjà une date de décembre 2023 ; ne pas confondre ancienneté d'une préférence et ancienneté de l'installation physique actuelle.

**Photothèque.** Toutes les lignes ci-dessous portent D16AP, le même UDID que TP-02 et le même `ZSTOREUUID` que `Z_METADATA.Z_UUID` actuel. Les dates exactes UTC et Cocoa sont conservées dans le JSON.

| PK | Date Europe/Paris | Build | Type / origine bruts |
|---|---|---|---|
| 1 | 11/06/2024 14:00:55.270360 | 21F90 | 3 / 2 |
| 2 | 03/09/2024 06:52:09.191969 | 21G93 | 2 / 8 |
| 3 | 06/12/2024 10:08:29.192623 | 22B91 | 2 / 8 |
| 4 | 21/02/2025 05:05:33.938345 | 22D72 | 2 / 8 |
| 8 | 16/03/2025 03:18:07.318947 | 22D82 | 0 / 8 |
| 10 | 28/04/2025 04:49:23.309826 | 22E252 | 2 / 8 |
| 11 | 25/05/2025 06:59:21.614924 | 22F76 | 2 / 8 |

Les changements de version du modèle de données accompagnent plusieurs changements de build. On ne doit pas transformer ces sept migrations de **photothèque** en sept restaurations de téléphone. `ZFORCEREBUILDREASON` est NULL pour les sept lignes. La date technique de fin de reconstruction en juin est proche de la restauration MobileBackup. Les reconstructions de l'index de recherche ultérieures ne démontrent pas une réinitialisation iOS.

**Journal miroir nouvellement exploité.** `CameraRollDomain/Media/PhotoData/Journals/MigrationHistory-change.plj`, fileID `e3f8a26449a3b2e3356f42998493a49ed5a71303`, SHA-256 `647eb6bbe11d8a080a6059578272892281675a43fa374c0576641037f96ac8ea` : sept dictionnaires binaires plist valides sont isolés dans les intervalles d'octets [21,382[, [403,1543[, [1564,3271[, [3292,6199[, [6220,9097[, [9118,11966[, [11987,14894[. Leurs dates, appareil et store correspondent aux sept lignes SQL. Le script valide les bornes du trailer bplist avant décodage ; il ne prétend pas documenter tout le format externe PLJ. Six autres signatures correspondent à des archives imbriquées, pas à six migrations supplémentaires. Les deux représentations d'un même historique corroborent sa lecture ; elles ne sont pas deux acquisitions indépendantes.

**Setup Assistant.** `purplebuddy` comporte `RestoreChoice=true`, `SetupState=SetupUsingAssistant`, `SetupDone=true`, `SetupFinishedAllSteps=true`. `SSDeviceType.hardwareModel=D79AP`, build17F80, diffère du D16AP actuel. C'est un contre-exemple concret à l'assimilation de toute préférence de configuration à une empreinte du matériel courant. Ce sous-état est historique ou hérité ; sa date de transport n'est pas établie. `chronicle` mentionne 17.4.1 et 18.1.1. `SetupLastExit` vaut **6 décembre 2024 11:00:19.000489 Paris** ; une sortie de l'assistant, notamment lors d'une mise à jour, ne suffit pas à établir une restauration. La date de migration Photos du même jour est à 10:08 Paris : ne pas les inverser ni les considérer comme simultanées. Le `CKStartupTime` de SetupAssistant est d'août 2025, pas un journal de démarrage d'octobre 2024.

## Ce que chaque identifiant permet de suivre

| Identifiant | Objet suivi et recoupement effectué | Restauration / synchronisation : limite vérifiée |
|---|---|---|
| UDID | Identifiant d'appareil Apple ; accord Info/Manifest et sept migrations Photos ; occurrences supplémentaires Safari, locationd, appstored, itunescloud, Accounts | Identifie le matériel auquel une valeur se réfère ; une chaîne archivée peut survivre au transport du fichier. Elle n'atteste pas physiquement son lieu d'écriture. |
| Photos store UUID | Store Core Data ; identique dans Z_METADATA, sept migrations, journal et mobileCPL.plist | Suit une lignée de base ; sa copie conserve sa valeur. Ce n'est pas un identifiant de Secure Enclave. |
| Health hardware identifier, identité 2 | Identité interne Santé ; identique à la préférence healthd et au contexte courant de la base | Aucun rattachement documenté à l'UDID ; la conservation exacte après restauration inter-appareils reste à tester. Le nom « hardware » ne suffit pas. |
| Health database identifier | Identité de base ; différente de l'identifiant précédent | Pas une nouvelle mesure du matériel ; peut suivre une base copiée. Pas de garantie de non-transfert validée. |
| Source Santé / modèle / version | Producteur et version logicielle ; source iOS 17.6.1 créée près de la migration Photos de septembre | Plusieurs appareils peuvent partager modèle et version ; les métadonnées de source peuvent accompagner les données. |
| Info.GUID, Status.UUID | Identifiants d'en-tête de sauvegarde ; valeurs hachées et recherche de correspondance littérale | N'établissent pas une installation remontant à 2024 ; pas de correspondance historique indépendante retrouvée par ce contrôle. Sémantique complète non validée. |
| UUID FSEvent / volume dans MobileBackup | État technique de suivi de sauvegarde, deux couples | Snapshot sans chronologie des volumes ; ni identité matérielle ni preuve d'absence de restauration. |
| Keybag UUID | Identité du conteneur de sauvegarde de trousseau | Ne remplace pas un numéro de série ; aucun lien historique Wi-Fi daté déchiffré dans les enveloppes internes. |

[Apple définit le device ID](https://developer.apple.com/help/glossary/device-id/) comme identifiant du dispositif. Cette définition ne rend pas authentique une ancienne chaîne extraite d'une base. La recherche littérale de huit identifiants sur 3 886 fichiers déchiffrés de taille au plus 32 Mio, hors trousseau, donne 13 correspondances ; elle n'est pas une recherche de toutes les formes d'encodage possibles. Voir [cross-artifact-identifier-matches.json](cross-artifact-identifier-matches.json).

## Tentative de réfutation de la continuité

Une restauration ultérieure d'un ensemble de fichiers pourrait conserver l'UDID historique, les dates et les transactions ; une copie logique de SQLite conserve effectivement ici les deux transactions Photos du 17 octobre. Ce contrôle démontre la transportabilité du contenu SQL, **pas** une restauration iOS réelle. Une [expérience de migration publiée par son auteure](https://theforensicscooter.com/2024/02/04/device-setup-transferring-data-to-new-iphone-effects-to-photos-sqlite/) montre la conservation de lignes historiques de migration et l'ajout d'une ligne sur la destination, dans un essai iOS 15.1 vers 16.7.5. Elle empêche de traiter toute ancienne ligne comme une preuve exclusive du matériel courant ; elle ne valide pas le transfert des deux plist Wi-Fi sous 17.6.1.

L'absence de nouvelle ligne avec un autre UDID défavorise une migration inter-appareils classique **enregistrée par cette photothèque**. Elle ne réfute pas une restauration sur le même téléphone, une copie de fichiers, ni une lacune d'historique. La chaîne de sept observations positives est plus informative qu'une seule absence de marqueur de restauration.

## Couverture et conclusion

La recherche ciblée dans le manifeste ne trouve pas `.obliterated`, `data_ark`, CurrentPowerLog ou netusage ; les résultats flous ADDataStore/knowledgeC ne sont pas les journaux système recherchés. Le détail, y compris les faux positifs et répertoires, est conservé dans [targeted-manifest-coverage.json](targeted-manifest-coverage.json). Les préférences MobileBackup et Setup ne sont pas un journal append-only. Leur ancienneté maximale de conservation n'est pas établie ici.

**Conclusion justifiée :** continuité d'une lignée de photothèque historiquement rattachée au matériel TP-02 renforcée entre juin 2024 et 2025, encore présente en 2026 ; cohérence avec Santé et les versions système. Continuité ininterrompue de toute l'installation iOS jusqu'en 2026 non démontrée. Restauration de juin 2024 établie au niveau des enregistrements ; aucune restauration postérieure expliquant le 17 octobre identifiée. Ni l'absence d'un journal complet ni l'UUID d'une base ne permettent d'aller au-delà.
