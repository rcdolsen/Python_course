# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html

import random

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico

r_range = random.randrange(0, 100, 10)
print(r_range)
print('1', '-' * 40)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"

r_int = random.randint(0, 100)
print(r_int)
print('2', '-' * 40)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"

r_uniform = random.uniform(0, 100)
print(r_uniform)
print('3', '-' * 40)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original

nomes = ['Marrom', 'Theo', 'Muzuda']
random.shuffle(nomes)
print(nomes)
print('4', '-' * 40)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=1)
print(nomes)
print(novos_nomes)
print('5', '-' * 40)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=2)
print(nomes)
print(novos_nomes)
print('5', '-' * 40)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
