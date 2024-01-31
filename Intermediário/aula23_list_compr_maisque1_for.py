lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)
print('---------1')

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]
print(lista)
print('---------2')

lista = [
    [(x, letra) for letra in 'Marrom']
    for x in range(3)
]

print(lista)