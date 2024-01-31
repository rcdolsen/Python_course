# 4 pilares da POO: Abstração, herança, encapsulamento e polimorfismo

#Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso e publico'
        self._protected = 'isso e protegido'
        self.__private = 'isso e privado'

    def metodo_publico(self):
        print(f'{self.__private}, aqui private pode ser usado')
        return 'metodo publico'
    
    def _metodo_protected(self):
        return 'metodo protegido'
    
    def metodo_protected_publico(self):
        return f'{self._metodo_protected()}, aqui posso usar o metodo protegido fora da classe'

f = Foo()
print(f.public)
print('1', '-' * 50)
print(f._protected)
print('2', '-' * 50)
print(f.metodo_publico())
print('3', '-' * 50)
print(f'{f._metodo_protected()}, funciona fora da classe ou subclasse, mas nao deve ser feito')
print('3', '-' * 50)
print(f.metodo_protected_publico())
print('3', '-' * 50)
#print(f.__private) # resulta em erro de atributo por causa do name mangling
print(f'{f._Foo__private}, aqui private nao pode ser usado') # contorna o name mangling, mas n'ao deve ser feito
