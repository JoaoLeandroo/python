import pandas as pd
import statistics as sts
import scipy.stats as stats
from IPython.display import display, HTML

valores = [
    1462.121, 1462.165, 1462.071, 1462.095, 1462.097,
    1462.088, 1462.163, 1462.045, 1462.108, 1462.091,
    1462.052, 1462.056, 1462.145, 1462.085, 1462.088,
    1462.057, 1462.081, 1462.094, 1462.144, 1462.085,
    1462.115, 1462.113, 1462.071, 1462.078, 1462.126,
    1462.164, 1462.088, 1462.101, 1462.084, 1462.164,
    1462.128, 1462.121, 1462.087, 1462.121, 1462.096,
    1462.106, 1462.13, 1462.107, 1462.051, 1462.118,
    1462.096, 1462.122, 1462.034, 1462.117, 1462.021,
    1462.08, 1462.074, 1462.14, 1462.097, 1462.1
]

# desviopadrao = sts.stdev(valores)
confianca = 0.95

#  Intervalo de 1 a 2
intervalo_1_2 = valores[0:2]
intervalo_2 = pd.Series(intervalo_1_2)

media_2 = sts.mean(intervalo_2)
desvio_padrao_1_2 = sts.stdev(intervalo_2)
desvio_da_media_1_2 = desvio_padrao_1_2/(len(intervalo_2))**0.5 

variancia_2 = desvio_padrao_1_2**2
graus_liberdade_2 = len(intervalo_2) - 1
intervalo_confianca_2 = stats.t.interval(confianca, graus_liberdade_2, loc=media_2, scale=desvio_da_media_1_2)
intervalo_conf_inteiro_2 = stats.t.interval(confianca, graus_liberdade_2, loc=variancia_2, scale=desvio_da_media_1_2)

# intervalo de 1 a 3
intervalo_1_3 = valores[0:3]
intervalo_3 = pd.Series(intervalo_1_3)

media_3 = sts.mean(intervalo_3)
desvio_padrao_1_3 = sts.stdev(intervalo_3)
desvio_da_media_1_3 = desvio_padrao_1_3/(len(intervalo_3))**0.5 

variancia_3 = desvio_padrao_1_3**2
graus_liberdade_3 = len(intervalo_3) - 1
intervalo_confianca_3 = stats.t.interval(confianca, graus_liberdade_3, loc=media_3, scale=desvio_da_media_1_3)
intervalo_conf_inteiro_3 = stats.t.interval(confianca, graus_liberdade_3, loc=variancia_3, scale=desvio_da_media_1_3)

# Intervalo de 1 a 4
intervalo_1_4 = valores[0:4]
intervalo_4 = pd.Series(intervalo_1_4)

media_4 = sts.mean(intervalo_4)
desvio_padrao_1_4 = sts.stdev(intervalo_4)
desvio_da_media_1_4 = desvio_padrao_1_4/(len(intervalo_4))**0.5 

variancia_4 = desvio_padrao_1_4**2
graus_liberdade_4 = len(intervalo_4) - 1
intervalo_confianca_4 = stats.t.interval(confianca, graus_liberdade_4, loc=media_4, scale=desvio_da_media_1_4)
intervalo_conf_inteiro_4 = stats.t.interval(confianca, graus_liberdade_4, loc=variancia_4, scale=desvio_da_media_1_4)

# Intervalo de 1 a 5
intervalo_1_5 = valores[0:5]
intervalo_5 = pd.Series(intervalo_1_5)

media_5 = sts.mean(intervalo_5)
desvio_padrao_1_5 = sts.stdev(intervalo_5)
desvio_da_media_1_5 = desvio_padrao_1_5/(len(intervalo_5))**0.5 

variancia_5 = desvio_padrao_1_5**2
graus_liberdade_5 = len(intervalo_5) - 1
intervalo_confianca_5 = stats.t.interval(confianca, graus_liberdade_5, loc=media_5, scale=desvio_da_media_1_5)
intervalo_conf_inteiro_5 = stats.t.interval(confianca, graus_liberdade_5, loc=variancia_5, scale=desvio_da_media_1_5)

# Intervalo de 1 a 6
intervalo_1_6 = valores[0:6]
intervalo_6 = pd.Series(intervalo_1_6)

media_6 = sts.mean(intervalo_6)
desvio_padrao_1_6 = sts.stdev(intervalo_6)
desvio_da_media_1_6 = desvio_padrao_1_6/(len(intervalo_6))**0.5 

variancia_6 = desvio_padrao_1_6**2
graus_liberdade_6 = len(intervalo_6) - 1
intervalo_confianca_6 = stats.t.interval(confianca, graus_liberdade_6, loc=media_6, scale=desvio_da_media_1_6)
intervalo_conf_inteiro_6 = stats.t.interval(confianca, graus_liberdade_6, loc=variancia_6, scale=desvio_da_media_1_6)

# Intervalo de 1 a 7
intervalo_1_7 = valores[0:7]
intervalo_7 = pd.Series(intervalo_1_7)

media_7 = sts.mean(intervalo_7)
desvio_padrao_1_7 = sts.stdev(intervalo_7)
desvio_da_media_1_7 = desvio_padrao_1_7/(len(intervalo_7))**0.5 

variancia_7 = desvio_padrao_1_7**2
graus_liberdade_7 = len(intervalo_7) - 1
intervalo_confianca_7 = stats.t.interval(confianca, graus_liberdade_7, loc=media_7, scale=desvio_da_media_1_7)
intervalo_conf_inteiro_7 = stats.t.interval(confianca, graus_liberdade_7, loc=variancia_7, scale=desvio_da_media_1_7)

# Intervalo de 1 a 8
intervalo_1_8 = valores[0:8]
intervalo_8 = pd.Series(intervalo_1_8)

media_8 = sts.mean(intervalo_8)
desvio_padrao_1_8 = sts.stdev(intervalo_8)
desvio_da_media_1_8 = desvio_padrao_1_8/(len(intervalo_8))**0.5 

variancia_8 = desvio_padrao_1_8**2
graus_liberdade_8 = len(intervalo_8) - 1
intervalo_confianca_8 = stats.t.interval(confianca, graus_liberdade_8, loc=media_8, scale=desvio_da_media_1_8)
intervalo_conf_inteiro_8 = stats.t.interval(confianca, graus_liberdade_8, loc=variancia_8, scale=desvio_da_media_1_8)

# Intervalo de 1 a 10
intervalo_1_10 = valores[0:10]
intervalo_10 = pd.Series(intervalo_1_10)

media_10 = sts.mean(intervalo_10)
desvio_padrao_1_10 = sts.stdev(intervalo_10)
desvio_da_media_1_10 = desvio_padrao_1_10/(len(intervalo_10))**0.5 

variancia_10 = desvio_padrao_1_10**2
graus_liberdade_10 = len(intervalo_10) - 1
intervalo_confianca_10 = stats.t.interval(confianca, graus_liberdade_10, loc=media_10, scale=desvio_da_media_1_10)
intervalo_conf_inteiro_10 = stats.t.interval(confianca, graus_liberdade_10, loc=variancia_10, scale=desvio_da_media_1_10)

# Intervalo de 1 a 15
intervalo_1_15 = valores[0:15]
intervalo_15 = pd.Series(intervalo_1_15)

media_15 = sts.mean(intervalo_15)
desvio_padrao_1_15 = sts.stdev(intervalo_15)
desvio_da_media_1_15 = desvio_padrao_1_15/(len(intervalo_15))**0.5 

variancia_15 = desvio_padrao_1_15**2
graus_liberdade_15 = len(intervalo_15) - 1
intervalo_confianca_15 = stats.t.interval(confianca, graus_liberdade_15, loc=media_15, scale=desvio_da_media_1_15)
intervalo_conf_inteiro_15 = stats.t.interval(confianca, graus_liberdade_15, loc=variancia_15, scale=desvio_da_media_1_15)

# Intervalo de 1 a 20
intervalo_1_20 = valores[0:20]
intervalo_20 = pd.Series(intervalo_1_20)

media_20 = sts.mean(intervalo_20)
desvio_padrao_1_20 = sts.stdev(intervalo_20)
desvio_da_media_1_20 = desvio_padrao_1_20/(len(intervalo_20))**0.5 

variancia_20 = desvio_padrao_1_20**2
graus_liberdade_20 = len(intervalo_20) - 1
intervalo_confianca_20 = stats.t.interval(confianca, graus_liberdade_20, loc=media_20, scale=desvio_da_media_1_20)
intervalo_conf_inteiro_20 = stats.t.interval(confianca, graus_liberdade_20, loc=variancia_20, scale=desvio_da_media_1_20)

# Intervalo de 1 a 30
intervalo_1_30 = valores[0:30]
intervalo_30 = pd.Series(intervalo_1_30)

media_30 = sts.mean(intervalo_30)
desvio_padrao_1_30 = sts.stdev(intervalo_30)
desvio_da_media_1_30 = desvio_padrao_1_30/(len(intervalo_30))**0.5 

variancia_30 = desvio_padrao_1_30**2
graus_liberdade_30 = len(intervalo_30) - 1
intervalo_confianca_30 = stats.t.interval(confianca, graus_liberdade_30, loc=media_30, scale=desvio_da_media_1_30)
intervalo_conf_inteiro_30 = stats.t.interval(confianca, graus_liberdade_30, loc=variancia_30, scale=desvio_da_media_1_30)

# Intervalo de 1 a 40
intervalo_1_40 = valores[0:40]
intervalo_40 = pd.Series(intervalo_1_40)

media_40 = sts.mean(intervalo_40)
desvio_padrao_1_40 = sts.stdev(intervalo_40)
desvio_da_media_1_40 = desvio_padrao_1_40/(len(intervalo_40))**0.5 

variancia_40 = desvio_padrao_1_40**2
graus_liberdade_40 = len(intervalo_40) - 1
intervalo_confianca_40 = stats.t.interval(confianca, graus_liberdade_40, loc=media_40, scale=desvio_da_media_1_40)
intervalo_conf_inteiro_40 = stats.t.interval(confianca, graus_liberdade_40, loc=variancia_40, scale=desvio_da_media_1_40)

# Intervalo de 1 a 50
intervalo_1_50 = valores[0:50]
intervalo_50 = pd.Series(intervalo_1_50)

media_50 = sts.mean(intervalo_50)
desvio_padrao_1_50 = sts.stdev(intervalo_50)
desvio_da_media_1_50 = desvio_padrao_1_50/(len(intervalo_50))**0.5 

variancia_50 = desvio_padrao_1_50**2
graus_liberdade_50 = len(intervalo_50) - 1
intervalo_confianca_50 = stats.t.interval(confianca, graus_liberdade_50, loc=media_50, scale=desvio_da_media_1_50)
intervalo_conf_inteiro_50 = stats.t.interval(confianca, graus_liberdade_50, loc=variancia_50, scale=desvio_da_media_1_50)

# Calculos Totais

media_total = [
    media_2, media_3, media_4, media_5, media_6, 
    media_7, media_8, media_10, media_15, media_20, 
    media_30, media_40, media_50
]

desvio_total = [
    desvio_padrao_1_2, desvio_padrao_1_3, desvio_padrao_1_4, desvio_padrao_1_5, desvio_padrao_1_6,
    desvio_padrao_1_7, desvio_padrao_1_8, desvio_padrao_1_10, desvio_padrao_1_15, desvio_padrao_1_20,
    desvio_padrao_1_30, desvio_padrao_1_40, desvio_padrao_1_50
]

desvio_media_total = [
    desvio_da_media_1_2, desvio_da_media_1_3, desvio_da_media_1_4, desvio_da_media_1_5, desvio_da_media_1_6,
    desvio_da_media_1_7, desvio_da_media_1_8, desvio_da_media_1_10, desvio_da_media_1_15, desvio_da_media_1_20,
    desvio_da_media_1_30, desvio_da_media_1_40, desvio_da_media_1_50
]

intervalos_media_total = [
    intervalo_confianca_2[0], intervalo_confianca_3[0], intervalo_confianca_4[0], intervalo_confianca_5[0], intervalo_confianca_6[0],
    intervalo_confianca_7[0], intervalo_confianca_8[0], intervalo_confianca_10[0], intervalo_confianca_15[0], intervalo_confianca_20[0],
    intervalo_confianca_30[0], intervalo_confianca_40[0], intervalo_confianca_50[0]
]

intervalos_media_total_2 = [
    intervalo_confianca_2[1], intervalo_confianca_3[1], intervalo_confianca_4[1], intervalo_confianca_5[1],
    intervalo_confianca_6[1], intervalo_confianca_7[1], intervalo_confianca_8[1], intervalo_confianca_10[1],
    intervalo_confianca_15[1], intervalo_confianca_20[1], intervalo_confianca_30[1], intervalo_confianca_40[1],
    intervalo_confianca_50[1]
]

intervalos_conf_total = [
    intervalo_conf_inteiro_2[0], intervalo_conf_inteiro_3[0], intervalo_conf_inteiro_4[0], intervalo_conf_inteiro_5[0],
    intervalo_conf_inteiro_6[0], intervalo_conf_inteiro_7[0], intervalo_conf_inteiro_8[0], intervalo_conf_inteiro_10[0],
    intervalo_conf_inteiro_15[0], intervalo_conf_inteiro_20[0], intervalo_conf_inteiro_30[0], intervalo_conf_inteiro_40[0],
    intervalo_conf_inteiro_50[0]
]

intervalos_conf_total_2 = [
    intervalo_conf_inteiro_2[1], intervalo_conf_inteiro_3[1], intervalo_conf_inteiro_4[1], intervalo_conf_inteiro_5[1],
    intervalo_conf_inteiro_6[1], intervalo_conf_inteiro_7[1], intervalo_conf_inteiro_8[1], intervalo_conf_inteiro_10[1],
    intervalo_conf_inteiro_15[1], intervalo_conf_inteiro_20[1], intervalo_conf_inteiro_30[1], intervalo_conf_inteiro_40[1],
    intervalo_conf_inteiro_50[1]
]

rango_obs = ['1 - 2','1 - 3','1 - 4','1 - 5','1 - 6','1 - 7','1 - 8','1 - 10','1 - 15','1 - 20','1 - 30','1 - 40','1 - 50']

tabela_total = pd.DataFrame(list(zip(rango_obs, media_total, desvio_total, desvio_media_total, intervalos_media_total, intervalos_media_total_2, intervalos_conf_total, intervalos_conf_total_2)))

display(tabela_total)