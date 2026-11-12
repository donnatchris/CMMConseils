#!/usr/bin/env python3
"""Inspection bornée des boîtes MP4 et des tables ; ne reconstruit aucun fichier."""
import collections
import json
import struct
from sd01_collect import OUT

CONTAINERS={b'moov',b'trak',b'mdia',b'minf',b'stbl',b'edts',b'dinf',b'udta'}
def inspect(data):
    boxes=[]; errors=[]; tracks=[]
    def walk(start,end,path='',track=None):
        pos=start
        while pos+8<=end:
            size=int.from_bytes(data[pos:pos+4],'big'); typ=data[pos+4:pos+8]; head=8
            if size==1:
                if pos+16>end:errors.append(dict(offset=pos,error='header64 incomplete'));break
                size=int.from_bytes(data[pos+8:pos+16],'big');head=16
            if size==0:size=end-pos
            if size<head or pos+size>end:
                errors.append(dict(offset=pos,type=typ.decode(errors='replace'),claimed_size=size,available=end-pos));break
            name=path+'/'+typ.decode(errors='replace')
            b=dict(path=name,offset=pos,size=size)
            payload=data[pos+head:pos+size]
            if typ in (b'mvhd',b'mdhd',b'tkhd') and len(payload)>=12:
                version=payload[0]; width=8 if version==1 else 4
                b.update(creation_raw=int.from_bytes(payload[4:4+width],'big'),modification_raw=int.from_bytes(payload[4+width:4+width*2],'big'))
            if typ==b'trak':
                track={};tracks.append(track)
            if typ in (b'stco',b'co64') and len(payload)>=8:
                width=8 if typ==b'co64' else 4; count=int.from_bytes(payload[4:8],'big')
                vals=[int.from_bytes(payload[8+i*width:8+(i+1)*width],'big') for i in range(min(count,(len(payload)-8)//width))]
                b.update(entry_count=count,min_offset=min(vals,default=None),max_offset=max(vals,default=None),offsets_outside_file=sum(v>=len(data) for v in vals))
                if track is not None:track['chunk_offsets']=vals
            if typ==b'stsz' and len(payload)>=12:
                size0=int.from_bytes(payload[4:8],'big');count=int.from_bytes(payload[8:12],'big')
                vals=[size0]*count if size0 else [int.from_bytes(payload[12+4*i:16+4*i],'big') for i in range(min(count,(len(payload)-12)//4))]
                b.update(sample_count=count,uniform_size=size0,sum_sample_bytes=sum(vals))
                if track is not None:track['sample_sizes']=vals;track['sample_count']=count
            if typ==b'stts' and len(payload)>=8:
                count=int.from_bytes(payload[4:8],'big')
                vals=[struct.unpack_from('>II',payload,8+i*8) for i in range(min(count,(len(payload)-8)//8))]
                b.update(entry_count=count,total_samples=sum(v[0] for v in vals),sum_ticks=sum(c*d for c,d in vals))
                if track is not None:track['stts_total_samples']=b['total_samples']
            if typ==b'stsc' and len(payload)>=8:
                count=int.from_bytes(payload[4:8],'big')
                vals=[struct.unpack_from('>III',payload,8+i*12) for i in range(min(count,(len(payload)-8)//12))]
                if track is not None:track['stsc']=vals
            boxes.append(b)
            if typ in CONTAINERS:walk(pos+head,pos+size,name,track)
            pos+=size
        if pos!=end:errors.append(dict(offset=pos,error='trailing bytes',count=end-pos))
    walk(0,len(data))
    tables=[]
    for t in tracks:
        stsc=t.get('stsc',[]);sizes=t.get('sample_sizes',[]);sample=0;over=[];maxend=0
        for index,off in enumerate(t.get('chunk_offsets',[]),1):
            matches=[entry for entry in stsc if entry[0]<=index]
            n=matches[-1][1] if matches else 0
            end=off+sum(sizes[sample:sample+n]);sample+=n;maxend=max(maxend,end)
            if end>len(data):over.append(dict(chunk_index=index,start=off,end=end,beyond_eof=end-len(data)))
        tables.append(dict(stsz_sample_count=t.get('sample_count'),stts_sample_count=t.get('stts_total_samples'),chunk_sample_count=sample,max_chunk_end=maxend,chunks_beyond_eof=over))
    return dict(size=len(data),boxes=boxes,errors=errors,tracks=tables)

def main():
    export=json.loads((OUT/'inventaires/export.json').read_text())
    results=[]
    for e in export['entries']:
        if not e.get('artifact','').endswith('.mp4'):continue
        r=inspect((OUT/e['artifact']).read_bytes());r.update(inode=e['inode'],path=e['path'],deleted=e['deleted']);results.append(r)
    with (OUT/'inventaires/mp4-structures.json').open('x') as f:json.dump(results,f,ensure_ascii=False,indent=2)
    anomalies=[dict(inode=r['inode'],path=r['path'],errors=r['errors'],tracks=r['tracks']) for r in results if r['errors'] or any(t['chunks_beyond_eof'] or t['stsz_sample_count']!=t['stts_sample_count'] or t['stsz_sample_count']!=t['chunk_sample_count'] for t in r['tracks'])]
    with (OUT/'inventaires/mp4-anomalies.json').open('x') as f:json.dump(anomalies,f,ensure_ascii=False,indent=2)
    print('MP4',len(results),'anomalies',len(anomalies))
    print(json.dumps(anomalies,ensure_ascii=False,indent=2)[:8000])

if __name__=='__main__':main()
