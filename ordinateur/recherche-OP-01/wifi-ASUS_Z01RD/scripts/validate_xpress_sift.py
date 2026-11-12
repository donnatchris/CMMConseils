"""Independent validation against original pagefile bytes; run in SIFT with sudo."""
import ctypes,pathlib,hashlib,json
libpath='/opt/volatility3/lib/python3.12/site-packages/leechcorepyc/libMSCompression.so'
lib=ctypes.CDLL(libpath)
lib.ms_decompress.argtypes=[ctypes.c_int,ctypes.c_void_p,ctypes.c_size_t,ctypes.c_void_p,ctypes.POINTER(ctypes.c_size_t)]
lib.ms_decompress.restype=ctypes.c_int
items=[(147842848,187),(331614992,284),(459192208,161),(549269216,161),(2752380080,265)];results=[]
with open('/mnt/windows/pagefile.sys','rb') as f:
 for off,n in items:
  f.seek(off);b=f.read(n);buf=ctypes.create_string_buffer(4096);size=ctypes.c_size_t(4096)
  rc=lib.ms_decompress(3,b,len(b),buf,ctypes.byref(size));out=buf.raw[:size.value]
  results.append({'start':off,'input_size':n,'returncode':rc,'output_size':size.value,'sha256':hashlib.sha256(out).hexdigest()})
O=pathlib.Path('/home/sansforensics/analysis/OP-01/wifi-ASUS_Z01RD-20261014/origine')
(O/'independent-decompression.json').write_text(json.dumps({'library':libpath,'library_sha256':hashlib.sha256(pathlib.Path(libpath).read_bytes()).hexdigest(),'results':results},indent=2))
