# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('C:', '\\Users', 'rcd_o', 'Desktop', 'FOTOS')
print(caminho)

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho, pasta)
    # print(caminho_completo)
    print(f'{pasta}\n')
    if not os.path.isdir(caminho_completo):
        continue

    for imagem in os.listdir(caminho_completo):
        print('    ', imagem)
