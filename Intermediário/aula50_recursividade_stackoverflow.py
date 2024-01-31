# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

'''
#from sys import setrecursionlimit # aumenta o limite da recursao

#sys.setrecursionlimit(1004)

def recursiva(start=0, end=10):

    print('start:', start, 'end:', end)

    if start >= end:
        return start

    start += 1
    return recursiva(start, end)

print(recursiva(0, 1000))
'''

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print('--------1')
print(factorial(10))
print('--------2')
print(factorial(100))