from exercicio9_auxiliary_functions import index_error_function, clear_function

deleted = []
erased = []
sim_nao = ''

def add(list_tasks = None):
    if list_tasks is None:
        list_tasks = []
    
    while True:
        print('digite a tarefa a ser adicionada')
        item = input()
        list_tasks.append(item)
        print()
        print(item, 'foi adicionado')

        print('deseja adicionar mais?')
        print('digite nao ou n para voltar ao menu ou qualquer tecla para continuar adicionando')
        sim_nao = input()
        clear_function()

        if sim_nao.lower() == 'n' or sim_nao.lower() == 'nao':
            break

    return list_tasks

def undo(list_tasks = None):
    if list_tasks is None:
        list_tasks = []

    return index_error_function(list_tasks, deleted, 'removido da', 'desfazer')
    
def redo(list_tasks = None):
    if list_tasks is None:
        list_tasks = []

    return index_error_function(deleted, list_tasks,'restaurado a', 'restaurar')

def erase(list_tasks = None):
    if list_tasks is None:
        list_tasks = []

    print('Quer mesmo apagar para sempre o ultimo item da lista?')
    print()
    sim_nao = input('Digite sim ou s para apagar. Pressione qualquer tecla para manter')
    print()

    if sim_nao.lower() == 's' or sim_nao.lower() == 'sim':
        return index_error_function(list_tasks, erased, 'apagado', 'apagar')
    
    else:
        return print('nenhum item foi apagado')

def see(task):
    if task:
        print()
        print('lista:')
        print()
        print(*task, sep='\n')
        print()
        input('pressione enter para continuar')
        clear_function()
    
    else:
        clear_function()
        print('A lista esta vazia')
        input('pressione enter para continuar')
        clear_function()