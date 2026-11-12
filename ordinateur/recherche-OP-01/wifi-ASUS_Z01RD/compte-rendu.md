# OP-01 — Recherche du réseau Wi-Fi ASUS_Z01RD

Analyse du 14 octobre 2026, à la demande du prestataire.

**Complément sur la nature des traces :** la décompression des fragments identifie des données Wi-Fi structurées, très probablement des listes de réseaux disponibles. L’interprétation la mieux étayée est un réseau externe, éventuellement un partage de connexion d’un téléphone ASUS ZenFone 5Z. Aucun élément ne démontre une émission par OP-01. Voir [l’analyse détaillée de l’origine](origine/interpretation.md), qui précise les validations et limites de cette conclusion.

**Contrôle de datation :** la relecture des connexions WLAN, du registre réseau et des tables réseau SRUM ne fournit aucune connexion attribuable à ce nom ni aucune date de connexion. Voir [datation.md](datation.md).

## Constat

**Oui : cinq occurrences exactes de `ASUS_Z01RD` ont été retrouvées dans `pagefile.sys`, le fichier d’échange Windows d’OP-01.** Elles établissent la présence du nom dans ce fichier. Aucun profil Wi-Fi mémorisé ni événement de connexion à ce réseau n’est identifié dans les artefacts examinés. Ces fragments ne permettent pas de démontrer une connexion, de la dater ou d’attribuer le point d’accès à une personne.

## Source et préservation

Équipement : OP-01, ASUS UX333F, numéro de série documentaire `KAN0CV116290436`. Image examinée dans SIFT : `/media/shared/forensic/SADEDINE-2026/OP-01/OP01.E01`.

Montage effectué avec le script fourni [remonter_op01.sh](../../scripts/remonter_op01.sh), transféré dans SIFT sous `/home/sansforensics/remonter_op01-20261014.sh`. La clé de récupération a été lue dans `docs/codes-d-acces.md`. Le loop `/dev/loop14` est en lecture seule (RO=1), Dislocker est lancé avec `-r`, et NTFS est monté avec `ro,norecover`. Voir [mount-check.txt](mount-check.txt). Le partage contenant l’acquisition demeure accessible en écriture ; aucune écriture sur l’acquisition n’a été effectuée par les scripts de cette recherche. Pas de nouvelle vérification EWF intégrale effectuée ici.

L’alias `ssh sift` exige sur cet hôte `-F /home/chris/.ssh/config`, la configuration SSH système provoquant autrement une erreur de permissions.

## Recherches structurées

- **65 profils XML Wi-Fi**, dans `ProgramData/Microsoft/Wlansvc/Profiles` et `MigrationData/Profiles` : aucune correspondance. Le nom, le SSID hexadécimal et les paramètres de connexion ont été inventoriés ; les secrets Wi-Fi ne figurent pas dans l’inventaire. Voir [profiles.json](profiles.json).
- **Registre SOFTWARE**, branches `Microsoft\Windows NT\CurrentVersion\NetworkList` et `Microsoft\WlanSvc` : aucune correspondance dans les clés et valeurs décodées. Voir [registry-hits.json](registry-hits.json) et [registry.json](registry.json).
- **6 512 événements réseau**, lus avec `pyevtx`, sans erreur de lecture signalée : aucune occurrence dans les XML décodés. Voir [event-inventory.json](event-inventory.json), [events.json](events.json) et [errors.json](errors.json).

| Journal | Événements | Première date UTC conservée | Dernière date UTC conservée |
| --- | ---: | --- | --- |
| WLAN-AutoConfig / Operational | 1 325 | 28/03/2024 06:02:41 | 08/10/2026 10:36:32 |
| NetworkProfile / Operational | 2 216 | 27/06/2024 15:58:15 | 12/10/2026 06:49:51 |
| DHCP Client / Admin | 1 042 | 28/09/2023 17:05:42 | 02/10/2026 19:22:08 |
| DHCPv6 Client / Admin | 49 | 28/09/2023 17:05:42 | 27/07/2026 16:55:14 |
| NCSI / Operational | 1 880 | 28/09/2023 17:05:42 | 08/10/2026 10:36:32 |

Ces bornes décrivent les événements encore lisibles ; elles ne garantissent pas une couverture continue entre les deux dates. Les heures UTC sont données sans conversion à Paris dans ce tableau.

Les cinq fichiers EVTX sont copiés sous [raw](raw), avec empreintes SHA-256 dans [sources.json](sources.json). Les empreintes des copies locales concordent : [copy-verification.json](copy-verification.json).

## Recherche résiduelle et fichiers supprimés

Le script [residual.py](scripts/residual.py) recherche, sans distinction de casse, les octets ASCII et UTF-16LE de `ASUS_Z01RD`, ainsi que la représentation hexadécimale du SSID `415355535F5A30315244`. Il lit tous les EVTX présents dans `Windows/System32/winevt/Logs`, les fichiers de `Windows/System32/config`, de SRUM et de Wlansvc, les ruches utilisateur `NTUSER*` et `UsrClass*`, ainsi que `pagefile.sys`, `swapfile.sys` et `hiberfil.sys`. **1 534 fichiers totalisant 14 868 582 069 octets ont été lus, sans erreur : seul `pagefile.sys` présente des correspondances.** Voir [residual-inventory.json](residual-inventory.json) et [residual-hits.json](residual-hits.json).

Les cinq occurrences sont en ASCII et respectent exactement la casse demandée. Les offsets sont absolus dans `pagefile.sys`, en octets, à partir de zéro :

| Occurrence | Offset décimal | Texte retrouvé |
| --- | ---: | --- |
| 1 | 147 842 884 | ASUS_Z01RD |
| 2 | 331 615 117 | ASUS_Z01RD |
| 3 | 459 192 222 | ASUS_Z01RD |
| 4 | 549 269 230 | ASUS_Z01RD |
| 5 | 2 752 380 159 | ASUS_Z01RD |

Les fragments voisins contiennent notamment `realme GT Master Edition` et `Galaxy XCover6 Pro 06D`. Cela est compatible avec des noms de réseaux ou d’appareils présents dans une liste ; **le composant producteur et la nature précise de cette liste ne sont pas identifiés**. Le cinquième fragment contient aussi une chaîne incomplète `ASUS_Z01R`, non comptée parmi les cinq occurrences exactes. Plusieurs fragments peuvent être des copies du même contenu : cinq occurrences ne signifient pas cinq connexions ni cinq détections distinctes.

Des extraits de 1 042 octets autour de chaque occurrence sont conservés sous [contexts](contexts), avec leurs offsets, chaînes ASCII et SHA-256 dans [pagefile-contexts.json](pagefile-contexts.json). Les empreintes des cinq copies locales et la présence exacte du nom à chacun des offsets annoncés sont vérifiées dans [context-verification.json](context-verification.json). Aucun horodatage ni BSSID attribuable au nom ciblé n’est établi dans ces fragments.

SHA-256 de `pagefile.sys`, taille 5 637 144 576 octets : `20c7948d317d2d7a41bb9cc62dcbcc59aed9304ea92118d09f27eb9fe0f5f1e5`. La date de modification du fichier d’échange ne date pas individuellement ces contenus résiduels.

Une recherche complémentaire dans l’inventaire MFT des fichiers supprimés, produit lors de la campagne antérieure, n’identifie aucun chemin contenant `Wlansvc` ni le nom ciblé. Voir [deleted-mft-path-check.json](deleted-mft-path-check.json). Cette vérification repose sur cet inventaire préexistant, pas sur une nouvelle récupération des fichiers supprimés.

## Limites et conclusion

Les journaux WLAN conservés ne remontent pas à 2021/2022. Un profil supprimé, des événements écrasés ou un autre nom de réseau peuvent échapper à cette recherche. La recherche dans `hiberfil.sys` porte sur les octets du fichier, sans décompression de la mémoire hibernée. Aucun balayage intégral des secteurs non alloués, aucune reconstruction des clichés VSS ni récupération générale des anciennes ruches n’ont été réalisés pour cette demande.

**Les éléments examinés ne permettent donc ni de dater une connexion à `ASUS_Z01RD`, ni d’identifier son point d’accès ou son propriétaire.** Le nom d’un SSID, s’il était retrouvé, ne suffirait d’ailleurs pas à attribuer une connexion à une personne.

## Reproduction

Après le montage avec le script fourni, exécuter dans SIFT [collect.py](scripts/collect.py) avec Python 3 (`pyregf` et `pyevtx` déjà présents), puis [residual.py](scripts/residual.py) et [contexts.py](scripts/contexts.py) avec `sudo -n python3` pour les fichiers nécessitant les droits root. Les scripts écrivent dans `/home/sansforensics/analysis/OP-01/wifi-ASUS_Z01RD-20261014`. Pour une nouvelle campagne, changer ce répertoire afin de préserver les sorties. Le script de collecte référence `/dev/loop14` pour son contrôle final : adapter cette référence au loop effectivement obtenu lors du remontage.
