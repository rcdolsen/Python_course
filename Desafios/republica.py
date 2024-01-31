#Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado e compraram alguns itens:

#75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)

#2 pacotes de macarrão: R$ 8,73 cada

#1 pacote de Molho de tomate: R$ 3,45

#420g Cebola: R$ 5,40/kg

#250g de Alho: R$ 30/kg

#450g de pães franceses: R$ 25/kg

#Calcule quanto ficou para cada um.

d ={
    'cerveja': [75, 2.2],
    'macarrao': [2, 8.73],
    'molho de Tomate': [1, 3.45],
    'cebola': [0.42, 5.4],
    'alho': [0.25, 30],
    'pao': [0.45, 25],
}

cost = 0.0
people = 5
sum = 0.0

def calculator(quant, price):
    total = quant * price

    def printer(item):
        print(f'o gasto total com {item} e: ${total:.2f}')
        return total

    return printer

for item in d:
    cost = calculator(d[item][0], d[item][1])
    sum += cost(item)

print()
print(f'O gasto total sera: ${sum:.2f}, cada um paga: ${sum/5:.2f}')

