"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

# nome = 'Marrom'
# preco = 1000.95897643
# variavel = '%s, o preco e %.2f' % (nome, preco)
# print(variavel)
hexa = input('digite um valor para saber qual o hexadecimal')
int_hexa = int(hexa)
print('o hexadecimal de %d e %04x' % (int_hexa, int_hexa))
print('o hexadecimal de %d e %X' % (int_hexa, int_hexa))