#!/usr/bin/env python3
"""Contrôles de livraison sur les résultats observés, puis manifeste du complément."""
import collections,hashlib,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[2];OUT=ROOT/'cartes_sd/recherche-transversale/20261016';REPORT=ROOT/'cartes_sd/analyse-cartes_sd-transversale.md'
def js(p):return json.loads(p.read_text())
def write(n,o):
 p=OUT/n
 if p.exists():
  assert js(p)==o, str(p)
 else:
  with p.open('x') as f:json.dump(o,f,ensure_ascii=False,indent=2)
x=js(OUT/'inventaires/tables-ciblees.json');assert len(x)==37
assert collections.Counter(r['card'] for r in x)=={'SD-01':21,'SD-02':3,'SD-03':13}
for r in x:
 b=(ROOT/r['source_artifact']).read_bytes();assert hashlib.sha256(b).hexdigest()==r['sha256']
an=[r for r in x if r['fat_written'].startswith('2000')];assert len(an)==11
assert all(next(t for t in r['inspection']['tracks'] if t['kind']=='soun')['cumulative_defect'] for r in an)
assert all(next(t for t in r['inspection']['tracks'] if t['kind']=='soun')['expected_last']==7 for r in an)
assert len([r for r in x if any(t['last_field']!=t['expected_last'] for t in r['inspection']['tracks'])])==17
assert len([r for r in an if any(t['chunks_outside_mdat'] for t in r['inspection']['tracks'])])==8
ex=js(OUT/'inventaires/compteurs-video-et-zones-non-indexees.json');assert len(ex['excess_video'])==7 and all(r['excess'] in (13,26) for r in ex['excess_video'])
assert len(js(OUT/'inventaires/fat-2000.json'))==20
v=js(OUT/'inventaires/verification-manifestes-historiques.json');assert v['checked']==4391 and not v['mismatches'] and not v['not_in_manifest']
tests=js(OUT/'inventaires/test-index-audio-video.json');assert len(tests)==11 and all(t['returncode']==0 and not t['stderr'] for t in tests)
ns=js(OUT/'inventaires/nal-non-indexes.json');assert [r['tests'][1]['frames']-r['tests'][0]['frames'] for r in ns]==[3,1]
assert all(t['returncode']==0 and not t['stderr'] for r in ns for t in r['tests'])
a=js(OUT/'inventaires/audio-714049800.json');assert a['samples']==2222080 and a['duration']==277.76 and not a['stderr']
assert all(r['rms']>0 for r in a['windows_1second'] if r['start_seconds']>=267)
assert js(OUT/'inventaires/ecarts-audio-video-SD02-actifs.json')['count']==3300
broken=[];checked=0
for path in [REPORT,OUT/'README.md']:
 for url in re.findall(r'\]\(([^)]+)\)',path.read_text()):
  if url.startswith(('https://','http://','#')):continue
  checked+=1
  if not (path.parent/url.split('#')[0]).exists():broken.append(url)
assert not broken,broken
context={'volume_processing':{},'historical_manifests':{},'web_references':[{'url':'https://developer.apple.com/documentation/quicktime-file-format/sample-to-chunk_atom','consulted':'2026-10-16','purpose':'Fonction de stsc ; aucune spécification de firmware caméra déduite'},{'url':'https://learn.microsoft.com/en-us/windows/win32/sysinfo/file-times','consulted':'2026-10-16','purpose':'Précision des champs FAT et temps locaux'}]}
for card,date,filename in [('01','20261015','lecture-fat-independante-v2.json'),('02','20261016','lecture-fat-v2.json'),('03','20261016','lecture-fat.json')]:
 base=ROOT/f'cartes_sd/recherche-SD-{card}'/date;p=base/'inventaires'/filename
 context['volume_processing'][card]={'source':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'entries':[e for e in js(p)['entries'] if e['path'].startswith('System Volume Information')]}
for camp,ext in [('SD-01/20261015','csv'),('SD-01/20261016-complement','csv'),('SD-02/20261016','txt'),('SD-03/20261016','txt')]:
 p=ROOT/('cartes_sd/recherche-'+camp)/('manifest-sha256.'+ext);context['historical_manifests'][str(p.relative_to(ROOT))]=hashlib.sha256(p.read_bytes()).hexdigest()
write('inventaires/contexte-transversal.json',context)
write('inventaires/controle-livraison.json',{'media_hashes':37,'anomalies_counted':17,'coupled_cases':11,'samples_expected_last_audio':7,'video_excess_cases':7,'outside_mdat_cases':8,'fat_slots':20,'historical_hash_matches':4391,'extra_frames_decoded':4,'local_links_checked':checked,'broken_links':broken,'assertions_passed':True})
files=set(OUT.rglob('*'))|set((ROOT/'cartes_sd/recherche-transversale/20261016-essais').rglob('*'))|set((ROOT/'cartes_sd/scripts').glob('sd_transversal*.py'))|{REPORT}
manifest=OUT/'manifest-sha256.txt'
expected=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+str(p.relative_to(ROOT))+'\n' for p in sorted(files) if p.is_file() and p!=manifest)
if manifest.exists():
 assert manifest.read_text()==expected, 'Manifeste courant différent ; contrôler les changements avant clôture.'
else:
 with manifest.open('x') as f:f.write(expected)
print('Contrôles de livraison et manifeste validés.')
