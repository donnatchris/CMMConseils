"""Rendre les pages de contrôle de chaque PDF principal, sans modifier les PDF."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'rendu'
QA = Path('/tmp/dmm-rendu-visuel')


def render(task):
    name, page, prefix = task
    subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile',
                    '-scale-to', '1200', '-png', str(OUT / name), str(prefix)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    return str(prefix.with_suffix('.png'))


def main():
    manifest_path = OUT / 'manifest-rendu.json'
    if not manifest_path.exists():
        manifest_path = OUT / 'rapports-subsidiaires/manifest-rendu.json'
    manifest = json.loads(manifest_path.read_text())
    QA.mkdir(exist_ok=True)
    tasks, index = [], []
    for number, item in enumerate(manifest['documents'], 1):
        reader = PdfReader(OUT / item['pdf'])
        pages = {1, len(reader.pages)}
        if len(reader.pages) > 8:
            pages.add(len(reader.pages) // 2)
        if len(reader.pages) > 40:
            pages.update({len(reader.pages) // 4, len(reader.pages) * 3 // 4})
        if item['pdf'] == 'RAPPORT-FINAL-SADEDINE-2026.pdf':
            pages.update({2, 3, 4})
        if item.get('images_in_source', 0) or item['pdf'] == 'note-de-constat-technique.pdf':
            for i, page in enumerate(reader.pages, 1):
                if '/XObject' in page.get('/Resources', {}):
                    pages.add(i)
        for page in sorted(pages):
            prefix = QA / f'doc-{number:02d}-page-{page:04d}'
            tasks.append((item['pdf'], page, prefix))
            index.append({'pdf': item['pdf'], 'page': page, 'image': str(prefix.with_suffix('.png'))})
    with ThreadPoolExecutor(max_workers=3) as pool:
        for i, result in enumerate(pool.map(render, tasks), 1):
            if i % 25 == 0:
                print(f'Pages rendues : {i}/{len(tasks)}', flush=True)
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    for offset in range(0, len(index), 16):
        entries = index[offset:offset + 16]
        sheet = Image.new('RGB', (1504, 2280), '#dce2e7')
        draw = ImageDraw.Draw(sheet)
        for position, row in enumerate(entries):
            x, y = (position % 4) * 376, (position // 4) * 570
            with Image.open(row['image']) as im:
                im.thumbnail((360, 518))
                sheet.paste(im, (x + 8, y + 42))
            title = row['pdf']
            draw.text((x + 8, y + 5), title[:48], font=font, fill='black')
            draw.text((x + 8, y + 21), f"page {row['page']} — contrôle {offset + position + 1}", font=font, fill='black')
        sheet.save(QA / f'planche-{offset // 16 + 1:02d}.jpg', quality=90)
    (QA / 'pages.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n')
    print(f'{len(tasks)} pages rendues, {(len(tasks)+15)//16} planches : {QA}', flush=True)


if __name__ == '__main__':
    main()
