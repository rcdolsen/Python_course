# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path

FILE_PATH = Path(__file__).parent / "aula20.txt"

locale.setlocale(locale.LC_ALL, '')


def converte_brl(numero: float) -> str:
    brl = 'R$' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='Theo',
    valor=converte_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='T. S.',
    telefone='+351 666666666'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))

texto = '''
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data.
Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone
$telefone.

Atenciosamente,

${empresa},
'''

# para mudar o delimitador


class MyTemplate(string.Template):
    delimiter = '%'


# Opens the text file specified by FILE_PATH in read mode ('r'), reads its
# content, and stores it in the texto variable.
# Creates a string.Template object called template using the contents of the
# text file.
# Uses the template.substitute(dados) method to replace the placeholders in the
# template with the values from the dados dictionary.
# Finally, it prints the modified text with the placeholders replaced by their
# respective values
with open(FILE_PATH, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    # template = MyTemplate(texto)
    template = string.Template(texto)
    print(template.substitute(dados))
