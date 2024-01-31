# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime

from pytz import timezone

# date_str = '2022-04-20 07:49:23'
# date_str_format = '%Y-%m-%d %H:%M:%S'

# ou

date_str = '20/04/2022 07:49:23'
date_str_format = '%d/%m/%Y %H:%M:%S'

# date = datetime(2022, 4, 20, 7, 49, 23)

date = datetime.strptime(date_str, date_str_format)

print(date)

print('-' * 49)
print(datetime.now())

print('-' * 49)
print(datetime.now(timezone('Europe/Madrid')))

print('-' * 49)
print(datetime(2023, 8, 16, 12, 12, 12, tzinfo=timezone('Europe/Madrid')))

print('-' * 49)
date = datetime.now()
print(date.timestamp())
print(datetime.fromtimestamp(1692202729.383866))
