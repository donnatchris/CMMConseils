# OP-01 — Peut-on dater une connexion à ASUS_Z01RD ?

Contrôle complémentaire du 14 octobre 2026 sur l’image montée en lecture seule dans SIFT.

**Aucune date de connexion à `ASUS_Z01RD` n’est établie avec les artefacts actuellement examinés. La connexion elle-même reste non démontrée : les fragments mémoire indiquent très probablement un réseau visible, ce qui ne signifie pas que l’ordinateur l’a rejoint.**

## Contrôles complémentaires

Le script [check_dates.py](scripts/check_dates.py) a relu les sources présentes dans l’image, sans utiliser les seules conclusions des campagnes antérieures. Les empreintes des sources et les résultats sont sous [datation](datation).

- **Journal WLAN-AutoConfig :** 1 325 événements conservés, du 28/03/2024 au 08/10/2026 en UTC. Parmi eux figurent **57 événements 8001** de connexion réussie, du 15/04/2024 au 02/10/2026 ; aucune occurrence de `ASUS_Z01RD`, `ASUS_Z01R` ou `Z01RD` dans l’ensemble du journal. Microsoft identifie l’événement 8001 comme une connexion Wi-Fi réussie dans son [guide d’administration](https://download.microsoft.com/download/56d34d76-4db1-48fd-b51e-1c8235736a4b/Administrative%20Guide.pdf). Les bornes de conservation ne garantissent pas un historique continu ou complet.
- **Registre réseau SOFTWARE :** aucune correspondance dans `Microsoft\WlanSvc` et `Microsoft\Windows NT\CurrentVersion\NetworkList`. Aucun profil nommé ne permet donc de rattacher une date de première ou dernière connexion à ce SSID. La recherche des profils XML réalisée précédemment était également négative.
- **SRUM :** lecture des **682 enregistrements de trafic réseau** et des **15 enregistrements de connectivité réseau**. Les dates `TimeStamp` conservées dans ces deux tables vont du **03/09/2026 au 08/10/2026 en UTC**. Les enregistrements comportent des identifiants `L2ProfileId` et la table de connectivité possède `ConnectStartTime`, mais aucun rapprochement avec un profil nommé `ASUS_Z01RD` n’est établi. La recherche complémentaire dans les 25 834 entrées de `SruDbIdMapTable` ne trouve pas le nom ciblé. L’absence de ce nom dans cette table n’est pas, à elle seule, une preuve d’absence de connexion. Les tables et champs sont décrits dans la [documentation du projet libyal](https://github.com/libyal/esedb-kb/blob/main/documentation/System%20Resource%20Usage%20Monitor%20%28SRUM%29.asciidoc).
- **Erreurs de lecture signalées par cette passe :** aucune.

Les dates des autres tables SRUM, notamment celles relatives à l’énergie et pouvant remonter à 2021, ne datent pas une connexion à ce réseau. Aucune date `TimeStamp` d’une ligne non attribuée n’est présentée comme une date ASUS_Z01RD.

## Pourquoi pagefile.sys ne donne pas la date recherchée

Les blocs reconstruits ne contiennent pas d’horodatage de connexion attribuable à ASUS_Z01RD. La position d’un fragment dans le fichier d’échange ne correspond pas à une date. La date de modification globale du fichier d’échange ne date pas chaque page qu’il contient. Les variations des valeurs compatibles avec la qualité du signal ne fournissent pas davantage une chronologie.

L’analyse ne permet donc ni d’affirmer « connexion le 15/10/2024 », ni de rattacher la trace au 28/10/2024, ni d’annoncer une connexion en octobre 2026 sur la seule base des dates du fichier d’échange.

## Ce qui pourrait changer ce résultat

Une connexion pourrait être datée si l’on retrouvait un ancien événement Wi-Fi, un ancien profil réseau avec ses métadonnées ou un enregistrement de connectivité relié de façon fiable à ce SSID. Une archive antérieure ou un cliché VSS lisible pourrait conserver ces éléments. Les investigations précédentes ont cependant rencontré une erreur de structure VSS ; aucun ancien cliché monté n’est disponible dans cette campagne. Une nouvelle tentative de récupération historique est une piste, sans garantie de retrouver une trace et sans garantie que le PC ait effectivement rejoint ce réseau.

**Conclusion : présence probable parmi les réseaux détectés ; connexion et date non établies.**
