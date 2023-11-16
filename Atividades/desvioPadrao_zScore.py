import statistics
# biblioteca utilizada para calcular o desvio padrao

mediaTotal_chmsl = [
    -21.736, -19.472, -16.32, -17.973, -14.86, -11.849,
    -6.201, -2.907, -0.151, 2.767, 7.774, 8.934, 8.921,
    12.586, 17.027, 18.391, 17.632, 28.173, 30.603, 34.586,
    44.455, 47.175, 48.573, 52.683
]

# variavel que recebe o desvio padrao
desvio__padrao = statistics.stdev(mediaTotal_chmsl)


lista_chmsl_desvio_padrao = []
for entrada in mediaTotal_chmsl:
    ano_ch = entrada
    z_score = (ano_ch - 11.200) / desvio__padrao
    lista_chmsl_desvio_padrao.append(round(z_score, 5))

print(lista_chmsl_desvio_padrao)

sst = [
    0.47, 0.32, 0.52, 0.65, 0.44,
    0.43, 0.57, 0.62, 0.64, 0.58,
    0.67, 0.64, 0.62, 0.54, 0.65,
    0.73, 0.58, 0.64, 0.68, 0.74,
    0.93, 1, 0.91, 0.83
]

padrao_sst = statistics.stdev(sst)
lista_padrao_sst = []
print("------------------------------------------------------------------------------------------------------------------------")
for entrada in sst:
    ano_sst = entrada
    z_score_sst = (ano_sst - 0.641) / padrao_sst
    lista_padrao_sst.append(round(z_score_sst, 5))

print(lista_padrao_sst)


