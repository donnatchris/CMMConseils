# TP-02 — Santé : intervalles, création et identité de source

## Conclusion nouvelle

**Les 73 lignes ne sont pas 73 observations d’activité physique ni 73 actions.** Elles comprennent 60 intervalles d’énergie de repos, dont 54 de 3 600 secondes exactement à la précision enregistrée. Le 17 octobre ne possède aucun début d’échantillon de pas ou de distance dans la sélection : ses 19 lignes sont 18 énergies de repos et une énergie active. Les créations d’objets apportent une corroboration temporelle technique du 17, sans rendre certaine l’attribution physique à TP-02.

Les résultats reproductibles sont dans `health-details.json`, `health-identity-crosschecks.json` et la chronologie. Les valeurs de quantité n’ont pas été interrogées ni exportées. Les bases `Health/healthdb.sqlite` (fileID `fa2e5ac3b7a62c8b7cb21e440c79eedd218550ea`) et `healthdb_secure.sqlite` (`516d7e19a4a0c9475c0015fae195626377b1b810`) ont leurs empreintes chiffrées/déchiffrées revérifiées. Lecture immutable ; aucun WAL compagnon référencé dans le manifeste pour ces deux bases.

## Types exacts et distribution

| Code samples.data_type | Type interprété | Total | 16/10 | 17/10 | 27/10 | 28/10 avant restitution, selon début |
|---|---|---:|---:|---:|---:|---:|
| 7 | HKQuantityTypeIdentifierStepCount — pas | 4 | 0 | 0 | 0 | 4 |
| 8 | HKQuantityTypeIdentifierDistanceWalkingRunning — distance marche/course | 4 | 0 | 0 | 0 | 4 |
| 9 | HKQuantityTypeIdentifierBasalEnergyBurned — énergie de repos | 60 | 7 | 18 | 12 | 23 |
| 10 | HKQuantityTypeIdentifierActiveEnergyBurned — énergie active | 5 | 0 | 1 | 0 | 4 |

Le codage privé numérique est recoupé avec les [requêtes iLEAPP](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/health.py) pour pas/distance et énergie repos/active, et le [lecteur de base HealthKit](https://github.com/ninyawee/healthkit-from-backup-to-sqlite/blob/main/healthkit_from_backup_to_sqlite.py) pour les quatre codes. Ce sont des correspondances de lecteurs de bases, pas une constante publique garantie par Apple pour toutes les versions.

Apple documente la production automatique de [pas](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/stepcount) et de [distance](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/distancewalkingrunning). Des types énergétiques peuvent également être collectés/calculés automatiquement selon la plateforme et la configuration ([source HealthKit](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/typestocollect)). Cette dernière documentation ne prouve pas le mécanisme précis d’iOS 17.6.1 dans ces lignes. Leur structure horaire et leur insertion groupée rendent plausible un calcul automatique, sans action sur Santé. Une estimation de repos n’atteste pas un mouvement du téléphone.

## Échantillonnage et insertion ne coïncident pas

Jointures vérifiées : `samples.data_id=objects.data_id`, `objects.provenance=data_provenances.ROWID`, puis `source_id` et `device_id` vers la base non sécurisée. Les 73 enregistrements, avec start/end/creation bruts, sont conservés séparément ; les conversions Cocoa peuvent arrondir à la microseconde, la valeur flottante brute fait référence.

**Lot du 17 :** objets 19582–19605, 24 intervalles horaires consécutifs d’énergie de repos, tous avec `creation_date=750870948.108443`, soit **17/10 17:15:48.108443 +02 / 15:15:48.108443Z**. Sept intervalles commencent le 16 et 17 le 17 ; compter leurs jours de début ne démontre donc pas 24 collectes aux heures représentées. Un traitement a enregistré ou conservé un lot couvrant les 24 heures précédentes.

Objet **19608**, énergie active : intervalle **17/10 17:15:27.424192–17:15:37.660830**, création **17:25:37.672403 +02** (`750871537.672403`). Cette création est à **9.958457 secondes avant** la génération Wi-Fi à 17:25:47.630860. Elle constitue un rapprochement entre traitements conservés ; l’intervalle représenté se termine environ dix minutes avant, pas pendant la connexion Wi-Fi.

Objet **19609**, énergie de repos : même début d’intervalle le 17 à 17:15:27, mais création conservée **28/10 11:57:22.733460 +01** (`751805842.73346`). C’est un contre-exemple direct à l’assimilation d’une ligne datée du 17 à une écriture le 17. L’écart dépasse dix jours ; sa cause (calcul différé, reprise ou autre chemin d’import) n’est pas prouvée.

**Lot du 28 :** objets 19610–19633, 24 intervalles horaires, création commune **12:01:56.572760 +01** (`751806116.57276`), avec débuts répartis sur le 27 et le 28. Six autres intervalles de repos partagent une création à **17:25:29.447636**. Ces lots expliquent une grande partie de la distribution horaire.

Les quatre couples pas/distance du 28 portent les mêmes intervalles de début/fin par couple :

| Début–fin Paris (+01) | Création pas / distance Paris (+01) |
|---|---|
| 12:01:32.839479–12:01:45.636046 | 12:14:06.270645 / .328949 |
| 15:11:20.920788–15:11:23.480246 | 15:22:23.679955 / .709420 |
| 17:24:02.269859–17:25:26.727090 | 17:35:29.136985 / .189960 |
| 17:39:47.807448–17:41:22.504158 | 17:55:55.676146 / .689275 |

Ils sont plus informatifs sur une collecte liée au mouvement que les estimations de repos. Ils peuvent résulter d’un transport de l’appareil sans déverrouillage. La coïncidence du premier avec la découverte Wi-Fi à 12:01:49 et du dernier avec les caches LSC/Xiaomi n’établit aucune causalité. L’échantillon d’énergie active de 19:18:05 se termine à 19:27:56, avec création à 19:28:15 : sa présence dans les 73 vient du filtre sur **start_date**, pas d’une fin et d’une insertion avant restitution.

## Attribution : un identifiant persistant supplémentaire retrouvé

Les 73 lignes ont la provenance 9 : produits origine/local iPhone14,4 ; builds origine/local `21G93` ; source 1 ; appareil 7 ; version 17.6.1 ; Europe/Paris ; `sync_provenance=0`, `sync_identity=2`, `derived_flags=0`. La source 1 est `local_device=1`. L’appareil 7 possède un UUID de 16 octets ; `localIdentifier` est vide. Les empreintes des UUID d’échantillons et de source permettent une comparaison sans publier les identifiants bruts.

**Nouveau :** `healthdb.sqlite.sync_identities.ROWID=2` porte un `hardware_identifier` non nul de 16 octets et un `database_identifier` distinct non nul. Le même `hardware_identifier` est présent **octet pour octet** sous `HomeDomain/Library/Preferences/com.apple.healthd.plist`, clé **`SyncIdentityHardwareIdentifier`**. Empreinte SHA-256 de ce plist : `6d1a0ea881562f94262c033110fa75f8536142c208f752caee310546abae19be`. Les **59 951 échantillons** conservés, tous modèles origine/local iPhone14,4, partagent l’identité 2 ; l’autre identité, 1, contient des identifiants nuls. La recherche dans 2 790 plist extraits retrouve cette représentation uniquement dans healthd.

Cela lie les données à l’identité Santé déclarée de l’installation sauvegardée et renforce leur cohérence locale au-delà du modèle. **Cela ne lie pas encore cet identifiant au numéro de série de TP-02 en octobre 2024.** Le nom hardware_identifier ne démontre ni un dérivé matériel infalsifiable ni son invariance lors d’une restauration. Aucun identifiant de MigrationHistory Photos ne correspond dans les représentations UUID testées. Il ne faut pas considérer les UUID de lignes, de source et de matériel comme interchangeables.

Aucune métadonnée associée aux 73 objets n’est présente via `metadata_values`/`metadata_keys` ; on ne peut donc ni confirmer ni rejeter une saisie manuelle par un marqueur `WasUserEntered`. Les drapeaux de provenance ne sont pas une chaîne de garde de l’appareil. Apple documente le [transfert des données Santé par restauration chiffrée](https://support.apple.com/en-in/120001) : la contre-hypothèse reste techniquement possible, sans restauration de TP-02 démontrée ici.

## Ce que Santé corrobore

**Vérifié :** activité de traitement représentée dans la base le 17 à 17:15:48 et 17:25:37, identité Santé commune au reste de la base et à healthd ; proximité avec les états Wi-Fi/Photos. **Probable :** production automatique plutôt qu’une saisie de ces 73 lignes. **Possible :** transport d’un état historique par restauration ; provenance d’un autre exemplaire de même modèle dont l’installation aurait été migrée. **Inconnu :** liaison physique de l’identité Santé à TP-02 à cette date, état de verrouillage, identité d’un opérateur.

La meilleure suite est la comparaison de `SyncIdentityHardwareIdentifier`, `sync_identities`, sources/devices et UUID d’échantillons entre sauvegardes historiques et TP-01/TP-03. Une identité identique sur deux acquisitions devra être interprétée à l’aide de leur historique de migration ; elle ne prouvera pas à elle seule une collecte simultanée sur deux appareils.
