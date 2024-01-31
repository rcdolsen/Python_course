# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from aula45_modulo import pessoas

from itertools import permutations

def printer(iterator):
    print(*list(iterator), sep='\n')

printer(permutations(pessoas, 1))
print('--------1')
printer(permutations(pessoas, 2))
print('--------2')
printer(permutations(pessoas, 3))
print('--------3')
printer(permutations(pessoas, 4))
print('--------4')
