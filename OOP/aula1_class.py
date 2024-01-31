# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

string = 'Marrom'
print(string.upper())
print(isinstance(string, str))

print('-' * 50)


class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'Marrom'
p1.sobrenome = 'Siqueira'

p2 = Pessoa()
p2.nome = 'Theo'
p2.sobrenome = 'Siqueira'

print(p1)
print(p1.nome)
print(p1.sobrenome)

print('-' * 50)

print(p2)
print(p2.nome)
print(p2.sobrenome)

print('-' * 50)
