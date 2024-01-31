# (Parte1) try e except para tratar exceções
a = 18
b = 0
#c = a / b

try:
    print('try antes')
    c = a / b
    print('try depois')
except ZeroDivisionError as error:
    print('divisao por 0')
    print(error.__class__.__name__)
    print(error)
except (NameError, IndexError) as error:
    print('variavel nao definida ou erro de indice')
    print('ERRO:', error)
    print('nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO')

print('Sem parar')