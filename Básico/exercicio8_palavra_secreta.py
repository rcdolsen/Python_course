"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

guess = ''
checagem = ''
letras_certas = ''
letras_erradas = ''
palavra = 'bico'
palavra_oculta = ''
tentativas = 0

print('Jogo da forca')

while True:
    palavra_oculta = ''

    # insere uma letra
    guess = input('digite uma letra para adivinhar a palavra: ')
    print('')

    # obriga a inserir apenas 1 letra
    while len(guess) != 1 or ' ' in guess:
        print('')
        guess = input('digite apenas 1 letra: ')

    # altera o numero de tentativas e regista as letras acertadas

    tentativas += 1

    if guess in letras_certas or guess in letras_erradas:
        print('essa letra ja foi usada')
        print('')
        continue
    if guess in palavra:
        letras_certas += guess
    else:
        letras_erradas += guess

    # Checa se a letra esta na palavra
    for checagem in palavra:
        if checagem in letras_certas:
            palavra_oculta += checagem
        else:
            palavra_oculta += '*'
    print('letras erradas: ', letras_erradas)
    print('')
    print('letras certas: ', letras_certas)
    print('')
    print('palavra secreta: ', palavra_oculta)
    print('')

    # Encerra o jogo e reinicia as variaveis se acertar a palavra
    if palavra_oculta == palavra:
        os.system('cls')
        print('Vc acertou a palavra, PARABENS POR PERDER SEU TEMPO')
        print('a palavra era: ', palavra)
        print('conseguiu em', tentativas, 'tentativas')
        
        tentativas = 0
        letras_certas = ''
        letras_erradas = ''
        
        input('digite qualquer coisa para reiniciar ')
        os.system('cls')
