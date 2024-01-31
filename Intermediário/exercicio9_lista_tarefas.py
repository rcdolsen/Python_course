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

from exercicio9_modulos import see, redo, undo, erase, add, clear_function, json_save, json_load

tasks = json_load[[]]
opcao = ''
more = ''

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
    opcao = input()
    print()

    if opcao.lower() == 'adicionar':
        add(tasks)
        see(tasks)
        continue

    elif opcao.lower() == 'desfazer':
        undo(tasks)
        see(tasks)
        continue

    elif opcao.lower() == 'restaurar':
        redo(tasks)
        see(tasks)
        continue

    elif opcao.lower() == 'apagar':
        erase(tasks)
        see(tasks)
        continue

    elif opcao.lower() == 'ver':
        see(tasks)
        continue

    elif opcao.lower() == 'gravar':
        json_save(tasks)
        print('lista gravada com sucesso')

    elif opcao.lower() == 'sair':
        print("Saindo... porta-te bem!")
        break

    else:
        print('digite 1 das opções listadas')
        continue