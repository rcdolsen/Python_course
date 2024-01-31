"""
Retorno de valores das funções (return)
encerra a funcao, so e executado 1 por funcao
"""

variavel = print('marrom')
print(variavel)

def soma(x, y):
    ...

#retorna erro

#soma1 = soma(2, 2)
#soma2 = soma(3, 3)
#print(soma1 + soma2)

def soma(x, y):
    if x > 10:
        return [10, 20] # ou esse
    return x + y # ou esse

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))