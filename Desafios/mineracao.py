#D3yver50n resolveu minerar criptomoedas. Ele decidiu minerar Ethereum e viu que 
# 1 ETH = $687,86 e $1 = R$3,59
#. Ele comprou o seguinte computador:

#5 placas de vídeo: GTX1080 TI, cada uma por R$5270,90

#1 placa mãe: ASRock H110 Pro, por R$920

#1 fonte: 1600 W, por R$2299,90

#1 HD: 1 TB, SATA3, 7200 RPM por R$208,90

#2 pentes de memória: 4 GB, DDR4, 2400 MHZ, cada um por R$259,90

#1 CPU: Intel Core i5-8500 por R$899,90

#E resolveu montar usando uma estante de madeira e dois tijolos, para refrigerar melhor:

#Essas GPUs (placas de vídeo) conseguem minerar Ethereum a uma taxa de 27Mh/s
# (mega hash / s = 10⒍hash / s). Cada bloco minerado dá uma recompensa de 3 ETH. Considere a dificuldade da rede de 3.29x10⒖
#, o block time médio de 15.44 s
#.

#Para calcular quantos dólares por segundo ele vai ganhar com esse computador, D3yver50n fez as seguintes contas:
#ETH/s = cluster_ratio x recompensa/block_time
 
#O cluster_ratio é calculado como:
#cluster_ratio = ngpu * GPU_hashrate / network_hashrate
 
#onde ngpu é o número de placas de vídeo que ele tem. O network_hashrate é calculado como:
#network_hashrate = dificuldade / blocktime
 
#Calcule quantos ETH por segundo D3yver50n vai ganhar com esse PC.

#Calcule quantos dólares por segundo ele vai ganhar.

#Calcule quanto ele vai pagar de energia elétrica por segundo para manter esse computador ligado, sabendo que o custo de energia elétrica é de 0.008 centavos/kw

#Após um mês, quantos ETH ele vai ganhar? Isso equivale a quantos reais? Quanto de energia elétrica ele vai gastar? Deu lucro ou prejuízo?

#Se ele teve lucro, após quanto tempo ele ganha o dinheiro que investiu no computador de volta?

ngpu = 5
gpu_hashrate = 27
dificult = 3.29 * (10 ** 15)
block_time = 15.44
reward = 3
energy = 1.6 * 0.008 * 24 * 30

network_hashrate = dificult / block_time

cluster_ratio = ngpu * gpu_hashrate / network_hashrate

eths = cluster_ratio * (reward / block_time)

dolar = eths * 687.86

ethm = eths *60 * 24 * 30

print(f'a) O ganho sera de {eths:.6} ETH por segundo')
print(f'b) O ganho em dolares sera de {dolar:.2} dolares por segundo')
print(f'c) O consumo sera de R${energy:.2}')
print(f'd) O ganho mensal sera de {ethm:.6} ETH, {ethm * 687.86}')
#print(f'e) O ganho sera de {eths:.6} ETH por segundo')