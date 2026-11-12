# OP-01 — Complément ciblé : opérations du 28 octobre 2024

Intervention du 14 octobre 2026. Mission privée, contexte relu dans `docs/mail.txt` et l’attestation de remise. Ce complément distingue les constatations nouvelles des reprises des campagnes précédentes. Les heures du tableau sont en Europe/Paris (UTC+1 le 28 octobre 2024). Les CSV et JSON gardent les dates UTC.

**Relecture documentaire du 12 novembre 2026 :** la campagne technique du 14 octobre n’est pas rejouée. Le PV est désormais consulté ; les repères de procédure et les suites documentaires ci-dessous sont harmonisés avec le [rapport final](../../../RAPPORT-FINAL-SADEDINE-2026.md). Le détail de la relecture et les empreintes actuelles figurent dans le [dossier de relecture](../../../investigations/20261112-coherence-rapports/compte-rendu.md).

## Résultat principal

Le décodage des Jump Lists complète les références LNK existantes avec des références concrètes à un volume **KINGSTON, numéro de système de fichiers `140B8328`**, et aux chemins **`E:\saddedine\Archive_saddedine.zip`**, **`E:\saddedine\Inventaire_saddedine.csv`** et **`E:\saddedine\Rejets_saddedine.txt`**. Des dernières interactions DestList sont datées entre **17:26:19 et 17:27:29 Paris**, le 28 octobre. Ce numéro de volume n’est pas le numéro de série matériel USB. Son rattachement à l’un des trois supports Kingston reste à établir.

Ces références sont des pistes de recherche précises pour le procès-verbal et les supports. Elles ne démontrent ni le contenu du ZIP, ni son intégrité, ni une copie de L16B ou des PST dans cette archive, ni l’identité de l’opérateur. Le ZIP lui-même n’a pas été récupéré dans cette campagne. Le LNK embarqué indique une taille de cible de **3 525 227 798 octets** pour le ZIP et **527 208 octets** pour l’inventaire ; ces tailles sont mémorisées, pas mesurées sur les fichiers externes. Les raccourcis autonomes `Archive_saddedine.lnk`, `Inventaire_saddedine.lnk` et `Rejets_saddedine.lnk`, déjà présents dans `integrite-evtx/independent/results.jsonl`, corroborent les chemins et les dates d’interaction.

## Montage et préservation

Connexion effectuée par `ssh sift`. Consignes `/media/shared/AGENTS.md` lues. Script `ordinateur/scripts/remonter_op01.sh` exécuté : EWF, loop `/dev/loop14` en lecture seule, déverrouillage Dislocker `-r`, NTFS `ro,norecover`. Vérification finale : `/mnt/windows` monté `ro` et loop `RO=1`. Aucun démarrage du Windows acquis.

Deux corrections de relance du script : contrôler le caractère RO du loop existant plutôt qu’utiliser `losetup --read-only` hors création, puis attendre `udevadm settle` avant de contrôler le nœud de partition. La clé BitLocker n’est reproduite ni dans ce document ni dans les scripts.

Copies de travail conservées sur SIFT : `/home/sansforensics/analysis/OP-01/operations-28oct-20261014/`. Le manifeste `resultats-sift/sources.json` contient 110 sources avec taille et SHA-256 : 107 Jump Lists, deux PST et `$LogFile`. Les bases cloud ont un manifeste distinct. Pas de vérification intégrale EWF supplémentaire effectuée ici.

## Chronologie technique et repères du procès-verbal

| Heure Paris | Élément | Nature et limite |
|---|---|---|
| 10:22 | Arrivée de la cliente | PV consulté depuis le 8 novembre ; ce n’est pas l’ouverture du PC. |
| 10:41 ; 10:41:56 | Ouverture du PC au PV ; reprise Windows | Concordance à la minute ; pas de nouvel examen de l’image dans cette relecture. |
| 10:47:55–11:11:10 | Créations FN de 1 389 fichiers `L16B/LOCAL` | Campagne précédente ; métadonnées de fichiers, pas auteur. |
| 12:42:33 | Date d’export affichée dans le manifeste Takeout | Campagne précédente ; ne prouve pas une demande depuis OP-01. |
| **13:02:47.994** | FN création de `dmmconseils@hotmail.com.pst` | MFT 98840 ; présence/création locale, pas date des messages. |
| **13:25:53–13:39:04** | Dernières interactions avec des EML sous `L16B/MESSAGERIES/fint.ms@hotmail.com` | Nouveau : plusieurs applications/entrées peuvent référencer les mêmes fichiers. |
| **13:46:16–13:57:41** | Dernières interactions avec des EML sous `L16B/MESSAGERIES/misssmalika@hotmail.com` | Nouveau : trace d’interaction Shell/application ; ne démontre pas la lecture humaine de chaque message. |
| 14:50:40–14:50:46 | Créations FN des 93 fichiers GDRIVE développés | Campagne précédente ; correspondances de contenu documentées au § 11 du rapport. |
| **15:02:53.476** | Dernière modification SI de `dmmconseils@hotmail.com.pst` | Ne certifie pas une fin d’export Outlook. |
| **15:04:42–15:12:02** | Journal Outlook : synchronisation et 937 éléments ajoutés, puis erreur | Message interne du PST 93300 ; heure du corps sans fuseau, cohérente avec son en-tête à 14:12:02 UTC. Ne localise pas la machine d’origine. |
| **15:35:26.154** | FN création de `dmmconseils93300@hotmail.com.pst` | MFT 31663. |
| 16:27:54.063 | Kingston `E0D55EA493C4F3A178B11467&0` | Début de section SetupAPI, heure locale brute. |
| 17:00:07.167 | Kingston `E0D55EA49333E49089B402AD&0` | Même limite ; pas une preuve de copie. |
| 17:14:51.903 | Kingston `0026188879D7F250D72E0E88&0` | Même limite. |
| **17:26:19.314–.330** | `E:\saddedine` et `Rejets_saddedine.txt` | DestList ; volume KINGSTON `140B8328`. |
| **17:26:33.886–.933** | `E:\saddedine\Inventaire_saddedine.csv` | Deux Jump Lists concordantes sur le chemin et le volume. |
| **17:27:29.634** | `E:\saddedine\Archive_saddedine.zip` | Dernière interaction DestList ; contenu non récupéré. |
| **17:28:51.353** | Dernière modification SI de `dmmconseils93300@hotmail.com.pst` | Proximité temporelle avec le ZIP ; aucun lien de contenu démontré. |
| 19:20 | Clôture au PV ; restitution approximative déclarée | Le PV consigne la restitution sans heure individuelle de remise. |

Sources : `pst-chronologie.csv`, `kingston-volumes.json`, `resultats-sift/jumplists-targets-standard.json`, les CSV JLECmd standard et les §§ 10–11 du rapport initial. Les événements sont hétérogènes : la proximité temporelle ne prouve pas une chaîne de copie.

## Jump Lists : couverture et validation

JLECmd 1.5.1.0, 107 fichiers des profils `fintm` et `INVITES`. Export standard : **4 351 entrées automatiques**, **187 personnalisées**. Neuf fichiers CustomDestinations sont signalés vides. La tentative `--withDir` rencontre une exception lors de l’export automatique ; elle est conservée pour traçabilité, mais les chiffres et recherches utilisent l’export standard relancé sans cette option.

Filtre documenté dans `scripts/jump_targets.py` : dates contenant le 28/10/2024, chemins L16B/PST ou mention Kingston. Il retient 502 entrées, dont 184 ont `LastModified` au 28 en UTC ; 93 de ces entrées ont un chemin mentionnant L16B. Ce sont des entrées, pas 93 fichiers uniques ni 93 consultations humaines.

Les deux PST sont aussi référencés par deux Jump Lists chacun, avec dernière interaction **le 29 octobre vers 18:36:59 et 18:37:09 Paris**. Ces dernières dates sont postérieures à la restitution déclarée et ne doivent pas être présentées comme des consultations du 28.

Vérification indépendante via `olefile` : dans `5f7b5f1e01b83767.automaticDestinations-ms`, les flux LNK `7b3` et `7b4` contiennent respectivement le nom de l’inventaire et du ZIP, l’étiquette ASCII KINGSTON et les octets du numéro `140B8328`. Les noms figurent aussi dans DestList. Les empreintes des flux sont consignées dans `jumplist-independent-check.json` sur SIFT.

Attention : `SourceCreated`, `SourceModified`, `SourceAccessed` des CSV JLECmd décrivent les copies de travail créées en 2026. Les dates source sont consignées séparément dans `jumplist-source-metadata.json`. Les champs `Target*` sont des métadonnées de cible ; ils ne datent pas directement une consultation. Les créations DestList en série autour de 14:19:48 UTC ne sont pas utilisées comme heures d’ouverture des documents.

## Archives PST

Les deux conteneurs ont été copiés, hachés et décodés avec `readpst` 0.6.76, options `-r -8`, dans deux répertoires distincts. Les messages décodés restent sur SIFT. Les journaux de lecture documentent les éléments traités et ignorés ; `PersonMetadata` comporte notamment 282 et 2 301 éléments ignorés. Le décodage n’est pas une certification exhaustive de toutes les structures ou des éléments supprimés ; l’option `-D` n’a pas été employée.

| Conteneur | Taille | SHA-256 |
|---|---:|---|
| `dmmconseils93300@hotmail.com.pst` | 1 156 260 864 | `06a98a15fe1c9b77a3c1eee0709fd1f5f9bd3f983d7342169e527e61a688d18a` |
| `dmmconseils@hotmail.com.pst` | 2 143 626 240 | `cbc13b5a409585309db8edd7f9532fd69c58c1a48cf66355124a78f11950e8f9` |

La recherche interne automatisée est décrite dans `scripts/pst_summary.py` : comptage par dossier, en-têtes Date et Message-ID, noms de pièces jointes, recherche des fragments `archive_saddedine`, `inventaire_saddedine`, `rejets_saddedine`, `l16b`, `kingston` dans les en-têtes et corps textuels décodés. Elle ne recherche pas le contenu binaire de toutes les pièces jointes. Une date d’en-tête de message ne date pas son export ou son import dans le PST.

**Résultats internes :** 2 039 messages reparsés dans quatre dossiers pour le PST 93300 et 3 836 dans quatre dossiers pour le PST dmm, soit **5 875 messages**. Les éléments contacts, calendriers et autres objets PST ne sont pas inclus dans ce comptage ; ce nombre n’est pas présenté comme une réconciliation exhaustive de chaque objet traité par readpst. Les bornes de dates et SHA-256 des MBOX sont dans `resultats-sift/pst-summary.json`. Aucun fragment `archive_saddedine`, `inventaire_saddedine`, `rejets_saddedine` ou `kingston` n’a été trouvé dans le périmètre textuel recherché. Treize correspondances brutes au fragment court `l16b` ont été contrôlées : séquences encodées et/ou en-têtes opaques, sans lien démontré avec le dossier L16B. Les contextes sont conservés dans `pst-contexts.json`.

**Journal Outlook du 28 :** le dossier `Problèmes de synchronisation` du PST 93300 contient un message dont l’en-tête Date est `28/10/2024 14:12:02 UTC`. Sa pièce RTF indique une synchronisation de boîte à lettres de **15:04:42 à 15:12:02**, un téléchargement depuis `https://outlook.office365.com/mapi/emsmdb/`, **937 éléments ajoutés dans le dossier en mode hors connexion**, puis une erreur **8004010E**, « Ressources système insuffisantes pour cette opération ». Le corps ne précise pas le fuseau ; ses heures sont cohérentes avec Paris et l’en-tête. Le message est conservé dans le PST créé localement à 15:35:26. Il documente un diagnostic Outlook, sans attester à lui seul que la synchronisation a eu lieu sur OP-01, ni qu’elle est complète. La pièce originale est `resultats-sift/sync-20241028.rtf`.

Les neuf autres en-têtes de messages datés du 28 sont dans la réception et les indésirables du PST dmm, entre 03:34:32 et 09:13:01 UTC. Ils peuvent correspondre à des messages reçus côté serveur avant l’ouverture déclarée : ils ne démontrent pas une utilisation d’OP-01 à ces heures. Aucun message du dossier Envoyés décodé n’a un en-tête Date au 28. Ce résultat n’exclut pas d’autres messageries, des messages supprimés/non exportés ou des canaux de transfert différents.

## Caches cloud et journal NTFS

Inventaire ciblé de 5 578 fichiers dans les emplacements OneDrive, Dropbox et les autres emplacements explicitement listés dans `scripts/collect_sift.py`. Aucun fichier trouvé sous les chemins Google DriveFS recherchés ; cela n’exclut pas un usage web de Google Drive ou d’autres emplacements.

Copie de 23 fichiers de bases OneDrive (bases et compagnons WAL/SHM disponibles) et ouverture en lecture seule de neuf bases SQLite. Schémas, comptes de lignes et recherche textuelle de `l16b`, `saddedine`, `140b8328`, `archive_saddedine` conservés dans `cloud-sqlite-triage.json` : **aucune ligne cible**. Plusieurs bases et journaux ont des dates en 2026 ; une date ancienne du fichier principal SQLite n’exclut pas un WAL récent. Aucun décodage exhaustif des journaux ODL ni des caches Dropbox n’est revendiqué. Ce triage ne permet pas de conclure à l’absence d’export ou de synchronisation en 2024.

`$LogFile` : **67 108 864 octets**, SHA-256 `98c2cce814a1b29a6cb957a9eb1ac73fb43e43bced5c63d06a83e1e67a5b8d29`. Contrôle structurel de pages de 4 096 octets : **2 signatures RSTR et 16 382 RCRD**. Les transactions redo/undo n’ont pas été décodées ni datées. La date de fichier affichée en 2019 ne prouve pas que le journal contient uniquement des transactions de 2019. La recherche littérale UTF-16LE des six noms/fragments documentés dans `logfile-triage.json` ne trouve aucune occurrence ; sans décodage des transactions et bornes temporelles, ce résultat ne permet pas d’exclure des opérations du 28. Aucune récupération intégrale de l’espace non alloué effectuée dans cette campagne.

## Confrontation documentaire restant nécessaire

Le PV, non disponible lors de la campagne initiale du 14 octobre, a depuis été consulté le 8 novembre. Il décrit le regroupement L16B, le filtrage, une copie sur une clé USB de l’administration, l’authentification des fichiers et deux CD d’inventaire. L16B reste un dossier informatif laissé sur le PC, distinct du jeu définitivement saisi. Le CD et les fichiers finaux n’ont pas été examinés dans cette mission ; l’existence d’une copie déclarée est documentée, sa composition exacte reste inconnue. Voir la [lecture du PV](../../../investigations/20261108-analyse-pv/compte-rendu.md).

Rechercher dans les inventaires, journaux d’outils et documents complémentaires : identification physique des trois Kingston et de leurs volumes, branchements et éventuels changements de lettres ; création et contenu de `Archive_saddedine.zip`, `Inventaire_saddedine.csv`, `Rejets_saddedine.txt` ; provenance de L16B ; opérations sur les deux comptes PST, Google Takeout et les EML ; heures de fermeture des opérations et de restitution. Obtenir les supports ou images correspondantes pour comparer les empreintes et l’inventaire au contenu d’OP-01.

Une mention au PV documenterait une opération consignée. Le caractère juridiquement autorisé et sa portée nécessitent l’examen des pièces de procédure ; les traces techniques seules ne permettent pas de le trancher.
