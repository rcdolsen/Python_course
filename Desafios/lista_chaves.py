#Escreva uma função que retorne uma lista com todas as chaves de um dicionário que contém um certo valor.

#Por exemplo, se o dicionário for {'a': 1, 'b': 2, 'c': 1, 'd': 4}, a função deve retornar ['a', 'c'] caso procure pelo valor 1; [] caso procure pelo valor 666.

dickt = {'a': 1, 'b': 2, 'c': 1, 'd': 4}

def finder(dict, to_find):
    list_key = []
    for key, value in dict.items():
        if value == to_find:
            list_key.append(key)
    return list_key

print(finder(dickt, 1))
print(finder(dickt, 666))