from pathlib import Path
import json
old=Path('/home/sansforensics/analysis/elargi-20261109-v2');new=Path('/home/sansforensics/analysis/elargi-20261109-final');new.mkdir(exist_ok=False);(new/'extracted').mkdir()
for name in ['blobs','messages.jsonl','references.jsonl','sources.json','blobs.json','blobs-expanded.json','archive-edges.json','archive-limits.json']:(new/name).symlink_to(old/name)
rows=[json.loads(x) for x in (old/'extraction.jsonl').open()];(new/'extraction-initiale.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
for x in rows:(new/'extracted'/(x['sha256']+'.txt')).symlink_to(old/'extracted'/(x['sha256']+'.txt'))
print('preserved',len(rows))
