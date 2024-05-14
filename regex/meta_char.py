# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
print('1')

print(re.findall(r'João|Maria|adultos', texto))

print('2')

print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'[Jj]oão|[Mfsdac]aria', texto))

print('3')

print(re.findall(r'João|Maria|ad.....', texto))

print('4')
# [a-z] -> between a and z
print(re.findall(r'[a-z]aria', texto))
print(re.findall(r'[a-zA-Z]aria', texto))

print('5')
print(re.findall(r'[0-9]', texto))

print('6')
# I and IGNORECASE are the same
print(re.findall(r'JOãO|MaRIa', texto, flags=re.I))
print(re.findall(r'JOãO|MaRIa', texto, flags=re.IGNORECASE))
