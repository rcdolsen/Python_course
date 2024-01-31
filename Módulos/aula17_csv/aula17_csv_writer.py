# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula17.csv'

lista_clientes = [
    {'Nome': 'Marrom Siqueira', 'Endereço': 'Av 1, 22'},
    {'Nome': 'Theo Siqueira', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Isabela Muzuda', 'Endereço': 'Av B, 3A'},
]


# print(lista_clientes[0])
# print(lista_clientes[0]['Nome'])
# print('-' * 40)

# for dict in (lista_clientes):
#     cliente = dict['Nome']
#     key = list(dict.keys())[0]
#     print(f'{key}: {cliente}')
# print('-' * 40)


with open(CAMINHO_CSV, 'w', encoding='utf8', newline='') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)

#  Usando lista no lugar de dict

# lista_clientes = [
#     ['Marrom Siqueira', 'Av 1, 22'],
#     ['Theo Siqueira', 'R. 2, "1"'],
#     ['Isabela Muzuda', 'Av B, 3A'],
# ]


# with open(CAMINHO_CSV, 'w', encoding='utf8', newline='') as arquivo:
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)
