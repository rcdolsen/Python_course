# reduce - faz a redução de um iterável em um valor
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total = 0
for price in produtos:
    total += price['preco']

print(total)
print('-------1')

# Ou

print(
    sum(
        [p['preco'] for p in produtos]
    )
)
print('-------2')

# Ou

def funcao_do_reduce(acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

total = reduce(
    funcao_do_reduce,
    produtos,
    0) # valor inicial

print('O total e', total)
print('-------3')

# Ou

total = reduce(
    lambda ac, p:ac + p['preco'],
    produtos,
    0
)

print('O total e', total)