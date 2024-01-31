frase = ' python e uma linguagem de programacao multiparadigma. Python foi criado por Guido van Rossum.'.lower()

i = 0
letra =''
count_letra = 0
count_letra_maior = 0
letra_maior = ''

while i < len(frase):
    letra = frase[i]
    count_letra = frase.count(letra)

    if letra == ' ':
        i += 1
        continue

    if count_letra > count_letra_maior:
        count_letra_maior = count_letra
        letra_maior = letra

    i += 1

print(letra_maior, count_letra_maior)