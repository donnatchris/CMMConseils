import pathlib,re,json,collections,datetime
root=pathlib.Path(__file__).resolve().parents[1];rows=[];coverage=[]
for p in sorted((root/'raw/Windows/INF').glob('setupapi*.log')):
 text=p.read_text(errors='replace');dates=re.findall(r'Section start (\d{4}/\d{2}/\d{2} [\d:.]+)',text);coverage.append({'source':p.name,'sections':len(dates),'first_local_unqualified':min(dates) if dates else None,'last_local_unqualified':max(dates) if dates else None})
 for block in re.split(r'(?m)(?=^>>>  \[)',text):
  if not block.startswith('>>>'):continue
  header=block.splitlines()[0]
  if not re.search(r'USBSTOR|VID_1058|PHILIPS|Disk&Ven_|CT2000X9SSD9',header,re.I):continue
  dates=re.findall(r'(?:Section start|Section end) ([\d/ :.]+)',block)
  rows.append({'source':p.name,'header':header,'dates_local_unqualified':dates,'text':block})
(root/'setupapi-usb-sections.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(root/'setupapi-coverage.json').write_text(json.dumps(coverage,indent=2));print('USB sections',len(rows));print(coverage)
for r in rows:
 if '1058' in r['text'] or any('2024/10/28' in d or '2024/10/15' in d for d in r['dates_local_unqualified']):print(r['source'],r['header'],r['dates_local_unqualified'])
