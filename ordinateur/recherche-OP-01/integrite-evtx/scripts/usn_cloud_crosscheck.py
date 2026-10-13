import pathlib,json,struct,datetime,collections
root=pathlib.Path(__file__).resolve().parents[1]/'ntfs';mft=[json.loads(s) for s in (root/'mft-gap-records.jsonl').read_text().splitlines()];refs={r['mft_index']+(r['sequence']<<48):r for r in mft if any('iCloudPhotos' in n['path'] for n in r['names'])};b=(root/'usn-tail.bin').read_bytes();off=0;matches=[]
while off+60<=len(b):
 size,major,minor=struct.unpack_from('<IHH',b,off)
 if not size:off+=8;continue
 if major!=2 or size<60 or off+size>len(b):off+=8;continue
 frn,parent,usn,stamp=struct.unpack_from('<QQQQ',b,off+8)
 if frn in refs:
  reason=struct.unpack_from('<I',b,off+40)[0];matches.append({'mft_index':frn&0xffffffffffff,'file_reference':frn,'utc':(datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=stamp//10)).isoformat(),'reason_hex':hex(reason),'basic_info_change':bool(reason&0x8000),'data_changed':bool(reason&7)})
 off+=size
(root/'usn-cloud-crosscheck.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in matches));summary={'cloud_mft_records':len(refs),'cloud_mft_records_found_in_usn':len({r['mft_index'] for r in matches}),'usn_matching_records':len(matches),'basic_info_change_records':sum(r['basic_info_change'] for r in matches),'data_change_records':sum(r['data_changed'] for r in matches),'first_utc':min((r['utc'] for r in matches),default=None),'last_utc':max((r['utc'] for r in matches),default=None)};(root/'usn-cloud-summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
