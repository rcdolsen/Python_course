# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

print(not True)
print(not False)

senha = input('Senha: ')

if senha == '123456':
    print('Entrou')
    # Campo vazio e' igual a falso
elif not senha:
    print('Senha nao inserida')
else:
    print('senha incorreta')