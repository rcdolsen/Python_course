"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero = input('vou dobrar o numero que for digitado ')

try:
    print('STR: ', numero)
    f_numero = float(numero)
    print('float: ', f_numero)
    print(f'O dobro do {f_numero} e {f_numero * 2:.2f}')
except:
    print('isso nao e um numero')


# if numero.isdigit():
#     f_numero = float(numero)
#     print(f'O dobro do {f_numero} e {f_numero * 2:.2f}')
# else:
#     print('isso nao e um numero')