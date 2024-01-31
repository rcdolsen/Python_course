#Escreva uma função chamada has_duplicates que tome uma lista e retorne True se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.

lister = [
    1,
    2,
    'abc',
    'bcd',
    1,
]

duplicate = []

def has_duplicate(list):
    for i in range(len(list) - 1):

        for x in range(i + 1, len(list)):
            if list[i] == list[x]:
                duplicate.append(list[i])
    return duplicate

has_duplicate(lister)

if len(duplicate) != 0:
    print(f'Os itens {duplicate} estao duplicados')
else:
    print('nao ha itens duplicados')