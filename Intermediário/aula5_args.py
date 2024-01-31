"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""

# Lembre-te de desempacotamento
#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)

#def soma(x, y):
#    return x + y

def soma(*args):
    print(args, type(args))

soma(1, 2, 3, 4, 5, 6)

print('-----------------')

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return(total)

print(soma(1, 2, 3, 4, 5, 6))
print(soma(1, 2, 5, 6))
print(soma(1, 6))

print('-----------')

print(sum((1, 2, 4, 87, 3245)))

print('------------')

numeros = 1, 2, 3, 4, 5
print(numeros)
#outra_soma = soma(numeros) # retorna uma tupla dentro de uma tupla
#print(outra_soma)

#solucao
print('---------------')

print(*numeros)
outra_soma = soma(*numeros)
print(outra_soma)