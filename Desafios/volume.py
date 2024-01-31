#Krissia gosta de bolinhas de queijo. Ela quer saber quantas bolinhas de queijo dá para colocar dentro de um pote de sorvete de 
#. Ela pensou assim:

#Um pote de sorvete tem dimensões 15 cm x 10 cm x 13 cm. Uma bolinha de queijo é uma esfera de raio r = 1.2 cm. O fator de empacotamento ideal é 0.74, mas o pote de sorvete tem tamanho comparável às bolinhas de queijo, aí tem efeitos de borda, então o fator deve ser menor. Mas as bolinhas de queijo são razoavelmente elásticas, então empacota mais. Esse valor parece razoável.

#Sabendo que o volume de uma esfera de raio r é V = 4/3 πr⒊, o volume do pote de sorvete é V = xyz
# e o fator de empacotamento é a fração de volume ocupado pelas bolinhas de queijo. Ou seja, 74%
# do pote de sorvete vai ser ocupado pelas bolinhas de queijo.

#Ajude a Krissia descobrir quantas bolinhas de queijo cabem no pote de sorvete!

import math

x = 15
y = 10
z = 13

r = 1.2

factor = 0.74

v_cheese = (4/3) * math.pi * (r ** 3)
v_ice_cream = x*y*z

occupation = v_ice_cream * factor / v_cheese

print(occupation)