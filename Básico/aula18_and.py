# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
print(entrada)

senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_permitida == senha_digitada:
    print('Entrar')
elif entrada == 'S':
    print('Sair')

# if entrada == 'E':
#     senha_digitada = input('Senha: ')
#     if senha_digitada == senha_permitida:
#         print('Entrar')
#     else:
#         print('Senha errada')
# elif entrada == 'S':
#     print('Sair')

# Avaliacao de curto cicuito
print(True and True and True)
print(True and False and True)
print(True and 0 and True)