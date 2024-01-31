from pathlib import Path

# from shutil import rmtree

# PATH_PROJECT = Path()
# print(PATH_PROJECT.absolute())
# print('1', '-' * 40)

# PATH_FILE = Path(__file__)
# print(PATH_FILE)
# print('2', '-' * 40)

# print(PATH_FILE.parent)
# print('3', '-' * 40)

# print(PATH_FILE.parent.parent)
# print('4', '-' * 40)

# ideas = PATH_FILE / 'ideas'
# print(ideas / 'arquivo.txt')
# print('5', '-' * 40)

# print(Path.home() / 'Desktop')
# print('6', '-' * 40)

# arquivo = Path.home() / 'Desktop' / 'Arquivo.txt'
# arquivo.touch()  # Cria o arquivo
# print(arquivo)
# arquivo.write_text('Hello World')
# arquivo.write_text('Hello again')  # Sobreescreve o anterior
# print(arquivo.read_text())
# # arquivo.unlink()  # Apaga o arquivo
# print('7', '-' * 40)

# arquivo.write_text('')
# with arquivo.open('a+') as file:
#     file.write('Uma linha\n')
#     file.write('outra linha')
# print(arquivo.read_text())
# print('8', '-' * 40)

FOLDER_PATH = Path.home() / 'Desktop' / 'Python e legal'
FOLDER_PATH.mkdir(exist_ok=True)  # Nao levanta excecao se o dir ja existir
subpasta = FOLDER_PATH / 'subpasta'
subpasta.mkdir(exist_ok=True)

another_file = subpasta / 'arquivo.txt'
# another_file.touch()
another_file.write_text('Olar')

mais_arquivo = FOLDER_PATH / 'arquivo.txt'
mais_arquivo.touch()
mais_arquivo.write_text('Olar de novo')

# FOLDER_PATH.rmdir()  # Remove o diretorio somente se estiver vazio

files = FOLDER_PATH / 'Files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Hello World\n')
        text_file.write(f'file_{i}.txt')

# rmtree(FOLDER_PATH)  # Remove o diretorio e todos os subdiretorios


def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE: ', file)
            file.unlink()

    if remove_root:
        root.rmdir()


rmtree(FOLDER_PATH)
