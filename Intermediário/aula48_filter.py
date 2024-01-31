# filter é um filtro funcional

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

def filtra_preco(produto):
    return produto['preco'] > 100

# e o mesmo que usar:
#lambda produto: produto['preco'] > 100
# A diferenca e que lambda e anonima e nao pode ser chamada diretamente em outras partes do codigo

novos_produtos = filter(
    filtra_preco, produtos
)

print_iter(produtos)
print('---------1')
print_iter(novos_produtos)