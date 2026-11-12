from pathlib import Path
import json,hashlib,email.utils,datetime,collections,html,re
from zoneinfo import ZoneInfo
B=Path('investigations/20261109-correspondances-elargies');P=B/'prive'
rows={r['id']:r for r in map(json.loads,(P/'messages.jsonl').open())};groups={}
def group(ids,typ,people,topic,q):
 for i in ids.split():groups[i]={'nature':typ,'interlocuteurs':people,'sujet_analyse':topic,'question':q}
q='Vérifier la qualification de la correspondance et son exclusion effective du jeu saisi.'
group('M00720','Échange avec avocat identifié dans la signature','Mustapha Khallouki','Dissolution et radiation EXPERT 2 MOBILE ; état civil du liquidateur',q)
group('M00721','Message à un avocat avec tiers en copie','Mustapha Khallouki / expert-comptable','Clôture EXPERT 2 MOBILE ; choix du liquidateur',q)
group('M00717 M01632 M01633','Reproduction/transfert d’un échange avec avocat','Mustapha Khallouki','Dissolution EXPERT 2 MOBILE',q)
group('M02532 M02589 M02590 M02591 M02592 M04788 M04789 M04790 M04791','Échange avec avocat identifié par signature ou chaîne citée','Nicolay Fakiroff ; Olivier Legrand en copie de certains messages','ALMU : acompte, justificatif et rendez-vous',q)
group('M02611 M02723 M02724 M04806 M04839 M04840 M04841','Échange avec avocat identifié par signature ou chaîne citée','Marc-Alexandre Wahrheit','ALMU : virements et confirmations de réception',q)
group('M04854','Adresse proche à vérifier, sans correction automatique','Adresse « wahreit » distincte de « wahrheit »','ALMU : transmission d’un inventaire de matériel','Vérifier l’adresse destinataire et la qualification avant de rattacher ce message au cabinet Wahrheit ; contrôler la copie finale.')
group('M04466 M04468 M04473 M04474 M04478','Message adressé au cabinet identifié dans l’en-tête','Cabinet Negrevergne','DMM/BRED : audience, pièces, justificatifs ou règlement',q)
group('M04494','Destinataire incomplet : « Cabinet »','Non identifié avec certitude','Attestation comptable et préparation d’une audience','Identifier le destinataire à partir des pièces de messagerie ; examiner le filtrage si correspondance protégée.')
group('M04546 M04555','Échange à qualifier ; destinataire appelé « Maître »','Véronique Duffay','DMM/BRED : courriers, report d’audience et demande de rendez-vous','Vérifier la qualité et le rôle du destinataire ; examiner la copie finale.')
group('M04429 M04439 M04440 M04441 M04442','Échange transféré ; destinataire appelé « Maître »','Pascal Coriou','Paiements, chèques, opposition ATD ou attestation concernant un tiers','Vérifier la qualité du destinataire, le lien au périmètre de l’ordonnance et le jeu final ; ne pas présumer une correspondance avocat-client.')
group('M02074 M02075 M02077 M02079','Avis de non-remise reproduisant des destinataires et échanges','Pascoët et autres adresses de cabinets citées','DMM : audience et correspondance reproduite','Distinguer l’avis technique des échanges cités ; ne pas déduire une réception effective ; contrôler le filtrage.')
group('M06167','Notification de recommandé, sans contenu du recommandé','Charlotte Liwer via AR24','Notification à RCT','Ne pas assimiler à la lettre elle-même ; vérifier si une lettre et ses pièces figurent dans la saisie.')
group('M04479','Note personnelle préparatoire, pas échange avocat-client démontré','Message envoyé à soi-même','Commentaires sur pièces et litige DMM/BRED','Examiner le contexte et le périmètre ; ne pas déduire une protection du seul contenu juridique.')
review=[];lines=['# Tableau des messages à examiner','', 'Une ligne par message conservé ; plusieurs lignes peuvent reproduire une même conversation. Les dates ci-dessous sont celles des en-têtes converties en heure de Paris, pas des dates de saisie. Aucune ligne ne prouve une inclusion dans le jeu final. Les références complètes et les Message-ID sont dans `prive/table-messages-preuves.json`.','', '| ID | Date Paris | Nature / interlocuteurs | Sujet observé | Question |','|---|---|---|---|---|']
def clean(s):return re.sub(r'\s+',' ',html.unescape(s)).replace('|','/')
for i,g in sorted(groups.items()):
 r=rows[i]
 try:d=email.utils.parsedate_to_datetime(r['headers']['Date']).astimezone(ZoneInfo('Europe/Paris')).isoformat()
 except Exception:d=r['headers']['Date']
 source='PST dmm' if '/pst-dmm/' in r['source'] else 'PST 93300' if '/pst-93300/' in r['source'] else 'Takeout' if '::' in r['source'] else 'EML'
 review.append({'id':i,**g,'date_paris':d,'source':r['source'],'source_index':r['index'],'message_id':r['headers']['Message-ID'],'headers':r['headers'],'attachments':r['attachments'],'exported_record_sha256':hashlib.sha256(json.dumps(r,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'source_group':source})
 lines.append('| '+' | '.join(map(clean,[i,d,g['nature']+' — '+g['interlocuteurs']+' ('+source+')',g['sujet_analyse'],g['question']]))+' |')
(P/'table-messages-preuves.json').write_text(json.dumps(review,ensure_ascii=False,indent=2));(B/'tableau-messages.md').write_text('\n'.join(lines)+'\n');print('rows',len(review))
