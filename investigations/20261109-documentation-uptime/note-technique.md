# TP-02 — portée du champ uptime et documentation Apple

Précision documentaire du 9 novembre 2026, fondée sur les références Apple consultées et les résultats techniques déjà conservés. Aucune nouvelle acquisition du téléphone.

## Définition documentée et distinction des horloges

Apple décrit le champ JSON `uptime` d’un rapport de crash comme une durée en secondes depuis le démarrage et indique son libellé de présentation **« Time Awake Since Boot »**, soit temps d’éveil depuis le démarrage. Source : [Interpreting the JSON format of a crash report](https://developer.apple.com/documentation/xcode/interpreting-the-json-format-of-a-crash-report).

Apple documente par ailleurs deux compteurs Mach distincts :

| Compteur | Comportement pendant le sommeil système |
|---|---|
| `mach_absolute_time` | Ne progresse pas pendant le sommeil système. |
| `mach_continuous_time` | Progresse également pendant le sommeil système. |

Source : [Apple Developer — C++ Runtime Support, rubrique Mach Timebase](https://developer.apple.com/documentation/driverkit/c-runtime-support). Ces définitions sont aussi cohérentes avec le code XNU étudié dans la [campagne horloges](../../telephones/recherche-TP-02/investigation-horloges-widgetkit/apple-clock-semantics.md).

Le sommeil système est distinct du simple verrouillage ou de l’extinction de l’écran. Le temps d’éveil n’est ni le temps d’écran allumé, ni une durée de manipulation humaine.

## Application au diagnostic conservé

Le diagnostic WidgetKit porte `captureTime=2024-10-28 12:26:28.7192 +0100` et `uptime=2500`. Cette dernière valeur est exprimée en secondes, soit **41 minutes et 40 secondes** dans sa présentation.

Les contrôles antérieurs des **312 diagnostics** sont compatibles avec une présentation tronquée à deux chiffres significatifs. Sous le modèle étudié, `2500` correspond à la tranche **[2 500 ; 2 600[ secondes**, et la conversion conditionnelle du compteur de sortie donne environ **2 512,667 secondes**. La troncature est un résultat empirique du corpus ; elle n’est pas décrite comme un algorithme garanti par Apple. Voir les [méthodes et résultats conservés](../../telephones/recherche-TP-02/investigation-horloges-widgetkit/methodes-et-reproduction.md).

La documentation publique du champ `uptime` ne désigne pas explicitement l’API interne utilisée pour le calculer. Le raccord aux compteurs Mach excluant le sommeil est une **inférence étayée par le code et la cohérence du corpus**, distincte de la définition publique du libellé. La fraction matérielle exacte de conversion n’est pas présente dans le diagnostic.

## Conséquence sur l’heure de démarrage

**La soustraction de 2 500 secondes à l’heure du diagnostic ne permet pas d’établir une heure de démarrage de TP-02 vers 11 h 45.** Il manque notamment la durée de sommeil système et une référence historique de démarrage attribuable au matériel. La précision réduite et les réserves d’horloge/provenance déjà documentées s’ajoutent à cette limite.

Le diagnostic ne permet donc pas d’affirmer que TP-02 a été allumé lors de l’ouverture des scellés à 11 h 30, ni qu’il était auparavant éteint. Le PV consigne un déverrouillage des téléphones après ouverture ; cet acte ne constitue pas une preuve de démarrage.

**Formulation retenue :** « Le diagnostic du 28 octobre à 12 h 26 conserve un uptime de 2 500 secondes, présenté par Apple comme un temps d’éveil depuis le démarrage. Cette valeur ne suffit pas à dater le démarrage physique de TP-02 ni à déterminer son état d’alimentation avant l’ouverture des scellés. »
