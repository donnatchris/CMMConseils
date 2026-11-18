from pathlib import Path
import hashlib
import difflib
import json

ROOT = Path('/mnt/data/codeProjects/DMMConseils')
STAGE = Path('/tmp/sadedine-cloture-q3-20261117')
STAGE.mkdir(exist_ok=False)
(STAGE / 'audit').mkdir()
changes = []

def update(rel, replacements):
    src = ROOT / rel
    old = src.read_text()
    new = old
    for before, after in replacements:
        assert new.count(before) == 1, (rel, before[:100], new.count(before))
        new = new.replace(before, after, 1)
    assert new != old
    out = STAGE / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(new)
    prior = STAGE / 'avant' / rel
    prior.parent.mkdir(parents=True, exist_ok=True)
    prior.write_bytes(src.read_bytes())
    headings = [line for line in old.splitlines() if line.startswith('#')]
    assert all(h in new.splitlines() for h in headings), rel
    diff = ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=rel, tofile=rel))
    (STAGE / 'audit' / (src.stem + '.diff')).write_text(diff)
    changes.append({'path': rel, 'before_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
                    'after_sha256': hashlib.sha256(out.read_bytes()).hexdigest()})

update('inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md', [
    ('**Mission SADEDINE-2026 — 14 novembre 2026 — complément à la réponse Q1.**',
     '**Mission SADEDINE-2026 — 14 novembre 2026 — complément à la réponse Q1.**\n\n**Complément du 17 novembre 2026 :** réponse à la question Q3 de la note cliente.'),
    ('Aucun décalage d’horloge unique n’est démontré. Le nommage ne désigne pas une application. La reproduction iOS/Windows sur appareils de test reste non réalisée.',
     'Aucun décalage d’horloge unique n’est démontré. Le nommage ne désigne ni une application ni un conflit iCloud ; l’origine des doublons reste indéterminée.'),
    ('**Ce scénario n’a pas été reproduit.**',
     '**Les données disponibles ne permettent pas d’établir que ce scénario a produit les attributs observés.**'),
    ('## C — Comment les PDF sont ils arrivés dans OP 01',
     '**Réponse à Q3 — accès aux PDF avant le premier déverrouillage.** Dans l’état sauvegardé de TP-03, les PDF examinés relèvent de la classe C : leur contenu est normalement inaccessible avant la première authentification après redémarrage. Une synchronisation iCloud ne suffit donc pas, à elle seule, à expliquer un nouvel accès local à ce contenu dans un état strictement antérieur au premier déverrouillage. En revanche, une date de métadonnée ne démontre ni un tel accès ni une création de PDF. La sauvegarde tardive ne permet pas d’établir l’état de protection et le lieu de production des traces aux heures litigieuses. Elle ne permet donc pas de déterminer si TP-03 a effectivement été déverrouillé ou a produit localement les fichiers à ces heures. La question du nommage des doublons est examinée ci-dessous, dans la partie E.\n\n## C — Comment les PDF sont ils arrivés dans OP 01'),
    ('Aucune reproduction native iOS ou Windows n’a été réalisée. L’absence d’iPhone de test a été confirmée par l’utilisateur ; aucun Windows de test natif n’est disponible dans l’environnement. Un [protocole reproductible](../travaux-techniques/investigations-B-E-20261114/protocole-reproduction.md) prépare ces essais sans utiliser les preuves comme matériel de test. Cette partie demeure une limite explicite de l’investigation E.',
     '**Réponse à Q3 — origine des doublons.** Les suffixes « 2 », « 3 » et « 4 » sont compatibles avec plusieurs mécanismes de copie ou de gestion de noms identiques. Ils ne permettent pas de distinguer des enregistrements répétés d’un mécanisme de conflit iCloud. Aucun élément retrouvé n’identifie ici un conflit iCloud comme origine des exemplaires de contenu identique, ni les conditions de sa survenue. La présence des contenus dans le stockage local Fichiers des deux Mini ne reconstitue pas leur circulation antérieure. **L’origine exacte des doublons reste indéterminée ; les éléments disponibles ne permettent ni de confirmer ni d’exclure une contribution d’iCloud.**'),
    ('Une reproduction sur matériel de test préciserait le comportement des métadonnées, mais ne remplacerait pas ces pièces historiques. ', ''),
])

update('telephones/analyse-TP-03.md', [
    ('**Équipement :** iPhone 13 mini — série `Y4Q9KGHG26`',
     '**Équipement :** iPhone 13 mini — série `Y4Q9KGHG26`\n\n**Mise à jour :** 17 novembre 2026 — réponse à Q3 sur le premier déverrouillage, iCloud et les doublons.'),
    ('### 7.4. Mail, Fichiers et traces indépendantes : investigation D',
     '**Réponse à Q3 — premier déverrouillage et iCloud.** Dans l’état sauvegardé, le contenu des PDF de classe C est normalement inaccessible avant la première authentification après redémarrage. Une synchronisation iCloud ne suffit pas, à elle seule, à expliquer un nouvel accès local à ce contenu dans un état strictement antérieur au premier déverrouillage. Mais les dates de métadonnées ne démontrent ni un accès au contenu ni une création de PDF. L’état historique de protection, le lieu de production des traces et leur éventuel transport ne sont pas établis. **Les données ne permettent donc pas de déterminer si TP-03 a été déverrouillé ou a produit localement les fichiers aux heures litigieuses.** L’origine des noms suffixés est examinée en section 7.6.\n\n### 7.4. Mail, Fichiers et traces indépendantes : investigation D'),
    (' Aucune reproduction native iOS/Windows n’a été réalisée : **aucun iPhone de test n’est disponible**, ni environnement Windows natif de test. Le [protocole préparé](../inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/protocole-reproduction.md) ne vaut pas résultat expérimental.', ''),
    ('Les conversions `Europe/Paris` sont cohérentes : **UTC+2 le 15**, **UTC+1 le 28**.',
     '**Réponse à Q3 — doublons et conflits iCloud.** Les suffixes « 2 », « 3 » et « 4 » sont compatibles avec plusieurs mécanismes de copie ou de gestion de noms identiques. Ils ne départagent pas des enregistrements répétés d’un mécanisme de conflit iCloud. Aucun élément retrouvé n’identifie ici un conflit iCloud comme origine des exemplaires identiques, ni les conditions de sa survenue. La présence des contenus dans le stockage local Fichiers des deux Mini ne reconstitue pas leur circulation antérieure. **L’origine exacte des doublons reste indéterminée ; une contribution d’iCloud n’est ni confirmée ni exclue par les données disponibles.**\n\nLes conversions `Europe/Paris` sont cohérentes : **UTC+2 le 15**, **UTC+1 le 28**.'),
])

update('RAPPORT-FINAL-SADEDINE-2026.md', [
    ('conservation S3 et rectification de la date de remise actualisées le 17 novembre 2026',
     'conservation S3, rectification de la date de remise et réponse à Q3 sur iCloud et les doublons actualisées le 17 novembre 2026'),
    ('Sa signification exacte et sa possible conservation lors de copies, synchronisations ou restaurations n’ont pas été validées expérimentalement.',
     'Les données disponibles ne permettent pas de déterminer si cette valeur a été produite localement à cette heure ou conservée lors d’une copie, d’une synchronisation ou d’une restauration.'),
    ('**4. Le regroupement des PDF sur l’ordinateur est daté du 28 octobre**',
     '**Réponse à Q3 — iCloud et origine des doublons.** Dans l’état sauvegardé de TP-03, le contenu des PDF examinés est normalement inaccessible avant la première authentification après redémarrage. Une synchronisation iCloud ne suffit donc pas à expliquer, à elle seule, un nouvel accès local à ce contenu avant cette authentification. Toutefois, une date de métadonnée ne prouve ni cet accès ni une création de PDF, et l’état historique du téléphone n’est pas établi. Les noms suffixés « 2 », « 3 » ou « 4 » ne permettent pas non plus de distinguer des enregistrements répétés d’un mécanisme de conflit iCloud. Aucun élément retrouvé n’identifie un tel conflit à l’origine des doublons. **La question reçoit donc une réponse sous réserve : le premier déverrouillage n’est pas démontré, l’origine exacte des doublons reste indéterminée et une contribution d’iCloud n’est ni confirmée ni exclue.** Voir les [sections 7.3 et 7.6 du rapport TP-03](telephones/analyse-TP-03.md#73-premier-déverrouillage-après-redémarrage--investigation-b) et le [complément B–E](inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md).\n\n**4. Le regroupement des PDF sur l’ordinateur est daté du 28 octobre**'),
])

update('inventaire-DNEF/rapports/Reponse_Q1_inventaire_DNEF_SADEDINE-2026.md', [
    ('Cette lecture est une interprétation technique des octets conservés, pas un journal de gestes validé par une reproduction sur iPhone.',
     'Cette lecture est une interprétation technique des octets conservés, pas un journal certifié de gestes effectués sur le téléphone.'),
])

for rel in ['pdfs/analyse-TP-03.pdf', 'pdfs/RAPPORT-FINAL-SADEDINE-2026.pdf']:
    old = ROOT / rel
    prior = STAGE / 'avant' / rel
    prior.parent.mkdir(parents=True, exist_ok=True)
    prior.write_bytes(old.read_bytes())
    changes.append({'path': rel, 'before_sha256': hashlib.sha256(old.read_bytes()).hexdigest()})

for item in changes:
    if item['path'].endswith('.md'):
        value = (STAGE / item['path']).read_text()
        assert not any(term in value.lower() for term in ['iphone de test', 'windows natif de test', 'matériel de test', 'n’a pas été reproduit', 'validées expérimentalement'])

(STAGE / 'audit' / 'modifications.json').write_text(json.dumps(changes, ensure_ascii=False, indent=2) + '\n')
print(STAGE)
print('\n'.join(item['path'] for item in changes))
