# Méthode, couverture et reproduction

Campagne du 14 octobre 2026, ciblée sur la continuité de l'installation et les hypothèses H1–H5. Elle réutilise les extractions antérieures et leurs traces ; elle ne refait pas un inventaire général de sauvegarde. Le rapport existant est `telephones/analyse-TP-02.md` ; le nom `analyse-telephone.md` cité dans la demande n'est pas présent dans cet espace. Les rapports antérieurs restent des antécédents, pas des constats nouveaux de cette campagne.

## Sources et contrôle d'intégrité

Sauvegarde chiffrée originale : `/mnt/data/forensic/SADEDINE-2026/TP-02/00008110-001C69A002BA801E/`. Manifeste déchiffré utilisé pour les recherches ciblées : `/mnt/data/forensic/SADEDINE-2026/ANALYSES/TP-02/Manifest-decrypted.db`. Extractions réutilisées : `telephones/recherche-TP-02/extraction-*-20261014/files/` avec leurs `extraction.jsonl`.

Les 31 sources principales comportent28 fichiers déjà extraits et 3 en-têtes de sauvegarde. Pour les fichiers issus d'extraction, le SHA-256 courant est comparé au journal ; l'objet chiffré correspondant est relu et haché. Tous concordent ; les sources principales sont rehachées à la fin et inchangées. Les en-têtes, sans référence d'extraction, sont hachés avant/après sans prétendre à une validation par acquisition indépendante. [source-verification.json](source-verification.json) donne chemins, fileID, empreintes chiffrées/déchiffrées et résultats. Les fichiers OP-01 complémentaires sont hachés avant/après dans leur JSON propre.

| Source Wi-Fi | Domaine / chemin relatif | fileID | SHA-256 déchiffré |
|---|---|---|---|
| Réseaux connus | SystemPreferencesDomain / com.apple.wifi.known-networks.plist | 0fa75546343ba224c9fe55adc73e8fdedc1029c3 | d32e9c13df0276375a6301cbae85b6e452c6e67081f78e39b23db37015318f82 |
| MAC privées | SystemPreferencesDomain / SystemConfiguration/com.apple.wifi-private-mac-networks.plist | e36b35ae4cc6038f9ce83b5e097f216144278b17 | 3d066811eea6285c3a70002743082d3b07d228df1b3d685588749b7db9c36454 |

Aucune extraction supplémentaire ni demande de mot de passe n'a été nécessaire. Le trousseau n'a fait l'objet que d'un examen de sa structure externe. Les sources sont ouvertes en lecture binaire ou en SQLite `mode=ro&immutable=1` via le module existant ; aucun checkpoint, réparation ou ouverture en écriture. Le test de copie SQLite a pour seule destination `:memory:` et ne modifie pas le fichier source. Les copies extraites sont celles déjà utilisées, sans WAL présent à fusionner par ces scripts ; le périmètre n'est donc pas une récupération de transactions effacées ou non extraites.

## Scripts et lancement

- [tp02_wifi17_investigation.py](../../scripts/tp02_wifi17_investigation.py) : métadonnées sélectionnées de restauration/setup, comparaison 36 réseaux, dates bplist natives, journal PLJ, lignée Photos/Santé, historiques TipKit et AddressBook, balayage borné de dates structurées, contrôles d'intégrité.
- [tp02_wifi17_crosschecks.py](../../scripts/tp02_wifi17_crosschecks.py) : propriétés Wi-Fi évolutives, entrée CommCenter, comparaison littérale d'identifiants et contrôles structurels OP-01, ajout du timestamp CommCenter à la chronologie.
- Dépendance locale préexistante : [tp02_forensic.py](../../scripts/tp02_forensic.py), bibliothèque standard Python ; aucun paquet installé pour ces contrôles.

Depuis la racine du projet, vers un dossier **nouveau** :

```sh
python3 telephones/scripts/tp02_wifi17_investigation.py --out /tmp/tp02-wifi17-nouvelle-execution
python3 telephones/scripts/tp02_wifi17_crosschecks.py --out /tmp/tp02-wifi17-nouvelle-execution
```

Le premier script refuse un dossier préexistant ; le second doit être exécuté une seule fois après lui et refuse d'écraser ses JSON. Il ne faut pas relancer ces commandes sur le dossier probatoire livré. Les journaux operations.json et crosscheck-operations.json identifient date d'exécution et SHA-256 du script correspondant. Le second enrichit le CSV de 97à98 lignes ; ce n'est pas une divergence entre les deux journaux.

Le décodage des offsets des dates utilise l'implémentation interne de `plistlib` de la version Python indiquée dans verification-livrables.json. L'isolation des plists du journal repose sur leurs trailers et sur une validation par le décodeur standard ; le conteneur externe PLJ n'a pas été intégralement rétro-ingéniéré.

## Couverture réelle, sans prétention d'exhaustivité

Le balayage de données déjà extraites a sélectionné3 326 fichiers structurés de 32 Mio maximum ;2 996ont été parsés,330ont produit des erreurs de format, recensées par fileID et classe d'erreur.5 392 plists imbriqués ont été lus. Le critère de signature peut sélectionner des fichiers nonJSON ; une erreur de parsing n'est pas une preuve de corruption. Les gros fichiers, les blobs nonstructurés, les valeurs temporelles non reconnues, les chaînes de date et les journaux absents ne sont pas couverts intégralement. Voir [structured-date-scan-coverage.json](structured-date-scan-coverage.json).

La recherche d'identifiants suit huit valeurs sélectionnées sur 3 886 fichiers de 32 Mio maximum, hors trousseau ; Photos.sqlite, plus gros, est interrogé séparément. Une absence de correspondance littérale n'exclut pas un encodage différent. La recherche du manifeste porte des termes précis liés aux boots/restaurations/configurations ; les faux positifs ne sont pas considérés comme sources système.

Les 289 candidats SQL antérieurs portant le 17 ont été réutilisés et dédupliqués dans [previous-sqlite-candidates-17.json](previous-sqlite-candidates-17.json). Ils comprennent notamment 170 valeurs Photos ZLASTVIEWEDDATE entre 02:23 et 10:10 Paris, des métadonnées d'actif 19:23, un appel 10:28 et des dates CloudDocs nocturnes présentes côté client/serveur. Ces valeurs déjà extraites ne sont pas promues en nouveaux événements de manipulation. Leur provenance locale ne peut être inférée de leur seul nom. Les 58 candidats SQL du créneau 16:45–18:00 relèvent des groupes Photos, Santé, TipKit et AddressBook déjà examinés ici ; aucun groupe SQL supplémentaire du créneau n'a été laissé sous une interprétation nouvelle non vérifiée. L'objet Santé 19609, dont l'intervalle commence le 17 mais la création date du 28, reste le contre-exemple documenté dans l'analyse antérieure ; il n'est pas recompté comme création du 17.

La chronologie [activite-17octobre.csv](activite-17octobre.csv) rassemble 98 **propriétés/commits contrôlés dans cette campagne**, dont 64 dans16:45–18:00 ; les bornes des intervalles Santé et les dates de création y sont distinguées. Elle n'est pas un relevé de gestes humains ni une liste exhaustive de toutes les valeurs temporelles candidates de la journée. Une propriété peut être copiée ; les colonnes `requirements_at_source` et `TP02_attribution` explicitent cette limite. Les autres candidats restent accessibles dans le JSON précédent pour éviter une fusion silencieuse de mesures, métadonnées synchronisables et commits locaux.

Les données sauvegardées reflètent plusieurs états et dates : Info.Last Backup Date12octobre2026, Manifest.Date18 septembre, Status.Date18 septembre. Ces valeurs conservées dans identifier-comparisons.json ne sont pas une horloge 2024 ni la preuve d'une acquisition atomique de tous les contenus.

## Temps, minimisation et résultats négatifs

Dates plist binaires : doubles Cocoa depuis 2001-01-01 UTC, avec hexadécimal et offset d'objet dans wifi-binary-date-validation.json. SQLite : valeurs natives et format explicite ; CommCenter : secondes Unix ; EVTX : FILETIME Windows, tronqué à la microseconde pour la couverture. Europe/Paris via zoneinfo, UTC+2 le 17 octobre etUTC+1 le 28. Les réglages timed actuels (`TMAutomaticTimeOnlyEnabled=true`, fuseau automatique=false) ne prouvent pas l'état de l'horloge 2024. [Apple documente l'époque de référence Date](https://developer.apple.com/documentation/foundation/date/timeintervalsincereferencedate-swift.property?changes=_9).

Les sorties ne publient ni mots de passe, tokens, numéros de téléphone, contenu de communication, valeurs médicales ni MAC/BSSID. Les SSID tiers et identités persistantes sont hachés/aliasés ; le SSID cible est conservé comme demandé. Les données brutes restent dans les sources déjà protégées ; leur copie intégrale dans Git n'est pas nécessaire à la reproductibilité. Une absence de trace n'est interprétée qu'au regard de la couverture explicitée.

Les références externes sont liées au passage qu'elles soutiennent. Les limites de version des tests publiés sont explicites ; aucun document de synchronisation générique n'est présenté comme validation du transfert d'une clé privée précise. Les demandes externes non réalisées et le protocole témoin figurent dans les études ; aucun accès à un compte personnel n'est autorisé implicitement par la présente analyse.

## Vérification finale effectuée

Une seconde exécution des deux scripts, dans `/tmp/tp02-wifi17-reproduction-20261014`, reproduit les **22 fichiers de résultats** : CSV identiques octet pour octet, JSON identiques après exclusion de la seule heure d’exécution des journaux. Le contrôle [tp02_wifi17_verify.py](../../scripts/tp02_wifi17_verify.py) vérifie ces comparaisons, les liens locaux, les comptes de lignes et l’égalité des instants UTC/Paris. Il examine aussi les 13 fichiers de configuration de profils déjà extraits : aucune occurrence littérale ASUS_Z01RD dans les encodages testés, empreintes conformes ; des profils effacés ou non sauvegardés ne sont pas couverts. Le résultat et la version Python figurent dans [verification-livrables.json](verification-livrables.json).

Commande de vérification vers un fichier de résultat nouveau (ne pas écraser le résultat livré) :

```sh
python3 telephones/scripts/tp02_wifi17_verify.py --out DOSSIER_RESULTATS_A_VERIFIER --reproduction DOSSIER_SECONDE_EXECUTION
```

Les empreintes de tous les livrables et des trois scripts sont listées dans `SHA256SUMS.txt` ; ce relevé contrôle leur stabilité ultérieure, pas leur existence en 2024.
