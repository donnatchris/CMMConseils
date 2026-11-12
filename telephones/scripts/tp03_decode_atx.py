#!/usr/bin/env python3
"""Decode the observed ATX envelope and SpringBoard LZFSE on SIFT copies.

Envelope inferred from this file, validated by complete length consumption,
45 bounded records, SQLite integrity and successful property-list parsing.
Unknown 8-byte per-record metadata is preserved, not assigned semantics.
Usage EXTRA NEW_OUTPUT. Requires isolated lzfse==0.4.2.
"""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import plistlib
import re
import sqlite3
import struct
import sys
from zoneinfo import ZoneInfo
import lzfse

P = ZoneInfo('Europe/Paris')
LO = dt.datetime(2024, 10, 16, tzinfo=P).timestamp()
HI = dt.datetime(2024, 10, 17, tzinfo=P).timestamp()
C = 978307200


def sha(b):
    return hashlib.sha256(b).hexdigest()


def encode(x):
    if isinstance(x, bytes):
        return {'bytes': len(x), 'sha256': sha(x), 'hex': x.hex()}
    if isinstance(x, dt.datetime):
        return x.isoformat()
    if isinstance(x, plistlib.UID):
        return {'UID': x.data}
    raise TypeError(type(x).__name__)


def plist_resolve(archive):
    if not isinstance(archive, dict) or archive.get('$archiver') != 'NSKeyedArchiver':
        return archive
    objects = archive['$objects']
    def resolve(v, visited=frozenset()):
        if isinstance(v, plistlib.UID):
            i = v.data
            if i == 0:
                return None
            if i in visited:
                return {'reference': i}
            return resolve(objects[i], visited | {i})
        if isinstance(v, list):
            return [resolve(x, visited) for x in v]
        if isinstance(v, dict):
            cls = objects[v['$class'].data].get('$classname') if isinstance(v.get('$class'), plistlib.UID) else None
            if cls in ['NSDictionary', 'NSMutableDictionary'] and 'NS.keys' in v:
                return {str(resolve(k, visited)): resolve(x, visited) for k, x in zip(v['NS.keys'], v['NS.objects'])}
            if cls in ['NSArray', 'NSMutableArray', 'NSSet', 'NSMutableSet']:
                return resolve(v.get('NS.objects', []), visited)
            if cls == 'NSDate' and 'NS.time' in v:
                return {'NSDate_Cocoa_seconds': v['NS.time'], 'paris': dt.datetime.fromtimestamp(v['NS.time'] + C, dt.timezone.utc).astimezone(P).isoformat()}
            return {**({'class_name': cls} if cls else {}), **{k: resolve(x, visited) for k, x in v.items() if k != '$class'}}
        return v
    return resolve(archive['$top'])


def protobuf(data, depth=0):
    """Strict wire framing only. Unknown fields have no inferred semantic names."""
    if depth > 15:
        raise ValueError('depth')
    pos, fields = 0, []
    def varint():
        nonlocal pos
        value = 0
        for shift in range(0, 70, 7):
            if pos >= len(data):
                raise ValueError('truncated varint')
            b = data[pos]; pos += 1; value |= (b & 127) << shift
            if b < 128:
                return value
        raise ValueError('varint too long')
    while pos < len(data):
        key = varint(); number, wire = key >> 3, key & 7
        if not number:
            raise ValueError('field zero')
        item = {'number': number, 'wire': wire}
        if wire == 0:
            item['integer'] = varint()
        elif wire in [1, 5]:
            size = 8 if wire == 1 else 4
            if pos + size > len(data):
                raise ValueError('truncated fixed')
            b = data[pos:pos+size];pos += size
            item.update(integer=int.from_bytes(b, 'little'), floating=struct.unpack('<d' if size == 8 else '<f', b)[0])
        elif wire == 2:
            length = varint()
            if pos + length > len(data):
                raise ValueError('truncated bytes')
            b = data[pos:pos+length];pos += length
            item.update(bytes=length, sha256=sha(b))
            try:
                text = b.decode('utf-8')
                if text and all(ch.isprintable() for ch in text):
                    item['text'] = text
            except UnicodeError:
                pass
            if 'text' not in item and b:
                try:
                    item['fields'] = protobuf(b, depth+1)
                except ValueError:
                    item['hex'] = b.hex()
        else:
            raise ValueError('unsupported wire')
        fields.append(item)
    return fields


def main():
    extra, out = map(Path, sys.argv[1:3])
    os.umask(0o077);out.mkdir(parents=True, exist_ok=False)
    path = extra/'files/HomeDomain/Library/DuetExpertCenter/D2DBackups/ATXBackupData'
    b = path.read_bytes();before = sha(b);count = struct.unpack_from('<I', b, 16)[0]
    if count > 1000:
        raise ValueError('record count')
    pos, entries, dates, schemas, native, errors = 20, [], [], {}, {}, []
    def walk(v, key, source):
        if isinstance(v, dict):
            for k, x in v.items():walk(x, key+'/'+str(k), source)
        elif isinstance(v, list):
            for i, x in enumerate(v):walk(x, key+'/'+str(i), source)
        elif isinstance(v, (int, float)) and not isinstance(v, bool):
            for name, epoch, scale in [('unix_s',0,1),('unix_ms',0,1000),('cocoa_s',C,1)]:
                if (LO-epoch)*scale <= v < (HI-epoch)*scale:
                    dates.append({'source':source,'key':key,'raw':v,'hypothesis':name,'paris':dt.datetime.fromtimestamp(v/scale+epoch,dt.timezone.utc).astimezone(P).isoformat()})
    for i in range(count):
        size = struct.unpack_from('<I', b, pos)[0];pos += 4
        name = b[pos:pos+size].decode('utf-8').rstrip('\x00');pos += size
        block_size = struct.unpack_from('<I', b, pos)[0];pos += 4
        if block_size < 8 or pos + block_size > len(b):raise ValueError('record boundary')
        metadata = b[pos:pos+8];content = b[pos+8:pos+block_size];offset=pos+8;pos += block_size
        decoded = lzfse.decompress(content) if content.startswith((b'bvx2', b'bvx1', b'bvx-', b'bvxn')) else content
        safe = re.sub('[^a-zA-Z0-9_.-]', '_', name);dest=out/f'{i:02d}-{safe}';dest.write_bytes(decoded)
        row={'name':name,'offset':offset,'encoded_bytes':len(content),'clear_bytes':len(decoded),'metadata_hex':metadata.hex(),'sha256':sha(decoded),'decoded_name':dest.name}
        if decoded.startswith(b'SQLite format 3\x00'):
            c=sqlite3.connect(dest.as_uri()+'?mode=ro',uri=True);c.row_factory=sqlite3.Row
            row['quick_check']=[list(x) for x in c.execute('pragma quick_check')]
            schemas[name]=[dict(x) for x in c.execute("select name,sql from sqlite_master where type='table'")]
            native['appInfo']=[dict(x) for x in c.execute('select bundleId,installDate,lastLaunchDate,lastSpotlightLaunchDate from appInfo order by bundleId')]
            native['appLaunchSequence']=[dict(x) for x in c.execute('select * from appLaunchSequence')]
            native['counts']={t:c.execute('select count(*) from '+t).fetchone()[0] for t in ['alog','afeedback','anchorOccurrence','appInfo','appLaunchSequence']}
            native['anchors_range']=[dict(x) for x in c.execute('select min(anchorDate) first,max(anchorDate) last from anchorOccurrence')]
            native['appInfo_sealed']=[dict(x) for x in c.execute('select bundleId,lastLaunchDate from appInfo where lastLaunchDate between ? and ?', (LO-C,HI-C))]
            for table in ['appInfo','appLaunchSequence','anchorOccurrence','alog','blobs','suggested','appActionInfo']:
                cols=[x[1] for x in c.execute('pragma table_info('+table+')') if re.search('date|time|launch|expiration|^ts$',x[1],re.I)]
                for col in cols:
                    vals=[dict(x) for x in c.execute('select '+col+' value from '+table+' where typeof('+col+") in ('integer','real')")]
                    walk(vals,table+'/'+col,name)
            # Cross-check every numeric/unspecified column, including model tables
            # whose names do not imply an application launch or a timestamp.
            numeric_candidates=[];column_count=0
            quote=lambda s:'"'+s.replace('"','""')+'"'
            for schema in schemas[name]:
                table=schema['name']
                for _,col,affinity,*_ in c.execute('pragma table_info('+quote(table)+')').fetchall():
                    if any(t in affinity.upper() for t in ['TEXT','CHAR','CLOB','BLOB']):continue
                    column_count+=1;field=quote(col);stem=' from '+quote(table)+' where typeof('+field+") in ('integer','real')"
                    minimum,maximum=c.execute('select min('+field+'),max('+field+')'+stem).fetchone()
                    if minimum is None:continue
                    for epoch_name,epoch,scale in [('unix_s',0,1),('unix_ms',0,1000),('unix_us',0,1000000),('unix_ns',0,1000000000),('cocoa_s',C,1),('cocoa_ns',C,1000000000)]:
                        low,high=(LO-epoch)*scale,(HI-epoch)*scale
                        if maximum<low or minimum>=high:continue
                        for value,n in c.execute('select '+field+',count(*)'+stem+' and '+field+'>=? and '+field+'<? group by '+field,(low,high)):
                            numeric_candidates.append({'table':table,'column':col,'raw':value,'count':n,'hypothesis':epoch_name,'paris':dt.datetime.fromtimestamp(value/scale+epoch,dt.timezone.utc).astimezone(P).isoformat()})
            native['all_numeric_columns_16oct']={'tables':len(schemas[name]),'columns':column_count,'candidates':numeric_candidates}
            c.close()
        elif decoded.startswith(b'bplist00'):
            try:
                value=plist_resolve(plistlib.loads(decoded));(out/(dest.name+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2,default=encode)+'\n');walk(value,'',name);row['plist_valid']=True
            except Exception as e:errors.append({'name':name,'error':str(e)})
        entries.append(row)
    if pos!=len(b):raise ValueError(f'Not fully consumed: {pos}/{len(b)}')
    if sha(path.read_bytes())!=before:raise ValueError('ATX source copy changed')
    recent=extra/'files/HomeDomain/Library/SpringBoard/RecentAppLayouts.pb.lzfse';pb=lzfse.decompress(recent.read_bytes());fields=protobuf(pb);walk(fields,'','RecentAppLayouts_wire')
    (out/'RecentAppLayouts.pb').write_bytes(pb)
    for name,value in [('entries',entries),('date-candidates',dates),('schemas',schemas),('native',native),('errors',errors),('recent-protobuf',fields),('integrity',{'ATX_sha256':before,'ATX_after':sha(path.read_bytes()),'ATX_records':count,'ATX_consumed':pos,'RecentAppLayouts_sha256':sha(recent.read_bytes()),'RecentAppLayouts_pb_sha256':sha(pb)})]:
        (out/(name+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2,default=encode,allow_nan=False)+'\n')
    print(json.dumps({'records':count,'consumed':pos,'plist_records':sum(x.get('plist_valid',False) for x in entries),'errors':errors,'date_candidates':len(dates)}))


if __name__=='__main__':main()
