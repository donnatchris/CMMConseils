from pathlib import Path
import hashlib
import json

ROOT = Path('/mnt/data/codeProjects/DMMConseils')
OUT = Path(__file__).resolve().parent
manifest = []

def replace(text, old, new):
    assert text.count(old) == 1, old[:100]
    return text.replace(old, new, 1)

target = ROOT/'telephones/analyse-TP-03.md'
before = target.read_bytes()
s = before.decode()
s = replace(s,
    '| Classes de protection, Mail, Fichiers et traces système | Éléments compatibles avec une activité après première authentification sous conditions ; premier déverrouillage après le démarrage constaté dans la vidéo non démontré. |',
    '| 15 octobre, 13:25–13:51 : 33 transactions Mail, cinq Fichiers et classes de protection | Activité logicielle conservée ; accès après première authentification compatible sous conditions, sans déverrouillage daté, partage, enregistrement ou impression PDF démontrés. |')
s = replace(s,
    'Les **26 exemplaires PDF TP-03**, la base TipKit de Mail et le modèle clavier sont de **classe C (`ProtectionClass=3`)** dans l’état sauvegardé : leur contenu est protégé jusqu’à la première authentification après redémarrage. Les fichiers TCC, PeopleSuggester, les préférences coreduetd et FrontBoard contrôlés sont de **classe D (`ProtectionClass=4`)** ; leur seule présence ne démontre pas la levée de la protection de classe C. Après une première authentification, AFU ne signifie pas que l’écran est actuellement déverrouillé.',
    'Les **26 exemplaires PDF TP-03**, les bases TipKit de **Mail et de Fichiers** et le modèle clavier sont de **classe C (`ProtectionClass=3`)** dans l’état sauvegardé. La classe C est une catégorie de protection iOS : **sur un appareil protégé par un code, le contenu de ces fichiers reste inaccessible jusqu’au premier déverrouillage après un redémarrage**. Après cette première authentification, il peut rester accessible aux traitements logiciels même si l’écran est de nouveau verrouillé, jusqu’à l’arrêt ou au redémarrage suivant. Un état **AFU** (*After First Unlock*, après le premier déverrouillage) ne signifie donc pas que l’écran est actuellement déverrouillé ; **BFU** (*Before First Unlock*) désigne l’état précédant cette première authentification. [Documentation Apple](https://developer.apple.com/documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication).\n\nLes fichiers TCC, PeopleSuggester, les préférences coreduetd et FrontBoard contrôlés sont de **classe D (`ProtectionClass=4`)** ; leur seule présence ne démontre pas la levée de la protection de classe C.')
s = replace(s,
    'Mail conserve une première transaction à **13:25:30,661993** et le modèle clavier une mise à jour à **13:35:42,098506**.',
    'Mail conserve une première transaction à **13:25:30,661993**, Fichiers à **13:29:50,324222**, et le modèle clavier une mise à jour à **13:35:42,098506**.')
mail_row = '| TipKit de Mail | **33 transactions, 8164–8196**, de **13:25:30,661993 à 13:29:09,106157** ; 35 mises à jour de règles et 13 de paramètres | Activité logicielle attribuée à Mail ; pas de message envoyé, PDF produit ou application au premier plan démontrés. Les deux conseils ont `ZLASTDISPLAYED=NULL`. Aucune transaction sélectionnée à 13:41–13:50. |'
s = replace(s, mail_row, mail_row+'\n| TipKit de Fichiers | **Cinq transactions, 254–258**, de **13:29:50,324222 à 13:29:50,341425**, attribuées au processus `Files` / `com.apple.DocumentsApp` ; sept changements de règles | Activité logicielle attribuée à Fichiers ; aucun document, ouverture, enregistrement ou partage identifié. Les tables actuelles de donations et d’événements sont vides ; l’unique conseil a `ZLASTDISPLAYED=NULL`. |')
s = replace(s,
    'TP-02 ne conserve aucune ligne TCC correspondante ni transaction Mail dans la fenêtre **13:20–14:05** examinée. Cette différence précise les états sauvegardés ; elle ne prouve pas l’absence passée de toute activité TP-02. **Des traces propres à Mail et Fichiers existent avant la séquence des PDF, mais aucun événement indépendant ne les relie directement aux 17 contenus.** Une coïncidence temporelle ne suffit pas à démontrer leur consultation ou partage.',
    '**Contrôle ciblé du 16 novembre 2026, fenêtre 13:25–13:51.** Les cinq transactions Fichiers ci-dessus complètent la synthèse antérieure. Les lignes `ACHANGE` 403–409 concernent exclusivement `CoreRuleRecord` ; le texte actuel du conseil relatif au partage familial ne prouve ni son affichage ni un partage. La base TipKit Fichiers est elle aussi de classe C. Les requêtes sur SIFT, en lecture seule sans rejeu WAL, confirment les 33 transactions Mail et les 17 attributs de dernière utilisation des PDF ; les 20 fichiers suivis ont des SHA-256 avant/après identiques, et le complément Fichiers confirme également l’intégrité de sa base et du manifeste. La [note de vérification](../inventaire-DNEF/documents-recus/verification-20241015-1325-1351/Note_reponse_TP02_TP03_15oct2024.md) conserve les requêtes, résultats et empreintes.\n\nTP-02 ne conserve aucune ligne TCC correspondante ni transaction Mail dans la fenêtre **13:20–14:05** précédemment examinée ; le nouveau contrôle ne retrouve aucune transaction TipKit Mail ou Fichiers sur **13:25–13:51**, ni attribut de dernière utilisation des PDF contrôlés dans ce créneau. Cette différence précise les états sauvegardés ; elle ne prouve pas l’absence passée de toute activité TP-02. **Des traces propres à Mail et Fichiers existent avant la séquence des PDF, mais aucun événement indépendant ne les relie directement aux 17 contenus.** Aucun événement explicite du créneau ne démontre un premier déverrouillage après redémarrage, un déverrouillage d’écran, une ouverture du menu de partage, un enregistrement ou une impression PDF. Les métadonnées documentaires ne suffisent pas à établir ces gestes. Les horloges de la vidéo et des téléphones n’ont pas été étalonnées indépendamment ; leur proximité temporelle ne relie pas formellement les transactions au démarrage visible.')
index_row = '| BFU, transfert, applications, doublons et horloges | [Investigations B à E](../inventaire-DNEF/rapports/Rapport_investigations_B_C_D_E_SADEDINE-2026.md), [contrôle d’intégrité](../inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/verification-finale.json) |'
s = replace(s, index_row, index_row+'\n| Contrôle du 15 octobre, 13:25–13:51, et complément Fichiers | [Note de vérification](../inventaire-DNEF/documents-recus/verification-20241015-1325-1351/Note_reponse_TP02_TP03_15oct2024.md), [résultats SIFT](../inventaire-DNEF/documents-recus/verification-20241015-1325-1351/resultats-sift-v2.json), [complément Fichiers](../inventaire-DNEF/documents-recus/verification-20241015-1325-1351/complement-fichiers-sift.json) |')

def stage(target, before, after):
    stem = target.name
    (OUT/(stem+'.avant')).write_bytes(before)
    (OUT/(stem+'.apres')).write_text(after)
    manifest.append({'target':str(target), 'before_sha256':hashlib.sha256(before).hexdigest(), 'after':stem+'.apres', 'after_sha256':hashlib.sha256(after.encode()).hexdigest()})

stage(target, before, s)
target = ROOT/'RAPPORT-FINAL-SADEDINE-2026.md'
before = target.read_bytes()
s = before.decode()
s = replace(s,
    "Les investigations ont également retrouvé des traces de fonctionnement de certaines applications, notamment Mail et Fichiers, à partir de 13 h 25.\n\nCependant, ces traces ne permettent pas de déterminer si une personne utilisait effectivement le téléphone, ni si les documents PDF ont été ouverts ou consultés.\n\nIl n'a pas non plus été possible d'établir si TP-03 avait été déverrouillé après le démarrage constaté dans la vidéo.",
    "Le contrôle ciblé sur SIFT du **15 octobre, entre 13 h 25 et 13 h 51**, confirme dans TP-03 **33 transactions internes de Mail entre 13 h 25 min 30 s et 13 h 29 min 09 s** et identifie **cinq transactions de Fichiers à 13 h 29 min 50 s**. Elles concernent TipKit, le mécanisme de conseils applicatifs, et ne désignent aucun document. Des entrées d’accès au service cloud sont également datées de **13 h 25 min 26 s pour Mail** et de **13 h 29 min 50 s pour Fichiers**. Les sources comparables de TP-02 ne reproduisent pas cette séquence, sans que cela prouve son inactivité.\n\nLes bases TipKit de Mail et de Fichiers, ainsi que les PDF contrôlés dans TP-03, sont de **classe C** dans la sauvegarde. Cette protection iOS rend leur contenu inaccessible avant le premier déverrouillage après redémarrage, puis permet aux traitements logiciels d’y accéder même lorsque l’écran est de nouveau verrouillé. Si les transactions ont été écrites localement après le démarrage et sous cette même protection, elles supposeraient une première authentification préalable. La sauvegarde ne certifie toutefois ni ces conditions historiques ni l’absence de transport ou de restauration des données.\n\n**Aucun événement explicite ne démontre sur ce créneau un premier déverrouillage, un déverrouillage d’écran, une ouverture du menu de partage, un enregistrement ou une impression PDF.** Les traces ne prouvent pas davantage une consultation humaine des documents. La date PeopleSuggester de 13 h 41 min 02 s concerne un identifiant ; elle ne démontre pas un partage. Les horloges vidéo et téléphoniques n’étant pas étalonnées indépendamment, la proximité des heures ne suffit pas à rattacher les transactions au démarrage visible. Le [rapport TP-03, sections 7.3–7.4](telephones/analyse-TP-03.md#73-premier-déverrouillage-après-redémarrage--investigation-b) expose les résultats et leurs limites.")
s = replace(s,
    '#19-tp-03-et-inventaire-dnef--27-pdf-identifiés-origine-du-transfert-à-expliquer',
    '#19-documents-retrouvés-sur-les-iphone--des-traces-datées-du-15-octobre-2024-qui-restent-à-expliquer')
stage(target, before, s)
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
