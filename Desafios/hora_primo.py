#Para escolher a melhor opção, você gostaria de saber todos os horários que satisfazem esta condição!

#Crie um programa que imprime no formato HH:MM todos os horários cuja hora e minuto são números primos.

minutes = []
hour = []
mod = 0
count = 0
condition = {}

def counter(count, test):
    count = 0
    for i in range(1, test + 1):
        mod = test % i
        if mod == 0:
            count += 1
    return count

for test in range(1, 60):

    if counter(count, test) <= 2:
        minutes.append(test)

for test in range(1, 24):

    if counter(count, test) <= 2:
        hour.append(test)

for x in range(len(hour)):
    for y in range(len(minutes)):
        print(f'{hour[x]:02d}:{minutes[y]:02d}')

#condition = dict(zip(hour, minutes))
#print(condition)