# Protocole de reproduction des doublons et des métadonnées

## Statut : protocole non exécuté

Les scénarios et observations attendues ci-dessous sont des critères d’expérience, pas des résultats de l’affaire. Utiliser des appareils témoins et des données de laboratoire, avec versions iOS et états de protection documentés. Comparer séparément synchronisation de mot de passe, transport complet d’historique et accès à un contenu de classe C avant/après première authentification. Une reproduction du seul nom ou d’une seule date ne valide pas la chaîne entière. Le résultat discriminant est la reproduction des mêmes champs, dates et transactions avec la destination éteinte au temps source, ou l’impossibilité bornée aux variantes effectivement testées. Aucune expérience sur les appareils de la cliente n’est déduite de cette notice.

Ce protocole reste à exécuter sur des équipements de test. Aucun iPhone de test n’est disponible, selon l’utilisateur. Aucun Windows de test natif n’est connecté à l’environnement de travail. Wine présent sur SIFT n’est pas assimilé à Windows. Les appareils et images de la mission ne doivent pas servir à cette expérimentation.

## Préparer les contrôles

Utiliser un PDF synthétique nommé `Q1-TEST.pdf`, avec son SHA-256 et une date de génération connues. Consigner modèle, version et build exacts de chaque OS, langue, fuseau, paramètres de synchronisation et outil/version. Relever une référence UTC indépendante avant et après chaque série. Filmer les actions et conserver les sorties dans un dossier neuf pour chaque essai.

## Nommage sur iOS

1. Depuis un message de test, enregistrer cinq fois le même PDF vers le même dossier de « Sur mon iPhone » avec Fichiers. Relever les noms proposés et retenus, ainsi que les confirmations demandées.
2. Refaire l’essai vers iCloud Drive, en séparant l’enregistrement répété d’une vraie situation de conflit de synchronisation. Un conflit nécessite un second environnement de test et une procédure de déconnexion/reconnexion explicitement consignée.
3. Tester séparément la fonction Dupliquer de Fichiers, le téléchargement depuis Safari et l’enregistrement depuis Quick Look. Ne pas attribuer à iOS une convention observée dans une seule application.
4. Quand l’accès technique est possible, relever avant/après `Birth`, modification, changement de statut, attributs étendus et classe de protection. Comparer les contenus par empreinte ; un suffixe identique n’établit pas l’identité du contenu.

## Nommage et copie sur Windows

Sur une VM Windows de test et un volume NTFS de test, comparer les copies répétées via l’Explorateur, `Copy-Item`, l’enregistrement d’une pièce jointe et, si son identité est établie, l’outil de transfert suspecté dans sa version pertinente. Conserver les choix de gestion des collisions : écrasement, conservation des deux exemplaires ou erreur.

Pour chaque méthode, relever le nom exact et les heures UTC avec `Get-Item`, l’empreinte avec `Get-FileHash`, les flux nommés avec `Get-Item -Stream *`, puis examiner SI et FN dans une acquisition du seul volume de test. Une modification via `SetFileTime` doit être un essai distinct, annoncé comme tel. Elle peut montrer la possibilité de rétablir des dates, sans identifier l’outil historique.

## Test BFU

Séparer trois scénarios : avant premier déverrouillage après redémarrage, après premier déverrouillage puis verrouillage, et appareil déverrouillé. Pour un fichier de classe C, distinguer une lecture de contenu d’une lecture ou modification de métadonnées. Le seul échec d’ouverture de l’interface Fichiers depuis l’écran verrouillé ne teste pas l’ensemble des opérations système sur les métadonnées.

Un test instrumental BFU exige un moyen validé de déclencher et tracer l’opération avant le premier déverrouillage. Si l’instrumentation ne le permet pas, consigner « non testé » ; ne pas remplacer ce contrôle par une déduction tirée d’une sauvegarde effectuée après déverrouillage. Tout test sur un build différent doit rester une comparaison de comportement, sans certification du comportement d’iOS 17.5.1 sur TP-03 en octobre 2024.

## Critère d’attribution

Un mécanisme ne peut être retenu pour la mission sur le seul nom des doublons. Il faut rapprocher la convention de nommage, le profil SI/FN, les attributs iOS, les empreintes et une trace indépendante du logiciel réellement utilisé. Sans cette concordance, plusieurs mécanismes restent possibles.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe DOnnat — Donnat Dev
