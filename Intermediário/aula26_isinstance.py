# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Marrom'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print('set', item, isinstance(item, set))
    
    elif isinstance(item, str):
        print('str', item.upper(), isinstance(item, set))

    elif isinstance(item, (int, float)): # Ou int ou float
        print('num', item,'dobro', item * 2)

    else:
        print('outro', item)