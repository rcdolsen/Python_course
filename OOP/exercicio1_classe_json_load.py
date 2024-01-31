# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

from exercicio1_classe_json_save import FILE_PATH, People

with open(FILE_PATH, 'r') as file:
    data = json.load(file)

    for p in range(len(data)):
        print(People(**data[p]).name)
        print(People(**data[p]).age)

    #p1 = People(**data[0])
    #print(p1.name, p1.age)

    #p2 = People(**data[1])
    #print(p2.name, p2.age)