#Receba dois números inteiros correspondentes à largura e altura. Devolva uma cadeia de caracteres # que representa um retângulo com as medidas fornecidas.

i = 1
l = 10
a = 10
width = 0

for i in range(l):
    width += 1

print('#' * width)

i = 1

for i in range(a-2):
    print('#' + (' ' * (width - 2)) + '#')

print('#' * width)