# TP-02 — précision des horodatages et nature des trois SMS

Contrôle du 9 novembre 2026, sur l’extraction existante. Les heures ci-dessous sont celles de Paris le 28 octobre 2024 (UTC+01).

| ROWID | Date du message (`date`) | `date_read` | Délai | Nature indiquée par le corps |
|---|---|---|---|---|
| 74688 | 12:03:14,750877 | 12:03:18,794336 | 4,043459072 s | Code de réinitialisation de mot de passe Microsoft |
| 74689 | 12:10:04,455465 | 12:10:06,276798 | 1,821332992 s | Code de validation Google |
| 74690 | 12:46:03,902439 | 12:46:06,075801 | 2,173361152 s | Code de validation Google |

Les trois lignes portent `is_from_me=0`, `service=SMS` et `is_read=1`, vérifiés lors de la contre-lecture précédente. Les trois `date_read` sont distincts et suivent de quelques secondes les dates des messages. Ils ne constituent donc pas un unique horodatage commun. Une copie ou une restauration pourrait toutefois conserver ces dates distinctes ; leur espacement ne prouve pas trois lectures sur le téléphone examiné.

## Contenu et méthode

La colonne `text` est NULL. Les trois corps `attributedBody` sont des archives `streamtyped` contenant une chaîne UTF-8 de 73, 75 et 75 octets, à l’offset 122. L’extraction ciblée contrôle le marqueur de chaîne, sa longueur, le délimiteur final et la phrase complète attendue. Il ne s’agit pas d’un décodage général des attributs. Les codes ne sont pas reproduits dans les résultats ou les rapports.

Le premier corps indique une réinitialisation de mot de passe Microsoft ; les deux autres indiquent une validation Google. Aucun des trois corps n’est un message de code Apple. Cela ne prouve pas l’absence d’un autre SMS Apple ailleurs. Les trois lignes ont une référence d’expéditeur résolue dans `handle`, mais l’identité réelle de l’émetteur n’est pas authentifiée. Les marques sont celles mentionnées dans le texte. Ni l’utilisation des codes, ni la réussite d’une connexion ou d’une réinitialisation, ni leur demandeur ne sont établis.

Le [script](scripts/verifier.py) s’exécute depuis la racine avec `python3 investigations/20261109-sms-lecture/scripts/verifier.py`. Il interroge SQLite en lecture seule (`mode=ro&immutable=1`), le WAL étant vide. Les empreintes avant/après de la base et de ses compagnons sont identiques ; les empreintes de chaque corps et les offsets sont conservés dans le [résultat](resultats/verification.json). Les dates sont calculées en arithmétique entière depuis l’époque Apple, avec troncature à la microseconde.

## Synchronisation, restauration et proximité temporelle

Les trois valeurs `ck_sync_state=1` sont conservées brutes : elles ne datent pas une synchronisation et n’identifient pas l’appareil ayant produit le marquage. Ce contrôle n’établit aucune session iCloud contemporaine des trois dates, ni aucune restauration expliquant spécifiquement ces lignes. Ces mécanismes restent des hypothèses, sans preuve positive apportée ici.

Le filtrage de la chronologie corrélée existante à ±60 secondes de chaque `date_read` retrouve, hors SMS, une date de préférence de clavier à **12:03:18,492020**, soit 302,316 ms avant le premier `date_read`, et une date Wi-Fi de localisation à **12:03:27,445469**. Le test antérieur de 12 956 candidats SHA-1 n’a pas relié le contexte clavier à ces messages ; ce test ne valide pas la dérivation Apple. Aucune de ces deux traces ne prouve une lecture ni une saisie du code. Aucun autre événement non SMS n’apparaît dans cette fenêtre de la chronologie pour les deux autres messages. Ce résultat limité ne démontre pas une absence d’activité : aucun nouveau dépouillement exhaustif des journaux n’a été réalisé.

**Conclusion : trois SMS entrants comportent des horodatages `date_read` du 28 octobre ; leur consultation locale sur TP-02 n’est pas établie. Ces valeurs ne permettent pas, à elles seules, d’identifier l’appareil à l’origine du marquage comme lu.** Le contenu précise la nature des messages, sans résoudre cette attribution.

Le 28 octobre correspond à la journée d’ouverture des scellés. Le rapport final distingue les heures du PV (ouverture des scellés téléphoniques à 11 h 30) des traces techniques ; ces SMS de midi ne doivent pas être décrits comme antérieurs à cette ouverture.
