import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import pchip
from scipy.stats import pearsonr

# criação de Data Frames para cada uma das estações
dados_def_naus = pd.read_csv('NAUS.txt', sep=" ", header = None) # Data Frame bruto de NAUS
dados_def_antc = pd.read_csv('ANTC.txt', sep=" ", header = None) # Data Frame bruto de ANTC
dados_def_p377 = pd.read_csv('P377.txt', sep=" ", header = None) # Data Frame

# seleção dos dados brutos de NAUS para valores maiores ou iguais a 2010.0:
dados_def_naus = dados_def_naus[dados_def_naus[2]>=2010.0]
dados_def_naus = dados_def_naus[dados_def_naus[2] <= 2018.0]
dados_def_antc = dados_def_antc[dados_def_antc[2]>=2010.0]
dados_def_antc = dados_def_antc[dados_def_antc[2] <= 2018.0]
dados_def_p377 = dados_def_p377[dados_def_p377[2]>=2010.0]
dados_def_p377 = dados_def_p377[dados_def_p377[2] <= 2018.0]


# fatiamento dos vetores
NAUS_TEMPO = dados_def_naus[2] # seleciona somente a coluna tempo de NAUS
naus_xyz = dados_def_naus[[2,3,4,5]] # seleciona somente tempo e coordenadas XYZ para a estação NAUS

ANTC_TEMPO = dados_def_antc[2] # seleciona somente tempo para a estação ANTC
antc_xyz = dados_def_antc[[2,3,4,5]] # seleciona somente tempo e coordenadas XYZ para a estação ANTC

P377_TEMPO = dados_def_p377[2] # seleciona somente tempo para a estação P377
p377_xyz = dados_def_p377[[2,3,4,5]] # seleciona somente tempo e coordenadas XYZ para a estação P377

# Fatiamento dos dados em listas separadas, caso seja necessário
# para NAUS
# para NAUS
tempo_naus = naus_xyz.iloc[:, [0]]
coordenada_x_naus = naus_xyz.iloc[:, [1]]
coordenada_y_naus = naus_xyz.iloc[:, [2]]
coordenada_z_naus = naus_xyz.iloc[:, [3]]

tempos_naus = tempo_naus.values.tolist()  # lista com os valores de tempo para NAUS
valores_x_naus = coordenada_x_naus.values.tolist()  # lista com os valores de x para NAUS
valores_y_naus = coordenada_y_naus.values.tolist()  # lista com os valores de y para NAUS
valores_z_naus = coordenada_z_naus.values.tolist()  # lista com os valores de z para NAUS

# para ANTC
tempo_antc = antc_xyz.iloc[:, [0]]
coordenada_x_antc = antc_xyz.iloc[:, [1]]
coordenada_y_antc = antc_xyz.iloc[:, [2]]
coordenada_z_antc = antc_xyz.iloc[:, [3]]

tempos_antc = tempo_antc.values.tolist()  # lista com os valores de tempo para ANTC
valores_x_antc = coordenada_x_antc.values.tolist()  # lista com os valores de x para ANTC
valores_y_antc = coordenada_y_antc.values.tolist()  # lista com os valores de y para ANTC
valores_z_antc = coordenada_z_antc.values.tolist()  # lista com os valores de z para ANTC

# para P377
tempo_p377 = p377_xyz.iloc[:, [0]]
coordenada_x_p377 = p377_xyz.iloc[:, [1]]
coordenada_y_p377 = p377_xyz.iloc[:, [2]]
coordenada_z_p377 = p377_xyz.iloc[:, [3]]

tempos_p377 = tempo_p377.values.tolist()  # lista com os valores de tempo para P377
valores_x_p377 = coordenada_x_p377.values.tolist()  # lista com os valores de x para P377
valores_y_p377 = coordenada_y_p377.values.tolist()  # lista com os valores de y para P377
valores_z_p377 = coordenada_z_p377.values.tolist()  # lista com os valores de z para P377

# cálculo das coordenadas geodésicas ϕ, λ, h a partir das cartesianas X, Y, Z
#Método Direto

a = 6378137 
f = 1/298.257222101 
b = a-(a*f)
e2 = (a**2-b**2)/a**2
e2_linha = (a**2-b**2)/b**2

def calcular_distancia(x, y):
    distancia = math.sqrt(x**2 + y**2)
    return distancia

def calcular_longitude(x, y):
    longitude_resultante = math.atan(y / x)
    return longitude_resultante

def calcular_teta(x, y, z):
    teta_resultante = math.atan((z * a) / (calcular_distancia(x, y) * b))
    return teta_resultante

def calcular_latitude(x, y, z):
    termo_numerador = z + e2_linha * b * (math.sin(calcular_teta(x, y, z))**3)
    termo_denominador = calcular_distancia(x, y) - e2 * a * (math.cos(calcular_teta(x, y, z))**3)
    latitude_resultante = math.atan(termo_numerador / termo_denominador)
    return latitude_resultante

def calcular_N(x, y, z):
    N_resultante = a / math.sqrt(1 - (e2 * (math.sin(calcular_latitude(x, y, z))**2)))
    return N_resultante

def calcular_altitude(x, y, z):
    altitude_resultante = calcular_distancia(x, y) / math.cos(calcular_latitude(x, y, z)) - calcular_N(x, y, z)
    return altitude_resultante

# Recuperação das coordenadas Geodésicas das estações
# cálculo das coordenadas geodésicas para TODAS as observações das estações
coordenadas_NAUS = dados_def_naus[[3, 4, 5]]  # seleciona todas as coordenadas XYZ para a estação NAUS
coordenadas_ANTC = dados_def_antc[[3, 4, 5]]  # seleciona todas as coordenadas XYZ para a estação ANTC
coordenadas_P377 = dados_def_p377[[3, 4, 5]]  # seleciona todas as coordenadas XYZ para a estação P377

# coordenadas de TODAS as observações em NAUS separadas
coordenadas_NAUS_X = coordenadas_NAUS.iloc[:, [0]]
coordenadas_NAUS_Y = coordenadas_NAUS.iloc[:, [1]]
coordenadas_NAUS_Z = coordenadas_NAUS.iloc[:, [2]]

array_NAUS_X = np.asarray(coordenadas_NAUS_X)  # array somente com os valores de x para NAUS
array_NAUS_Y = np.asarray(coordenadas_NAUS_Y)  # array somente com os valores de y para NAUS
array_NAUS_Z = np.asarray(coordenadas_NAUS_Z)  # array somente com os valores de z para NAUS

# cálculo das latitudes geodésicas para todos os pontos da estação NAUS
latitudes_NAUS = []
for x, y, z in zip(array_NAUS_X, array_NAUS_Y, array_NAUS_Z):
    latitude_NAUS = calcular_latitude(x, y, z)
    latitudes_NAUS.append(latitude_NAUS)

# cálculo das longitudes geodésicas para todos os pontos da estação NAUS
longitudes_NAUS = []
for x, y in zip(array_NAUS_X, array_NAUS_Y):
    longitude_NAUS = calcular_longitude(x, y)
    longitudes_NAUS.append(longitude_NAUS)

# cálculo das altitudes geodésicas para todos os pontos da estação NAUS
altitudes_NAUS = []
for x, y, z in zip(array_NAUS_X, array_NAUS_Y, array_NAUS_Z):
    altitude_NAUS = calcular_altitude(x, y, z)
    altitudes_NAUS.append(altitude_NAUS)

# coordenadas de todas as observações em ANTC separadas
antc_X = coordenadas_ANTC.iloc[:, [0]]
antc_Y = coordenadas_ANTC.iloc[:, [1]]
antc_Z = coordenadas_ANTC.iloc[:, [2]]

array_antc_X = np.asarray(antc_X)  # array somente com os valores de x para ANTC
array_antc_Y = np.asarray(antc_Y)  # array somente com os valores de y para ANTC
array_antc_Z = np.asarray(antc_Z)  # array somente com os valores de z para ANTC

# cálculo das latitudes geodésicas para todos os pontos da estação ANTC
latitudes_ANTC = []
for x, y, z in zip(array_antc_X, array_antc_Y, array_antc_Z):
    latitude_ANTC = calcular_latitude(x, y, z)
    latitudes_ANTC.append(latitude_ANTC)

# cálculo das longitudes geodésicas para todos os pontos da estação ANTC
longitudes_ANTC = []
for x, y in zip(array_antc_X, array_antc_Y):
    longitude_ANTC = calcular_longitude(x, y)
    longitudes_ANTC.append(longitude_ANTC)

# cálculo das altitudes geodésicas para todos os pontos da estação ANTC
altitudes_ANTC = []
for x, y, z in zip(array_antc_X, array_antc_Y, array_antc_Z):
    altitude_ANTC = calcular_altitude(x, y, z)
    altitudes_ANTC.append(altitude_ANTC)

# coordenadas de todas as observações em P377 separadas
P377_X = coordenadas_P377.iloc[:, [0]]
P377_Y = coordenadas_P377.iloc[:, [1]]
P377_Z = coordenadas_P377.iloc[:, [2]]

array_P377_X = np.asarray(P377_X)  # array somente com os valores de x para P377
array_P377_Y = np.asarray(P377_Y)  # array somente com os valores de y para P377
array_P377_Z = np.asarray(P377_Z)  # array somente com os valores de z para P377

# cálculo das latitudes geodésicas para todos os pontos da estação P377
latitudes_P377 = []
for x, y, z in zip(array_P377_X, array_P377_Y, array_P377_Z):
    latitude_P377 = calcular_latitude(x, y, z)
    latitudes_P377.append(latitude_P377)

# cálculo das longitudes geodésicas para todos os pontos da estação P377
longitudes_P377 = []
for x, y in zip(array_P377_X, array_P377_Y):
    longitude_P377 = calcular_longitude(x, y) - math.pi
    longitudes_P377.append(longitude_P377)

# cálculo das altitudes geodésicas para todos os pontos da estação P377
altitudes_P377 = []
for x, y, z in zip(array_P377_X, array_P377_Y, array_P377_Z):
    altitude_P377 = calcular_altitude(x, y, z)
    altitudes_P377.append(altitude_P377)

# Separação de XYZ e do tempo em arrays do NumPy para cada estação
# para NAUS
naus_x = np.asarray(valores_x_naus)  # array somente com os valores de x para NAUS de 2010.0 a 2018.0
naus_y = np.asarray(valores_y_naus)  # array somente com os valores de y para NAUS de 2010.0 a 2018.0
naus_z = np.asarray(valores_z_naus)  # array somente com os valores de z para NAUS de 2010.0 a 2018.0
naus_d = np.asarray(tempo_naus)  # array somente com os valores de tempo para NAUS de 2010.0 a 2018.0

# para ANTC
antc_d = np.asarray(tempo_antc)  # array somente com os valores de tempo para ANTC de 2010.0 a 2018.0
antc_x = np.asarray(valores_x_antc)  # array somente com os valores de x para ANTC de 2010.0 a 2018.0
antc_y = np.asarray(valores_y_antc)  # array somente com os valores de y para ANTC de 2010.0 a 2018.0
antc_z = np.asarray(valores_z_antc)  # array somente com os valores de z para ANTC de 2010.0 a 2018.0

# para P377
p377_d = np.asarray(tempo_p377)  # array somente com os valores de tempo para P377 de 2010.0 a 2018.0
p377_x = np.asarray(valores_x_p377)  # array somente com os valores de x para P377 de 2010.0 a 2018.0
p377_y = np.asarray(valores_y_p377)  # array somente com os valores de y para P377 de 2010.0 a 2018.0
p377_z = np.asarray(valores_z_p377)  # array somente com os valores de z para P377 de 2010.0 a 2018.0

# altitudes geométricas h das estações de 2010.0 a 2018.0

# para NAUS
naus_h = []  # vetor com as altitudes geométricas para NAUS de 2010.0 a 2018.0
for x, y, z in zip(naus_x, naus_y, naus_z):
    naus_h.append(calcular_altitude(x, y, z))

# para ANTC
antc_h = []  # vetor com as altitudes geométricas para ANTC de 2010.0 a 2018.0
for x, y, z in zip(antc_x, antc_y, antc_z):
    antc_h.append(calcular_altitude(x, y, z))

# para P377
p377_h = []  # vetor com as altitudes geométricas para P377 de 2010.0 a 2018.0
for x, y, z in zip(p377_x, p377_y, p377_z):
    p377_h.append(calcular_altitude(x, y, z))

print('As séries da componente h no periodo 2010.0-2018.0 estão armazenadas nos vetores naush, antch, e p377h ')
print()
# imprime os gráficos das séries brutas de 2010.0 a 2018.0
plt.figure(figsize=(15, 5))
plt.scatter(naus_d, naus_h, label='observações h de 2010.0 a 2018.0 brutos', color='green')
plt.xlabel('Tempo')
plt.ylabel('h (m)')
plt.legend(bbox_to_anchor = (1, -0.1))
plt.title('NAUS')
plt.show()

plt.figure(figsize=(15, 5))
plt.scatter(antc_d, antc_h, label='observações h de 2010.0 a 2018.0 brutos', color='blue')
plt.xlabel('Tempo')
plt.ylabel('h (m)')
plt.legend(bbox_to_anchor = (1, -0.1))
plt.title('ANTC')
plt.show()

plt.figure(figsize=(15, 5))
plt.scatter(p377_d, p377_h, label='observações h de 2010.0 a 2018.0 brutos', color='purple')
plt.xlabel('Tempo')
plt.ylabel('h (m)')
plt.legend(bbox_to_anchor = (1, -0.1))
plt.title('P377')
plt.show()