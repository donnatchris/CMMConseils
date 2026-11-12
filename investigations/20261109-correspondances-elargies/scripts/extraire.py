from pathlib import Path
import json,sys,subprocess,os,tempfile,zipfile,hashlib,concurrent.futures,collections,xml.etree.ElementTree as ET,re
from PIL import Image
O=Path(sys.argv[1]);items=json.loads((O/'blobs.json').read_text());D={x['sha256']:x for x in items};edges=[];limits=[]
def add(d,name,parent):
 h=hashlib.sha256(d).hexdigest()
 if h not in D:(O/'blobs'/h).write_bytes(d);D[h]={'sha256':h,'size':len(d),'names':[name]}
 edges.append({'parent':parent,'child':h,'name':name})
for depth in range(2):
 batch=list(D.values())
 for x in batch:
  if x.get('archive_examined'):continue
  if not any(Path(n).suffix.lower() in ('.zip','.gz') for n in x['names']):continue
  x['archive_examined']=True
  try:
   with zipfile.ZipFile(O/'blobs'/x['sha256']) as z:
    if sum(v.file_size for v in z.infolist())>200*1024**2 or len(z.infolist())>5000:raise ValueError('archive_expansion_limit')
    for v in z.infolist():
     if not v.is_dir():add(z.read(v),v.filename,x['sha256'])
  except Exception as e:limits.append({'sha256':x['sha256'],'error':type(e).__name__})
(O/'archive-edges.json').write_text(json.dumps(edges,ensure_ascii=False));(O/'archive-limits.json').write_text(json.dumps(limits));(O/'blobs-expanded.json').write_text(json.dumps(list(D.values()),ensure_ascii=False))
ENV=dict(os.environ,OMP_THREAD_LIMIT='1');(O/'extracted').mkdir(exist_ok=False)
def run(args,timeout=60):
 r=subprocess.run(args,capture_output=True,timeout=timeout,env=ENV)
 if r.returncode:raise RuntimeError('tool_exit_'+str(r.returncode))
 return r.stdout.decode('utf8',errors='replace')
def xml(data):
 root=ET.fromstring(data);return ' '.join(root.itertext())
def extract(x):
 h=x['sha256'];p=O/'blobs'/h;data=p.read_bytes();ext={Path(n).suffix.lower() for n in x['names']};r={'sha256':h,'names':x['names'],'size':len(data),'method':[],'limitations':[]};text=''
 try:
  if data.startswith(b'%PDF-'):
   try:text=run(['pdftotext','-layout',str(p),'-']);r['method'].append('pdftotext')
   except Exception as e:r['limitations'].append('pdf_text_'+type(e).__name__)
   pages=text.split('\f');pages=pages[:-1] if pages and not pages[-1].strip() else pages
   try:info=run(['pdfinfo',str(p)]);count=int(re.search(r'Pages:\s+(\d+)',info).group(1))
   except Exception:count=len(pages);r['limitations'].append('pdf_page_count_unverified')
   r['pages']=count;ocr=[]
   for i in range(count):
    if i<len(pages) and len(re.sub(r'\s','',pages[i]))>=60:continue
    try:
     with tempfile.TemporaryDirectory() as td:
      q=Path(td)/'page';run(['pdftoppm','-f',str(i+1),'-l',str(i+1),'-singlefile','-scale-to','1800','-png',str(p),str(q)],45)
      t=run(['tesseract',str(q)+'.png','stdout','-l','fra+eng','--psm','3'],45);ocr.append(f'\n[OCR PAGE {i+1}]\n'+t)
    except Exception as e:r['limitations'].append(f'ocr_page_{i+1}_{type(e).__name__}')
   if ocr:text+='\n'.join(ocr);r['method'].append('tesseract_sparse_pages');r['ocr_pages']=len(ocr)
  elif data.startswith(b'PK') and ext & {'.docx','.xlsx','.odt','.ods','.pptx'}:
   with zipfile.ZipFile(p) as z:
    ns=[v for v in z.infolist() if v.filename.endswith('.xml')]
    if sum(v.file_size for v in ns)>100*1024**2:raise ValueError('xml_limit')
    text='\n'.join(xml(z.read(v)) for v in ns)
   r['method'].append('office_xml_all_parts')
  elif data.startswith(bytes.fromhex('d0cf11e0a1b11ae1')):
   if '.xls' in ext:
    import xlrd
    w=xlrd.open_workbook(file_contents=data);text='\n'.join(str(c.value) for sh in w.sheets() for row in sh for c in row);r['method'].append('xlrd_all_sheets')
   else:text=run(['antiword',str(p)]);r['method'].append('antiword')
  elif data.startswith(b'{\\rtf'):
   text=data.decode('cp1252',errors='replace');text=re.sub(r"\\'([0-9a-fA-F]{2})",lambda m:bytes.fromhex(m[1]).decode('cp1252'),text);text=re.sub(r'\\[a-z]+-?\d* ?',' ',text);r['method'].append('rtf_approximate');r['limitations'].append('rtf_not_full_parser')
  elif ext & {'.txt','.csv','.html','.htm','.xml','.eml','.ics'}:
   text=data.decode('utf8',errors='replace');r['method'].append('utf8_replacement')
  else:
   try:
    with Image.open(p) as im:w,hh=im.size
   except Exception:r['limitations'].append('unsupported_format');w=hh=0
   if w and (w<200 or hh<80):r['limitations'].append('small_image_not_ocred')
   elif w:
    text=run(['tesseract',str(p),'stdout','-l','fra+eng','--psm','3'],60);r['method'].append('tesseract_image');r['image_dimensions']=[w,hh]
  r['status']='decoded' if r['method'] else 'not_decoded';r['text_chars']=len(text)
 except Exception as e:r['status']='error';r['limitations'].append(type(e).__name__)
 (O/'extracted'/(h+'.txt')).write_text(text);return r
with (O/'extraction.jsonl').open('x') as f,concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for i,future in enumerate(concurrent.futures.as_completed([pool.submit(extract,x) for x in D.values()]),1):
  r=future.result()
  f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
  if i%50==0:print('decoded',i,'/',len(D),flush=True)
print('done',len(D),flush=True)
