#Receba uma lista com números inteiros e devolva um número inteiro correspondente à soma dos números recebidos.

numbers = []

def sum():
    summer = 0
    for x in numbers:
        summer += numbers[x - 1]
    return summer

while True:
    number = int(input('digite quais numeros quer somar'))
    numbers.append(number)
    sim_nao = input('fazer a soma (s) ou (n)').lower()
    if sim_nao == 's':
        break

print(sum())