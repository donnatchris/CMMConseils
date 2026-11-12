import sys,json,hashlib
f=open(sys.argv[1],'rb');offset=16587108352;f.seek(offset);b=f.read(16384)
print(json.dumps(dict(absolute_offset=offset,size=len(b),sha256=hashlib.sha256(b).hexdigest(),hex=b.hex())))
