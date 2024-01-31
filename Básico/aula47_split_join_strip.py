"""
split, strip e join com list e str
split - divide uma string (list)
strip corta os espacos a direita e esquerda
rstrip corta a direita
lstrip corta a esquerda
join - une uma string (nao aceita numeros)
"""

# frase = "hello world , it's a beautiful day"
# lista_frases = frase.split(',')
# print(lista_frases)

# for i, frase in enumerate(lista_frases):
#     print(lista_frases[i])

# for i, frase in enumerate(lista_frases):
#     lista_frases[i] = lista_frases[i].strip()

# print(lista_frases)

frase = "hello world , it's a beautiful day"
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frases)

frases_unidas = '-'.join('abc')
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)