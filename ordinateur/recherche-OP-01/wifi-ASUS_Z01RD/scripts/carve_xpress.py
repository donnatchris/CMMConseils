"""Exploratory bounded Plain XPRESS carving; candidates require later validation.
Decoder follows MS-XCA Plain LZ77; output is capped at a 4096-byte page.
"""
import pathlib,json,struct,re,hashlib
O=pathlib.Path(__file__).resolve().parents[1]/'origine'
def decode(b,start):
 p=start;out=bytearray();flags=0;bits=0;nibble=None
 while len(out)<4096:
  if bits==0:flags=struct.unpack_from('<I',b,p)[0];p+=4;bits=32
  bits-=1
  if not flags&(1<<bits):out.append(b[p]);p+=1;continue
  token=struct.unpack_from('<H',b,p)[0];p+=2;distance=(token>>3)+1;length=token&7
  if distance>len(out):raise ValueError('distance')
  if length==7:
   if nibble is None:nibble=b[p]>>4;length=b[p]&15;p+=1
   else:length=nibble;nibble=None
   if length==15:
    length=b[p];p+=1
    if length==255:
     length=struct.unpack_from('<H',b,p)[0];p+=2
     if length==0:length=struct.unpack_from('<I',b,p)[0];p+=4
     if length<22:raise ValueError('length')
     length-=22
    length+=15
   length+=7
  length+=3
  if len(out)+length>4096:raise ValueError('page overflow')
  for _ in range(length):out.append(out[-distance])
 return bytes(out),p
results=[]
for row in json.loads((O/'wide-contexts.json').read_text()):
 b=(O/('pagefile-%s-64k.bin'%row['offset'])).read_bytes();target=row['offset']-row['start'];found=[]
 for start in range(max(0,target-16384),target):
  try:out,end=decode(b,start)
  except (ValueError,IndexError,struct.error):continue
  if not start<=target<end or b'ASUS_Z01RD' not in out:continue
  strings=[{'offset':m.start(),'text':m.group().decode('ascii')} for m in re.finditer(rb'[\x20-\x7e]{6,}',out)]
  fn='decoded-%s-%s.bin'%(row['offset'],row['start']+start);(O/fn).write_bytes(out)
  found.append({'input_start':row['start']+start,'input_end':row['start']+end,'file':fn,'sha256':hashlib.sha256(out).hexdigest(),'strings':strings})
 results.append({'match_offset':row['offset'],'candidates':found});print(row['offset'],'candidates',len(found),flush=True)
 for x in found:
  print(x['input_start'],[(s['offset'],s['text']) for s in x['strings'] if re.search('asus|realme|xcover|wlan|wifi|ssid|network',s['text'],re.I)],flush=True)
(O/'xpress-candidates.json').write_text(json.dumps(results,indent=2))
