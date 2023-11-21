# Abra o arquivo no modo de leitura
with open('GPS_KRTV.txt', 'r') as arquivo:
    # Leia todas as linhas do arquivo
    linhas = arquivo.readlines()

# Crie uma lista para armazenar os dados
krtv = []

print("Dados KRTV")
# Itere sobre as linhas, começando da segunda linha (índice 1)
for linha in linhas[1:]:
    # Divida a linha em palavras usando o espaço como delimitador
    partes = linha.split()

    # Converta as partes relevantes para float e int
    ano = float(partes[0])
    dado = float(partes[1])

    # Adicione os dados à lista apenas se o ano estiver entre 2010 e 2016 (inclusive)
    if 2010 <= ano <= 2016:
        krtv.append([ano, dado])
        print(dado)

    if ano == 2016:
        print("-------------------------------------------------------------------------")
        break
        

# Abra o arquivo no modo de leitura
with open('GPS_NAUS.txt', 'r') as arquivo:
    # Leia todas as linhas do arquivo
    linhas_naus = arquivo.readlines()

# Crie uma lista para armazenar os dados
naus = []

# Itere sobre as linhas, começando da segunda linha (índice 1)
print("Dados NAUS")
for linha in linhas_naus[1:]:
    # Divida a linha em palavras usando o espaço como delimitador
    partes = linha.split()

    # Converta as partes relevantes para float
    ano = float(partes[0])
    dado = float(partes[1])

    # foi adicionado os dados à lista apenas se o ano estiver entre 2010 e 2016
    if 2010 <= ano <= 2016:
        naus.append([ano, dado])
        print(dado)

    if ano == 2016:
        break