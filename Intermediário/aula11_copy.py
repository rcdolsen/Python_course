# copy - retorna uma cópia rasa (shallow copy)

d1 = {
    'c1': 1,
    'c2': 2,
    'c3': [0, 1, 2],
}

d2 = d1 # serao sempre iguais, se um for alterado o outro tambem vai

d2['c1'] = 1000
print(d1)
print('------------')

d2 = d1.copy() # so copia o que for imutavel para economizar dados

d2['c1'] = 50 # so altera em 1
d2['c3'][1] = 9999 # altera nos 2

print(d1)
print(d2)
print('------------')

# para resolver o problema

import copy

d2 = copy.copy(d1) # faz o mesmo que o copy normal

d2 = copy.deepcopy(d1)

d2['c3'][1] = 743

print(d1)
print(d2)
print('------------')