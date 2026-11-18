# Révision documentaire SADEDINE-2026 — 18 novembre 2026

Le corpus initial comptait 123 Markdown hors `s3.md` : 84 documents courants et 39 copies historiques. La révision porte sur les textes et la livraison ; aucune nouvelle acquisition, accès à un compte ou expérience sur les supports n’est présentée comme réalisée.

## Documents courants et livraison

Le rapport final donne sept points utilisables pour l’avocate, une chronologie séparant faits/conservation/ouvertures et les demandes de pièces avec détenteur présumé et priorité. OP-01, TP-01, TP-02 et SD-03 exposent leur propre réponse, les observations, les scénarios classés, les références, la méthode et les limites. Les autres rapports et notices conservent leurs résultats propres et leurs dates.

Le [registre des 123 documents](statuts-corpus.json) donne un statut explicite pour chaque chemin initial : révisé, conservé, fusionné, réservé à l’usage interne ou supprimé. La sélection de livraison est définie dans `generer-pdf/livraison-20261118.json` ; codes d’accès, cours, mémos et correspondance ancienne en sont exclus. La note 13:25–13:51 est une analyse produite, déplacée vers `inventaire-DNEF/rapports/` ; les scripts et résultats techniques de son ancien dossier restent conservés.

## Suppressions et récupération

Les 39 copies historiques et les notices redondantes sont retirées après comparaison. Le [registre des suppressions/déplacements](suppressions-et-deplacements.json) contient pour chacune un commit et un blob Git vérifiés ainsi qu’une commande de récupération en lecture. La commande `git show COMMIT:"chemin" > /tmp/copie-historique.md` permet de retrouver le contenu commité sans remplacer le texte courant. Les seules modifications préexistantes des copies historiques étaient les ajouts de signature du 18 novembre, avec une actualisation de nom/signature dans certains en-têtes : leur état est identifié par SHA-256 dans `etat-initial.json`. Les rapports courants conservent la signature demandée.

La [comparaison des archives](comparaison-archives.json) indique les versions confrontées. Les [commandes uniques](annexe-commandes-conservees.md) et les interventions d’acquisition reprises dans OP-01 restent disponibles. Les anciennes conclusions remplacées restent dans Git. La copie initiale Sage a été rapprochée de la référence : ses tableaux sont identiques. Les [contrôles historiques](controles-historiques.md) conservent les vérifications utiles et leurs dates ; les scripts, résultats bruts et journaux n’ont pas été supprimés.

## Actes de remise et références

L’attestation d’origine conserve son texte, ses dates et ses emplacements de signature ; les chemins des photographies sont corrigés dans le Markdown de travail. Son PDF d’origine est préservé. Le rectificatif reste une pièce séparée. Le bordereau distingue confirmation du prestataire, contrôles d’empreintes, accès S3 et téléchargement complet, sans attester une remise de disque dur. L’ancienne référence absente `note-s3.md` est remplacée par une notice sans secrets ; le fichier interne de configuration n’est pas livré.

## Contrôles de livraison

Les manifestes historiques ne sont pas recalculés. La livraison du 18 novembre possède ses propres empreintes et contrôles de liens, ancres, tableaux, sources et limites de page, consignés séparément après génération. Les tableaux exhaustifs de comparaison et d’inventaire conservent leurs lignes de preuve. Les dérivés privés nécessaires à la reproduction restent distincts de la livraison documentaire et peuvent manquer dans un clone Git.


## Livraison générée et vérifiée

La sélection comprend 69 PDF, dont l’attestation d’origine, pour 925 pages au total. La synthèse d’ouverture tient sur trois pages. Les contrôles automatisés valident 911 liens locaux, les 1 555 comparaisons individuelles et tous les tableaux de preuve, les références Git des 39 copies et des 13 autres fusions/déplacements, les sources hors corpus rétablies et les empreintes de la livraison. Les longs champs de destinataires sont reportés intégralement en annexe de lecture dans les PDF ; chaque comparaison SHA-512 tient dans un bloc indivisible. Les sources et manifestes historiques restent datés. Les détails sont dans `validation-documentaire.json` et le relevé de contrôle visuel.

Le fichier `docs/mail-5.txt`, apparu pendant les travaux, est laissé intact et hors des 123 documents du plan ; la demande d’une note distincte qu’il contient n’est pas présentée comme accomplie par cette révision.

Christophe DOnnat — Donnat Dev
