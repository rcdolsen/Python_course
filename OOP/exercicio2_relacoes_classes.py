# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

i = 0

class Car:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._fabricator = None

    @property
    def car_motor(self):
        return self._motor
    
    @car_motor.setter
    def car_motor(self, valor):
        self._motor = valor
    
    @property
    def car_fabricator(self):
        return self._motor
    
    @car_fabricator.setter
    def car_fabricator(self, valor):
        self._fabricator = valor
    
    def printer(self):
        global i
        i += 1
        print(f'carro {i}:')
        print('Nome:', self.name)
        print('Fabricante:', self.car_fabricator.name)
        print('Motor:', self.car_motor.name)
        print()

class Motor:
    def __init__(self, name):
        self.name = name
    
class Fabricator:
    def __init__(self, name):
        self.name = name
    

# Carros
i10 = Car('I10')
yaris = Car('yaris')
clio = Car('clio')
i30 = Car('i30')

# Motores
hyundai_motor = Motor('Hyundai')
toyota_motor = Motor('Toyota')
renault_motor = Motor('Renault')

# Fabricantes
hyundai_fabricator = Fabricator('Hyundai')
toyota_fabricator = Fabricator('Toyota')
renault_fabricator = Fabricator('Renault')

i10.car_fabricator = hyundai_fabricator
i10.car_motor = hyundai_motor

yaris.car_fabricator = toyota_fabricator
yaris.car_motor = toyota_motor

clio.car_fabricator = renault_fabricator
clio.car_motor = renault_motor

i30.car_fabricator = hyundai_fabricator
i30.car_motor = hyundai_motor

i10.printer()
yaris.printer()
clio.printer()
i30.printer()
