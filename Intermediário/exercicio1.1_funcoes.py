# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

import os

# cria as variaveis
total = 1
numero = 0
n = '0'
inserido = []
resultado = ''

# define e funcao que faz a multiplicacao
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

# pede ao usuario para inserir os numeros
while n.isdigit():
    n = input('digite os numeros a serem multiplicados 1 de cada vez, ou qualquer letra ou palavra para fazer a multiplicacao do que foi inserido',)
    os.system('cls')
    if n.isdigit():
        print(f'numero {n} inserido')
        print('')
        inserido.append(int(n))
    else:
        break
    
resultado = multiplicacao(*inserido)
print(f'o resultado da multiplicacao dos numeros {inserido} e:, {resultado}')