# Exemplo de uso dos sets
letras = set()
tentativas = 0

while True:
    letra = input('Qual o nome certo? ')
    letras.add(letra.lower())
    tentativas += 1

    if 'julian' in letras:
        print(f'bicooooo, vc encontrou o nome certo em {tentativas} tentativas')
        print('eu me remexo muito 🕺')
        print('')
        break
    else:
        print('errou, vc sabe qual e!!!!!')

    print(letras)