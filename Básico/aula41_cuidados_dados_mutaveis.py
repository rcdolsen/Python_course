"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Alfredo', 'Maria']
lista_b = lista_a

lista_a[0] = 'Marrom'
print(lista_b)
print(lista_a)

lista_a = ['Alfredo', 'Maria']
lista_b = lista_a.copy()

lista_a[0] = 'Marrom'
print(lista_b)
print(lista_a)