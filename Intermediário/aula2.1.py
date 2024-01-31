"""
Valores padrao para parametros
ao definir uma funcao, os parametros podem ter valores padrao. Caso o valor nao seja enviado para o parametro, o valor padrao sera usado.
refatorar: editar o seu codigo.
"""

def soma(x, y, z=0):
    if z:
        print(f'{x=} {y=} {z=}; soma:', x + y + z)
    else:
        print(f'{x=} {y=}; soma:', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(100, 200, 0)
soma(100, 200, 1)

print('-----------------------')
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}; soma:', x + y + z)
    else:
        print(f'{x=} {y=}; soma:', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(100, 200, 0)