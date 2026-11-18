#!/usr/bin/env python3
"""Complète les attributs bruts et rédige la réponse Q1 sans écraser de sortie."""
import collections
import datetime as dt
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import plistlib
import struct
import sys
from zoneinfo import ZoneInfo

project = Path(sys.argv[1])
base = project / 'inventaire-DNEF'
work = base / 'travaux-techniques/recherche-Q1-20261114'
r = json.loads((work / 'prive/resultats.json').read_text())
paris = ZoneInfo('Europe/Paris')


def write_new(path, text):
    with path.open('x', encoding='utf-8') as f:
        f.write(text)


def table(headers, rows):
    def safe(s):
        return str(s).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(map(safe, headers)) + ' |',
                      '| ' + ' | '.join('---' for _ in headers) + ' |'] +
                     ['| ' + ' | '.join(map(safe, row)) + ' |' for row in rows]) + '\n'


def pretty(s):
    return dt.datetime.fromisoformat(s).strftime('%d/%m/%Y %H:%M:%S')


def stamp(s):
    return dt.datetime.fromisoformat(s.split('[')[0])


def name(x):
    return x['path'].rsplit('\\', 1)[-1]


groups = collections.defaultdict(list)
for x in r['inventory']:
    groups[x['sha512']].append(x)
groups = dict(sorted(groups.items(), key=lambda kv: min(stamp(x['creation']) for x in kv[1])))
ids = {h: f'C{i:02d}' for i, h in enumerate(groups, 1)}
for ph, rows in r['phones'].items():
    for x in rows:
        x['content_id'] = ids[x['sha512']]
        raw = x['mbfile'].get('ExtendedAttributes', {}).get('hex')
        x['xattrs'] = {}
        if raw:
            attrs = plistlib.loads(bytes.fromhex(raw))
            for k, v in attrs.items():
                x['xattrs'][k] = {'hex': v.hex()} if isinstance(v, bytes) else v
                if k == 'com.apple.lastuseddate#PS':
                    assert isinstance(v, bytes) and len(v) == 16
                    sec, ns = struct.unpack('<qq', v)
                    assert 0 <= ns < 1000000000
                    x['lastused'] = {'seconds': sec, 'nanoseconds': ns,
                                     'paris': dt.datetime.fromtimestamp(sec, dt.timezone.utc).astimezone(paris).isoformat(),
                                     'interpretation': 'hypothese structure timespec little endian, seconds Unix et nanosecondes'}
        x['mbfile'].pop('EncryptionKey', None)

window_start = dt.datetime(2024, 10, 15, 13, 41, tzinfo=paris)
window_end = dt.datetime(2024, 10, 15, 13, 51, tzinfo=paris)
central = {}
for ph, rows in r['phones'].items():
    central[ph] = [x for x in rows if x.get('lastused') and window_start <= stamp(x['lastused']['paris']) < window_end]
assert len(central['TP-02']) == 0 and len(central['TP-03']) == 17
assert len({x['sha512'] for x in central['TP-03']}) == 17
assert sum(window_start <= stamp(x['status_change_paris']) < window_end for x in r['phones']['TP-03']) == 16
assert not any(window_start <= stamp(x['birth_paris']) < window_end for rr in r['phones'].values() for x in rr)

write_new(work / '.gitignore', 'prive/\n')
write_new(work / 'prive/attributs-et-chronologie.json', json.dumps(r, ensure_ascii=False, indent=2) + '\n')
annex = ['# Annexe technique des objets retrouvés pour Q1\n',
         '14 novembre 2026. Données privées. Les chemins et noms Unicode sont reproduits sans normalisation. '
         'Les dates sont celles des métadonnées sauvegardées, converties en Europe/Paris.\n']
for ph, rows in r['phones'].items():
    annex.append(f'## {ph}\n')
    for x in sorted(rows, key=lambda x: (x['content_id'], x['relativePath'])):
        annex.append(f"### {x['content_id']} objet {x['fileID']}\n\n"
                     f"Domaine : `{x['domain']}`\n\nChemin exact : `{x['relativePath']}`\n\n"
                     f"SHA-512 : `{x['sha512']}`\n\nSHA-256 : `{x['sha256']}`\n\n"
                     f"Création Birth : **{pretty(x['birth_paris'])}**. Modification : {pretty(x['modified_paris'])}. "
                     f"Changement LastStatusChange : {pretty(x['status_change_paris'])}.\n\n"
                     f"Attribut lastused : {pretty(x['lastused']['paris']) + ' ; nanosecondes ' + str(x['lastused']['nanoseconds']) if x.get('lastused') else 'absent'}. "
                     f"Lignes CSV DNEF, en-têtes compris : {', '.join(map(str, x['dnef_lines']))}.\n\n"
                     f"Métadonnées internes PDF : `{json.dumps(x['pdf_metadata'], ensure_ascii=False)}`.\n")
write_new(work / 'prive/annexe-objets.md', '\n'.join(annex))

birth_rows = []
location_rows = []
chrono_rows = []
for h, inv in groups.items():
    n = min(inv, key=lambda x: (len(name(x)), name(x)))
    rr = {ph: [x for x in rows if x['sha512'] == h] for ph, rows in r['phones'].items()}
    local = {ph: [x for x in rows if 'FileProvider.LocalStorage' in x['domain']] for ph, rows in rr.items()}
    births = [' ; '.join(pretty(v) for v in sorted({x['birth_paris'] for x in local[ph]})) for ph in rr]
    meta = rr['TP-03'][0]['pdf_metadata']
    creator = meta.get('Creator')
    if creator and creator.startswith('Mozilla/'):
        creator = 'Chrome 105 / ChromeOS (Skia)'
    if not creator:
        creator = 'Creator absent ; Producer ' + meta.get('Producer', 'absent')
    birth_rows.append([ids[h] + ' — ' + name(n), *births, creator])
    def locations(ph):
        codes = []
        for x in rr[ph]:
            rel = x['relativePath']
            if 'FileProvider.LocalStorage' in x['domain']:
                if rel.startswith('File Provider Storage/Downloads/Télécharge\xadments/'):
                    code = 'D/T'
                elif rel.startswith('File Provider Storage/Downloads/'):
                    code = 'D'
                elif rel.startswith('File Provider Storage/Télécharge\xadments/'):
                    code = 'T'
                else:
                    code = 'R'
                if '/London/Qonto/' in rel:
                    code += '/London/Qonto'
            elif 'whatsapp' in x['domain']:
                code = 'WA'
            else:
                assert x['domain'] == 'AppDomain-com.tencent.xin'
                code = 'WX'
            codes.append(code)
        return ', '.join(sorted(codes))
    location_rows.append([ids[h], locations('TP-02'), locations('TP-03')])
    tx = next((x for x in central['TP-03'] if x['sha512'] == h), None)
    first = min(inv, key=lambda x: stamp(x['creation']))
    dnef_time = stamp(first['creation'])
    if tx:
        sec = Decimal(tx['lastused']['seconds']) + Decimal(tx['lastused']['nanoseconds']) / Decimal(1000000000)
        delta = Decimal(str(dnef_time.timestamp())) - sec
        chrono_rows.append([ids[h], dnef_time.strftime('%H:%M:%S.%f').rstrip('0').rstrip('.'),
                            stamp(tx['lastused']['paris']).strftime('%H:%M:%S') + '.' + f"{tx['lastused']['nanoseconds']:09d}",
                            f'{delta:+.3f} s', pretty(tx['status_change_paris'])])
    else:
        tx = next(x for x in local['TP-03'] if '/Télécharge\xadments/' in x['relativePath'])
        chrono_rows.append([ids[h], dnef_time.strftime('%H:%M:%S.%f').rstrip('0').rstrip('.'),
                            pretty(tx['lastused']['paris']) if tx.get('lastused') else 'absent',
                            'hors fenêtre', pretty(tx['status_change_paris'])])

body = '''# Réponse technique à la question Q1 de la note DNEF

**Mission SADEDINE-2026 — 14 novembre 2026 — OP-01, TP-02 et TP-03.**

## Conclusion

**Les 27 PDF de l’inventaire représentent bien 20 contenus distincts, retrouvés à l’identique par SHA-512 dans les deux sauvegardes. Aucune date de création `Birth` des 72 exemplaires examinés ne tombe le 15 octobre 2024 entre 13 h 41 et 13 h 50. Leurs métadonnées de création sont essentiellement anciennes, de 2019 à 2023.** Il faut donc distinguer la création du contenu PDF, la date de création conservée par sa copie sur le téléphone et la date de « création » figurant dans l’inventaire de saisie.

**Un élément nouveau favorise toutefois TP-03 : 17 des 20 contenus possèdent, dans cette sauvegarde, un attribut `com.apple.lastuseddate#PS` daté dans la même séquence du 15 octobre. Pour 16 de ces 17 objets, `LastStatusChange` tombe aussi dans cette fenêtre.** Ce rapprochement documentaire et temporel est plus discriminant que l’identité de contenu commune aux deux Mini. Aucun attribut de dernière utilisation des exemplaires TP-02 contrôlés ne tombe dans cette fenêtre.

La réponse à « lequel les a créés le 15 octobre ? » est donc : **une création ce jour-là n’est pas établie ; TP-03 est la piste la mieux étayée pour l’installation ayant conservé des traces d’utilisation ou de traitement de ces documents à ces heures.** Les données ne prouvent pas, à elles seules, que le téléphone physique TP-03 a été manipulé, que les 27 copies proviennent directement de lui, ni qui aurait effectué une opération. Les possibilités de copie, restauration, transport de métadonnées et d’horloge incorrecte restent ouvertes.

## Question et périmètre

La question Q1, § 3.4 de la [note cliente](../documents-recus/Note_analyse_inventaire_DNEF_SADEDINE-2026.docx), demande les dates de création, l’emplacement et l’application d’origine des 20 contenus dans TP-02 et TP-03, puis l’identification du Mini qui les aurait créés le 15 octobre entre 13 h 41 et 13 h 50. La présente réponse se limite à Q1. Elle ne conclut pas sur le déverrouillage, la possibilité d’une synchronisation avant premier déverrouillage ou le rattachement des traces TCC et PeopleSuggester, objets des questions suivantes.

| Code | Série | UDID de la sauvegarde |
| --- | --- | --- |
| TP-02 | F5466LV9V7 | `00008110-001C69A002BA801E` |
| TP-03 | Y4Q9KGHG26 | `00008110-001249321444801E` |

Les numéros de scellé 3 et 4 ne sont pas attribuables avec certitude à ces codes internes dans les pièces examinées.

## Contrôles réalisés

Les [rapports TP-02](../../telephones/analyse-TP-02.md#113-autres-téléphones-pdf-et-relation-de-confiance), [TP-03](../../telephones/analyse-TP-03.md#72-pdf-communs-aux-deux-mini) et [OP-01](../../ordinateur/analyse-ordinateur.md#62-les-3-461-entrées-datées-dans-lintervalle-central), ainsi que la [fiche Bourarach](../../investigations/20261109-clarification-correspondances/fiche-bourarach.md), ont servi de point de départ. Les anciennes réserves sur l’absence d’inventaire de saisie sont réévaluées ici pour les seuls 27 PDF grâce au CSV désormais fourni.

L’empreinte du [CSV fourni](../documents-recus/Inventaire_saddedine.csv) est exactement celle annoncée dans la note cliente :

```text
SHA-256 f2a4e9d05cca5c7b8082da42df76fca45e870f3e3acbbdf6ff03c07e68293c40
```

Sur SIFT, les PDF déjà déchiffrés lors des campagnes antérieures ont été relus. Leurs SHA-256 concordent avec les comparaisons antérieures, et leurs SHA-512 calculés cette fois concordent directement avec les 27 lignes du CSV. Les 20 contenus sont couverts sur chaque Mini : **46 objets dans TP-02 et 26 dans TP-03**. Il s’agit de 72 exemplaires correspondants, pas du nombre total de PDF de chaque sauvegarde. Les recherches antérieures sélectionnaient les candidats par nom normalisé ou taille déclarée ; elles ne constituent pas un hachage exhaustif de tous les objets des sauvegardes.

Les manifestes déchiffrés et leurs compagnons disponibles ont été copiés dans un nouveau dossier de travail, puis les copies ont été ouvertes en lecture seule. Les empreintes des sources sont identiques avant et après copie ; les deux copies donnent `quick_check=ok`. Les 72 `fileID`, domaines et chemins ont été revérifiés. Les champs `Birth`, `LastModified`, `LastStatusChange`, les attributs étendus et les champs internes PDF ont été extraits. Aucun déchiffrement nouveau ni accès aux comptes en ligne n’a été nécessaire.

| Manifeste déchiffré | SHA-256 |
| --- | --- |
| TP-02 | `cd34919ad3a2cb958e130b6ea7453e71f30fb02336d61f2e1dca0f2fb2b46eeb` |
| TP-03 | `334123a803c20b59c9610b459b8769a07d24cab7ea805e35c6f64caec65f365c` |

Les dates ci-dessous sont en **Europe/Paris**, avec le décalage applicable à chaque date. `Birth` est une métadonnée conservée dans la sauvegarde tardive, susceptible d’être héritée lors d’une copie ou restauration. Elle ne certifie pas la première apparition sur cet exemplaire physique du téléphone.

## Dates de création et origine déclarée des PDF

Le tableau donne les `Birth` de tous les exemplaires du stockage local Fichiers retrouvés. Les autres exemplaires applicatifs sont détaillés ensuite. Le nom le plus court d’un groupe de contenus identiques sert de libellé ; les variantes suffixées du CSV restent identifiées par leurs empreintes dans les pièces techniques.

{{BIRTH_TABLE}}

**Le champ `Creator` décrit le logiciel déclaré à l’intérieur du PDF, pas l’application qui l’aurait ouvert ou exporté le 15 octobre.** Sept contenus déclarent `Creator=Mail`, avec un `Producer` Quartz iOS 13.1.3, 14.2, 15.3.1 ou 15.6.1 et des dates PDF de 2019 à 2022. Cela étaye une ancienne génération de ces PDF par Mail. Les autres déclarent Safari sur macOS, Word, Excel, WPS, Chrome/Skia ou wkhtmltopdf ; plusieurs n’ont qu’un `Producer` Microsoft Print To PDF ou FPDF. Ces indications ne désignent ni l’utilisateur, ni le téléphone créateur, ni le mécanisme de transfert en octobre 2024.

Les différences de `Birth` entre copies d’un même contenu sont significatives : l’avis d’échéance possède dans TP-02 une copie supplémentaire datée de février 2025 ; FA0046 possède sur les deux Mini une copie du 13 mai et une du 17 mai 2022. Elles montrent qu’une date de copie n’est pas une date unique de création du contenu.

## Emplacements dans les sauvegardes

Les 20 contenus ont tous un exemplaire sous **`AppDomainGroup-group.com.apple.FileProvider.LocalStorage`**. Ce domaine désigne le stockage local géré par le fournisseur de Fichiers, interprété comme l’espace **« Sur mon iPhone »**. Le mot « Téléchargements » dans un chemin local ne le transforme pas en dossier iCloud Drive.

Les codes du tableau représentent les chemins sous `File Provider Storage/` : **R** = racine ; **D** = `Downloads/` ; **D/T** = `Downloads/Téléchargements/` ; **T** = `Téléchargements/`. La graphie « Téléchargements » est simplifiée pour la lecture ; les caractères Unicode exacts sont conservés dans l’annexe technique. **WA** = objet du domaine partagé WhatsApp, sous `Message/Media/` ; **WX** = objet de `AppDomain-com.tencent.xin`, sous `Documents/…/OpenData/…/1935.pdf`, correspondant au conteneur de WeChat.

{{LOCATION_TABLE}}

Pour **FACTURE RCT OCTOBRE**, les copies WA des deux Mini portent `Birth=23/11/2022 20:34:58`, tandis que les copies Fichiers portent `06/12/2022 16:40:58`. Pour **Fattura-37**, l’exemplaire WX porte `27/10/2022 16:05:22` dans les deux sauvegardes ; la copie TP-02 dans D/T porte une seconde de plus. Les autres dates WA sont identiques à celles du contenu correspondant dans Fichiers.

L’exemplaire local **FACTURE RCT NOVEMBRE** porte, sur les deux Mini, l’attribut `com.whatsapp.original` contenant le chemin du média WhatsApp identique retrouvé. C’est un indice d’association à un média WhatsApp, sans preuve autonome du sens ou de la date d’un export.

**Aucun des 72 objets correspondants examinés n’est situé dans un domaine iCloud Drive ou un magasin de pièces jointes Mail.** Cela décrit les exemplaires retrouvés ; la couverture d’une sauvegarde logique et la sélection de candidats ne permettent pas d’exclure un autre exemplaire ancien, supprimé, exclu de sauvegarde ou non sélectionné. L’application ayant réalisé chaque enregistrement ou export le 15 octobre reste indéterminée. La présence dans Fichiers, WhatsApp ou WeChat ne signifie pas que ces applications ont créé le contenu PDF.

## Rapprochement temporel nouveau avec TP-03

Les attributs `com.apple.lastuseddate#PS` sont présents sous forme de 16 octets. Leur décodage retenu est celui de deux entiers signés de 64 bits en ordre little endian : secondes Unix et nanosecondes. Les valeurs obtenues ont des nanosecondes valides et des dates cohérentes avec les autres métadonnées. Cette lecture est une interprétation technique des octets conservés, pas un journal de gestes validé par une reproduction sur iPhone. Les octets bruts restent disponibles pour contre-vérification.

Dans TP-03, **17 objets représentant 17 contenus** portent cet attribut dans la fenêtre du 15 octobre. Le tableau compare sa valeur à la **première** date de création DNEF du même contenu. L’écart est « date DNEF moins attribut TP-03 ». Les doublons ultérieurs du CSV ne sont donc pas utilisés pour choisir artificiellement un meilleur écart.

{{CHRONO_TABLE}}

Les 17 rapprochements se situent tous à moins de 11 secondes en valeur absolue. Pour **16** de ces objets, `LastStatusChange` est daté dans cette même séquence ; pour **TR Urgent**, ce champ a une date ultérieure mais l’attribut lastused conserve celle du 15 octobre. Les trois contenus dont l’attribut actuel est ultérieur sont C08, C11 et C12 : leur absence de valeur dans la fenêtre ne démontre pas une absence d’activité ce jour-là.

Exemple particulièrement précis : **Rép Dossier bourarach.pdf** a dans TP-03 `Birth=17/12/2019 19:20:21`, un attribut lastused au **15/10/2024 13:42:55,987134933**, puis `LastStatusChange=13:42:56`. Le CSV lui attribue une création à **13:42:57,930**. L’écart est de **1,943 seconde** environ. TP-02 contient deux copies identiques de ce PDF, mais leurs attributs lastused actuels sont datés du 28 octobre vers 23 h 36 et 23 h 53.

**Ce faisceau favorise la lignée logique de TP-03 pour la séquence de traitements du 15 octobre.** Il ne permet pas de transformer les dates DNEF en dates `Birth` du téléphone. Les attributs de dernière utilisation peuvent être réécrits ou transportés ; leur nom et leur proximité avec les dates de changement ne prouvent pas une consultation humaine ni un export direct. L’absence de valeur comparable dans l’état tardif de TP-02 ne prouve pas que TP-02 n’a jamais connu ces traitements.

## Portée de l’inventaire et réponse à l’identification du Mini

Le rapport OP-01 relevait pour les 27 PDF une création NTFS `$STANDARD_INFORMATION` le 15 octobre et une création `$FILE_NAME` le 28 octobre. **Le constat nouveau ne valide pas la déduction de la note cliente selon laquelle la date SI serait nécessairement la date de création sur le téléphone source.** Les `Birth` des exemplaires sauvegardés ne portent précisément pas ces dates du 15. Le mécanisme qui a produit la date de création inventoriée reste à établir.

Le CSV permet maintenant de dire que les **20 contenus**, sous les **27 chemins IPHONE13_MINI**, figurent dans l’inventaire fourni avec les mêmes SHA-512 que les PDF sauvegardés et déjà rapprochés de L16B. Cela lève pour ces entrées la seule réserve ancienne tenant à l’indisponibilité de cet inventaire. Le fichier CSV n’authentifie pas à lui seul le CD ou son origine administrative ; le contenu d’`Archive_saddedine.zip` et le support effectivement emporté n’ont pas été examinés ici.

Les sauvegardes sont postérieures aux faits : les métadonnées de TP-03 portent septembre 2025 et son `Info.plist` manque ; celles de TP-02 présentent des dates de septembre/octobre 2026 dont l’écart reste documenté dans son rapport. Elles ne constituent pas des acquisitions contemporaines d’octobre 2024. L’héritage ancien des dates et des fichiers communs empêche une attribution matérielle exclusive.

**Réponse Q1 utilisable :** les contenus existaient sous forme de PDF avec des métadonnées anciennes, et se retrouvent dans le stockage local Fichiers des deux Mini, avec des exemplaires supplémentaires WhatsApp et WeChat pour certains. Les métadonnées internes renseignent partiellement le logiciel de génération ancien. Une création des PDF le 15 octobre entre 13 h 41 et 13 h 50 n’est pas démontrée. Les attributs de 17 contenus constituent en revanche un indice temporel nouveau et concordant en faveur de TP-03 pour l’installation concernée par la séquence, sans certifier un transfert direct, une manipulation humaine, un auteur ou le numéro de scellé.

## Pièces et reproduction

- [Annexe privée des 72 objets](../travaux-techniques/recherche-Q1-20261114/prive/annexe-objets.md) : chemins exacts, `fileID`, empreintes, création, modification, changement, attribut lastused, métadonnées PDF et lignes du CSV.
- [Résultats structurés et attributs bruts](../travaux-techniques/recherche-Q1-20261114/prive/attributs-et-chronologie.json) et [résultats de la première passe](../travaux-techniques/recherche-Q1-20261114/prive/resultats.json). Les plists MBFile originaux extraits des manifestes sont conservés avec leurs copies de travail.
- [Script de vérification](../travaux-techniques/recherche-Q1-20261114/scripts/verifier_q1.py) et [script de rédaction et décodage](../travaux-techniques/recherche-Q1-20261114/scripts/rediger_q1.py). Le second export retire `EncryptionKey` de sa représentation JSON ; les preuves brutes restent privées.

Commandes exécutées sur SIFT, depuis le partage du projet :

```sh
python3 /media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/scripts/verifier_q1.py /media/shared/codeProjects/DMMConseils /media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive
python3 /media/shared/codeProjects/DMMConseils/inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/scripts/rediger_q1.py /media/shared/codeProjects/DMMConseils
```

Les scripts refusent de remplacer leurs sorties. Pour reproduire, adapter dans une copie les destinations vers un dossier neuf. Les accès SSH ont utilisé `ssh -F /home/chris/.ssh/config sift` : la commande simple `ssh sift` rencontrait une erreur locale de permissions sur la configuration SSH système. Une exploration préliminaire d’attributs a échoué sur l’agrégation des noms de clés ; elle a été corrigée, puis tous les attributs utiles ont été relus par le script conservé. Aucun résultat d’une passe échouée n’est utilisé comme preuve d’absence.
'''
body = body.replace('{{BIRTH_TABLE}}', table(['Contenu', 'Birth Fichiers TP-02', 'Birth Fichiers TP-03', 'Logiciel déclaré dans le PDF'], birth_rows))
body = body.replace('{{LOCATION_TABLE}}', table(['Contenu', 'TP-02', 'TP-03'], location_rows))
body = body.replace('{{CHRONO_TABLE}}', table(['Contenu', 'Première création DNEF le 15/10', 'Attribut lastused TP-03', 'Écart', 'LastStatusChange TP-03'], chrono_rows))
write_new(base / 'rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md', body)
manifest = []
for p in [base / 'documents-recus/Inventaire_saddedine.csv', base / 'documents-recus/Note_analyse_inventaire_DNEF_SADEDINE-2026.docx',
          base / 'rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md', Path(__file__), work / 'scripts/verifier_q1.py',
          work / 'prive/resultats.json', work / 'prive/attributs-et-chronologie.json', work / 'prive/annexe-objets.md']:
    manifest.append(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + str(p.relative_to(project)))
write_new(work / 'manifest-sha256.txt', '\n'.join(manifest) + '\n')
print(json.dumps({'report': str(base / 'rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md'),
                  'contents': len(groups), 'lastused_central': {ph: len(v) for ph, v in central.items()},
                  'objects': {ph: len(v) for ph, v in r['phones'].items()}}, ensure_ascii=False))
