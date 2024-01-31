""" Calculadora com while """
numeros_validos = None
op_valido = ('+-/*')
num1 = ''
num2 = ''
num1_f = ''
num2_f = ''
operador = ''
sair = ''

while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break

    num1 = input('digite o primeiro numero: ')
    num2 = input('digite o segundo numero: ')
    try:
        num1_f = float(num1)
        num2_f = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('1 ou os 2 valores sao invalidos')
        continue

    operador = input('Digite o operador (+-/*): ')

    while operador not in op_valido:
        print('operador invalido')
        operador = input('Digite o operador (+-/*): ')
        continue
    
    if len(operador) != 1:
        print('Apenas um operador permitido')

    if operador == '-':
        print(f'{num1_f} - {num2_f} =', num1_f - num2_f)
    elif operador == '+':
        print(f'{num1_f} + {num2_f} =', num1_f + num2_f)
    elif operador == '/':
        print(f'{num1_f} / {num2_f} =', num1_f / num2_f)
    elif operador == '*':
        print(f'{num1_f} * {num2_f} =', num1_f * num2_f)   

    # sair = input('Quer sair? [s]im: ').lower().startswith('s')

    # if sair:
    #     break