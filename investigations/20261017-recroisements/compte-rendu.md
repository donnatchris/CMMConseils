# Complément d’investigation et réponse aux demandes de la cliente

**Mission SADEDINE-2026 — 17 octobre 2026.** Compte rendu technique de travail, à lire avec les rapports individuels. Périmètre : Freebox, OP-01, TP-02 et SD-01/02/03. TP-01 et TP-03 sont exclus de cette campagne à la demande de l’utilisateur, car indisponibles. Le PV et le journal d’acquisition de la sauvegarde Mac sont également déclarés indisponibles ; leurs contenus ne sont ni supposés ni reconstitués.

## 1. Réponse générale

Les rapports répondent largement aux demandes d’analyse de [docs/mail.txt](../../docs/mail.txt), dans la limite des traces conservées. Le complément apporte des identifications d’équipements, un candidat pour l’origine de deux échecs SMB anciens, une recherche plus complète des manipulations des cartes sous Windows et des contrôles supplémentaires des applications caméra et des archives du 28 octobre.

**Aucune nouvelle preuve d’accès distant non autorisé, d’identité d’un intervenant ou de réinitialisation volontaire des caméras n’est établie.** Cela ne permet pas de conclure à l’absence historique d’accès : les données sont tardives, partielles et parfois importables entre appareils. L’incertitude n’est pas levée par la seule répétition des recherches.

**La conservation demandée n’est pas entièrement satisfaite : l’inventaire cloud contrôlé est incomplet.** La copie sur le disque neuf et la durée prévue au devis ne sont pas attestées par les éléments examinés. Ce point doit être traité avant de présenter la mission comme intégralement achevée.

### Couverture des demandes du mail

| Demande | État après ce complément |
|---|---|
| Freebox et historique depuis 2021/2022 | Inventaire et traces conservées examinés ; aucun historique exhaustif de sessions depuis 2021/2022 n’est disponible dans les exports analysés. |
| Accès réseau/caméras avant et autour du 15 octobre | Recoupements approfondis ; équipements mieux identifiés, mais pas de session distante non autorisée démontrée ni d’auteur identifié. |
| Opérations du 15 au 28 octobre | Chronologie consolidée ; distinction maintenue entre dates techniques et déclarations. Le PV absent empêche la confrontation documentaire. |
| SD : réinitialisations, suppressions et anomalies | Analyses individuelles et transversales disponibles ; défauts précis identifiés, cause intentionnelle et poste Windows non établis. |
| Deux supports de conservation | **Non attesté comme achevé** : lacunes chiffrées dans le cloud contrôlé et copie sur disque client non justifiée. |
| Modalités de paiement | Demande 30 % / 70 % conservée comme telle ; acceptation du prestataire non démontrée par l’analyse technique. |

## 2. Nouveaux recoupements réseau et appareils

| Élément | Constat vérifié | Portée et limite |
|---|---|---|
| `LAPTOP-RMCOB2VU`, MAC `50:E0:85:63:41:5B` | La MAC de l’interface Intel d’OP-01 dans les événements WLAN du 15/10/2024 correspond exactement à celle de la Freebox. | Cet appareil doit désormais être classé comme **OP-01 identifié**, plutôt qu’inconnu. Le rapprochement n’identifie pas son utilisateur. |
| MAC `E0:A2:5A:0A:A3:F7` | Correspondance exacte entre l’entrée Freebox et une configuration Xiaomi Home conservée dans TP-02, modèle `mxiang.camera.mwc11`. Première activité Freebox : 19/07/2024 à 21:02:47 Paris. | L’entrée auparavant non identifiée est rattachable à cette configuration de caméra. Pas de preuve de session distante, de numéro physique ou de carte SD associée. |
| Modèle `mxiang.camera.mwc10` | Xiaomi Home conserve `E0:A2:5A:0D:06:DE`, IP `192.168.1.135`. La Freebox conserve `…:DF`, même IP et nom comportant `miap06DE`. | Rapprochement plausible, **pas une égalité de MAC**. Ne pas fusionner les deux interfaces sans preuve complémentaire. |
| TP-02 et iPhone Freebox | Deux correspondances exactes de MAC parmi les 36 entrées privées Wi-Fi conservées. `0E:41:84:EF:66:27` présente aussi une cohérence de dates le 11/06/2024 : ajout à 14:27:28,692, première activité Freebox à 14:27:30. | Cohérence locale utile, sans étalonnage global. L’autre correspondance, `08:87:C7:76:C4:10`, associe une entrée du téléphone de 2025 à une activité Freebox de 2024 : les préférences actuelles ne sont pas un historique exhaustif. |
| iPhone nocturnes d’octobre | `EA:21:6C:F7:47:E7`, `9C:64:8B:0A:BD:0C` et `FE:AA:76:95:AC:29` ne correspondent pas aux MAC privées conservées de TP-02. | Ils restent non attribués. Rotation des adresses, restauration et perte de traces empêchent d’exclure TP-02 sur cette seule absence. |
| `DESKTOP-ICPNCMD`, `AC:ED:5C:DA:47:74` | Première activité Freebox le 16/10/2024 à 21:27:48 Paris ; pas de rattachement positif à OP-01/TP-02 dans les recherches ciblées. | Identité et opérateur restent inconnus. Un nom d’hôte ne prouve pas une origine administrative. |

Sources : [identité OP-01](resultats/recoupements-v2/op01-freebox-identite.json), [caméras](resultats/recoupements-v2/cameras-identites.json), [Wi-Fi TP-02](resultats/recoupements-v2/tp02-freebox-wifi.json), [événements bruts reparsés](resultats/evtx/), [contrôle indépendant](resultats/verification.json).

### Les deux échecs SMB du 26 mars 2024

Les événements SMBServer 551 à **15:20:36 et 15:21:12 Paris** portent le statut d’échec `0xC000006D`. Le décodage indépendant de l’adresse binaire confirme **192.168.1.139**. L’inventaire Freebox associe cette IP à **LAPTOP-205Q5H9C**, MAC **F8:28:19:77:42:71**, avec dernière activité IPv4 le même jour à **15:48:20**.

C’est un **candidat étayé par l’IP et la proximité temporelle**, pas une attribution certaine : aucun historique de bail couvrant exactement les deux tentatives ne garantit que cette IP appartenait alors à cet appareil. Les événements sont des échecs ; ils ne prouvent ni accès réussi ni intrusion. [Résultat détaillé](resultats/recoupements-v2/smb-26mars2024.json).

## 3. Caméras et limites des historiques

Le décodage structurel des catalogues LSC conservés a livré **18 références de médias pour deux identifiants d’appareils**, réparties sur douze fichiers de catalogue. **Aucune référence n’est datée du 15 au 28 octobre 2024.** Il s’agit de références de médias, pas d’un journal exhaustif de visionnage ou d’accès distant. Le contenu des médias référencés n’a pas été nouvellement extrait ni examiné dans cette campagne.

Cinq archives de couvertures ont également été examinées. Leurs dates et leurs données ne fournissent pas de session historique attribuable autour de la perquisition. Les cinq fichiers APM restent opaques : les sondages de signatures et de décompression n’ont pas livré de flux complet interprétable. Leur extension `.db` ne suffit pas à les traiter comme des bases SQLite. Leurs noms de versions et dates de compilation ne datent pas une action de l’utilisateur.

**Les configurations Xiaomi permettent d’identifier des équipements ; les données LSC conservées ne permettent pas de reconstituer qui a regardé les caméras, depuis où et à quelle heure en octobre 2024.** La trace de cache de panneau du 28 octobre déjà décrite dans le rapport TP-02 ne devient pas une preuve de consultation vidéo. [Résultats et empreintes](resultats/cameras/).

L’étape supplémentaire utile nécessiterait soit des historiques de compte réellement conservés par le fournisseur, soit la documentation du format APM correspondant à la version iOS, soit des caméras de référence pour reproduire les artefacts. Aucun compte n’a été connecté ni fournisseur contacté dans cette campagne. La disponibilité d’archives de 2024 n’est pas présumée.

## 4. Cartes SD : recherche du poste Windows du 12 novembre

Les précédents rapports établissent la présence de fichiers auxiliaires Windows datés du 12/11/2024 sur les trois cartes. Le complément recherche leur rattachement à OP-01 : dix journaux SetupAPI, le journal System, neuf journaux PnP/stockage, les ruches SYSTEM/SOFTWARE et les NTUSER.DAT accessibles ont été examinés.

La recherche des identifiants de volume `386d4397` et `6546a41d`, du lecteur `121220160204`, du volume Kingston `140b8328` et des identifiants réseau ciblés n’a pas produit de correspondance dans les ruches complètes parcourues. Aucun événement du 11 au 13 novembre n’est sélectionné dans les neuf journaux de stockage disponibles ; aucune clé parcourue n’a de dernière écriture au 12 novembre. **Le poste ayant traité les cartes n’est donc pas identifié.**

Ces résultats négatifs n’excluent pas OP-01 : SetupAPI ne journalise pas toutes les insertions, les journaux sont circulaires et la dernière écriture d’une clé remplace les dates antérieures. La recherche des numéros est textuelle ou sur une valeur entière de quatre octets ; ce n’est pas un décodage universel des structures binaires du registre. `Default` et `Default User` sont parcourus séparément ; leurs comptes ne représentent pas nécessairement deux profils indépendants.

Les conclusions [transversales SD](../../cartes_sd/analyse-cartes_sd-transversale.md) restent valables : onze vidéos présentent une même erreur de compteur audio associée aux dates FAT de 2000 ; ce défaut existe avant le 15 octobre. Une cause logicielle commune est fortement plausible, mais ni une réinitialisation volontaire ni une coupure précise n’est démontrée. L’année du « février » mentionné dans le mail reste non spécifiée ; février 2024 est le périmètre de comparaison choisi dans les travaux antérieurs.

Sources : [recoupement SD/SetupAPI](resultats/recoupements-v2/sd-windows-12novembre.json), [recherche complète SIFT](resultats/sift/resultats/).

## 5. OP-01 : approfondissements après redémarrage de SIFT

Les opérations ont utilisé le volume Windows monté **en lecture seule**, avec contrôle d’empreintes des sources consommées. Le parcours du registre couvre 451 874 clés et 832 924 valeurs (avec les deux chemins du profil par défaut), et celui du stockage 5 914 événements dans neuf journaux. Les recherches registre, stockage et messagerie se terminent sans erreur de parseur signalée et avec des empreintes avant/après identiques.

La recherche MIME décodée des **5 875 messages** des deux PST a retrouvé deux invitations à une connexion distante **Sage Assistance**, datées des **4 juillet et 14 novembre 2022**, dont l’expéditeur déclaré utilise le domaine `LogMeInRescue.com`. Leur texte invite à démarrer une session de support ; l’authenticité de l’expéditeur n’est pas certifiée par ce seul champ. Elle n’a pas retrouvé le fragment exact du nom du PDF de phishing détecté en mai 2024. Une occurrence de téléassistance dans un courrier ne prouve pas qu’une session s’est établie ; elle ne relie pas à elle seule ce courrier au raccourci de 2023. Le résultat négatif sur le nom exact du PDF ne couvre pas un renommage, toutes les pièces jointes compressées ou une messagerie disparue. [Résultats](resultats/sift/resultats/messageries-cibles.json).

Le contrôle complet de décompression de **GDRIVE (2).zip** révèle **92 fichiers lisibles sur 93**, avec une erreur sur `GDRIVE/ALMU 2023 ZIP.zip`. Le contrôle répété de **GDRIVE.zip** retrouve les trois erreurs déjà décrites, donc 90 fichiers lisibles sur 93. Les **89 fichiers lisibles dans les deux archives ont des SHA-256 identiques**. Les erreurs concernent des membres différents : leurs contenus lisibles sont complémentaires. Le contrôle supplémentaire des **93 fichiers distincts** couverts par ces membres confirme leur identité SHA-256 avec les fichiers du dossier `L16B/GDRIVE`, dont les empreintes restent inchangées. Les contenus sont donc disponibles dans le corpus malgré les défauts des conteneurs ZIP. Voir la [comparaison au dossier](resultats/sift/zip/comparaison-dossier.json). Cela n’identifie ni le moment ni la cause des corruptions et ne prouve pas une falsification. [Contrôles détaillés](resultats/sift/zip/results.json).

### Décodage complet du journal NTFS

Le fichier `$LogFile` de **67 108 864 octets** a été décodé avec dfir_ntfs 1.1.20, en utilisant la MFT pour la résolution des chemins. Le traitement se termine avec un code de retour nul et livre **388 732 enregistrements de journal NTFS**, en plus des structures de reprise. Les [compteurs détaillés](resultats/sift/ntfs/metrics.json) distinguent ces enregistrements des transactions et des structures USN. Les empreintes avant/après du journal et de la MFT concordent. Le décodage complet, conservé dans SIFT, mesure **341 997 834 octets** ; son SHA-256 figure dans le [résumé](resultats/sift/ntfs/summary.json).

Les **31 063 structures USN** interprétées portent exclusivement des dates du **08/10/2026 (16 840)** et du **12/10/2026 (14 223)**. Ce nombre compte les structures décodées, pas nécessairement autant d’événements indépendants. Des dates de fichiers embarquées sont plus anciennes, notamment en 2024 : elles ne datent pas les transactions qui les contiennent.

Les **sept correspondances ciblées** concernent des raccourcis `Recent` : L16B, trois GDRIVE, Inventaire_saddedine, Rejets_saddedine et Archive_saddedine. Les données redo/undo concernées indiquent des mises à jour de dates d’accès du **8 octobre 2026 vers 10:36:36–10:36:37 UTC**, soit **12:36:36–12:36:37 Paris**. Elles ne prouvent ni ouverture humaine des documents, ni nouvelle exportation, ni modification de leur contenu. Les chemins sont résolus à partir de la MFT conservée ; une réutilisation de numéro d’entrée reste une limite du décodage.

**Ce journal n’apporte donc pas de nouvelle transaction datée d’octobre 2024 permettant de reconstruire les exports recherchés.** Il complète la recherche littérale antérieure, sans démontrer que les opérations anciennes n’ont jamais eu lieu. Aucune correspondance LogMeIn Rescue ou du nom exact du PDF de phishing n’est retrouvée dans ce décodage. [Transactions ciblées](resultats/sift/ntfs/target-blocks.txt), [empreintes des sources](resultats/sift/ntfs/sources.json).

## 6. Chronologie commune et portée des rapprochements

Heures de Paris, avec changement UTC+2 vers UTC+1 le 27 octobre. Les dates applicatives sont rapportées comme telles ; les horloges n’ont pas été étalonnées globalement.

| Date | Éléments rapprochés | Conclusion permise |
|---|---|---|
| 15/10/2024 | OP-01 : Wi-Fi vers 10:43, mise en veille prolongée vers 10:53. Perte d’accès aux téléphones déclarée vers 13:30. SD-03 : vidéo nominale 13:28 présentant les défauts déjà étudiés. | Les traces concernent des systèmes et horloges différents. La vidéo ne date pas à elle seule une intervention ; 13:30 n’est pas l’heure établie du début de perquisition. |
| 16/10 | Première activité du DESKTOP à 21:27:48 ; champ de réveil Windows auparavant étudié. | Le champ Windows est une échéance programmée, pas un réveil réel prouvé. Pas de lien positif entre le DESKTOP et OP-01. |
| 17/10 | TP-02 : traitements internes vers 17:15–17:18 puis propriétés d’association `ASUS_Z01RD` vers 17:25. | Séquence informative, mais provenance physique et éventuelles restaurations restent à distinguer. Pas de session Windows contemporaine démontrée sur OP-01. |
| 28/10 | Ouverture déclarée vers 10:22 ; reprise OP-01 vers 10:41 ; exports L16B ; références Kingston vers 17:26–17:27 ; cache de panneau LSC vers 17:39 ; restitution déclarée vers 19:20. | Plusieurs opérations sont documentées après l’ouverture déclarée. Le PV manque pour les confronter à des actes consignés et identifier leur cadre. |
| 12/11 | Fichiers auxiliaires Windows sur les trois SD, vers 23:35–23:51 selon les métadonnées étudiées. | Traitement Windows compatible ; poste et auteur non établis. |

Les 53 appels et les traitements Photos conservés dans TP-02 ne sont pas réattribués au téléphone physique par ces nouveaux recoupements. Les limites détaillées du [rapport TP-02](../../telephones/analyse-TP-02.md) demeurent.

## 7. Conservation : écart concret à traiter

L’inventaire en lecture seule du bucket `sadedine-2026` comporte **76 objets finalisés**, soit **154 083 440 668 octets**. La comparaison des clés et tailles avec les acquisitions locales donne :

| Acquisition | Fichiers locaux | Objets correspondants de même taille | Absents du bucket contrôlé | Octets absents |
|---|---:|---:|---:|---:|
| OP-01 | 75 | 54 | 21 | 45 074 723 943 |
| SD-01 | 3 | 3 | 0 | 0 |
| SD-02 | 16 | 16 | 0 | 0 |
| SD-03 | 13 | 3 | 10 | 17 324 869 116 |
| TP-02 | 137 848 | 0 | 137 848 | 102 822 949 109 |

Il manque donc **165 222 542 168 octets, soit environ 165,22 Go**, pour ces acquisitions dans le bucket inventorié. Cette conclusion ne porte pas sur un éventuel autre stockage non inventorié. Les extractions et résultats d’analyse ne sont pas couverts par cette seule comparaison des acquisitions : la demande de conserver « l’ensemble des données extraites » exige également leur inventaire.

Douze transferts multipart non finalisés sont visibles ; ils ne constituent pas des objets complets utilisables. Aucune reprise, suppression ou annulation de transfert n’a été effectuée. Le versionnement est activé, mais aucune règle de cycle de vie n’est configurée : cela ne fixe pas la durée contractuelle et ne constitue pas une garantie d’immutabilité.

Sur un échantillon de **quatre segments E01**, la reconstruction locale de l’ETag multipart concorde avec l’ETag distant. Ce contrôle n’est **pas une relecture SHA-256 intégrale du cloud**, et une égalité de taille n’est pas une preuve d’identité de contenu. [Inventaire](resultats/cloud/), [comparaison et échantillon](resultats/conservation/resume-conservation.json).

Pour clôturer ce volet : terminer les copies manquantes en conservant les originaux ; inventorier aussi les dérivés ; vérifier les empreintes des deux destinations ; identifier le disque neuf et établir un bordereau de copie/remise ; documenter la durée selon le devis. Aucune copie sur disque client ni durée chiffrée ne peut être attestée ici.

## 8. Ce qui reste réellement approfondissable

| Suite | Apport attendu | Condition et état |
|---|---|---|
| Historiques de comptes caméra/cloud | Sessions, exports et éventuelles adresses d’origine | Historiques disponibles et accès approprié ; non collectés. Aucun accès de 2024 garanti. |
| Identification physique caméras/SD | Relier modèles, interfaces MAC et cartes | Caméras, étiquettes et versions de firmware non disponibles dans ce travail. |
| Essai contrôlé sur matériel de référence | Tester le défaut commun FAT/MP4 et les dates par défaut | Protocole préparé dans le guide ; non exécuté. Ne jamais tester sur les cartes originales. |
| Supports Kingston ou image de destination | Vérifier l’archive et relier numéro de volume à matériel | Supports de destination non disponibles ; les Jump Lists seules ne livrent pas leur contenu. |
| Conservation sur deux supports | Satisfaire la demande de sécurité des données | Complétude cloud et copie sur disque à achever/attester. |
| PV et journal Mac | Lever certaines limites documentaires et de provenance | Déclarés indisponibles ; pas de nouvelle demande dans cette campagne. |

Cette campagne ne constitue pas un examen exhaustif de tout l’espace non alloué : aucun carving intégral supplémentaire, aucune restauration de cliché VSS illisible et aucun décodage du format APM propriétaire n’ont été menés à terme ici. Une recherche plus large reste techniquement envisageable, mais sans cible ni garantie de conservation d’artefacts de 2024 ; elle ne remplace pas les pièces externes manquantes.

Les modalités 30 % / 70 % sont une demande du mail, pas une acceptation contractuelle démontrée. L’attestation prévoit une restitution au plus tard le 06/11/2026 ; elle ne prouve pas la remise du disque de conservation.

**Bilan : les pistes exploitables avec les sources accessibles ont été approfondies et les conclusions mieux circonscrites. Les principales limites restantes portent sur des historiques externes, les appareils de référence, la provenance ancienne des données et la conservation complète.** Les résultats ne justifient pas une affirmation d’intrusion ou de manipulation volontaire.
