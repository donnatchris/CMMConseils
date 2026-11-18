# Vérification et extraction des messageries d’OP-01 — 16 novembre 2026

## Portée de la notice

Les sources sont les trois conteneurs présents dans l’image OP-01 ; les destinations sont leurs copies sous `fichiers/`, distinctes de la source montée en lecture seule. Les empreintes avant/après et la relecture des copies contrôlent cette extraction, sans authentifier l’histoire antérieure de l’image. Refaire l’extraction dans un répertoire nouveau, puis recalculer les deux algorithmes sur chaque copie : SHA-256 pour les contrôles de travail, SHA-512 pour la comparaison au CSV. Résultat de référence : PST DMM et Takeout concordants, PST 93300 divergent. Aucun secret ni corps de message n’est publié dans cette notice.

Les trois fichiers recherchés sont encore présents, non supprimés, dans le système de fichiers de l’image OP-01. Ils ont été ouverts et copiés depuis la VM SIFT, avec montage NTFS en lecture seule et loop EWF en lecture seule. Les copies sont conservées sous `fichiers/`, avec l’arborescence source.

| Chemin dans Windows | Taille exacte | Copie |
|---|---:|---|
| `C:\L16B\MESSAGERIES\dmmconseils@hotmail.com.pst` | 2 143 626 240 octets | [PST dmmconseils](fichiers/L16B/MESSAGERIES/dmmconseils@hotmail.com.pst) |
| `C:\L16B\MESSAGERIES\dmmconseils93300@hotmail.com.pst` | 1 156 260 864 octets | [PST dmmconseils93300](fichiers/L16B/MESSAGERIES/dmmconseils93300@hotmail.com.pst) |
| `C:\L16B\MESSAGERIES\rct93300@gmail.com\takeout-20241028T114105Z-001.zip` | 41 828 775 octets | [Archive Takeout](fichiers/L16B/MESSAGERIES/rct93300@gmail.com/takeout-20241028T114105Z-001.zip) |

Total extrait : **3 341 715 879 octets**.

La recherche préalable dans le projet local DMMConseils n’a trouvé aucune copie complète de ces PST, du ZIP Takeout ou du MBOX, ni comme fichiers distincts ni comme membres des archives TAR et ZIP examinées. Les inventaires, le manifeste Takeout, des raccourcis et les résultats d’analyses antérieurs étaient disponibles. Le détail et le périmètre de cette recherche figurent dans [recherche-extractions-preexistantes.json](recherche-extractions-preexistantes.json).

## Contrôles

Pour chaque fichier, le SHA-256 calculé pendant la lecture de la source concorde avec celui recalculé par relecture intégrale de la copie et avec l’empreinte du contrôle antérieur conservé dans `investigations/20261109-controle-l16b-photos/prive/controle-sift.json`. Les tailles, inodes et dates de modification de la source sont restés identiques pendant l’extraction. Les signatures des deux PST ont été vérifiées ; aucun nouveau décodage complet des PST n’a été effectué.

Les deux membres du ZIP Takeout se décompressent intégralement sans erreur CRC : `Takeout/Mail/L16.mbox` (66 015 300 octets) et `Takeout/archive_browser.html` (197 837 octets). Leurs SHA-256 sont consignés dans le rapport technique.

- [Présence constatée directement sur SIFT](presence-sift.json).
- [Rapport technique et empreintes source/copie](verification-extraction.json).
- [Empreintes SHA-256 des fichiers extraits](SHA256SUMS).
- [Journal filtré du montage](montage-sift.txt).
- [Script d’extraction reproductible, sans écrasement](extraire_sift.py).

Commande d’extraction utilisée après montage :

```sh
ssh -F /home/chris/.ssh/config -o BatchMode=yes sift 'python3 /media/shared/codeProjects/DMMConseils/ordinateur/recherche-OP-01/extraction-messageries-20261116/extraire_sift.py'
```

Le choix explicite de la configuration SSH utilisateur évite une erreur de permissions rencontrée dans la configuration SSH système. Le script refuse un montage NTFS ou loop non protégé en lecture seule et refuse d’écraser une copie existante.

## Portée

La présence et la récupérabilité des trois fichiers dans l’image acquise sont confirmées. Une recherche de versions supprimées n’était pas nécessaire pour les retrouver et aucune recherche exhaustive de telles versions n’a été effectuée. Ce contrôle ne certifie pas la composition des fichiers définitivement emportés par l’administration en 2024, ni l’exhaustivité des boîtes de messagerie serveur.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe DOnnat — Donnat Dev
