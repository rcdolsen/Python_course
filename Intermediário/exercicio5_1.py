# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

from exercicio5_modulos import produtos

new_price = [
    {**product, 'preco': round(product['preco'] * 1.1, 2)}
    if isinstance(product['preco'], (int, float)) else {**product, 'preco': 'N/A'}
    for product in copy.deepcopy(produtos)
]

print(*produtos, sep='\n')
print('------------1')
print(*new_price, sep='\n')