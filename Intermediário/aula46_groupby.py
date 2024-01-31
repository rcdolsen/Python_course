# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

#alunos = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'a']
#grupos = groupby(alunos) # os dados tem que ser ordenados, senao nao sao corretamente agrupados

##for chave, grupo in grupos:
##    print(chave)
##    print(grupo)

#for chave, grupo in grupos:
#    print(chave)
#    print(list(grupo))

#print('---------1')

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for nota, grupo in grupos:
    print(f'nota: {nota}')
    print()
    for g in grupo:
        print(g['nome'])
    print()