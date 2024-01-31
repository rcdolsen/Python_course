"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

# print('Valor' if True else 'Outro valor')

# condicao = 10 == 10
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito >=9 else 9
print(novo_digito)

print('Valor' if True else 'outro valor' if False else 'Fim')