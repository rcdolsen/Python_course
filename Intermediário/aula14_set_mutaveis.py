# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Seus valores serão sempre únicos;
# - Não aceitam valores mutáveis;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

t1 = [1, 2, 3, 3, 3, 3, 1]
s1 = set(t1)
t2 = list(s1)
print(t1)
print(t2)
print('-------------')

# s1 = {1, 2, 3, [123]} erro, lista e mutavel
s1 = {1, 2, 3, (123,)} # tuplas sao aceitas com uma virgula no final
print(s1)
print('-------------')

s1 = {1, 2, 3}
print(3 in s1)
print(4 in s1)
print(4 not in s1)
print('-------------')

for numero in s1:
    print(numero)