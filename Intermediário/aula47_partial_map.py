# map, partial, GeneratorType e esgotamento de Iterators

from functools import partial # retorna uma closure
from types import GeneratorType # serve para checar se a funcao e um generator ou um iterator

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return f'{(valor * porcentagem):.2f}'

aumentar_dez_porcento = partial(
    aumentar_porcentagem, 
    porcentagem=1.1
)

#novos_produtos = [
#    {**p,
#        'preco': aumentar_dez_porcento(p['preco'])} 
#        for p in produtos
#]

def muda_preco(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(
            produto['preco']
        )
    }

novos_produtos = list(map( #map e um iterator, list serve para nao esgotar o iterator e poder usar novamente
    muda_preco, produtos
))

print_iter(produtos)
print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorType))
print()

# Map com lambda

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)