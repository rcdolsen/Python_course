# dir, hasattr e getattr em Python

string = 'Marrom'
metodo = 'upper'

print(string)

if hasattr(string, 'upper'):
    print('existe upper')
    print(string.upper())

print('----------1')

if hasattr(string, metodo):
    print('existe upper')
    print(getattr(string, metodo)())
else:
    print('Nao existe o metodo', metodo)