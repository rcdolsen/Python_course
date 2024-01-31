# Escopo da classe e de métodos da classe

class Animal:
    #nome = 'salsicha'

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def acao(self, alimento='uma mao'):
        return f'{self.nome} esta comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.acao(*args, **kwargs)

salsicha = Animal(nome='Marrom')
print(salsicha.nome)
print(salsicha.executar(alimento='um pe'))