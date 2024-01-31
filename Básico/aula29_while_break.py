"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# condicao = True

# while condicao:
#     nome = input('Qual o seu nome? ')

#     if nome == 'sair' or nome == 'Sair':
#         print('Fim do programa')
#         print(' ')
#         break
    
#     print(f'Seu nome e {nome}')
#     print(' ')

# contador = 4

# while contador <= 10000:
#     print(contador)
#     contador = contador*2

# print('fim')

q_linha = 5
q_col = 5

linha = 1
while linha <= q_linha:
    coluna = 1
    
    while coluna <= q_col:
        print(f'{linha=} {coluna=}') 
        coluna += 1
    linha += 1

print('fim')

