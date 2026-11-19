# Méthodes, reproductibilité et limites

Campagne du 14 octobre 2026, limitée aux clocks et à l'attribution temporelle. Aucun accès distant au téléphone, aucune acquisition, aucun déchiffrement nouveau. Les seuls téléchargements concernent des sources publiques Apple, sans transmission de preuve. Le rapport `telephones/analyse-TP-02.md` a été consulté et son empreinte contrôlée ; il n'a pas été modifié.

## Traitements exécutés

1. Lecture des journaux d'extractions existants pour retrouver les preuves par fileID ; ensemble des 312 IPS comparé à l'inventaire précédent, puis parsing direct des deux enveloppes de chacun. Aucune durée du précédent script n'est reprise comme donnée primaire.
2. Conservation des dates/offsets et compteurs bruts ; différences civiles en datetime/Decimal, ticks en entiers puis modèles de conversion explicitement nommés.
3. Contrôle séparé du second parseur (première ligne/reste), de GNU date pour les dates et fractions exactes pour les ticks. Même preuve, même hypothèse 24 MHz : deux calculs, **pas deux sources indépendantes de validation historique**.
4. Manifeste copié avec compagnons dans `/tmp`, recherche de chemins ciblés ; SQLite ouverte seulement sur copies, `query_only=ON`. Aucun `immutable` sur les bases de preuve ni ouverture source susceptible de créer un SHM.
5. Recherche bornée des marqueurs clocks dans les fichiers Apple/système déjà déchiffrés <=32 Mio, puis résolution des quatre hits. Pas de balayage général des médias, conversations ou activités de la sauvegarde.
6. Relecture SQL ciblée des créations/transactions des 17 et 28, plus snapshots Wi-Fi et références CommCenter. Conservation de dates d'intervalles Santé séparées ; aucun payload personnel exporté. Contrôle de conversion de la chronologie antérieure.
7. Empreintes des sources avant/après et comparaison aux journaux d'extraction ; manifeste et rapport principal inclus. Contrôle indépendant et reproduction dans une destination distincte.

Environnement : `3.14.4 (main, Aug 20 2026, 10:41:58) [GCC 15.2.0]` ; SQLite `3.46.1` ; `Linux-7.0.0-38-generic-x86_64-inconnu-with-glibc2.43` ; `# version 2026c` ; Decimal précision 40. GNU date et SHA des scripts : `independent-verification.json` et `analysis-operations.json`. Versions des sources publiques : tags et snapshots dans `sources/`.

## Modèles de conversion et résultat nouveau

Formule générale : `secondes = ticks × numer / denom / 10^9`. Le modèle 24 MHz correspond à `numer/denom=125/3` ns/tick ; **cette fraction est calculée sous l'hypothèse, pas mesurée dans le diagnostic**. Nanosecondes déjà converties, microsecondes et secondes ont été testées comme lectures concurrentes et obtiennent zéro correspondance aux tranches empiriques d'uptime sur 312.

Le modèle d'uptime est une **troncature**, pas un arrondi au plus proche : si `u` a deux chiffres significatifs et un quantum `q`, `u <= exit_ticks/f < u+q`. À 24 MHz, 312/312 correspondances ; pour WidgetKit q=100. Intersection conditionnelle des fréquences admissibles : **]23998227.24551315789473684210526315789474, 24000335.76234042553191489361702127659574] unités/s**. Elle suppose même origine, même instant de référence et cette règle de présentation ; elle ne représente ni une mesure matérielle exacte ni un intervalle statistique de confiance. Les 53 cas courts 0,1–10 s de la même clé donnent une médiane de 23 852 839,227 unités/s civiles ; latence de capture/sortie et petite durée rendent ce quotient bruité et ne justifient pas d'en faire une fréquence exacte.

Les neuf lignes PlaybackEventStreams fournissent un contrôle local différent et hors octobre : colonnes compatibles avec absolute/ticks et continuous/ns ; les incréments longs sans sommeil sont proches de 24 MHz. Le schéma additive `monoTimebaseNS` ne fournit pas la fraction Mach. Leurs dates candidates et résidus sont conservés, sans certifier leur API ni leur horloge historique.

## Corpus : comparaison et biais

312 rapports, zéro erreur ; toutes les durées civiles et différences de compteurs positives ; incidents/bundles concordants 312/312 ; schéma v2, type 309 et modèle iPhone14,4 pour tous. Huit builds : 21E236 (79), 21F90 (73), 21G93 (40), 22B91 (34), 22D72 (15), 22D82 (23), 22E252 (7), 22F76 (41). Deux clés diagnostiques hachées : 88 et 224 rapports ; la comparaison globale et celle de la clé WidgetKit sont séparées.

| Groupe | n | Médiane civile (s) | Médiane ratio civil/24MHz | Maximum ratio |
|---|---:|---:|---:|---:|
| application | 177 | 20.4788 | 1.10798 | 15.5212 |
| extension | 116 | 1.92425 | 1.01006 | 532.059 |
| service_systeme | 19 | 6205.26 | 1.69603 | 10.0925 |
| intermediaire_10_100s | 64 | 20.9526 | 1.00033 | 1.01868 |
| long_plus_100s | 98 | 9318.12 | 2.39854 | 532.059 |
| tres_court_0_10s | 150 | 0.0898 | 1.01711 | 1.71776 |


Les catégories sont dérivées du chemin (.appex/.app/autre), sans déduire qu'une application est tierce ni qu'un service était réellement suspendu. **Aucun groupe de processus dont la suspension serait directement observée ne peut être constitué** ; le CSV porte `suspension_observed=non_documentee`. Le rôle instantané ne remplace pas un historique de suspension. Les classes temporelles sont civiles et non physiologiques.

98 cas >100 s dans tout le corpus, 71 de la même clé ; WidgetKit est premier dans les deux comparaisons, ratio 532,059 ; deuxième 15,521. Les durées très courtes ont des quotients sensibles à la latence et à la précision d'impression ; quelques ratios légèrement <1 ne prouvent pas une inversion d'horloge. Voir `ips-distributions.json` (quartiles/rangs, groupes par build/rôle/clé) et `ips-comparison.csv` (312 lignes et valeurs brutes). Rapports sélectionnés parce qu'ils existent dans une sauvegarde et concernent des diagnostics : **échantillon non représentatif du fonctionnement général iOS**, sans distribution témoin de onze jours de veille. L'exception statistique n'est pas un test de cause ni une probabilité H1/H2.

## Reproduire sans réécrire cette campagne

Depuis `/home/chris/codeProjects/CMMConseils`, choisir une destination neuve accessible, puis :

```sh
python3 telephones/recherche-TP-02/investigation-horloges-widgetkit/analyze_clocks.py --out /tmp/tp02-clock-reproduction
python3 telephones/recherche-TP-02/investigation-horloges-widgetkit/verify_independently.py --out /tmp/tp02-clock-reproduction
python3 telephones/recherche-TP-02/investigation-horloges-widgetkit/recheck_sequences.py --out /tmp/tp02-clock-reproduction
python3 telephones/recherche-TP-02/investigation-horloges-widgetkit/inspect_clock_markers.py --out /tmp/tp02-clock-reproduction
python3 telephones/recherche-TP-02/investigation-horloges-widgetkit/write_reports.py --out /tmp/tp02-clock-reproduction
```

Les scripts écrivent leurs propres résultats à `--out` ; ils ne doivent pas être lancés avec une destination contenant des preuves sources. Les preuves existantes restent aux chemins des journaux d'extraction ; le manifeste déjà déchiffré est requis au chemin déclaré dans le script. Aucune dépendance Python supplémentaire, aucun mot de passe, aucun secret dans les commandes. GNU date et zoneinfo/tzdata nécessaires. Les snapshots Apple ne nécessitent pas de réseau pour reproduire les calculs ; `fetch_sources.py` permet seulement une récupération publique séparée, dont un contenu changé n'écrase pas la preuve de consultation initiale si l'on choisit une autre destination.

Les journaux `analysis-run.log`, `verification-run.log`, `sequence-run.log`, `markers-run.log`, `reproduction-check.json` et `deliverable-verification.json` décrivent les passes réussies. Les ajustements de script avant clôture ont concerné le filtrage de faux positifs et la conservation de procLaunch, jamais les preuves. `SHA256SUMS` scelle les livrables et snapshots (hors son propre fichier) ; contrôle : `sha256sum -c SHA256SUMS` depuis ce dossier. Ce scellement est une vérification locale, pas une signature d'authenticité d'Apple.

## Critères d'arrêt et reliquats

Fraction exacte, contrat IPS des AbsTime, compteur continuous d'octobre, résidence/sommeil effectifs et événement de correction historique absents. Pas de date physique de boot calculée à partir de capture−uptime. Les champs privés non documentés sont marqués incertains. Les marqueurs hors octobre ne datent pas TP-02 pendant la rétention. Aucun résultat négatif n'est étendu à l'ensemble non déchiffré de la sauvegarde. Aucun classement causal arbitraire ni attribution d'opérateur. L'incidence Wi-Fi est explicitée dans le livrable dédié ; la compréhension des nombres a atteint le niveau vérifiable disponible.
