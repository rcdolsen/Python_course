"""
Iterando strings com while
"""

# #       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
# #      1110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

# nova_string += '*L*u*i*z* *O*t*á*v*i*o'

nome = input('Qual o nome:')

letra = 0
palavra = ''

while letra < len(nome):
    palavra += f'*{nome[letra]}'
    letra += 1

print(f"'{palavra}'")