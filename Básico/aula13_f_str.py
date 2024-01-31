nome = 'Marrom Siqueira'
peso = 8.5
alt = 0.5
imc = peso / (alt * alt)

"f-strings"
linha_1 = f'{nome} tem {alt:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu IMC e: {imc:.2f}'
print(linha_1)
print(linha_2)