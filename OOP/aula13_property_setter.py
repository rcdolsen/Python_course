# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

class Pen:
    def __init__(self, colour):
        # private, protected
        self.colour = colour
        self._colour_cap = None

    @property
    def colour1(self):
        print('Property')
        return self._colour
    
    @colour1.setter
    def colour1(self, value):
        print('estou no setter,', value)
        print('S', '-' * 50)
        self._colour = value

    @property
    def colour_cap(self):
        return self._colour_cap
    
    @colour_cap.setter
    def colour_cap(self, value):
        self._colour_cap = value

    
pen = Pen('Blue')
print(pen.colour)
print('1', '-' * 50)

pen.colour = 'Rosa'
pen.colour_cap = 'Black'
# Getter -> obter valor
print(pen.colour)
print(pen.colour_cap)