#Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva uma função que dado duas palavras, retorne True caso sejam.

word_1 = 'ovo'
word_2 = 'carro'

def inverse(word):
    word_inv = word[::-1]
    if word_inv == word:
        return True
    return False

def printer(word):
    if inverse(word):
        return print(f'a palavra {word} e um par inverso')
    else:
        return print(f'a palavra {word} nao e um par inverso')

printer(word_1)
printer(word_2)