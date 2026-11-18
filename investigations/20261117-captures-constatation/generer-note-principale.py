from pathlib import Path
import hashlib
import sys
import xml.etree.ElementTree as ET
sys.path.insert(0, '/tmp/dmm-note-pdf-deps')
import markdown
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from pypdf import PdfReader

root = Path('/mnt/data/codeProjects/DMMConseils')
source = Path('/tmp/sadedine-captures-20261117/audit/note-sans-annexe.md')
output = Path('/tmp/sadedine-captures-20261117/audit/note-main.pdf')
for name, file in [('DejaVu','DejaVuSans.ttf'), ('DejaVu-Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/' + file))
pdfmetrics.registerFontFamily('DejaVu', normal='DejaVu', bold='DejaVu-Bold', italic='DejaVu', boldItalic='DejaVu-Bold')
navy = colors.HexColor('#183b56')
styles = {
 'body': ParagraphStyle('body', fontName='DejaVu', fontSize=8.8, leading=11.8, spaceAfter=6),
 'header': ParagraphStyle('header', fontName='DejaVu', fontSize=8.6, leading=11.3, spaceAfter=11),
 'title': ParagraphStyle('title', fontName='DejaVu-Bold', fontSize=17.5, leading=22, textColor=navy, spaceAfter=6),
 'subtitle': ParagraphStyle('subtitle', fontName='DejaVu', fontSize=9.6, leading=13, spaceAfter=8),
 'section': ParagraphStyle('section', fontName='DejaVu-Bold', fontSize=10.2, leading=14, textColor=navy, spaceBefore=4, spaceAfter=6),
 'cell': ParagraphStyle('cell', fontName='DejaVu', fontSize=8.15, leading=10.7),
 'th': ParagraphStyle('th', fontName='DejaVu-Bold', fontSize=8.3, leading=11, textColor=navy),
}

def inner(el):
    text = ET.tostring(el, encoding='unicode', method='html')
    text = text[text.index('>')+1:text.rfind('</')]
    return text.replace('<strong>','<b>').replace('</strong>','</b>').replace('<em>','<i>').replace('</em>','</i>').replace('<br>','<br/>')

text = source.read_text()
blocks = list(ET.fromstring('<div>' + markdown.markdown(text, extensions=['tables']) + '</div>'))
story = []
signing = []
for i, el in enumerate(blocks):
    value = inner(el)
    if el.tag == 'table':
        rows = []
        for tr in el.findall('.//tr'):
            rows.append([Paragraph(inner(cell), styles['th' if cell.tag == 'th' else 'cell']) for cell in tr])
        table = Table(rows, colWidths=[119, A4[0]-80-119], repeatRows=1, hAlign='LEFT')
        table.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e9eff3')),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f7f9fb')]),
            ('GRID',(0,0),(-1,-1),.4,colors.HexColor('#cbd5df')),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
            ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
        ]))
        story.extend([Spacer(1,2), table, Spacer(1,8)])
    elif el.tag == 'h1':
        story.append(Paragraph(value,styles['title']))
    elif el.tag == 'h3':
        story.append(Paragraph(value,styles['section']))
    elif el.tag == 'p':
        if value.startswith('Fait à '):
            signing.append(Paragraph(value,styles['body']))
        elif signing:
            signing.append(Paragraph(value,styles['body']))
        else:
            style = 'header' if i == 0 else 'subtitle' if i == 2 else 'body'
            story.append(Paragraph(value,styles[style]))
assert signing and 'Christophe DONNAT' in text and '16 novembre 2026' in text
signing.append(Spacer(1,55))
story.append(KeepTogether(signing))

def footer(canvas, doc):
    canvas.setFont('DejaVu',7)
    canvas.setFillColor(colors.HexColor('#64748b'))
    canvas.drawString(40,23,'SADEDINE-2026 | Note de constatation')
    canvas.drawRightString(A4[0]-40,23,str(doc.page))

doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=40,leftMargin=40, topMargin=33,bottomMargin=37,
 title='NOTE DE CONSTATATION - SADEDINE-2026',author='Christophe DONNAT - DONNAT DEV')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
pdf = PdfReader(output)
extracted = '\n'.join(p.extract_text() for p in pdf.pages)
assert len(pdf.pages) == 1, f'Unexpected page count: {len(pdf.pages)}'
for expected in ['Christophe DONNAT','16 novembre 2026','Signature :','Arrivée supposée des enquêteurs','sur les enregistrements et']:
    assert expected in extracted, expected
print(f'{output}: {len(pdf.pages)} page, {output.stat().st_size} bytes')
print('SHA-256 source:',hashlib.sha256(source.read_bytes()).hexdigest())
print('SHA-256 PDF:',hashlib.sha256(output.read_bytes()).hexdigest())
