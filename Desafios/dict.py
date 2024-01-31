#Faça um dicionário com as 5 pessoas mais perto de você, tendo o nome como chave e a cor da camisa que está usando como valor.

people = dict(marrom = 'pelado', theo = 'bolsa', mozuda = 'roupa do trabalho')
print(people)

#Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).

week = {}
week['segunda'] = 'python'
week['terca'] = 'python'
week['quarta'] = 'python'
week['quinta'] = 'python'
week['sexta'] = 'python'
week['sabado'] = ''
week['domingo'] = ''
print(week)

#Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi lançado. Preencha 5 filmes.

movies = dict()
movies['tlotr'] = {'Sauron', 2001}
print(movies)


mes = int(input('qual o mes'))