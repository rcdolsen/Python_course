#Davinir não gosta de ir às aulas. Mas ele é obrigado a comparecer a pelo menos 75% delas. Ele quer saber quantas aulas pode faltar, sabendo que tem duas aulas por semana, durante quatro meses. Ajude o Davinir!

#Nota

#Um mês tem quatro semanas.
import math

classes = 2 * 4 * 4
max_f = math.floor(classes * 0.25)
print('pode faltar a', max_f, 'aulas')

gatinhos = {"Português": "gato", "Inglês": "cat", "Francês": "chat", "Finlandês": "Kissa"}
for chave, valor in gatinhos():
    print(chave, "->", valor)