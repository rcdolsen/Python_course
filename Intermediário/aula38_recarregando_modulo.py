import importlib

import Aula38_m

print(Aula38_m.variavel)

for i in range(3):
    print(i)
    import Aula38_m # O modulo so e importado 1 vez, e necessario usar o import lib para importar varias vezes

print("C'est finis")

for i in range(3):
    print(i)
    importlib.reload(Aula38_m)

print("C'est finis de novo")