# Indices de copie du PDF « Rép  Dossier bourarach.pdf »

**9 novembre 2026 — consolidation de preuves déjà extraites, sans nouvelle acquisition.**

## Conclusion utilisable

**Des indices techniques concordants étayent la copie ou le regroupement de ce PDF dans `C:\L16B\TELEPHONES\IPHONE13_MINI` pendant les opérations du 28 octobre 2024. Sa présence dans ce dossier et l’identité de son contenu avec deux fichiers de la sauvegarde TP-02 sont établies. Ces éléments ne prouvent ni un transfert direct depuis ce téléphone, ni l’auteur individuel de la copie, ni son inclusion dans le support définitivement emporté par l’administration.**

## Identification et preuves

Nom exact relevé : `Rép  Dossier bourarach.pdf` (deux espaces après « Rép »).

Chemin dans l’image d’OP-01 : `C:\L16B\TELEPHONES\IPHONE13_MINI\Rép  Dossier bourarach.pdf`.

SHA-256 du contenu :

```text
2e82aa66ecbc307a98ce2a170799bed53af49c0de9dd9c0c2da00c87c530df3c
```

| Élément | Valeur ou résultat | Portée |
| --- | --- | --- |
| Enregistrement NTFS MFT | Index **381463**, séquence **41**, alloué | Identifie précisément le fichier dans les extractions MFT d’OP-01. |
| Création `$FILE_NAME` du nom long et du nom court `RPDOSS~1.PDF` | **28/10/2024 16:13:43,799497 UTC**, soit **17:13:43,799497 Paris** | Date compatible avec l’apparition du fichier à cet emplacement pendant les opérations. Les deux noms décrivent le même fichier, pas deux copies indépendantes. |
| Création `$STANDARD_INFORMATION` | **15/10/2024 11:42:57,930 UTC**, soit **13:42:57,930 Paris** | Date différente, pouvant être préservée lors d’un transfert ; ne prouve pas une copie sur OP-01 le 15. |
| Modification `$STANDARD_INFORMATION` | **17/12/2019 18:20:21 UTC** | Ancienneté de métadonnée, pas heure d’extraction du téléphone. |
| Comparaison des contenus | Deux fichiers de la sauvegarde TP-02 ont exactement le même SHA-256 | Identité binaire, au-delà d’une simple ressemblance de nom ou de texte. Ne prouve pas le sens de transfert ni l’exclusivité de la source. |
| Deux références Jump Lists au chemin local | Dernières dates d’interaction **29/10/2024 00:45:21,4984924 et 00:45:21,5887220 UTC**, soit **01:45:21 Paris** | Références Windows au fichier local ; ces dates sont après la restitution. Elles ne prouvent ni une lecture par les agents le 28, ni une copie sur clé USB. |

Les deux contreparties TP-02 se trouvent dans le domaine `AppDomainGroup-group.com.apple.FileProvider.LocalStorage`, sous `File Provider Storage/Downloads/`, l’une directement et l’autre dans un sous-dossier de téléchargements. Leurs identifiants d’objet sont `cb7ee8ca7b9c5f6ceb7f3f0dd1f3f955666f0729` et `4819b0420457b0ea52104732499297533326e379`. Leurs chemins Unicode exacts sont conservés dans l’annexe d’identité ci-dessous.

Les Jump Lists sources sont `588cea7e4abed698.automaticDestinations-ms` et `5f7b5f1e01b83767.automaticDestinations-ms`. Le champ `TrackerCreatedOn=2024-10-28 14:19:48.6879217` ne doit pas être présenté comme une heure de copie ou de lecture de ce document.

## Sources vérifiables

- [Enregistrement brut et décodé MFT, ligne 1544](../../ordinateur/recherche-OP-01/extractions-acces/l16b-mft.jsonl:1544) : octets bruts `raw_record_hex`, noms, index, séquence et dates.
- [Table documentaire privée](../20261109-correspondances-elargies/prive/table-documents-preuves.json) : entrée SHA-256 `2e82aa66ecbc…`, avec chemin, métadonnées et deux références Jump Lists.
- [Comparaison binaire privée avec TP-02](../20261108-complement-pv/prive/comparaison-pdf-identites.json) : entrée du même SHA-256, domaines, chemins et identifiants des deux contreparties.
- [Compte rendu antérieur, emplacement et traces du PDF Guillou](../20261109-correspondances-elargies/compte-rendu.md:62).

## Ce que la preuve ne permet pas d’affirmer

L’identité des contenus et la date FN constituent des indices de regroupement/copie locale, pas un journal de commande de copie. Les horodatages peuvent être conservés ou modifiés et ne désignent pas un opérateur. Le contenu commun pourrait provenir d’un transfert direct, d’une synchronisation ou d’une autre copie.

**Aucune référence individuelle retrouvée ne démontre la copie de ce PDF vers la clé de l’administration.** Les références connues à `E:\saddedine\Archive_saddedine.zip` désignent une archive globale dont nous n’avons pas le contenu. Pour établir l’emport de ce PDF, il faudrait le retrouver dans le jeu final avec un contenu identique, ou dans un inventaire authentifié permettant de le rattacher sans ambiguïté au contenu saisi.

Le PDF reproduit des échanges avec Me Isabelle Guillou concernant un recours administratif relatif à un tiers. La qualification de la correspondance et le lien avocat-client exact doivent être examinés séparément de la preuve technique de copie.
