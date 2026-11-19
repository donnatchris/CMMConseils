# Comparaison aux empreintes de l’inventaire DNEF — 16 novembre 2026

**Deux concordances et un écart.** J’ai recalculé les empreintes sur les copies extraites. SHA-256 sert ici à contrôler les copies de travail ; SHA-512 permet la comparaison avec l’algorithme annoncé dans le CSV. Une valeur SHA-256 ne se compare pas directement à une valeur SHA-512. Le CSV déclare l’algorithme SHA-512, tandis que les contrôles d’extraction antérieurs étaient en SHA-256. Les deux algorithmes ont été recalculés sur les trois copies extraites pour cette comparaison.

Source : `inventaire-DNEF/documents-recus/Inventaire_saddedine.csv`, SHA-256 du CSV : `f2a4e9d05cca5c7b8082da42df76fca45e870f3e3acbbdf6ff03c07e68293c40`.

| Fichier | Ligne du CSV | Concordance SHA-512 |
|---|---:|---|
| `dmmconseils93300@hotmail.com.pst` | 1497 | **Différent** |
| `dmmconseils@hotmail.com.pst` | 1498 | Identique |
| `takeout-20241028T114105Z-001.zip` | 1529 | Identique |

## Empreintes complètes

### dmmconseils93300@hotmail.com.pst

Inventaire :

```text
9a523a8a621bd4364caea02e0a7c0a8953a6e3ca57d1d31d85df03932ad9a9b9c70aec6516a97ad09ec4131a3cf7ee16bcbb0c6573a870d0522affc8b11cb62c
```

Fichier extrait :

```text
1949987f20fced4a2b0a3c6c4000e5afb8a54e5ec8b08c667ed5397feab60ad18b87fe0a78348ee4b992306cfd8773eb53a3560e6ba82bd6d86e79523ec03361
```

### dmmconseils@hotmail.com.pst

Inventaire :

```text
025226d8e15182ce26a93ea8d450244a65efd1ee164be955a641544e6f96aba2d06f499f12b98a6db690e417efb5e13af0f6b9394013b53e8fe9dffedf2ecffe
```

Fichier extrait :

```text
025226d8e15182ce26a93ea8d450244a65efd1ee164be955a641544e6f96aba2d06f499f12b98a6db690e417efb5e13af0f6b9394013b53e8fe9dffedf2ecffe
```

### takeout-20241028T114105Z-001.zip

Inventaire :

```text
e1026d76b643485b5c3da5686d10ac6d69225cca33c46e18038db93be2593a7f2baacc82d1661285fac9b791f49eaaef35b8c99ab8cd80878f0404b9c8a82265
```

Fichier extrait :

```text
e1026d76b643485b5c3da5686d10ac6d69225cca33c46e18038db93be2593a7f2baacc82d1661285fac9b791f49eaaef35b8c99ab8cd80878f0404b9c8a82265
```

## Contrôles et portée

- Les SHA-256 recalculés concordent avec ceux des extractions vérifiées depuis l’image OP-01. Les tailles, inodes et dates de modification des copies sont restés identiques pendant la lecture.
- L’écart du PST `dmmconseils93300@hotmail.com.pst` est confirmé par un second calcul indépendant avec la commande `sha512sum`.
- Les contrôles antérieurs validaient l’identité entre les fichiers de l’image, leurs copies et les résultats techniques précédents. Ils ne constituaient pas une comparaison aux SHA-512 du CSV.
- Le PST `dmmconseils@hotmail.com.pst` et le ZIP Takeout concordent octet pour octet selon leur SHA-512 avec les empreintes listées dans cet inventaire.
- Le PST `dmmconseils93300@hotmail.com.pst` ne concorde pas avec l’empreinte listée au même chemin. Ce constat ne détermine ni la date, ni le mécanisme, ni l’auteur d’une éventuelle modification, et ne permet pas d’attribuer l’écart à l’extraction.

[Résultats structurés](comparaison-inventaire-SHA512-20261116.json).

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe Donnat — Donnat Dev
