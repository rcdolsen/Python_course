"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# texto = 'Marrom'.__iter__() 

# ou

# texto = iter('Marrom')

# print(texto)

# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())

# ou

# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# for letra in texto
# print(letra)

texto = 'Marrom' # Iteravel
iterador = iter(texto) #iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break