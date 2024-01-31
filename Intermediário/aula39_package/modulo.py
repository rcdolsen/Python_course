__all__ = [  # Quando se usar import * so o que estiver dentro sera importado
    'variavel',
    'soma_do_modulo',
]

variavel = 'Marrom'

def soma_do_modulo(x, y):
    return x + y


#from modulo2 import fala_oi
# funciona aqui, mas nao funciona no main por ser outro package

# para funcionar no main tem que ser usado o mesmo que seria usado la e para de funcionar aqui

from Aula39_package.modulo2 import fala_oi

#fala_oi()