
# A variável sst é uma lista de listas, onde cada sublista contém dois elementos: o primeiro elemento da lista é o ano e o segundo é um valor associado a esse ano.
sst = [
    [1995, 0.47], [1996, 0.32], [1997, 0.52], [1998, 0.65], [1999, 0.44],
    [2000, 0.43], [2001, 0.57], [2002, 0.62], [2003, 0.64], [2004, 0.58],
    [2005, 0.67], [2006, 0.64], [2007, 0.62], [2008, 0.54], [2009, 0.65],
    [2010, 0.73], [2011, 0.58], [2012, 0.64], [2013, 0.68], [2014, 0.74],
    [2015, 0.93], [2016, 1], [2017, 0.91], [2018, 0.83]
]
# aqui é calculada a media geral do sst de acordo com cada ano, dentro do loop for
soma_sst = 0
for i in sst:
    soma_sst += i[1]

media_sst = soma_sst / len(sst)
print(f'Media total sst: {round(media_sst, 4)}')



# Dados com os resultados das medias anuais de 1995 até 2018 de acordo com os dados da chmsl, gerados no exercicio 02
mediaTotal_chmsl = [
    [1995, -21.736], [1996, -19.472], [1997, -16.32], [1998, -17.973], [1999, -14.86], [2000,-11.849], 
    [2001, -6.201], [2002, -2.907], [2003, -0.151], [2004, 2.767], [2005, 7.774], [2006, 8.934], [2007, 8.921],
    [2008, 12.586], [2009, 17.027], [2010, 18.391], [2011, 17.632], [2012, 28.173], [2013, 30.603], [2014, 34.586],
    [2015, 44.455], [2016, 47.175], [2017, 48.573], [2018, 52.683]
]
# Loop de repetição para somar os dados de acordo com cada ano na lista mediaTotal_chmsl
media_chmsl = 0
for i in mediaTotal_chmsl:
    media_chmsl += i[1]

resultado_media_total_chmsl = media_chmsl / len(mediaTotal_chmsl)
print(f'Media total chmsl: {round(resultado_media_total_chmsl, 4)}')



# área para calcular a covariancia total
dados_covariancia_total = [
    [1995, 5.632], [1996, 9.846], [1997, 3.33], [1998, -0.263], [1999, 5.238], [2000, 4.863], [2001, 1.235], [2002, 0.296], [2003, 0.011],
    [2004, 0.514], [2005, 0.099], [2006, 0.002], [2007, 0.048], [2008, -0.140], [2009, 0.052], [2010, 0.640], [2011, -0.392], [2012, -0.017],
    [2013, 0.757], [2014, 2.315], [2015, 9.611], [2016, 12.915], [2017, 10.053], [2018, 7.84] 
]

soma_covariancia = 0
for i in dados_covariancia_total:
    soma_covariancia += i[1]

print(f'Total covariancia: {soma_covariancia}')
# o metodo len verifica quantos elementos existem dentro do array
# na variável abaixo esta pegando o resultando da covariacia e fazendo a divisão pela quantidade de elementos(24)
resp_covariancia = soma_covariancia / len(dados_covariancia_total)
# Resultado final
print(f'Resultado Final: {resp_covariancia - 1}')


