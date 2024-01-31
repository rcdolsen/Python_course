"""
enumerate - enumera iteráveis (índices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

# lista_enumerada = enumerate(lista)
# # print(lista_enumerada)
# # print(next(lista_enumerada))

# for item  in lista_enumerada:
#     print(item)

# print('O que tem na lista enumerada: ', lista_enumerada)

# for item in lista_enumerada:
#     print(lista_enumerada)

lista_enumerada = list(enumerate(lista))
print(lista_enumerada)

lista_enumerada = list(enumerate(lista, start=10))
print(lista_enumerada)

for indice, nome in enumerate(lista):
    print(indice, nome)
    print(lista[indice])

for tupla_enumerada in enumerate(lista):
    print('For da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')