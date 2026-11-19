#!/usr/bin/env python3
"""Inventaire documentaire en lecture seule ; Python standard et Poppler.

Usage : python3 analyser_sage.py /chemin/sage.pdf /nouveau/dossier
Le dossier de destination peut exister, mais aucun résultat existant n'est écrasé.
"""
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def extract(source, mode):
    return subprocess.run(['pdftotext', mode, str(source), '-'],
                          check=True, capture_output=True).stdout.decode('utf-8')


def pages(text):
    result = text.split('\f')
    assert not result[-1].strip(), 'Séparateur final inattendu'
    return result[:-1]


def compact(numbers):
    result = []
    for n in sorted(set(numbers)):
        if result and result[-1][-1] + 1 == n:
            result[-1].append(n)
        else:
            result.append([n])
    return ', '.join(str(x[0]) if len(x) == 1 else f'{x[0]}–{x[-1]}' for x in result)


def kind(value):
    return {0: 'Absent', 9: '9 chiffres (format SIREN)',
            14: '14 chiffres (format SIRET)'}[len(value)]


def table(headers, rows):
    def safe(v):
        return str(v).replace('|', '\\|').replace('\n', ' ')
    return '\n'.join(['| ' + ' | '.join(map(safe, headers)) + ' |',
                      '| ' + ' | '.join('---' for _ in headers) + ' |'] +
                     ['| ' + ' | '.join(map(safe, row)) + ' |' for row in rows])


def main():
    source = Path(sys.argv[1]).resolve()
    out = Path(sys.argv[2]).resolve()
    out.mkdir(parents=True, exist_ok=True)
    before = sha256(source)
    layout = extract(source, '-layout')
    raw = extract(source, '-raw')
    bbox = extract(source, '-bbox-layout')
    lp, rp = pages(layout), pages(raw)
    ns = {'h': 'http://www.w3.org/1999/xhtml'}
    xp = ET.fromstring(bbox).findall('.//h:page', ns)
    assert len(lp) == len(rp) == len(xp) == 458
    records = []
    for n, (text, raw_page, xml_page) in enumerate(zip(lp, rp, xp), 1):
        lines = text.splitlines()
        issuer = re.split(r'\s{2,}', lines[0].strip())[0]
        match = re.search(r'\b(FA\d+)\s+(\d{2}/\d{2}/\d{4})\s+(\d+)\s*$', lines[1])
        assert match, f'En-tête non reconnu : page {n}'
        invoice, date, code = match.groups()
        vat_line = next(i for i, line in enumerate(lines) if 'TVA intracom' in line)
        name = next(line.strip() for line in lines[vat_line + 1:] if line.strip())
        emitter_id = re.findall(r'^\s*SIRET\s*:\s*(\d+)\s*$', text, re.M)
        client_ids = re.findall(r'^\s*SIRET client\s*:\s*([^\n]+)', text, re.M)
        assert len(emitter_id) == 1 and len(client_ids) <= 1
        value = client_ids[0].strip() if client_ids else ''
        assert not value or re.fullmatch(r'\d{9}|\d{14}', value)
        assert issuer == 'SAS ALMU' and emitter_id[0] == '81816735500010'
        # Deuxième mode d'extraction, comparé sur chaque page.
        normalize_spaces = lambda value: re.sub(r'\s+', '', value)
        assert normalize_spaces(name) in [normalize_spaces(line) for line in raw_page.splitlines()], (n, name)
        assert re.findall(r'SIRET client\s*:\s*(\d+)', raw_page) == ([value] if value else [])
        assert re.search(r'Facture N°\s+' + invoice + r'\s+Date\s+' + date +
                         r'\s+Client\s+' + code + r'\b', raw_page), n
        # Contrôle géométrique : bloc destinataire et cases de l'en-tête.
        xml_lines = [(float(line.get('xMin')), float(line.get('yMin')),
                      ' '.join(word.text or '' for word in line.findall('h:word', ns)))
                     for line in xml_page.findall('.//h:line', ns)]
        recipient_lines = [t for x, y, t in xml_lines if x > 270 and 140 < y < 155]
        assert list(map(normalize_spaces, recipient_lines)) == [normalize_spaces(name)], (n, recipient_lines, name)
        assert [t for x, y, t in xml_lines if 270 < x < 350 and 35 < y < 45] == [invoice], n
        assert [t for x, y, t in xml_lines if 380 < x < 450 and 35 < y < 45] == [date], n
        assert [t for x, y, t in xml_lines if x > 500 and 35 < y < 45] == [code], n
        xml_sirets = [t for x, y, t in xml_lines if t.startswith('SIRET client')]
        assert xml_sirets == ([f'SIRET client : {value}'] if value else []), (n, xml_sirets)
        records.append(dict(page=n, facture=invoice, date=date, emetteur=issuer,
                            siret_emetteur=emitter_id[0], destinataire=name,
                            code_client=code, identifiant_client_transcrit=value,
                            qualification=kind(value), provisoire='Provisoire' in text))

    after = sha256(source)
    assert before == after, 'Le hash du PDF a changé pendant l’analyse'
    counts = Counter(len(r['identifiant_client_transcrit']) for r in records)
    names = {r['destinataire'] for r in records}
    codes = {r['code_client'] for r in records}
    values = {r['identifiant_client_transcrit'] for r in records if r['identifiant_client_transcrit']}
    invoices = defaultdict(list)
    by_company = defaultdict(list)
    by_value = defaultdict(list)
    for r in records:
        invoices[r['facture']].append(r)
        by_company[(r['destinataire'], r['code_client'])].append(r)
        by_value[r['identifiant_client_transcrit']].append(r)
    assert sum(map(len, by_company.values())) == sum(map(len, by_value.values())) == 458
    assert len(invoices) == 455
    assert {k: [r['page'] for r in v] for k, v in invoices.items() if len(v) > 1} == {
        'FA0463': [375, 376, 377, 378]}
    for key, group in by_company.items():
        assert len({r['identifiant_client_transcrit'] for r in group}) == 1, key
    dates = [datetime.strptime(r['date'], '%d/%m/%Y') for r in records]
    date_range = f'{min(dates):%d/%m/%Y} au {max(dates):%d/%m/%Y}'
    pct = lambda n: f'{100*n/458:.2f}'.replace('.', ',') + ' %'
    visual_pages = [1, 2, 8, 21, 195, 207, 232, 298, 363, 375, 376, 377, 378, 458]
    parts = [
        '# Répartition des 458 pages de sage.pdf par société et identifiant',
        '**Date de l’analyse :** ' + datetime.now().astimezone().strftime('%d/%m/%Y') + '.',
        '## 1. Source et périmètre',
        f'**Source unique des affectations :** [sage.pdf]({source}).\n\n'
        f'- Taille : {source.stat().st_size:,} octets.\n'
        '- Pagination utilisée : position physique dans le PDF, de 1 à 458, et non numéro de facture.\n'
        f'- SHA-256 avant et après lecture : `{before}`. Les deux empreintes sont identiques.\n'
        f'- Dates portées par les factures : du {date_range}. Ces dates ne constituent pas une datation des opérations informatiques.\n'
        '- Le PDF source a été ouvert en lecture seule ; aucun contenu n’a été modifié.',
        '## 2. Résultats et règles de lecture',
        f'Les **458 pages ont pour émetteur SAS ALMU, SIRET `81816735500010`**. '
        f'Le bloc destinataire présente **{len(names)} dénominations distinctes**, réparties sur '
        f'**{len(codes)} codes client Sage**. Ces dénominations incluent des associations et des personnes physiques ; '
        'elles ne constituent pas un décompte de personnes morales vérifiées. '
        f'Le fichier comporte **{len(invoices)} numéros de facture distincts** : '
        'la facture **FA0463**, destinataire **R-STM**, code **097**, occupe les pages **375 à 378**.',
        table(['Contenu du champ « SIRET client »', 'Pages', 'Part des 458 pages', 'Valeurs distinctes'], [
            ['14 chiffres : format SIRET', counts[14], pct(counts[14]), sum(len(x) == 14 for x in values)],
            ['9 chiffres : format SIREN', counts[9], pct(counts[9]), sum(len(x) == 9 for x in values)],
            ['Absent de la page', counts[0], pct(counts[0]), 'Sans objet'],
            ['Total', 458, '100,00 %', f'{len(values)} identifiants clients renseignés']]),
        '**Distinction essentielle :** le SIRET de l’émetteur ne doit pas être attribué aux destinataires. '
        'Les valeurs de 9 chiffres restent transcrites telles qu’elles apparaissent sous le libellé « SIRET client » ; '
        'leur longueur correspond au format SIREN, mais ne fournit pas un SIRET d’établissement à 14 chiffres. '
        'Aucun suffixe NIC n’est reconstitué. « Format SIRET » décrit ici uniquement une longueur de 14 chiffres. '
        'Aucune vérification de clé, de registre, d’existence ou de titularité n’a été effectuée.',
        '« Absent » signifie que la page ne porte pas de champ « SIRET client » renseigné dans le texte extrait. '
        'Aucun identifiant n’est imputé à partir d’une autre source. Les identifiants transcrits sont stables '
        'pour chacun des 86 codes client au sein de ce PDF.',
        '## 3. Répartition par société destinataire et code client',
        'Classement alphabétique sur la dénomination transcrite, puis sur le code. '
        'Chaque ligne conserve le code client pour éviter les fusions non démontrées. '
        'Le nombre de factures correspond aux numéros distincts dans chaque groupe.',
    ]
    company_rows = []
    for (name, code), group in sorted(by_company.items(), key=lambda kv: (kv[0][0].casefold(), kv[0][1])):
        value = group[0]['identifiant_client_transcrit']
        company_rows.append([name, f'`{code}`', f'`{value}`' if value else 'Absent', kind(value),
                             len(group), len({r['facture'] for r in group}), compact(r['page'] for r in group)])
    parts += [table(['Destinataire transcrit', 'Code client', 'Champ « SIRET client »', 'Qualification',
                     'Pages', 'Factures distinctes', 'Pages PDF'], company_rows),
              '**Total : 458 pages et 455 factures distinctes, réparties sur 86 lignes de classement.**',
              '## 4. Répartition par SIRET et par identifiant client transcrit',
              '### 4.1. Émetteur',
              table(['Société', 'SIRET transcrit', 'Pages', 'Pages PDF'],
                    [['SAS ALMU', '`81816735500010`', 458, '1–458']]),
              '### 4.2. Destinataires : valeurs renseignées',
              'Les deux catégories sont séparées pour ne pas présenter une valeur de 9 chiffres comme un SIRET complet.']
    for length, title in [(14, 'SIRET clients de 14 chiffres'), (9, 'Identifiants de 9 chiffres, au format SIREN')]:
        value_rows = []
        for value in sorted(v for v in by_value if len(v) == length):
            group = by_value[value]
            labels = '; '.join(sorted({r['destinataire'] + ' (code ' + r['code_client'] + ')' for r in group}))
            value_rows.append([f'`{value}`', labels, len(group), compact(r['page'] for r in group)])
        parts += [f'#### {title}', table(['Identifiant transcrit', 'Destinataire et code', 'Pages', 'Pages PDF'], value_rows)]
    parts += ['### 4.3. Destinataires sans identifiant client sur la page',
              f'**{counts[0]} pages**, concernant **{sum(not group[0]["identifiant_client_transcrit"] for group in by_company.values())} '
              'couples dénomination/code. Les lignes « Absent » du tableau de la section 3 donnent le détail par destinataire.',
              '**Pages concernées :** ' + compact(r['page'] for r in by_value['']) + '.',
              '## 5. Inventaire page par page',
              'Pour **chacune des lignes ci-dessous**, l’émetteur est **SAS ALMU**, '
              'SIRET **`81816735500010`**. La colonne « Destinataire » décrit la société, '
              'l’association ou la personne facturée. La qualification porte uniquement sur le champ client de la page. '
              'La mention « Provisoire » est reproduite lorsqu’elle figure sur la page.']
    detail_rows = []
    for r in records:
        note = 'Provisoire' if r['provisoire'] else '—'
        if r['facture'] == 'FA0463':
            note += f' ; volet {r["page"] - 374}/4 de FA0463'
        detail_rows.append([r['page'], r['facture'], r['date'], r['destinataire'],
                            f'`{r["code_client"]}`', f'`{r["identifiant_client_transcrit"]}`' if r['identifiant_client_transcrit'] else 'Absent',
                            r['qualification'], note])
    parts += [table(['Page PDF', 'Facture', 'Date portée', 'Destinataire', 'Code client',
                     'Champ « SIRET client »', 'Qualification', 'Observation'], detail_rows),
              '## 6. Points de rapprochement et limites',
              '- **IBS TRANSPORT ET SERVICES** apparaît sous le code **042** sur 6 pages et le code **082** '
              'sur la page **298**. La dénomination est identique, mais aucun SIRET client ne permet de démontrer '
              'l’identité juridique des deux comptes. Ils restent séparés dans la répartition par code.\n'
              '- **SARL KATY** (024 ; pages 1, 4) et **KATY** (092 ; pages 363, 413, 443) restent distincts. '
              'Le PDF ne fournit pas d’identifiant client pour les rapprocher.\n'
              '- **SAM THAI** (052 ; 6 pages ; identifiant absent) et **SAM THAI (LIMITESS)** '
              '(072 ; pages 232, 313, 380 ; valeur `844734277`) restent distincts.\n'
              '- **STM** (063) et **R-STM** (097) restent distincts. Aucun identifiant client n’est renseigné pour ces deux comptes.\n'
              '- Les pages 375 à 378 sont les quatre volets de la même facture FA0463, '
              'et ne sont pas comptées comme quatre factures distinctes.\n'
              '- Les graphies des destinataires sont conservées, avec normalisation des espacements typographiques '
              '(notamment « R M D P » rendu « RMDP » en page 30). Les comptes Sage ne sont pas assimilés '
              'automatiquement à des sociétés juridiquement distinctes.\n'
              '- Cette analyse décrit le contenu documentaire du PDF. Elle ne détermine ni l’authenticité '
              'des factures, ni leur règlement, ni l’origine ou les conditions de création du fichier.',
              '## 7. Méthode, contrôles et reproductibilité',
              'Extraction de la couche texte native avec Poppler `pdftotext`, sans OCR, '
              'selon trois modes : `-layout`, `-raw` et `-bbox-layout`. '
              'Le premier fournit les lignes du tableau ; le deuxième contrôle sur les 458 pages '
              'le destinataire, le numéro de facture, la date, le code client et la valeur du champ client ; '
              'le troisième contrôle le bloc destinataire par coordonnées et les cases facture/date/client, '
              'ainsi que la présence ou l’absence du champ « SIRET client ». '
              'Le SIRET émetteur est relevé et contrôlé sur les 458 pages. '
              'Ces trois extractions proviennent de la même couche texte et ne constituent pas trois sources indépendantes.',
              f'Contrôle visuel complémentaire effectué sur **14 pages** : {compact(visual_pages)}. '
              'Les en-têtes, destinataires et champs client de cet échantillon ont été comparés aux rendus, '
              'notamment les deux SIRET clients de 14 chiffres et les quatre volets de FA0463. '
              'Les autres pages ont fait l’objet des contrôles textuels et géométriques systématiques, '
              'sans relecture visuelle manuelle exhaustive.',
              'Contrôles de couverture : 458 positions uniques, aucune page non affectée, '
              'sommes des regroupements égales à 458, 455 numéros de facture distincts, '
              'une seule facture présente sur plusieurs pages (FA0463), '
              'et empreinte du PDF inchangée entre le début et la fin de l’extraction.',
              'L’instruction du projet privilégie la VM SIFT. La connexion au service SSH local '
              '`sift` a échoué (connexion refusée sur le port 2222) ; les traitements ont donc été '
              'effectués avec les outils Poppler locaux. Cette indisponibilité ne bloque pas '
              'l’extraction documentaire en lecture seule.',
              'Fichiers associés : [données page par page](sage-repartition-pages.csv), '
              '[données JSON](sage-repartition-pages.json), [script d’analyse](analyser_sage.py), '
              '[contrôles et provenance](controle-analyse.json), '
              '[empreintes des livrables](SHA256SUMS.txt). '
              'Les rendus de contrôle sont conservés dans `controle-visuel/`.',
              'Pour reproduire dans un **nouveau dossier** :\n\n```sh\n'
              f"python3 analyser_sage.py '{source}' /tmp/nouvelle-analyse-sage\n```\n\n"
              'Le script conserve les valeurs comme chaînes de caractères pour préserver les zéros des codes clients. '
              'Le CSV utilise le point-virgule ; lors de son import dans un tableur, '
              'choisir le type Texte pour les codes et identifiants. '
              'La reproduction automatise les extractions et contrôles ; les 14 rendus et leur relecture visuelle '
              'relèvent du contrôle complémentaire documenté ci-dessus.']
    report = '\n\n'.join(parts) + '\n'
    files = {'rapport-repartition-sage-458-pages.md': report,
             'sage-repartition-pages.json': json.dumps(records, ensure_ascii=False, indent=2) + '\n'}
    buffer = io.StringIO(newline='')
    writer = csv.DictWriter(buffer, fieldnames=list(records[0]), delimiter=';')
    writer.writeheader()
    writer.writerows(records)
    files['sage-repartition-pages.csv'] = '\ufeff' + buffer.getvalue()
    checks = dict(source=str(source), sha256_before=before, sha256_after=after,
                  source_bytes=source.stat().st_size,
                  analysed_at_utc=datetime.now(timezone.utc).isoformat(),
                  pages=458, distinct_invoices=455, distinct_names=len(names),
                  distinct_client_codes=len(codes), distinct_nonempty_client_values=len(values),
                  pages_by_client_value_length=dict(counts),
                  provisional_pages=sum(r['provisoire'] for r in records),
                  layout_raw_bbox_crosscheck_pages=458,
                  source_unchanged=before == after,
                  visual_sample_pages=visual_pages,
                  visual_sample_note='Rendus et relecture manuelle dans la session initiale, hors script.',
                  pdftotext_version=subprocess.run(['pdftotext', '-v'], capture_output=True, text=True).stderr.strip())
    files['controle-analyse.json'] = json.dumps(checks, ensure_ascii=False, indent=2) + '\n'
    # Création exclusive : préserver les résultats d'une analyse précédente.
    for name in files:
        if (out / name).exists():
            raise FileExistsError(out / name)
    for name, content in files.items():
        with (out / name).open('x', encoding='utf-8', newline='') as f:
            f.write(content)
    print(json.dumps(checks, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
