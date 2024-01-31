# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    def __init__(self, nome):
        #self.nome = 'i10' # Hard coded
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta celerando')

hyundai = Carro('i10')
print(hyundai.nome)
hyundai.acelerar()

opel = Carro('corsa')
print(opel.nome)
opel.acelerar()