"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
lista.append('Marrom')
print(lista, lista.pop())

lista.append('khgdwfv')
print(lista)
del lista[-1]
print(lista)

# lista.clear() limpa a lista
# print(lista)

lista.insert(0, 'Marrom')
print(lista)

lista.insert(100, 5) # insere no indice 100 ou no ultimo sem retornar um erro
print(lista)

