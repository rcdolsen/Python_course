try:
    print('abrir arquivo')
    #8/0
except IndexError:
    print('erru')
else:
    print('nao deu erro')
finally:
    print('fechar arquivo') # e executado mesmo com erro