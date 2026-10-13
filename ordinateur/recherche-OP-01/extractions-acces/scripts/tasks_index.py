import pathlib,json,xml.etree.ElementTree as E,re
root=pathlib.Path(__file__).resolve().parents[1];base=root.parent/'reveil-16oct/tasks';rows=[]
for p in sorted(base.rglob('*')):
 if not p.is_file():continue
 row={'source':str(p.relative_to(base))}
 try:
  t=E.fromstring(p.read_bytes());row['author']=t.findtext('.//{*}Author');row['registration_date']=t.findtext('.//{*}Date');row['actions']=[{n.tag.rsplit('}',1)[-1]:n.text for n in action} for action in t.findall('.//{*}Actions/*')]
 except Exception as ex:row['error']=str(ex)
 rows.append(row)
(root/'tasks-actions.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));rx=re.compile(r'anydesk|teamviewer|screenconnect|rustdesk|ultraview|tightvnc|ultravnc|realvnc|radmin|splashtop|remotepc|logmein|dwagent|meshagent|netsupport|ngrok|rclone|winscp|filezilla|ldsd|lmiruntime',re.I);print('tasks',len(rows),'errors',sum('error' in r for r in rows),'tool matches',sum(bool(rx.search(json.dumps(r))) for r in rows))
for r in rows:
 if re.search(r'powershell|cmd\.exe|wscript|cscript|mshta',json.dumps(r.get('actions',[])),re.I):print(r['source'],r.get('actions'))
