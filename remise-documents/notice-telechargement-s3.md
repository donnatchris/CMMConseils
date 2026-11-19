# Télécharger la copie mise à disposition sur S3

Cette notice accompagne le bordereau du 17 novembre 2026. Elle remplace le renvoi à `note-s3.md`, absent du dossier. Le fichier interne de configuration S3 est réservé aux accès ; aucun de ses identifiants n’est reproduit ici. La rédaction de cette notice n’est ni un contrôle distant ni un téléchargement exécuté.

## Configuration séparée

Installer AWS CLI v2 et disposer des identifiants communiqués séparément. Configurer un profil local dédié ; ne pas enregistrer les clés dans le dossier des rapports :

```bash
aws configure --profile ovh-forensic
```

Renseigner la clé d’accès et le secret dans les invites de configuration, la région `sbg` et le format `json`. Le profil peut être nommé autrement sur le poste destinataire en adaptant les commandes.

## Copie vers un dossier neuf

Choisir un disque disposant de l’espace nécessaire et conserver toute l’arborescence, notamment chaque segment EWF :

```bash
mkdir -p /CHEMIN/COPIE-NEUVE
aws --profile ovh-forensic --endpoint-url https://s3.sbg.io.cloud.ovh.net --region sbg s3 sync s3://sadedine-2026/SADEDINE-2026/ /CHEMIN/COPIE-NEUVE/ --only-show-errors
```

Remplacer `/CHEMIN/COPIE-NEUVE` par la destination choisie. Cette commande copie depuis S3 sans suppression des objets distants ; elle n’emploie pas `--delete`. Enregistrer le code de retour et la date du téléchargement. Ne pas publier les clés ni les fichiers de configuration AWS avec les rapports.

## Contrôle et portée de la remise

Comparer les tailles et empreintes aux manifestes correspondants depuis leur répertoire de référence. Les empreintes des flux d’images EWF concernent le disque reconstitué, celles des segments leurs fichiers individuels. Les manifestes historiques restent attachés à leurs versions datées ; la livraison documentaire révisée possède son propre manifeste.

La confirmation du prestataire que le stockage est complet, la possibilité de téléchargement, le contrôle cryptographique des objets et l’achèvement d’une copie chez la cliente sont quatre constats distincts. Cette notice ne certifie aucun téléchargement intégral. Aucun disque dur n’avait été remis à la cliente à la date du bordereau ; une remise ultérieure doit être documentée séparément.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe Donnat — Donnat Dev
