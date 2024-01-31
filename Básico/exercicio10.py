"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
lista = []
lista_opcao = ('a', 'i', 'l', 's')
indice = ''
nome = ''
opcao_inserida = ''
int_opcao_inserida = ''
opcao = ''
programa = True

import os

# enumera a lista e cria as opcoes do programa
while programa == True:
    lista_enumerada = list(enumerate(lista))
    print('LISTA DE COMPRAS')
    print('Selecione uma opcao:')
    opcao = input('[i]nserir, [a]pagar, [l]istar, [s]air, ----- ').lower()
    print('')

# obriga a digitar apenas as letras aceitas
    if opcao not in lista_opcao:
        os.system('cls')
        print("digite 'i' para inserir, 'a' para apagar, 'l' para listar ou 's' para sair")
        print('')
        continue

# insere valores na lista
    os.system('cls')
    while opcao == 'i':
        opcao_inserida = input('digite o item que quer inserir ou "fim" para terminar: ')

        if opcao_inserida.lower() == 'fim':
            os.system('cls')
            break

        os.system('cls')
        print(opcao_inserida, 'inserido com sucesso')
        print('')
        lista.append(opcao_inserida)
        continue

    # apaga valores da lista
    if opcao == 'a':
        try:
            os.system('cls')
            opcao_inserida = input('digite o indice que quer apagar: ')
            int_opcao_inserida = int(opcao_inserida)
            del lista[int_opcao_inserida]
            os.system('cls')
            print(opcao_inserida, 'apagado com sucesso')
            print('')
        except:
            os.system('cls')
            print('o indice', opcao_inserida, 'nao existe')
            print('')
        continue

    # lista os itens inseridos
    if opcao == 'l':
        os.system('cls')
        print('estes sao os itens da lista:')
        print('')
        for indice, nome in lista_enumerada:
            print(indice, nome)
        print('')
        continue

    # encerra o programa
    if opcao == 's':
        os.system('cls')
        print('Voce saiu com sucesso')
        break