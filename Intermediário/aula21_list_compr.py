# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

print(list(range(10)))
print('----------1')
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)
print('----------2')

lista = [numero for numero in range(10)]
print(lista)
print('----------3')

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)
print('----------4')