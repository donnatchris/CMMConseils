# Complément du 19 octobre 2026

Point d’entrée : [compte-rendu.md](compte-rendu.md). Neuf rapports courants ont été actualisés ; leurs états précédents figurent sous `rapports-avant/`, leurs empreintes avant/après dans `resultats/rapports-modifies.json`.

## Sources et périmètre

- `docs/mail-2.txt`, mail initial et attestation. Le prestataire a confirmé dans la conversation que le **PV n’est pas disponible**. La date « le 15 / le 28 » du branchement reste non précisée.
- OP-01 : image existante, montée en lecture seule dans SIFT, 359 EVTX, corbeille, MFT complète et fichiers Apple/Lockdown.
- TP-02 : manifeste et contenus déjà déchiffrés, préférences Wi-Fi, profils/comptes, états LSC et chronologies antérieures. Aucune nouvelle acquisition ni extraction exhaustive de la sauvegarde.
- SD : inventaires complets déjà produits ; nouvelle agrégation des bornes et unions d’intervalles nominaux. Une image SD-03 existante a été examinée ponctuellement. Pas de nouveau carving général ni de visionnage intégral.
- Freebox : mise à jour du contexte et des rapprochements ; pas de nouvelle collecte réseau.
- TP-01/03 : aucune acquisition identifiée dans le répertoire de preuves SIFT examiné ; pas d’analyse nouvelle de ces appareils.

## Scripts et destinations

Les scripts écrivent dans des **répertoires neufs**, et les sorties de preuve antérieures ne doivent pas être écrasées. Pour une reproduction SIFT, copier les scripts et changer leurs destinations `/home/sansforensics/analysis/complement-20261019/...` vers une nouvelle campagne. La procédure de montage utilise le script RO existant, sans journaliser la clé. Ne pas exécuter les scripts de mise à jour des rapports à répétition : ils insèrent les sections une fois ; les versions antérieures ont été archivées au préalable.

| Script | Opération |
|---|---|
| `scripts/monter_sift.py` | Montage EWF / loop RO / Dislocker -r / NTFS ro,norecover ; clé lue localement, non affichée |
| `scripts/sift_readonly.py` | Dates des 275 577 événements, sélection du 16 au 29, corbeille et métadonnées d’appairage ; SHA-256 avant/après |
| `scripts/sift_xml_fallback.py` | Relecture des 285 rendus XML refusés : dates/identifiants par pyevtx, XML brut conservé, fournisseur obtenu par expression régulière |
| `scripts/mft_after1920.py` | Parcours complet des enregistrements MFT, filtres SI/FN strictement après 18:20 UTC et avant 23:00 UTC le 28, plus le fichier d’appairage sélectionné par son nom |
| `scripts/local_checks.py --out <destination-neuve>` | Couverture SD, union des durées, comparaison corbeille, tri manifeste TP-02, chronologies post-restitution, états LSC |
| `scripts/plist_checks.py` | Contre-lecture Wi-Fi/BSSID, profils/comptes et trois champs de cache LSC ; destination fixée à adapter dans une copie pour reproduction |
| `scripts/update_reports.py` | Mise à jour éditoriale des neuf rapports ; les états précédents sont archivés |
| `scripts/verify.py` | Contrôles de cohérence, empreintes sources locales, liens Markdown du complément et résultats ; pas une acquisition indépendante |

Commande de contre-lecture par second outil, sortie conservée dans `resultats/sift/istat-pairing-113002.txt` :

```sh
ssh -F /home/chris/.ssh/config sift 'sudo -n istat /mnt/dislocker/dislocker-file 113002'
```

Reproduction de la partie locale, depuis la racine du projet :

```sh
python3 investigations/20261019-retour-cliente/scripts/local_checks.py --out /tmp/cmm-retour-client-reproduction-neuve
```

## Résultats de référence

- `resultats/local-v2/` est la version retenue : le filtre est strictement postérieur à 19:20 et exclut le repère déclaratif de restitution. `resultats/local/` conserve la passe initiale, qui incluait ce repère et ne doit pas servir de comptage final. Les lignes des trois chronologies peuvent se recouvrir : **elles ne sont pas autant d’événements indépendants**.
- `resultats/sift/` conserve inventaires, événements, erreurs, empreintes et corbeille ; `xml-fallback/` complète les résultats XML stricts. Les 285 erreurs sont des erreurs de rendu/interprétation XML, pas des dates manquantes dans le contrôle repris.
- `resultats/sift/mft-apres1920/` contient cinq fichiers iCloud et un fichier d’appairage sélectionné séparément. Les dates anciennes iCloud ne datent pas une utilisation locale de Windows.
- `resultats/plists/` contient les nouveaux contrôles directs des états Wi-Fi, profils/comptes et LSC. Aucune clé privée, certificat privé ou mot de passe n’a été copié dans les rapports.
- `resultats/verification.json`, `SHA256SUMS.txt` et `resultats/rapports-modifies.json` documentent la livraison courante. Les anciens manifestes décrivent leurs versions historiques, pas les nouveaux rapports.

Les fichiers de résultats sont privés au prestataire et à la cliente. Aucun mail envoyé, compte externe connecté, fichier publié, upload cloud ou copie sur disque client effectué par cette campagne. La conservation contractuelle et les lacunes de copie documentées le 17 restent distinctes.
