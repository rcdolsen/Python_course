"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete (CRUD)
Criar, ler, alterar, apagar = lista[i] 
"""
#        0    1  2   3
lista = [10, 20, 30, 40]
numero = lista[2] = 300 
print(numero)

del lista[2]
print(lista)
print(lista[2])

lista.append(50) #insere no ultimo indice
lista.append(60)
lista.append(70)
print(lista)

lista.pop() #apaga o ultimo
print(lista)

print('removido', lista.pop()) #apaga e mostra o apagado ao mesmo tempo
print(lista)

removi_o_20 = lista.pop(1)
print('removi o', removi_o_20)
print(lista)



