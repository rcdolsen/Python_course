# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'chamando', self.phone)
        return 'alo mamae'

call1 = CallMe('2345678')
returny = call1('Marrom')
print(returny)