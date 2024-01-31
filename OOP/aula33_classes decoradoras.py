# Classes decoradoras (Decorator classes)

from typing import Any


class Multiplicar:
    def __init__(self, mult):
        self._mult = mult

    def __call__(self, func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._mult
        return inner

@Multiplicar(2)
def soma(x, y):
    return x + y

sum_mult = soma(2, 4)
print(sum_mult)