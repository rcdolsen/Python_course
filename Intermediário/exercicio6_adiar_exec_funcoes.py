# Exercício - Adiando execução de funções
def soma(x, y):
    print('somado')
    return x + y


def multiplica(x, y):
    print('multiplicado')
    return x * y


def criar_funcao(funcao, x):
    print('funcao criada')
    def delay(y):
        print('funcao executada')
        return (funcao(x, y))
    return delay


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(2))
print(multiplica_por_dez(3))