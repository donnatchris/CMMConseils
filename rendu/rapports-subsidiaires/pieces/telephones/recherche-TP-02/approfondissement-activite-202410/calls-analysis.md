# TP-02 — origine des 53 appels

## Résultat

**Aucun des 53 appels centraux ne peut être attribué de façon discriminante à l’exemplaire TP-02 avec les champs conservés.** L’analyse complète du schéma et des distributions apporte une raison précise : la base enregistre le contenu logique des appels mais ne conserve pas, pour ces lignes, de relation vers un appareil d’origine ni de date d’importation.

Pièce : `HomeDomain/Library/CallHistoryDB/CallHistory.storedata`, fileID `5a4935c78a5255723f707230a451d79c540d2741`, SHA-256 `d9f9b69b847164cc03081b275d6b2189a1eda2148695bddcfe178e4985079b0c`. Empreintes source chiffrée et déchiffrée revérifiées ; pas de WAL/SHM/journal compagnon référencé au manifeste. `calls-details.json` contient toutes les distributions non nominatives, le schéma et les lignes techniques ; les coordonnées et contenus ne sont pas exportés.

## Ce que les nouveaux champs établissent

| Propriété | Résultat des 53 lignes | Limite |
|---|---|---|
| `ZSERVICE_PROVIDER` | com.apple.Telephony, 53 | Service téléphonique, pas numéro de série |
| `ZCALLTYPE`, `ZCALL_CATEGORY`, `ZHANDLE_TYPE` | 1, 1 et 2 pour toutes | Codes conservés ; ne distinguent pas une copie synchronisée |
| `ZORIGINATED` | 22 à 1, 31 à 0 | Direction logique, sans appareil initiateur identifié |
| `ZANSWERED` | 15 à 1, 38 à 0 | État conservé, pas 15 réponses prouvées sur TP-02 |
| `ZREAD`, `ZVERIFICATIONSTATUS` | 1 et 4 pour toutes | Ni lecture au premier plan ni origine matérielle garanties |
| `Z_OPT` | 1 pour toutes | Compteur Core Data, pas « jamais synchronisé » |
| `ZUNIQUE_ID` | 53 présents, 53 distincts | Identifiants d’appels comparables entre acquisitions ; pas identifiants d’appareil |
| `ZCONVERSATIONID`, `ZPARTICIPANTGROUPUUID` | NULL pour toutes | Aucun groupe/liaison exploitable |
| `ZLOCALPARTICIPANTUUID`, `ZOUTGOINGLOCALPARTICIPANTUUID`, `ZINITIATOR` | NULL pour toutes | Aucune clé permettant une attribution matérielle de ces appels |
| `ZDISCONNECTED_CAUSE`, plusieurs champs d’extension/urgence | NULL pour toutes | Pas de cause réseau ou de provenance déductible |

Les 53 timestamps ZDATE, Z_PK et directions sont dans la chronologie ; leur séquence du 15 au 26 ne forme pas un journal de radio locale. Les durées sont présentes dans le résultat technique, sans interlocuteurs. Les tables ordinaires du schéma sont `ZCALLRECORD`, `ZCALLDBPROPERTIES`, `Z_METADATA` et `Z_PRIMARYKEY` ; pas de table de dispositifs ou de provenance par ligne ni de date de création/import/synchronisation exploitable.

La comparaison de toute la base montre **657/821** lignes de 2024 et **840/841** de 2025 avec un localparticipant UUID non nul. `ZINITIATOR` est toujours nul pour 2024 mais présent dans 423 lignes de 2025. Cela confirme que le parseur sait lire des champs renseignés ailleurs ; leur absence centrale est réelle. Ces contrastes peuvent refléter plusieurs générations de schéma, producteurs ou chemins d’import ; ils ne démontrent pas à eux seuls la synchronisation des 53 lignes. Un participant UUID, même présent, nécessiterait encore une sémantique et une liaison matérielle vérifiées.

## Pourquoi les trois scénarios restent compatibles

1. **Appel local :** TP-02 peut produire un enregistrement Telephony avec date, durée, direction et état. Aucun champ central ne l’interdit.
2. **Historique synchronisé :** le même enregistrement logique peut être distribué par le compte Apple. Apple documente la [synchronisation Téléphone/FaceTime, y compris pour iOS 16–17](https://support.apple.com/en-gb/guide/icloud/mmfbf206de44/1.0/icloud/1.0). Aucun champ central ne désigne le téléphone ayant porté la session radio.
3. **Restauration :** une base contenant ces lignes peut être restaurée ultérieurement. Les [sauvegardes chiffrées peuvent contenir l’historique d’appels](https://support.apple.com/en-ie/108353). ZDATE date l’appel représenté, pas son arrivée dans cette copie de base.

Désactiver actuellement la synchronisation ne résoudrait pas l’origine historique : Apple précise que [les appels précédemment synchronisés restent dans l’historique](https://support.apple.com/en-euro/guide/personal-safety/ipsc169ffeb0/web). Aucun changement de réglage n’a été effectué.

**Démonstration de la limite :** les trois scénarios produisent les mêmes valeurs observables retenues ; la base ne fournit pas la variable discriminante « appareil ayant émis/reçu localement », ni la date d’arrivée du record. Une direction sortante, une date pendant rétention et com.apple.Telephony ne suffisent donc pas à choisir. Ni la proximité avec Santé ni celle avec Wi-Fi n’ajoutent cette variable absente.

## Suites utiles

Comparer `ZUNIQUE_ID` entre anciennes sauvegardes et TP-01/TP-03 peut démontrer la duplication d’un même record, sans nécessairement désigner son producteur initial. Un futur export comparatif devra pseudonymiser les IDs, sans publier les numéros. Les relevés opérateur devraient inclure si disponibles **IMEI/IMSI et cellule de session**, obtenus dans le cadre approprié : un relevé ne comportant que la ligne et l’heure ne suffit pas à distinguer deux appareils successifs utilisant cette ligne. Les journaux téléphonie/CommCenter contemporains et l’historique de restauration seraient également discriminants ; leur présence n’est pas établie dans l’acquisition disponible.
