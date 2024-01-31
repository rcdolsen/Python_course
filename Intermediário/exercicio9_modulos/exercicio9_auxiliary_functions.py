import os

def clear_function():
    return os.system('cls')

def index_error_function(to_remove, to_apend, message_1, message_2):
    try:
        print(to_remove[-1], 'Foi', message_1 ,'lista')
        print()
        
        return to_apend.append(to_remove.pop())
    
    except(IndexError):
        print('nao ha mais nada a', message_2)
        print()