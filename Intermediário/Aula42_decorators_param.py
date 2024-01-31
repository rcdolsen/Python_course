# Decoradores com parâmetros
def decorators_factory(a=None, b=None, c=None):
    def functions_factory(func):
        print('decoradora 1')

        def inner(*args, **kwargs):
            print('inner')
            res = func(*args,**kwargs)
            return res
        return inner
    return functions_factory

@decorators_factory(1, 2, 3)
def soma(x, y):
    return x + y

sum = soma(1, 2)
print(sum)

multiplica = decorators_factory()(lambda x, y: x * y)

multiply = multiplica(2, 3)
print(multiply)