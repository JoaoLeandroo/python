import pandas as pd
import numpy as np

# Leitura dos dados
def openData(files):
    with open(files, 'r') as file:
        lines = file.readlines()
    
    listDados = []
    for line in lines:
        division_line = line.split()
        listDados.append({
            'id': division_line[0],
            'ano': division_line[1],
            'x': float(division_line[3]),
            'y': float(division_line[4]),
            'z': float(division_line[5])
        })
    return pd.DataFrame(listDados)

dados_naus_origin = openData('NAUS.txt')
dados_antc_origin = openData('ANTC.txt')
dados_p377_origin = openData('P377.txt')

# Parâmetros do elipsoide GRS80(Mritz, 1980)
a = 6378137
b = 6356752.3142
f = 1/298.257222101
e2 = 0.00669438002290
e2_ = 0.00673949677548

# funcoes que serão usadas para as transformações
# Função para calcular a distância radial
def calcular_distancia_radial(x, y):
    return np.sqrt(x**2 + y**2)

# Função para calcular a longitude em radianos
def calcular_longitude(x, y):
    return np.arctan2(y, x)

# Função para calcular o ângulo polar (azimute)
def calcular_angulo_polar(x, y, z):
    return np.arctan2(z * a, calcular_distancia_radial(x, y) * b)

# Função para calcular a latitude em radianos
def calcular_latitude(x, y, z):
    t = calcular_angulo_polar(x, y, z)
    return np.arctan2((z + e2_ * b * (np.sin(t)**3)), (calcular_distancia_radial(x, y) - e2 * a * (np.cos(t)**3)))

# Função para calcular o raio de curvatura da seção vertical
def calcular_raio_curvatura_vertical(x, y, z):
    return a / np.sqrt(1 - (e2 * (np.sin(calcular_latitude(x, y, z))**2)))

# Função para calcular a altitude em relação ao elipsoide GRS80
def calcular_altitude(x, y, z):
    return calcular_distancia_radial(x, y) / np.cos(calcular_latitude(x, y, z)) - calcular_raio_curvatura_vertical(x, y, z)

# Calculando as coordenadas geodésicas de cada estação
coordenada_naus_geo = pd.DataFrame({
    'id': dados_naus_origin['id'],
    'ano': dados_naus_origin['ano'],
    'latitude': np.degrees(calcular_latitude(dados_naus_origin['x'], dados_naus_origin['y'], dados_naus_origin['z'])),
    'longitude': np.degrees(calcular_longitude(dados_naus_origin['x'], dados_naus_origin['y'])),
    'altitude': calcular_altitude(dados_naus_origin['x'], dados_naus_origin['y'], dados_naus_origin['z'])
})

coordenada_antc_geo = pd.DataFrame({
    'id': dados_antc_origin['id'],
    'ano': dados_antc_origin['ano'],
    'latitude': np.degrees(calcular_latitude(dados_antc_origin['x'], dados_antc_origin['y'], dados_antc_origin['z'])),
    'longitude': np.degrees(calcular_longitude(dados_antc_origin['x'], dados_antc_origin['y'])),
    'altitude': calcular_altitude(dados_antc_origin['x'], dados_antc_origin['y'], dados_antc_origin['z'])
})

coordenada_p377_geo = pd.DataFrame({
    'id': dados_p377_origin['id'],
    'ano': dados_p377_origin['ano'],
    'latitude': np.degrees(calcular_latitude(dados_p377_origin['x'], dados_p377_origin['y'], dados_p377_origin['z'])),
    'longitude': np.degrees(calcular_longitude(dados_p377_origin['x'], dados_p377_origin['y'])),
    'altitude': calcular_altitude(dados_p377_origin['x'], dados_p377_origin['y'], dados_p377_origin['z'])
})

# Função para calcular as medias
def calcularMedias(geo):
    num1 = 0
    for i in geo:
        num1 += i
    return num1

naus_latitude = calcularMedias(coordenada_naus_geo.latitude) / len(coordenada_naus_geo)
naus_altitude = calcularMedias(coordenada_naus_geo.altitude) / len(coordenada_naus_geo)
naus_longitude = calcularMedias(coordenada_naus_geo.longitude) / len(coordenada_naus_geo)

antc_latitude = calcularMedias(coordenada_antc_geo.latitude) / len(coordenada_antc_geo)
antc_altitude = calcularMedias(coordenada_antc_geo.altitude) / len(coordenada_antc_geo)
antc_longitude = calcularMedias(coordenada_antc_geo.longitude) / len(coordenada_antc_geo)

p377_latitude = calcularMedias(coordenada_p377_geo.latitude) / len(coordenada_p377_geo)
p377_altitude = calcularMedias(coordenada_p377_geo.altitude) / len(coordenada_p377_geo)
p377_longitude = calcularMedias(coordenada_p377_geo.longitude) / len(coordenada_p377_geo)

print("Média Latitude NAUS:", naus_latitude,'°')
print("Média longitude NAUS:", naus_longitude,'°')
print("Média altitude NAUS:", naus_altitude,'m')

print("Média latitude ANTC:", antc_latitude,'°')
print("Média longitude ANTC:", antc_longitude,'°')
print("Média altitude ANTC:", antc_altitude,'m')

print("Média latitude P377:", p377_latitude,'°')
print("Média longitude P377:", p377_longitude,'°')
print("Média altitude P377:", p377_altitude,'m')
