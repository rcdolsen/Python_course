# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

from exercicio9_modulos import see, redo, undo, erase, add, clear_function, json_save, json_load, file_path

tasks = json_load([file_path])
option = ''

clear_function()

while True:

    print('*' * 10, 'LISTA DE TAREFAS', '*' * 10)
    print()
    print('O que deseja fazer à lista?')
    print()
    print('Adicionar ✅')
    print('Desfazer ⬅')
    print('Restaurar ➡')
    print('Apagar ❌')
    print('Ver 👀')
    print('Sair 🔚')
    print('gravar 💾')
    print()
    option = input().lower()
    print()

    commands = {
        'adicionar': lambda: (add(tasks), see(tasks)),

        'desfazer': lambda: (undo(tasks), see(tasks)),

        'restaurar': lambda: (redo(tasks), see(tasks)),

        'apagar': lambda: (erase(tasks), see(tasks)),

        'ver': lambda: (see(tasks)),

        #'gravar': lambda: (json_save(tasks), print('lista gravada com sucesso'), see(tasks)),
        
        'sair': lambda: (print("Saindo... porta-te bem!"), exit()),
    }

    if commands.get(option) is not None:
        command = commands.get(option)
    else:
        print('digite 1 das opções listadas')
        continue

    command()

    json_save(tasks)