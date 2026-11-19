# Horloges Apple : définitions, code et limites d'application

Les sources publiques consultées le 14 octobre 2026 sont conservées sous `sources/`, avec URL, date de récupération et SHA-256 dans [sources/fetch-log.json](sources/fetch-log.json). Documentation actuelle et code publié ne constituent pas une inspection du binaire CrashReporter de TP-02 sous 21G93. Les tags XNU `xnu-10063.121.3` et Libc `Libc-1534.100.14` servent de références vérifiables ; leur identité exacte avec les composants exécutés sur ce téléphone n'est pas établie ici.

## Contrats documentés

La [documentation Apple du JSON IPS](https://developer.apple.com/documentation/xcode/interpreting-the-json-format-of-a-crash-report) définit `procLaunch` comme date de lancement et `captureTime` comme date du crash. `timestamp` est destiné au suivi du rapport. `uptime` est en secondes et s'affiche comme « Time Awake Since Boot ». Elle décrit deux objets JSON et le type 309. Elle ne définit pas les deux champs `proc…AbsTime`, leur conversion ni l'algorithme de réduction de précision d'uptime. La clé diagnostique est un identifiant anonymisé par appareil, réinitialisé à l'effacement ; un rapport archivé conserve néanmoins sa valeur lors d'une copie.

La [documentation Mach](https://developer.apple.com/documentation/kernel/mach) distingue `mach_absolute_time` (ticks monotones, arrêt pendant le sommeil système) et `mach_continuous_time` (ticks monotones incluant le sommeil). La fraction `numer/denom` de `mach_timebase_info` convertit les ticks en nanosecondes : `ns = ticks × numer / denom`. Une fréquence de CPU ou la seule mention ARM-64 ne remplace pas cette fraction. Ces API ne donnent pas directement une date civile.

## Implémentations publiques pertinentes

| Source primaire conservée | Observation vérifiable | Portée |
|---|---|---|
| [XNU kern_fork.c](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/bsd/kern/kern_fork.c), lignes 1124–1132 | Création : `microtime_with_abstime` remplit `p_start` et `ps_start`. Cas `in_exec` : conservation des départs du processus antérieur. | Deux référentiels conservés ; une date de naissance du processus peut précéder un nouvel exec. Cela ne démontre aucun exec particulier de WidgetKit. |
| [XNU kern_time.c](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/bsd/kern/kern_time.c), fonction `microtime_with_abstime` | Appel de `clock_get_calendar_absolute_and_microtime`, obtention conjointe civil/absolu. | Une correction ultérieure de calendrier n'oblige pas à modifier une date de départ déjà stockée. |
| [XNU kern_resource.c](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/bsd/kern/kern_resource.c), fonction `gather_rusage_info` | `ri_proc_start_abstime` reçoit `p_stats->ps_start`. | Raccord plausible des compteurs, distinct du temps CPU des ledgers. |
| [XNU kern_exit.c](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/bsd/kern/kern_exit.c), ligne 2062 | `ri_proc_exit_abstime` reçoit `mach_absolute_time()` dans les statistiques de sortie. | Existence d'un mécanisme primaire pertinent ; pas preuve que CrashReporter exporte directement ces champs sans traitement. |
| [XNU resource.h](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/bsd/sys/resource.h) | Champs de départ/sortie en `uint64_t`. | Un rollover 32 bits ne convient pas à ces champs. |
| [XNU rtclock.c ARM](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/osfmk/arm/rtclock.c), `timebase_callback`, `clock_timebase_info` | Fraction construite à partir des paramètres de plateforme ; conversion des ticks en temps. | Aucune constante universelle 24 MHz n'est démontrée par ce code ; la fraction exacte manque dans l'IPS. |
| [Libc clock_gettime.c](https://github.com/apple-oss-distributions/Libc/blob/Libc-1534.100.14/gen/clock_gettime.c) | `CLOCK_UPTIME_RAW` utilise absolute ; `CLOCK_MONOTONIC_RAW` continuous ; REALTIME utilise gettimeofday ; PROCESS_CPUTIME additionne temps user/system. | Darwin ne doit pas être interprété à partir des seuls noms des horloges Linux. CLOCK_MONOTONIC emprunte calendrier moins boottime dans cette implémentation. |

Le [code XNU clock.c](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/osfmk/kern/clock.c) permet de distinguer mise à jour de calendrier, ajout du sommeil au calendrier et temps continu. `clock_set_calendar_microtime` modifie époque/offset et ajuste aussi le boottime civil ; `clock_get_uptime` retourne absolute. `mach_continuous_time` utilise selon configuration une horloge matérielle continue ou absolute augmenté du sommeil cumulé. Ces observations expliquent pourquoi une référence de boot civile peut elle-même dépendre de corrections et pourquoi `captureTime − uptime` est injustifié ici. Elles ne désignent pas l'API interne utilisée par chaque champ IPS.

## Effets à ne pas confondre

| Mécanisme | Conséquence possible dans le modèle examiné |
|---|---|
| Suspension/freeze d'un processus, système éveillé | Le processus consomme peu ou pas de CPU ; le compteur global absolute continue. La suspension seule ne justifie pas 10,84 jours pour 1 760 s de compteur global. |
| Sommeil système, sans reboot, processus conservé | Absolute s'arrête ; continuous et calendrier tiennent compte du sommeil. Un long écart civil peut exister sans mauvaise date. |
| Correction de date manuelle ou automatique par saut | Une ancienne date de départ stockée peut coexister avec une capture au calendrier corrigé ; les compteurs monotones ne subissent pas le même saut civil. |
| Correction progressive NTP | Ajustement de vitesse/phase du calendrier ; ne se confond pas avec un saut de plusieurs jours. |
| Changement de fuseau / heure saisonnière | Change la représentation locale ; après prise en compte des offsets conservés, n'explique pas les dix jours. |
| Redémarrage / extinction réelle | Le processus ordinaire ne reste pas vivant dans le nouveau noyau. Un fichier IPS déjà écrit peut subsister ; sa présence ne prouve pas la continuité d'un processus sur le matériel de sauvegarde. |
| Restauration / copie | Des fichiers, dates et historiques peuvent être hérités. La copie d'un rapport ne crée pas à elle seule sa divergence interne. Une reprise d'un processus vivant après restauration ne doit pas être postulée. |

Dans [timex.h](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/bsd/sys/timex.h), MAXFREQ est 500 000 ns/s, soit 500 ppm, MAXPHASE 500 000 000 ns. Le [code de discipline NTP](https://github.com/apple-oss-distributions/xnu/blob/xnu-10063.121.3/bsd/kern/kern_ntptime.c) applique des bornes. La seule correction de fréquence à cette limite représente environ 0,88 s sur 1 760 s, pas 934 881 s ; ce calcul ne borne pas tous les appels de mise à l'heure possibles. Un grand saut par mise à l'heure reste techniquement distinct et possible, sans événement NTP observé ici.

[Apple, cycle des widgets](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date) indique que l'affichage est rendu dans un autre processus et que l'extension n'est pas continuellement active. [Apple, réseau des extensions](https://developer.apple.com/documentation/widgetkit/making-network-requests-in-a-widget-extension) décrit des ressources et temps d'exécution limités et un arrêt possible par le système. Cela rend l'inactivité d'une extension attendue, mais ne garantit ni la conservation du même processus onze jours ni son arrêt automatique à une échéance précise sous iOS 17.6.1. Aucun journal de suspension/résidence de ce processus n'est disponible.

Le raccord `IPS AbsTime → rusage XNU → mach_absolute_time` est une **inférence appuyée par code et corpus**, pas une définition obtenue du seul suffixe. Les conclusions restent explicitement conditionnelles à ce raccord. Aucun article forensic secondaire n'est utilisé pour combler cette lacune de définition.
