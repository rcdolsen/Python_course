"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
print(nome2)

# ou

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

# erro
# nome1, nome2 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

# # erro
# nome1, nome2, nome3, nome4 = ['Maria', 'Helena', 'Luiz']
# print(nome2)

nome1, *resto = ['Maria', 'Helena', 'Luiz']
print(nome1)
print(resto)

# ou

nome1, *_ = ['Maria', 'Helena', 'Luiz']
print(nome1)
# _ e usado por convencao para designar variaveis que nao serao usadas

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
print(resto)