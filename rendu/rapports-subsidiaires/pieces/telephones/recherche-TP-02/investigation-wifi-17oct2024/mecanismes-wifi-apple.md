# Mécanismes Wi-Fi Apple : tests internes et limites de transfert

Les deux plist originaux déchiffrés ont été réutilisés ; leurs SHA-256 concordent avec les journaux d'extraction et les empreintes des objets chiffrés ont aussi été revérifiées. Les références complètes sont dans [source-verification.json](source-verification.json). Les 36 configurations sont comparées dans [comparaison-reseaux.csv](comparaison-reseaux.csv), avec valeurs Cocoa natives, UTC et Europe/Paris, sans mot de passe, MAC ni SSID tiers en clair.

## La séquence ASUS_Z01RD

| Propriété | Europe/Paris, 17/10/2024 | Observation certaine / limite |
|---|---|---|
| MacGenerationTimeStamp | 17:25:47.630860 | Date enregistrée de génération ; mécanisme d'écriture exact non obtenu dans un code Apple public. |
| JoinedByUserAt | 17:25:48.147446 | Date typée par le système « user » ; pas un événement d'écran ni une signature humaine. |
| AddedAt / addedAt | 17:25:48.153697 | Valeur exactement identique dans les deux fichiers. Deux représentations cohérentes d'un même état. |
| WiFiNetworkPasswordModificationDate | 17:25:48.196428 | Date de modification enregistrée du mot de passe ; ne prouve pas sa frappe locale. |
| FirstJoinWithNewMacTimestamp | 17:25:52.303180 | 4.672320 secondes après la génération ; marqueur d'association enregistré, pas capture radio. |

`AddReason="WiFi Settings"`, `privateMacSuccessfulAssocAtleastOnce=true`, `NoAssociationWithNewMac=false` accompagnent cette séquence. Le maintien de la date de génération au 17 octobre, contrairement à d'autres réseaux qui ont évolué, renforce sa cohérence. Toutes ces dates portent ici UTC+2 : UTC15:25 correspond à Paris17:25 ; le passage à UTC+1 est le 27 octobre. Le décodage direct des doubles IEEE754 des objets bplist est conservé dans [wifi-binary-date-validation.json](wifi-binary-date-validation.json). Une erreur de conversion Unix/Cocoa ou de fuseau n'explique pas ces cinq valeurs.

Les [parsers iLEAPP](https://github.com/abrignoni/iLEAPP/blob/main/scripts/artifacts/appleWifiPlist.py) lisent des propriétés : ils ne démontrent pas les conditions exactes de leur écriture. Aucun code écrivain Apple ni essai contrôlé sous 17.6.1 établissant l'exclusivité humaine de `JoinedByUserAt` ou de `WiFi Settings` n'a été trouvé dans les sources consultées. La lecture du nom ne doit pas être élevée au rang de comportement expérimental.

## Contrôles internes nouveaux

| AddReason | Nombre | MacGeneration présent | FirstJoin présent | AddedAt=addedAt |
|---|---:|---:|---:|---:|
| WiFi Settings | 25 | 25 | 24 | 25 |
| Cloud Sync | 3 | 0 | 0 | 3 |
| System App | 4 | 4 | 4 | 4 |
| WiFi Password Sharing | 3 | 3 | 3 | 3 |
| 3rd Party App | 1 | 1 | 1 | 1 |

1. Les trois réseaux Cloud Sync n'ont aucune date de génération ou première association dans le snapshot privé, bien qu'ils aient une entrée correspondante. **Aucun contre-exemple Cloud Sync présentant toute la séquence ASUS n'a été retrouvé.** Trois cas ne constituent pas une règle universelle.
2. `network-16` possède `JoinedByUserAt` au 15 avril 2024 12:20:55 Paris, mais `AddedAt` au 11 juin 2024 13:46:15 Paris et `AddReason=Cloud Sync`. C'est un exemple interne d'une date utilisateur historique conservée lors d'un ajout ultérieur. Ce constat réfute l'équivalence « date user = action humaine locale sur ce matériel à cette date ». Il ne dit pas quel service a transporté chaque clé.
3. Un réseau `System App` présente une génération puis première association séparées de **6.910436 secondes**. Une séquence de quelques secondes n'est donc pas exclusive à WiFi Settings. Les trois réseaux de partage de mot de passe possèdent aussi les deux dates ; le partage n'est pas assimilable à une synchronisation cloud silencieuse.
4. Sur 32 couples de dates, **22 premières associations précèdent la génération courante** ; 15 écarts sont proches de quatorze jours (tolérance descriptive quatre heures). Les valeurs évoluent et ne désignent pas nécessairement le même cycle de MAC. La rotation est une explication crédible, pas un résultat expérimental du présent dossier. Ne pas diagnostiquer 22 voyages dans le temps ni utiliser ces différences comme durées de sessions radio.
5. Des générations exactement simultanées existent pour plusieurs réseaux les 28 octobre, 6 décembre et septembre 2026. Cela révèle des traitements groupés possibles. La génération ASUS du 17 octobre n'appartient pas à ces clusters.

Données et contrôles : [network-comparison-summary.json](network-comparison-summary.json), [network-field-history-controls.json](network-field-history-controls.json).

## Quel transport est effectivement validé ?

| Mécanisme | Validation disponible | Peut-il expliquer exactement les deux plist et les dates ASUS ? |
|---|---|---|
| Trousseau iCloud / mots de passe Wi-Fi | Apple documente la synchronisation des mots de passe Wi-Fi ; les trois exemples Cloud Sync confirment un état importé dans ce dossier. | Le transport de MacGeneration, FirstJoin, BSSID et AddReason précis n'est pas validé. La synchronisation seule explique moins bien le profil ASUS que les trois profils Cloud Sync observés. |
| Partage de mot de passe à proximité | Apple décrit sélection du réseau sur le destinataire et appareil donneur déverrouillé ; trois profils locaux disposent de dates privées. | Peut permettre ensuite une association effective du destinataire, mais pas identifier l'auteur ni justifier WiFi Settings au lieu de Sharing sans essai. |
| Migration directe iPhone à iPhone | Conservation de données historiques Photos démontrée dans un essai publié sur versions plus anciennes ; marqueurs DeviceTransferInfo recherchés ici. | Copie d'état plus large plausible ; survie exacte de chaque propriété Wi-Fi sous 17.6.1 non validée, aucune migration ultérieure démontrée ici. |
| Restauration locale chiffrée | Apple inclut paramètres Wi-Fi et données Santé dans les sauvegardes chiffrées ; les deux plist sont effectivement dans celle analysée. | Transport du fichier source possible au niveau sauvegarde ; conservation/réécriture exacte à la restauration sur même/autre appareil reste à mesurer. Présence en sauvegarde ≠ garantie de restauration inchangée. |
| Restauration iCloud | Restauration du 11 juin documentée localement ; règles de couverture différentes du local. | Pas de restauration post17 identifiée. L'importation directe de tous les champs privés n'est pas démontrée ; un réapport ultérieur par sync est distinct de la restauration du fichier. |
| Profil Wi-Fi / MDM / app système | Mécanismes de configuration réseau possibles ; profils extraits examinés, `IsSupervised=false` dans l'état courant. | Aucun payload ASUS ou événement daté du 17 découvert. `PostSetupProfileWasInstalled=true` ne démontre ni payload Wi-Fi ni MDM historique. |
| Import de credentials suivi d'auto-join | Peut produire une activité réelle du destinataire sans consultation ; les catégories System App montrent un traitement distinct. | Pour écrire au temps réel du 17, le destinataire doit fonctionner le 17. Pour rester éteint le 17, H4 doit ajouter un transport de dates anciennes ou une horloge erronée : ce n'est plus une explication autonome par simple auto-join tardif. |

Références primaires : [sécurité du trousseau Apple](https://support.apple.com/en-euro/guide/security/sec0a319b35f/web), [contenu des sauvegardes chiffrées](https://support.apple.com/en-us/108353), [partage de mot de passe](https://support.apple.com/en-gb/102635). Une liste de règles de sauvegarde [relevée par rétro-ingénierie sous iOS 16.4 et explicitement limitée à ces versions](https://gist.github.com/leminlimez/c602c067349140fe979410ef69d39c28/0cb94731cbe5afce512522cf8faca0d6bed58b17) marque ces fichiers de SystemPreferencesDomain `OnlyBackupEncrypted`, `NotToBackupToService`, `NotToBackupInMegaBackup`, `ToRestoreOnly`. C'est un indice spécifique de différence entre voies locale et cloud, **pas** une validation sous 17.6.1/18.5.

Une [étude instrumentée de restauration iCloud](https://dfrws.org/wp-content/uploads/2025/10/From-sync-to-seizure-A-binary-instrumentatio_2025_Forensic-Science-Internat.pdf), notamment sur deux iPhone8 sous 16.7.10, distingue données téléchargées et fichiers présents après restauration ; certaines informations Wi-Fi pourraient arriver par synchronisation ultérieure (hypothèse des auteurs). Elle n'établit pas le transport de nos clés précises. Ne pas convertir ce résultat en « les deux plist ASUS ont été importés ».

Le trousseau déjà extrait contient 6 248 objets genp, 288 inet, 13 certificats, 309 clés, mais leurs enveloppes internes ne livrent pas en clair les attributs de provenance nécessaires : [keychain-format-limit.json](keychain-format-limit.json). Aucun mot de passe n'a été déchiffré ou exporté par cette campagne. L'absence d'attribut lisible n'est pas l'absence de synchronisation.

## Point d'accès et rapprochement OP-01

La MAC privée est celle du **client iPhone** ; les deux BSSID sont ceux de points d'accès observés. La représentation binaire privée de BSSID correspond au premier des deux BSSList (comparaison d'octets, identifiants masqués). Cela rattache des représentations du **28 octobre** au même BSS enregistré ; aucun BSSID explicitement daté du 17 n'a été retrouvé qui permettrait d'étendre ce rapprochement au 17. L'association au même SSID ne prouve pas le même émetteur radio. Les dates `lastJoined`, découverte et système portent le 28 ; leur seule présence n'en fait pas des observations du 17. Les configurations examinées n'apportent pas de bail DHCP, passerelle ou journal de canal daté permettant cette discrimination.

Un [document ASUS officiel](https://dlcdnets.asus.com/pub/ASUS/ZenFone/ZS620KL/SK13920_ZS620KL_2SIM_EM_WEB.pdf) relie Z01RD à la famille ZS620KL/ZS621KL. Un [manuel ASUS d'un autre modèle](https://dlcdnets.asus.com/pub/ASUS/ZenFone/ZA550KL/E13969_ZA550KL_EM_WEB.pdf) illustre un hotspot à nom de modèle ASUS_X00RD. Cela rend l'hypothèse d'un hotspot de téléphone ASUS crédible ; le nom par défaut exact ASUS_Z01RD n'est pas démontré par ces documents. Un SSID est modifiable et copiable : aucun propriétaire ou lieu n'est attribuable à partir de ce nom.

Contrôle nouveau OP-01 : un EVTX WLAN brut de 1 052 672 octets comporte **1 325 enveloppes d'événements valides**, dans seize chunks dont les CRC sont cohérents ; bornes 28 mars 2024–8 octobre 2026 UTC. Aucun événement ne porte une date du 17 octobre 2024. Aucune occurrence littérale du SSID, de la MAC cliente ou des deux BSSID n'y est trouvée dans les encodages recherchés. Le fichier supprimé récupéré de même taille n'a pas d'en-tête/chunks valides dans ce contrôle. Voir [op01-raw-wlan-controls.json](op01-raw-wlan-controls.json). Le contrôle n'a pas décodé les événements BinXML ; une recherche d'octets négative et des dates extrêmes éloignées ne garantissent pas une couverture continue. Aucun lien OP-01/ASUS n'est établi, aucune absence de lien n'est démontrée. Le disque E01 existe ; aucun nouveau montage n'a été effectué.

## Expérience discriminante à préparer sur témoins uniquement

Aucune expérience sur téléphone n'a été réalisée ici. Protocole proposé : deux témoins identifiés matériellement, iOS 17.6.1 si légalement et techniquement disponible, sinon indiquer explicitement la différence ; compte de test isolé, SSID inédit, horloges UTC contrôlées, journaux AP et capture des associations, sauvegardes chiffrées avant/après chaque étape. Ne pas utiliser le compte de la cliente.

Réaliser séparément : connexion manuelle ; seul trousseau iCloud ; partage de mot de passe ; profil auto-join ; migration directe ; restauration locale sur le même appareil puis autre appareil ; restauration cloud avec sync désactivée puis activée. Entre variantes, remettre les témoins à un état connu et changer de SSID. Pour le test de transfert différé, éteindre le destinataire pendant la création du réseau sur la source, puis le rallumer à une date contrôlée différente ; distinguer état reçu avant toute association et état après association. Comparer chaque clé native des deux plist, BSSID, MAC cliente, AddReason, dates et attributs de trousseau sans publier secrets. Répéter chaque variante ; conserver vidéo de la procédure et empreintes des acquisitions.

Un transfert reproduisant **les deux dates privées anciennes**, WiFi Settings et la chaîne complète avec destinataire éteint au temps initial fournirait un mécanisme précis pour H2/H3. Si seul le mot de passe est transféré et les dates privées sont créées à l'horloge courante, il réfuterait ce mécanisme particulier, pas toutes les restaurations possibles. La rotation privée documentée par [Apple](https://support.apple.com/en-us/102509) impose de tenir compte de la version et des paramètres ; elle ne remplace pas ces tests.
