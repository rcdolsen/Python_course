"""
Exercício
Exiba os índices DINAMICOS da lista
0 Maria
1 Alfredo
2 Marrom
"""

lista = ['Maria', 'Alfredo', 'Marrom']
lista.append('Mozuda')
lista.append('Julia')

index = 0
nome = ''

indice = range(len(lista))


for nome in lista:
    print(index, nome)
    index += 1

# ou

for i in indice:
    print(i, lista[i])
