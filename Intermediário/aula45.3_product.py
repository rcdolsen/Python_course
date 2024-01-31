# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from aula45_modulo import camisetas

from itertools import product

def printer(iterator):
    print(*list(iterator), sep='\n')

printer(product(camisetas))
print('--------1')
printer(product(*camisetas))
