# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}, se for um '{}' vazio, sera um dict
s1 = {}
print(type(s1))

s1 = {1, 2, 3}
print(type(s1))

s1 = set()
print(type(s1))

s1 = set('marrom')
print(s1) # Nao garante a ordem

s1 = {'marrom', 1, 2, 3}
print(s1)
#s1 = set()  # vazio
#s1 = {'Luiz', 1, 2, 3}  # com dados