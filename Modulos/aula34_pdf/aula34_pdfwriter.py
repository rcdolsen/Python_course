# PyPDF2 para manipular arquivos PDF (PdfReader)
# PyPDF2 para manipular arquivos PDF (PdfWriter)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

ROOT = Path(__file__).parent
ORIGINALS_FILE = ROOT / 'pdf_original'
NEW_FILE = ROOT / 'pdf_novo'

RELATORIO = ORIGINALS_FILE / 'R20230908.pdf'

NEW_FILE.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO)

# Criar um novo pdf com as mesmas paginas
writer = PdfWriter()

with open(NEW_FILE / 'PDF_novo.pdf', 'wb') as fp:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(fp)

# Criar um novo PDF com cada pagina
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()

        with open(NEW_FILE / f'pagina{i}.pdf', 'wb') as fp:
            writer.add_page(page)
            writer.write(fp)
