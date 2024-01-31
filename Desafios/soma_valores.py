#Dado 3 valores inteiros lidos do teclado: A, B e C, retorne a soma deles. Porém, caso algum desses valores seja 13, então ele não conta para a soma, e os valores a sua direita também não.

#Por exemplo:
#1, 2, 3 -> 6
#1, 2, 13 -> 3
#1, 13, 3 -> 1
#13, 2, 3 -> 0

letters = 'abc'
imputs = {
}

def imputer():
    num = 0
    for letter in letters:
        num += 1
        while True:
            try:
                number = float(input(f'digite o {num}º de 3 numeros para serem somados'))
                break
            except(ValueError):
                print('digite apenas numeros')

        imputs[letter] = number

#numbers = []

#for key, item in imputs.items():
#    numbers.append(item)

#def sumer():
#    sum = 0
#    for i in numbers:
#        if i != 13:
#            sum += i
#        else:
#            break
#    return sum

# Ou

def sumer():
    sum = 0
    for key, item in imputs.items():
        if item != 13:
            sum += item
        else:
            break
    return f'{sum:.2f}'

imputer()
print(sumer())
