# Funções decoradoras e decoradores com classes
    
def my_repr(cls):
    def reper(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}{class_dict}'
        return class_repr
    cls.__repr__ = reper
    return cls

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return('vc esta em casa')

        return resultado
    return interno

@my_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@my_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
    @meu_planeta
    def falar_nome(self):
        return f'O planeta e {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')


print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())