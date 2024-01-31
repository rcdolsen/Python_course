# Criando arquivos com Python + Context Manager with
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

import os
from pathlib import Path

caminho = Path('c:/Users/rcd_o/Desktop/Projeto//Intermediário/nova pasta atencao')
caminho.mkdir(parents=True, exist_ok=True)

caminho_arquivo = caminho / 'aula54.txt'

print(caminho_arquivo)

'''
with open(caminho_arquivo, 'a') as arquivo: 
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines( # escreve varias linhas
        ('Linha 3\n', 'Linha 4\n')
    )
'''

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines( # escreve varias linhas
        ('Linha 3\n', 'Linha 4\n')
    )

'''
os.unlink(caminho_arquivo) #os.remove faz o mesmo
'''

os.rename(caminho_arquivo, 'aula54.2.txt')