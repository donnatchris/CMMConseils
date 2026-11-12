from pathlib import Path
import json,sys,subprocess,os,tempfile,zipfile,hashlib,concurrent.futures,collections,xml.etree.ElementTree as ET,re
from PIL import Image
O=Path(sys.argv[1]);done={x['sha256'] for x in map(json.loads,(O/'extraction-initiale.jsonl').open())};D={x['sha256']:x for x in json.loads((O/'blobs-expanded.json').read_text()) if x['sha256'] not in done}
ENV=dict(os.environ,OMP_THREAD_LIMIT='1')
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
with (O/'extraction-reprise.jsonl').open('x') as f,concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
 for i,future in enumerate(concurrent.futures.as_completed([pool.submit(extract,x) for x in D.values()]),1):
  r=future.result()
  f.write(json.dumps(r,ensure_ascii=False)+'\n');f.flush()
  if i%50==0:print('decoded',i,'/',len(D),flush=True)
print('done',len(D),flush=True)

with (O/'extraction.jsonl').open('x') as f:
 for name in ['extraction-initiale.jsonl','extraction-reprise.jsonl']:
  with (O/name).open() as g:
   for line in g:f.write(line)
subprocess.run([sys.executable,str(Path(__file__).resolve().with_name('rechercher.py')),str(O)],check=True)
