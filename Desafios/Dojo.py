#A pessoa na posição do piloto programará por 5 minutos, orientada pela pessoa na posição de copiloto, e ao final deste tempo, o piloto voltará para a plateia, o copiloto será promovido a piloto e uma pessoa da plateia tomará a posição de copiloto.

#plateia -> copiloto -> piloto -> plateia

#Você está responsável pela organização do Coding Dojo de hoje, e, para garantir que todas as pessoas participarão da atividade da forma mais justa possível, você resolveu criar um programa que imprimirá o nome de cada dupla que representará copiloto e piloto em cada rodada.

#Você pegou no Meetup uma lista com N nomes de participantes, a duração do evento é de 2 horas, e cada rodada dura 5 minutos. Caso você chegue ao final da lista e o tempo ainda não tiverem passado as 2h do Coding Dojo, você começará de novo.

n = 13
list_n = []
duration = 120
round_duration = 5
total_time = 0

for i in range(1, n + 1):
    list_n.append(i)

i = 0

while total_time <= duration:
    pilot = list_n[i % n]
    copilot = list_n[(i + 1) % n]
    total_time += round_duration
    i += 1
    if total_time >= duration:
        break

    print(f"Rodada {total_time//round_duration}: Piloto {pilot} - Copiloto {copilot} - Tempo total: {total_time}")