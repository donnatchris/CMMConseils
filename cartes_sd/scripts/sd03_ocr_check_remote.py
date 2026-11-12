import shutil,subprocess,json
p=subprocess.run(['ffmpeg','-hide_banner','-filters'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
print(json.dumps(dict(tesseract=shutil.which('tesseract'),ffmpeg_ocr_lines=[line for line in p.stdout.splitlines() if 'ocr' in line.lower()],stderr=p.stderr),indent=2))
if shutil.which('tesseract'):subprocess.run(['tesseract','--version'])
