# Confrontation H1–H5

Les hypothèses sont des mécanismes à tester, non des probabilités. Plusieurs peuvent se combiner. Les résultats de calcul ne sont pas indépendants de leur hypothèse de timebase ; les lectures de plusieurs services ne sont pas des étalons indépendants de l'horloge civile commune.

## H1 — Lancement réellement daté du 17, puis conservation/suspension

**Compatible :** deux dates explicitement décalées ; départ < sortie ; à 24 MHz, départ ≈752,256 s et sortie ≈2 512,667 s dans le référentiel awake ; uptime dans la tranche empirique [2 500,2 600[. Les horloges Apple autorisent un calendrier qui progresse pendant l'arrêt du compteur absolute.

**Conditions nécessaires :** horloge civile correcte aux instants concernés ; raccord IPS/absolute valide ; même session de noyau pour les deux compteurs ; processus conservé jusqu'à la capture. Pour un écart réellement écoulé de 936 641,8884 s, environ **934 881,478 s de sommeil système** doivent séparer départ et sortie, soit environ 99,812 % de l'intervalle. Les 1 760,410 s restantes sont du temps global awake, pas du CPU consommé par WidgetKit. Une suspension de l'extension sur un téléphone continuellement éveillé est insuffisante.

**Défavorable :** extrême isolé du corpus ; aucune autre mesure du sommeil d'octobre ; aucune trace de résidence de cette extension pendant onze jours. L'architecture WidgetKit rend l'inactivité possible mais ne garantit pas cette conservation. Un redémarrage ordinaire entre les deux événements contredirait la conservation du même processus ; aucun redémarrage intermédiaire n'est démontré ici.

**Tests obtenus :** compatibilité des trois valeurs et existence documentée d'horloges distinctes. **Non obtenu :** boot commun vérifié par identifiant, 10,82 jours de sommeil mesurés, continuité de résidence. H1 est techniquement possible, **pas un fonctionnement normal de ce cas particulier démontré**.

## H2 — Horloge civile ancienne, puis correction

**Compatible :** XNU conserve des dates de départ distinctes du compteur monotone ; calendrier modifiable. Le modèle awake/uptime demeure cohérent si le calendrier avance brusquement. La proximité de procLaunch, Santé et transactions convient aussi à une même horloge erronée.

**Conditions nécessaires :** départ civil conservé sous une date trop ancienne, correction positive ultérieure ou mécanisme équivalent ; raccord des champs au modèle étudié. Si aucun sommeil n'intervient et si la capture est correcte, le saut net requis est ≈934 881,478 s. Avec sommeil, la correction nécessaire est différente et peut être nulle. On ne calcule pas une date de boot physique.

**Défavorable :** aucune ancienne/nouvelle date enregistrée, pas de journal timed/NTP central ; offsets de Paris cohérents et autres valeurs civiles ordonnées. Ces deux derniers points n'excluent pas une date incorrecte partagée. La préférence de réglage automatique ne date pas la correction et ne garantit pas la justesse historique.

**Tests obtenus :** recherche complète de chemins ciblés, relecture préférences, recherche de marqueurs et chronologies ; aucun événement de correction validé. **Limite :** couverture logique et conservation insuffisantes pour exclure H2. Hypothèse explicative possible, **aucun fait concret ne permet d'affirmer une correction**.

## H3 — Horodatage hérité, transfert ou reconstruction

**Compatible :** sauvegarde tardive contenant un rapport ancien ; dates et métadonnées de fichiers peuvent être archivées. Une restauration iCloud de juin est documentée ; d'autres préférences historiques relues antérieurement sont héritées. XNU conserve aussi les départs à travers certains exec : date de processus et première exécution du code courant ne sont pas nécessairement identiques.

**Conditions nécessaires :** pour modifier l'attribution à TP-02, copie/transport du rapport ou de l'état porteur depuis une autre source ; pour expliquer la divergence sur le système producteur, H1/H2 ou un traitement de dates spécifique supplémentaire. **Copier l'IPS seul conserve les deux dates et les compteurs ; cela n'explique pas leur divergence interne.** Une restauration ordinaire de fichiers ne doit pas être assimilée à une reprise du processus vivant d'un ancien noyau.

**Défavorable :** enveloppes, bundle et métadonnées d'écriture cohérents avec une capture le 28 ; même clé que 224 diagnostics et lignée Photos historiquement rattachée à TP-02. Pas de restauration postérieure identifiée expliquant octobre. L'absence d'un historique exhaustif empêche d'en faire une exclusion.

**Tests obtenus :** cohérence des enveloppes et du manifeste ; restauration antérieure relue dans les résultats précédents. **Non obtenu :** chaîne matérielle de production de cet IPS, journal d'importation, implémentation de construction/reconstruction des champs CrashReporter. Transport reste une réserve d'attribution ; ni transport effectif ni réécriture temporelle démontrés.

## H4 — Mauvaises unités ou référentiels

**Compatible comme risque initial :** timebase absente, champs IPS non documentés, unités réellement mixtes dans PlaybackEventStreams. Le suffixe AbsTime ne suffit pas ; l'uptime brut n'a pas nécessairement une précision d'une seconde.

**Tests obtenus :** différence brute **42 249 843 429**, calculs Decimal/Fraction et GNU date concordants ; hypothèses nanosecondes, microsecondes, secondes incompatibles avec le modèle commun d'uptime (0/312 correspondances), contre 312/312 à 24 MHz. Les 53 cas courts de la même clé et les neuf lignes multimédia de 2025 appuient une échelle proche de 24 MHz. Ajuster une fréquence pour faire coïncider la durée civile WidgetKit exigerait ≈45 107,788 unités/s, contradictoire avec les autres contrôles dans un modèle commun.

**Conditions et limites :** la troncature d'uptime et l'origine partagée sont des modèles empiriques ; fraction exacte et raccord IPS/clock non lus dans l'artefact. H4 est fortement défavorisée comme **simple erreur d'échelle**, mais une sémantique privée différente n'est pas formellement exclue. Appeler le résultat « temps CPU du processus » serait une mauvaise interprétation : ce point est corrigé dans cette campagne.

## H5 — Anomalie interne du diagnostic

**Compatible :** valeur temporelle très atypique ; producteur fermé, exact pipeline inconnu ; bug de construction théoriquement possible. `logWritingSignature` n'est pas traité comme une signature cryptographique validant les dates.

**Défavorable :** parsing complet réussi ; 312/312 concordances incident/bundle ; WidgetKit même schéma v2 et compteurs ordonnés ; uptime cohérent sous le modèle partagé ; capture, suivi et dates de fichier proches. Aucun mélange structurel détecté, aucun rollover requis. Les valeurs >2^32 et le type uint64 primaire défavorisent le rollover 32 bits ; à 24 MHz un wrap uint64 correspond à environ 24 356 ans, pas onze jours.

**Tests obtenus :** inventaire de clés, champs bruts, versions, conversions et cohérence interne de tout le corpus. **Non obtenu :** symbolication approfondie ou instrumentation du producteur. Une anomalie de calendrier/diagnostic reste possible ; **l'écart seul ne permet pas de diagnostiquer un rapport corrompu**.

## Niveau de preuve des trois affirmations

| Proposition | Niveau atteint |
|---|---|
| A. Le rapport porte un lancement du 17 octobre | Établi par lecture directe et intégrité de l'objet disponible. |
| B. Le processus a effectivement commencé le 17 selon une horloge correcte | Conditionnel à la sémantique de procLaunch, à la justesse civile et au mécanisme de conservation ; pas étalonné. |
| C. Le matériel physique TP-02 était alors allumé | Exige en plus l'attribution matérielle du système producteur et l'absence d'état transporté ; non établi de manière exclusive. |

Un mécanisme ordinaire de clocks peut rendre les valeurs compatibles sans anomalie civile, **à condition** d'un sommeil système et d'une conservation du processus suffisants. Cette condition n'est pas vérifiée par le rapport. Aucune nécessité démontrée de correction ou de transfert d'état ; aucune démonstration que tout le cas s'explique effectivement par une longue suspension normale.
