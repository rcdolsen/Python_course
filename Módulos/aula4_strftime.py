# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

from datetime import datetime

fmt = '%d/%m/%Y'
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data)
print('-' * 40)

print(data.strftime(fmt))
print('-' * 40)

print(data.strftime('%d/%m/%Y'))
print('-' * 40)

print(data.strftime('%d/%m/%Y %H:%M'))
print('-' * 40)

print(data.strftime('%d/%m/%Y %H:%M:%S'))
print('-' * 40)

print(data.strftime('%Y'))
print('-' * 40)

print(type(data.strftime('%d/%m/%Y')))
print('-' * 40)

print(data.strftime('%Y'), data.month)
print('-' * 40)

print(type(data.strftime('%Y')), data.strftime(
    '%Y'), type(data.month), data.month)
print('-' * 40)
