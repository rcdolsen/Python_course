# cria o cpf e as variaveis
cpf = input('Qual o cpf a ser analisado? deve ter 9 numeros ')
cpf_lista = list(cpf)
cpf_numero = []
digito_soma = ''
numero = ''
cpf_soma = 0
prim_digito = 0
seg_digito = 0
i = 10

# separa os numeros do cpf

# 1 forma: .isdigit()
    # for numero in cpf_lista:
    #     if numero.isdigit():
    #         cpf_numero.append(numero)

#2 forma: .replace( , )
    # a str e imutavel, so pode ser usado o replace assim que for criada
    # cpf_numero = cpf.replace('.', '') \
    #     .replace('-', '') \
    #     .replace(' ', '')

#3 forma: re.sub(r'', , )
import re
cpf_numero = re.sub(r'[^0-9]', # substitui tudo que nao e um inteiro de 0 a 9
 '', cpf)

# impede o envio de numeros repetidos
import sys

if cpf == '' or cpf_numero == (cpf[0] * len(cpf_numero)) or len(cpf_numero) != 9:
    print('O CPF', cpf, 'nao e valido')
    sys.exit()

# soma os numeros do CPF
for numero in cpf_numero:
    digito_soma = int(numero) * i
    cpf_soma += digito_soma
    i -= 1
    if i == 1:
        break

# trabalha a soma e informa o primeiro digito
cpf_soma = cpf_soma * 10
cpf_soma = cpf_soma % 11

prim_digito = 0 if cpf_soma > 9 else cpf_soma
print('o primeiro digito do cpf e', prim_digito)

# reseta o indice e a soma, e soma os numeros do CPF
i = 11
cpf_soma = 0

for numero in cpf_numero:
    digito_soma = int(numero) * i
    cpf_soma += digito_soma
    i -= 1
    if i == 2:
        break

cpf_soma += prim_digito * 2

# trabalha a soma e informa o segundo digito
cpf_soma = cpf_soma * 10
cpf_soma = cpf_soma % 11

seg_digito = 0 if cpf_soma > 9 else cpf_soma
print('o segundo digito do cpf e', seg_digito)

# retorna se o CPF e valido
for n, numero in enumerate(cpf_numero):
    ...
if int(cpf_numero[9]) == prim_digito and int(cpf_numero[10]) == seg_digito:
    print('O CPF', cpf, 'e valido')
else:
    print('O CPF', cpf, 'nao e valido')
