#As reuniões mais memoráveis do grupy-sanca são, sem dúvidas, os PyBares! Quando finalmente foi decretado o final da pandemia de Covid-19, pythonistas de São Carlos e região se reuniram para comemorar, e a comemoração foi tanta, que neste momento estão com dificuldades de listar quais atividades e eventos são organizados pelo grupo, sem repetirem as já listadas.

#Como programar já é a sua especialidade, você resolveu escrever um programa para sanar este pequeno problema. Seu programa deve ler um número N que determina quantos eventos e atividades foram elencados (que pode ter itens repetidos), e, em seguida, N nomes de atividades e eventos organizados pelo grupy-sanca e imprimir uma lista ordenada alfabeticamente e sem itens repetidos.

#Dica: utilize o operador in para testar se uma entrada já está na lista, e o método sort para ordená-la. Também pode ser útil utilizar o método strip no seu input para evitar que espaços em branco interfiram nas suas comparações.

events = {
    "Palestra sobre Inteligência Artificial": {
        "data": "2023-05-19",
        "hora": "14:00"
        },
    "Workshop de Desenvolvimento Web": {
        "data": "2023-05-20", 
        "hora": "10:30"
        },
    "Conferência de Ciência de Dados": {
        "data": "2023-05-21", 
        "hora": "16:45"
        },
    "Sessão de Networking": {
        "data": "2023-05-22", 
        "hora": "18:00"
        },
    "Hackathon de Programação": {
        "data": "2023-05-23", 
        "hora": "09:00"
        },
    "Curso de Machine Learning": {
        "data": "2023-05-24", 
        "hora": "15:30"
        },
    "Conferência de Ciência deDados": {
        "data": "2023-05-21", 
        "hora": "16:45"
        },
    "Meetup de Python": {
        "data": "2023-05-25", 
        "hora": "19:00"
        },
    "Hackathonde Programação": {
        "data": "2023-05-23", 
        "hora": "09:00"
        },
    "Oficina de Design Thinking": {
        "data": "2023-05-26", 
        "hora": "14:30"
        },
    "Workshopde Desenvolvimento Web": {
        "data": "2023-05-20", 
        "hora": "10:30"
        },
    "Apresentação de Startups": {
        "data": "2023-05-27", 
        "hora": "11:00"
        },
}

stripped = []
n = len(events)
deleted = 0
unique_events = {}

def sorted_events(index, value):
    return sorted(unique_events.items(), key=lambda x: x[index][value])


print(f'Foram elencados {n} eventos', end='\n\n')

for key, value in events.items():
    if key.replace(' ', '') not in stripped:
        stripped.append(key.replace(' ', ''))
        unique_events[key] = events[key]
    else:
        deleted += 1


alphabetical = sorted_events(0, 0)

print(f'Por ordem alfabetica:', end='\n\n')

for key, value in alphabetical:
    print(key, value, sep='\n', end='\n\n')

date = sorted_events(1, 'data')

print(f'Por ordem de data:', end='\n\n')
for key, value in date:
    print(key, value, sep='\n', end='\n\n')

hour = sorted_events(1, 'hora')

print(f'Por ordem de hora:', end='\n\n')
for key, value in hour:
    print(key, value, sep='\n', end='\n\n')

#print(f'Por ordem alfabetica:', sorted_events(0, 0), sep='\n\n', end='\n\n')
#print('Por ordem de data:', sorted_events(1, 'data'), sep='\n\n', end='\n\n')
#print(f'Por ordem de horario:', sorted_events(1, 'hora'), sep='\n\n', end='\n\n')

print(f'foram excluidos {deleted} eventos')

