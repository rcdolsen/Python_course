"""
Flag (bandeira) = marcar um local
None = nao valor
is e is not = e ou nao e (tipo, valor, identidade)
id = identidade
"""

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('faca algo')
else:
    print('Nao faca algo')

if passou_no_if is None:
    print('nao passou no if')
else:
    print('passou no if')