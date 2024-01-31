# count é um iterador sem fim (itertools)
from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))
print('---------0')


print(r1)
print('---------1')
print(c1)
print('---------2')
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print(next(c1))
print('---------3')

#for i in c1:
#    if i > 100:
#        break
#    print(i)

#for i in r1:
#    print(i)

print('--------4')

c1 = count(10, 5)
r1 = range(10, 30, 2)


for i in c1:
    if i > 100:
        break
    print(i)

for i in r1:
    print(i)