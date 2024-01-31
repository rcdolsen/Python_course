# Exemplo de uso de dunder methods (métodos mágicos)
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__ 
        return f'{class_name}(x={self.x!r}, y={self.y!r})'
    
    def __add__(self, other):
        soma_x = self.x + other.x
        soma_y = self.y + other.y
        return Ponto(soma_x, soma_y)
    
    def __gt__(self, other):
        maior_self = self.x + self.y
        maior_other = other.x + other.y
        return maior_self > maior_other

if __name__ == '__main__':
    p1 = Ponto(10, 2)
    p2 = Ponto(100, 200)
    p3 = p1 + p2

    print(p3)
    print('P1 e maior que p2?', p1 > p2)
    print('P2 e maior que p1?', p1 < p2)