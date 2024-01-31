#Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.

int_list = []

for x in range(5):
    while True:
        try:
            int_list.append(int(input('digite um numero inteiro\n')))
        except(ValueError):
            print('so numeros inteiros sao aceitos')
            continue
        break

print(min(int_list))

#Ler do teclado uma lista com 5 inteiros e imprimir True se a lista estiver ordenada de forma crescente ou False caso contrário.

if int_list == sorted(int_list):
    print(True)
else:
    print(False)