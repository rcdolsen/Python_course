# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
    'nome:': 'Marrom',
    'sobrenome:': 'Siqueira'
}

print(len(pessoa))
print('--------')
print(pessoa.keys())
print(list(pessoa.keys()))
print('--------')
print(list(pessoa.values()))
print('--------')

for chave in pessoa.keys():
    print(chave)
# retorna a mesma coisa
for chave in pessoa:
    print(chave)

print('--------')

for valor in pessoa.values():
    print(valor)
print('--------')

print(list(pessoa.items()))
print('--------')

for chave, valor in pessoa.items():
    print(chave, valor)

print('--------')
pessoa.setdefault('idade', 0)
print(pessoa['idade']) # nao retorna erro mais