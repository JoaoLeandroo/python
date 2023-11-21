import numpy as np
from scipy.interpolate import CubicSpline

# Abra o arquivo no modo de leitura
with open('GPS_KRTV.txt', 'r') as arquivo:
    # Ler todas as linhas do arquivo
    linhas = arquivo.readlines()

# Cria uma lista para armazenar os dados
krtv = []

# Itere sobre as linhas, começando da segunda linha (índice 1)
for linha in linhas[1:]:
    # Divida a linha em palavras usando o espaço como delimitador
    partes = linha.split()

    # Converta as partes relevantes para float 
    ano = float(partes[0])
    dado = float(partes[1])

    # Adicione os dados à lista apenas se o ano estiver entre 2010 e 2016 (inclusive)
    if 2010 <= ano <= 2016:
        krtv.append([ano, dado])

    # Para o loop após captar o primeiro dado do ano de 2016
    if ano == 2016:
        break
        

# Abra o arquivo no modo de leitura
with open('GPS_NAUS.txt', 'r') as arquivo:
    # Ler todas as linhas do arquivo
    linhas_naus = arquivo.readlines()

# Cria uma lista para armazenar os dados
naus = []

# Itere sobre as linhas, começando da segunda linha (índice 1)
for linha in linhas_naus[1:]:
    # Divida a linha em palavras usando o espaço como delimitador
    partes = linha.split()

    # Converta as partes relevantes para float 
    ano = float(partes[0])
    dado = float(partes[1])

    # Adicione os dados à lista apenas se o ano estiver entre 2010 e 2016 (inclusive)
    if 2010 <= ano <= 2016:
        naus.append([ano, dado])

    # Para o loop após captar o primeiro dado do ano de 2016
    if ano == 2016:
        break


def interpolar_kubic(dados):
    anos = np.array([item[0] for item in dados])
    valores = np.array([item[1] for item in dados])

    # Criar uma função de interpolação cúbica
    interp_cubica = CubicSpline(anos, valores)

    # Gerar novos anos para interpolação
    novos_anos = np.arange(min(anos), max(anos), (1/365.25)*30)

    # Aplicar a função de interpolação cúbica aos novos anos
    novos_valores = interp_cubica(novos_anos)

    # Criar lista de novos dados
    novos_dados = list(zip(novos_anos, novos_valores))

    return novos_dados

# Aplicar a interpolação cúbica aos seus dados
novos_dados_interpolados_krtv = interpolar_kubic(krtv)
novos_dados_interpolados_naus = interpolar_kubic(naus)

# Exibir os novos dados interpolados
for dado in novos_dados_interpolados_krtv:
    print(dado)

print("------------------------------------------")
for dado in novos_dados_interpolados_naus:
    print(dado)
