#Alanderson quer saber se um endereço IP é válido. Faça um programa para ajudar Alanderson a testar se um endereço é válido.

#Para isso, a entrada deve ser um endereço IP (digitado pelo usuário) e o programa deve escrever na tela se é válido ou não. Um endereço IPv4 é composto por 4 números inteiros entre 0 e 255, separados por um ponto.

#Por exemplo, o endereço 123.123.123.123 é válido, mas 666.123.k.3 não é.

checker = True

l = []

def inputer(number):
    part = input(f'digite o {number}º numero do ip')

    try:
        part_int = int(part)
    except(ValueError):
        return part
    
    return part_int

l = [
    inputer(1),
    inputer(2),
    inputer(3),
    inputer(4),
]

ip = f'{l[0]}.{l[1]}.{l[2]}.{l[3]}'
print(ip)

for i in range(len(l)):
    if type(l[i]) != int or l[i] > 255 or l[i] < 0:
        checker = False
        break

if checker:
    print('O ip e valido')
else:
    print('O ip nao e valido')
