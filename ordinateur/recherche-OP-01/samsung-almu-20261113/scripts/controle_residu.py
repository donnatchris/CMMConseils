# À exécuter dans SIFT : comptes ciblés uniquement, aucun fragment du registre exporté.
from pathlib import Path
import hashlib,json
B=Path('/mnt/windows');O=Path('/home/sansforensics/analysis/OP-01/samsung-almu-20261113');rows=[]
for rel in ['Windows/System32/config/SYSTEM','Windows/System32/config/SYSTEM.LOG1','Windows/System32/config/SYSTEM.LOG2']:
 p=B/rel;b=p.read_bytes();rows.append({'path':rel,'size':len(b),'sha256':hashlib.sha256(b).hexdigest(),'exact_serial_ascii_count':b.lower().count(b'r58rb2etqer'),'exact_serial_utf16le_count':b.lower().count('r58rb2etqer'.encode('utf-16le'))})
(O/'registry-serial-presence.json').write_text(json.dumps(rows,indent=2))
