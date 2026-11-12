import pathlib,json,collections,re
root=pathlib.Path('/home/sansforensics/analysis/OP-01/fichiers-supprimes-20261013');counts=collections.Counter();exts=collections.Counter();users=collections.Counter();choices=[];special=[]
rx=re.compile(r'ldsd|l16b|takeout|gdrive|whatsapp|appleid|phish|rescue|logmein|anydesk|teamviewer|screenconnect|rustdesk|ultraview|tightvnc|ultravnc|realvnc|radmin|splashtop|remotepc|dwagent|meshagent|netsupport|ngrok|rclone|winscp|filezilla|exfil|consolehost_history|transfer',re.I)
useful={'.pdf','.doc','.docx','.xls','.xlsx','.ppt','.pptx','.odt','.ods','.zip','.7z','.rar','.pst','.ost','.mbox','.eml','.msg','.lnk','.url','.rdp','.bat','.cmd','.ps1','.vbs','.vbe','.hta','.py','.sql','.sqlite','.db','.txt','.csv','.log','.json','.xml','.html','.htm','.exe','.dll','.dat','.pf'}
for line in (root/'mft-deleted-records.jsonl').open():
 r=json.loads(line);counts['selected']+=1;counts['allocated' if r['allocated'] else 'unallocated']+=1
 if r['directory']:counts['directories']+=1;continue
 if r['base_reference']:counts['extension_records']+=1;continue
 names=[n for n in r['names'] if n['namespace']!=2] or r['names']
 if not names:counts['no_name']+=1;continue
 n=names[0];path=n['path'];ext=pathlib.PureWindowsPath(n['name']).suffix.lower();exts[ext]+=1;uncertain=any(x['parent_sequence_uncertain'] for x in names);knownuser=any(x['path'].startswith('Users\\') and not x['parent_sequence_uncertain'] for x in names);knownsystem=any(x['path'].startswith(('Windows\\','Program Files\\','Program Files (x86)\\')) and not x['parent_sequence_uncertain'] for x in names);recycle=any('$Recycle.Bin' in x['path'] and not x['parent_sequence_uncertain'] for x in names)
 if knownuser:counts['known_user_files']+=1;users['\\'.join(path.split('\\')[:4])]+=1
 if uncertain:counts['uncertain_parent_files']+=1
 attrs=[a for a in r['data_attributes'] if a['stream']==''];size=max((a.get('logical_size',0) for a in attrs),default=0);reasons=[]
 if knownuser:reasons.append('user_path')
 if recycle:reasons.append('recycle_bin')
 if rx.search(path) and not knownsystem:reasons.append('target_name')
 if uncertain and ext in useful and ext not in ['.dll','.exe','.dat','.json','.xml','.html','.htm','.log','.txt','.db']:reasons.append('orphan_document_or_script')
 if not knownsystem and ext in ['.pf','.lnk','.rdp','.url','.ps1','.bat','.cmd','.vbs','.hta','.eml','.msg','.pst','.ost','.mbox']:reasons.append('execution_or_mail_artifact')
 if reasons and (not r['allocated'] or recycle):
  r.update({'preferred_path':path,'parent_uncertain':uncertain,'extension':ext,'logical_size_from_mft':size,'selection_reasons':reasons});choices.append(r)
  if any(k in reasons for k in ['target_name','recycle_bin','execution_or_mail_artifact']):special.append({'mft_index':r['mft_index'],'path':path,'size':size,'SI':r['SI'],'reasons':reasons})
choices.sort(key=lambda r:(not 'recycle_bin' in r['selection_reasons'],not 'target_name' in r['selection_reasons'],not 'execution_or_mail_artifact' in r['selection_reasons'],not 'user_path' in r['selection_reasons'],r['mft_index']))
(root/'recovery-selection.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in choices));(root/'triage-summary.json').write_text(json.dumps({'counts':counts,'extensions':exts,'user_groups':users,'selected_for_recovery':len(choices),'selected_logical_bytes':sum(r['logical_size_from_mft'] for r in choices),'selection_reasons':collections.Counter(k for r in choices for k in r['selection_reasons'])},indent=2));(root/'priority-names.json').write_text(json.dumps(special,ensure_ascii=False,indent=2));print('COUNTS',counts,'selection',len(choices),flush=True)
