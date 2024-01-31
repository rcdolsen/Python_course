# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import asdict, astuple, dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


p1 = Pessoa('Marrom', 'Siqueira')
print(asdict(p1))
print('-' * 49)
print(astuple(p1))
print('-' * 49)
print(asdict(p1).keys())
print(asdict(p1).values())
print(asdict(p1).items())
print('-' * 49)
print(astuple(p1)[0])
print(astuple(p1)[1])
