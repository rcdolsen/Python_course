"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nomes):
        return f'{saudacao}, {nomes}!'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')

for nome in ('Marrom', 'Julia', 'Mozuda', 'Julian'):
    print(s1(nome))
    print(s2(nome))