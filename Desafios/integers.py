#Receba uma lista com números inteiros. Verifique se a lista possui números repetidos, caso possua, exclua-os e retorne a lista alterada.

numbers = []
yes_no = ''
x = 0

def insert_number():
    while True:
        number = input('adicione um numero a lista')
        numbers.append(number)
        yes_no = input('deseja adicionar mais numeros? (s) ou (n)').lower()
        if yes_no == 'n':
            break
    return numbers

def repeat_eraser():
    for i in range(len(numbers)):
        x = i

        while True:
            if x == len(numbers) - 1:
                break
            x += 1
            if numbers[i] == numbers[x]:
                numbers.pop(x)
                x -= 1


        if i >= len(numbers) - 1:
            break

    return numbers

print(insert_number())
print(repeat_eraser())