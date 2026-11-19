# WidgetKit : lecture directe de l'IPS

Campagne exécutée le 14 octobre 2026. Les dates d'octobre 2024 ci-dessous sont des valeurs des preuves, pas des dates d'investigation.

Source : `SysSharedContainerDomain-systemgroup.com.apple.osanalytics/DiagnosticReports/WidgetKitExtension-2024-10-28-122629.ips`, fileID `daf74a189f4b8e8e71c8e3a2feb211d940ca875c`. Le fichier déchiffré déjà disponible a été relu intégralement ; il contient deux objets JSON successifs, sans erreur de syntaxe ni texte résiduel.

SHA-256 clair : `a6da7e464e750a2961b3c315458f39be5abaf8966cb865ac014ea6b6f3a89ed0`.
SHA-256 objet chiffré : `a1dd285d7ed1577938599d0a3547c8809cfb253e1bdc08414df9463c4d594aee`.
Contrôles actuels conformes aux extractions antérieures, avant/après identiques. L'empreinte contrôle l'intégrité de l'objet disponible ; elle ne certifie pas la justesse de sa date ni son origine matérielle historique.

## Propriétés temporelles

| Localisation / propriété | Valeur brute | Type et unité | Référentiel / conversion / limite |
|---|---|---|---|
| En-tête `timestamp` | `2024-10-28 12:26:29.00 +0100` | Chaîne JSON, date civile avec offset | UTC 11:26:29 ; suivi de rapport ; +0,2808 s après capture ; pas une nouvelle mesure indépendante de l'événement. |
| Corps `procLaunch` | `2024-10-17 17:15:46.8308 +0200` | Chaîne JSON, date civile avec offset | UTC 15:15:46.830800 ; lancement indiqué ; exactitude de l'horloge au lancement non établie. |
| Corps `captureTime` | `2024-10-28 12:26:28.7192 +0100` | Chaîne JSON, date civile avec offset | UTC 11:26:28.719200 ; capture du crash indiquée ; pas un étalon extérieur. |
| Corps `uptime` | `2500` | Nombre JSON entier ; secondes documentées | Durée système présentée ; le corpus suggère une troncature à deux chiffres significatifs ; aucune date de boot calculée. |
| Corps `procStartAbsTime` | `18054155057` | Nombre JSON entier ; ticks hypothétiques | Compteur de départ ; correspondance aux statistiques XNU plausible, pas contrat IPS public démontré. |
| Corps `procExitAbsTime` | `60303998486` | Nombre JSON entier ; ticks hypothétiques | Compteur de sortie ; même origine attendue sous le modèle XNU ; aucun boot UUID pour la vérifier directement. |
| Corps `wasUnlockedSinceBoot` | `1` | Nombre JSON entier, indicateur | État compatible avec un déverrouillage antérieur dans cette session ; ni durée ni date ; sémantique privée non complètement validée. |
| Corps `throttleTimeout` | `10` | Nombre JSON entier ; unité non validée | Paramètre de diagnostic ; pas une durée de vie ni une mesure de sommeil retenue. |
| Corps `isLocked` | `1` | Nombre JSON entier, indicateur | État conservé à la capture ; ne date pas le verrouillage ni l'état du 17. |

Le rapport ne fournit ni fraction `mach_timebase_info`, ni compteur continu de capture, ni total de sommeil, ni historique de correction, ni référence civile de boot, ni `bootSessionUUID`. Aucun temps CPU cumulé exploitable n'a été identifié. Les huit candidats temporels détectés par parcours structurel sont conservés dans [widgetkit-raw-fields.json](widgetkit-raw-fields.json), avec la liste complète des clés ; `isLocked` est conservé dans le contexte technique. Les propriétés de versions/builds et de déploiement ne deviennent pas des dates par leur nom.

Les offsets +02:00 et +01:00 sont explicitement utilisés. Ils sont compatibles avec Europe/Paris avant/après le passage à l'heure d'hiver du 27 octobre 2024 ; cela ne prouve pas que le fuseau était automatique ou que la date civile était correcte. La soustraction sans offsets donnerait 932 041,8884 s, soit une erreur de 3 600 s. Avec offsets : **936 641,8884 s**, environ **10,84076 jours**. La précision d'affichage à 0,0001 s n'est pas une précision forensic certifiée.

## Cohérence structurelle et attribution

`bug_type=309`, schéma `version=2`, `platform=2`, ARM-64, `iPhone14,4`, iOS 17.6.1/21G93. Le bundle est `com.google.GoogleDigitalEditions.WidgetKitExtension` : extension Google News. Parent `launchd`, PID parent 1, rôle `Unspecified`. Exception `EXC_BAD_ACCESS`/`SIGSEGV`, adresse 0x10 ; terminaison SIGNAL 11. Pas de drapeau de simulation/corpse/non-fatal dans ce corps. Ces constats ne constituent pas une analyse symboliquée de la cause du crash.

Incident et bundle concordent entre les deux enveloppes, comme dans les 312 rapports. Le nom du fichier et son en-tête situent le suivi le 28. Les métadonnées MBFile du manifeste sont `Birth=1730114790`, `LastModified=1730114800`, `LastStatusChange=1730114800`, taille 21 882 octets. Sous epoch Unix : 28 octobre 11:26:30 et 11:26:40 UTC, respectivement +1,2808 et +11,2808 s après capture. C'est une cohérence avec l'écriture du rapport ; des métadonnées de fichier transportables ne sont pas un horodatage radio externe.

La clé diagnostique, publiée uniquement sous SHA-256, est commune à 224 rapports. Aucun UDID ou numéro de série discriminant n'est présent dans ce diagnostic. Le modèle n'identifie pas TP-02 individuellement. La proximité avec Santé à 17:15:48 et les traitements à 17:16 renforce un rapprochement de valeurs civiles ; elle ne calibre pas cette horloge.

Les définitions documentées et le raccord XNU conditionnel sont détaillés dans [apple-clock-semantics.md](apple-clock-semantics.md). Les deux implémentations de calcul vérifient les conversions, pas la date réelle.
