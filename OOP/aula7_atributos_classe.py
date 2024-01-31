# Atributos de classe

class Pessoa:
    this_year = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_birth_date(self):
        return Pessoa.this_year - self.idade
    
p1 = Pessoa('Marrom', 5)
p2 = Pessoa('Mozuda', 35)
print(Pessoa.this_year)
print(p1.get_birth_date())
print(p2.get_birth_date())