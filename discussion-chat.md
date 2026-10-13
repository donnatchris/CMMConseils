
---

Concernant le PC Windows, Mme Sadedine souhaite principalement déterminer si son ordinateur a été utilisé, consulté ou modifié pendant la période où elle n'en avait plus la possession, et rechercher d'éventuelles traces d'accès non autorisés.

## 1. Les dates essentielles

| Date                    | Événement                                                                        |
| ----------------------- | -------------------------------------------------------------------------------- |
| 15 octobre 2024         | Perquisition fiscale. Elle perd l'accès à son PC dès le début de l'intervention. |
| 28 octobre 2024 à 10h22 | Début de l'ouverture des scellés dans les locaux de l'administration.            |
| 28 octobre 2024 à 19h20 | Restitution des appareils.                                                       |

La période prioritaire d'investigation est donc du 15 au 28 octobre 2024, sans exclure les activités antérieures.

## 2. Ce qu'elle souhaite vérifier sur le PC

| Investigation             | Ce que tu dois rechercher                                                              |
| ------------------------- | -------------------------------------------------------------------------------------- |
| Utilisation du PC         | Démarrages, arrêts, ouvertures et fermetures de sessions Windows.                      |
| Consultation des fichiers | Traces d'ouverture de documents, photos, dossiers et autres fichiers personnels.       |
| Copies et extractions     | Connexions de clés USB ou disques externes, indices de transferts de fichiers.         |
| Modifications             | Fichiers créés, modifiés, déplacés ou supprimés pendant la période.                    |
| Accès à distance          | Traces de RDP, logiciels de prise en main à distance, connexions réseau suspectes.     |
| Logiciels exécutés        | Programmes lancés, outils installés ou désinstallés.                                   |
| Activité Internet         | Historique des navigateurs, téléchargements et éventuelles connexions réseau.          |
| Événements inhabituels    | Effacements de journaux, réinitialisations, changements de configuration ou d'horloge. |

## 3. Ce que tu dois chercher dans ton image forensic

Pour ton analyse avec Autopsy et les outils de Zimmerman, les artefacts Windows particulièrement intéressants seront :

- Windows Event Logs (`.evtx`) : démarrages, sessions, authentifications et événements système.
- MFT et USN Journal : chronologie des créations, modifications et suppressions de fichiers.
- LNK et Jump Lists : traces de documents consultés.
- USBSTOR et SetupAPI : historique des périphériques USB connectés.
- Prefetch, Amcache et ShimCache : indices d'exécution de programmes.
- SRUM et artefacts réseau : indices d'activité applicative et réseau.

Attention : ces artefacts n'établissent pas tous, à eux seuls, qu'une personne a effectué une action. Il faudra les recouper et tenir compte des horodatages.

## 4. Le véritable objectif de l'expertise

Mme Sadedine ne te demande pas seulement de trouver des anomalies. Elle veut pouvoir répondre à trois questions :

1. Son ordinateur a-t-il été utilisé entre le 15 et le 28 octobre 2024 ?
2. Quelles opérations ont été réalisées et à quelles dates ?
3. Peut-on distinguer les opérations normales, celles éventuellement liées à la procédure et celles qui pourraient correspondre à des accès non autorisés ?

Elle souhaite également rechercher d'éventuels accès à distance avant le 15 octobre 2024, notamment depuis 2021/2022 lorsque les traces existent encore.

Ma recommandation pour ton analyse : commence par construire une chronologie détaillée des événements Windows entre le 14 et le 29 octobre 2024, puis élargis les recherches aux années précédentes pour les accès à distance et les connexions de périphériques.

Le livrable le plus utile sera un tableau indiquant pour chaque événement : date et heure, opération détectée, artefact source, interprétation et niveau de certitude.

C'est cette chronologie technique, accompagnée des éléments vérifiables, qui permettra à son avocate d'exploiter éventuellement tes constatations.