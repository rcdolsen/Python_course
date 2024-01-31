# Exercício com classes
# 1 - Crie uma classe canetas (Nome)
# 2 - Crie uma classe tampa (Nome)
# 3 - Crie uma classe cor (Nome)
# 4 - Faça a ligação entre caneta tem uma tampa
# Obs.: Uma tampa pode ser de várias canetas
# 5 - Faça a ligação entre caneta e uma cor
# Obs.: Uma cor pode fabricar várias canetas
# Exiba o nome da caneta, tampa e cor na tela

class Pen:
    def __init__(self, name):
        self.name = name
        self._colour = Colour('sem tinta')
        self._cap = PenCap('sem tampa')

    @property
    def pen_colour(self):
        return self._colour
    
    @pen_colour.setter
    def pen_colour(self, value):
        self._colour = value

    @property
    def pen_cap(self):
        return self._cap
    
    @pen_cap.setter
    def pen_cap(self, value):
        self._cap = value

    def printer(self):
        if self.pen_cap.name == 'sem tampa':
            print(f'Caneta {self.name} {self.pen_colour.name} {self.pen_cap.name}')
        else:
            print(f'Caneta {self.name} {self.pen_colour.name} com tampa {self.pen_cap.name}')

class Colour:
    def __init__(self, name):
        self.name = name

class PenCap:
    def __init__(self, name):
        self.name = name

# Pens
bic = Pen('Bic')
faber = Pen('Faber Castell')
stabilo = Pen('Stabilo')
velha = Pen('velha')

# Colours
black = Colour('preta')
red = Colour('vermelha')
blue = Colour('azul')

# Caps
black_cap = PenCap('preta')
red_cap = PenCap('vermelha')
blue_cap = PenCap('azul')

# Bic
bic.pen_colour = black
bic.pen_cap = black_cap
Pen.printer(bic)

# Faber
faber.pen_colour = blue
faber.pen_cap = blue_cap
faber.printer()

# Stabilo
stabilo.pen_colour = red
stabilo.pen_cap = red_cap
Pen.printer(stabilo)

velha.printer()
