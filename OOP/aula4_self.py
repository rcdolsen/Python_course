# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

# Self e definido por convencao, pode ser qualquer palavra
class Carro:
    def __init__(abc, nome):
        abc.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta celerando')

hyundai = Carro('i10')
print(hyundai.nome)
hyundai.acelerar()
# Ou
Carro.acelerar(hyundai)

opel = Carro('corsa')
print(opel.nome)
opel.acelerar()
# Ou
Carro.acelerar(opel)
