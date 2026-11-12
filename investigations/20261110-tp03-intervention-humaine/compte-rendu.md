# TP-03 — approfondissement de la séquence du 16 octobre 2024

**Mission SADEDINE-2026 — complément du 10 novembre 2026.** Réponse à la demande de rechercher au maximum les éléments permettant de valider ou d’invalider une intervention humaine à **05:31:33–05:31:39, heure de Paris**. Travail effectué sur SIFT, sur copies de la sauvegarde logique déjà déchiffrée, avec deux déchiffrements supplémentaires ciblés. Aucun accès au téléphone ou aux comptes en ligne.

## 1. Résultat de l’approfondissement

**La séquence est confirmée dans les données, mais son examen détaillé ne permet pas de valider une intervention humaine. Il rapproche les transactions Messages d’un mécanisme récurrent de gestion des conseils, sans identifier son déclencheur.** L’hypothèse d’un fonctionnement automatique reste compatible avec les observations. Une manipulation humaine qui déclencherait les mêmes traitements n’est pas exclue.

Les résultats les plus discriminants sont :

- Les **huit transactions Messages** correspondent à **14 changements TipKit** : trois insertions de conseils, trois insertions de règles, trois mises à jour de paramètres et cinq mises à jour de règles. Aucun de ces changements ne concerne un message ou une donation d’événement utilisateur.
- Les règles visent **`ktWaitingForCloud`**, **`isEligibleForOnboarding`** et **`updateAppleID`**. Les trois conseils liés n’ont **aucun `ZLASTDISPLAYED` renseigné**. Aucun affichage ni clic n’est donc attesté par ces lignes.
- Le même **profil de huit transactions et quatorze changements**, défini par les types d’entités et de changements, apparaît dans **41 groupes au total, dont celui du 16 : 40 autres occurrences**. Ce n’est pas une comparaison binaire des contenus ni un classement de ces autres occurrences comme humaines ou automatiques.
- L’événement PersonalAudio est un **échec de préparation CloudKit** : `ZSUCCEEDED=0`, erreur **134400 / NSCocoaErrorDomain**, zéro objet affecté ou terminé. Sa durée est **48,652 ms**. Il ne démontre ni un transfert réussi, ni une connexion Internet, ni une écoute.
- Les deux objets Santé reprennent des mesures du **15 octobre à 13:14**, avec environ **16 h 16 min 44 s** de décalage entre la fin représentée et la création d’objet. Ils ne décrivent aucun déplacement du 16.
- Aucun nouveau témoin daté d’interaction humaine du 16 n’est retrouvé dans les sources supplémentaires exploitables. Plusieurs magasins de communications, d’interaction et de réseau s’arrêtent cependant en **juin 2024** : leur silence en octobre ne permet pas une exclusion.

**Conclusion : intervention humaine non établie ; absence d’intervention humaine non démontrée.** La séquence demeure un indice de traitement logiciel daté pendant la conservation déclarée, avec les réserves de provenance et d’horloge de la sauvegarde. Elle n’est pas un marqueur validé de déverrouillage, d’utilisation au premier plan ou d’extraction.

## 2. Sources, fenêtre et préservation

Le [rapport TP-03](../../telephones/analyse-TP-03.md) documente série **Y4Q9KGHG26**, UDID **00008110-001249321444801E**, iPhone14,4, iOS déclaré 17.5.1, absence d’Info.plist et dates de sauvegarde de septembre 2025. Le [rapport transversal initial](../20261110-telephones/compte-rendu.md) expose le PV et les rapprochements avec les autres supports.

Le PV situe le scellement après le repère de **14:19 le 15 octobre**, sans heure individuelle certaine de fermeture, puis l’ouverture des téléphones à **11:30 le 28**. Le rattachement de TP-03 à l’un des deux numéros de scellés Mini n’est pas résolu. L’expression « pendant les scellés » désigne ici la concordance des dates enregistrées avec cette fenêtre documentaire, pas une certification de l’état physique du scellé.

Le [mail complémentaire](../../docs/mail-2.txt), rubrique 5, indique des téléphones éteints puis un rallumage allégué vers 13:30 le 15. Ce récit est conservé comme déclaration ; les contrôles audiovisuels antérieurs ne démontrent pas techniquement l’allumage ou le déverrouillage d’un téléphone. Il n’existe pas ici de mesure indépendante de l’état d’alimentation à la fermeture de chaque scellé et pendant la nuit suivante. **Si une extinction effective à la fermeture était établie indépendamment, le scénario « demeuré allumé » devrait être écarté : une production locale ultérieure supposerait une reprise, dont il resterait à identifier la cause, ou une autre explication des dates.** L’état éteint n’est ni supposé faux ni considéré techniquement prouvé par les seuls artefacts.

Source chiffrée SIFT : `/media/shared/forensic/SADEDINE-2026/TP-03/00008110-001249321444801E/`. Les sources sont ouvertes en lecture. Les écritures sont réservées aux dossiers de travail ; aucun fichier d’acquisition n’est une destination. Les anciens rapports sont conservés dans `rapports-avant/`.

Copies générales et prioritaires réutilisées :

```text
/home/sansforensics/analysis/tp03-20261110/
/home/sansforensics/analysis/tp03-priority-20261110/
```

Nouveaux dossiers SIFT, distincts et conservés :

```text
/home/sansforensics/analysis/tp03-human-20261110/
/home/sansforensics/analysis/tp03-human-window-20261110/
/home/sansforensics/analysis/tp03-human-controls-20261110/
/home/sansforensics/analysis/tp03-human-extra-20261110/
/home/sansforensics/analysis/tp03-human-atx-20261110/
/home/sansforensics/analysis/tp03-human-atx-v2-20261110/
/home/sansforensics/analysis/tp03-human-plist-recovery-20261110/
```

Les bases et WAL de travail sont contrôlés par SHA-256 ; les requêtes ciblées et leurs paramètres sont conservés. Les SHM sont des auxiliaires de coordination de lecteurs, distingués des bases et WAL. Les trois fichiers principaux de la séquence n’ont pas de compagnon WAL référencé dans le manifeste contrôlé : leur constat ne résulte pas de l’assimilation d’une ancienne trame WAL à une ligne courante.

## 3. Messages : déterminer ce que les huit transactions ont changé

Artefact : `AppDomainGroup-group.com.apple.tipsnext/com.apple.MobileSMS/.tipkit/tips-store.db`. Lecture des **1 266 transactions conservées**, de `ACHANGE`, `Z_PRIMARYKEY`, des règles, paramètres, conseils et donations. Les auteurs/processus ont été joints à `ATRANSACTIONSTRING`, sans assimiler le nom `MobileSMS` à une application affichée à l’écran.

| Transactions | Changements constatés | Rattachement actuel |
|---|---|---|
| 1217–1218 | Insertion conseil 129/règle 132, mise à jour paramètre 6 et règle | `Bool.ktWaitingForCloud` |
| 1219–1220 | Mises à jour des règles 10 et 11 | Règles du magasin de conseils, pas lignes de messages |
| 1221–1222 | Insertion conseil 130/règle 133, mise à jour paramètre 5 et règle | `Bool.isEligibleForOnboarding` |
| 1223–1224 | Insertion conseil 131/règle 134, mise à jour paramètre 4 et règle | `Bool.updateAppleID` |

Les blobs de règles et de conseils sont des archives plist lisibles. Les prédicats évaluent un paramètre booléen. **La valeur actuelle `false` des trois paramètres n’est pas présentée comme leur valeur historique au 16** : `ACHANGE` fournit une entité, une opération et un masque de colonnes, pas ici toutes les anciennes valeurs.

Les trois conseils 129–131 ont `ZLASTDISPLAYED=NULL`. L’historique conservé les concernant retrouve seulement leurs insertions du 16, sans changement ultérieur d’affichage identifié. Le magasin contient néanmoins **un autre conseil avec une date d’affichage renseignée**, en 2024 avant octobre : la colonne n’est donc pas entièrement vide. Cela renforce l’absence de témoin d’affichage pour les trois conseils ciblés, sans garantir qu’un événement supprimé ou non journalisé serait détecté.

L’unique donation conservée est liée à `com.apple.MobileSMS.send-message`, datée du **31 mai 2024**. Aucun envoi le 16 n’est attesté par cette donation. Les événements de conseils ne constituent pas un historique complet des SMS envoyés.

Pour comparer la forme de la séquence, les transactions du même auteur sont regroupées lorsque l’écart entre deux transactions successives ne dépasse pas **deux secondes**. Le profil cible est :

```text
CoreRuleRecord, insertion : 3
CoreTipRecord, insertion : 3
CoreParameterRecord, mise à jour : 3
CoreRuleRecord, mise à jour : 5
```

Il existe **41 groupes identiques selon ce critère**, entre avril 2024 et septembre 2025, dont trois le **15 octobre à 13:13:13, 13:24:57 et 13:28:05**, celui du **16 à 05:31:39**, et un le **4 novembre à 23:40:45**. Le détail est dans `prive/controles/results.json`. Cette récurrence est compatible avec un chemin réutilisé de création/évaluation de conseils. **Elle ne prouve pas que ce chemin ne peut s’exécuter qu’en arrière-plan, ni qu’une personne l’a déclenché.** Aucun témoin expérimental sur un iPhone iOS 17.5.1 équivalent n’est disponible.

La documentation Apple distingue l’éligibilité à l’affichage et la présentation d’un conseil ; une règle évaluée ne suffit pas à attester sa présentation. Voir [TipKit, shouldDisplay](https://developer.apple.com/documentation/tipkit/tip/shoulddisplay). La structure interne SQLite est interprétée à partir de ses propres schémas et relations, sans prétendre qu’Apple documente ce format forensique.

## 4. PersonalAudio : un échec, sans objets traités

Artefact : `HomeDomain/Library/Accessibility/com.apple.personalaudio.sqlite`, `ANSCKEVENT.Z_PK=31013`.

| Champ | Valeur |
|---|---|
| Début Paris | 16/10/2024 **05:31:35.372222** |
| Fin Paris | **05:31:35.420874** |
| `ZCLOUDKITEVENTTYPE` | **0**, correspondant à la préparation (`setup`) dans l’énumération publique |
| `ZSUCCEEDED` | **0** |
| `ZERRORDOMAIN` / `ZERRORCODE` | **NSCocoaErrorDomain / 134400** |
| `ZCOUNTAFFECTEDOBJECTS` / `ZCOUNTFINISHEDOBJECTS` | **0 / 0** |

Sur les **11 018 événements conservés**, treize portent le même triplet type 0/échec/134400, notamment quatre le 15 avant scellement et plusieurs en novembre/décembre. L’événement du 16 n’est pas, à lui seul, une anomalie nouvelle propre à la conservation. `ATRANSACTION` de ce magasin est vide dans la copie examinée ; aucune modification datée de réglage audio n’est attribuable au 16 par cette table.

Le code brut 134400 est conservé **sans lui assigner une cause détaillée certaine** : le texte explicatif de l’erreur n’est pas dans cette ligne. L’échec ne permet pas d’affirmer une authentification réussie, un import/export ou l’absence de réseau.

Références : [Apple, Event](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/event), [Apple, setup](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer/eventtype/setup), [énumération numérique publiée par Microsoft pour son binding CoreData](https://learn.microsoft.com/en-us/dotnet/api/coredata.nspersistentcloudkitcontainereventtype). Les mécanismes automatiques de planification, d’import et d’export sont décrits dans [Apple TN3163](https://developer.apple.com/documentation/technotes/tn3163-understanding-the-synchronization-of-nspersistentcloudkitcontainer). Ces documents décrivent des mécanismes possibles ; ils ne constituent pas un journal de ce téléphone.

## 5. Santé, verrouillage et horloge : tester les arguments indirects

Les objets **348331/348332**, types 8/7, ont le même intervalle représenté : **15/10 à 13:14:16.834842–13:14:49.933610**. Leurs créations du 16 sont décalées respectivement de **58 604,001448 s** et **58 604,011964 s** après cette fin. D’autres objets de même provenance montrent également des retards de plusieurs heures ou jours. La création d’un objet ne doit pas être confondue avec le moment d’un pas, un déplacement ou un geste sur l’écran.

La recherche des métadonnées associées et des `external_sync_ids` ne retrouve aucune ligne pour ces deux objets. Cette absence n’est pas une preuve de saisie manuelle, ni son exclusion. La provenance logique iPhone14,4/17.5.1/identité Santé 2 reste celle décrite dans le rapport initial ; aucun nouvel ancrage physique ou opérateur n’est identifié.

Les classes du manifeste sont **2 pour la base Santé**, **3 pour PersonalAudio et TipKit**. Elles décrivent l’état sauvegardé, pas nécessairement celui de chaque fichier en octobre 2024. Les protections « sauf si déjà ouvert » et « jusqu’à la première authentification » permettent certains traitements lorsque l’écran est verrouillé. **Ces valeurs ne datent ni un redémarrage ni un nouveau déverrouillage le 16.**

Il faut aussi conserver l’hypothèse opposée : Apple explique que certaines écritures Santé peuvent être mises en cache puis enregistrées lorsque l’utilisateur déverrouille l’appareil. Un déverrouillage déclenchant un traitement différé est donc compatible avec le mécanisme général. **Mais le champ interne `creation_date` n’est pas une attestation d’authentification ou de validation du code, et aucune trace indépendante de déverrouillage ne tranche ici.** La classe de fichier autorisant certains accès verrouillés et l’absence de journal d’authentification empêchent de rendre ce scénario obligatoire.

Références : [Apple, protection de la vie privée HealthKit](https://developer.apple.com/documentation/healthkit/protecting-user-privacy), [protection sauf si ouvert](https://developer.apple.com/documentation/foundation/fileprotectiontype/completeunlessopen), [protection jusqu’à première authentification](https://developer.apple.com/documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication). Il s’agit d’une analyse des possibilités, pas d’une reproduction de la séquence sur le matériel.

Les préférences `timed` déclarent un réglage automatique de l’heure et un fuseau non automatique dans l’état sauvegardé. Cela ne calibre pas l’horloge du 16. Les dates des trois magasins peuvent partager une même horloge et être transportées ensemble dans un historique. Ni le réglage actuel ni leur proximité temporelle ne constituent trois références indépendantes de temps civil.

## 6. Recherche élargie et contre-épreuves

### 6.1. Toutes les colonnes numériques SQLite

La nouvelle passe parcourt **1 548 fichiers SQLite distincts**, **10 985 tables ordinaires** et **47 770 colonnes numériques ou sans affinité textuelle/BLOB explicite**, sans filtre sur le nom des colonnes. Fenêtre : **16/10 00:00–17/10 00:00 Paris**. Hypothèses : Unix secondes/millisecondes/microsecondes/nanosecondes, Cocoa secondes/nanosecondes. Les colonnes déclarées BLOB/texte et les tables virtuelles ne sont pas réputées décodées.

Elle donne **16 valeurs candidates par couple table/colonne**, sans erreur de requête dans cette passe : les deux créations Santé, début/fin PersonalAudio, huit transactions et trois évaluations de règles, plus un repère quotidien Apple. Ce décompte ne représente pas seize événements indépendants.

Le repère quotidien et les **treize lignes centrales de `spotlight_sfm` ont tous un payload de longueur zéro**. La réserve initiale « payload non décodé » est donc précisée : aucun contenu d’activité n’est fourni par ces lignes vides. Elles n’attestent pas un fonctionnement quotidien ni un logiciel espion.

### 6.2. Préférences, réveil, biométrie et communications

**2 493 plists** sont parsés, avec recherche dans toutes leurs valeurs numériques prises en charge et leurs plists embarqués. Les deux seuls candidats du 16 sont le champ `mediaremote` à **01:40:51** déjà connu, de sémantique non validée, et l’échéance **NextFreshmint** à **13:13:33**, qui n’est pas une exécution.

Les trois exceptions ont fait l’objet d’une reprise explicite : `.GlobalPreferences_m.plist` est vide ; `CircleJoinRequested` comporte une date année 0000 et une date `lastWritten` du **15 à 13:13:34 Paris**, avant scellement ; `sleepd` contient une même date sentinelle hors plage dans huit champs. Une lecture tolérante conserve ce marqueur au lieu de fabriquer des dates : les autres dates natives récupérées ne donnent aucun événement du 16. Il ne s’agit pas d’une réparation des sources.

Les préférences SpringBoard, backboardd, biométrie, ScreenTime, UsageTracking, planification et horloge ne donnent pas de déverrouillage ou de démarrage daté du 16 dans les champs exploitables. Ce sont des états partiels, souvent hérités, et non des journaux exhaustifs de l’écran.

Les **157 alarmes** de l’état `mobiletimerd` ne fournissent pas une alarme déclenchée à 05:30 le 16. L’entrée 05:30 est désactivée et porte une ancienne date de 2021 ; le dernier déclenchement enregistré dans la préférence date de juin 2024. Cela n’établit pas l’état de toutes les alarmes au 16, ni une cause de réveil.

| Source de corroboration | Couverture observée | Portée de l’absence au 16 |
|---|---|---|
| `interactionC`, 8 interactions | Toutes au 24 juin 2024 ; dernières créations vers 15:39:23 | Pas de contre-épreuve fiable pour octobre |
| DataUsage, 2 151 processus | Dernier `ZTIMESTAMP` le 24 juin à 15:42:46 | Pas une mesure de trafic à 05:31 |
| DataUsage, 4 061 lignes `ZLIVEUSAGE` | Dernier horodatage le 24 juin à 15:38:24 | Lignes de cumuls, pas 4 061 sessions ; pas d’exclusion d’octobre |
| `ZWIFIDATA`, `ZEVENT` | Tables vides | Pas de session radio corroborée |
| Safari `history_visits` | Table vide | Aucune conclusion d’absence de navigation |
| SMS/appels/photos | Limites et recherches du rapport TP-03 maintenues | Aucun geste humain du 16 identifié ; SMS/appels arrêtés en juin |
| Diagnostics et journaux présents | Aucun nouveau journal textuel du 16 trouvé ; diagnostics déjà datés d’avril–juin | Absence de trace de redémarrage exploitable, pas preuve d’absence de redémarrage |

Le trousseau sauvegardé contient **3 540 éléments genp, 106 inet, 18 certificats et 312 clés**, avec des contenus internes `v_Data` non décodés dans cette campagne, sans `cdat`/`mdat` directement lisibles dans cette représentation. Aucun secret n’est exporté et aucune chronologie complète du trousseau n’est revendiquée.

### 6.3. Deux artefacts supplémentaires d’usage des applications

Une sélection exacte de deux fileID déchiffre **1 813 127 octets** supplémentaires, avec empreintes chiffrées source avant/après et empreintes claires :

- `HomeDomain/Library/DuetExpertCenter/D2DBackups/ATXBackupData` ;
- `HomeDomain/Library/SpringBoard/RecentAppLayouts.pb.lzfse`.

Le mot de passe est saisi par `getpass`, sans écho ni argument de commande. `lzfse` **0.4.2** est installé dans `/home/sansforensics/analysis/tp03-human-dependencies-20261110`, isolément des preuves et des dépendances initiales.

L’enveloppe ATX est décodée par longueurs explicites : **45 entrées**, consommation exacte des **1 811 246 octets**, aucun octet restant. Les huit octets de métadonnées internes de chaque bloc restent bruts, sans sémantique inventée. Résultat : **une base SQLite de 3 715 072 octets, `quick_check=ok`, et 44 archives plist valides**. Une exploration initiale par signatures LZFSE, également conservée, rencontrait des débuts de blocs internes incomplets : ses erreurs ne désignent pas des corruptions d’archive. La passe structurée est la référence.

Le magasin ATX contient **480 lignes `appInfo`**, mais seulement **une ligne `appLaunchSequence`**, et zéro ligne `alog`/`afeedback`. Les 106 ancrages conservés vont du **22 mai au 17 juin 2024**. `appInfo` contient des derniers lancements et inclut un pseudo-composant `backlightActivated` ; ce dernier est daté du **9 décembre à 07:56:54**, et le dernier lancement Messages du **4 novembre à 23:40:45**. **Ce sont des derniers états qui peuvent écraser des événements plus anciens.** Aucun candidat du 16 n’est retrouvé dans les dates examinées de la base et des modèles plist. La seconde passe ATX étend le contrôle aux **30 tables et 112 colonnes numériques ou non explicitement textuelles/BLOB** de cette base, selon six échelles/époques : **zéro candidat du 16**. La première passe est conservée ; `tp03-human-atx-v2-20261110` est la référence finale pour ce contrôle.

RecentAppLayouts se décompresse en **13 808 octets**. Le flux respecte le cadrage protobuf parcouru intégralement ; les champs restent numérotés faute de schéma sémantique validé. Il ne fournit aucun candidat numérique du 16 selon les époques testées. **Une disposition récente d’applications n’est pas un journal historique de leurs passages au premier plan** ; les champs opaques ne permettent pas d’exclure un usage antérieur.

### 6.4. Transport d’historique et rapprochement avec TP-02

Les huit timestamps/auteurs/bundles/processus du 16 ne sont pas retrouvés à l’identique parmi les **12 081 transactions Messages** de la copie TP-02 comparée. L’événement PersonalAudio de TP-02 pendant sa période centrale porte une autre date et réussit ; il n’est pas une duplication de l’échec TP-03. Cela écarte une duplication exacte de ces lignes dans **ce comparatif limité**, sans rendre la lignée TP-03 intransportable.

Les migrations Photos, l’identité Santé et les anciennes préférences de restauration sont maintenues comme indices de lignée. Aucun nouvel événement de restauration postérieur expliquant positivement la séquence n’est identifié. Les dates tardives de sauvegarde, l’absence d’Info.plist et du journal d’acquisition empêchent néanmoins de fermer cette hypothèse. La comparaison des PDF communs aux deux Mini ne tranche pas la provenance de la séquence système.

## 7. Évaluation contradictoire des scénarios

| Scénario | Éléments compatibles | Ce qui manque pour le valider |
|---|---|---|
| Traitement automatique, appareil demeuré allumé | Échec interne CloudKit, mécanisme récurrent TipKit, enregistrement différé Santé ; accès verrouillé possible selon protection/état | Déclencheur précis, journal de veille/réveil, alimentation et état de verrouillage contemporains |
| Déverrouillage ou ouverture de Messages par une personne | Une interaction peut déclencher les mêmes routines ; HealthKit peut vider des données en attente lors d’un déverrouillage | Authentification, écran/premier plan ou action utilisateur datés ; aucun de ces témoins n’est identifié |
| Simple réveil écran/alimentation sans déverrouillage | Peut provoquer des tâches selon l’état antérieur | Aucun événement contemporain de rétroéclairage ou de branchement ne le démontre |
| Redémarrage suivi d’un déverrouillage | Compatible avec certaines initialisations | Pas de démarrage daté du 16 ; la forme TipKit ne constitue pas un marqueur de boot validé |
| Historique transporté ou horloge incorrecte | Sauvegarde tardive et magasins transportables partageant leur horloge | Aucun transport explicatif ou saut d’horloge n’est positivement daté ; aucune référence indépendante n’étalonne 05:31 |
| Extraction de données | Certains outils déclenchent des traitements système | Aucun outil, hôte, transfert ou session d’extraction rattaché au 16 ; les lignes observées ne le caractérisent pas |

**Aucune probabilité chiffrée n’est calculable avec ces seules pièces.** La répétition d’une routine rend son contenu peu discriminant pour l’intervention humaine ; elle n’efface pas sa date ni la question du fonctionnement pendant la conservation. Il n’existe pas ici de moyen de passer de « aucun geste retrouvé » à « personne n’est intervenu ».

Les pièces les plus utiles pour trancher sont des éléments contemporains : conditions de stockage et d’alimentation, registre des manipulations, rapprochement séries/scellés, journaux d’authentification/démarrage/radio ou acquisition système conservée plus proche d’octobre 2024, avec référence de temps indépendante. Leur disponibilité n’est pas présumée. Une nouvelle acquisition actuelle ne recréerait pas les journaux de 2024 déjà absents.

## 8. Reproduction, limites et livraison

Six nouveaux scripts sont sous `telephones/scripts/` : `tp03_human_sequence.py`, `tp03_window_all_columns.py`, `tp03_collect_selected.py`, `tp03_decode_atx.py`, `tp03_human_controls.py`, `tp03_recover_preferences.py`. Les commandes sont dans la [notice](../../telephones/scripts/README-TP-01-TP-03.md). Les résultats détaillés et sources de documentation sont dans `prive/`, exclus de Git. Les clairs des artefacts restent sur SIFT.

Les captures de documentation Apple ont leurs URL et SHA-256 ; elles n’ont reçu aucune donnée du dossier. Les détails des échecs et limites restent conservés. Les scripts utilisent les formats et API indiqués ; aucune reconstitution exhaustive du système de fichiers, des BLOB applicatifs chiffrés, de l’espace SQLite supprimé ou des journaux absents n’est revendiquée. La recherche numérique élargie complète le tri initial, sans certifier l’interprétation des tables virtuelles/propriétaires.

Les empreintes des résultats rapatriés et les contrôles finaux des sources sélectionnées sont consignés séparément dans `prive/verification-livraison.json` et `prive/verification-sources-finale.json`. L’empreinte de livraison des rapports/scripts est dans `SHA256SUMS-livraison.txt`. Ces contrôles établissent la cohérence des travaux et transferts, pas l’authenticité de l’horloge de 2024.

**Vérification de livraison : 117 fichiers JSON rapatriés ont les mêmes SHA-256 que sur SIFT ; les onze sources chiffrées sélectionnées, dont le manifeste, sont inchangées.** Les liens locaux des cinq documents de livraison et la syntaxe des six nouveaux scripts sont contrôlés. Le manifeste de livraison du complément précédent reste un état historique ; les versions avant la présente mise à jour sont conservées dans `rapports-avant/`, et le nouveau manifeste couvre les versions courantes.
