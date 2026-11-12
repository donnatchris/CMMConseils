#!/usr/bin/env python3
"""Consolidate only measured outputs; no narrative forensic report."""
import argparse
import collections
import csv
import json
import os
from pathlib import Path
import tp02_forensic as common

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--root',default='telephones/recherche-TP-02')
p.add_argument('--out',required=True)
a=p.parse_args();os.umask(0o077);root=Path(a.root);out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
inventory=root/'inventaire-detaille'
summary=json.loads((inventory/'summary.json').read_text())
logs=[]
for name in ('extraction-cameras-20261014','extraction-systeme-20261014'):
 logs.extend(json.loads(line) for line in (root/name/'extraction.jsonl').read_text().splitlines())
sqlite=[];checks=[];analysis_errors=[];temporal=[]
for name in ('analyse-cameras-20261014','analyse-systeme-finale-20261014'):
 base=root/name
 schema=json.loads((base/'sqlite-schema.json').read_text());byfile={r['file']:r for r in schema}
 with (base/'sqlite-inventory.csv').open() as f:
  for r in csv.DictReader(f):
   db=byfile.get(r['file']);r.update(schema_status='catalogued' if db else 'schema_failed',
     integrity=json.dumps(db['integrity']) if db else 'unavailable',tables=len(db['tables']) if db else '')
   sqlite.append(r)
 status=json.loads((base/'analysis-status.json').read_text())
 analysis_errors.extend(status['errors'])
 checks.extend(db for db in schema)
 with (base/'temporal-candidates.csv').open() as f:temporal.extend(csv.DictReader(f))
common.write_csv(out/'sqlite-confirmed.csv',sqlite,['file','sha256','size','signature_type','fileID','schema_status','integrity','tables'])
with (root/'chronologie-ciblee-v2-20261014/chronology-evidence.csv').open() as f:
 reader=csv.DictReader(f);fields=reader.fieldnames;chronology=list(reader)
common.write_csv(out/'chronology-expanded.csv',chronology,fields)
central=[r for r in chronology if r['central_window']!='False']
common.write_csv(out/'chronology-central.csv',central,fields)
common.write_csv(out/'sqlite-temporal-candidates.csv',sorted(temporal,key=lambda r:r['utc']),list(temporal[0]))
(out/'sqlite-schemas.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2)+'\n')
verification=json.loads((root/'verification-empreintes-20261014.json').read_text())
facts={'inventory_entries':summary['rows'],'interesting_entries':summary['interesting_files'],
 'selected_extracted':len(logs),'extraction_statuses':dict(collections.Counter(r['status'] for r in logs)),
 'plaintext_bytes':sum(r.get('size',0) for r in logs),'size_discrepancies':sum('warning' in r for r in logs),
 'sqlite_signatures':len(sqlite),'sqlite_catalogs':len(checks),'sqlite_analysis_errors':analysis_errors,
 'temporal_candidates_unvalidated':len(temporal),'targeted_observations_in_comparison_window':len(chronology),
 'targeted_observations_overlapping_central_window':len(central),
 'central_counts':dict(collections.Counter(r['observation'] for r in central)),
 'hash_rechecks_ok':verification['ok'],'hash_rechecks_total':verification['files'],
 'manifest_sha256_after':common.sha(common.MANIFEST),
 'limits_and_next_steps':[
  'Les dates et états observés ne démontrent pas automatiquement une interaction humaine sur TP-02.',
  '53 lignes CallHistory dans la fenêtre principale : vérifier synchronisation/restauration, identifiants d’origine, autres appareils et relevés opérateur avant attribution locale.',
  'Wi-Fi ASUS_Z01RD : champs concordants le 17 octobre dans deux plist ; vérifier historique normal, provenance/synchronisation et réseau physique. Un SSID ne désigne pas une personne.',
  'LSC __access_time__.json : date de panneau applicatif le 28 à 17:39:17 ; nature du panneau et cause de mise à jour à établir, pas de consultation caméra démontrée.',
  'Cinq fichiers APM LSC ne portent pas de signature SQLite ; format interne ou chiffrement applicatif à identifier. Une base health_data_center.db est vide.',
  'Inventaire fondé sur les chemins et métadonnées ; signatures vérifiées seulement pour les fichiers sélectionnés. Des bases sous des extensions exclues peuvent subsister.',
  'Photos.sqlite (835297280 octets annoncés) et médias non extraits lors de cette passe ; limites de volume explicitement appliquées.',
  '91 écarts taille manifeste/contenu extrait : documenter cohérence de la sauvegarde et confronter métadonnées, copies d’acquisition et état des fichiers ; pas de conclusion de falsification.',
  'Info.plist date 12/10/2026, Status.plist et Manifest.plist dates 18/09/2026, IsFullBackup=False : provenance et complétude de la copie à clarifier.',
  '22 contrôles SQLite quick_check non exécutables avec les collations de cette installation ; schémas lus sans substituer des collations arbitraires. Voir erreurs détaillées.',
  'Colonnes temporelles détectées par noms ; formats et unités candidats doivent être validés par schéma/source. BLOB et formats propriétaires non exhaustivement décodés.',
  'Dates plist exportées sous leur valeur date décodée ; encodage binaire d’origine conservé dans les fichiers hachés. Dates sans fuseau non extrapolées.',
  'OperatingDates utilise un mois 0..11 et un jour UTC sans heure : comparer des intervalles journaliers, pas une heure de lancement. Pas un historique de consultations.',
  'Les lectures ciblées SQLite sont immutable sans WAL ; la passe générale travaille sur des copies avec compagnons. Contrôler leur présence pour toute interprétation ciblée.',
  'Aucune trace de déverrouillage ou connexion USB historique établie ; faux positifs des recherches de noms écartés. Rechercher équivalents disponibles et données de l’ordinateur d’extraction.',
  'Comparer TP-01/TP-03, Freebox et cartes SD si acquisitions disponibles ; obtenir les procès-verbaux pour confronter les opérations et horaires déclarés.',
  'Empreintes revérifiées pour 1141 objets sources sélectionnés et contenus extraits ; cela ne remplace pas le contrôle intégral des 96 Go ni une chaîne de conservation documentée.',
  'Deux catalogues de tables AddressBook n’ont pas pu restituer toutes les colonnes avec cette installation SQLite ; voir erreurs de stade columns. Aucun scan temporel n’est déclaré exhaustif pour ces tables.'
 ]}
(out/'results-and-limits.json').write_text(json.dumps(facts,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:facts[k] for k in ('selected_extracted','plaintext_bytes','size_discrepancies','sqlite_signatures','sqlite_catalogs','targeted_observations_overlapping_central_window','hash_rechecks_ok')}))
