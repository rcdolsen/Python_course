import json

pessoa = {
    'nome': 'Téo',
    'sobrenome': 'Siqueira',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 0.5,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula55.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2) # Sem o ensure_ascii téo fica T\u00e9o, o indent serve para formatar e não ficar em uma única linha
print(pessoa)

with open('aula55.json', 'r', encoding='UTF8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))
    print(pessoa['nome'])