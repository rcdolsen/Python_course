import Aula37_m

print('Este modulo chame-se', __name__)
print('-----------1')
print(Aula37_m.variavel_modulo)
print('-----------2')

# ou 

from Aula37_m import variavel_modulo

print(variavel_modulo)
print('-----------3')

from Aula37_m import variavel_modulo, soma

print(variavel_modulo, soma(2, 3))
print(Aula37_m.soma(2, 3))