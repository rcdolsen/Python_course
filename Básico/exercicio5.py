"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('digite um numero: ')

# if numero.isdigit():
#     int_numero = int(numero)
#     if (int_numero % 2) == 0:
#         print('O numero e par')
#     else:
#         print('O numero e impar')
# else:
#     print('o numero nao e inteiro')
    
try:
    f_numero = float(numero)

    if (f_numero % 2) == 0:
        print('O numero e par')
    elif (f_numero % 2) == 1:
        print('O numero e impar')
    else:
        print('o numero nao e inteiro')
        
except:
    print('isso nao e um numero')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('qual e a hora? ')

try:
    str_hora = int(hora)

    dia = str_hora >= 0 and str_hora <=11
    tarde = str_hora >= 12 and str_hora <=17
    noite = str_hora >= 18 and str_hora <=23

    if dia:
        print('bom dia')
    elif tarde:
        print('boa tarde')
    elif noite:
        print('Boa noite')
    else:
        print('isso nao e uma hora')
except:
    print('a hora deve ser numerica')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual o seu nome? ')
tamanho = len(nome)

curto = tamanho <= 4
normal = tamanho > 4 and tamanho <= 6
longo = tamanho > 6

if curto:
    print('Seu nome e curto')
elif normal:
    print('Seu nome e normal')
else:
    print('Seu nome e muito longo')