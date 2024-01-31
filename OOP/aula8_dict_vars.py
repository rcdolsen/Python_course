# __dict__ e vars para atributos de instância

class Pessoa:
    this_year = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birth_date(self):
        return Pessoa.this_year - self.idade
    
p1 = Pessoa('Marrom', 5)
p1.nome = 'Pingo'
print(p1.nome)
print(p1.idade)
del p1.nome
#print(p1.nome) erro sem atributo
p2 = Pessoa('Mozuda', 35)
print(p2.__dict__)
print(vars(p2))

print('-' * 50)
# __dict__ e editavel

#p2.__dict__['nome'] = 'Nova Mozuda'
#p2.__dict__['wheg'] = 'jqsdhg'
#print(p2.__dict__)

dados = {'nome': 'Theo', 'idade': 0}
p3 = Pessoa(**dados)
print(vars(p3))