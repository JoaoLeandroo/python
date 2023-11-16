import matplotlib.pyplot as plt

# Dados fornecidos
sst = [
    [1995, -1.06216], [1996, -1.99387], [1997, -0.75158], [1998, 0.0559], [1999, -1.2485], [2000, -1.31061], 
    [2001, -0.44101], [2002, -0.13044], [2003, -0.00621], [2004, -0.3789], [2005, 0.18013], [2006, -0.00621], 
    [2007, -0.13044], [2008, -0.62736], [2009, 0.0559], [2010, 0.55282], [2011, -0.3789], [2012, -0.00621], 
    [2013, 0.24225], [2014, 0.61493], [2015, 1.79511], [2016, 2.22991], [2017, 1.67088], [2018, 1.17396]
]

mediaTotal_chmsl = [
    [1995, -1.41698], [1996, -1.31958], [1997, -1.18397], [1998, -1.25509], [1999, -1.12116], [2000, -0.99162],
    [2001, -0.74863], [2002, -0.60692], [2003, -0.48835], [2004, -0.36281], [2005, -0.14739], [2006, -0.09749], 
    [2007, -0.09805], [2008, 0.05963], [2009, 0.25069], [2010, 0.30937], [2011, 0.27672], [2012, 0.73022], 
    [2013, 0.83476], [2014, 1.00612], [2015, 1.43071], [2016, 1.54773], [2017, 1.60787], [2018, 1.78469]
]

# Os anos e valores são extraídos das listas usando a função zip e a descompactação do operador *. 
# Isso cria quatro listas: anos_sst, valores_sst, anos_media, e valores_media.
anos_sst, valores_sst = zip(*sst)
anos_media, valores_media = zip(*mediaTotal_chmsl)

# Duas linhas são plotadas no gráfico usando os dados extraídos. A opção 'o-' e 's-' especifica o estilo da linha, 
# onde 'o' e 's' representam marcadores circulares e quadrados, respectivamente.
plt.plot(anos_sst, valores_sst, 'o-', label='SST')  # 'o-' adiciona marcadores circulares nos pontos
plt.plot(anos_media, valores_media, 's-', label='Média Total CHMSL')  # 's-' adiciona marcadores quadrados nos pontos

# Rótulos são adicionados aos eixos x e y, e um título é atribuído ao gráfico.
plt.xlabel('Ano')
plt.ylabel('Valor Padronizado')
plt.title('Plot das Variáveis Padronizadas')

# Rótulos são adicionados a cada ponto no gráfico, exibindo os valores correspondentes. 
# Os rótulos são posicionados acima dos pontos para a variável SST e abaixo para a Média Total CHMSL.
for i, txt in enumerate(valores_sst):
    plt.annotate(f'{txt:.2f}', (anos_sst[i], valores_sst[i]), textcoords="offset points", xytext=(0, 10), ha='center')

for i, txt in enumerate(valores_media):
    plt.annotate(f'{txt:.2f}', (anos_media[i], valores_media[i]), textcoords="offset points", xytext=(0, -12), ha='center')

plt.legend()  # Adiciona a legenda com base nos rótulos usados

# Exibe o gráfico na tela
plt.show()
