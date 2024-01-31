#from sys import path

#from Aula39_package.modulo import soma_do_modulo

##print(*path, sep='\n')
#print(soma_do_modulo(1, 2))

## OU

#import Aula39_package.modulo

#print(Aula39_package.modulo.soma_do_modulo(2, 2))

## OU

#from Aula39_package import modulo

#print(modulo.soma_do_modulo(2, 3))

## OU (ma pratica)

#from Aula39_package.modulo import *

#print(soma_do_modulo(3, 3))
#print(variavel)

#print('----------1')

#from Aula39_package.modulo import fala_oi

#fala_oi()

#print('----------2')


from Aula39_package import soma_do_modulo

print(soma_do_modulo(2, 3))