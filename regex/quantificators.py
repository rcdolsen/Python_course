# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

print('1')
# + -> {1,} are the same
print(re.findall(r'JO+ão+', texto, flags=re.I))
print(re.findall(r'JO{1,}ão{1,}', texto, flags=re.I))

print('2')
print(re.sub(r'JO+ão+', 'John', texto, flags=re.I))

print('3')
print(re.findall(r'JO*ão*', texto, flags=re.I))

print('4')
print(re.findall(r'JO?ão?', texto, flags=re.I))

print('5')
print(re.findall(r'JO{5,10}ão+', texto, flags=re.I))
print(re.findall(r've{3,3}m{1,2}', texto, flags=re.I))

print('6')
text2 = 'lov to be loved'
print(re.findall(r'lov[ed]', text2, flags=re.I))
print(re.findall(r'lov[ed]{2}', text2, flags=re.I))
print(re.findall(r'lov[ed]{0,2}', text2, flags=re.I))
print(re.findall(r'lov[ed]{0,1}', text2, flags=re.I))
print(re.findall(r'lov[ed]*', text2, flags=re.I))

print('6')
