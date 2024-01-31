"""
Higher Order Functions == Funções que podem receber e/ou retornar outras funções
First-class functions == Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

name = input('Qual o seu nome?')
print(
    executa(saudacao, 'Bom dia', name)
)