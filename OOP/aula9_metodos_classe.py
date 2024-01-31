# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.



class People:
    year = 2023 # atributo de classe

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def class_method(cls):
        print('Hey')

    @classmethod
    def create_with_50(cls, name):
        return cls(name, 50)

    @classmethod
    def create_no_name(cls, age):
        return cls('Anonymous', age)
    
    @classmethod
    def create_no_name_with_50(cls):
        return cls('Anonymous', 50)

p1 = People('Marrom', 5)
print(People.year)
p1.class_method()
People.class_method()

print('1', '-' * 50)

p2 = People.create_with_50('Mozuda')
print(p2.name, p2.age)

print('2', '-' * 50)

p3 = People.create_no_name(23)
print(p3.name, p3.age)

print('3', '-' * 50)

p4 = People.create_no_name_with_50()
print(p4.name, p4.age)
