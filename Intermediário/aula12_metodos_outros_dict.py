# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Marrom',
    'sobrenome': 'Siqueira'
}

# print(p1['idade:']) # retorna erro se nao existir
print(p1.get('idade:', 'nao existe'))

print('----------')

"""
nome = p1.pop('nome:')
print(nome) # retorna o que foi apagado
print('----------')
print(p1)

print('----------')
"""

'''
ultima_chave = p1.popitem()
print(ultima_chave) # retorna o que foi apagado
print('----------')
print(p1)
'''

p1.update({
    'nome': 'Julia', # atualiza o valor da chave
    'idade': 0, # adiciona uma nova chave
    })
print(p1)
print('----------')

# ou

p1.update(nome= 'Julia', idade= 0)
print(p1)
print('----------')

# ou

tupla = ('nome', 'Julian'), ('idade', 1)
p1.update(tupla)
print(p1)
print('----------')

lista = ('nome', 'theo'), ('idade', 2)
p1.update(lista)
print(p1)