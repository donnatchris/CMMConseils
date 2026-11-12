#!/usr/bin/env python3
"""Read only selected image metadata; do not render images or export GPS/credentials."""
import argparse
import collections
import ctypes as C
import ctypes.util
import json
import os
from pathlib import Path
from PIL import Image
import tp02_forensic as common

class Error(C.Structure):
    _fields_=[('code',C.c_int),('subcode',C.c_int),('message',C.c_char_p)]


def heif_exif(path):
    lib=C.CDLL(ctypes.util.find_library('heif'))
    void=C.c_void_p;ids=C.c_uint32
    specs={
      'heif_context_alloc':([],void),
      'heif_context_free':([void],None),
      'heif_context_read_from_file':([void,C.c_char_p,void],Error),
      'heif_context_get_primary_image_handle':([void,C.POINTER(void)],Error),
      'heif_image_handle_release':([void],None),
      'heif_image_handle_get_number_of_metadata_blocks':([void,C.c_char_p],C.c_int),
      'heif_image_handle_get_list_of_metadata_block_IDs':([void,C.c_char_p,C.POINTER(ids),C.c_int],C.c_int),
      'heif_image_handle_get_metadata_size':([void,ids],C.c_size_t),
      'heif_image_handle_get_metadata':([void,ids,void],Error)}
    for name,(args,ret) in specs.items():f=getattr(lib,name);f.argtypes=args;f.restype=ret
    ctx=lib.heif_context_alloc();handle=void()
    try:
        if lib.heif_context_read_from_file(ctx,os.fsencode(path),None).code:raise ValueError('HEIF read failed')
        if lib.heif_context_get_primary_image_handle(ctx,C.byref(handle)).code:raise ValueError('HEIF primary handle failed')
        count=lib.heif_image_handle_get_number_of_metadata_blocks(handle,b'Exif')
        if not count:return Image.Exif()
        if count>16:raise ValueError('metadata block limit')
        blocks=(ids*count)();n=lib.heif_image_handle_get_list_of_metadata_block_IDs(handle,b'Exif',blocks,count)
        size=lib.heif_image_handle_get_metadata_size(handle,blocks[0])
        if size<8 or size>8*1024**2:raise ValueError('metadata size limit')
        data=C.create_string_buffer(size)
        if lib.heif_image_handle_get_metadata(handle,blocks[0],data).code:raise ValueError('metadata read failed')
        raw=data.raw;offset=int.from_bytes(raw[:4],'big')+4
        if offset>=len(raw):raise ValueError('invalid EXIF offset')
        ex=Image.Exif();ex.load(b'Exif\x00\x00'+raw[offset:]);return ex
    finally:
        if handle.value:lib.heif_image_handle_release(handle)
        lib.heif_context_free(ctx)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--extracted',required=True);p.add_argument('--out',required=True)
    a=p.parse_args();os.umask(0o077);root=Path(a.extracted);rows=[]
    for line in (root/'extraction.jsonl').read_text().splitlines():
        item=json.loads(line)
        if item.get('status')!='ok':continue
        path=Path(item['output']);r={'fileID':item['fileID'],'relativePath':item['relativePath'],'sha256':item['sha256']}
        try:
            if path.suffix.lower() in ('.heic','.heif'):
                ex=heif_exif(path);r['reader']='libheif metadata API + Pillow TIFF reader'
            else:
                with Image.open(path) as image:
                    ex=image.getexif();r.update(width=image.width,height=image.height,format=image.format)
                r['reader']='Pillow metadata'
            extra=ex.get_ifd(34665) if ex.get(34665) else {}
            r.update(make=ex.get(271),model=ex.get(272),datetime_raw=ex.get(306),datetime_original_raw=extra.get(36867),
                offset_time_original_raw=extra.get(36881),software=ex.get(305),status='ok')
        except Exception as error:r.update(status='error',error_class=type(error).__name__)
        rows.append(r)
    result={'files':len(rows),'status_counts':dict(collections.Counter(r['status'] for r in rows)),
        'model_counts':dict(collections.Counter(str(r.get('model')) for r in rows)), 'rows':rows,
        'limits':['EXIF model identifies a declared model, not a serial number or operator','EXIF can be edited','DateTimeOriginal without offset kept raw, not assigned a timezone','Only selected originals available in backup examined; no image content viewed']}
    with open(a.out,'x') as f:json.dump(result,f,ensure_ascii=False,indent=2,default=str);f.write('\n')
    print(json.dumps({k:result[k] for k in ('files','status_counts','model_counts')}))
if __name__=='__main__':main()
