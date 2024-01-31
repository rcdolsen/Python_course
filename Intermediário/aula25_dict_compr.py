# Dictionary Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

dc = {
    chave.upper(): valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}
print(dc)
print('-----------1')

dc = {
    chave.upper(): valor
    if isinstance(valor, (int, float)) else valor.upper()
    for chave, valor in produto.items()
}
print(dc)
print('-----------2')

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
dc = {
    chave: valor
    for chave, valor in lista
}
print(dc)

print('-----------3')

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
print(dict(lista))

print('-----------4')

# Set Comprehension

s1 = {i ** 2 for i in range(10)}
print(s1)