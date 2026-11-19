# Méthode, opérations et références

## Périmètre réellement exécuté

Lecture intégrale du rapport disponible `telephones/analyse-TP-02.md`, des scripts existants et du cadrage client (`docs/mail.txt`, attestation de remise, compétence cmm-attentes-cliente). La référence demandée `analyse-telephone.md` est absente. Les **107 fichiers de résultats CSV/JSON/JSONL préexistants** ont été parcourus et décodés par le script ; leurs empreintes, structures, colonnes, nombres de lignes et statuts sont dans `prior-results-review.json`. Les anciennes passes ne sont pas additionnées aux finales. Cela ne constitue pas un nouveau scan général de la sauvegarde : seuls les artefacts de la demande ont été réinterrogés.

Les opérations nouvelles sont dans deux scripts :

```sh
python3 telephones/scripts/tp02_activity_oct2024.py --out /tmp/TP02-activite-reproduction
python3 telephones/scripts/tp02_activity_correlations.py --out /tmp/TP02-activite-reproduction
```

La première destination doit être nouvelle. La seconde commande ajoute ses fichiers nouveaux et complète la chronologie ; elle ne doit être exécutée qu’une fois dans ce dossier. Aucun mot de passe n’est nécessaire. Les résultats de cette campagne sont dans `telephones/recherche-TP-02/approfondissement-activite-202410/`, déjà couvert par l’exclusion Git de recherche-TP-02. Les scripts sont dans `telephones/scripts/`. Les permissions des résultats sont restrictives (umask 077).

Lectures SQLite avec `mode=ro&immutable=1` ; pas de checkpoint, VACUUM, récupération ou rejeu WAL sur les sources. Le manifeste a été interrogé uniquement sur les compagnons des bases ciblées, sans réinventaire. L’absence de compagnons référencés est consignée. Les empreintes des 13 premières cibles chiffrées/déchiffrées ont été revérifiées ; les quatre pièces complémentaires (healthd, deux Books, CommCenter) ont le même contrôle dans `additional-source-verification.json`. Photos et les 13 premières cibles ont aussi un contrôle avant/après. Les empreintes ne prouvent pas l’intégrité historique avant la première acquisition.

Les identifiants réseau sont comparés en mémoire et remplacés par des alias. **Correction de méthode pendant la campagne :** les BSSID doivent être normalisés comme six octets, car la notation privée omet un zéro de tête ; le résultat final est une égalité, pas le faux désaccord d’une comparaison textuelle initiale. Une première exécution a également rencontré l’absence de colonne UTC dans le CSV MBFile précédent ; UTC est désormais reconstruit depuis la valeur Unix brute. Les sorties intermédiaires propres à cette campagne ont été écartées du dossier final ; les anciennes pièces n’ont pas été modifiées.

Les requêtes Santé n’interrogent jamais les colonnes de quantité. Les contenus/coordonnées de messages et appels ne sont pas exportés. Le test des identifiants de clavier utilise seulement des hash en mémoire ; aucune correspondance n’a été trouvée et aucune dérivation Apple n’est présumée validée. La métadonnée binaire LSC reste non décodée.

## Temps, confiance et limites

Paris via zoneinfo Europe/Paris ; UTC+02 avant le changement du 27/10, UTC+01 le 28. Le CSV préserve valeurs brutes et UTC. Plist : valeur décodée depuis les octets d’origine hachés, pas dump de l’octet double. Santé/Photos/appels : secondes Apple depuis 2001 ; les flottants peuvent arrondir l’affichage à la microseconde. SMS : entiers nanosecondes, affichage tronqué à la microseconde. MBFile : secondes Unix, empreinte de provenance du manifeste distincte de celle d’un contenu extrait. Une date SETTIME n’est pas une touche ; une transaction n’est pas un geste ; un intervalle Santé ne date pas son écriture.

Les horaires déclarés sont inclus séparément. L’horloge de 2024 n’est pas calibrée par cette campagne. Aucune acquisition physique, connexion distante, accès cloud ou extraction volumineuse nouvelle. Le test OP-01 porte seulement sur 193 exports textuels ≤64 Mio, avec leur empreinte ; aucun EVTX binaire ni hive n’a été nouvellement parsé. Le scan de corroboration réseau dans les extractions exclut les fichiers >32 Mio et les encodages inconnus. Il ne démontre pas une absence dans l’ensemble de l’image.

Les termes **vérifié** concernent lecture/jointure/égalité d’octets ; **probable** désigne une interprétation soutenue mais non exclusive ; **possible** une voie technique non prouvée dans ce dossier ; **inconnu** une variable non disponible. Les interprétations de code privé Apple ne sont pas garanties par le seul libellé d’un champ. Une restauration de base complète peut transporter des historiques locaux ; une synchronisation d’objets ne doit pas être présumée transporter toutes les tables de transactions.

## Recherche technique consultée le 14/10/2026

Les liens sont placés auprès des conclusions dans les rapports. Références primaires utilisées :

- [iLEAPP appleWifiPlist.py](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/appleWifiPlist.py) et [mac_apt airport_preferences.py](https://github.com/ydkhatri/mac_apt/blob/master/plugins/airport_preferences.py) : parseurs des structures, pas implémentation de leur producteur Apple.
- [Apple Secure keychain syncing](https://support.apple.com/en-au/guide/security/sec0a319b35f/web), [adresses privées](https://support.apple.com/en-ie/102509), [sauvegardes chiffrées](https://support.apple.com/en-ie/108353) : mécanismes possibles, sans activation historique présumée.
- [ASUS ZS620KL/ZS621KL](https://dlcdnets.asus.com/pub/ASUS/ZenFone/ZS620KL/SK13920_ZS620KL_2SIM_EM_WEB.pdf) : correspondance du code modèle, pas identification du point d’accès.
- [iLEAPP health.py](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/health.py), [lecteur HealthKit](https://github.com/ninyawee/healthkit-from-backup-to-sqlite/blob/main/healthkit_from_backup_to_sqlite.py) ; API Apple [stepCount](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/stepcount), [distanceWalkingRunning](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/distancewalkingrunning), [typesToCollect](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/typestocollect) ; [restauration chiffrée](https://support.apple.com/en-in/120001).
- [Apple Messages et sécurité](https://support.apple.com/en-ca/guide/personal-safety/-ipsdccb7919d/web), [Messages in iCloud](https://support.apple.com/en-ie/guide/security-pdf/sec2c21e7f49/1/web/1), [Photos iCloud](https://support.apple.com/en-us/108782).
- [Apple NSPersistentHistoryTransaction](https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction), [change type](https://developer.apple.com/documentation/coredata/nspersistenthistorychangetype?language=objc) : contexte et changements, sans preuve tactile.
- [Apple Phone & FaceTime](https://support.apple.com/en-gb/guide/icloud/mmfbf206de44/1.0/icloud/1.0), [persistance des appels déjà synchronisés](https://support.apple.com/en-euro/guide/personal-safety/ipsc169ffeb0/web).
- [iphone_backup_decrypt amont](https://github.com/jsharkey13/iphone_backup_decrypt/blob/master/src/iphone_backup_decrypt/iphone_backup.py), code local 0.11.2 haché ; [SQLite WAL](https://www.sqlite.org/wal.html), [Backup API](https://www.sqlite.org/backup.html), [VACUUM](https://www.sqlite.org/lang_vacuum.html).

Recherches ciblées `JoinedByUserAt`, `MacGenerationTimeStamp`, restauration/migration et sources Apple publiques : **aucune branche d’écriture iOS 17.6.1 validée** n’a été trouvée. Les résultats secondaires/forum n’ont pas été utilisés pour transformer un nom de champ en preuve d’action. Les documentations actuelles soutiennent des possibilités générales ; elles ne remplacent pas une expérience sur la version historique. La nature IPC du panneau repose sur son code extrait, pas sur une supposition de catalogue Tuya ; aucune API de préchargement moderne n’a été invoquée comme preuve du comportement de LSC 2024.

## Validation finale

Une seconde exécution dans `/tmp/TP02-activite-reproduction-published` retrouve les mêmes résultats : **18 fichiers de données comparés, dont la chronologie de 663 lignes**, identiques (égalité structurée JSON, octets identiques pour CSV). Les journaux d’opérations horodatés sont exclus de cette comparaison. Les SHA-256 des versions publiées des scripts figurent dans `verification-new-campaign.json` ; les journaux initiaux conservent ceux des versions exécutées avant les ajustements de présentation/masquage et l’ajout explicite d’UTC aux dates annexes.

Les 17 cibles ont des empreintes chiffrées et déchiffrées conformes aux journaux d’extraction. Les 663 couples UTC/Paris, les valeurs brutes et les empreintes de provenance ont été contrôlés ; les identifiants réseau et la clé de rotation connus sont absents des nouvelles sorties. Le vérificateur est reproductible :

```sh
python3 telephones/scripts/tp02_activity_verify.py \
  --out telephones/recherche-TP-02/approfondissement-activite-202410 \
  --reproduction /tmp/TP02-activite-reproduction-published
```

Cette reproduction utilise les mêmes sources et ne remplace pas une acquisition indépendante. Les SHA-256 des livrables sont dans `SHA256SUMS`.
