#!/usr/bin/env python3
import json,mailbox,re,hashlib
from pathlib import Path
base=Path('/home/sansforensics/analysis/complement-20261017');hits=json.loads((base/'resultats/messageries-cibles.json').read_text());out=[]
def clean(s):
 s=re.sub(r'https?://\S+','[URL masquée]',s,flags=re.I)
 s=re.sub(r'[\w.+-]+@[\w.-]+','[adresse masquée]',s)
 return re.sub(r'\d{4,}','[nombre masqué]',s)
for x in hits:
 m=mailbox.mbox(x['source'],create=False)[x['mbox_key']];texts=[]
 for p in m.walk():
  if p.get_content_type()=='text/plain':
   t=(p.get_payload(decode=True) or b'').decode(p.get_content_charset() or 'utf-8',errors='replace');texts.append(clean(t))
 out.append({'message_id_sha256':x['message_id_sha256'],'date':x['date_header'],'subject':clean(str(m['Subject'])),'sender_domain':str(m['From']).split('@')[-1].strip('> '),'body_redacted':'\n'.join(texts)[:12000]})
p=base/'resultats/rescue-context-redacted.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2));p.chmod(0o600);print(p.read_text())
