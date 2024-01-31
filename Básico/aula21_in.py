# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  M a r r o m
# -6-5-4-3-2-1

nome = 'Marrom'
print(nome[2])
print(nome[-4])

print(10 * '-')
print('r' in nome)
print('Mar' in nome)

print(10 * '-')
print('z' in nome)
print('maz' in nome)

print(10 * '-')
print('r' not in nome)
print('z' not in nome)

nome = input('Digite seu nome:')
encontrar = input('Digte o que deseja encontrar: ')

if (encontrar in nome):
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')