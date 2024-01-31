"""
CONSTANTE = "Variáveis" que não vão mudar (sempre em maiusculas)
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 #velocidade atual do carro
local_carro = 101 #local em km em que o carro esta na estrada

RADAR_1 = 60 #velocidade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #a distancia onde o radar pega

vel_passou_radar1 = velocidade > RADAR_1
dentro_alcance_menor =  local_carro >= (LOCAL_1 - RADAR_RANGE)
dentro_alcance_maior =  local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar1 = vel_passou_radar1 and dentro_alcance_maior and dentro_alcance_menor

if dentro_alcance_maior and dentro_alcance_maior:
    print('carro passou no radar 1')

if vel_passou_radar1:
    print('Velocidade acima do limite')
else:
    print('Velocidade permitida')

if carro_multado_radar1:
    print('carro multado')
elif not carro_multado_radar1 and vel_passou_radar1:
    print('carro fora do alcance do radar')