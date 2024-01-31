# Problema dos parâmetros mutáveis em funções Python

def add_clients(name, list=[]):
    list.append(name)
    return list

client1 = add_clients('Marrom')
add_clients('theo', client1)
print(client1)

client2 = add_clients('Julian')
add_clients('Julia', client2)
print(client2)
# A lista 2 vai receber a lista 1
print('-' * 50)

# Resolve-se nao criando parametros mutaveis

def add_clients(name, list=None):
    if list is None:
        list = [] # Cria uma lista nova sempre que nao for passada a lista
    list.append(name)
    return list

client1 = add_clients('Marrom')
add_clients('theo', client1)
print(client1)

client2 = add_clients('Julian')
add_clients('Julia', client2)
add_clients('Mozuda', client2)
print(client2)