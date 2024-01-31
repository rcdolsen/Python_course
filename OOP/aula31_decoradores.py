# Funções decoradoras e decoradores com classes
    

# Para evitar o uso de heranca
def my_repr(cls):
    def reper(self): # a funcao reper pode ficar fora da funcao my_repr, e indiferente
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}{class_dict}'
        return class_repr
    cls.__repr__ = reper
    return cls

#class ReprMixin:
#    def __repr__(self):
#        class_name = self.__class__.__name__
#        class_dict = self.__dict__
#        class_repr = f'{class_name}{class_dict}'
#        return class_repr
    
@my_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@my_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

#Time = my_repr(Time) fica confuso, nao deve ser feito, usar decoradores ao inves disso
brasil = Time('Brasil')
portugal = Time('Portugal')

#Planeta = my_repr(Planeta)
terra = Planeta('Terra')
marte = Planeta('Marte')


print(brasil)
print(portugal)

print(terra)
print(marte)