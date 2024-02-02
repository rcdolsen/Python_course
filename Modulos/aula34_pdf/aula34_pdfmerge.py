# PyPDF2 para manipular arquivos PDF (PdfWriter)
# PyPDF2 para manipular arquivos PDF (PdfMerger)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

ROOT = Path(__file__).parent
ORIGINALS_FILE = ROOT / 'pdf_original'
NEW_FILE = ROOT / 'pdf_novo'

RELATORIO = ORIGINALS_FILE / 'R20230908.pdf'

NEW_FILE.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO)

files = [
    NEW_FILE / 'pagina0.pdf',
    NEW_FILE / 'pagina1.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)

# e o mesmo que usando with open
merger.write(NEW_FILE / 'merged.pdf')
merger.close()

files_inverted = [
    NEW_FILE / 'pagina1.pdf',
    NEW_FILE / 'pagina0.pdf',
]

merger = PdfMerger()
for file in files_inverted:
    merger.append(file)

# e o mesmo que usando with open
with open(NEW_FILE / 'merged_inverted.pdf', 'wb') as fp:
    merger.write(fp)
