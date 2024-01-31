import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
#iterator = iter(iterable)  # tem __iter__ e __next__

#print(iterator)

#for i in range(0,4):
#    print(next(iterator)) # a cada print ele imprime o proximo valor e para a iteracao no ultimo

lista = [n for n in range(1000000)]
print(sys.getsizeof(lista))

generator = (n for n  in range(1000000))
print(sys.getsizeof(generator)) 

for i in generator:
    print(i)
# generator fica pausado na memoria como o iterator, diferente da lista que entrega ocupa todo o espaco de uma vez