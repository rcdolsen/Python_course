import json
import os

file_path = 'exercicio9.json'

def json_save(tasks):

    data = tasks
    with open(file_path, 'w', encoding='utf8') as package:
        #package.write('*' * 10 + ' LISTA DE TAREFAS ' + '*' * 10 + '\n')
        data = json.dump(tasks, package, ensure_ascii=False, indent=2)
        return data

def json_load(tasks):
    data = []

    try:
        with open(file_path, 'r', encoding='utf8') as package:
            data = json.load(package)
    except(FileNotFoundError):
        print('A lista esta vazia')
        json_save(tasks)
    return data
            #print(*tasks, sep='\n')