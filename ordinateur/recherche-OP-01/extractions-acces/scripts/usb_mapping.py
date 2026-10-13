import pathlib,json,datetime
root=pathlib.Path(__file__).resolve().parents[1];rows=json.loads((root/'registry.json').read_text());md=next(r for r in rows if r['hive']=='SYSTEM' and r['key']=='MountedDevices');result=[];dates=[]
for v in md['values']:
 if 'Volume{' not in (v['name'] or ''):continue
 guid=v['name'].split('Volume',1)[1];raw=bytes.fromhex(v['hex']);decoded=raw.decode('utf-16le','replace');mp=[r for r in rows if 'MountPoints2\\'+guid in r['key'] and r['hive'].startswith('NTUSER:')]
 if any('2024-10-28' in r.get('lastwrite_utc','') for r in mp):result.append({'mounteddevices_name':v['name'],'device_utf16':decoded,'raw_hex':v['hex'],'mountpoints_keys':mp})
for r in rows:
 if r['hive']=='SYSTEM' and '\\Enum\\USBSTOR\\' in r['key'] and '\\Properties\\{83da6326-97a6-4088-9453-a1923f573b29}\\' in r['key']:
  ts=[]
  for v in r.get('values',[]):
   b=bytes.fromhex(v['hex'])
   if len(b)==8:
    try:ts.append((datetime.datetime(1601,1,1,tzinfo=datetime.timezone.utc)+datetime.timedelta(microseconds=int.from_bytes(b,'little')//10)).isoformat())
    except OverflowError:pass
  if ts:dates.append({'key':r['key'],'property':r['key'].rsplit('\\',1)[-1],'dates_utc':ts})
(root/'usb-mounteddevices-crosscheck.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));(root/'usb-property-dates.json').write_text(json.dumps(dates,indent=2));print('matched historic volume keys',len(result),'USB property rows',len(dates))
