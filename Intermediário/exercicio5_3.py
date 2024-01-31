# copy, sorted, produtos.sort
# Exercícios

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

from exercicio5_modulos import produtos

New_sort_price = [
    p
    for p in sorted(copy.deepcopy(produtos), key=lambda x: x['preco'] if x['preco'] else float('inf'))
]  


print(*produtos, sep= '\n')
print('------------1')
print(*New_sort_price, sep= '\n')