# Guide de la campagne du 17 octobre 2026

Lire d’abord le [compte rendu](compte-rendu.md). Les résultats bruts peuvent contenir des identifiants techniques et des noms de fichiers privés ; ce dossier n’est pas destiné à une publication publique.

## Méthode et traçabilité

Les images maîtresses et les extractions historiques n’ont pas été modifiées par les scripts d’analyse. La VM SIFT utilise `/mnt/windows` monté en lecture seule. Les sorties distantes sont conservées dans `/home/sansforensics/analysis/complement-20261017/`. Les copies locales des nouveaux résultats sont dans `resultats/`. Les manifestes `sources.json` enregistrent les empreintes avant/après ; `SHA256SUMS` couvre les fichiers du présent dossier au moment de sa finalisation, sauf lui-même.

Les versions antérieures des rapports modifiés sont préservées dans `rapports-avant/`. Elles incluent les modifications préexistantes de l’utilisateur : aucune remise à zéro Git n’a été faite. Les résultats historiques des campagnes antérieures ne sont pas réécrits.

`recoupements/` est une première sortie conservée pour traçabilité. Son parseur initial ne lisait pas `UserData` des événements SMB ; **utiliser `recoupements-v2/`**, qui corrige ce défaut. Les 1 167 événements de ce résultat agrègent deux exports pouvant contenir des doublons ; ils ne représentent pas 1 167 événements indépendants.

L’analyse EVTX locale utilise python-evtx 0.8.1. Un contrôle des chunks physiques du DHCP complète les chunks déclarés dans l’en-tête : les événements 985/986 sont accessibles dans les chunks physiques supplémentaires. Le contrôle ne transforme pas une absence de résultat en preuve d’absence historique. Le script `evtx_chunks.py` reproduit ce contrôle physique ; sa sortie est identique au contrôle initial. Un premier appel de reproduction utilisait le mauvais niveau d’API (`Evtx.chunks` au lieu de `FileHeader.chunks`) ; corrigé avant production du résultat, il n’a modifié aucune source. Les parcours SIFT utilisent pyregf/pyevtx ; les erreurs et couvertures sont consignées.

La vérification locale compare 51 sources consommées et contrôle notamment 28 extractions TP-02 contre leurs empreintes historiques, ainsi que leurs fichiers chiffrés dans la sauvegarde. Elle ne remplace pas un journal d’acquisition Mac absent ni une certification de toute l’histoire des supports.

### Reproduction locale

Depuis la racine du dépôt, choisir à chaque fois une **nouvelle** destination :

```sh
python3 investigations/20261017-recroisements/scripts/recouper.py --out /tmp/cmm-recouper-nouvel-essai
python3 investigations/20261017-recroisements/scripts/cameras_complement.py --out /tmp/cmm-cameras-nouvel-essai
/tmp/cmm-recroisements-venv/bin/python investigations/20261017-recroisements/scripts/evtx_cibles.py --out /tmp/cmm-evtx-nouvel-essai
python3 investigations/20261017-recroisements/scripts/verifier.py --out /tmp/cmm-verification-nouvel-essai.json
```

Les scripts `cloud_inventaire.py` et `conservation.py` requièrent le profil S3 local et l’accès au stockage d’acquisition ; ils effectuent des inventaires/lectures, pas des transferts. L’inventaire cloud est un constat daté : une nouvelle exécution peut légitimement différer si des transferts ont eu lieu depuis.

### Traitements SIFT

`sift_complement.py` parcourt les ruches complètes accessibles, les journaux PnP/stockage et les MBOX dérivés des deux PST. `zip_complement.py` contrôle la décompression et les SHA-256 des membres des deux archives GDRIVE. `zip_dossier.py` vérifie les membres lisibles contre les 93 fichiers correspondants du dossier GDRIVE, avec empreintes avant/après. `rescue_context.py` conserve le contexte des deux invitations de téléassistance en masquant liens, adresses et codes ; aucun lien n’a été suivi.

`ntfs_complement.py` utilise **dfir_ntfs 1.1.20**, installé dans un répertoire de dépendances isolé, et le CLI `ntfs_parser --log`. Le parseur reconstruit les pages du journal dans une copie en mémoire (`prepare_for_writes`), sans écrire dans le fichier source. Il utilise la MFT contemporaine pour résoudre des chemins ; ces chemins peuvent être erronés si un numéro d’entrée a été réutilisé. Les dates de fichiers embarquées dans redo/undo ne sont pas nécessairement les dates des transactions. Le décodage complet demeure dans la VM ; son empreinte et les résumés sont rapatriés.

Les scripts SIFT contiennent des destinations fixes volontairement protégées contre l’écrasement. Pour les rejouer, conserver les sorties antérieures et adapter les chemins vers une nouvelle campagne. `monter_sift.py` ne doit pas être relancé quand le montage est actif. Lors du montage initial, le terminal a renvoyé des fragments du secret BitLocker malgré un premier masquage insuffisant ; le journal local a été expurgé et le filtrage remplacé par une liste de messages autorisés. Cela n’efface pas rétroactivement la sortie déjà transmise dans la session. Aucun secret n’est reproduit dans le compte rendu ou le manifeste.

## Protocole de référence caméra — préparé, non exécuté

1. Photographier et relever modèle, série, MAC de chaque interface, firmware, application et version ; documenter le lien physique entre caméra et emplacement SD.
2. Employer une caméra de référence et des cartes de test neuves, jamais les cartes originales. Photographier leur état et calculer une image/empreinte initiale.
3. Synchroniser une horloge de référence et filmer son affichage dans le champ ; documenter fuseau, NTP, absence de réseau et heure affichée par l’application.
4. Sur des essais séparés et répétés : enregistrement normal, arrêt propre, coupure d’alimentation pendant un clip, redémarrage hors réseau, saturation/recyclage. Réserver la réinitialisation aux seuls matériels de test, avec paramètres sauvegardés.
5. Acquérir les cartes après chaque scénario en lecture seule. Comparer dates FAT, noms, MP4 `stsc/stsz/stts/stco`, fins de médias et fichiers temporaires ; rechercher précisément le cumul audio à la place du reste de sept échantillons.
6. Séparer les faits reproductibles des analogies. Un défaut reproduit rend un mécanisme compatible ; il ne prouve pas que ce scénario s’est produit en 2024. Une différence de firmware limite toute transposition.

## Pièces externes utiles, sans demande envoyée

Pour les comptes caméra/cloud : export natif des connexions, partage d’appareils, visionnages s’ils existent, changements de configuration et sécurité, avec fuseaux, période effectivement couverte et description des champs. Ne pas assimiler un journal de connexion au compte à une consultation vidéo. Conserver les exports originaux avec empreintes.

Pour les Kingston : photographies/identifiants matériels, image du support et archive/inventaire/rejets correspondants, afin de vérifier les chemins référencés le 28 octobre. Pour la conservation : devis fixant la durée, inventaire complet des extractions, disque client identifié, contrôles d’empreintes et bordereau de remise. PV et journal Mac sont déjà déclarés indisponibles et ne conditionnent pas les travaux réalisables ici.

## Références techniques

- [dfir_ntfs, code du parseur LogFile](https://github.com/msuhanov/dfir_ntfs/blob/master/dfir_ntfs/LogFile.py) et [CLI](https://github.com/msuhanov/dfir_ntfs/blob/master/ntfs_parser) : structure, copie en mémoire, interprétation des données redo/undo.
- [python-evtx, discussion sur les chunks non actifs](https://github.com/williballenthin/python-evtx/issues/85) : motive le contrôle physique complémentaire, sans valider à elle seule les événements de cette affaire.
- La documentation Tuya sur les journaux SDK Android ne constitue pas un décodeur des fichiers APM iOS observés. Aucun format de chiffrement précis n’est attribué à ces fichiers sur cette seule base.

La reproduction locale des recoupements et catalogues caméra produit quatorze fichiers JSON identiques aux résultats retenus (`resultats/reproduction.json`). Le contrôle de livraison vérifie aussi les empreintes SIFT et NTFS, les liens, la syntaxe des scripts et l’absence de clé de récupération complète dans ce dossier. Les compteurs de `ntfs/metrics.json` proviennent des lignes `Log record, redo operation:`, `LSN:` et ` Timestamp:` du décodage complet.
