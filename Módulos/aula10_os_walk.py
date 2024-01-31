# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('C:', '\\Users', 'rcd_o', 'Desktop', 'FOTOS')
count_ = count()

for root, dirs, files in os.walk(caminho):
    counter = next(count_)
    print(counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('    ', counter, 'Dir:', root)

    for file_ in files:
        print('    ', counter, 'File:', file_)

        # os.unlink(caminho_completo) #NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
