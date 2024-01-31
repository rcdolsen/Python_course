# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_enderecos(self, rua, numero='S/N'):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('apagando, ', self.nome) 

class Endereco:
    def __init__(self, rua, numero='S/N'):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('apagando, ', self.rua, self.numero) 

cliente1 = Cliente('Marrom')
cliente1.inserir_enderecos('Av Alberto Sampaio', 1090)
cliente1.inserir_enderecos('Rua Belize')
endereco_externo = Endereco('abc', 123)
cliente1.inserir_endereco_externo(endereco_externo)

cliente1.listar_endereco()

del cliente1

print(f'{"-" * 15} Fim do codigo {"-" * 15}')