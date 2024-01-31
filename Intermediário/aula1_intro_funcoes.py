"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

def printy():
    print('Hello world, its a beautyful day')
    print('Hello world, its a beautyful morning')
    print('Hello world, lets go out')

printy()

def imprimir(a, b, c):
    print(a, b, c)

imprimir(1, 2, 3)
imprimir(3, 2, 1)
#imprimir() # erro

def saudacao(nome = 'sem nome'):
    print(f'ola, {nome}')

saudacao('julia')
saudacao('Ana julia')
saudacao('juliana')
saudacao()