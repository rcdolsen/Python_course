# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('7/9/1988 7:30:30', fmt)
data_fim = datetime.strptime('12/12/2023 03:30:30', fmt)

# print(data_fim > data_inicio)
# print(data_fim < data_inicio)
# print(data_fim == data_inicio)

print(data_fim - data_inicio)
print('-' * 49)

dif = data_fim - data_inicio

print(dif.days, dif.seconds, dif.total_seconds())
print('-' * 49)

dif = timedelta(weeks=10)
print(dif)
print('-' * 49)

print(data_fim + dif)
print('-' * 49)

print(data_fim + relativedelta(seconds=60))
print('-' * 49)

print(datetime.now() + relativedelta(seconds=15, hours=2))
print('-' * 49)

print(relativedelta(data_inicio, datetime.now()))
