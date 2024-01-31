# Manipulando chaves e valores em dicionarios

pessoa = {}

pessoa['nome'] = 'Marrom Siqueira'
lista = []

print(pessoa)
print(pessoa['nome'])

print('------------')

chave = 'nome'

pessoa[chave] = 'Marrom Siqueira'
lista = []

print(pessoa)
print(pessoa[chave])

print('------------')

chave = 'nome'

pessoa[chave] = 'Marrom'
pessoa['sobrenome'] = 'Siqueira'

print(pessoa)

pessoa[chave] = 'Julia'

del pessoa['sobrenome']

print(pessoa)
# print(pessoa['sobrenome'])  o indice nao existe mais e gera um erro no programa

# para resolver
print('----------')

print(pessoa.get('sobrenome')) # Retorna None
# if pessoa.get('sobrenome', None): Nome e o padrao, nao e preciso escrver]
print('----------')

if pessoa.get('sobrenome') is None:
    print('Nao existe')
else:
    print(pessoa['sobrenome'])

print('----------')

pessoa['sobrenome'] = 'Siqueira'

if pessoa.get('sobrenome') is None:
    print('Nao existe')
else:
    print(pessoa[chave], pessoa['sobrenome'])