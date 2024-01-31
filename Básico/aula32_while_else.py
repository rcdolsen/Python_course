str = input('Digite um nome: ')

i = 0
while i < len(str):
    letra = str[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Nao encontrei um espaco na string')
print('fora do while')