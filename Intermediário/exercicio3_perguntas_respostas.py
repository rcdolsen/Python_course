# Exercício - sistema de perguntas e respostas

# Define as variaveis
letter = ['A)', 'B)', 'C)', 'D)']
i = 0
right_letter = ''
user_answer = ''
score = 0

# Cria as perguntas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# Seleciona o dict dentro da lista e mostra as perguntas ao usuario
for question in perguntas:
    print(question['Pergunta'])
    i = 0

# Mostra as alternativas ao usuario
    for i, option in enumerate(question['Opções']):
        print(letter[i], option)

        # Define a letra da resposta certa
        if option == question['Resposta']:
            right_letter = (letter[i].replace(')', ''))

    # pergunta a resposta certa ao usuario
    user_answer = input('qual a resposta correta? 👆')

    # Da o feeback sobre a resposta do usuario
    if user_answer == question['Resposta'] or user_answer.upper().replace(' ', '') == right_letter:
        print('parabens, vc acertou, nao fez mais que a obrigacao!!!! 😎')
        score += 1
    elif user_answer == '':
        print('nao sabe ne? 🤦‍♂️')
    else:
        print('que burrice!!! 🤡')
    print('')

# Mostra a pontuacao
print(f'vc acertou {score} de {len(perguntas)} questoes')
print('')