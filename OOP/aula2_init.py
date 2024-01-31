# Introdução ao método __init__ (inicializador de atributos)


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Marrom', 'Siqueira')
#p1.nome = 'Marrom'
#p1.sobrenome = 'Siqueira'

p2 = Pessoa('Theo', 'Siqueira')
#p2.nome = 'Theo'
#p2.sobrenome = 'Siqueira'

#print(p1)
print(p1.nome)
print(p1.sobrenome)

print('-' * 50)

#print(p2)
print(p2.nome)
print(p2.sobrenome)