#Ler do teclado 5 números e imprima a quantidade de números entre 10 e 50.

number = []
count = 0

for x in range(5):
    while True:

        try:
            number.append(float(input('digite um numero\n')))
        except(ValueError):
            print('so numeros reais sao aceitos')
            continue

        if number[x] > 10 and number[x] < 50:
            count += 1

        break

print(f'existem {count} numeros entre 10 e 50')