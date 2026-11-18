# Bordereau de mise à disposition des données

**Dossier :** SADEDINE-2026  
**Date d’établissement :** 17 novembre 2026  
**Prestataire :** Christophe Donnat, Donnat Dev  
**Bénéficiaire :** DMM Conseils, représentée par Mme Malika Sadedine.

## Mise à disposition et accès au téléchargement

Le prestataire confirme que **l’ensemble des données extraites et du dossier de travail de la mission est stocké sur OVHcloud S3 et que ce stockage est complet** à la date du présent bordereau.

**Mme Malika Sadedine dispose d’un accès lui permettant de consulter et de télécharger ces données au moyen d’une clé d’accès S3 et de la clé secrète associée.** Les identifiants sont communiqués séparément ; ils ne sont pas reproduits dans ce bordereau. La notice de téléchargement précise la configuration de l’accès et la récupération des dossiers.

| Paramètre | Destination |
|---|---|
| Fournisseur | OVHcloud Object Storage S3 |
| Endpoint | `https://s3.sbg.io.cloud.ovh.net` |
| Région | `sbg` |
| Bucket | `sadedine-2026` |
| Préfixe du dossier | `SADEDINE-2026/` |

## Contenu mis à disposition

Les données comprennent les acquisitions et sauvegardes d’**OP-01, TP-01, TP-02, TP-03 et SD-01, SD-02, SD-03**, les données et vidéos récupérées, les extractions et résultats d’analyse, les rapports, les journaux techniques et les fichiers d’empreintes associés. Les éléments d’analyse de la Freebox et du réseau sont compris dans le dossier de travail.

La conservation sur S3 se poursuit pendant la durée prévue au devis. Les fichiers techniques doivent être téléchargés en conservant leurs noms et leur arborescence, notamment tous les segments des images EWF.

**Aucun disque dur n’a été remis à la cliente à la date du présent bordereau.** Ce document constate la mise à disposition par accès S3 ; la copie et la remise ultérieure sur le disque dur neuf fourni par la cliente seront documentées séparément.

## Validation

**Le prestataire** — Christophe Donnat  
Date et signature :

<div style="height: 9mm"></div>

**La cliente** — Mme Malika Sadedine, pour DMM Conseils  
Je reconnais disposer de l’accès S3 et des identifiants permettant le téléchargement. Cette reconnaissance ne vaut pas attestation d’un téléchargement intégral déjà réalisé.  
Date et signature :

<div style="break-before: page"></div>

## Annexe des empreintes de contrôle

Les empreintes **SHA-256** ci-dessous sont les valeurs de référence consignées dans les rapports et contrôles techniques de la mission. Elles identifient précisément les objets indiqués. Les valeurs des flux EWF s’appliquent au disque reconstitué ou décompressé, et non à chacun de ses fichiers segments. Une empreinte de manifeste iPhone identifie ce manifeste, et non l’intégralité de la sauvegarde.

**OP-01 — Flux disque reconstitué de l’image EWF**

```text
0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484
```

**SD-01 — Flux décompressé de l’image EWF**

```text
42fa8f6d3351a4ba2446b267637f51a0c1e44df4abd31b002a1ac2212c023c09
```

**SD-02 — Flux décompressé de l’image EWF**

```text
ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d
```

**SD-03 — Flux décompressé de l’image EWF**

```text
7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0
```

**TP-01 — Manifest.db de la sauvegarde logique**

```text
ab12f937dc0a6d1c1ca15312a8c3a9faf1322e8d44fa5e68b4dd18e8676ca0a8
```

**TP-02 — Manifest-decrypted.db, manifeste déchiffré**

```text
cd34919ad3a2cb958e130b6ea7453e71f30fb02336d61f2e1dca0f2fb2b46eeb
```

**TP-03 — Manifest.db, manifeste chiffré**

```text
e99a859fe1ed8dcd682eb15b10ec9ab61ac0cbc9d36bd26e734f751ca194c768
```

**TP-03 — Manifeste déchiffré**

```text
334123a803c20b59c9610b459b8769a07d24cab7ea805e35c6f64caec65f365c
```

Les listes détaillées d’empreintes des segments, extractions et résultats restent jointes aux dossiers techniques correspondants. Le fichier `empreintes-controle-remise-20261117.sha256` accompagne le présent bordereau : il réunit les empreintes des documents remis et des principaux inventaires de contrôle. Les valeurs ci-dessus reprennent les contrôles de la mission ; elles ne constituent pas un nouveau calcul intégral du stockage S3.

**Pièces associées :** notice de téléchargement ; rectificatif de la date de remise du 17 novembre 2026 ; fichier d’empreintes de contrôle.
