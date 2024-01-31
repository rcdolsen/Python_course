from dataclasses import dataclass


# @dataclass(frozen=True) # you can't change the attributes or characteristics
# of an object after it's initialised
# @dataclass(repr=True, order=True)
@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'Z')]
    print(sorted(lista, reverse=False, key=lambda p: p.nome))
    print(sorted(lista, reverse=False, key=lambda p: p.sobrenome))
