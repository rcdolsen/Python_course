# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def nao_aceito_zero(b):
    if b == 0:
        raise ZeroDivisionError('nao ha divisao por 0')
    return True

def so_aceito_numeros(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser numero. '
            f'"{tipo_n.__name__}" enviado'
        )
    return True

def divide(a, b):
    nao_aceito_zero(b)
    so_aceito_numeros(a)
    so_aceito_numeros(b)
    return a / b

print(divide('sad', 2))