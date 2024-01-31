#Um supermercado está tendo muitos problemas com a validade de seus produtos e pediu sua ajuda com esse problema. Faça um programa que leia o dia, o mês e o ano da data atual e de validade de um produto, e imprima se o produto já está vencido ou não.

import datetime

today = datetime.date.today()

while True:

    try:
        best_before = datetime.datetime.strptime(input('digite a data de validade no formato dd/mm/aaaa\n'), '%d/%m/%Y').date()
    except(ValueError):
        print('a data deve ser digitada no formato dd/mm/aaa\n')
        continue

    break

days = (best_before - today).days

if days > 0:
    print(f'faltam {days} dias para o fim da validade')
elif days == 0:
    print('A validade acaba hoje')
else:
    print('O produto ja esta fora da validade')