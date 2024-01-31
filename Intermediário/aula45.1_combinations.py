# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from aula45_modulo import pessoas

from itertools import combinations

def printer(iterator):
    print(*list(iterator), sep='\n')

printer(combinations(pessoas, 1))
print('--------1')
printer(combinations(pessoas, 2))
print('--------2')
printer(combinations(pessoas, 3))
print('--------3')
printer(combinations(pessoas, 4))
print('--------4')
