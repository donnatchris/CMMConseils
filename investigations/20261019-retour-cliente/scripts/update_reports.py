from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[3];C=R/'investigations/20261019-retour-cliente';changed=[]
link='../investigations/20261019-retour-cliente/compte-rendu.md'
blocks={
'ordinateur/analyse-ordinateur.md':f'''## Actualisation du 19 octobre 2026 — retour de la cliente

Le [nouveau mail](../docs/mail-2.txt) décrit l’ouverture d’OP-01 à **10 h 41**, le regroupement `C:\\L16B`, les exports Outlook/Takeout et une clé Kingston. Le prestataire confirme ne pas disposer du PV : ces éléments restent **déclarés**, sans confrontation directe au document. Le début général vers 10 h 22 et l’ouverture du PC à 10 h 41 sont des repères distincts et compatibles.

La nouvelle lecture de **359 EVTX / 275 577 enregistrements** ne trouve aucun événement du 16 au 27 octobre, ni après **19 h 20 le 28**. Les 285 rendus XML non valides ont été repris pour leurs dates/identifiants, sans perte silencieuse de couverture. Les **dix mises à la corbeille** sont revérifiées sur l’image ; métadonnées `$I` et contenus `$R` concordent avec les extractions précédentes. Le [détail complet des dix chemins et heures]({link}#4-dix-mises-à-la-corbeille--contre-lecture-directe) répond à la nouvelle demande.

Le parcours complet de la MFT retrouve **cinq fichiers iCloud** avec des dates SI/FN du 28 après 19 h 20, mais un changement MFT SI en octobre 2026 : **ces dates ne prouvent pas une utilisation locale du PC le soir du 28**. Un fichier d’appairage Apple est présent, création SI en juillet 2022, création FN/modification en décembre 2023 ; son UDID est différent de TP-02. Aucun branchement/extraction d’octobre 2024 n’en est déduit.

La différence entre la clé unique décrite et les **trois identifiants Kingston** reste non résolue. Le nom Takeout correspond à **12:41:05 Paris**, son manifeste à **12:42:33** : ces 88 secondes ne calibrent pas l’horloge Windows. ASUS_Z01RD reste non datable sur le PC ; le réveil programmé du 16 reste non corroboré. Résultats, pièces et limites : [complément du 19 octobre]({link}). Les sections historiques suivantes décrivent leurs campagnes à leur date.
''',
 'telephones/analyse-TP-02.md':f'''## Actualisation du 19 octobre 2026 — retour de la cliente

Le [mail complémentaire](../docs/mail-2.txt) et la confirmation du prestataire précisent le contexte : **PV indisponible**, ouverture des téléphones déclarée à **11 h 30**, insertion SIM à **11 h 45** sur le premier Mini, téléphones déclarés éteints puis rallumés vers 13 h 30 le 15. La date de branchement d’un appareil d’extraction reste « le 15 / le 28 ». Aucun de ces éléments n’est certifié par un PV consulté.

**TP-02 ne peut pas être rattaché avec certitude au scellé n° 3 ou n° 4.** Sa série F5466LV9V7 est confirmée par la sauvegarde ; les deux Mini rouges ne sont pas départagés par le mail. TP-01 est vert dans l’attestation, noir dans le récit du scellé n° 2. Ne pas attribuer les scellés par simple ordre numérique.

La contre-lecture ASUS conserve deux BSSID, **22:B0:A5:94:1F:AF** et **32:0D:CA:FD:68:8C**, associés à des dates du **28 octobre**. Ils ne certifient pas le point d’accès physique du **17**. Synchronisation/restauration et incertitude d’horloge ne sont toujours pas exclues. **Après 19 h 20 le 28**, l’historique comporte un appel à **19:39:46**, l’entrée ASUS un `LinkDownTimestamp` à **19:40:02**, et les caches LSC des dates vers **22:35 et 23:26**. Ces états postérieurs à la restitution déclarée ne prouvent pas la poursuite d’une intervention administrative, ni un visionnage de caméra.

Le nouveau tri du manifeste ne trouve pas de nom de pair record, d’outil d’extraction ou des applications de télécommande ciblées ; cette recherche de noms n’est pas exhaustive des logiciels inconnus. La relecture de 25 plist de profils/comptes montre notamment deux `ProfileTruth` vides et `IsSupervised=false` dans l’état conservé, sans historique complet depuis 2021. Sur OP-01, un fichier d’appairage Apple ancien est retrouvé pour **un autre UDID que TP-02**, sans connexion d’octobre 2024 démontrée.

Les catalogues et états LSC ne restituent pas l’historique des partages/réappairages depuis mars 2023. La réinitialisation de la **chambre en février 2024** est désormais explicitement déclarée, sans être techniquement démontrée. Voir les [résultats, contre-lectures et limites]({link}). Les sections antérieures gardent leur portée historique ; les nouvelles observations sont séparées de leurs contrôles d’origine.
''',
'freebox/analyse-freebox.md':f'''## Actualisation du 19 octobre 2026 — contexte client et rapprochements

Le [nouveau mail](../docs/mail-2.txt) précise une installation des caméras après mars 2023, une réinitialisation déclarée de la chambre en février 2024, un fonctionnement déclaré continu de la terrasse et l’absence connue de téléphone ASUS dans l’entourage. Ces déclarations n’identifient ni un auteur ni un point d’accès physique. Le **PV est confirmé indisponible**.

La contre-lecture TP-02 conserve deux BSSID ASUS_Z01RD avec dates d’association du **28 octobre**, sans certifier le BSSID au 17 ni le propriétaire. Le PC contient le nom dans des fragments compatibles avec un réseau visible, sans date de connexion. Aucun de ces éléments ne devient un historique de sessions Freebox depuis 2021. Les exports Freebox n’ont pas fait l’objet d’une nouvelle acquisition ; leurs limites de rétention demeurent.

Les nouvelles analyses des cartes quantifient des lacunes du corpus terrasse ; elles ne prouvent pas des accès réseau, des suppressions à distance ou une coupure de la Freebox. Les nouveaux faits et les réponses au mail sont dans le [complément du 19 octobre]({link}).
''',
'cartes_sd/analyse-cartes_sd-SD-01.md':f'''## Actualisation du 19 octobre 2026 — chambre et février 2024

La cliente précise désormais dans [mail-2.txt](../docs/mail-2.txt) que la réinitialisation observée concernait la **chambre en février 2024**, après une installation déclarée des caméras à partir de mars 2023. L’année et la pièce ne sont donc plus indéterminées. L’interface, le libellé et la date exacte de l’observation restent inconnus ; la présence déclarée d’un proche ne constitue pas une attribution technique.

La relecture de l’inventaire couvre **81 jours** de noms vidéo entre le **02/12/2023 et le 28/10/2024**, dont 16 lignes en février et 37 le 15 octobre. Elle ne reconstitue pas mars–novembre 2023 ni une continuité 24 h/24. Les anomalies du **21 février et du 1er mars** restent des défauts de dates/finalisation, **pas un reset usine ou changement de compte établi**. Leur signature existe aussi au salon dès novembre 2023. Les dates 2000 ne datent pas la captation réelle des images.

Aucun historique complet LSC de partages ou réappairages n’a été obtenu ; les états tardifs et formats opaques ne permettent pas d’exclure des changements anciens. Le **PV est confirmé indisponible**. Résultats détaillés et incidence du nouveau témoignage : [complément du 19 octobre]({link}).
''',
'cartes_sd/analyse-cartes_sd-SD-02.md':f'''## Actualisation du 19 octobre 2026 — terrasse déclarée en continu

Dans [mail-2.txt](../docs/mail-2.txt), la cliente indique que la terrasse enregistre **24 h/24 et 7 j/7** et qu’un arrêt ou effacement ne correspond pas à son usage habituel. Cette déclaration est désormais prise en compte : **les lacunes du corpus ne doivent pas être assimilées à un arrêt normal démontré**. La gestion circulaire du stockage reste fortement compatible avec la réutilisation des clusters, sans expliquer à elle seule chaque lacune.

Le nouveau calcul de l’union des intervalles des vidéos actives à nom datable donne **48,892 à 64,937 %** d’une journée de 24 h pour les journées intérieures du **6 au 11 novembre**. Il mesure la couverture nominale des fichiers conservés, pas le temps certain d’alimentation de la caméra ; les supprimés récupérés, le temporaire et le nom impossible sont exclus de ce calcul. Les dates de noms exploitables vont du 4 au 12 novembre ; le clip `20242010` reste séparément daté du **21 octobre par ses images**. Aucun enregistrement récupéré du 15 ne permet d’examiner l’intervention déclarée sur la terrasse.

La présence rapportée d’une inspectrice sur la terrasse ne relie aucune manipulation aux suppressions. Le signalement de février **2024** concerne désormais explicitement la **chambre**, sans pouvoir être transposé à SD-02. Le **PV est confirmé indisponible**. Méthode, tableaux journaliers et limites : [complément du 19 octobre]({link}).
''',
'cartes_sd/analyse-cartes_sd-SD-03.md':f'''## Actualisation du 19 octobre 2026 — salon, période ancienne et téléphones

Le [nouveau mail](../docs/mail-2.txt) demande l’examen depuis l’installation déclarée après mars 2023. La relecture des noms conservés sur SD-03 couvre **175 jours entre le 04/11/2023 et le 31/10/2024**, sans continuité garantie ; 125 lignes portent février 2024 et 65 le 15 octobre. La signature de finalisation avec date 2000 existe dès novembre 2023. Le signalement de réinitialisation en **février 2024** concerne explicitement la **chambre** ; les cas du salon sont des comparaisons techniques, pas la provenance démontrée de ce signalement.

La cliente rapporte l’allumage des téléphones vers 13 h 30 le 15 pendant son absence. La contre-lecture de l’image conservée affichant **13:30:21** montre plusieurs personnes et des objets sur une table, **sans démontrer un allumage, un branchement ni l’identité ou le rôle des personnes**. Aucun visionnage intégral ou analyse audio sémantique supplémentaire n’est revendiqué. L’erreur vidéo intermédiaire vers 13:30:05 et la fin des images vers 13:32:26 ne sont pas attribuées à ce geste déclaré.

Les enregistrements manquants du 16 au 28 ne démontrent pas leur cause. Le **PV est confirmé indisponible**. Voir la [réponse détaillée et les limites]({link}).
''',
'cartes_sd/analyse-cartes_sd-transversale.md':f'''## Actualisation du 19 octobre 2026 — nouveau périmètre déclaré

[mail-2.txt](../docs/mail-2.txt) précise **chambre, février 2024**, une installation après mars 2023 et le fonctionnement **continu de la terrasse**. L’année et la caméra du signalement de février sont désormais renseignées. Le **PV est confirmé indisponible** ; les horaires décrits dans le mail ne sont pas des constatations documentaires indépendantes.

La nouvelle relecture établit les bornes et les lacunes des inventaires : pas de couverture continue depuis mars 2023 ; SD-01 débute en décembre 2023, SD-03 en novembre 2023, SD-02 conserve principalement novembre 2024 et un clip daté du 21 octobre par ses images. L’union des intervalles nominaux SD-02 ne couvre que **48,892–64,937 %** de 24 h les 6–11 novembre. Cela établit une discontinuité du corpus, **pas sa cause ni une suppression ciblée le 15**.

Les onze défauts communs et la possibilité d’une finalisation défaillante restent étayés ; ni reset usine, ni réappairage, ni changement de compte n’est démontré. L’absence de dysfonctionnement remarqué n’exclut pas des défauts binaires dans des clips encore lisibles. Les catalogues et états LSC ne constituent pas un historique complet de partages. Résultats et tableaux : [complément du 19 octobre]({link}).
''',
'cartes_sd/analyse-cartes_sd.md':f'''## Actualisation documentaire du 19 octobre 2026

Ce document conserve le compte rendu d’acquisition. Les nouvelles analyses du retour de la cliente figurent dans le [complément du 19 octobre]({link}) et les rapports SD-01/02/03 et transversal. La cliente précise **février 2024, caméra de la chambre**, une installation après mars 2023 et un fonctionnement continu de la terrasse. Ces déclarations ne changent ni les empreintes ni les dates d’acquisition. Le **PV est confirmé indisponible** ; aucune réinitialisation ou suppression intentionnelle nouvelle n’est démontrée.
'''
}
for name,block in blocks.items():
 p=R/name;s=p.read_text();i=s.index('\n');s=s[:i+1]+'\n'+block+'\n'+s[i+1:];p.write_text(s);changed.append(name)
# Current-context corrections; historical campaign copies are preserved unchanged.
replacements={
 'cartes_sd/analyse-cartes_sd-transversale.md':[("Le mail indique seulement « en février », sans année, sans carte, interface, fichier ni champ authentifiés. Février 2024 est le périmètre demandé pour cette investigation.","Le premier mail disait « en février » sans année ni caméra. Le nouveau mail précise désormais **février 2024, caméra de la chambre** ; l’interface, le fichier et le champ d’origine ne sont toujours pas authentifiés.")],
 'cartes_sd/analyse-cartes_sd-SD-02.md':[("Le mail dit seulement « en février », **sans année**, et n'identifie pas la carte concernée par chacun des deux événements. Le complément demandé cible février 2024 ; cette année constitue le périmètre de recherche demandé, pas une précision présente dans le mail.","Le premier mail ne précisait pas l’année ni la caméra ; [le nouveau mail](../docs/mail-2.txt) indique désormais **février 2024 et la chambre**, distincte de SD-02/terrasse. Le fichier et l’interface de l’observation restent non établis.")],
 'cartes_sd/analyse-cartes_sd-SD-03.md':[("Le mail ne rattache pas chaque événement à une carte, ne nomme pas l'interface ou le fichier observé et dit seulement **« en février » sans année**. Février 2024 est le périmètre du complément demandé.","Le premier mail disait « en février » sans année. Le nouveau mail précise **février 2024 et la chambre**, sans interface ou fichier authentifié ; les anomalies SD-03 restent des éléments de comparaison."),("Elle mentionne février sans année ; le complément demande de cibler 2024.","Le nouveau mail précise désormais février 2024 et la chambre ; le premier mail ne donnait pas ces précisions.")],
 'cartes_sd/analyse-cartes_sd-SD-01.md':[("Le mail ne précise ni l'année de février, ni le logiciel ayant affiché cette date, ni un fichier ou une carte déterminée. Le complément demandé le 16/10/2026 oriente l'investigation vers **février 2024** ; cette précision ne doit pas être attribuée rétroactivement au mail.","Le premier mail ne précisait pas l’année ni la caméra. Le nouveau mail indique désormais **février 2024 et la chambre** ; cette précision ne doit pas être attribuée rétroactivement au premier mail. Le logiciel et le fichier à l’origine de l’affichage restent inconnus.")],
 'telephones/analyse-TP-02.md':[("L’année de février n’est pas précisée.","Le nouveau mail précise désormais février 2024 et la caméra de la chambre."),("**La présente mise à jour n’a pas relancé les campagnes d’investigation.**", "**La synthèse antérieure n’avait pas relancé les campagnes d’investigation. Le complément du 19 octobre comporte de nouvelles contre-lectures, documentées séparément.**")]
}
for name,pairs in replacements.items():
 p=R/name;s=p.read_text()
 for old,new in pairs:
  assert old in s,(name,old);s=s.replace(old,new)
 p.write_text(s)
# Final consolidated report: integrate new findings into its current account.
p=R/'RAPPORT-FINAL-SADEDINE-2026.md';s=p.read_text().replace('**Date du rapport :** 18 octobre 2026','**Date du rapport :** 19 octobre 2026')
s=s.replace('Cette synthèse reprend les résultats déjà documentés, en donnant priorité au compte rendu général du **17 octobre 2026** et aux conclusions actualisées. Les procès-verbaux de procédure et le journal de création de la sauvegarde du téléphone sur Mac étaient indisponibles et n’ont pas été consultés.', 'Cette synthèse intègre les résultats antérieurs et les **investigations complémentaires du 19 octobre 2026**, motivées par [le retour de la cliente](docs/mail-2.txt). Le prestataire confirme ne pas disposer du PV : les horaires et actes rapportés dans le mail restent des déclarations, sans consultation du document. Le journal de création de la sauvegarde sur Mac demeure indisponible. Les preuves et réponses détaillées sont dans le [complément du 19 octobre](investigations/20261019-retour-cliente/compte-rendu.md).')
s=s.replace('**Le 28 octobre, Windows reprend à 10 h 41 min 56 s**, environ vingt minutes après l’ouverture déclarée vers 10 h 22. Des traces de session et d’applications sont enregistrées avant la restitution déclarée ; leur rapprochement avec les actes de procédure reste à effectuer.', '**Le 28 octobre, Windows reprend à 10 h 41 min 56 s**, ce qui concorde à la minute avec l’ouverture d’OP-01 désormais déclarée à **10 h 41**. Le début général vers 10 h 22 est un repère distinct. Les actes décrits dans le nouveau mail sont compatibles avec le regroupement L16B et les exports ; le PV n’a pas été consulté.')
s=s.replace('Son mail évoque « février » sans année ; les analyses ont retenu février 2024 pour comparaison.', 'Le nouveau mail précise désormais **février 2024 et la caméra de la chambre** ; l’interface et le fichier à l’origine de l’affichage restent non établis.')
s=s.replace('| 28 octobre, vers 10 h 22 — déclaration | Matériels concernés par les scellés | Début d’ouverture indiqué par la cliente. | Repère à confronter au procès-verbal indisponible. |','| 28 octobre, vers 10 h 22 puis 10 h 41 — déclarations | Matériels, puis OP-01 | Début général puis ouverture de l’ordinateur selon les deux mails. | Repères distincts, PV confirmé indisponible. |')
insert='''### Complément du 19 octobre : après la restitution, appairages et contexte

Le récit du nouveau mail précise que `C:\\L16B` a été laissé sur l’ordinateur avec l’accord de la cliente. Cette présence est cohérente avec les opérations déclarées. L’absence de suppression dans le PV est seulement rapportée : les **dix mises à la corbeille** sont techniquement confirmées, mais aucune omission du document n’a été directement vérifiée. Le [tableau détaillé](investigations/20261019-retour-cliente/compte-rendu.md#4-dix-mises-à-la-corbeille--contre-lecture-directe) donne chaque chemin d’origine et chaque heure.

La relecture de **359 journaux Windows, soit 275 577 enregistrements**, ne retrouve aucun événement après **19 h 20 le 28**, ni du 16 au 27. Les 285 rendus XML non valides ont été repris pour leurs dates. Le contrôle complet de la MFT retrouve toutefois **cinq fichiers iCloud avec des dates anciennes après 19 h 20**, mais une modification de leur entrée MFT en 2026 : **ces métadonnées ne prouvent pas une activité locale du PC le soir du 28**. Les interactions PST du 29 déjà décrites sont également postérieures à la restitution déclarée.

Un enregistrement d’appairage Apple existe sur OP-01 pour un UDID **différent de TP-02**, avec création SI en juillet 2022 et création FN/modification en décembre 2023. Il ne démontre ni un branchement en octobre 2024 ni l’emploi d’un outil d’extraction. Les deux dates ne sont pas fusionnées en une date certaine de premier appairage.

Les trois identifiants Kingston restent à rapprocher de la **clé unique décrite par la cliente** ; la concordance de marque n’identifie pas un support physique. Le nom Takeout donne **12:41:05 Paris**, le manifeste **12:42:33** : ces 88 secondes sont compatibles avec des étapes d’export, sans permettre de calibrer l’horloge Windows.

'''
s=s.replace('## 5. Résultats concernant les téléphones',insert+'## 5. Résultats concernant les téléphones')
insert='''### Complément du 19 octobre : scellés, BSSID et traces du soir

**La correspondance TP-02/TP-03 avec les scellés n° 3/n° 4 reste indéterminée.** Les deux sont des iPhone 13 mini rouges ; la sauvegarde identifie TP-02 par sa série, mais le mail ne donne pas les séries des scellés. TP-01 est vert dans l’attestation et l’iPhone 13 du scellé n° 2 est décrit noir : rapprochement candidat, divergence non résolue. OP-01 correspond au modèle du scellé n° 1.

Deux BSSID ASUS_Z01RD sont conservés avec des associations du **28 octobre**, **22:B0:A5:94:1F:AF** et **32:0D:CA:FD:68:8C**. Ils ne certifient pas le point d’accès utilisé le **17**. Aucun propriétaire identifié ; synchronisation/restauration toujours non exclues. L’absence connue d’ASUS dans l’entourage est une déclaration, pas une identification de l’émetteur.

Des dates existent **après 19 h 20 le 28** : appel à **19:39:46**, champ `LinkDownTimestamp` ASUS à **19:40:02**, caches LSC vers **22:35 et 23:26**. Elles sont postérieures à la restitution déclarée, sans auteur établi et sans preuve de visionnage des caméras. Le tri ciblé du manifeste et la relecture de 25 plist de gestion/comptes ne révèlent pas de session d’extraction d’octobre 2024 ni d’historique complet des appareils associés depuis 2021.

La cliente rapporte un allumage des téléphones vers 13 h 30 le 15. Une image du salon à 13:30:21 ne suffit pas à prouver ce geste. La date du branchement de l’appareil d’extraction demeure « le 15 / le 28 ». Le point concernant TP-03 reste « à compléter ». Ces éléments sont conservés comme déclarations et questions ouvertes.

'''
s=s.replace('## 6. Résultats concernant la Freebox et les connexions',insert+'## 6. Résultats concernant la Freebox et les connexions')
insert='''### Complément du 19 octobre : installation en 2023 et terrasse en continu

La cliente situe l’installation après mars 2023. Les noms vidéo conservés de la chambre commencent en décembre 2023, ceux du salon en novembre 2023 ; ils ne couvrent pas continûment cette période. La terrasse conserve principalement novembre 2024 et un clip daté du 21 octobre par ses images. Les données LSC ne restituent pas une chronologie complète des partages, réappairages ou changements de compte.

La terrasse est déclarée fonctionner **24 h/24**. Le nouveau calcul de l’union des intervalles des MP4 actifs à nom datable couvre **48,892 à 64,937 %** d’une journée sur les journées intérieures du **6 au 11 novembre**. Ce sont des lacunes du **corpus conservé**, pas une mesure certaine du temps d’arrêt de la caméra. Le calcul exclut les supprimés récupérés et le temporaire ; les durées restent nominales. Les mécanismes d’enregistrement, pertes, écrasements, interruptions ou suppressions restent à départager. La réutilisation circulaire des anciennes données est distincte d’une coupure du flux. **Aucun effacement ciblé le 15 ni intervention d’une personne sur la terrasse n’est démontré.**

'''
s=s.replace('## 8. Éléments inexpliqués et limites des conclusions',insert+'## 8. Éléments inexpliqués et limites des conclusions')
s=s.replace('1. Comparer les opérations constatées sur OP-01 le **28 octobre**, dès **10 h 41 min 56 s**, avec le procès-verbal : ouverture déclarée vers 10 h 22, personnes présentes, consultations, copies, **dix mises à la corbeille** et supports utilisés.', '1. Le **PV est confirmé indisponible** : le rapprochement du 19 octobre utilise le récit de la cliente (début général vers 10 h 22, ouverture d’OP-01 à 10 h 41, téléphones à 11 h 30). Les dix mises à la corbeille, les trois identifiants Kingston, les identités des Mini et la date du branchement restent à confronter aux pièces si elles deviennent disponibles.')
s += '\n- [Complément du 19 octobre 2026 — retour de la cliente, contre-lectures et réponses détaillées](investigations/20261019-retour-cliente/compte-rendu.md).\n'
p.write_text(s);changed.append(str(p.relative_to(R)))
(C/'resultats/rapports-modifies.json').write_text(json.dumps([{'path':n,'sha256_before':hashlib.sha256((C/'rapports-avant'/n).read_bytes()).hexdigest(),'sha256_after':hashlib.sha256((R/n).read_bytes()).hexdigest()} for n in changed],ensure_ascii=False,indent=2))
print('Updated',len(changed),'reports')
