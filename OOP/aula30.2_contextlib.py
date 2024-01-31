# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula30.txt', 'w', encoding= 'utf8') as arquivo:
#     ...
from contextlib import contextmanager

@contextmanager
def my_open(file_path, mode):
    try:
        print('Abrindo arquivo')
        file = open(file_path, mode, encoding='utf8')
        yield file
    #except Exception as e:
    #    print('Ocorreu erro', e) # O tratamento das excecoes e deixado para o dev que estiver tratando disso
    finally:
        print('Fechando arquivo')
        file.close

with my_open('OOP/aula30.2.txt', 'w') as file:
    file.write('Linha1\n')
    file.write('Linha2\n', 123)
    file.write('Linha3\n')
    print('WITH', file)