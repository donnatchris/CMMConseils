#!/usr/bin/env python3
"""Produit un relevé de métadonnées uniquement, après qualification des candidats."""
from pathlib import Path
import json,hashlib,re,collections,email.utils
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
ROOT=Path('/mnt/data/codeProjects/DMMConseils')
OUT=ROOT/'ordinateur/recherche-OP-01/correspondances-avocats-20261116'
OLD=ROOT/'investigations/20261109-correspondances-elargies/prive/messages.jsonl'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
old={r['id']:r for r in map(json.loads,OLD.open())}
fresh=json.loads((OUT/'candidats-metadonnees.json').read_text())
validation=json.loads((OUT/'validation-nouveaux-decodages.json').read_text())
assert validation['total']==5875 and validation['all_headers_match']
decodage=json.loads((OUT/'decodage-sift.json').read_text())
expected={Path(x['path']).name:x['sha256'] for x in fresh['sources'] if 'path' in x}
assert all(x['returncode']==0 and x['sha256']==expected[Path(x['pst']).name] for x in decodage['sources'])
byid={i:r for r in fresh['candidates'] for i in r['previous_ids']}
GROUPS={
 'KHALLOUKI':'M00720 M00721',
 'FAKIROFF / Roosevelt Avocats':'M02532 M02589 M02590 M02591 M02592 M04788 M04789 M04790 M04791',
 'WAHRHEIT':'M02611 M02723 M02724 M04806 M04839 M04840 M04841',
 'NEGREVERGNE':'M04466 M04468 M04473 M04474 M04478',
}
def paris(s):
 try:
  d=email.utils.parsedate_to_datetime(s)
  return d.astimezone(ZoneInfo('Europe/Paris')).isoformat() if d.tzinfo else d.isoformat()+' (fuseau absent)'
 except Exception:return s

def record(i,lawyer,nature):
 r=byid.get(i)
 if r:
  h=r['headers'];src=r['source'];idx=r['index'];grp=r['source_group']
  # New decoding must preserve the identifying metadata of each selected message.
  for k in ('Date','From','To','Cc','Bcc','Subject','Message-ID'):
   assert re.sub(r'\s+',' ',h[k]).strip()==re.sub(r'\s+',' ',old[i]['headers'][k]).strip(),(i,k)
  provenance=r.get('provenance','Corpus complet vérifié')
 else:
  assert i=='M03025',i
  r=old[i];h=r['headers'];src=r['source'];idx=r['index'];grp='dmm'
  provenance='Métadonnées du décodage antérieur, source messages.jsonl empreintée ; notification annexe uniquement'
 return {'reference':i,'avocat':lawyer,'nature':nature,'date_paris':paris(h['Date']),'date_header':h['Date'],'expediteur':h['From'],'destinataires':h['To'],'cc':h['Cc'],'cci':h['Bcc'],'objet':h['Subject'],'message_id':h['Message-ID'],'source_group':grp,'source':src,'source_index':idx,'provenance':provenance}
main=[record(i,n,'Interlocuteur avocat dans les en-têtes') for n,ids in GROUPS.items() for i in ids.split()]
assert len(main)==23
near=[record('M04854','WAHRHEIT — attribution non confirmée','Adresse distincte wahreit.ma.avocat@gmail.com')]
notifications=[record('M06167','LIWER','Notification AR24, pas le contenu du recommandé'),record('M03025','DRESS / Aston','Notification DocuSign avec document joint, pas un échange direct avec Me Dress')]
carriers=[record(i,'KHALLOUKI','Transfert ou reproduction d’un échange déjà recensé') for i in 'M00717 M01632 M01633'.split()]
carriers += [record(i,'PASCOËT / RUBIO','Avis de non-remise contenant une correspondance reproduite ; réception non démontrée') for i in 'M02074 M02075 M02077 M02079'.split()]
quotes=[]
for q in byid['M02079']['quoted_headers']:
 h=q['headers']
 if 'pascoet@enkadenn-avocat.com' in h['Cc'].lower() and 'jrubio@shieldavocats.com' in h['To'].lower():
  quotes.append({'reference':'CITE-M02079','avocat':'RUBIO ; PASCOËT','nature':'En-têtes du message original reproduits dans un avis de non-remise','date_paris':paris(h['Date']),'date_header':h['Date'],'expediteur':h['From'],'destinataires':h['To'],'cc':h['Cc'],'cci':h['Bcc'],'objet':h['Subject'],'message_id':h['Message-ID'],'source_group':'dmm','source':'Avis M02079, en-tête RFC822 reproduit','source_index':byid['M02079']['index']})
assert len(quotes)==1,len(quotes)
quotes.append({'reference':'CITE-PJ-M04468','avocat':'PASCOËT','nature':'En-tête de réponse cité dans une pièce jointe PDF ; métadonnées incomplètes','date_paris':'2024-09-03 17:36 (fuseau non indiqué dans la citation)','date_header':'Le 3 sept. 2024 à 17:36','expediteur':'Christian Pascoët <pascoet@enkadenn-avocat.com>','destinataires':'Non indiqués dans l’en-tête cité','cc':'','cci':'','objet':'Non indiqué dans l’en-tête cité','message_id':'','source_group':'dmm','source':'Pièce jointe PDF du message M04468','attachment_sha256':'2df0ac642950387aa4e9508c0e45a772fa2d9b553d11ace3f180d73749b8ba00'})
summary=[
 ('Yann SOYER',0,'Aucun interlocuteur retrouvé ; occurrence documentaire non attribuée à cet avocat.'),
 ('Laurent DE LA ROCHÈRE',0,'Aucun échange identifié.'),
 ('Jean-Charles NEGREVERGNE',5,'PST DMM : cinq messages adressés au cabinet.'),
 ('Rachel DRESS',0,'Une notification DocuSign liée à une proposition de services Aston ; voir annexe.'),
 ('Jonathan RUBIO',0,'Un message cité dans un avis de non-remise le désigne comme destinataire ; voir annexe.'),
 ('Christian PASCOËT',0,'Un message cité le désigne en copie ; une réponse du 03/09/2024 est citée dans un PDF joint.'),
 ('Jean-Claude DRIE (lecture manuscrite)',0,'Aucun échange identifié ; résultats DRIEETS et Calendrier exclus comme faux positifs.'),
 ('Caroline BENVENISTE',0,'Aucun échange identifié.'),
 ('Grégory LEPROUX',0,'Aucun échange identifié.'),
 ('Charlotte LIWER',0,'Une notification AR24 dans Takeout ; voir annexe.'),
 ('Georges MEYER',0,'Mentions documentaires et homonymies non assimilées à un échange direct.'),
 ('Mustapha KHALLOUKI',2,'PST 93300 : deux messages ; trois transferts/reproductions séparés en annexe.'),
 ('Nicolay FAKIROFF / Roosevelt Avocats',9,'PST DMM ; Olivier Legrand figure dans plusieurs destinataires ou copies.'),
 ('Marc-Alexandre WAHRHEIT',7,'PST DMM ; un message à l’adresse distincte « wahreit » est séparé en annexe.'),
 ('Isabelle GUILLOU',0,'Aucun message identifié dans ces trois conteneurs ; le PDF déjà documenté dans TELEPHONES/IPHONE13_MINI est hors de ce périmètre.'),
]
# 11 names on the PV list plus five additional names (Pascoët occurs in both).
assert len(summary)==15
meta={'created_utc':datetime.now(timezone.utc).isoformat(),'corpus_counts':fresh['counts'],'direct_message_count':len(main),'summary':summary,'messages':main,'adresse_a_verifier':near,'notifications':notifications,'transferts_et_avis':carriers,'echanges_cites':quotes,'previous_metadata_source_sha256':sha(OLD),'limitations':['Les en-têtes et corps MIME décodés ont été recherchés ; les corps ne sont pas reproduits dans les livrables.','Les pièces jointes non textuelles ne font pas l’objet d’un nouvel OCR exhaustif. La pièce jointe PDF de M04468 est relevée à partir de son extraction textuelle existante.','Un zéro signifie aucun échange identifié dans ce corpus et selon cette méthode, pas une absence historique de correspondance.','Les en-têtes des messages envoyés, notifications et avis de non-remise ne prouvent pas leur réception effective.','Les destinataires enregistrés sous un nom seul sont conservés tels quels ; aucune adresse n’est inventée.']}

def clean(s):return re.sub(r'\s+',' ',str(s)).strip().replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;') or '—'
def table(rows):
 lines=['| Réf. | Avocat / cabinet | Date et heure Paris* | Expéditeur | Destinataire(s) | Cc / Cci | Objet | Source |','|---|---|---|---|---|---|---|---|']
 for r in sorted(rows,key=lambda r:(r['avocat'],r['date_paris'],r['reference'])):
  cp=r['cc']+(' ; Cci : '+r['cci'] if r['cci'] else '')
  lines.append('| '+' | '.join(clean(s) for s in [r['reference'],r['avocat'],r['date_paris'],r['expediteur'],r['destinataires'],cp,r['objet'],r['source_group']])+' |')
 return '\n'.join(lines)
lines=['# Relevé des correspondances avec les avocats — OP-01','',
 'Recherche du 16 novembre 2026 dans les deux PST et l’archive Takeout extraits d’OP-01. **Seuls les en-têtes et références sont reproduits : date, expéditeur, destinataires, copies et objet. Aucun corps de message ni contenu de pièce jointe n’est reproduit.**','',
 '**Corpus parcouru : 3 836 messages du PST DMM, 2 039 du PST 93300 et 301 de Takeout, soit 6 176 messages.** Les 30 EML extérieurs à ces trois conteneurs ne sont pas inclus.','',
 '**23 messages identifient un avocat ou son cabinet dans leurs en-têtes.** Les messages cités, transferts, notifications et l’adresse proche à vérifier sont détaillés séparément. Ce nombre ne mesure pas les conversations uniques ni les réceptions effectives.','',
 'La liste recherchée reprend les onze noms manuscrits de la [page 17 du PV](../../../docs/PV%20DE%20SAISIE.pdf), complétés par KHALLOUKI, FAKIROFF, WAHRHEIT et GUILLOU ; PASCOËT figure déjà sur la liste. La lecture « DRIE » reste signalée comme transcription manuscrite.','',
 '## Résultat par avocat','', '| Avocat recherché | Messages avec interlocuteur en en-tête | Autres traces / résultat |','|---|---:|---|']
for n,c,comment in summary:lines.append('| '+clean(n)+' | '+str(c)+' | '+clean(comment)+' |')
lines += ['', '## Messages avec interlocuteur avocat identifié dans les en-têtes','',table(main),'',
 'DMM = `dmmconseils@hotmail.com.pst` ; 93300 = `dmmconseils93300@hotmail.com.pst` ; Takeout = `takeout-20241028T114105Z-001.zip`, membre `Takeout/Mail/L16.mbox`.','',
 '*Dates des en-têtes converties en Europe/Paris, avec décalage UTC conservé. Une date citée sans fuseau n’est pas convertie. Les champs contenant seulement un nom et les adresses atypiques sont conservés tels qu’enregistrés. Un tiret indique un champ vide.','',
 '## Échanges cités dans un avis ou une pièce jointe','',
 'Le message `CITE-M02079` est reproduit sous forme d’en-têtes RFC822 dans un avis de non-remise. Il comporte Jonathan Rubio parmi les destinataires et Christian Pascoët en copie. La date de l’en-tête reproduit est retenue ; une citation textuelle imbriquée indique 18:40:26, soit sept secondes de plus. Ces traces ne prouvent pas la réception par chacun des destinataires. La citation du PDF joint ne fournit ni destinataire ni objet propres au message de Me Pascoët.','',table(quotes),'',
 '## Messages porteurs des transferts et avis de non-remise','',
 'Les dates et parties ci-dessous sont celles du message porteur, pas nécessairement celles de l’échange cité. Les transferts Khallouki reproduisent des échanges déjà recensés ci-dessus.','',table(carriers),'',
 '## Notifications de services','',table(notifications),'',
 'AR24 annonce un recommandé demandé par Charlotte Liwer ; cette notification ne fournit pas le contenu du recommandé. DocuSign annonce la finalisation du document Aston associé à Rachel Dress ; cette notification n’est pas un courriel directement envoyé par Me Dress.','',
 '## Adresse proche, attribution non confirmée','',table(near),'',
 'L’adresse `wahreit.ma.avocat@gmail.com` diffère de `wahrheit.ma.avocat@gmail.com`. Aucune correction ni attribution automatique à Me Wahrheit n’est effectuée.','',
 '## Méthode et traçabilité','',
 'Les 5 875 messages PST du corpus MIME complet conservé le 9 novembre ont été réexaminés intégralement pour les noms et adresses recherchés. Les deux PST ont aussi été redécodés sur SIFT avec `readpst -r -q -t e` (LibPST 0.6.76), dans un répertoire neuf ; tous les en-têtes du nouveau décodage ont été comparés au corpus conservé. Le ZIP Takeout a été relu directement et les en-têtes de ses 301 messages reparsés et comparés au corpus antérieur. La recherche textuelle utilise la normalisation de la casse et des accents, les variantes et adresses observées. Les candidats ont été qualifiés pour exclure les faux positifs lexicaux.','',
 'Les empreintes des deux PST et du ZIP Takeout ont été recalculées localement et concordent avec les contrôles antérieurs. Les empreintes consignées lors du nouveau décodage SIFT concordent aussi. Le redémarrage de la VM a interrompu une première validation MIME ; après redémarrage, la comparaison complète des en-têtes a pu être effectuée. Les références Mxxxxx permettent le rapprochement avec le décodage du 9 novembre ; le relevé JSON conserve aussi le dossier, l’index du message, le Message-ID et les en-têtes de date d’origine.','',
 '- [Métadonnées structurées, sans corps](releve-metadonnees.json).',
 '- [Candidats et sources du nouveau parcours, sans corps](candidats-metadonnees.json).',
 '- [Provenance du nouveau décodage PST](decodage-sift.json).',
 '- [Recherche locale sur le corpus complet](rechercher_local.py).',
 '- [Validation complète des nouveaux en-têtes PST](validation-nouveaux-decodages.json).',
 '- [Script de validation SIFT](valider_entetes_sift.py).',
 '- [Premier parcours SIFT interrompu, conservé pour traçabilité](rechercher_sift.py).',
 '- [Script de production du relevé](generer_releve.py).','']
for limit in meta['limitations']:lines.append('- '+limit)
with (OUT/'releve-metadonnees.json').open('x') as f:json.dump(meta,f,ensure_ascii=False,indent=2);f.write('\n')
with (OUT/'releve-messages.md').open('x') as f:f.write('\n'.join(lines)+'\n')
print(json.dumps({'messages_en_entete':len(main),'counts':fresh['counts'],'echanges_cites':len(quotes),'notifications':len(notifications),'transferts_avis':len(carriers),'adresse_a_verifier':len(near)},ensure_ascii=False))
