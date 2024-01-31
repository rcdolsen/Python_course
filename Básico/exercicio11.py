"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

# cria o cpf e as variaveis
cpf = input('Qual o cpf a ser analisado? deve ter 11 numeros ')
cpf_lista = list(cpf)
cpf_numero = []
digito_soma = ''
numero = ''
cpf_soma = 0
prim_digito = 0
seg_digito = 0
i = 10

# separa os numeros do cpf
for numero in cpf_lista:
    if numero.isdigit():
        cpf_numero.append(numero)

# Faz a soma dos numeros do CPF
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

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

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

# cpf_enumerado = list(enumerate(cpf_numero))
for n, numero in enumerate(cpf_numero):
    ...
if int(cpf_numero[9]) == prim_digito and int(cpf_numero[10]) == seg_digito:
    print('O CPF', cpf, 'e valido')
else:
    print('O CPF', cpf, 'nao e valido')
