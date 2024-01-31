# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def double(number):
    return f'{(number * 2):.10}'

def triple(number):
    return f'{(number * 3):.10}'

def quadruple(number):
    return f'{(number * 4):.10}'

def get_number():
    while True:
        try:
            number_given = float(input('Digite um numero ').replace(',' , '.'))
            break
        except ValueError:
            print('digite apenas numeros ')
    return number_given

number = get_number()

print('Resultados:')
print('Dobro: ', double(number))
print('triplo: ', triple(number))
print('quadruplo: ', quadruple(number))
