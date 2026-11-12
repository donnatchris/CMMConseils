import pathlib,mailbox,email.utils,datetime,collections,json,hashlib
out=pathlib.Path('/home/sansforensics/analysis/OP-01/operations-28oct-20261014');summary=[]
terms=['archive_saddedine','inventaire_saddedine','rejets_saddedine','l16b','kingston']
for folder in ['pst-93300','pst-dmm']:
 records=[]
 for f in (out/folder).rglob('*'):
  if not f.is_file() or f.name!='mbox':continue
  box=mailbox.mbox(f,create=False);dates=[];n=0;hits=[];day=[];attach=collections.Counter()
  for msg in box:
   n+=1;date=msg.get('Date','');iso=None
   try:
    dt=email.utils.parsedate_to_datetime(date)
    if dt.tzinfo:iso=dt.astimezone(datetime.timezone.utc).isoformat();dates.append(iso)
   except (ValueError,TypeError,OverflowError):pass
   names=[part.get_filename() for part in msg.walk() if part.get_filename()]
   for name in names:attach[pathlib.Path(name).suffix.lower()]+=1
   matched=set()
   for part in msg.walk():
    if part.get_content_maintype()=='text':
     body=part.get_payload(decode=True)
     if body:
      text=body.decode(part.get_content_charset() or 'utf-8',errors='replace').lower()
      matched.update(t for t in terms if t in text)
   headers=str(msg.items()).lower();matched.update(t for t in terms if t in headers or any(t in name.lower() for name in names))
   if matched:hits.append({'index':n,'message_id':msg.get('Message-ID'),'date_header':date,'date_utc':iso,'terms':sorted(matched),'attachments':names})
   if iso and '2024-10-28T' in iso:day.append({'index':n,'message_id':msg.get('Message-ID'),'date_header':date,'date_utc':iso,'attachments':names})
  records.append({'path':str(f.relative_to(out)),'messages':n,'dated_messages':len(dates),'date_min_utc':min(dates) if dates else None,'date_max_utc':max(dates) if dates else None,'date_28_utc':day,'target_hits':hits,'attachment_extensions':dict(attach),'sha256':hashlib.file_digest(f.open('rb'),'sha256').hexdigest()})
 summary.append({'pst':folder,'folders':records})
(out/'pst-summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
for s in summary: print(s['pst'],'folders',len(s['folders']),'messages',sum(r['messages'] for r in s['folders']),'target_hits',sum(len(r['target_hits']) for r in s['folders']),'28utc',sum(len(r['date_28_utc']) for r in s['folders']))
