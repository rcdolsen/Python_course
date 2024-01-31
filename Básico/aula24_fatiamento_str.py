"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i == inicio
f == fim
p == passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Ola mundo'
print(variavel[-4])
print(variavel[4:])
print(variavel[4:7])
print(variavel[:7])
print(variavel[-8:-2])
print(variavel[0:9:2])
print(variavel[-1:-10:-1])
print(variavel[::-1])
print(variavel[0:-1])
print(len(variavel[-8:-2]))