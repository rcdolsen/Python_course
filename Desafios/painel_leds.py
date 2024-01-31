#João quer montar um painel de LEDs contendo diversos números. Ele não possui muitos LEDs, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos LEDs dos números, faça um algoritmo que ajude João a descobrir a quantidade de LEDs necessário para montar o valor.

#1234567890
#Exemplos de entrada e saída:

#115380 —> 27

#2819311 —> 29

#23456 —> 25

#000 —> 18

leds = {
        '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
        '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}
numbers = ['1234567890', '115380', '2819311', '23456', '000']

def led_count(leds, numbers):
    total = 0

    for number in numbers:
        for key, value in leds.items():
            if key == number:
                total += value
                break
    return total

for number in numbers:
    print(led_count(leds, number))


