numeros = [1, 2, 3, 4, 5]
novos_numeros = numeros # as 2 var apontam ao mesmo valor na memoria, nao e uma copia

numeros[0] = 20
print(novos_numeros)

novos_numeros[1] = 10
print(numeros)
print('----------1')

# Shallow copy

numeros = [1, 2, 3, 4, 5]
novos_numeros = numeros.copy()

numeros[0] = 20
novos_numeros[1] = 10

print(numeros)
print(novos_numeros)

print('----------2')

numeros = [1, 2, 3, 4, 5]
novos_numeros = []

for numero in numeros:
    novos_numeros.append(numero)

print(novos_numeros)
print('----------3')

novos_numeros = [
    numero
    for numero in numeros
]
print(novos_numeros)
print('----------4')

divisao = [
    numero / 2
    for numero in numeros
]
multiplicacao = [
    numero * 2
    for numero in numeros
]
quadrado = [
    numero ** 2
    for numero in numeros
]
print(divisao)
print(multiplicacao)
print(quadrado)
print('----------5')

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def square(x, y):
    return x ** y

divisao = [
     divide(numero, 2)
    for numero in numeros
]
multiplicacao = [
    multiply(numero, 2)
    for numero in numeros
]
quadrado = [
    square(numero, 2)
    for numero in numeros
]
print(divisao)
print(multiplicacao)
print(quadrado)
print('----------6')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [
    numero
    for numero in numeros
    if numero > 5
]
impares = [
    numero
    for numero in numeros
    if numero % 2 != 0 
]
pares = [
    numero
    for numero in numeros
    if numero % 2 == 0
]
outro_if = [
    numero
    if numero != 6 else 600
    for numero in numeros
    if numero % 2 == 0
]
outro_if_2 = [
    numero
    if numero != 6 else 600
    for numero in pares
]
print(numeros)
print(novos_numeros)
print(impares)
print(pares)
print(outro_if)
print(outro_if_2)

print('----------7')

for x in range(1, 11):
    for y in range(1, 6):
        print(x, y)
print('----------8')

linhas_e_colunas = [
    (x, y)
    if y == 2 else 'Voce nao e 2'
    for x in range(1, 11)
    for y in range(1, 6)
    if x == 2
]
print(linhas_e_colunas)
print('----------9')

stringue = 'Marrom Siqueira'
nova_string = [
    letra
    for letra in stringue
]
print(nova_string)
print('----------10')

stringue = 'Marrom Siqueira'
nova_string = ''.join([
    letra
    for letra in stringue
])
print(nova_string)
print('----------11')

nova_string = [
    stringue.replace(' ', '')[indice:indice + 2]
    for indice in range(0, len(stringue) - 1, 2)
]
print(nova_string)
print('----------12')

nomes = ['Marrom', 'Mozuda', 'Julian', 'Julia', 'Theo']
inicial = [
    letra
    for nome in nomes
        for letra in nome
        if letra == letra.upper()
]
print(inicial)
print('----------13')

nomes = ['marrom', 'mozuda', 'julian', 'julia', 'theo']
novos_nomes = [
    nome.title()
    for nome in nomes
]
print(novos_nomes)
print('----------14')

nomes = ['marrom', 'mozuda', 'julian', 'julia', 'theo']
novos_nomes = [
    nome.upper()
    for nome in nomes
]
print(novos_nomes)
print('----------15')

nomes = ['marrom', 'mozuda', 'julian', 'julia', 'theo']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
print(novos_nomes)
print('----------16')

numeros = [
    [numero, numero ** 2]
    for numero in range(10)
]
flat = [y for x in numeros for y in x]
print(numeros)
print('----------17')
print(flat)