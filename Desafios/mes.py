#Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.
months = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

while True:

    try:
        x = int(input(f'digite o numero do mes\n'))
    except(ValueError):
        print('digite apenas numeros inteiros')
        continue

    if x > 0 and x <= 12:
        print(f'O mes e {months[x-1]}')
    else:
        print('Os meses sao de 1 a 12')
        continue
    
    break