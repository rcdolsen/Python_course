"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#       +01234
#       -54321
string = 'abcde' # r caracteres (len)
lista = list()
# ou
lista = []
print(lista, type(lista))
print('')
print(bool([])) #  falsy
print('')

#         0     1           2           3   4
#        -5    -4          -2          -3 -4
lista = [123, True, 'Marrom Siqueira', 1.2, []]
print(lista)
print('')
print(lista[2].upper(), type(lista[2]))
print('')
lista[2] = 'Maria'
print(lista[2].upper())
