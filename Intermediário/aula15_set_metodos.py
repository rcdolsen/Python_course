# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Marrom')
s1.add(1)
print(s1)
s1.update(('ola mundo', 1, 2, 3, 4)) # Pode ser usado para adicionar varios valores ao mesmo tempo
print(s1)
print('-----------------')
s1.clear()
print(s1)
print('-----------------')

s1 = set(('ola mundo', 1, 2, 3, 4))
s1.discard('ola mundo')
print(s1)