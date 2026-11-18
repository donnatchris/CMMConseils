from pathlib import Path
import hashlib, json, re, shutil

ROOT = Path('/mnt/data/codeProjects/DMMConseils')
STAGE = Path('/tmp/sadedine-remise-20261117')
STAGE.mkdir(exist_ok=True)
AUDIT = STAGE / 'audit'
AUDIT.mkdir(exist_ok=True)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(rel, content):
    p = STAGE / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)

sources = ['RAPPORT-FINAL-SADEDINE-2026.md', 'cartes_sd/analyse-cartes_sd.md']
before = {}
for rel in sources + ['pdfs/RAPPORT-FINAL-SADEDINE-2026.pdf', 'pdfs/analyse-cartes_sd.pdf', 'remise-documents/attestation-de-remise.md', 'remise-documents/attestation-de-remise.pdf']:
    p = ROOT / rel
    if p.exists():
        backup = AUDIT / 'avant' / rel
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, backup)
        before[rel] = sha(p)

report = (ROOT / sources[0]).read_text()
start = report.index('Mme Sadedine a demandé la conservation', report.index('### Annexe D'))
end = report.index('<a id="annexe-e"></a>', start)
new = '''L’ensemble des données extraites et du dossier de travail est conservé sur **OVHcloud S3**. **Le prestataire confirme le 17 novembre 2026 que le stockage S3 est complet.** Cette actualisation remplace l’état de conservation mentionné dans la version précédente du rapport.

**Mme Sadedine dispose d’un accès lui permettant de télécharger les données depuis le stockage S3 au moyen d’une clé d’accès.** Les identifiants de connexion sont communiqués séparément du rapport et du bordereau. L’espace de destination est le bucket `sadedine-2026`, sous le préfixe `SADEDINE-2026/`. La [notice de téléchargement](note-s3.md) décrit les modalités d’accès et de récupération.

Le [bordereau de mise à disposition des données](remise-documents/bordereau-mise-a-disposition-donnees-20261117.md) décrit le contenu accessible et les empreintes de contrôle de référence. **Aucun disque dur n’a été remis à la cliente à la date de cette actualisation.** La copie et la remise sur un disque dur neuf fourni par elle feront l’objet d’un bordereau distinct lors de cette remise. La conservation sur S3 se poursuit selon la durée prévue au devis.

#### Rectification de la date de remise des matériels

**La date de remise effective à retenir est le 7 octobre 2026**, conformément aux notes d’intervention, qui indiquent **16 h 15**. La mention du 6 octobre 2026 portée sur l’attestation d’origine est rectifiée par le [rectificatif du 17 novembre 2026](remise-documents/rectificatif-attestation-remise-20261117.md), à conserver avec celle-ci. L’attestation d’origine et ses signatures ne sont pas réécrites. TP-03, indiqué comme non remis lors de cette remise initiale, reste hors du périmètre de cette correction de date.

Les horaires notés pour l’acquisition d’OP-01 en 2026 ne sont pas entièrement raccordés aux horaires automatiques. Cet écart concerne la documentation de l’acquisition et ne permet pas de conclure à une manipulation en 2024.

'''
report = report[:start] + new + report[end:]
needle = 'inventoriés intégrés le 16 novembre 2026\\'
assert report.count(needle) == 1
report = report.replace(needle, 'inventoriés intégrés le 16 novembre 2026 ; conservation S3 et rectification de la date de remise actualisées le 17 novembre 2026\\')
report = report.replace('Sa remise matérielle, postérieure à l’attestation du 6 octobre 2026, est confirmée par le prestataire.', 'Sa remise matérielle, postérieure à la remise initiale du 7 octobre 2026, rectifiée par le document du 17 novembre, est confirmée par le prestataire.')
report = report.replace('datée du **6 octobre 2026**, et tient compte de la remise ultérieure de TP-03 confirmée par le prestataire.', 'portant la date du **6 octobre 2026**, rectifiée au **7 octobre 2026** par le [rectificatif du 17 novembre](remise-documents/rectificatif-attestation-remise-20261117.md), et tient compte de la remise ultérieure de TP-03 confirmée par le prestataire.')
put(sources[0], report)

sd = (ROOT / sources[1]).read_text()
old = 'Les notes indiquent une remise le **07/10/2026 à 16h15**, avec adaptateur USB ; l’[attestation](../remise-documents/attestation-de-remise.md) est datée du **06/10/2026**. Cette divergence documentaire reste non résolue.'
assert sd.count(old) == 1
sd = sd.replace(old, 'La remise effective est retenue au **07/10/2026 à 16 h 15**, avec adaptateur USB, conformément aux notes d’intervention. La date du **06/10/2026** portée sur l’[attestation d’origine](../remise-documents/attestation-de-remise.md) est rectifiée par le [rectificatif du 17 novembre 2026](../remise-documents/rectificatif-attestation-remise-20261117.md), à conserver avec cette attestation.')
sd = sd.replace('# Analyse des cartes SD\n', '# Analyse des cartes SD\n\n**Actualisation documentaire du 17 novembre 2026.** Rectification de la date de remise au 7 octobre 2026 par document séparé ; les dates et résultats d’acquisition sont conservés.\n', 1)
put(sources[1], sd)

put('remise-documents/rectificatif-attestation-remise-20261117.md', '''# Rectificatif de la date de remise des matériels

**Dossier :** SADEDINE-2026  
**Date du rectificatif :** 17 novembre 2026  
**Document concerné :** attestation de remise de matériels portant la date du 6 octobre 2026, avec ses annexes.

## Parties concernées

**Prestataire :** Christophe Donnat, Donnat Dev, entrepreneur individuel, 40 rue Albert Janicot, 66000 Perpignan.  
**Cliente :** DMM Conseils, représentée par Mme Malika Sadedine, 111 avenue Victor Hugo, 93300 Aubervilliers.

## Date de remise rectifiée

La date de remise effective des matériels visés par l’attestation est le **7 octobre 2026**, les notes d’intervention indiquant une remise à **16 h 15**, avec l’adaptateur USB des cartes SD.

En conséquence, la mention du **6 octobre 2026**, en tant que date de remise effective dans l’attestation, doit être lue **7 octobre 2026**. Le présent rectificatif est établi le 17 novembre 2026 ; il ne modifie pas les dates des signatures figurant sur l’original.

La correction concerne les matériels déclarés remis dans l’annexe 1 : **OP-01, TP-01, TP-02 et les cartes SD-01, SD-02 et SD-03**. TP-03, déclaré non remis ce jour-là et envoyé ultérieurement, n’est pas concerné par cette rectification de la remise initiale.

## Conservation des documents

Ce rectificatif doit être conservé et communiqué avec l’attestation d’origine et ses annexes. Il corrige uniquement la date de remise effective. Les caractéristiques des matériels, leur périmètre et les conditions prévues dans l’attestation demeurent ceux de l’original.

**Référence documentaire :** notes de remise reprises dans le rapport d’acquisition des cartes SD, section « État antérieur », qui indiquent le 07/10/2026 à 16 h 15.

Fait à Perpignan, le 17 novembre 2026.

**Le prestataire**  
Christophe Donnat, Donnat Dev  
Signature :

<div style="height: 15mm"></div>

**La cliente pour prise de connaissance**  
Mme Malika Sadedine, pour DMM Conseils  
Date et signature :
''')

refs = [
 ('OP-01', 'Flux disque reconstitué de l’image EWF', '0b00ac18a92cdb0b0f0a416199bc4955c3313a65b6cd034041cb99d097bb4484'),
 ('SD-01', 'Flux décompressé de l’image EWF', '42fa8f6d3351a4ba2446b267637f51a0c1e44df4abd31b002a1ac2212c023c09'),
 ('SD-02', 'Flux décompressé de l’image EWF', 'ba77335e75bdcb140922d3275fefea4441bbc4fdac3dea846a30bd37960d1f9d'),
 ('SD-03', 'Flux décompressé de l’image EWF', '7a59d086d809d27bdb2f203e7449c024e50ca919e528792c151cb8a604c852c0'),
 ('TP-01', 'Manifest.db de la sauvegarde logique', 'ab12f937dc0a6d1c1ca15312a8c3a9faf1322e8d44fa5e68b4dd18e8676ca0a8'),
 ('TP-02', 'Manifest-decrypted.db, manifeste déchiffré', 'cd34919ad3a2cb958e130b6ea7453e71f30fb02336d61f2e1dca0f2fb2b46eeb'),
 ('TP-03', 'Manifest.db, manifeste chiffré', 'e99a859fe1ed8dcd682eb15b10ec9ab61ac0cbc9d36bd26e734f751ca194c768'),
 ('TP-03', 'Manifeste déchiffré', '334123a803c20b59c9610b459b8769a07d24cab7ea805e35c6f64caec65f365c'),
]
board = '''# Bordereau de mise à disposition des données

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

'''
for code, desc, value in refs:
    board += f'**{code} — {desc}**\n\n```text\n{value}\n```\n\n'
board += '''Les listes détaillées d’empreintes des segments, extractions et résultats restent jointes aux dossiers techniques correspondants. Le fichier `empreintes-controle-remise-20261117.sha256` accompagne le présent bordereau : il réunit les empreintes des documents remis et des principaux inventaires de contrôle. Les valeurs ci-dessus reprennent les contrôles de la mission ; elles ne constituent pas un nouveau calcul intégral du stockage S3.

**Pièces associées :** notice de téléchargement ; rectificatif de la date de remise du 17 novembre 2026 ; fichier d’empreintes de contrôle.
'''
put('remise-documents/bordereau-mise-a-disposition-donnees-20261117.md', board)
put('audit/sources-avant.json', json.dumps(before, indent=2) + '\n')
put('audit/empreintes-reference.json', json.dumps(refs, ensure_ascii=False, indent=2) + '\n')
print(STAGE)
print('Documents préparés :', *sources, 'bordereau', 'rectificatif', sep='\n')
