# copy, sorted, produtos.sort
# Exercícios

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

import copy

from exercicio5_modulos import produtos

new_sort = copy.deepcopy(produtos)

new_sort.sort(key=lambda n: n['nome'], reverse= True)

print(*produtos, sep = '\n')
print('-----------1')
print(*new_sort, sep = '\n')