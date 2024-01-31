

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

print(
    executa(
        lambda x, y: x + y, 2, 3,
    ),
    # lambda x, y, e o mesmo que: def soma(x, y)
    # x + y no lambda e o mesmo que return x+ y
    executa (soma, 2, 3),
    soma(2, 3)
)

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(
        lambda *args: sum(args), 1, 2, 3
    )
)