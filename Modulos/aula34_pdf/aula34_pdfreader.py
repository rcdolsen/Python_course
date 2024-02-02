# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path

from PyPDF2 import PdfReader

ROOT = Path(__file__).parent
ORIGINALS_FILE = ROOT / 'pdf_original'
NEW_FILE = ROOT / 'pdf_novo'

RELATORIO = ORIGINALS_FILE / 'R20230908.pdf'

NEW_FILE.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
image3 = page0.images[3]

# print(page0.extract_text())
# print(len(page0.images))
# print(page0.images[3])
with open(NEW_FILE / image3.name, 'wb')as fp:
    fp.write(image3.data)
