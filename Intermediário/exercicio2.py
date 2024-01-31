# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

number_given = ''

def outer_function():
    def double_function():
        number = float(number_given)
        return f'{number * 2:.10}'
    def triple_function():
        number = float(number_given)
        return f'{number * 3:.10}'
    def quadruple_function():
        number = float(number_given)
        return f'{number * 4:.10}'
    return double_function(), triple_function(), quadruple_function()

number_given = input('digite um numero').replace(',' , '.')

while not number_given.replace('.', '').isdigit:
    number_given = input('digite apenas numeros')

print(*outer_function())