# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# for nome in lista:
#     print(nome, end='\n', sep='\n')

# print(lista)
# print(*lista)
# print(*string)
# print(*tupla)

print(salas)
print(*salas)
print(*salas, sep='\n')