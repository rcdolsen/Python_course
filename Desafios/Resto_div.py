#Calcule o resto da divisão
n = 0
d = 0
r = 0
t = 0
div = 0

def division(n, d):
    if d == 0:
        print('Nao existe divisao por 0, digite outro numero')
        d = try_value_error()

    div = n // d
    print('O resultado da divisao de ', n, ' por ', d, ' e:', div)
    r = n % d
    return r

def try_value_error():
    while True:
        try:
            t = int(input())
        except(ValueError):
            print('Digite um numero inteiro')
            continue
        break
    return t

print('Qual o numero a ser dividido?')
n = try_value_error()
    
print('Por quanto quer dividir?')
d = try_value_error()

print('O resto da divisao de ', n, ' por ', d, ' e:', division(n, d))