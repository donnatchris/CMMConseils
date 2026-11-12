# Identification des caméras — sondage des caches LSC

**9 novembre 2026 — examen local de dérivés déjà extraits de TP-02.**

## Résultat

**Aucun modèle exact ni firmware des caméras associées à SD-01, SD-02 et SD-03 n'a pu être identifié par cette passe.** Les caches `Documents/home/detailv1` et `Documents/home/list313` restent non décodés. Ce résultat ne signifie pas que ces informations sont absentes de leur contenu.

Les fichiers sources sont conservés intacts. Les 104 fichiers lus par le script sont vérifiés contre leurs SHA-256 dans le journal d'extraction du 14 octobre 2026, puis contrôlés de nouveau après analyse : toutes les empreintes concordent. Il s'agit d'une vérification des dérivés analysés, pas d'une nouvelle acquisition du téléphone ni d'un contrôle intégral de sa sauvegarde.

## Sources et opérations

Sources : `telephones/recherche-TP-02/extraction-cameras-20261014/files/AppDomain-com.lscsmartconnection.smart/`, journal `extraction.jsonl` de cette même extraction, et [identifications antérieures](../20261017-recroisements/resultats/recoupements-v2/cameras-identites.json).

Script : [probe_lsc.py](scripts/probe_lsc.py). Sorties : [résultats](resultats/resultats.json) et [empreintes des sources](resultats/sources.json). Les clés candidates, jetons et contenus privés ne sont pas exportés. Aucun accès au compte, à une caméra en fonctionnement ou au cloud n'est effectué ; les recherches documentaires externes ne transmettent pas les données extraites.

| Cache | Taille | Entropie mesurée, bits/octet | Lecture directe JSON/plist | Flux zlib/gzip complet retrouvé |
| --- | ---: | ---: | --- | --- |
| `home/detailv1` | 186 272 octets | 7,99897 | Non | Aucun |
| `home/list313` | 1 120 octets | 7,81056 | Non | Aucun |

Les tailles sont multiples de 16. L'entropie élevée et cet alignement sont compatibles avec un chiffrement, mais ne permettent pas d'identifier un algorithme ni d'exclure un format comprimé ou propriétaire.

Les sondages comprennent :

- une tentative de lecture JSON/plist et un repérage de flux zlib/gzip complets à l'intérieur des deux caches, sous un plafond de décompression de 8 Mo ;
- la recherche de champs d'identité dans les préférences et ressources locales JSON/plist ou base64 décodables, et la collecte en mémoire de candidats depuis ces objets et les chaînes lisibles MMKV ;
- des hypothèses AES limitées, sans protocole propriétaire validé : 16 004 clés candidates issues de 5 205 éléments locaux, par utilisation directe des tailles compatibles, MD5 binaire/hexadécimal ou SHA-256 ; modes ECB et CBC avec IV nul, préfixe de clé ou bloc précédent ; décalages de début 0, 16, 32, 48 et 64 octets ;
- **304 076 sondages AES par cache**, sans décodage structuré validé. Un préfixe ressemblant à un format n'est pas considéré comme un succès : le résultat complet doit pouvoir être analysé comme objet JSON/plist, directement ou après décompression.

Ces essais ne constituent pas une recherche exhaustive des clés, modes, IV, formats, fonctions de dérivation ou encodages possibles. L'absence de résultat ne prouve ni l'absence de clé dans la sauvegarde ni l'impossibilité d'un décodage ultérieur. Les candidats et leurs dérivations sont des hypothèses exploratoires, pas une identification du mécanisme de LSC.

## Ressources décodées et pièges d'interprétation

Les **54 fichiers `Documents/panel/*.json` de ressources de produit** sont décodables en **base64 puis JSON**. Ils contiennent tous des dictionnaires de traduction `en`, `fr`, `zh` :

| Référence dans le nom de fichier | Nombre de fichiers |
| --- | ---: |
| `5egzavnxtqsczrho` | 17 |
| `jrtivcmjvidhxq2u` | 17 |
| `k56etquy1kdmbtvl` | 19 |
| `ixar3nxaes57uv6n` | 1 |

Ces références sont des pistes de ressources de produit/panneau. Leur présence ne permet pas de rattacher une référence commerciale à une caméra physique ni à une carte SD. Les textes sur les versions, réinitialisations et mises à jour décrivent des commandes d'interface : ils ne constituent ni une version installée ni la preuve d'une commande exécutée.

Les versions `1.1.5` à `1.2.0` figurant dans les noms APM concernent l'application LSC ; les versions de panneaux ou mini-applications ne sont pas des firmwares de caméra.

Les résultats antérieurs Xiaomi Home comportent `mxiang.camera.mwc10` et `mxiang.camera.mwc11`, avec champs `ZEXTFWVERSION` vides. Aucune correspondance avec les trois cartes SD n'est établie par cette passe.

## Ce qui permettrait de poursuivre

La piste technique suivante serait d'obtenir légalement le binaire de la version LSC correspondant à la sauvegarde et ses bibliothèques natives, afin d'identifier la routine de stockage de `home/detailv1` et `home/list313`, le format et la dérivation de clé. Ce binaire n'a pas été identifié dans les fichiers locaux examinés ; les ressources JavaScript et traductions ne le remplacent pas. Il faudrait ensuite valider le décodeur sur des données témoins, avant de conclure sur les données du dossier.

Pour identifier les appareils sans attendre ce travail : relever l'étiquette physique et les informations d'appareil/mise à jour dans l'application, avec un rapprochement explicite chambre/terrasse/salon et carte SD. Une version relevée actuellement ne prouverait pas le firmware installé en 2024 ; il faudrait une trace historique datée ou un historique de mises à jour.

## Reproduction

Depuis la racine du projet, avec Python 3 et `cryptography`, exécuter vers un **nouveau répertoire** :

```sh
python3 investigations/20261109-identification-cameras/scripts/probe_lsc.py --out /tmp/cmm-lsc-reproduction
```

Les sorties doivent présenter les mêmes empreintes, compteurs et résultats. Le script refuse de remplacer une destination existante et arrête l'analyse en cas de désaccord avec une empreinte d'extraction.
