# Inventaire DNEF

Ce dossier sépare les pièces reçues des analyses produites dans le cadre de la mission SADEDINE-2026.

| Dossier | Contenu |
| --- | --- |
| [Documents reçus](documents-recus/) | Les sept fichiers transmis : inventaire CSV, note Word et PDF, annexe Excel et trois images WhatsApp. Leurs noms et contenus sont conservés. |
| [Rapports](rapports/) | Les conclusions rédigées pendant la mission. |
| [Travaux techniques](travaux-techniques/) | Scripts, extractions, résultats détaillés, journaux et empreintes des investigations. Les sous-dossiers `prive/` restent exclus de Git. |

## Rapports disponibles

- [Répartition des 458 pages de sage.pdf](rapports/rapport-repartition-sage-458-pages.md) : destinataires, codes client et identifiants SIRET/SIREN page par page.
- [Réponse à Q1](rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md) : identité des contenus, dates et emplacements dans les deux iPhone mini.
- [Investigations B à E](rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md) : déverrouillage, transfert vers OP-01, traces applicatives, doublons et horloges.
- [Recherche de récupération du ZIP et des rejets dans OP-01](rapports/Recherche_recuperation_Archive_Rejets_OP-01_20261116.md) : MFT, candidats supprimés, VSS, mémoire et balayage intégral des clusters libres ; aucun fichier cible récupéré.

- [Séquence TP-02/TP-03 du 15 octobre, 13:25–13:51](rapports/Note_reponse_TP02_TP03_15oct2024.md) : analyse produite, transactions et limites de l’attribution humaine.

Les conclusions sont intégrées dans le [rapport TP-03, section 7](../telephones/analyse-TP-03.md#7-rapprochements-avec-op-01-et-tp-02) et résumées pour l’avocate au [point 1.5 du rapport final](../RAPPORT-FINAL-SADEDINE-2026.md#15-parcours-des-pdf-associés-à-tp-03).

## Navigation et contrôle des déplacements

Le [journal de déplacement](travaux-techniques/reorganisation-20261114/prive/journal-deplacement.json) décrit les 331 déplacements du 14 novembre, leurs chemins et empreintes avant/après. Les manifestes antérieurs restent des constats datés. Le contrôle historique s’exécute avec `python3 inventaire-DNEF/travaux-techniques/reorganisation-20261114/verifier.py --historique` ; le contrôle courant de ces anciens manifestes ne peut pas authentifier les textes révisés le 18 novembre. Le nouveau manifeste documentaire est distinct. `reorganiser.py` ne doit pas être relancé sur le dossier existant.

La note de séquence 13:25–13:51 est déplacée le 18 novembre des documents reçus vers les rapports ; le registre de révision conserve son ancien chemin. Les sept pièces reçues restent intactes.

## Traçabilité du rangement

La [réorganisation du 14 novembre 2026](README.md) conserve la correspondance entre anciens et nouveaux chemins. Les documents reçus, les résultats bruts, les journaux d’analyse et les anciens relevés d’empreintes n’ont pas été réécrits.

Les liens des rapports et les chemins des scripts ont été adaptés. Leurs versions antérieures sont conservées avec leurs empreintes. Les chemins inscrits dans les résultats historiques décrivent l’organisation au moment de l’analyse ; ils sont conservés comme tels.

---

Révision documentaire : 18 novembre 2026. Les dates des faits et des analyses restent celles indiquées dans le texte.

Christophe Donnat — Donnat Dev
