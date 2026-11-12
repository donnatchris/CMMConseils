# Confrontation des rapports aux procès-verbaux de saisie

**8 novembre 2026 — mission SADEDINE-2026.** Relecture documentaire et proposition d'analyses complémentaires. Aucune nouvelle acquisition ni nouvelle investigation des supports n'est effectuée dans cette note. Les rapports historiques restent inchangés.

## Résultat

**Oui, des compléments ciblés sont justifiés.** Les plus utiles concernent l'inventaire numérique de saisie, le filtrage des correspondances, l'examen audiovisuel des séquences du 15 octobre et la provenance des fichiers issus du premier iPhone Mini. Le PV permet surtout de préciser le contexte des constats existants ; il ne démontre pas une intrusion, une rupture clandestine des scellés ou une suppression malveillante.

## Sources et méthode

Source nouvelle : [PV DE SAISIE.pdf](../../docs/PV%20DE%20SAISIE.pdf), 34 pages, SHA-256 `18928481d246c8dff907dcebb37dc3133289b291d0007c2c5900613b8c780db3`.

Le PDF est un scan sans texte exploitable par `pdftotext`. Les 34 pages ont été rendues puis examinées visuellement, y compris les annexes manuscrites. Les numéros ci-dessous sont ceux du **fichier PDF**, qui comporte des versos blancs :

| Pages PDF | Pièce |
|---|---|
| 1 et 3 | Notification du 13 novembre 2024 |
| 5, 7, 9, 11, 13, 15 | PV d'ouverture des scellés et de saisie du 28 octobre, six feuillets |
| 17 | Liste manuscrite d'avocats |
| 19 | Observations de Mme Sadedine du 28 octobre, datées de 18 h |
| 21, 23, 25, 27 | PV de visite et de saisie du 15 octobre, quatre feuillets |
| 29 et 31 | Observations de Mme Sadedine du 15 octobre |
| 33 et 34 | Textes législatifs joints ; aucune analyse juridique menée ici |

Rapprochement avec le [rapport final](../../RAPPORT-FINAL-SADEDINE-2026.md), les synthèses et passages pertinents des rapports [OP-01](../../ordinateur/analyse-ordinateur.md), [TP-02](../../telephones/analyse-TP-02.md), [Freebox](../../freebox/analyse-freebox.md), [SD-01](../../cartes_sd/analyse-cartes_sd-SD-01.md), [SD-02](../../cartes_sd/analyse-cartes_sd-SD-02.md), [SD-03](../../cartes_sd/analyse-cartes_sd-SD-03.md), [transversal SD](../../cartes_sd/analyse-cartes_sd-transversale.md), et les compléments des [17](../20261017-recroisements/compte-rendu.md) et [19 octobre](../20261019-retour-cliente/compte-rendu.md). Les mails et l'attestation de remise ont également été relus.

Les constats techniques sont repris de ces rapports, sans nouvelle validation des acquisitions. Une mention au PV établit ce que le document consigne ; les observations annexées restent les déclarations de leur signataire.

## Ce qui était déjà établi

- OP-01 : activité le 15 vers 10 h 43–10 h 53, puis reprise le 28 à 10:41:56 ; aucune activité Windows corroborée entre les deux. Regroupement `L16B`, exports, dix mises à la corbeille récupérées et trois identifiants Kingston distincts documentés.
- TP-02 : séquence système/Wi-Fi du 17 octobre, traces d'applications et de communications pendant la rétention, avec limites de synchronisation, restauration et attribution physique. TP-01 et TP-03 ne sont pas couverts par cette campagne.
- SD : récupérations sur la terrasse ; défaut structurel commun à onze vidéos chambre/salon, antérieur à la perquisition ; dernière vidéo du salon du 15 jusqu'à environ 13:32:26 selon la caméra et lacune jusqu'au 29. Aucune cause intentionnelle établie.
- Réseau : aucun accès distant non autorisé démontré ; plusieurs identités ou rapprochements restent incertains. Les historiques conservés ne sont pas exhaustifs.

## Chronologie désormais documentée

Heures du PV traitées comme heures civiles locales. Les heures techniques restent soumises aux limites d'horloge déjà exposées.

| Repère du PV | Référence | Incidence sur les analyses |
|---|---|---|
| 15 octobre : arrivée à 6 h 56, porte ouverte par Mme Sadedine à 9 h 45, invitation à entrer à 10 h 10, notification à 10 h 20, visite à 10 h 34 | p. 21 et 23 | Il faut distinguer arrivée, entrée et début de visite. Les observations manuscrites contestent certains éléments du déroulement : ne pas fusionner les deux récits. |
| Présence des appareils constatée à 13 h 51 ; nouvelle demande de codes à 14 h 04 ; contact du magistrat à 14 h 10 ; fin de communication demandée à 14 h 16 ; mise sous scellés à la suite du repère de 14 h 19 | p. 25 | Le PV ne donne pas la seconde de fermeture de chaque enveloppe. **13 h 30 reste la perte d'accès déclarée, pas l'heure documentaire de scellement.** |
| Clôture à 16 h 50 puis départ | p. 27 | Nouveau repère pour les images conservées du 15, si elles couvrent cette période. |
| 28 octobre : présentation de Mme Sadedine à 10 h 22 ; ouverture du scellé PC à 10 h 41 et saisie du mot de passe par elle | p. 7 | **10 h 22 est l'arrivée, pas l'ouverture de l'ordinateur.** Concordance à la minute avec la reprise Windows à 10:41:56, sans étalonnage à la seconde. |
| Ouverture des trois téléphones à 11 h 30 ; déverrouillage par Mme Sadedine ; insertion SIM autorisée à 11 h 45 dans le scellé n° 3 pour obtenir le code Apple donnant accès à iCloud sur le PC | p. 9 | Utiliser 11 h 30 comme repère documentaire d'ouverture des téléphones. L'insertion SIM a un objectif précis de vérification Apple, utile pour un recoupement ciblé. |
| Restitution des quatre appareils consignée ; clôture à 19 h 20 | p. 13 | La restitution est documentée, mais **19 h 20 date explicitement la clôture**, sans horaire séparé de remise de chaque appareil. |

L'activité OP-01 de 10 h 43–10 h 53 le 15 se situe donc pendant la visite décrite et avant le scellement consigné. La dernière image du salon vers 13 h 32 est également antérieure à ce scellement selon les heures affichées. Cela n'identifie aucun opérateur et n'explique pas l'anomalie vidéo.

## Concordances et questions encore ouvertes

**Copies du 28.** Les pages 7 à 11 décrivent les copies LOCAL, GDRIVE, iCloud Drive, messageries, SAGE, SHINE et TELEPHONES. Le PV cite l'archive Takeout déjà retrouvée et l'impression PDF de factures Sage. Ces mentions apportent un contexte documentaire aux traces. Le PDF `test.pdf` supprimé pourrait être un essai lié à cette production : une comparaison avec `SAGE/sage.pdf` permettrait de tester cette hypothèse, sans présumer son résultat.

**Copie externe et inventaire.** La page 11 consigne une copie sur une clé USB vierge de l'administration, préalablement formatée devant les personnes présentes, puis l'authentification numérique de chaque fichier et la gravure des inventaires sur deux CD finalisés. Elle ne donne ni marque, ni série, ni algorithme d'authentification. Les noms `Archive_saddedine.zip`, `Inventaire_saddedine.csv` et `Rejets_saddedine.txt` n'y figurent pas. Leur rapprochement avec cette opération est désormais mieux motivé, mais leur contenu reste à obtenir. **Une copie est consignée au PV ; son contenu exact et son support physique ne sont toujours pas vérifiés techniquement.**

**Trois Kingston.** Le PV décrit une clé de destination, tandis que les rapports établissent trois identifiants de périphériques. Ce n'est pas nécessairement une contradiction : d'autres supports peuvent avoir servi aux outils ou à des étapes intermédiaires. Le formatage décrit n'explique pas, à lui seul, trois identifiants matériels distincts. Les traces `LdSD.bat` et WD restent sans fonction ou destination complètement attribuée.

**Suppressions.** Les dix mises à la corbeille ne sont pas détaillées dans les PV lus. La page 11 décrit cependant une sélection et une exclusion de données personnelles et de correspondances d'avocats avant copie. Le document de mots de passe absent du dossier GDRIVE conservé, mais présent dans l'archive de téléchargement récupérée, peut être examiné sous cet angle. Cela ne démontre ni le motif de sa suppression, ni l'identité de l'opérateur, ni l'absence du document dans la saisie finale. Les fichiers Ciel restent des états, sans base comptable détruite démontrée.

**Dossier laissé sur le PC.** La page 13 confirme l'accord de Mme Sadedine pour conserver les dossiers créés, à titre informatif, et précise qu'ils ne remplacent pas les fichiers saisis. **La présence d'un document dans `L16B` ne prouve donc pas à elle seule sa présence dans la saisie finale.** C'est une limite centrale pour tout contrôle du filtrage.

**Identité des téléphones.** Les pages 7, 9, 11 et 25 ne donnent aucun numéro de série, IMEI ou UDID permettant de départager les deux Mini rouges. La divergence noir/vert pour TP-01 subsiste. Le PV distingue les copies du premier Mini et l'absence d'édition ou de copie depuis le second, sans établir l'équivalence TP-02/scellé n° 3. L'examen du second téléphone est bien décrit : absence de copie ne signifie pas absence d'utilisation.

**Scellés.** Le corps du PV du 28 affirme une vérification de leur intégrité avant ouverture. L'annexe p. 19 rapporte au contraire des différences d'emballages (kraft au départ, enveloppes blanches pour les téléphones à l'arrivée) et l'absence de caractères identifiants sur les pastilles. Il s'agit d'une divergence documentaire à instruire par photos, emballages ou documents de conservation ; les traces du 17 ne la résolvent pas. Le refus de signer est visible p. 15 et 27, et ne permet aucune conclusion technique sur l'intégrité.

## Analyses complémentaires recommandées

| Priorité | Travail proposé | Apport et condition |
|---|---|---|
| **1** | Acquérir en lecture seule le CD d'inventaire ; identifier ses colonnes et empreintes ; rapprocher inventaire, éventuels rejets, archive saisie et `L16B` | Meilleur moyen de vérifier les fichiers réellement retenus et leur identité. Comparer aussi les contenus récupérés dans la corbeille. **Le contenu du CD n'a pas été consulté ici** ; les références LNK retrouvées ne le remplacent pas. |
| **1** | Contrôler le filtrage à partir de la liste d'avocats annexée p. 17 | Recherche ciblée dans PST, EML, MBOX et archives de conversations, avec variantes des noms manuscrits, adresses vérifiées dans le corpus, pièces jointes et citations de conversations. Produire une liste de candidats, pas une qualification juridique automatique. Le contrôle final exige l'inventaire et les fichiers saisis ; une occurrence dans `L16B` seul ne prouve pas un défaut de filtrage final. |
| **1** | Examiner intégralement les séquences audiovisuelles disponibles du salon autour de 13 h 28–13 h 32, puis les séquences pertinentes de la journée sur chambre/salon | Les rapports documentent les défauts techniques et quelques images, **pas une analyse sémantique complète du son et des gestes**. Relever uniquement les actions et paroles observables, les passages inaudibles et les limites ; confronter aux repères 10 h 10, 10 h 34, 13 h 51 et 14 h 19 si couverts. Ne pas déduire l'allumage ou le déverrouillage d'un téléphone d'un simple geste. Ne pas forcer la synchronisation des horloges pour faire coïncider les récits. |
| **2** | Comparer les 27 fichiers `L16B/TELEPHONES/IPHONE13_MINI` aux fichiers disponibles de TP-02 et, si accessible, TP-03 | Les rapports décrivent des créations SI du 15 et FN du 28 ; le PV décrit la copie du premier Mini le 28. Comparer contenus et empreintes, chemins et métadonnées d'origine pour expliquer les dates et rechercher une attribution. Un fichier partagé par le cloud n'est pas un identifiant matériel suffisant. |
| **2** | Recouper le repère SIM/code Apple du 28 à 11 h 45 avec les traces déjà extraites | Examiner une fenêtre autour de 11 h 30–12 h 15 : messages de vérification, comptes, traces radio réellement datables et activité iCloud du PC. Les remappages CommCenter déjà étudiés ne prouvent pas une insertion SIM ; ne pas les réinterpréter automatiquement. Résultat attendu : cohérence ou absence de corroboration, pas attribution certaine sans identifiant discriminant. |
| **2** | Comparer `test.pdf` aux factures de `SAGE/sage.pdf` et rapprocher les dix suppressions des phases d'export/filtrage | Peut expliquer des fichiers de travail et distinguer le retrait d'une copie intermédiaire de la perte d'une donnée source. Les suppressions sont déjà récupérées et datées : inutile de recommencer la même récupération. |
| **2, avec pièces nouvelles** | Documenter les supports USB et les outils utilisés ; comparer les identifiants et le volume `140B8328` | Nécessite inventaires matériels, supports/images ou documentation d'opération. Identifier `LdSD-1.0.4` si un binaire ou un document fiable est disponible ; ne pas le qualifier d'outil d'extraction sur son nom. |
| **2, avec pièces nouvelles** | Examiner la provenance des traces TP-02 du 17 et la conservation des scellés | Anciennes sauvegardes, historique de restauration, journaux contemporains, relevés opérateur et pièces de conservation peuvent être discriminants. Le seul PV n'exclut ni import de traces, ni fonctionnement automatique, ni erreur d'horloge. |

La recherche locale nominale dans `docs` et `ordinateur` a retrouvé les raccourcis de l'inventaire et des rejets, pas leur contenu ni une image de CD identifiée. Ce contrôle limité ne certifie pas l'absence du CD dans tous les stockages du prestataire.

## Ce qu'il n'est pas utile de relancer sans source nouvelle

Les passes générales sur les EVTX, la MFT, les mises à la corbeille, le réveil programmé du 16, le Wi-Fi ASUS et les anomalies FAT/MP4 ont déjà fait l'objet de compléments substantiels. Le PV ne justifie pas de les répéter à l'identique. La Freebox ne gagne aucun historique d'accès supplémentaire par l'arrivée de ce document. Le défaut commun aux vidéos antérieures reste un élément à conserver dans l'interprétation ; le PV ne transforme pas les dates de 2000 en preuve de réinitialisation volontaire.

Pour les caméras, la nouveauté utile est la confrontation du contenu audiovisuel aux pièces, plutôt qu'un nouveau carving général. Pour TP-02 le 17, la priorité reste une source indépendante ou un test de provenance ciblé, plutôt qu'un nouveau comptage des mêmes dates.

## Incidence sur le rapport final

Préparer un addendum daté, puis une version révisée de la synthèse : remplacer l'indisponibilité du PV par les références présentes ; distinguer arrivée à 10 h 22, ouverture PC à 10 h 41, téléphones à 11 h 30 ; intégrer le scellement consigné après 14 h 19 le 15 ; distinguer clôture à 19 h 20 et restitution sans heure individuelle ; mentionner la copie USB consignée sans prétendre en avoir vérifié le contenu ; exposer le filtrage et les observations contradictoires sur les emballages.

La présente note fournit ce rapprochement documentaire sans réécrire les rapports de leurs campagnes respectives. Elle ne réévalue pas la conservation cloud ou la copie de livraison de 2026, et n'atteste pas la résolution des lacunes précédemment signalées.
