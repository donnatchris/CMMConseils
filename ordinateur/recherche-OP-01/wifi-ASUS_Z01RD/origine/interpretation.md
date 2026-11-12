# OP-01 — Nature des occurrences ASUS_Z01RD

Complément du 14 octobre 2026.

**L’explication la mieux étayée est un SSID de réseau Wi-Fi externe présent dans des listes de réseaux disponibles. Rien dans les éléments contrôlés n’établit qu’OP-01 émettait ce réseau. Un partage de connexion d’un téléphone ASUS ZenFone 5Z est une hypothèse plausible, mais le matériel émetteur n’est pas identifié.**

## Ce que la reconstruction apporte

Les cinq occurrences initiales étaient contenues dans des blocs compressés, et non dans cinq chaînes isolées en mémoire non compressée. Une recherche bornée de débuts de flux Plain XPRESS dans les contextes élargis permet de reconstruire cinq pages de 4 096 octets. Le script de décodage [carve_xpress.py](../scripts/carve_xpress.py) suit la variante Plain LZ77 décrite par [Microsoft MS-XCA](https://learn.microsoft.com/openspecs/windows_protocols/ms-xca).

| Occurrence brute dans pagefile.sys | Début du flux reconstruit | Octets compressés consommés | Offset ASUS dans la page décompressée |
| ---: | ---: | ---: | ---: |
| 147 842 884 | 147 842 848 | 187 | 636 |
| 331 615 117 | 331 614 992 | 284 | 1 228 |
| 459 192 222 | 459 192 208 | 161 | 460 |
| 549 269 230 | 549 269 216 | 161 | 460 |
| 2 752 380 159 | 2 752 380 080 | 265 | 1 196 et 4 004 |

Les trois flux des lignes 1, 2 et 5 sont également décompressés avec succès (`returncode=0`) par la bibliothèque indépendante `libMSCompression.so` déjà installée dans SIFT ; les 4 096 octets produits sont identiques par SHA-256 au décodeur Python. Pour les lignes 3 et 4, la bibliothèque produit les mêmes 4 096 octets mais renvoie une erreur de validation du flux (`-3`) : ces deux reconstructions sont secondaires, et ne sont pas nécessaires à l’interprétation principale. Voir [independent-decompression.json](independent-decompression.json), [decoder-comparison.json](decoder-comparison.json) et [xpress-candidates.json](xpress-candidates.json).

Les pages des lignes 3 et 4 sont identiques. La page de la ligne 5 contient deux occurrences complètes après décompression : la seconde était partiellement représentée dans les octets compressés. **Le nombre d’occurrences brutes ne mesure donc ni un nombre de connexions, ni un nombre de scans.** Les offsets des pages décompressées ne sont pas des offsets physiques de l’acquisition.

## Identification du contenu

Le nom est précédé du DWORD little-endian `10`, puis stocké dans un champ de 32 octets, complété par des zéros. Cette représentation correspond précisément au couple longueur/SSID de [DOT11_SSID](https://learn.microsoft.com/en-us/windows/win32/nativewifi/dot11-ssid). Les entrées voisines portent `realme GT Master Edition` et, après décompression complète, `Galaxy XCover6 Pro 06DD`. Les trois noms se répètent à un pas de **688 octets** dans les premières listes reconstituées.

Après le champ SSID, on observe des DWORD cohérents avec des informations WLAN : type de réseau, paramètres physiques, qualité de signal, sécurité et algorithmes. Pour ASUS, les DWORD à SSID+92 valent **86, 90, 82, 82 et 84** ; ceux à SSID+96/+100/+104 valent **1/7/4**. Ils sont compatibles avec une qualité de signal variable, une sécurité activée, une authentification RSNA-PSK et un chiffrement AES-CCMP. Les valeurs 7 et 4 correspondent aux constantes Microsoft [DOT11_AUTH_ALGORITHM](https://learn.microsoft.com/en-us/windows/win32/nativewifi/dot11-auth-algorithm) et [DOT11_CIPHER_ALGORITHM](https://learn.microsoft.com/en-us/windows/win32/nativewifi/dot11-cipher-algorithm).

**La structure complète n’est toutefois pas exactement celle du `WLAN_AVAILABLE_NETWORK` public.** Un DWORD supplémentaire décale les champs par rapport à sa définition publiée ; la variante interne ou sérialisée précise n’est pas identifiée. La comparaison avec [WLAN_AVAILABLE_NETWORK](https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_available_network), qui décrit les réseaux disponibles et leurs paramètres, soutient fortement l’interprétation comme liste Wi-Fi. Elle ne justifie pas d’appliquer aveuglément ses offsets pour annoncer un état « connecté » ou « profil présent ». Aucun processus producteur n’a été attribué à ces pages.

Ainsi, ce ne sont pas simplement des noms de téléphones trouvés dans un document : **leur organisation binaire est celle d’informations de réseaux Wi-Fi**. Leur présence parmi plusieurs SSID avec des paramètres de signal est un indice fort de réseaux vus par la partie cliente Wi-Fi du PC. Le constat est plus précis que la première extraction de chaînes, sans constituer un enregistrement horodaté de capture radio.

## Le nom correspond-il au PC ou à un téléphone ?

[ASUS associe officiellement la référence Z01RD au ZenFone 5Z](https://www.asus.com/in/support/faq/1014441/), modèles commerciaux ZS620KL/ZS621KL. OP-01 est un ordinateur UX333F : il s’agit de deux références distinctes. Un téléphone peut émettre un point d’accès Wi-Fi avec un nom de ce type ; **le seul SSID ne certifie pas la marque ou le modèle de l’émetteur**, car il peut être choisi ou modifié.

Contrôles sur le registre acquis, conservés dans [registry-origin.json](registry-origin.json) :

- Nom Windows d’OP-01 : `LAPTOP-RMCOB2VU`, dans `SYSTEM\ControlSet001\Control\ComputerName\ComputerName`.
- Réseau hébergé classique : `SYSTEM\ControlSet001\Services\WlanSvc\Parameters\HostedNetworkSettings`. La valeur binaire `HostedNetworkSettings` contient le nom de profil `HOSTED_NETWORK_PROFILE`, un champ SSID de longueur 11 et le texte **`DEFAULTSSID`**. La valeur `EverUsed` vaut **0**. Aucun `ASUS_Z01RD` ne figure dans ces données.
- Les branches `SOFTWARE\Microsoft\WcmSvc\Tethering`, `Tethering\Devices` et `TetheringManager` examinées ne fournissent aucune configuration au nom `ASUS_Z01RD`.
- Les données contrôlées de `WlanSvc`, `SharedAccess`, `icssvc` et des appareils Bluetooth ne fournissent pas de rapprochement positif avec ce nom.

Ces états acquis corroborent l’absence de preuve d’un réseau ASUS_Z01RD émis par OP-01. **Le réseau hébergé classique et le point d’accès mobile moderne sont des mécanismes différents ; `EverUsed=0` dans la branche classique ne prouve pas à lui seul qu’aucun partage moderne n’a jamais fonctionné.** Microsoft décrit le point d’accès mobile Windows comme une fonction avec un SSID configurable : [NetworkOperatorTetheringAccessPointConfiguration](https://learn.microsoft.com/en-us/uwp/api/windows.networking.networkoperators.networkoperatortetheringaccesspointconfiguration).

## Réponse et limites

- **Nature des occurrences :** fragments de données Wi-Fi structurées, très probablement des listes de réseaux disponibles gardées dans la mémoire compressée puis le fichier d’échange.
- **Réseau externe :** interprétation fortement soutenue par les listes et les paramètres associés ; le partage de connexion d’un téléphone ASUS ZenFone 5Z est plausible.
- **Wi-Fi émis par OP-01 :** aucune preuve positive ; les paramètres du réseau hébergé retrouvés portent un autre nom.
- **Connexion d’OP-01 au réseau :** non démontrée. Une visibilité dans une liste n’est pas une connexion.
- **Date, lieu, adresse MAC/BSSID et propriétaire :** non établis. Le fichier d’échange ne fournit pas l’horodatage de ces pages ni leur processus d’origine. Il n’est pas possible de rattacher ces fragments à la perquisition du 15/10/2024 ou à l’ouverture du 28/10/2024.

Les contextes élargis bruts et leurs empreintes sont décrits dans [wide-contexts.json](wide-contexts.json). Ils correspondent à 69 632 octets autour de chacune des cinq occurrences, lus sur le montage protégé dans SIFT. Les pages décompressées et les fichiers bruts sont conservés dans ce même dossier. Aucune modification de l’acquisition ou de la configuration Windows n’a été effectuée.
