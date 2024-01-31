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

from pathlib import Path

caminho = Path('c:/Users/rcd_o/Desktop/Projeto//Intermediário/nova pasta atencao')
caminho.mkdir(parents=True, exist_ok=True)

caminho_arquivo = caminho / 'aula54.txt'

print(caminho_arquivo)

'''
arquivo = open(caminho_arquivo, 'w')

arquivo.write('Linha 1\n')
arquivo.write('Linha 2\n')

arquivo.close() # o arquivo sempre tem que ser fechado depois de aberto 
'''

# tambem pode ser feito assim:

'''
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

# Para imprimir o conteudo no terminal

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read()) # imprime o conteudo do arquivo no terminal
'''

# tambem pode ser feito de outra maneira

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines( # escreve varias linhas
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0) # Volta ao inicio do with para fazer a leitura, caso contrario so vai fazer a escrita
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0,0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline()) # sem end ou strip ele vai quebrar 2 linhas
    print(arquivo.readline()) # Funciona como o next, mas sem levantar excecao no final
    # Utilizando o for
    print('readlines com for')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())

print('-' * 50, '1')