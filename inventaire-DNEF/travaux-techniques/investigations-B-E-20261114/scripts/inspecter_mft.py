#!/usr/bin/env python3
"""Parcours MFT complet ciblé B/E, sans écrire dans l'image OP-01."""
import collections
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import sys
import unicodedata

P=Path('/media/shared/codeProjects/DMMConseils')
O=P/'inventaire-DNEF/travaux-techniques/investigations-B-E-20261114/prive'/(sys.argv[1] if len(sys.argv)>1 else 'op01-mft');os.umask(0o077);O.mkdir(exist_ok=False)
src=Path('/mnt/windows/$MFT')
q1=json.loads((P/'inventaire-DNEF/travaux-techniques/recherche-Q1-20261114/prive/resultats.json').read_text())
def norm(v):return unicodedata.normalize('NFKD',v).casefold()
names={norm(x['path'].rsplit('\\',1)[-1]) for x in q1['inventory']}
candidate_sizes={x['bytes'] for rows in q1['phones'].values() for x in rows}
rx=re.compile(r'ldsd|itunes|appledevices|applemobile|usbmux|imazing|3utools|ifunbox|iexplorer|cellebrite|ufed|oxygen|elcomsoft|xry|iphone13|archive_saddedine|inventaire_saddedine|rejets_saddedine',re.I)
U16=lambda b,o:struct.unpack_from('<H',b,o)[0]
U32=lambda b,o:struct.unpack_from('<I',b,o)[0]
U64=lambda b,o:struct.unpack_from('<Q',b,o)[0]
def filetime(n):
    if not n:return None
    seconds,frac=divmod(n,10000000)
    return (dt.datetime(1601,1,1,tzinfo=dt.timezone.utc)+dt.timedelta(seconds=seconds)).strftime('%Y-%m-%dT%H:%M:%S')+f'.{frac:07d}+00:00'
def times(b,o):return {k:{'filetime':U64(b,o+i*8),'utc':filetime(U64(b,o+i*8))} for i,k in enumerate(['creation','modification','mft_change','access'])}
dirs={};rows=[];counts=collections.Counter();digest=hashlib.sha256();index=0
with src.open('rb') as f:
    while block:=f.read(16*1024*1024):
        digest.update(block)
        for pos in range(0,len(block),1024):
            raw=block[pos:pos+1024];idx=index;index+=1;counts['slots']+=1
            if raw[:4]!=b'FILE':continue
            counts['FILE']+=1;b=bytearray(raw)
            try:
                usa,num=U16(b,4),U16(b,6)
                if num!=3 or usa+num*2>1024:raise ValueError('fixup bounds')
                for i in range(1,num):
                    if b[i*512-2:i*512]!=b[usa:usa+2]:raise ValueError('fixup')
                    b[i*512-2:i*512]=b[usa+i*2:usa+i*2+2]
                flags,seq=U16(b,22),U16(b,16);a=U16(b,20);si=None;fn=[];streams=[]
                while a+24<=min(U32(b,24),1024):
                    typ=U32(b,a)
                    if typ==0xffffffff:break
                    length=U32(b,a+4)
                    if length<24 or a+length>1024:raise ValueError('attribute bounds')
                    nonresident=b[a+8];nl=b[a+9];no=U16(b,a+10)
                    aname=bytes(b[a+no:a+no+nl*2]).decode('utf-16le','replace') if nl else ''
                    if not nonresident:
                        size=U32(b,a+16);v=a+U16(b,a+20)
                        if v+size>a+length:raise ValueError('value bounds')
                        if typ==0x10 and size>=32:si=times(b,v)
                        if typ==0x30 and size>=66:
                            n=b[v+64]
                            if v+66+n*2>v+size:raise ValueError('filename bounds')
                            fn.append({'name':bytes(b[v+66:v+66+n*2]).decode('utf-16le','replace'),'namespace':b[v+65],'parent_ref':U64(b,v),'times':times(b,v+8)})
                        if typ==0x80:streams.append({'name':aname,'resident':True,'size':size,'value_hex':bytes(b[v:v+size]).hex() if aname else None})
                    elif typ==0x80:streams.append({'name':aname,'resident':False,'size':U64(b,a+48)})
                    a+=length
                counts['allocated' if flags&1 else 'unallocated']+=1
                if flags&2 and fn:
                    main=next((n for n in fn if n['namespace']!=2),fn[0]);dirs[idx]={'name':main['name'],'parent_ref':main['parent_ref'],'sequence':seq,'allocated':bool(flags&1)}
                wanted=any(norm(n['name']) in names or rx.search(n['name']) or n['name'] in ['L16B','TELEPHONES'] for n in fn)
                zipday=any(n['name'].lower().endswith(('.zip','.7z','.rar','.tar')) for n in fn) and any(t['utc'] and t['utc'].startswith(('2024-10-15','2024-10-28')) for ts in [si or {}]+[x['times'] for x in fn] for t in ts.values())
                sized=bool(flags&1) and not flags&2 and any(s['name']=='' and s['size'] in candidate_sizes for s in streams)
                if wanted or zipday or sized:rows.append({'index':idx,'sequence':seq,'allocated':bool(flags&1),'directory':bool(flags&2),'SI':si,'FN':fn,'streams':streams,'raw_hex':raw.hex(),'zip_day_candidate':zipday,'pdf_size_candidate':sized})
            except Exception as e:counts['error_'+str(e)]+=1
        if index%131072==0:print('scanned',index,flush=True)
for r in rows:
    for fn in r['FN']:
        parts=[fn['name']];ref=fn['parent_ref'];seen=set();uncertain=False
        while ref&0xffffffffffff not in [0,5] and ref&0xffffffffffff not in seen:
            idx=ref&0xffffffffffff;seen.add(idx);d=dirs.get(idx)
            if not d:parts.append('[parent inconnu '+str(idx)+']');uncertain=True;break
            if ref>>48!=d['sequence'] or not d['allocated']:uncertain=True
            parts.append(d['name']);ref=d['parent_ref']
        fn['path']='\\'.join(reversed(parts));fn['parent_uncertain']=uncertain
with (O/'records.jsonl').open('x') as f:
    for x in rows:f.write(json.dumps(x,ensure_ascii=False)+'\n')
summary={'source':str(src),'sha256':digest.hexdigest(),'expected_previous_sha256':'4b56e70ac59c0b8cdbf25a429e633991960862f4fa827368d83ef824c18f673b','counts':dict(counts),'selected':len(rows)}
summary['same_as_previous']=summary['sha256']==summary['expected_previous_sha256']
with (O/'summary.json').open('x') as f:json.dump(summary,f,indent=2)
print(json.dumps(summary))
