# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''
list_long = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_short = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    size = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(size)]


print(zipper(list_long, list_short))
'''

# OU

list_long = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_short = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(list_short, list_long)))

# para a lista maior

from itertools import zip_longest

print(list(zip_longest(list_short, list_long)))
print(list(zip_longest(list_short, list_long, fillvalue='sem dados')))
