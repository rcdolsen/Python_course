# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)
print('--------------1')

pessoa = {
    'nome': 'Marrom',
    'sobrenome': 'Siqueira',
}

a, b = pessoa
print(a, b)
print('--------------2')

a, b = pessoa.values() # Retorna os valores de a e b
print(a, b)
print('--------------3')

a, b = pessoa.items() # Retorna uma tupla com as chaves e os valores
print(a, b)
print('--------------4')

((a1, a2), (b1, b2)) = pessoa.items() # Retorna a chaves na primeira variavel e os valores na segunda
print(a1, a2)
print(b1, b2)
print('--------------5')

for chave, valor in pessoa.items():
    print(valor)
print('--------------6')

pessoa = {
    'nome': 'Marrom',
    'sobrenome': 'Siqueira',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

print(pessoa, dados_pessoa)
print('--------------7')

pessoa_completa = {**pessoa, **dados_pessoa} # desempacota os 2 dicionarios dentro de um novo

print(pessoa_completa)
print('--------------8')

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados) (sempre com 2 **)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NAO NOMEADOS', args)
    print("nomeados''", kwargs)
    
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(1, 2, 'sou o args', nome='Joana', qlq=123)
print('--------------9')

mostro_argumentos_nomeados(**pessoa_completa)# retorna o dicionario desempacotado
print('--------------10')

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)