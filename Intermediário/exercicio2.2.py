# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_mult(multiplicador):
    def mult(numero):
        return multiplicador * numero
    return mult

number_given = input('digite um numero').replace(',' , '.')

while not number_given.replace('.', '').isdigit():
    number_given = input('digite apenas numeros')

number_float = float(number_given)

r2 = criar_mult(2)
r3 = criar_mult(3)
r4 = criar_mult(4)

print(r2(number_float))
print(r3(number_float))
print(r4(number_float))