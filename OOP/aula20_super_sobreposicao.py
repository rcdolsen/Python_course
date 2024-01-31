# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        print('burlei o sistema')
        super().__init__(*args, **kwargs)

    def metodo(self):
        #super().metodo() # O super e o B (implicito)
        #super(B, self).metodo() # O super e o A (explicito)
        A.metodo(self) # faz o mesmo que o super
        B.metodo(self)
        print('C')

#print(C.mro())

c = C('pinto', 'outro pinto')
print(c.atributo)
print(c.outra_coisa)
#print(c.atributo_a)
#print(c.atributo_b)
#print(c.atributo_c)

c.metodo()