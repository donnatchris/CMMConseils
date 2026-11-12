#!/usr/bin/env python3
"""Read the three exceptional plists without changing their source bytes.

Retain out-of-range bplist dates as explicit markers, never fabricated dates.
For XML, inspect date elements directly instead of replacing invalid year 0000.
Usage GENERAL NEW_OUTPUT. Python 3.12 on SIFT (private plistlib API pinned by source).
"""
import datetime as dt
import hashlib
import io
import json
import os
from pathlib import Path
import plistlib
import struct
import sys
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo


class TolerantDates(plistlib._BinaryPlistParser):
    def _read_object(self, ref):
        offset=self._object_offsets[ref];self._fp.seek(offset)
        if self._fp.read(1)==b'\x33':
            raw=struct.unpack('>d',self._fp.read(8))[0]
            try:return dt.datetime(2001,1,1)+dt.timedelta(seconds=raw)
            except (ValueError,OverflowError):
                result={'out_of_range_plist_date':raw,'object_ref':ref,'offset':offset}
                self._objects[ref]=result;return result
        return super()._read_object(ref)


def main():
    root,out=map(Path,sys.argv[1:3]);os.umask(0o077);out.mkdir(parents=True,exist_ok=False);results=[]
    for name in ['.GlobalPreferences_m.plist','com.apple.security.CircleJoinRequested.plist','com.apple.sleepd.plist']:
        p=root/'files/HomeDomain/Library/Preferences'/name;b=p.read_bytes();h=hashlib.sha256(b).hexdigest();row={'name':name,'bytes':len(b),'sha256':h}
        if not b:row['status']='empty'
        elif b.startswith(b'bplist00'):
            value=TolerantDates(dict_type=dict).parse(io.BytesIO(b));dates=[];invalid=[]
            def walk(v,key):
                if isinstance(v,dict):
                    if 'out_of_range_plist_date' in v:invalid.append({'key':key,**v});return
                    for k,x in v.items():walk(x,key+'/'+str(k))
                elif isinstance(v,list):
                    for i,x in enumerate(v):walk(x,key+'/'+str(i))
                elif isinstance(v,dt.datetime):dates.append({'key':key,'utc':v.isoformat(),'paris':v.replace(tzinfo=dt.timezone.utc).astimezone(ZoneInfo('Europe/Paris')).isoformat()})
            walk(value,'');row.update(status='parsed_with_explicit_out_of_range_dates',dates=dates,invalid_dates=invalid)
        else:
            tree=ET.fromstring(b);dates=[]
            for parent in tree.iter('dict'):
                children=list(parent)
                for i,x in enumerate(children):
                    if x.tag=='date':dates.append({'preceding_key':children[i-1].text if i else None,'literal':x.text})
            row.update(status='xml_date_elements_only',dates=dates)
        assert hashlib.sha256(p.read_bytes()).hexdigest()==h;results.append(row)
    (out/'results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n');print(json.dumps(results,ensure_ascii=False))


if __name__=='__main__':main()
