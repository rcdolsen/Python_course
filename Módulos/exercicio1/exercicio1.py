# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

import json
from datetime import datetime

from dateutil.relativedelta import relativedelta

FILE_PATH = 'Módulos\exercicio1\exercicio1.json'
# data Variable
format = '%d/%m/%Y'
total = 1_000_000.00
loan_date = datetime(2020, 12, 20)
delta_years = relativedelta(years=5)

# Variables for the calculation
loan_date_end = loan_date + delta_years
installment_months = delta_years.years * loan_date.month
installment_value = total / installment_months

# print payment informations
print(f'data inicial do emprestimo {loan_date.strftime(format)}\n')
print(f'data final do emprestimo {loan_date_end.strftime(format)}\n')
print(f'Valor total devido {total:,.2f}\n')
print(f'valor da parcela {installment_value:,.2f}\n')
print('')
print('---- plano de pagamento do emprestimo ----')
print('')

# calculate the payment plan
i = 0
save_data = []
while i < installment_months:
    i += 1
    total -= installment_value

    # save in a json file
    save_data.append({
        'pagamento': i,
        'data de vencimento': loan_date.strftime(format),
        'Total restante a pagar': f'{total:,.2f}'
    })

    with open(FILE_PATH, 'w', encoding='utf8') as archive:
        json.dump(save_data, archive, ensure_ascii=False, indent=2)

    # Show the payment plan
    print(
        f'Pagamento {i}\n'
        'data de vencimento: '
        f'{loan_date.strftime(format)}\n'
        f' total restante a pagar: {total:,.2f}'
    )

    if loan_date.month < 12:
        loan_date = datetime(
            loan_date.year, loan_date.month + 1, loan_date.day
        )
    else:
        loan_date = datetime(
            loan_date.year + 1, 1, loan_date.day
        )
