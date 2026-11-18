# Relecture transversale et nouveaux indices téléphoniques

**Mission SADEDINE-2026 — 10 novembre 2026.** Analyse de TP-01, TP-03, recoupements avec TP-02/OP-01/Freebox et relecture des rapports courants. Pas de nouvelle acquisition physique, ni de connexion aux comptes de la cliente.

**Actualisation après approfondissement ciblé :** la [nouvelle étude TP-03](../20261110-tp03-intervention-humaine/compte-rendu.md) confirme la séquence mais identifie un échec CloudKit sans objet traité et un profil TipKit retrouvé dans 40 autres séquences. Aucun affichage des trois conseils ni déverrouillage du 16 n’est attesté. Les nouveaux contrôles ne valident pas l’intervention humaine et ne permettent pas non plus de l’exclure. Les détails de couverture ci-dessous décrivent la passe initiale ; la nouvelle étude ajoute deux artefacts déchiffrés et une recherche élargie.

## 1. Résultats propres et portée actuelle

J’ai analysé TP-01 et TP-03 et exécuté les recoupements décrits ci-dessous le 10 novembre 2026. La séquence du 16 de TP-03 a ensuite été approfondie : les 40 profils comparables privilégient les traitements internes, sans identifier leur déclencheur. Le [rapport détaillé](../20261110-tp03-intervention-humaine/compte-rendu.md) et la [revue comparative](../20261110-revue-intervention-scelles/compte-rendu.md) portent les conclusions actuelles. Cette note conserve les collectes, requêtes et résultats spécifiques de la première passe.

## 2. Périmètre de relecture et travaux nouveaux

La relecture porte sur le rapport final, les rapports courants OP-01, TP-02, Freebox, acquisition SD, SD-01/02/03 et transversal SD, les compléments synthétiques des 17/19 octobre et 8/9 novembre, les précisions SMS/uptime, les contrôles L16B et les recherches documentaires. Les études OP-01 sur les opérations du 28 et le réseau ASUS ont été rapprochées de ces conclusions. Les guides et annexes techniques sont consultés selon les pistes, sans assimiler leur consultation à une répétition de toutes les analyses.

Pièces de cadrage relues : `docs/mail.txt`, `docs/mail-2.txt` et l’attestation de remise. `docs/memo.md`, la passation OP-01 et les notes de cadrage sont des supports de méthode ou d’historique, **pas des preuves indépendantes de 2024**. Le journal de sauvegarde reste absent. Le fichier des codes est utilisé seulement comme ressource d’accès si nécessaire, jamais comme pièce publique.

**PV original :** le SHA-256 reste `18928481d246c8dff907dcebb37dc3133289b291d0007c2c5900613b8c780db3`. Les pages PDF **7, 9, 11, 13, 19 et 25** ont été rendues puis revues visuellement pour les appareils, horaires, copies, restitution et observations sur les enveloppes. Il s’agit d’une contre-lecture ciblée ; les 34 pages avaient fait l’objet de la campagne du 8 novembre. Aucune nouvelle qualification juridique n’est effectuée.

| Opération | Statut dans cette campagne |
|---|---|
| Inventaire, copies et analyse TP-01 | **Nouveau**, sur SIFT |
| Déchiffrement et analyse TP-03 | **Nouveau**, sur SIFT |
| Vérification de la séquence TP-03 du 16 | **Nouvelle lecture directe** des bases déchiffrées et de leurs schémas |
| Comparaison PDF TP-03/L16B | **Nouvelle**, par SHA-256 des contenus déchiffrés ; empreintes L16B déjà établies |
| Identification du pair record d’OP-01 | **Nouveau rapprochement** avec l’UDID de Manifest.plist ; résultats OP-01 antérieurs réutilisés, pas nouveau montage Windows |
| Comparaison des adresses clientes Wi-Fi des téléphones aux exports Freebox | **Nouvelle**, sur fichiers conservés ; pas d’appel à la Freebox |
| EVTX/MFT/corbeille/SD et contenu des correspondances d’avocats | **Relecture des résultats existants**, pas nouvelle récupération/scans généraux/OCR |
| Caméras, comptes Apple/Google/Microsoft, opérateurs, cloud prestataire | Aucun accès supplémentaire, aucun message ni contact externe |

Les copies antérieures des rapports modifiés sont dans `rapports-avant/`. Les anciennes annexes et manifestes ne sont ni effacés ni recalculés pour masquer leurs versions historiques. Les nouveaux contrôles et empreintes ont leur propre dossier.

## 3. Bornes de procédure désormais applicables

| Repère | Source | Conséquence |
|---|---|---|
| Perte d’accès aux téléphones vers 13:30 le 15 | Mail initial | Déclaration ; ne date pas la fermeture des scellés |
| Mise sous scellés après le repère de 14:19 le 15 | PV, p. 25 | Les traces de 13:30–13:50 ne sont pas automatiquement sous scellé fermé |
| Arrivée à 10:22 le 28 | PV, p. 7 | Pas l’heure d’ouverture de tous les appareils |
| Ouverture du PC à 10:41 | Même page | Reprise Windows à 10:41:56 après cette ouverture |
| Ouverture des trois téléphones à 11:30 | PV, p. 9 | Les traces du 28 avant 11:30 doivent être séparées des opérations après ouverture |
| Insertion SIM à 11:45 dans le scellé n° 3 | Même page | Pas de correspondance certaine avec TP-02 ou TP-03 |
| Restitution consignée ; clôture à 19:20 | PV, p. 13 | Pas d’heure individuelle de remise de chaque appareil |

Les pages 7/25 décrivent un téléphone noir et deux rouges ; la page 11 précise iPhone 13 et deux Mini. Les séries/UDID ne sont pas fournis. TP-01 est vert dans l’attestation : la divergence demeure. Les deux Mini rouges ne sont pas identifiés par leur seul ordre interne TP-02/03.

Les heures sont converties par **Europe/Paris**, sans UTC+2 fixe après le changement du 27 octobre. Les horloges caméra ne sont pas forcées à coïncider avec iOS, Windows ou le PV. Les caméras n’étaient pas sous scellés.

## 4. TP-03 : nouvelle séquence pendant la conservation

| Heure de Paris | Constat vérifié | Ce que cela ne démontre pas |
|---|---|---|
| 15/10 18:33:26.915492–18:36:27.578715 | Préférences `routined` de registration/désinscription GNSS | Pas de coordonnées, trajet, déplacement ou opérateur |
| 16/10 01:40:51.941617 | Date native `mediaremote/MRDPQPDS.PED` | Sémantique exacte non validée ; pas de lecture musicale ou télécommande démontrée |
| 16/10 05:31:33.935058 et .945574 | Créations Santé, objets 348331/348332 | Les mesures représentent le **15 à 13:14** ; aucun déplacement du 16 établi |
| 16/10 05:31:35.372222–.420874 | Événement interne PersonalAudio 31013 | Pas d’enregistrement sonore ni d’écoute déduits du nom du magasin |
| 16/10 05:31:39.196280–.252170 | Huit transactions TipKit 1217–1224, processus MobileSMS | Pas huit SMS lus/envoyés ; aucun premier plan ou déverrouillage certifié |

Les jointures Santé donnent une provenance `iPhone14,4`, iOS 17.5.1, identité logique 2, identique au champ matériel logique healthd. Les migrations Photos d’avril/juin 2024 portent l’UDID TP-03. **Cela rattache une lignée logicielle à TP-03 ; cela ne rend pas ses historiques matériellement intransportables.** Un ancien type de produit dans la table de sources Santé et les migrations antérieures montrent un héritage de données.

Le regroupement du 16 est un **indice positif de traitement système sur l’installation source**, plus précis qu’une date de message entrant ou un rendez-vous. Il reste impossible de départager une production sur TP-03 à horloge correcte, un historique transporté plus tard ou une date source erronée. Les magasins distincts peuvent être copiés ensemble et partager la même horloge ; ils ne constituent pas trois étalons matériels indépendants.

Deux échéances de préférences au 16/21 (`Next…`) ne sont pas des exécutions. Des dates de calendrier, clés Facebook et statistiques journalières restent des métadonnées ou contenus non validés comme activité locale. Six intervalles Santé du 28 ont été créés le 29 : ils ne prouvent pas une écriture avant l’ouverture du 28.

Le [rapport TP-03](../../telephones/analyse-TP-03.md) conserve identifiants, méthode, limites et pièces. Les contrôles finaux trouvent **62 déchiffrements communs identiques** entre passes et **32 contrôles source/clair inchangés** ; aucune erreur de déchiffrement. Ces vérifications authentifient la cohérence des dérivés avec la copie analysée, pas l’heure civile des événements de 2024.

## 5. TP-01 : conserver les pistes sans surinterpréter les dates

Le [rapport TP-01](../../telephones/analyse-TP-01.md) détaille :

- deux messages WhatsApp entrants datés du 15 après le scellement, avec un autre horodatage groupé le 28 vers 16:13 ; récupération différée compatible, réception locale le 15 non démontrée ;
- des dates de messages vocaux du 15, 17 et 19 dans `deleted`, avec `trashed_date=0` : aucune suppression à ces dates établie ;
- des métadonnées iCloud Drive du 23, reproduites côté client/serveur, sans attribution matérielle ;
- des dates de ressources/configurations et quatorze fichiers de cache AliExpress du 15 au 24 : provenance locale non établie, mais pas écartée par principe ;
- des traitements système et deux lignes WhatsApp sortantes le 28 après ouverture.

Aucune preuve locale avant ouverture n’est établie ; l’inactivité n’est pas certifiée. La sauvegarde est non chiffrée, identifiée par la série Q13QT4F164. Les copies et bases ont été traitées sur SIFT. Une correction des bornes du complément auxiliaire a été reproduite vers `supplement-v2`, **sans changement des résultats structurés** ; la première passe est conservée.

## 6. Nouveaux recoupements entre supports

### 6.1. Les mêmes PDF dans les deux Mini

Les 26 PDF candidats de TP-03 fournissent un équivalent SHA-256 exact aux **27 entrées L16B**, soit **20 contenus distincts**. TP-02 donnait déjà un résultat de 27/27.

**Conséquence : ces PDF ne départagent pas TP-02 et TP-03.** Leur présence dans les deux sauvegardes ne démontre ni une extraction directe depuis l’un, ni une copie de l’un vers l’autre, ni la date du partage, ni une synchronisation précise. Leurs champs NTFS SI du 15 et FN du 28 ne deviennent pas des dates d’extraction matérielle. L16B n’est toujours pas identifié au jeu définitivement saisi.

### 6.2. Appairage ancien TP-03/OP-01

Le nom `00008110-001249321444801E.plist`, déjà relevé dans Apple/Lockdown d’OP-01, correspond à l’UDID exact du manifeste TP-03. La concordance de sa chaîne SHA-256 avec le contrôle antérieur est positive.

La relation de confiance conservée peut désormais être nommée **TP-03**. Les dates du fichier restent **juillet 2022 pour la création SI, décembre 2023 pour FN/modification** ; aucune heure de connexion d’octobre 2024 n’est obtenue. Ce rapprochement n’est pas une preuve d’extraction sous scellé.

### 6.3. Réseau : résultat du contrôle étendu

Les contrôles distinguent les **adresses clientes** des **BSSID de points d’accès**. Les six égalités de champs avec Freebox se ramènent à **trois MAC distinctes** : deux déjà documentées dans TP-02 et une nouvelle dans TP-03, `C6:A2:88:AC:F8:CB`, associée à une fiche de septembre 2025.

Aucune MAC cliente exploitable n’est obtenue pour TP-01 dans les préférences examinées ; aucun champ Wi-Fi matériel n’est disponible dans les en-têtes contrôlés des trois sauvegardes. **Le contrôle ne consiste donc pas à disposer de trois identifiants matériels Wi-Fi complets.**

Les trois identités nocturnes `EA:21:6C:F7:47:E7`, `9C:64:8B:0A:BD:0C`, `FE:AA:76:95:AC:29` restent sans correspondance parmi les adresses clientes disponibles. Cela laisse leur attribution ouverte ; une rotation de MAC ou un état perdu peut supprimer la correspondance. Les SSID et adresses de routeurs ne sont pas utilisés à leur place.

`ASUS_Z01RD` n’est pas présent dans les préférences Wi-Fi TP-01/03 contrôlées. Cela ne transforme pas la séquence TP-02 du 17 en preuve matérielle certaine. OP-01 conserve ce nom dans des listes de réseaux visibles, sans connexion ou date commune établie. Le DESKTOP du 16 reste non identifié.

## 9. Traçabilité et livraison

Scripts sous `telephones/scripts/`, notice [README-TP-01-TP-03.md](../../telephones/scripts/README-TP-01-TP-03.md). Les résultats détaillés sont dans `telephones/recherche-TP-01/`, `telephones/recherche-TP-03/` et `prive/` de cette campagne. Les contenus déchiffrés restent dans les dossiers SIFT identifiés dans les rapports. Les **71 fichiers JSON de résultats rapatriés** ont des SHA-256 identiques à ceux calculés sur SIFT ; les liens locaux des cinq documents de livraison et la syntaxe des onze scripts ont été contrôlés. Le détail est conservé dans `prive/verification-livraison.json`. Ce contrôle de livraison reste distinct de l’analyse historique ; aucun succès de transfert n’est assimilé à une authentification historique de 2024.

Les erreurs de déchiffrement, parseur et limites de schéma sont conservées. Les 116 contrôles SQLite incomplets de TP-03 ne sont pas qualifiés de corruptions ; les 525 écarts MBFile/clair ne sont pas corrigés par troncature. Les références aux dates de programmation, aux mesures Santé, aux contenus cloud et aux transactions sont gardées distinctes.

**La conclusion générale reste proportionnée : des indices techniques supplémentaires existent, notamment le 16 sur TP-03. Ils ne démontrent pas à eux seuls qu’une personne a ouvert ou utilisé un appareil sous scellé.**

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe DOnnat — Donnat Dev
