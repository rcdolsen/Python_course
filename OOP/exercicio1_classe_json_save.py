# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

FILE_PATH = 'OOP\exercicio1.json'


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = People('Marrom', 5)

p2 = People('Theo', 0)

bd = (vars(p1), p2.__dict__)  # tanto faz vars ou __dict__


def save():
    with open(FILE_PATH, 'w', encoding='utf8') as file:
        print('dumping')
        json.dump(bd, file, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('exercicio_save e o main')
    save()
