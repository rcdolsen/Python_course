import random
import re
import sys

# cria as variaveis
digito_soma = ''
numero = ''
cpf_soma = 0
prim_digito = 0
seg_digito = 0
i = 10

# gera os 9 digitos aleatoriamente
nove_digitos = []
for i in range(9):
    nove_digitos.append(random.randint(0, 9))

# gera novamente se os numeros forem repetidos
if nove_digitos == (nove_digitos[0] * len(nove_digitos)):
    nove_digitos == []
    for i in range(9):
        nove_digitos.append(random.randint(0, 9))

# soma os numeros do CPF
for numero in nove_digitos:
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

for numero in nove_digitos:
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

print(*nove_digitos,prim_digito,seg_digito)
