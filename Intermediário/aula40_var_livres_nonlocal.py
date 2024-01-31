# Variáveis livres + nonlocal (locals, globals)

def fora(x):
    a = x

    def dentro():
        print(locals())
        print(dentro.__code__.co_freevars)
        return a
    return dentro

dentro1 = fora(2)
dentro2 = fora(45)

print(dentro1())
print(dentro2())
print('--------1')

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        #valor_final += valor_a_concatenar # retorna erro por valor_final ser uma variavel livre definida em outra funcao
        nonlocal valor_final #resolve o problema
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('M')
c('a')
c('r')
c('r')
c('o')
c('m')
print(c())