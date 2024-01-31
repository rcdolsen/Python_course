# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

# Código cliente - é o código que usa seu código

#############################
# MEU CODIGO

class Pen:
    def __init__(self, colour):
        #encapsulamento (private, protected, public)
        self.colour = colour

    # Getter (nao quebra o codigo client se eu alterar o self colour no init)
    def get_colour(self):
        print('getter')
        return self.colour
    
##################################
# CODIGO CLIENTE (NORMALMENTE FEITO POR OUTRAS PESSOAS)

pen1 = Pen('Blue')
print(pen1.get_colour())
print('-' * 50)
pen2 = Pen('pink')
print(pen2.get_colour())
print('-' * 50)
pen3 = Pen('Magenta')
print(pen3.get_colour())
print('-' * 50)

...

pen9186478123 = Pen('scarlet violet')
print(pen9186478123.get_colour())
print('-' * 50)

########################################

# METODO PYTHONICO

class Pen2:
    def __init__(self, colour):
        self.tint_colour = colour

    @property
    def colour(self):
        print('Property')
        return self.tint_colour
    
    @property
    def pen_cap(self):
        return 'black'
    
pen = Pen2('yellow')
print(pen.colour)
print('-' * 50)

pen1 = Pen2('blue')
print(pen1.colour)
print('-' * 50)

pen2 = Pen2('white')
print(pen2.colour)
print('-' * 50)

...

pen165742 = Pen2('raspberry')
print(pen165742.colour)
print('-' * 50)

print(pen1.pen_cap)