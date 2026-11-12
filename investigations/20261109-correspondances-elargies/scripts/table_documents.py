from pathlib import Path
import json,re,collections,unicodedata
B=Path('investigations/20261109-correspondances-elargies');P=B/'prive'
native=json.loads((P/'native-complet/hits.json').read_text());docs={x['sha256']:x for x in native}
if (P/'recherche/documents.json').exists():
 for x in json.loads((P/'recherche/documents.json').read_text()):
  if 'profession' in x['hits'] or 'procedure_fiscale' in x['hits'] or x['sha256'].startswith('cadbebfd2f26'):docs.setdefault(x['sha256'],x)
# Two scanned titles were checked separately before the exhaustive OCR was stopped.
for x in json.loads((P/'blobs-expanded.json').read_text()):
 if x['sha256'].startswith(('df165f7996f1','cadbebfd2f26')):docs.setdefault(x['sha256'],x)
refs=collections.defaultdict(list)
for r in map(json.loads,(P/'references.jsonl').open()):refs[r['sha256']].append(r)
edges=json.loads((P/'archive-edges.json').read_text());parents=collections.defaultdict(list)
for e in edges:parents[e['child']].append(e)
def origins(h,seen=None):
 seen=set() if seen is None else seen
 if h in seen:return []
 seen.add(h);rr=list(refs[h])
 for e in parents[h]:rr += [{**x,'archive_member':e['name']} for x in origins(e['parent'],seen)]
 return rr
def key(s):return re.sub('/+','/',s.replace('\\','/').replace('/mnt/windows/','').removeprefix('C:/')).casefold()
mft={key(r['path']):{k:v for k,v in r.items() if k!='raw_record_hex'} for r in map(json.loads,Path('ordinateur/recherche-OP-01/extractions-acces/l16b-mft.jsonl').open())}
jl=collections.defaultdict(list)
for r in json.loads(Path('ordinateur/recherche-OP-01/operations-28oct/resultats-sift/jumplists-targets-standard.json').read_text())['matches']:
 row=r['row'];path=row.get('LocalPath') or row.get('Path') or '';jl[key(path)].append({k:row[k] for k in ['SourceFile','AppIdDescription','LocalPath','Path','LastModified','TargetCreated','TargetModified','TargetAccessed','TrackerCreatedOn'] if k in row})
pairs=json.loads(Path('ordinateur/recherche-OP-01/fichiers-supprimes/recycle-pairs.json').read_text());deleted=collections.defaultdict(list)
for x in pairs:
 for y in x['R_matches']:deleted[y['sha256']].append(x['info'])
manual={}
def put(prefixes,cat,desc,q,priority=2):
 for pre in prefixes.split():manual[pre]=(cat,desc,q,priority)
put('4993136469b4','Proposition de services d’avocats','Aston : Rachel Dress / Amélie Elmaleh, mission fiscale du 24/05/2022','Qualifier le document et vérifier sa présence ou son exclusion du jeu final.',1)
put('2df0ac642950','PDF reproduisant une correspondance','Échange avec Christian Pascoët concernant une audience et le dossier DMM/BRED','Contrôler le filtrage du contenu incorporé dans le PDF.',1)
put('2e82aa66ecbc','PDF reproduisant une correspondance','Échanges avec Isabelle Guillou, recours administratif concernant un tiers, juillet-août 2017','Qualifier la correspondance et son lien au périmètre ; contrôler la copie finale.',1)
put('1b6b6de04420 daac26f49b5c 725bad368324 d0795792876a','Courrier d’avocat adressé à l’administration','Jonathan Rubio : désignation de bénéficiaires ou prorogation de délai, septembre 2022','Distinguer d’un échange confidentiel avocat-client ; vérifier contexte et jeu final.')
put('ac91d79de0d4 acc7f970525d','Observations du contribuable','Réponse DMM à la proposition de rectification de juillet 2022','Pièce fiscale antérieure à la saisie ; ne prouve pas un usage de données saisies en octobre 2024.')
put('187198774424 d21efadbbb8e','Courrier à des experts-comptables, copies à l’administration','DMM/Audire Conseil, novembre 2023','Vérifier destinataires et contexte ; pas une correspondance avocat-client démontrée.')
put('eae492001795 f32a7f19946c','Réclamation fiscale','AMR TVA : réclamation DMM du 28/11/2023','Pièce antérieure ; ne démontre pas l’utilisation ultérieure des fichiers saisis.')
put('1c633481f133','Requête juridictionnelle','Requête DMM au TA de Montreuil, reçue le 16/06/2024','Comparer au périmètre autorisé ; ne remplace pas l’ordonnance de visite.')
put('1c7d199cf224 e320373b3d92','Pièce de procédure de plainte','Procès-verbaux de plainte de 2024 ; déclarations de la plaignante','Les déclarations contenues ne deviennent pas des faits techniques établis ; examiner lien au périmètre.')
put('241cd2899961 8d251c5a545b','Relevé bancaire mentionnant un cabinet','Mentions de paiements Aston ou Roosevelt Avocats','Un libellé de paiement ne constitue pas un échange avocat-client.')
put('9f13b7bddb34 72928b0e8822','Procès-verbal descriptif immobilier','Description de biens à saisir en 2019 ; avocats cités','Ne pas confondre avec l’ordonnance ou le PV fiscal de 2024 ; lien au périmètre à examiner.')
put('2db4bfb25592','Correspondance de gestion locative','Mention d’un recours possible à l’avocat du propriétaire','Simple mention ; pas d’échange direct avec un avocat démontré.')
put('9448b2c2987f','Faux positif pour les correspondances','CV mentionnant un stage dans un cabinet','Écarté du groupe des correspondances d’avocats.',3)
put('18743d6ffbdb a06a22c70017','Homonymie lexicale','Mention du fruit « avocat » dans un catalogue ou un guide économique','Écarté du groupe des correspondances d’avocats.',3)
put('87282ce9787d 4d9d01fe677a','Documentation générale','Circulaires relatives à la gestion des scellés','Ne documentent pas à elles seules les scellés de cette affaire.',3)
put('e1fdcb9552d6','Mention dans une publication générale','Présentation d’une personne exerçant la profession d’avocat','Écarté du groupe des correspondances d’avocats.',3)
put('b3c350873cb8','Document notarial étranger','Mention de professionnels du droit dans un document mexicain','Aucune correspondance avec un avocat de la cliente établie.',3)
put('effb9a350685','Prévisionnel scanné','Lignes de frais de notaire ou avocat dans un prévisionnel','Pas de correspondance avocat-client démontrée.',3)
put('b75f365644f7','Écritures comptables','Libellé de paiement comportant le mot avocat','Un libellé ne constitue pas une correspondance.',3)
put('3ba567b9175a 3468845746fe 37509c78b434 d9d6ce8f885f','Pièce fiscale antérieure scannée','Recouvrement, réponse contentieuse ou commission, avant octobre 2024','Documenter le contexte antérieur ; ne prouve pas un usage de fichiers saisis en octobre 2024.')
put('735e02c505d5','Pièce de procédure civile scannée','Ensemble intitulé assignation ; première page : avis de renvoi d’audience','Examiner le lien au périmètre ; ne pas assimiler les mentions générales d’avocat à un échange confidentiel.')
put('4e34b48ebcec 54b52c22805a','Courrier à des experts-comptables, copies à l’administration','Versions DOCX du courrier DMM/Audire Conseil de novembre 2023','Distinguer variantes de documents et correspondances avocat-client.')
put('32286b8f786a','Justificatif de virement','Capture de virement à Roosevelt Avocats, février 2023','Rapprocher du message parent ; ne pas assimiler à une consultation juridique.')
put('1e00d0612c04','État de frais et honoraires d’avocat','Marc-Alexandre Wahrheit, ALMU, étude de dossier et rédaction de contrat, 15/11/2022','Qualifier le document et vérifier sa présence dans le jeu final.',1)
put('6afe8dda9654','Clause contractuelle générale scannée','Contrat d’apporteur : clause de prise en charge des frais','Pas une correspondance avocat-client démontrée.',3)
put('df165f7996f1','Proposition de rectification antérieure','DMM, 29/07/2022, vérification de 2019–2020, scan de 56 pages','Éclairer le contexte antérieur ; ne remplace pas l’ordonnance de 2024 et ne prouve pas l’usage de données saisies ensuite.')
put('cadbebfd2f26','Honoraires de commissaires-priseurs judiciaires','Kapandji Morhange, ALMU, note du 27/01/2023','Ne pas classer comme honoraires d’avocat sur le seul titre.',3)
put('16c3c51983e3','Projet ou texte de plainte','Document Word intitulé plainte contre Ensenat, récit de la procédure de 2022','Distinguer les déclarations de leur preuve ; le fichier seul ne prouve pas le dépôt de la plainte.')
put('5713ecbec222','Capture de correspondance bancaire','Message relatif à l’encaissement d’un chèque destiné à un avocat','Échange avec la banque ; ne constitue pas à lui seul une consultation juridique.')
put('62014fbe2364','Présentation commerciale','Offre de services mentionnant des avocats partenaires','Pas une correspondance avocat-client démontrée.',3)
put('65dc78356e48 82f47ac459b5 00e7a749b2dc 3f013b478f6f f96c95125178 4737b27145f4','Clause contractuelle générale','Mentions de frais de recouvrement, d’honoraires ou de professions réglementées','Pas une correspondance avocat-client démontrée.',3)
put('340dab34c44b','Tableau comptable','Compte d’attente ALMU : mention de Me Wahreit et d’une cession de matériel','Rapprocher des pièces d’honoraires et du message parent ; une écriture comptable ne vaut pas consultation juridique.')
put('8988a8b8ef04','Clause contractuelle générale','Contrat DOCX : clause de frais, droits et honoraires','Pas une correspondance avocat-client démontrée.',3)
put('b6a5822e9b10','Acte de procédure civile','Avis mentionnant une ordonnance de saisie-appréhension de mai 2023','Ne pas confondre avec l’ordonnance de visite fiscale de 2024 ; vérifier le rattachement au périmètre.')
def classify(x):
 if x['sha256'][:12] in manual:return manual[x['sha256'][:12]]
 n=' '.join(x['names']).lower();n=''.join(c for c in unicodedata.normalize('NFKD',n) if not unicodedata.combining(c))
 if any(w in n for w in ['avis_d','impot','ir_','2020.pdf','2021.pdf']):return ('Avis fiscal / formule générale','Mention standard de la proposition de rectification','Ne constitue pas la proposition de rectification recherchée.',3)
 if 'previsionnel' in n:return ('Prévisionnel','Ligne de frais de comptable, avocat ou notaire','Pas un échange avocat-client démontré.',3)
 if x['sha256'] in {y['sha256'] for y in native}:return ('Clause ou information générale','Contrat, assurance ou conditions générales mentionnant des avocats','Écarté des correspondances ; le mot seul ne suffit pas.',3)
 return ('Candidat supplémentaire à vérifier','Résultat de recherche OCR ou autre format','Lecture de contrôle nécessaire ; aucune qualification juridique automatique.',2)
lines=['# Tableau des documents repérés','', 'Une ligne par contenu binaire distinct (SHA-256). Les doublons exacts partagent une ligne ; des variantes de PDF au texte identique peuvent avoir des empreintes différentes. Le classement est technique et documentaire, pas une décision de protection juridique. La présence dans le jeu définitivement saisi reste inconnue pour chaque ligne.','', '| Identifiant SHA-256 abrégé | Fichier(s) | Nature | Sujet / constat | Question / suite |','|---|---|---|---|---|'];details=[]
def cl(t):return re.sub(r'\s+',' ',t).replace('|','/')
for h,x in sorted(docs.items(),key=lambda item:(classify(item[1])[3],item[0])):
 cat,desc,q,priority=classify(x);rr=origins(h);paths=sorted({r['source'] for r in rr if r.get('standalone')});tr=[{'path':path,'mft':mft.get(key(path)),'jumplists':jl.get(key(path),[])} for path in paths]
 details.append({'sha256':h,'names':x['names'],'category':cat,'description':desc,'question':q,'priority':priority,'origins':rr,'standalone_traces':tr,'recycle_matches':deleted[h]})
 lines.append('| '+' | '.join(cl(t) for t in [h[:12],'; '.join(x['names']),cat,desc,q])+' |')
(B/'tableau-documents.md').write_text('\n'.join(lines)+'\n');(P/'table-documents-preuves.json').write_text(json.dumps(details,ensure_ascii=False,indent=2));print('documents',len(details),'categories',dict(collections.Counter(x['category'] for x in details)))
