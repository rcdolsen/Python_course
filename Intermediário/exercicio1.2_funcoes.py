# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

import os
# cria as variaveis
numero = ''
resultado = ''

# define e funcao que faz a checagem
def checagem(numero):
    if numero % 2 == 0:
        return f'o numero {numero} e par'
    return f'o numero {numero} e impar'

# pede ao usuario para inserir um numero inteiro
numero = input('digite um numero inteiropara saber se e par ou impar: ')
while numero.isdigit() == False:
    os.system('cls')
    numero = input('digite apenas numeros inteiros: ')
resultado = checagem(int(numero))

os.system('cls')
print(resultado)