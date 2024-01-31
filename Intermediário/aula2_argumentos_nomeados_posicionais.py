"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado (posicional) recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    # definicao
    print(f'{x=} y={y} {z=}', '|', 'x + y + z =', x + y + z) # {x=} e o mesmo que x={x}]
    

#print(soma)
#print('-----------------------------')
#print(soma(1, 2)) # redundante
#print('------------------------------')

soma(1, 2, 3) # nao nomeado (posicional)
soma(y = 2, x = 1, z = 3) # nomeado (fora de ordem)

print(1, 2, 3, sep ='-')