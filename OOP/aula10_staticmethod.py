# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classy:

    @staticmethod
    def Function_in_the_class(*args, **kwargs):
        print('Hi', args, kwargs)

def function(*args, **kwargs):
    print('Hi', args, kwargs)

c1 = Classy()

c1.Function_in_the_class(1, 2, 3, 'funcao classe')

function(1, 2, 3, 'funcao')

Classy.Function_in_the_class(funcao_classe=1)

function(funcao=1)